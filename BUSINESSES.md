# Business list

**Target: $500 a day, which is about $15,000 a month.** Every "path" line below is an estimate
from stated assumptions, not a tested result.

## 1. AuditPilot: website fixes for local businesses — SAVED, TO DO

**Status:** built and tested in this repo (`auditpilot/`), not yet run live.
**Model:** service. $499 flat fix + $149/month care plan.
**Daily effort:** run one command, press send, answer replies, do 1-3 hour fixes.
**Path to $15k/month:** about 5-8 months if reply and close rates hold (unproven).

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
**Path to $15k/month:** about 75-150 subscribers across two or three metro areas. One closed job pays
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
**Path to $15k/month:** about $150,000 recovered per month, for example 7-8 claims averaging
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
**Path to $15k/month:** about 150 locations at $99, or 100 at $149. Multi-location owners
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
**Path to $15k/month:** about 100 businesses on text-back, or 43 on the voice plan.

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

---

# Easy tech ideas (build once, mostly runs itself)

These five need no client work and no phone calls. They are quicker to build than the ones above
but depend more on finding an audience.

## 6. RestockRadar: instant restock and price-drop alerts for collectors — IDEA, NOT BUILT

**What it is:** a paid Discord or Telegram channel. A bot watches shops for things that sell out
in minutes (trading cards, retiring LEGO sets, graphics cards, limited sneakers, consoles) and
pings members the second something is back in stock or drops in price.
**Why people pay:** being two minutes early is the whole game for collectors and resellers.
**Pricing:** $15/month. **Path to $15k/month:** about 1,000 members.
**Build:** a script that checks product pages every minute and posts to a channel. A weekend.
**Effort after:** adding new products and shops; keeping the checkers working when shops change.
**Risks:** many such groups exist for sneakers, so pick a category that is underserved; some shops
forbid automated checking in their terms, so stick to those that allow it or offer feeds; members
leave quickly if alerts are slow or wrong.

## 7. StatementSwift: bank statement PDFs into spreadsheets — IDEA, NOT BUILT

**What it is:** a website where a bookkeeper or accountant drops in a PDF bank statement and
gets back a clean spreadsheet of every transaction, ready for their accounting software.
**Why people pay:** bookkeepers type these in by hand for clients who only have PDFs. It is
hours of dull work every month, and they bill by the hour.
**Pricing:** $29/month for 50 statements; $79/month unlimited.
**Path to $15k/month:** about 300 subscribers at an average of $50.
**Build:** PDF text extraction plus an AI model for the awkward layouts, a checkout page, and a
totals check so every converted statement balances. One to two weeks.
**Effort after:** fixing bank layouts that fail; answering support email.
**Risks:** a handful of small competitors already do this (which also proves people pay);
statements are sensitive, so files must be deleted after conversion and that promise kept; scanned
or photographed statements are much harder than digital ones.

## 8. DropCatch: buying expired web addresses and reselling them — IDEA, NOT BUILT

**What it is:** every day thousands of web addresses expire because the owner forgot to renew.
A script scans the daily lists for ones that are short, are real words, or still have other
sites linking to them, you register the best for about $10 each, and list them for sale.
**Why people pay:** a good name saves a new business from a clumsy one; an address with history
gets found on Google faster.
**Pricing:** typical sales run $200 to $2,000; most names never sell.
**Path to $15k/month:** hard to promise. Roughly 15-30 sales a month from a stock of several
hundred names, which means several thousand dollars tied up and a year of patience.
**Build:** a daily script that scores the expiring list. A few days.
**Effort after:** ten minutes a day picking names; replying to offers.
**Risks:** the only idea here that needs money up front and can lose it; never register names
containing brands or trademarks (that gets them taken away and can bring a legal claim); the
obvious good names are caught by professionals within seconds.

## 9. NicheBoard: an automated job board for one narrow field — IDEA, NOT BUILT

**What it is:** a job site for one specific kind of work (for example remote jobs in one
programming language, climate tech, or veterinary nurses) that fills itself: a script collects
openings from company career pages every day and a weekly email goes to subscribers.
**Why people pay:** employers pay to have their listing pinned at the top and included in the
email, because the audience is exactly the people they need.
**Pricing:** $199 per featured listing; $300-500 per newsletter sponsor slot.
**Path to $15k/month:** about 50 featured listings plus weekly sponsors, which needs roughly
10,000-20,000 email subscribers. That takes 6-12 months to grow.
**Build:** collectors for career pages, a simple site, an email list, a checkout. One to two weeks.
**Effort after:** an hour a week; mostly growing the audience.
**Risks:** no income until the audience exists; link out to the original posting and never copy
listings from other job boards; popular fields already have boards, so narrow is better.

## 10. BotPremium: a Discord bot with a paid tier — IDEA, NOT BUILT

**What it is:** a bot that server owners add for free, with extra features behind a monthly fee.
Best bets are bots tied to one game or hobby: stat tracking, tournament brackets, trading
price checks, event reminders, giveaways.
**Why people pay:** community owners pay small amounts readily for things that keep their
server lively, and Discord has built-in subscriptions so no payment system is needed.
**Pricing:** $5/month per server. **Path to $15k/month:** about 3,000 paying servers, which
usually means the bot is in 100,000 or more. Realistic for a hit, rare for most.
**Build:** a basic bot in a few days; the premium features over a few weeks.
**Effort after:** hosting, keeping up with game and Discord changes, support in your own server.
**Risks:** the longest odds on this list of reaching the target; a more likely outcome is a few
hundred to a couple of thousand dollars a month; a bot built around someone else's game depends
on that game staying popular and on its rules for third-party tools.

