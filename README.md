# AuditPilot

A one-command-a-day business: find local businesses whose websites are losing them customers,
show them exactly what is wrong, and get paid to fix it.

Each morning AuditPilot:

1. **Finds** businesses in a city and niche from OpenStreetMap (free, no API key, no paid lead lists).
2. **Audits** each website on 12 things that cost real customers (not secure, not mobile-ready, slow,
   no tap-to-call, invisible to Google, looks abandoned ...).
3. **Writes** a one-page report per business and a short, specific email quoting their own top 3 problems.
4. **Queues** the emails for you to preview and send from your own mailbox, with a hard daily cap.
5. **Lists** businesses with no email (or no website at all) in a call list.

Your part: read the preview, press send, answer replies, do the fix (an AI coding assistant does
most of it), collect payment.

## Setup (10 minutes, once)

```bash
pip install -r requirements.txt
cp config.example.json config.json      # then fill in your name, email, postal address, prices
export AUDITPILOT_SMTP_PASSWORD='your-mailbox-app-password'
```

Use a mailbox on your own domain (about $6/month), not a free Gmail address: it looks credible and
protects your personal account.

## Every day

```bash
python -m auditpilot daily --city "Austin, Texas" --niche dentist   # find, audit, draft, preview
python -m auditpilot send --confirm                                  # send today's batch
python -m auditpilot status                                          # funnel + money booked
```

When things happen:

```bash
python -m auditpilot mark hello@smilecare.com replied
python -m auditpilot mark hello@smilecare.com client
python -m auditpilot mark hello@smilecare.com optout    # never contacted again
```

Other commands: `niches` (built-in list), `import leads.csv` (your own list), `export`
(rewrites `out/drafts.csv` and `out/call_list.csv`). Change city or niche whenever one runs dry.

## The money, honestly

Nothing here guarantees $500 a day, and nobody selling a method that does is telling the truth.
What this gives you is a path where the arithmetic works and the work is small. The target of
$500/day is about $15,000/month, which the table below reaches around months 6-12. Default pricing is a **$499 flat fix** plus a **$149/month care plan**.

| Stage | What it looks like | Monthly income |
|---|---|---|
| Month 1 | 40 emails/day, first 3-6 clients | $1,500 - $3,000 |
| Months 2-4 | Same volume, care plans stacking up, referrals starting | $4,000 - $9,000 |
| Months 6-12 | 2-3 mailboxes, call list worked, prices raised to $799 / $249 | $15,000 - $30,000 |

Those rows are projections from assumptions, not results: roughly a 3% reply rate (published 2026
cold-email benchmarks range from about 2% to 6%, higher when the email is specific to the recipient)
and one in four replies becoming a client. Your real numbers show up in `status` after the first
couple of weeks; believe those, not this table.

The recurring care plan is what makes it low effort over time: 100 care-plan clients at $149 is
$14,900/month before you send a single new email.

Levers, in order of effect: raise prices once you have three happy clients; phone the call list
(far higher hit rate than email); pick niches where one new customer is worth a lot (dentists,
lawyers, roofers, HVAC); ask every client for one referral.

## Doing the work

A typical fix is 1-3 hours: SSL, mobile layout, titles and descriptions, tap-to-call, structured
data, alt text, footer year. Ask the client for site access, paste the report's issue list into an
AI coding assistant, review what it changes, and re-run the audit to show the new score. Take
payment by invoice (Stripe or PayPal) after they have seen the fixed version.

## Rules the tool enforces (keep them)

- Every email carries your real name, a real postal address and a one-reply opt-out; these are
  legal requirements for commercial email in the US (CAN-SPAM). The tool refuses to run on
  placeholder values.
- `optout` is permanent, and a business is never emailed twice.
- Sending is a dry run unless you pass `--confirm`, and stops at `daily_send_cap`. Keep the cap at
  or below 40 per mailbox or you will land in spam.
- Emails only state things the audit actually measured. Do not edit them into scare tactics.
- Outside the US, check local rules before emailing (for example GDPR/PECR in the EU and UK,
  CASL in Canada); use the call list there instead.
- Income is taxable; keep the invoices.

## Tests

```bash
python -m unittest -v     # runs the whole pipeline against a local test server, no internet needed
```
