# Business list

## 1. AuditPilot: website fixes for local businesses — SAVED, TO DO

**Status:** built and tested in this repo (`auditpilot/`), not yet run live.
**Model:** service. $499 flat fix + $149/month care plan.
**Daily effort:** run one command, press send, answer replies, do 1-3 hour fixes.
**Path to $30k/month:** about 6-12 months if reply and close rates hold (unproven).

To start:
- [ ] Buy a domain and a mailbox on it (about $6/month)
- [ ] Copy `config.example.json` to `config.json` and fill it in
- [ ] First live run: `python -m auditpilot daily --city "<your city>" --niche dentist`
- [ ] Read the preview email, then `python -m auditpilot send --confirm`
- [ ] After 2 weeks, check `python -m auditpilot status` and adjust niche or price

See `README.md` for the full playbook.

## 2. PermitPulse: fresh building-permit leads for contractors — SAVED, TO DO

**Status:** saved as a business to do; nothing built yet.
**Model:** subscription product, no client work. Contractors pay monthly for a morning email of
new permits in their area and trade.

**Why it works:** when a homeowner pulls a permit for a new roof, a pool, solar, a remodel or a
new build, a dozen other trades want to reach them that week (roofers, HVAC, electricians,
landscapers, window and flooring companies, dumpster rental, lenders). Hundreds of US cities and
counties publish permits daily as free open data. The existing sellers of this data aim at large
companies with expensive national plans; a small roofer wants one county, one trade, in their
inbox, cheaply.

**How it runs:** a script pulls yesterday's permits from each city's open-data feed, sorts them by
trade and value, and emails each subscriber their slice with address, work description, value and
owner or contractor name. Stripe handles billing. Once a city is wired up it runs untouched.

**Pricing:** $99/month per trade per county; $249/month for all trades.
**Path to $30k/month:** about 150-300 subscribers across several metro areas. One closed job pays
a contractor's subscription for years, so cancellations should be low (assumption, untested).

**Daily effort once live:** near zero for delivery. The work is getting subscribers: a free 2-week
trial emailed to contractors, using their own city's real permits from that morning as the sample.

**Risks:** selling is still required at the start; some cities publish late or with thin detail;
some states restrict using permit records for solicitation, so each area needs a check first.

**Compared with AuditPilot:** slower to first dollar, but no fulfilment work and income is
recurring from day one. The two share the same outreach engine.

To start:
- [ ] Pick the first metro area and confirm it publishes daily permit data
- [ ] Check that state's rules on using permit records for solicitation
- [ ] Build the permit fetcher, trade sorter and morning email
- [ ] Set up Stripe subscriptions ($99 per trade, $249 all trades)
- [ ] Email local contractors a free 2-week trial using that morning's real permits
- [ ] Add a second metro once the first has 20 paying subscribers