---

# Best odds, cheap, automated: the "public records" family

Each of these sells a daily or weekly email built from free government data to a kind of business
that already buys leads. They cost about $20-50 a month to run (a small server and an email
service), deliver themselves, and all five reuse the same engine as PermitPulse (#2): fetch a
public feed, filter, email subscribers, bill by card. Build the engine once and each extra
product is a few days of work, so you can launch several and keep whichever sells.

"Best odds" means better than the other ideas on this list, in my judgment, because the buyers
are proven and the product needs no audience. It does not mean certain. Getting the first 20
subscribers still takes outreach, though that can be a mostly automated free-trial email.

## 11. DistressList: neglected-property leads for real estate investors — IDEA, NOT BUILT

**What it is:** a weekly list of properties with fresh code violations (overgrown, boarded up,
unsafe structure) or overdue property taxes, with address and owner name from public records.
**Who pays:** house flippers and "we buy houses" investors, who already spend hundreds a month
on exactly these lists because such owners often want to sell.
**Pricing:** $149/month per county. **Path to $15k/month:** about 100 subscribers.
**Why the odds are good:** the most proven buyers on this whole list; they understand the
product instantly and one deal is worth tens of thousands to them.
**Risks:** established list sellers exist (compete on freshness and one-county focus); data
quality varies by city; a few places restrict commercial use of these records.

## 12. FreshFilings: newly registered businesses, delivered weekly — IDEA, NOT BUILT

**What it is:** a list of every new company registered in a state or county that week, with
name, address, type and owner where published.
**Who pays:** accountants, insurance agents, payroll and card-processing reps, sign makers,
commercial cleaners, web designers. A new business needs all of them within its first month.
**Pricing:** $79/month per area. **Path to $15k/month:** about 190 subscribers.
**Why the odds are good:** very wide range of buyers, so outreach rarely runs dry; also feeds
AuditPilot for free (new businesses need websites).
**Risks:** some states charge for bulk data or publish slowly; lists carry postal addresses
more often than emails, so buyers must be happy to mail or visit.

## 13. InspectAlert: failed health inspections for the companies that fix them — IDEA, NOT BUILT

**What it is:** a daily alert of restaurants and food businesses that were just cited, sorted
by problem: pests, grease and ventilation, refrigeration, plumbing, general cleanliness.
**Who pays:** pest control, hood and duct cleaners, refrigeration repair, commercial cleaners.
The restaurant has a deadline to fix it before re-inspection, so the timing is perfect.
**Pricing:** $99/month per trade per county. **Path to $15k/month:** about 150 subscribers.
**Why the odds are good:** almost nobody sells this, the buyer's need is urgent, and many
cities publish inspections as open data.
**Risks:** a smaller pool of buyers per city than the others, so it needs more cities; the
pitch to restaurants must stay helpful, never shaming.

## 14. BidBeacon: government contract alerts for small businesses — IDEA, NOT BUILT

**What it is:** a daily email of new federal, state and city contracts matching a subscriber's
trade and area: landscaping, janitorial, IT support, printing, construction, catering.
**Who pays:** small firms that want government work but cannot watch dozens of procurement
sites. The big alert services charge far more than a small firm will pay.
**Pricing:** $59/month. **Path to $15k/month:** about 255 subscribers.
**Why the odds are good:** federal opportunities come from one free official feed, so a
national product works from day one with no city-by-city setup.
**Risks:** the most competition in this family; state and city sites each need their own
collector; subscribers who never win a bid cancel.

## 15. PriceWatch: competitor price tracking for small online shops — IDEA, NOT BUILT

**What it is:** a shop owner lists competitor product pages; they get an email whenever a
competitor changes a price, runs a sale or goes out of stock. (Not public records, but the same
engine and the same cheap, automatic delivery.)
**Who pays:** small online stores, who currently check rivals by hand or not at all.
**Pricing:** $39/month for 100 products. **Path to $15k/month:** about 385 subscribers.
**Why the odds are good:** fully self-serve, so no selling conversations; existing tools are
priced for big retailers.
**Risks:** needs the most subscribers; finding shop owners costs effort or ad money; some
sites block automated checking, so coverage is never perfect.

**Ranked by odds of reaching $500/day (my judgment):** 11 DistressList, 2 PermitPulse,
13 InspectAlert, 12 FreshFilings, 14 BidBeacon, 15 PriceWatch.

**Shared caution for 2 and 11-14:** check each state's rules on using public records to contact
people before launching there, and sell only to businesses, not as a way to target individuals.

---

## Which to pick

| Want | Pick |
|---|---|
| Money soonest | 1 AuditPilot (already built), 5 NightDesk |
| Least ongoing work | 2 PermitPulse, 11-14 (same engine), 7 StatementSwift |
| Biggest single paydays | 3 ClaimScout |
| Most fun to build | 6 RestockRadar, 10 BotPremium |
| Cheapest to run | 2 and 11-15: about $20-50 a month |
| Best odds of actually reaching $500/day | 1 AuditPilot, 11 DistressList, 2 PermitPulse, 5 NightDesk (my judgment) |
