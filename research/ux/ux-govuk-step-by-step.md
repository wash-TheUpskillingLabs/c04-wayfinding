# UX case: GOV.UK, step-by-step navigation and transaction start pages
**Kind:** wayfinding
**Recognition:** Documented as an OECD digital-government good practice (toolkit case "United Kingdom P10 – Step by step"); published as a pattern in the GOV.UK Design System with its research history; written up by its makers on the GDS blog. Sources below.
**Logged:** 2026-11-06

## What it is and who made it
A navigation pattern on GOV.UK, built by the Government Digital Service (GDS), that lays out every step of a real-life task that crosses departments (learn to drive, employ someone, what to do when someone dies), marks where the user is, and links each step to the guidance or transaction that completes it. It exists in two forms: a sidebar on each page that belongs to the journey, and a standalone page listing the whole journey ([GOV.UK Design System, step by step navigation](https://design-system.service.gov.uk/patterns/step-by-step-navigation)). The makers' account is a GDS blog post of 17 October 2018 by Sam Dub and Gabrielle Acosta ([Building a better GOV.UK, step by step](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)). The older "start page" work (the single page that fronts each transaction) was studied in a 2013 discovery by the GOV.UK mainstream team and revisited in 2015 when the team printed every start page onto one sheet to review them together ([GDS Design Notes, tag "start page discovery"](https://designnotes.blog.gov.uk/tag/start-page-discovery)).

## What it does well (specific, observable design decisions)
- **Organises by task, not by department.** GDS grouped content around user-centred tasks and built the pattern to sit on top of existing content types and transactions rather than replacing them ([GDS blog, 2018](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- **Shows the whole route and the current position.** The pattern highlights the current and next steps and shows earlier steps the user may have missed; it appears alongside the content of each step ([GDS blog, 2018](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- **Plain numbered steps that expand; parallel and alternative steps marked with "and" / "or"; costs placed after the link text.** A journey can mix guidance and transactions from different departments, be done in one sitting or several, and include offline actions ([Design System pattern page](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- **Scope rules are published.** Use only for journeys with a defined start and end, where order helps, and where most of the journey lives on GOV.UK; do not use when the user only needs to read, or when there is no logical order ([Design System pattern page](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- **Research cadence.** Eight rounds of research and iteration, including users with disabilities and low digital literacy, and a review at the Digital Accessibility Centre; live-site testing started about halfway through lab research ([GDS blog, 2018](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/); [Design System pattern page](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- **The mapping process is treated as part of the design.** The authors describe the cross-government service-mapping process as mattering as much as the on-page pattern ([GDS blog, 2018](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).

## Where it fails or was criticized (sourced)
- The Design System's own "known issues": users rarely use the step-by-step header, so its purpose may be unclear; users get frustrated when looping between two step-by-steps; the pattern cannot be shown on confirmation pages; effects on mobile of turning off in-page navigation were untested ([Design System pattern page](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- The pattern is not shipped in `govuk-frontend`; only GDS builds live journeys, and others can only prototype it ([Design System pattern page](https://design-system.service.gov.uk/patterns/step-by-step-navigation)).
- A commenter on the GDS post questioned the headline usage figure; the authors replied that GDS staff traffic is filtered out but external UX professionals' traffic is not ([GDS blog, 2018, comments](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).

## Measured effects, if any (sourced)
- "Learn to drive a car" was used 1.24 million times in its first six months; 25 journeys with 15+ departments in six months; 36 by February 2019 ([GDS blog, 2018](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- A remote before/after study of three journeys found a significant rise in task completion and in users' confidence; the per-page "Is this page useful?" banner indicated users found the pattern useful ([GDS blog, 2018](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/)).
- OECD case: 24 live journeys at time of writing, a core team of about 10, more than 12 departments collaborating; step-by-step pages consistently scored higher in user feedback than existing content ([OECD toolkit PDF](https://t4.oecd.org/governance/digital-government/toolkit/goodpractices/united-kingdom-p10-step-by-step.pdf)).

## What we can borrow without copying (patterns, not visuals)
- A single ordered list of steps that is visible from every page that belongs to the journey, with "you are here" marked.
- Explicit "and" / "or" for parallel and alternative steps; cost or effort stated next to the link, not hidden behind it.
- Published rules for when the pattern does *not* apply.
- Mapping the real route across organisations before designing the page that shows it.

## Sources
- [Building a better GOV.UK, step by step](https://gds.blog.gov.uk/2018/10/17/building-a-better-gov-uk-step-by-step/), GDS blog, 17 Oct 2018. Makers' write-up with research and numbers.
- [Step by step navigation](https://design-system.service.gov.uk/patterns/step-by-step-navigation), GOV.UK Design System, undated. Pattern documentation incl. research and known issues.
- [United Kingdom P10 – Step by step](https://t4.oecd.org/governance/digital-government/toolkit/goodpractices/united-kingdom-p10-step-by-step.pdf), OECD Digital Government Toolkit, undated. Good-practice case with team size and lessons.
- [Research on this component](https://www.effortmark.co.uk/?p=5878), Effortmark, undated. Mirror of the research notes; points to three GDS posts.
- [Start page discovery (tag)](https://designnotes.blog.gov.uk/tag/start-page-discovery), GDS Design Notes, posts dated 14 Nov 2013 and 15 Oct 2015. Excerpts only; full findings not retrieved.
