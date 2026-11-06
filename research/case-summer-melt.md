# Case: "Summer melt" and the Castleman–Page text-message experiments, nudging people across a gap they had already committed to cross

**Kind:** paradigmatic (and, at scale, a failure)
**Bears on:** pre-cycle, activation-mobilization, interfaces
**Product part:** pre-cycle | channels
**Logged:** 2026-11-06 (desk research, sources below)

## 1. What it is
"Summer melt" is the share of US high-school graduates who are accepted to college, intend to go, and then never enroll in the fall. In 2012 Benjamin Castleman and Lindsay Page ran randomized trials of automated, personalized text reminders (and separately, peer-mentor outreach) over the summer; the texts raised enrollment in some sites and not others, and later statewide and national replications mostly did not.

## 2. Where it came from
Castleman (University of Virginia) and Page (then Harvard/Pittsburgh), with uAspire and school districts. This file draws on the authors' 2013 NEBHE write-up, the 2015 journal abstract, the What Works Clearinghouse (WWC) review of the study, the 2017 Page–Gehlbach Georgia State chatbot follow-up, Castleman's own 2021 retrospective on why texting stopped working at scale, and the IES record of the AIR replication.

## 3. When
Experiments summer 2012; journal publication 2015; WWC review 2017–2018; Georgia State chatbot summer 2016 (published 2017); Castleman retrospective May 2021; AIR replication grant 2019–2025 (findings not yet on the IES page).

## 4. What it says

