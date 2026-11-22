"""Find local businesses for free via OpenStreetMap (no API key, no paid lead lists)."""
import csv

import requests

UA = {"User-Agent": "AuditPilot/1.0 (local website audit tool)"}
NOMINATIM = "https://nominatim.openstreetmap.org/search"
OVERPASS = "https://overpass-api.de/api/interpreter"

# Friendly niche name -> OpenStreetMap tag. Anything else can be passed raw as key=value.
NICHES = {
    "dentist": "amenity=dentist",
    "chiropractor": "healthcare=chiropractor",
    "veterinarian": "amenity=veterinary",
    "physiotherapist": "healthcare=physiotherapist",
    "optician": "shop=optician",
    "lawyer": "office=lawyer",
    "accountant": "office=accountant",
    "real-estate": "office=estate_agent",
    "insurance": "office=insurance",
    "plumber": "craft=plumber",
    "electrician": "craft=electrician",
    "hvac": "craft=hvac",
    "roofer": "craft=roofer",
    "auto-repair": "shop=car_repair",
    "hair-salon": "shop=hairdresser",
    "beauty": "shop=beauty",
    "gym": "leisure=fitness_centre",
    "restaurant": "amenity=restaurant",
    "florist": "shop=florist",
    "funeral-home": "shop=funeral_directors",
}


def niche_tag(niche):
    tag = NICHES.get(niche, niche)
    if "=" not in tag:
        raise ValueError(f"Unknown niche '{niche}'. Use one of: {', '.join(sorted(NICHES))} "
                         "or a raw OpenStreetMap tag like craft=painter")
    return tag


def city_bbox(city):
    """(south, west, north, east) for a place name."""
    r = requests.get(NOMINATIM, params={"q": city, "format": "json", "limit": 1}, headers=UA, timeout=30)
    r.raise_for_status()
    hits = r.json()
    if not hits:
        raise ValueError(f"Could not find a place called '{city}'")
    s, n, w, e = (float(x) for x in hits[0]["boundingbox"])
    return s, w, n, e


def find_businesses(city, niche):
    """Yield dicts: name, website, email, phone."""
    key, value = niche_tag(niche).split("=", 1)
    s, w, n, e = city_bbox(city)
    query = f'[out:json][timeout:60];nwr["{key}"="{value}"]["name"]({s},{w},{n},{e});out tags;'
    r = requests.post(OVERPASS, data={"data": query}, headers=UA, timeout=90)
    r.raise_for_status()
    for el in r.json().get("elements", []):
        t = el.get("tags", {})
        site = t.get("website") or t.get("contact:website") or t.get("url") or ""
        if site and "://" not in site:
            site = "http://" + site
        yield {
            "name": t["name"],
            "website": site,
            "email": t.get("email") or t.get("contact:email") or "",
            "phone": t.get("phone") or t.get("contact:phone") or "",
        }


def read_csv(path):
    """Import your own list. Columns: name, website, email, phone (only name is required)."""
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}
            if not row.get("name"):
                continue
            site = row.get("website", "")
            if site and "://" not in site:
                site = "http://" + site
            yield {"name": row["name"], "website": site,
                   "email": row.get("email", ""), "phone": row.get("phone", "")}
