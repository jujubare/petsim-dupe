"""Command line: python -m auditpilot <command>. `daily` is the one you run every morning."""
import argparse
import csv
import json
import sys
from pathlib import Path

from . import discover, outreach, report, sender
from .audit import audit_site
from .store import STATUSES, Store, now

GOOD_ENOUGH = 85  # sites scoring at or above this aren't worth pitching


def load_config(path):
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"{path} not found. Copy config.example.json to config.json and fill it in.")
    cfg = json.loads(p.read_text(encoding="utf-8"))
    if cfg.get("your_name") == "Your Name" or "Your St" in cfg.get("postal_address", ""):
        raise SystemExit("config.json still has placeholder values. Fill in your real name, email "
                         "and postal address (a real address is legally required in commercial email).")
    return cfg


def cmd_find(store, args, cfg=None):
    added = 0
    for b in discover.find_businesses(args.city, args.niche):
        added += store.add(city=args.city, niche=args.niche, **b)
    print(f"Found {added} new businesses ({args.niche}, {args.city}).")


def cmd_import(store, args, cfg=None):
    added = sum(store.add(city=args.city or "", niche=args.niche or "", **b)
                for b in discover.read_csv(args.csv))
    print(f"Imported {added} new businesses from {args.csv}.")


def cmd_audit(store, args, cfg):
    leads = store.by_status("new", args.limit)
    pitched = 0
    for lead in leads:
        result = audit_site(lead["website"])
        if not result["ok"]:
            store.update(lead["id"], status="skipped", note=f"unreachable: {result['error']}")
            print(f"  skip  {lead['name']}: {result['error']}")
            continue
        email = lead["email"] or result["email"]
        if result["score"] >= GOOD_ENOUGH or not result["issues"]:
            store.update(lead["id"], status="skipped", score=result["score"], email=email, note="site is fine")
            print(f"  skip  {lead['name']}: scored {result['score']}, nothing to sell")
            continue
        path = report.write_report(lead, result, cfg, args.out + "/reports")
        subject, body = outreach.draft(lead, result, cfg)
        store.update(lead["id"], status="drafted" if email else "audited", score=result["score"],
                     issues=result["issues"], email=email, report_path=path, subject=subject, body=body)
        pitched += 1
        print(f"  {result['score']:>3}   {lead['name']}  {'-> ' + email if email else '(no email found: call list)'}")
    print(f"Audited {len(leads)} sites, {pitched} worth pitching.")


def cmd_export(store, args, cfg=None):
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    drafts = store.by_status("drafted")
    with open(out / "drafts.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "email", "score", "subject", "body", "report"])
        for d in drafts:
            w.writerow([d["id"], d["name"], d["email"], d["score"], d["subject"], d["body"], d["report_path"]])
    calls = store.by_status("audited") + store.by_status("nosite")
    with open(out / "call_list.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "phone", "website", "score", "why"])
        for c in calls:
            if c["phone"]:
                why = "has no website at all" if c["status"] == "nosite" else (c["subject"] or "weak website")
                w.writerow([c["id"], c["name"], c["phone"], c["website"], c["score"], why])
    print(f"Wrote {out}/drafts.csv ({len(drafts)} emails ready) and {out}/call_list.csv.")


def cmd_send(store, args, cfg):
    cap = cfg.get("daily_send_cap", 40)
    room = max(0, cap - store.sent_today())
    leads = store.by_status("drafted", min(room, args.limit or room) or None) if room else []
    if not leads:
        print(f"Nothing to send (drafted leads: {len(store.by_status('drafted'))}, "
              f"sent today: {store.sent_today()}/{cap}).")
        return
    if not args.confirm:
        print(f"DRY RUN: would send {len(leads)} emails. First one:\n")
        print(f"To: {leads[0]['email']}\nSubject: {leads[0]['subject']}\n\n{leads[0]['body']}\n")
        print("Read it. If it is accurate and you are happy to put your name on it, run again with --confirm.")
        return
    n = sender.send_batch(leads, cfg, lambda l: store.update(l["id"], status="sent", sent_at=now()))
    print(f"Sent {n} emails ({store.sent_today()}/{cap} today).")


def cmd_mark(store, args, cfg=None):
    lead = store.find(args.lead)
    if not lead:
        raise SystemExit(f"No lead matching '{args.lead}'.")
    store.update(lead["id"], status=args.status)
    print(f"{lead['name']} -> {args.status}")


def cmd_status(store, args, cfg=None):
    c = store.counts()
    for s in STATUSES:
        if c.get(s):
            print(f"  {s:<8} {c[s]}")
    sent = sum(c.get(s, 0) for s in ("sent", "replied", "client", "optout"))
    clients = c.get("client", 0)
    if sent:
        print(f"\n  reply rate  {100 * (c.get('replied', 0) + clients) / sent:.1f}%"
              f"   close rate  {100 * clients / sent:.1f}%  (of {sent} emailed)")
    try:
        cfg = load_config(args.config)
        print(f"  booked so far: ${clients * cfg['fix_price']:,} one-off"
              f" + ${clients * cfg['care_plan_price']:,}/month if every client takes the care plan")
    except SystemExit:
        pass


def cmd_daily(store, args, cfg):
    cmd_find(store, args)
    cmd_audit(store, args, cfg)
    cmd_export(store, args)
    args.confirm, args.limit = False, None
    cmd_send(store, args, cfg)


def main(argv=None):
    p = argparse.ArgumentParser(prog="auditpilot", description=__doc__)
    p.add_argument("--config", default="config.json")
    p.add_argument("--db", default="auditpilot.db")
    p.add_argument("--out", default="out")
    sub = p.add_subparsers(dest="cmd", required=True)

    def where(sp, required=True):
        sp.add_argument("--city", required=required, help='e.g. "Austin, Texas"')
        sp.add_argument("--niche", required=required, help="e.g. dentist, plumber, or a raw tag like craft=painter")

    sp = sub.add_parser("daily", help="find + audit + draft + preview. Run this every morning.")
    where(sp); sp.add_argument("--limit", type=int, default=60)
    sp = sub.add_parser("find", help="discover businesses from OpenStreetMap"); where(sp)
    sp = sub.add_parser("import", help="import your own CSV (name, website, email, phone)")
    sp.add_argument("csv"); where(sp, required=False)
    sp = sub.add_parser("audit", help="audit new leads and draft emails"); sp.add_argument("--limit", type=int)
    sub.add_parser("export", help="write drafts.csv and call_list.csv")
    sp = sub.add_parser("send", help="send drafted emails (dry run unless --confirm)")
    sp.add_argument("--confirm", action="store_true"); sp.add_argument("--limit", type=int)
    sp = sub.add_parser("mark", help="record an outcome: replied, client, optout ...")
    sp.add_argument("lead", help="lead id, email or domain"); sp.add_argument("status", choices=STATUSES)
    sub.add_parser("status", help="funnel numbers")
    sub.add_parser("niches", help="list built-in niches")

    args = p.parse_args(argv)
    if args.cmd == "niches":
        print("\n".join(sorted(discover.NICHES)))
        return 0
    needs_cfg = args.cmd in ("daily", "audit", "send")
    cfg = load_config(args.config) if needs_cfg else None
    store = Store(args.db)
    try:
        globals()[f"cmd_{args.cmd}"](store, args, cfg)
    except (ValueError, OSError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0
