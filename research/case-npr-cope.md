# Case: NPR, "Create Once, Publish Everywhere" (COPE), separating content from every screen it appears on

**Kind:** paradigmatic
**Bears on:** interfaces, facilitators
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
An architecture and editorial rule at US public broadcaster NPR: all content goes into one content management system stored without display formatting, and every outlet (website, mobile apps, member-station sites, podcasts, widgets, partners) pulls from the same API. It is the usual reference point for what later became "headless CMS".

## 2. Where it came from
NPR's then Director of Application Development, Daniel Jacobson, described it in a 2009 guest post on ProgrammableWeb (archived). NPR's "Inside NPR" blog published API usage figures in 2010. A 2013 Information Today Europe article shows the idea spreading to libraries and archives. NPR's current developer documentation for its Content Distribution Service (CDS) shows how access works today.

## 3. When
- COPE post: 13 Oct 2009 ([ProgrammableWeb, archived](https://webarchive.library.unt.edu/web/20130214221052mp_/http://blog.programmableweb.com/2009/10/13/cope-create-once-publish-everywhere)).
- Usage report: covering October 2009 to March 2010 ([Inside NPR, 2010](https://www.npr.org/sections/inside/2010/04/12/125882632/api-usage-and-metrics)).
- Spread to cultural-heritage sector: Nov 2013 ([Information Today Europe](https://www.infotoday.eu/Articles/Editorial/Featured-Articles/Are-you-COPEing--93562.aspx)).
- CDS documentation: current, read 2026-11-05 ([NPR CDS FAQ](https://npr.github.io/content-distribution-service/faq)).

## 4. What it says
**What was tried**
- Four rules: build a content management system, not a web publishing tool; separate content from display; keep content modular; keep it portable ([ProgrammableWeb, 2009](https://webarchive.library.unt.edu/web/20130214221052mp_/http://blog.programmableweb.com/2009/10/13/cope-create-once-publish-everywhere)).
- Content is stored without presentation markup; each outlet's templates decide how it looks. Outlets named: web, mobile apps, TV and radio displays, RSS, podcasts, APIs; the post claims outlets not yet invented could be served the same way ([ProgrammableWeb, 2009](https://webarchive.library.unt.edu/web/20130214221052mp_/http://blog.programmableweb.com/2009/10/13/cope-create-once-publish-everywhere)).
- The public API took about two developer-months to build, most of it on user and rights management ([ProgrammableWeb, 2009](https://webarchive.library.unt.edu/web/20130214221052mp_/http://blog.programmableweb.com/2009/10/13/cope-create-once-publish-everywhere)).

**What happened**
- API requests rose from about 3.5 million to about 53 million in the period after NPR's July 2009 launches; over 1.1 billion stories were delivered in March 2010 alone ([Inside NPR, 2010](https://www.npr.org/sections/inside/2010/04/12/125882632/api-usage-and-metrics)).
- NPR's own products were by far the largest consumer (new NPR.org, the iPhone app, the mobile site), followed by member stations (four named) and third-party widgets; no exact public share was given ([Inside NPR, 2010](https://www.npr.org/sections/inside/2010/04/12/125882632/api-usage-and-metrics)).
- NPR's internal XML format went from about 55% to about 86% of requests, while Atom stayed near zero ([Inside NPR, 2010](https://www.npr.org/sections/inside/2010/04/12/125882632/api-usage-and-metrics)).
- By 2013 the model was being pitched to libraries, museums and archives; one speaker argued the real question is what users should be able to do, not which APIs to expose, and criticised hackathons that hand developers data without users ([Information Today Europe](https://www.infotoday.eu/Articles/Editorial/Featured-Articles/Are-you-COPEing--93562.aspx)).
- Today's documentation describes the Content Distribution Service running in parallel with the older Story API, with keys issued through NPR Member Partnership (member stations named) and no public sign-up process described ([NPR CDS FAQ](https://npr.github.io/content-distribution-service/faq); [CDS getting started](https://npr.github.io/content-distribution-service/getting-started)).

## Failure modes seen
- **Open API mostly feeds the owner:** In the first measured period, NPR's own apps and site were the API's dominant users ([Inside NPR, 2010](https://www.npr.org/sections/inside/2010/04/12/125882632/api-usage-and-metrics)).
- **Rights are the real cost:** Most of the API build time went to user and rights management, not content delivery ([ProgrammableWeb, 2009](https://webarchive.library.unt.edu/web/20130214221052mp_/http://blog.programmableweb.com/2009/10/13/cope-create-once-publish-everywhere)).
- **Data without users:** Adopters elsewhere ran hackathons whose apps did not last, per a 2013 critique ([Information Today Europe](https://www.infotoday.eu/Articles/Editorial/Featured-Articles/Are-you-COPEing--93562.aspx)).
- **Openness narrows over time:** Current access runs through a partner key process; when public access changed is not documented in sources we could open ([NPR CDS FAQ](https://npr.github.io/content-distribution-service/faq)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- COPE worked for *published stories*. Is a person's position in The Labs (where they are, what's next) the same kind of thing as a story, or is it a conversation that changes as it is read?
- NPR's channels were all owned or licensed by NPR. Which Labs "heads" (Slack, email, SMS, calendar, AI agents) are run by the branch, the region, the hub, or a third-party vendor?
- Most of the build cost went to rights. What are the equivalent permissions questions when a facilitator, an organizer and a participant see the same record?

## 6. Hearsay and limits
- Usage numbers come from NPR's own server logs, which the post says are approximate.
- We could not find a dated, official source for when NPR stopped issuing public API keys, so that is left out; the Wikipedia list of news APIs marks NPR's developer centres "no longer available" without dates (not cited as evidence).
- We have no measure of editorial cost (staff time) of writing display-agnostic content.
- **Rival explanation:** NPR's 2009–2010 growth may reflect the iPhone app boom and the July 2009 site relaunch, which would have driven requests under any architecture; COPE made it cheaper, not necessarily larger.
- Could confirm: NPR Digital Media / Member Partnership; member-station digital teams that consume CDS.

## Sources
- [COPE: Create Once, Publish Everywhere](https://webarchive.library.unt.edu/web/20130214221052mp_/http://blog.programmableweb.com/2009/10/13/cope-create-once-publish-everywhere), Daniel Jacobson, ProgrammableWeb (UNT web archive), 13 Oct 2009. Original statement.
- [API Usage and Metrics](https://www.npr.org/sections/inside/2010/04/12/125882632/api-usage-and-metrics), Inside NPR blog, April 2010. First published usage figures.
- [Are you COPEing?](https://www.infotoday.eu/Articles/Editorial/Featured-Articles/Are-you-COPEing--93562.aspx), Katherine Allen, Information Today Europe, 29 Nov 2013. Uptake and critique in libraries and archives.
- [Content Distribution Service FAQ](https://npr.github.io/content-distribution-service/faq) and [Getting started](https://npr.github.io/content-distribution-service/getting-started), NPR on GitHub Pages, read 2026-11-05. Current access model.
