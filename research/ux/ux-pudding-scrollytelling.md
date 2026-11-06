# UX case: The Pudding, scroll-driven visual essays and its published method
**Kind:** explainer
**Recognition:** Peabody Award for Digital Journalism (2017); Online Journalism Award for General Excellence, Micro Newsroom (2019); SND Best in Show (2024, 2025); World Press Photo Interactive of the Year (2021, with The Washington Post); Pamela Tobey Award for Excellence in Visual Storytelling (2026). Sources below.
**Logged:** 2026-11-06

## What it is and who made it
A digital publication, active since 2017, that explains ideas debated in culture through visual essays; a small collective in which members handle research, analysis, design, writing and code, with no news-cycle deadlines and no ads or paywall ([The Pudding, FAQ](https://pudding.cool/faq/)). The 2019 OJA entry describes six full-time "journalist-engineers" and cites projects such as hand-measuring 80 pairs of jeans to test women's pocket sizes ([ONA awards entry, 2019](https://awards.journalists.org/entries/the-pudding/)). The team publishes its method in "process" posts; the two used here are by Russell Samora: a comparison of six scrollytelling libraries (January 2017, updated November 2017 with his own library, Scrollama) and a set of responsive-scrollytelling practices (April 2017) ([How to implement scrollytelling](https://pudding.cool/process/how-to-implement-scrollytelling/); [Responsive scrollytelling best practices](https://pudding.cool/process/responsive-scrollytelling/)).

## What it does well (specific, observable design decisions)
- **Scroll-to-trigger, not scroll-jacking.** Text blocks tell the graphic which state to show; scroll behaviour itself is never altered. The graphic stays fixed while text scrolls, then snaps back into flow on exit, because the scrolly section is usually only part of the story ([How to implement scrollytelling](https://pudding.cool/process/how-to-implement-scrollytelling/)).
- **Keep the scrolly only when the transition carries meaning.** Otherwise stack static charts; avoid steppers (require clicks) and swipe/tap interfaces (override native scrolling) ([Responsive scrollytelling](https://pudding.cool/process/responsive-scrollytelling/)).
- **Short pacing.** A few steps to hook and make the point, then exit; credited to Tony Chu's OpenVis talk ([Responsive scrollytelling](https://pudding.cool/process/responsive-scrollytelling/)).
- **Mobile is treated as width first, then touch, location and connection.** Replace hover with fixed annotations; make any mouse interaction an explicit control; compute step heights from `window.innerHeight` rather than `vh` because mobile browser bars change viewport height ([Responsive scrollytelling](https://pudding.cool/process/responsive-scrollytelling/)).
- **Separate chart setup from chart drawing** so a resize updates rather than rebuilds ([Responsive scrollytelling](https://pudding.cool/process/responsive-scrollytelling/)).
- **The method is open.** Example code is published on GitHub under the polygraph-cool organisation; the FAQ invites readers to office hours ([How to implement scrollytelling](https://pudding.cool/process/how-to-implement-scrollytelling/); [FAQ](https://pudding.cool/faq/)).

## Where it fails or was criticized (sourced)
- None found in the sources opened. The FAQ itself says many ideas are dropped during production ([FAQ](https://pudding.cool/faq/)). The 2019 award page gives no judges' comments ([ONA entry](https://awards.journalists.org/entries/the-pudding/)).

## Measured effects, if any (sourced)
- None published. Neither process post reports reader-behaviour data ([Responsive scrollytelling](https://pudding.cool/process/responsive-scrollytelling/)).

## What we can borrow without copying (patterns, not visuals)
- Animate only where the change *is* the point; otherwise show a static state.
- One fixed graphic, text that moves past it, and a clean entry and exit from the fixed region.
- Hook, point, exit: a handful of steps, not a tour.
- Design the mobile case as a width problem first and remove hover entirely.

## Sources
- [FAQ](https://pudding.cool/faq/), The Pudding, undated. Self-description, process, awards list.
- [The Pudding – General Excellence in Online Journalism, Micro Newsroom](https://awards.journalists.org/entries/the-pudding/), Online News Association, 2019. Award entry.
- [How to implement scrollytelling with six different libraries](https://pudding.cool/process/how-to-implement-scrollytelling/), Russell Samora, The Pudding, Jan 2017 (updated Nov 2017). Makers' method post.
- [Responsive scrollytelling best practices](https://pudding.cool/process/responsive-scrollytelling/), Russell Samora, The Pudding, Apr 2017. Makers' method post.