**The intervention**
- Students got about ten text messages over the summer with personalized reminders of tasks at their intended college (log in to the portal, register for orientation and placement tests, complete housing forms, handle health insurance), most with links, plus an offer to be connected to a counselor; a further set offered help with the FAFSA and aid letters. Cost was about $7 per student including counselor time. [NEBHE, Can text messages mitigate summer melt?](https://www.nebhe.org/post/can-text-messages-mitigate-summer-melt)
- Prior research the authors cite put summer melt at 10% to 40% of college-intending graduates. [NEBHE](https://www.nebhe.org/post/can-text-messages-mitigate-summer-melt)

**Effects, by site**
- The authors' own summary: texts raised fall enrollment by over four percentage points among low-income students in Dallas and over seven points in Lawrence and Springfield, MA, and had zero impact in Boston, which they attribute to the stronger existing college-planning supports there. Effects concentrated among students with less access to college counseling. [NEBHE](https://www.nebhe.org/post/can-text-messages-mitigate-summer-melt); [Castleman & Page 2015, JEBO abstract](https://econpapers.repec.org/RePEc:eee:jeborg:v:115:y:2015:i:c:p:144-160)
- WWC's independent reading of the same RCT (6,196 students, five sites, "meets standards without reservations"): full-sample texting, any-college enrollment 71.5% vs 69.6%, not significant; Lawrence and Springfield texting 69.9% vs 62.8%, significant; Dallas 74.2% vs 71.8%, marked not significant in the 2018 intervention report (and significant in a 2017 grant review — the two WWC documents disagree); Boston 68.5% vs 70.1%, not significant. Peer mentoring showed no significant positive effect on any-college enrollment at any site. [WWC study review 86044](https://ies.ed.gov/ncee/wwc/Study/86044)
- WWC's domain rating for the summer counseling intervention as a whole: "indeterminate effect." [WWC study review 86044](https://ies.ed.gov/ncee/wwc/Study/86044)

**Follow-ups**
- Georgia State University, summer 2016: an AI chatbot ("Pounce," built by AdmitHub) texted admitted students about their specific outstanding tasks and answered questions. Among students who had already committed to GSU, treatment students were 3.3 percentage points more likely to enroll, which the authors describe as a 21% reduction in melt; no comparable effect is reported for uncommitted students. [Page & Gehlbach, APPAM 2018 panel paper](https://appam.confex.com/appam/2018/webprogram/Paper26632.html)
- Castleman's 2021 retrospective: the original work was replicated two summers later in more cities with similar results, but later statewide and national text campaigns "have not had the same impact," and their efficacy did not seem to vary with framing, timing, delivery method, or one-on-one help (citing Bird et al. 2021 on FAFSA campaigns). His candidate explanations: large campaigns dropped the advising and sent one-way content; students did not know or trust the sender; messages were generic; and text channels became saturated as every college and agency started texting. [Behavioral Scientist, Castleman 2021](https://behavioralscientist.org/why-arent-text-message-interventions-designed-to-boost-college-success-working-at-scale/)
- An IES-funded AIR effectiveness study (2019–2025, $3.7M) set out to replicate the design at scale in Alabama, Connecticut and Indiana with roughly 18,000 four-year-bound and 18,000 two-year-bound seniors and a first-year persistence add-on; the grant is closed and the IES page lists no findings. [IES award R305A190074](https://ies.ed.gov/use-work/awards/reducing-summer-melt-text-messaging-effectiveness)

**What the case assumes that The Labs can't**
- A single hard date (fall enrollment) that everyone shares, an institution with an administrative record of each student's outstanding tasks, a counselor on the other end of the "reply for help" offer, and a population that had already applied and been accepted.

## Failure modes seen
- **No effect where support already exists:** Boston, with existing college-planning supports, showed zero enrollment effect. [NEBHE](https://www.nebhe.org/post/can-text-messages-mitigate-summer-melt)
- **Headline effect is a subgroup effect:** the full-sample texting effect was not statistically significant in WWC's reading; the significant result is one two-city site. [WWC 86044](https://ies.ed.gov/ncee/wwc/Study/86044)
- **The human-contact arm did nothing measurable:** peer mentors produced no significant enrollment gain at any site. [WWC 86044](https://ies.ed.gov/ncee/wwc/Study/86044)
- **Decay at scale (channel saturation, unknown sender, no advisor behind the text):** later statewide and national campaigns did not reproduce the effect, by the original author's account. [Castleman 2021](https://behavioralscientist.org/why-arent-text-message-interventions-designed-to-boost-college-success-working-at-scale/)
- **Only works on the already-committed:** the GSU chatbot effect is reported for students who had already committed, not for the undecided. [Page & Gehlbach 2018](https://appam.confex.com/appam/2018/webprogram/Paper26632.html)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- The texts worked where they stood in for a missing counselor and failed where a counselor already existed. In a branch-library lab, what is the "Boston" condition — who is already the counselor — and where is the "Lawrence"?
- Every message in the trial pointed to a specific outstanding task from an institutional record. What record would a pre-cycle reminder be reading from, and who maintains it?
- Castleman's explanation for failure at scale is trust in the sender and loss of the human behind the text. If OLOS sends via SMS, whose name is on the message?
- The effect was measured against a hard start date. What is the analogue of "fall enrollment" for a Cycle, and does a rolling program have a melt at all?

## 6. Hearsay and limits
From outside we cannot see which specific messages or links students acted on, how many used the counselor offer, or what happened after enrollment. The Georgia State sample size is not reported in the panel abstract. **Rival explanation:** the site differences may reflect differences in the *counselor-reply* capacity behind the texts (uAspire counselors in Massachusetts) rather than in the texts themselves; the Boston null could then be a difference in who answered, not in what the students already had. The authors (Castleman, Page), uAspire, and AIR (unpublished replication results) could confirm.

## Sources
- [Can text messages mitigate summer melt?](https://www.nebhe.org/post/can-text-messages-mitigate-summer-melt), New England Board of Higher Education, May 6, 2013. The authors' own plain-language summary of the 2012 experiment.
- [Summer nudging (JEBO 115, 2015), abstract](https://econpapers.repec.org/RePEc:eee:jeborg:v:115:y:2015:i:c:p:144-160), EconPapers. Peer-reviewed publication record.
- [WWC study review 86044](https://ies.ed.gov/ncee/wwc/Study/86044), What Works Clearinghouse, 2017–2018. Independent re-analysis with site-by-site significance.
- [How an AI virtual assistant helps students navigate the road to college](https://appam.confex.com/appam/2018/webprogram/Paper26632.html), APPAM 2018 panel paper (Page & Gehlbach). Georgia State chatbot results.
- [Why aren't text message interventions working at scale?](https://behavioralscientist.org/why-arent-text-message-interventions-designed-to-boost-college-success-working-at-scale/), Behavioral Scientist, May 3, 2021. Castleman's retrospective on the null results at scale.
- [Reducing summer melt: text messaging effectiveness](https://ies.ed.gov/use-work/awards/reducing-summer-melt-text-messaging-effectiveness), IES award record, 2019–2025. Design of the AIR scale replication; no findings posted.
