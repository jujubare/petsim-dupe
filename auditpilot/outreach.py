"""Draft a short, specific, honest first email from the audit findings."""

TEMPLATE = """Hi {name} team,

I was looking at {niche_phrase} in {city} and ran a quick check on {host}. It scored {score}/100, and {lead_in}:

{bullets}

These are all fixable. I do it for a flat ${fix_price}, and you pay nothing until you have seen the fixed version.

Want me to send over the full one-page report? Just reply "yes".

{your_name}
{business_name}
{contact}

{address}
Not interested? Reply "no thanks" and I won't contact you again."""


def draft(lead, result, cfg):
    top = result["issues"][:3]
    host = lead["website"].split("://")[-1].split("/")[0]
    bullets = "\n".join(f"- {i['headline']}. {i['impact']}" for i in top)
    lead_in = ("one thing stood out" if len(top) == 1 else
               f"{'two' if len(top) == 2 else 'three'} things stood out")
    niche = (lead["niche"] or "local business").split("=")[-1].replace("-", " ").replace("_", " ")
    contact = " | ".join(x for x in (cfg["reply_email"], cfg.get("phone", "")) if x)
    body = TEMPLATE.format(
        name=lead["name"], niche_phrase=f"{niche} websites", city=(lead["city"] or "your area").split(",")[0],
        host=host, score=result["score"], lead_in=lead_in, bullets=bullets,
        fix_price=cfg["fix_price"], your_name=cfg["your_name"], business_name=cfg["business_name"],
        contact=contact, address=cfg["postal_address"],
    )
    subject = f"{top[0]['headline'].replace(chr(34), '')} ({host})"
    return subject, body
