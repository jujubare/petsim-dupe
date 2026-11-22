"""Render a one-page, self-contained HTML audit the owner can read in a minute (prints cleanly to PDF)."""
import re
from datetime import date
from html import escape
from pathlib import Path

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Website audit - {name}</title>
<style>
  :root {{ --ink:#16202b; --muted:#5b6876; --line:#e3e8ee; --bg:#f6f8fa; --accent:{color}; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
         font:16px/1.55 -apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }}
  main {{ max-width:760px; margin:0 auto; padding:32px 16px 56px; }}
  header {{ display:flex; gap:24px; align-items:center; flex-wrap:wrap; background:#fff;
           border:1px solid var(--line); border-radius:14px; padding:24px; }}
  .ring {{ width:112px; height:112px; border-radius:50%; flex:none; display:grid; place-items:center;
          background:conic-gradient(var(--accent) {score}%, var(--line) 0); }}
  .ring div {{ width:86px; height:86px; border-radius:50%; background:#fff; display:grid;
              place-items:center; font-size:30px; font-weight:700; }}
  h1 {{ margin:0 0 4px; font-size:24px; line-height:1.25; }}
  h2 {{ font-size:18px; margin:32px 0 12px; }}
  .muted {{ color:var(--muted); font-size:14px; }}
  .issue {{ background:#fff; border:1px solid var(--line); border-left:4px solid var(--accent);
           border-radius:10px; padding:16px 18px; margin:10px 0; }}
  .issue h3 {{ margin:0 0 6px; font-size:16px; }}
  .issue p {{ margin:4px 0; }}
  .fix {{ color:var(--muted); font-size:14px; }}
  .cta {{ background:var(--ink); color:#fff; border-radius:14px; padding:24px; margin-top:32px; }}
  .cta h2 {{ margin-top:0; }} .cta a {{ color:#fff; }}
  @media print {{ body {{ background:#fff; }} .issue, header {{ break-inside:avoid; }} }}
</style></head><body><main>
<header>
  <div class="ring"><div>{score}</div></div>
  <div>
    <h1>Website audit: {name}</h1>
    <div class="muted">{url} &middot; checked {today}</div>
    <p style="margin:8px 0 0">{verdict}</p>
  </div>
</header>
<h2>{count} things costing you customers</h2>
{issues}
<section class="cta">
  <h2>I can fix all of this for a flat ${fix_price}</h2>
  <p>No contract and nothing to pay until you have seen the fixed version. Optional ${care_price}/month
  care plan keeps the site fast, secure and updated afterwards.</p>
  <p><strong>{your_name}</strong>, {business_name}<br>
  <a href="mailto:{reply_email}">{reply_email}</a>{phone}</p>
</section>
<p class="muted" style="margin-top:20px">This audit was produced from the public homepage only. Nothing on
your site was changed or accessed beyond what any visitor sees.</p>
</main></body></html>"""


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "site"


def verdict(score):
    if score < 50:
        return "Serious problems. The site is likely turning away more visitors than it converts."
    if score < 75:
        return "Working, but several fixable gaps are sending customers to competitors."
    return "Solid foundation with a few easy wins left on the table."


def write_report(lead, result, cfg, out_dir="out/reports"):
    score = result["score"]
    color = "#c62828" if score < 50 else "#b26a00" if score < 75 else "#2e7d32"
    issues = "\n".join(
        f'<div class="issue"><h3>{n}. {escape(i["headline"])}</h3><p>{escape(i["impact"])}</p>'
        f'<p class="fix">Fix: {escape(i["fix"])}</p></div>'
        for n, i in enumerate(result["issues"], 1)
    )
    html = PAGE.format(
        name=escape(lead["name"]), url=escape(result["final_url"]), today=date.today().strftime("%B %d, %Y"),
        score=score, color=color, verdict=verdict(score), count=len(result["issues"]), issues=issues,
        fix_price=cfg["fix_price"], care_price=cfg["care_plan_price"],
        your_name=escape(cfg["your_name"]), business_name=escape(cfg["business_name"]),
        reply_email=escape(cfg["reply_email"]),
        phone=f' &middot; {escape(cfg["phone"])}' if cfg.get("phone") else "",
    )
    path = Path(out_dir) / f"{slug(lead['name'])}.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return str(path)
