"""Audit one website. Every check maps to money the owner is losing, in plain English."""
import json
import re
import time
from datetime import date
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

UA = {"User-Agent": "Mozilla/5.0 (compatible; AuditPilot/1.0; website audit)"}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
JUNK_EMAIL = ("example.", "sentry", "wixpress", "domain.com", "email.com", "yoursite", "godaddy",
              ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", "noreply", "no-reply")
SLOW_SECONDS = 3.0

# id: (weight, headline when failing, what it costs them, how you fix it)
CHECKS = {
    "https": (15, "Browsers mark your site \"Not Secure\"",
              "Visitors see a security warning before they see your business, and Google ranks secure sites higher.",
              "Install an SSL certificate and redirect all traffic to https."),
    "speed": (15, "Your homepage is slow to respond",
              "Most mobile visitors give up on a page that takes more than about 3 seconds.",
              "Enable caching and compression, and trim heavy scripts and images."),
    "mobile": (15, "Your site is not set up for phones",
               "Most local searches happen on a phone; a desktop-only layout forces pinching and zooming.",
               "Add a responsive viewport and mobile layout."),
    "title": (8, "Your page title is missing or poorly sized for Google",
              "The title is the blue headline people see in search results; a weak one gets fewer clicks.",
              "Write a 30-60 character title with your service and city."),
    "description": (8, "No search-result description",
                    "Google invents its own snippet for your listing, which is usually less convincing.",
                    "Add a meta description that says what you do, where, and why to call."),
    "h1": (5, "No clear main headline on the page",
           "Search engines and visitors both use the main headline to understand what you offer.",
           "Add a single H1 headline naming your service and area."),
    "click_to_call": (8, "Phone number is not tap-to-call",
                      "Phone visitors have to memorise and retype your number instead of tapping it.",
                      "Make every phone number a tap-to-call link."),
    "contact_path": (7, "No contact form or online booking found",
                     "After-hours visitors have no way to reach you, so they move on to a competitor.",
                     "Add a short contact form or a booking link above the fold."),
    "local_schema": (6, "No business details for Google to read",
                     "Structured data helps Google show your hours, address and reviews in search and maps.",
                     "Add LocalBusiness structured data (name, address, phone, hours)."),
    "image_alt": (5, "Images are missing descriptions",
                  "Screen-reader users can't tell what your images show, and Google image search skips them.",
                  "Add descriptive alt text to every meaningful image."),
    "fresh": (5, "The site looks out of date",
              "An old copyright year makes visitors wonder whether the business is still open.",
              "Update the footer year (and make it update itself)."),
    "social_preview": (3, "Links to your site look blank when shared",
                       "Shared links on Facebook, iMessage and WhatsApp show no image or summary.",
                       "Add Open Graph title, description and image tags."),
}


def _fetch(url, timeout):
    start = time.monotonic()
    r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
    return r, time.monotonic() - start


def _emails(soup, text):
    found = []
    for a in soup.select('a[href^="mailto:"]'):
        found.append(a["href"][7:].split("?")[0])
    found += EMAIL_RE.findall(text)
    out = []
    for e in found:
        e = e.strip().strip(".").lower()
        if EMAIL_RE.fullmatch(e) and not any(j in e for j in JUNK_EMAIL) and e not in out:
            out.append(e)
    return out


def _has_local_schema(soup):
    for tag in soup.find_all("script", type="application/ld+json"):
        try:
            blob = json.dumps(json.loads(tag.string or ""))
        except (ValueError, TypeError):
            continue
        if '"address"' in blob or '"telephone"' in blob or "LocalBusiness" in blob:
            return True
    return bool(soup.find(attrs={"itemtype": re.compile("schema.org/.*(Business|Organization|Dentist)", re.I)}))


def _contact_page(soup, base):
    for a in soup.find_all("a", href=True):
        label = (a.get_text(" ") + " " + a["href"]).lower()
        if "contact" in label and not a["href"].startswith(("mailto:", "tel:", "#")):
            url = urljoin(base, a["href"])
            if urlparse(url).netloc == urlparse(base).netloc:
                return url
    return None


def audit_site(url, timeout=15):
    """Return {ok, score, issues:[{id,headline,impact,fix}], email, final_url, seconds} or {ok: False, error}."""
    try:
        r, seconds = _fetch(url, timeout)
    except requests.RequestException as e:
        return {"ok": False, "error": type(e).__name__}
    if r.status_code >= 400 or "html" not in r.headers.get("content-type", "html").lower():
        return {"ok": False, "error": f"HTTP {r.status_code}"}

    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.get_text(" ")
    title = (soup.title.string or "").strip() if soup.title else ""
    desc = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
    images = soup.find_all("img")
    with_alt = [i for i in images if (i.get("alt") or "").strip()]
    years = [int(y) for y in re.findall(r"(?:©|&copy;|copyright)\D{0,20}(?:\d{4}\s*[-–]\s*)?(20\d{2})", r.text, re.I)]
    booking = re.search(r"book(ing)?\b|schedule|appointment|calendly|acuity|squareup", r.text, re.I)

    emails = _emails(soup, text)
    contact_url = _contact_page(soup, r.url)
    has_form = bool(soup.find("form"))
    if contact_url and (not emails or not has_form):
        try:
            c, _ = _fetch(contact_url, timeout)
            csoup = BeautifulSoup(c.text, "html.parser")
            emails = emails or _emails(csoup, csoup.get_text(" "))
            has_form = has_form or bool(csoup.find("form"))
        except requests.RequestException:
            pass

    passed = {
        "https": r.url.startswith("https://"),
        "speed": seconds <= SLOW_SECONDS,
        "mobile": bool(soup.find("meta", attrs={"name": re.compile("^viewport$", re.I)})),
        "title": 15 <= len(title) <= 70,
        "description": bool(desc and (desc.get("content") or "").strip()),
        "h1": bool(soup.find("h1")),
        "click_to_call": bool(soup.select('a[href^="tel:"]')),
        "contact_path": has_form or bool(booking),
        "local_schema": _has_local_schema(soup),
        "image_alt": not images or len(with_alt) / len(images) >= 0.7,
        "fresh": not years or max(years) >= date.today().year - 1,
        "social_preview": bool(soup.find("meta", attrs={"property": "og:title"})),
    }
    total = sum(w for w, *_ in CHECKS.values())
    earned = sum(CHECKS[k][0] for k, ok in passed.items() if ok)
    issues = [
        {"id": k, "weight": CHECKS[k][0], "headline": CHECKS[k][1], "impact": CHECKS[k][2], "fix": CHECKS[k][3]}
        for k, ok in passed.items() if not ok
    ]
    issues.sort(key=lambda i: -i["weight"])
    if not passed["speed"]:
        next(i for i in issues if i["id"] == "speed")["headline"] = (
            f"Your homepage took {seconds:.1f} seconds to respond")
    return {"ok": True, "score": round(100 * earned / total), "issues": issues,
            "email": emails[0] if emails else "", "final_url": r.url, "seconds": round(seconds, 2)}
