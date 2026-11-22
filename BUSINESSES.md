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

## 11. DistressList: neglected-property leads for real estate investors — SAVED, TO DO

**Status:** saved as a business to do; nothing built yet.

**What it is:** a weekly list of properties with fresh code violations (overgrown, boarded up,
unsafe structure) or overdue property taxes, with address and owner name from public records.
**Who pays:** house flippers and "we buy houses" investors, who already spend hundreds a month
on exactly these lists because such owners often want to sell.
**Pricing:** $149/month per county. **Path to $15k/month:** about 100 subscribers.
**Why the odds are good:** the most proven buyers on this whole list; they understand the
product instantly and one deal is worth tens of thousands to them.
**Risks:** established list sellers exist (compete on freshness and one-county focus); data
quality varies by city; a few places restrict commercial use of these records.

To start:
- [ ] Pick the first county: one that publishes code violations and tax-delinquent lists online
- [ ] Check that state's rules on commercial use of those records
- [ ] Build the shared engine: fetch, filter, weekly email, card billing
- [ ] Build the buyer finder: local investors and "we buy houses" companies with public emails
- [ ] Send a free 2-week trial using that week's real list as the sample
- [ ] Add a second county once the first has 20 paying subscribers

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

# Gaming and creator ideas

More fun than the business-to-business ideas above, and startable with almost no money. The
trade-off is honest: most people doing these earn pocket money, a few earn a lot, and $500 a
day is the top end, not the typical result. If you are under 18, the payout accounts (Roblox
Developer Exchange, Stripe, PayPal, ad networks) need a parent or guardian to set up with you.
All of these stay inside the platforms' rules; exploits, dupes and botting get accounts banned
and earnings taken back, so none of that is here.

## 16. An original Roblox game — IDEA, NOT BUILT

**What it is:** your own game with its own name, look and mechanics. Money comes from game
passes, in-game purchases and premium playtime, and Roblox converts earned Robux to real money
through its Developer Exchange once you pass its minimum.
**Automated part:** the game earns while you sleep; I can write the scripts, shop, data saving
and daily-reward systems with you.
**Odds:** a small share of games earn real money, but a simple, polished game in a popular
style (simulator, tycoon, obby, tower defence) with weekly updates has a real chance at
hundreds to a few thousand dollars a month. Hits earn far more.
**Catch:** needs updates every week or players leave; in-game purchases must follow Roblox's
rules on paid random items.

## 17. Tools and scripts for other Roblox developers — IDEA, NOT BUILT

**What it is:** sell what developers need: ready-made systems (pets, inventory, trading, shops,
admin panels), Studio plugins, UI kits, and paid commissions for custom scripting.
**Why it is a better bet than a game:** developers pay up front, so you do not need a hit.
**Pricing:** $5-50 per asset; $50-500 per commission.
**Odds:** steady. A good scripter with a portfolio can reach $1,000-5,000 a month; $15k needs
a store of popular products or a small team.
**Catch:** commissions are real work, not automated; get paid part up front.

## 18. A value and stats site for a trading game — IDEA, NOT BUILT

**What it is:** a website with item values, a trade calculator ("is this trade fair?"), tier
lists and update news for one popular game with trading. Players check these constantly.
**Automated part:** values update from a simple admin page or community votes; pages build
themselves. Money comes from ads, so no selling at all.
**Odds:** the top sites for big games get millions of visits a month. Being early for a new,
rising game matters more than being best for an old one.
**Catch:** income follows the game's popularity; ad networks need an adult account holder; use
your own design and wording and never copy another site's value list.

## 19. Clipping for streamers and YouTubers — IDEA, NOT BUILT

**What it is:** turn long streams and videos into short clips for TikTok, Shorts and Reels.
Creators pay per clip or per view, and some run open clipping programs anyone can join.
**Automated part:** software finds the loud, funny or high-chat moments, cuts them vertical and
adds captions; you pick the best and post.
**Pricing:** $5-20 per clip, or a monthly deal of $200-800 per creator.
**Odds:** good for a few hundred to a couple of thousand a month quickly; 20-40 creators on
monthly deals reaches the target but that is a small agency, not a solo hobby.
**Catch:** only clip creators who have agreed to it; pay per view swings wildly.

## 20. Discord server setups — IDEA, NOT BUILT

**What it is:** build complete servers for creators, game communities and small brands:
channels, roles, verification, welcome flow, ticket system, moderation and custom bot commands.
**Automated part:** a template script builds a whole server in minutes, so each sale is mostly
adjusting names and colours.
**Pricing:** $50-300 per server; $20-50 a month to keep it maintained.
**Odds:** easy first sales through communities you are already in; the monthly maintenance
fees are what add up.
**Catch:** one-off sales need a constant stream of new buyers.

## 21. Small web games on game portals — IDEA, NOT BUILT

**What it is:** simple, original browser games (the kind played in a spare five minutes)
published on the big free-game portals, which share ad money with the developer.
**Automated part:** once published, a game earns with no further work; I can build these
with you quickly, so you can release several and see which catches on.
**Odds:** most games earn little; one that gets featured can earn hundreds to thousands a
month for a long time. Publishing many small games is the strategy.
**Catch:** portals review games and reject clones, so each needs its own idea and art.

