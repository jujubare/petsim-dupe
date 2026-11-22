"""End-to-end test against a local web server: no internet needed. Run: python -m unittest -v"""
import http.server
import json
import tempfile
import threading
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from auditpilot import cli, sender
from auditpilot.audit import audit_site
from auditpilot.store import Store

BAD = """<html><head><title>Home</title></head><body>
<img src="a.jpg"><img src="b.jpg"><p>Call 555-0100 or write hello@smilecare.test</p>
<p>&copy; 2017 Smile Care</p></body></html>"""

GOOD = f"""<html><head><title>Bright Dental | Family Dentist in Austin</title>
<meta name="viewport" content="width=device-width"><meta name="description" content="Family dentist.">
<meta property="og:title" content="Bright Dental">
<script type="application/ld+json">{{"@type":"Dentist","telephone":"555","address":"1 Main"}}</script>
</head><body><h1>Family dentist in Austin</h1><a href="tel:5550101">Call</a>
<img src="a.jpg" alt="Our office"><form></form><p>&copy; {date.today().year}</p></body></html>"""


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = (GOOD if self.path.startswith("/good") else BAD).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


class FakeSMTP:
    def __init__(self):
        self.sent = []

    def send_message(self, msg):
        self.sent.append(msg)

    def quit(self):
        pass


class PipelineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.cfg = json.loads(Path("config.example.json").read_text())
        self.cfg.update(your_name="Sam Tester", postal_address="1 Real Rd, Austin, TX 78701", daily_send_cap=1)
        (self.tmp / "config.json").write_text(json.dumps(self.cfg))
        self.argv = ["--config", str(self.tmp / "config.json"), "--db", str(self.tmp / "t.db"),
                     "--out", str(self.tmp / "out")]

    def run_cli(self, *a):
        return cli.main(self.argv + list(a))

    def test_bad_site_fails_the_right_checks(self):
        r = audit_site(self.base + "/bad")
        ids = {i["id"] for i in r["issues"]}
        self.assertTrue({"https", "mobile", "description", "h1", "click_to_call", "fresh", "image_alt"} <= ids)
        self.assertLess(r["score"], 50)
        self.assertEqual(r["email"], "hello@smilecare.test")

    def test_good_site_only_fails_https(self):
        r = audit_site(self.base + "/good")
        self.assertEqual([i["id"] for i in r["issues"]], ["https"])

    def test_unreachable_site(self):
        self.assertFalse(audit_site("http://127.0.0.1:1/", timeout=2)["ok"])

    def test_full_pipeline(self):
        found = [
            {"name": "Smile Care", "website": self.base + "/bad", "email": "", "phone": "555-0100"},
            {"name": "Bright Dental", "website": self.base.replace("127.0.0.1", "localhost") + "/good", "email": "", "phone": ""},
            {"name": "No Site Dental", "website": "", "email": "", "phone": "555-0102"},
        ]
        with mock.patch("auditpilot.discover.find_businesses", return_value=found):
            self.assertEqual(self.run_cli("daily", "--city", "Austin, Texas", "--niche", "dentist"), 0)
            self.run_cli("find", "--city", "Austin, Texas", "--niche", "dentist")  # dedupes

        store = Store(self.tmp / "t.db")
        self.assertEqual(store.counts(), {"drafted": 1, "skipped": 1, "nosite": 1})
        lead = store.by_status("drafted")[0]
        self.assertIn("Smile Care", lead["body"])
        self.assertIn("1 Real Rd", lead["body"])          # postal address present
        self.assertIn("won't contact you again", lead["body"])  # opt-out present
        self.assertNotIn("{", lead["body"])
        self.assertIn("Smile Care", Path(lead["report_path"]).read_text())
        self.assertIn("No Site Dental", (self.tmp / "out" / "call_list.csv").read_text())

        self.run_cli("send")  # dry run sends nothing
        self.assertEqual(store.sent_today(), 0)

        smtp = FakeSMTP()
        with mock.patch.object(sender, "connect", return_value=smtp):
            self.run_cli("send", "--confirm")
            self.run_cli("send", "--confirm")  # cap of 1/day already reached
        self.assertEqual(len(smtp.sent), 1)
        self.assertEqual(smtp.sent[0]["To"], "hello@smilecare.test")

        self.run_cli("mark", "hello@smilecare.test", "client")
        self.assertEqual(store.counts()["client"], 1)

    def test_placeholder_config_is_refused(self):
        (self.tmp / "config.json").write_text(Path("config.example.json").read_text())
        with self.assertRaises(SystemExit):
            self.run_cli("send")


if __name__ == "__main__":
    unittest.main()
