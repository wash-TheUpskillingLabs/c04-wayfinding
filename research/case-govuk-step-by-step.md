# Case: GOV.UK (Government Digital Service), a "step by step" map for journeys that cross departments

**Kind:** paradigmatic
**Bears on:** pre-cycle, cycle, post-cycle, interfaces
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
A page pattern on GOV.UK that lays out every stage of a real-world task (learning to drive, employing someone, what to do when someone dies) in order, marks where the person is, and links out to the guidance and transactions owned by different departments.

## 2. Where it came from
Built by the Government Digital Service (GDS) for GOV.UK. This file draws on the GDS blog post announcing it, the GOV.UK Design System page that now documents it, a GDS service designer's essay on what it did to cross-government work, the UK's self-submitted entry to the OECD digital government toolkit, and the LocalGov Drupal module that reuses it for English councils.

## 3. When
- Pattern built over roughly a year by a team of about 10; GDS announcement post 17 October 2018, updated February 2019 ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/); [OECD toolkit entry](https://t4.oecd.org/governance/digital-government/toolkit/goodpractices/united-kingdom-p10-step-by-step.pdf)).
- Design System guidance: current page, read 2026-11-05 ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- LocalGov Drupal module: release activity through September 2026 ([Drupal.org](https://www.drupal.org/project/localgov_step_by_step)).

## 4. What it says
**The problem as GDS framed it**
- Real-world tasks often require many steps in a set order across several departments; GOV.UK had been organised around the structure of government rather than around tasks ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- Content and forms sat with separate departments, so users had to work out the order themselves ([OECD toolkit entry](https://t4.oecd.org/governance/digital-government/toolkit/goodpractices/united-kingdom-p10-step-by-step.pdf)).
- Starting a business could involve up to 12 government organisations ([Ivey-Williams, The Service Gazette](https://medium.com/the-service-gazette/improving-government-services-step-by-step-29ebfcb47e92)).

**What they built and how**
- The pattern shows every step, highlights the current and next steps, and shows earlier steps the person may have skipped; it sits beside each step's own content ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- 8 rounds of research, including disabled users and people with low digital literacy, plus a review by the Digital Accessibility Centre ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- First journeys were picked for high traffic, variety (to test the pattern's limits), and departments' reports of high drop-out ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- The page cannot be self-published by a department: changes go through the central GOV.UK content team via a change request ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).

**What happened (numbers)**
- "Learn to drive a car" was used 1.24 million times in its first 6 months ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- 25 journeys published with 15+ departments in six months; 36 by February 2019 ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)); 24 live at the time of the OECD submission ([OECD toolkit entry](https://t4.oecd.org/governance/digital-government/toolkit/goodpractices/united-kingdom-p10-step-by-step.pdf)); 42 cited in the service-design essay ([Ivey-Williams](https://medium.com/the-service-gazette/improving-government-services-step-by-step-29ebfcb47e92)).
- A remote before/after study on three journeys found a significant rise in task completion and in users' confidence; no figures are given in the post ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- The OECD entry says the step-by-step pages scored higher than existing content in user feedback, without published numbers ([OECD toolkit entry](https://t4.oecd.org/governance/digital-government/toolkit/goodpractices/united-kingdom-p10-step-by-step.pdf)).
- About 519 sites report using the LocalGov Drupal port, which states its aim as implementing the GOV.UK journeys for councils (figure as displayed on [Drupal.org](https://www.drupal.org/project/localgov_step_by_step), read 2026-11-05).

**What the pattern did to the organisations**
- The essay argues the larger effect was organisational: it gave departments a shared artefact to scope a service from the user's side, and mapping workshops were sometimes the first time the teams owning different parts of one service had met ([Ivey-Williams](https://medium.com/the-service-gazette/improving-government-services-step-by-step-29ebfcb47e92)).
- Where a service was too complex to explain in a simple step list, some departments moved on to changing service design and policy ([Ivey-Williams](https://medium.com/the-service-gazette/improving-government-services-step-by-step-29ebfcb47e92)).
- GDS's own lesson: cross-government collaboration mattered as much as the navigation design ([GDS blog](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).

**Stated limits of use**
- Not for journeys whose services mostly live off GOV.UK, not for read-only guidance, not where there is no meaningful order, and not inside a transactional service ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).

## Failure modes seen
- **Back-and-forth between maps:** Users get frustrated moving between one step by step and another; the guidance allows linking forward to another map but not back ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- **Unread wayfinding chrome:** Users rarely use the step by step header, so its purpose may be unclear ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- **Map stops at the edge of the platform:** The pattern is ruled out when most of a journey happens off GOV.UK ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- **No end-to-end owner:** No single organisation owns a whole service, and a case-by-case consultancy model stalls when the service designers leave ([Ivey-Williams](https://medium.com/the-service-gazette/improving-government-services-step-by-step-29ebfcb47e92)).
- **Untested on mobile:** The effect of turning off in-page navigation was tested only on desktop ([GOV.UK Design System](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- Which of The Labs' thresholds are "ordered tasks with a start and end" (the pattern's stated use) and which are "a series of options" (its stated non-use)?
- GDS found the artefact's main effect was on the owners, not just the users. Who are the separate "departments" whose pieces a participant must stitch together between a branch workshop, a regional Cycle and a maintained project?
- The pattern was held centrally (no self-publishing). What happened to coherence when councils took a copy and ran it themselves?

## 6. Hearsay and limits
- All outcome evidence is self-reported by GDS or the UK government; the completion study's figures are not published in the sources read, and the OECD entry does not evaluate the claims.
- The counts of live journeys (24, 25, 36, 42) differ by source and date; we cannot tell which journeys were later retired.
- **Rival explanation:** Rises in completion and "useful" ratings may come from the content rewriting and department coordination done to build each map, not from the navigation component itself; the essay's own framing points this way.
- Could confirm: GOV.UK content and performance analysts at GDS; LocalGov Drupal councils on whether the pattern works without a central editor.

## Sources
- [Building a better GOV.UK, step by step](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/), Government Digital Service blog (Sam Dub, Gabrielle Acosta), 17 Oct 2018, updated Feb 2019. Launch account with usage and research figures.
- [Step by step navigation](https://design-system.service.gov.uk/patterns/step-by-step-navigation), GOV.UK Design System, current page read 2026-11-05. Official guidance, known issues and open research questions.
- [Improving government services, step by step](https://medium.com/the-service-gazette/improving-government-services-step-by-step-29ebfcb47e92), Kate Ivey-Williams, The Service Gazette (Medium), undated in extract. GDS service design lead on the organisational effects.
- [United Kingdom: GOV.UK step-by-step navigation](https://t4.oecd.org/governance/digital-government/toolkit/goodpractices/united-kingdom-p10-step-by-step.pdf), OECD Digital Government Toolkit, undated. UK government's self-submitted good-practice entry.
- [LocalGov Step-by-step](https://www.drupal.org/project/localgov_step_by_step), Drupal.org project page, read 2026-11-05. Council reuse of the pattern; reported install count.