**Ranked for a realistic start (my judgment):** 17 tools for developers (surest money), 19
clipping, 18 value site (if you catch a rising game), 16 original game (biggest upside), 20, 21.

---

# Clipping and creator tools

## 22. ClipForge: all-in-one clipping software plus your own account network — IDEA, NOT BUILT

**What it is:** one program that takes a long video or stream, finds the best moments, cuts
them vertical with captions, and queues them to post across about 10 accounts on YouTube
Shorts, TikTok and Instagram, each account with its own niche and its own clips.

**Three ways it earns, weakest to strongest:**
1. **Platform ad share.** The weakest. YouTube does not count views of non-original Shorts for
   revenue sharing and can remove monetisation from a whole channel for reused or
   template-looking content, even when the original creator gave permission.
2. **Paid clipping campaigns.** Creators and brands pay clippers per view through clipping
   marketplaces. Listed rates in late 2026 centre on about $1 per 1,000 views (range roughly
   $0.20 to $6), usually with a cap per campaign and payment only for verified views.
3. **Selling the software.** Other clippers pay monthly for the tool. This is the part that
   can become a real business, and your own accounts are the proof it works.

**The math for $500/day:**
- On campaigns alone: about 500,000 paid views a day at $1 per 1,000, so 50,000 a day from
  each of 10 accounts. Possible, but views come in spikes, not evenly, and caps bite.
- On software: about 400 subscribers at $39/month.
- Realistic mix: campaigns bring the first few hundred to few thousand dollars a month, and
  the software grows on top.

**What makes or breaks it:**
- **Only clip with permission:** campaign content, creators who have agreed, or your own
  footage. Clipping without it gets copyright strikes and accounts removed.
- **Ten different accounts, not one account ten times.** The same clip posted across accounts
  looks like spam and gets all of them limited. Each needs its own niche and clips.
- **Add something.** A hook line, captions, a reaction or context. Bare cuts get less reach
  and no ad share.
- **Post through the official routes.** YouTube and Instagram allow scheduled uploads through
  their developer programs; TikTok requires an app review first and until then uploads land as
  private drafts you publish by hand. Fake devices and view bots end in bans.
- **Pick the best clips yourself.** Software can find candidates; ten minutes a day of human
  choosing is the difference between views and none.

**Build:** moment finder (speech, loudness, chat spikes), vertical crop that follows the
speaker, captions, a posting queue per account, and a campaign tracker. Two to four weeks for
a solid first version. Running cost is mostly the computer time for video processing.

**Odds (my judgment):** good for a few hundred to a couple of thousand dollars a month within
the first months; $500 a day needs either a run of viral clips or the software side taking off.

## 23. Stream packs: overlays, alerts and emotes — IDEA, NOT BUILT

**What it is:** matching sets of stream graphics (overlays, alert animations, panels, emotes,
transitions) sold as downloads to small streamers. Build a generator that recolours and
renames a pack automatically, so each design becomes dozens of variants.
**Pricing:** $10-40 per pack; $50-150 for a custom one.
**Odds:** steady small sales; a store with 50+ packs can reach $1,000-3,000 a month.
**Catch:** crowded market, so a distinct style or a single game's theme helps; use only your
own art, never a game's official logos or characters.

## 24. Game server hosting for friend groups — IDEA, NOT BUILT

**What it is:** rent a large server, split it into many small private game servers (Minecraft
and other games that allow private servers), and rent those out monthly with one-click setup.
**Automated part:** free open-source control panels handle creation, billing, restarts and
backups without you touching anything.
**Pricing:** $5-15 per server a month. **Path to $15k/month:** about 1,500 servers; a
realistic small host has 50-300.
**Odds:** proven model with thin margins; customers stay for months once their world is there.
**Catch:** when a server is down at 2am, customers message you; needs a little money up front.

## 25. Thumbnail and title testing for small YouTubers — IDEA, NOT BUILT

**What it is:** a creator uploads a video idea; they get back five thumbnail designs and ten
titles, scored against what is currently working in their niche.
**Automated part:** all of it, apart from spot checks.
**Pricing:** $19/month. **Path to $15k/month:** about 800 subscribers.
**Odds:** small YouTubers want this badly but cancel fast, so it lives on steady new signups.
**Catch:** several tools exist; never use other people's faces or copy thumbnails.

---

## Which to pick

| Want | Pick |
|---|---|
| Money soonest | 1 AuditPilot (already built), 5 NightDesk |
| Least ongoing work | 2 PermitPulse, 11-14 (same engine), 7 StatementSwift |
| Biggest single paydays | 3 ClaimScout |
| Most fun to build | 16 original Roblox game, 18 value site, 21 web games, 6 RestockRadar |
| Cheapest to run | 2 and 11-15: about $20-50 a month |
| Best odds of actually reaching $500/day | 1 AuditPilot, 11 DistressList, 2 PermitPulse, 5 NightDesk (my judgment) |
