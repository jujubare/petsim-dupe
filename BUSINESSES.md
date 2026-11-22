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

## 3. ClaimScout: recovering unclaimed money owed to businesses — SAVED, TO DO

**Status:** saved as a business to do; nothing built yet.
**Model:** contingency fee. You find money a business is owed, help them claim it, and keep a
percentage. No fee unless they get paid.

**Why it works:** US states hold tens of billions of dollars in unclaimed property: uncashed
vendor cheques, customer refunds, insurance payouts, utility deposits, old bank accounts. A lot
of it belongs to businesses that are still operating and have no idea, because the cheque went to
an old address or a closed department. Every state publishes a searchable list, and several offer
the whole list as a download. Nobody at a mid-sized company has the job of checking it.

**How it runs:** a script loads the state lists, keeps only business names with large amounts
(say $5,000 and up), matches them to companies that are still active, and finds a finance contact.
You email: "Your company is listed as owed money by the state of X. I handle the paperwork for
N%; you pay nothing unless you receive it." They sign a short agreement, you file the claim
with their documents, the state pays them, they pay you.

**Pricing:** typically 10% of what is recovered (many states cap finder fees around there).
**Path to $30k/month:** about $300,000 recovered per month, for example 15 claims averaging
$20,000. Large claims exist but how many you can win per month is untested.

**Daily effort:** low for finding and emailing (automated); moderate per signed claim (forms,
proof of ownership, follow-up with the state).

**Risks, stated plainly:**
- Owners can claim for free themselves, and you must say so. You are selling the finding and the
  paperwork, not access.
- Rules differ by state: fee caps, required contract wording, waiting periods before finders may
  contact owners, and in some states a licence. Each state needs checking before any outreach.
- Payout is slow: states often take 2-6 months to pay, so the first income arrives late.
- Many states hide exact amounts on the public list, which makes picking the big claims harder.

**Compared with the others:** biggest payout per deal and the easiest pitch (you are telling
someone they are owed money), but the slowest cash and the most rules to follow.

To start:
- [ ] Pick one state that publishes its full list with amounts and allows finders
- [ ] Read that state's finder rules: fee cap, contract wording, waiting period, licence
- [ ] Build the list loader, business matcher and contact finder
- [ ] Have a lawyer review the one-page finder agreement once (a few hundred dollars)
- [ ] Email the 50 largest matches; file the first signed claims
- [ ] Add a second state once the first claim pays out

## 4. ReplyDesk: Google review replies done for local businesses — IDEA, NOT BUILT

**Model:** monthly subscription. Every review a business gets on Google receives a thoughtful
reply within a day, written in the owner's voice. The owner does nothing.

**Why it works:** most local businesses never reply to their reviews, good or bad. Replies make
the listing look cared for, soften bad reviews for everyone who reads them later, and Google
says responding helps local visibility. Owners know they should and never get round to it.

**How it runs:** the owner grants manager access to their Google Business Profile once. A script
checks for new reviews each day, an AI model drafts a reply using the business's details and tone,
and it posts. Good reviews go out automatically; 1-2 star reviews are held for you (or the owner)
to approve with one click, because a wrong reply to an angry customer does real damage.

**Pricing:** $99/month per location; $149 with a weekly summary of what customers praise and
complain about.
**Path to $30k/month:** about 300 locations at $99, or 200 at $149. Multi-location owners
(dental groups, franchises, restaurant groups) bring 5-20 locations in one sale.

**Daily effort:** a few minutes approving the held replies. Selling is the work.

**How to sell it:** the same outreach engine as AuditPilot, with a different hook: "You have 14
reviews nobody answered, including this 2-star one from March. Here is the reply I would have
posted." Every AuditPilot client is also a ready buyer, so the two stack on one customer.

**Risks:**
- Posting replies automatically needs Google's approval for access to its Business Profile
  system; until that is granted, replies are drafted and you paste them in by hand.
- Other companies sell this, mostly bundled into bigger, pricier marketing packages.
- $99 is a small ticket, so it takes many customers; cancellations matter more than in the others.
- Replies must be honest and must never invent facts about a customer's visit.

**Compared with the others:** the smallest price but the least work per customer, and the only
one that sells naturally to customers you already have.

## 5. NightDesk: answering the calls local businesses miss — IDEA, NOT BUILT

**Model:** monthly subscription. When a plumber, roofer, dentist or locksmith misses a call
(on a job, after hours, at the weekend), the caller is answered anyway: first by an instant
text, and on the higher plan by an AI voice assistant that takes the details and books the job.

**Why it works:** for trades, a missed call is usually a lost job, because the caller rings the
next name on the list instead of leaving a voicemail. One recovered job (a few hundred to a few
thousand dollars) pays for the service many times over, which makes it an easy yes and a hard
thing to cancel.

**How it runs:** the business forwards unanswered calls to a number you provide. Plan one sends
the caller a text within seconds ("Sorry we missed you, this is Mike's Plumbing. What do you
need?") and passes the conversation to the owner. Plan two has a voice assistant answer, ask
what the problem is, where and how urgent, then text the owner a summary or put it in their
calendar. Both are assembled from existing phone and voice services, not built from nothing.

**Pricing:** $149/month for text-back; $349/month for the voice assistant.
**Path to $30k/month:** about 200 businesses on text-back, or 85 on the voice plan.

**Daily effort:** close to zero once a client is set up (about an hour each). Selling is the work.

**How to sell it:** with proof. Call the business after hours yourself; if nobody answers, the
email writes itself: "I rang at 6:40pm on Tuesday and got voicemail. Here is what your caller
would have received instead." Offer 14 days free and show them the jobs it caught.

**Risks:**
- The idea is known among marketing agencies, so it is not unique everywhere; it is still rare
  among small trades, and the after-hours proof call is the edge.
- Running costs: phone numbers, texts and voice minutes come out of the fee (roughly $10-60 per
  client per month depending on call volume; an estimate).
- Business texting in the US requires registering each sender with the phone carriers first,
  which takes days to weeks and some paperwork.
- A voice assistant that mishears an address or promises a price it should not is your problem;
  it must stick to taking details and never quote or diagnose.

**Compared with the others:** the highest monthly price per customer of the subscription ideas
and the clearest payback for the buyer, but with real running costs and setup per client.
