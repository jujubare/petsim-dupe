"""SQLite lead store. One row per business; the website (or name+city) is the identity."""
import json
import sqlite3
from datetime import datetime, timezone

SCHEMA = """
CREATE TABLE IF NOT EXISTS leads (
  id INTEGER PRIMARY KEY,
  key TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  website TEXT DEFAULT '',
  email TEXT DEFAULT '',
  phone TEXT DEFAULT '',
  city TEXT DEFAULT '',
  niche TEXT DEFAULT '',
  score INTEGER,
  issues TEXT DEFAULT '[]',
  report_path TEXT DEFAULT '',
  subject TEXT DEFAULT '',
  body TEXT DEFAULT '',
  status TEXT DEFAULT 'new',
  note TEXT DEFAULT '',
  created_at TEXT,
  sent_at TEXT
);
"""

# new -> audited -> drafted -> sent -> replied -> client
# side exits: nosite (phone-only lead), skipped (site too good / unreachable), optout
STATUSES = ("new", "nosite", "audited", "skipped", "drafted", "sent", "replied", "client", "optout")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def lead_key(name, website, city=""):
    if website:
        host = website.lower().split("://")[-1].split("/")[0]
        return host[4:] if host.startswith("www.") else host
    return f"{name.strip().lower()}|{city.strip().lower()}"


class Store:
    def __init__(self, path="auditpilot.db"):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)

    def add(self, name, website="", email="", phone="", city="", niche=""):
        """Insert a lead; returns True if it was new."""
        key = lead_key(name, website, city)
        if not key or key == "|":
            return False
        cur = self.db.execute(
            "INSERT OR IGNORE INTO leads (key,name,website,email,phone,city,niche,status,created_at)"
            " VALUES (?,?,?,?,?,?,?,?,?)",
            (key, name.strip(), website.strip(), email.strip().lower(), phone.strip(), city, niche,
             "new" if website else "nosite", now()),
        )
        self.db.commit()
        return cur.rowcount == 1

    def update(self, lead_id, **fields):
        if "issues" in fields and not isinstance(fields["issues"], str):
            fields["issues"] = json.dumps(fields["issues"])
        cols = ", ".join(f"{k}=?" for k in fields)
        self.db.execute(f"UPDATE leads SET {cols} WHERE id=?", (*fields.values(), lead_id))
        self.db.commit()

    def by_status(self, status, limit=None):
        q = "SELECT * FROM leads WHERE status=? ORDER BY id"
        if limit:
            q += f" LIMIT {int(limit)}"
        return self.db.execute(q, (status,)).fetchall()

    def find(self, needle):
        """Look a lead up by id, email, or website host."""
        if str(needle).isdigit():
            return self.db.execute("SELECT * FROM leads WHERE id=?", (int(needle),)).fetchone()
        n = str(needle).lower()
        return self.db.execute("SELECT * FROM leads WHERE email=? OR key=?", (n, n)).fetchone()

    def counts(self):
        rows = self.db.execute("SELECT status, COUNT(*) c FROM leads GROUP BY status").fetchall()
        return {r["status"]: r["c"] for r in rows}

    def sent_today(self):
        day = now()[:10]
        return self.db.execute(
            "SELECT COUNT(*) FROM leads WHERE sent_at LIKE ?", (day + "%",)
        ).fetchone()[0]
