# Case: Making progress visible, portable Open Badges versus Duolingo-style streaks

**Kind:** maximum variation (a portable, issuer-controlled record of achievement vs an in-app daily counter)
**Bears on:** pre-cycle, post-cycle, activation-mobilization, interfaces
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
Two opposite ways of showing people where they stand. Open Badges (launched by Mozilla in 2011, now a standard held by 1EdTech) are verifiable records of achievement a person can carry between platforms. Streaks (Duolingo; also Snapchat) count consecutive days of activity inside one product and reset to zero on a missed day.

## 2. Where it came from
Open Badges: Mozilla's own announcements, a peer-reviewed classroom study of badge types, Credential Engine's national credential count, and a 2026 hiring experiment preprint. Streaks: Duolingo's product blog (two posts reporting its own A/B tests), a 2023 *Journal of Consumer Research* paper, and two peer-reviewed studies of Snapchat streaks among adolescents.

## 3. When
- Open Badges launched 15 Sept 2011 with MacArthur Foundation funding; stewardship moved to IMS Global 1 Jan 2017; IMS renamed 1EdTech in 2022 ([Wikipedia](https://en.wikipedia.org/wiki/Mozilla_Open_Badges)).
- Mozilla Backpack retired and users moved to Badgr, August 2019 ([Mozilla, 2019](https://medium.com/read-write-participate/the-mozilla-backpack-is-transitioning-to-badgr-c080e68d5603)). Wikipedia dates the announcement to late 2018 ([Wikipedia](https://en.wikipedia.org/wiki/Mozilla_Open_Badges)).
- Duolingo posts: Nov 2020 and Jan 2022 ([Duolingo, 2020](https://blog.duolingo.com/improving-the-streak); [Duolingo, 2022](https://blog.duolingo.com/how-duolingo-streak-builds-habit)).
- Research: 2013, 2022, 2023, 2026 (see sources).

## 4. What it says
**Open Badges and portable credentials**
- Mozilla handed off the Backpack (the place people stored badges) because it judged a steward closer to education standards was needed; users got an emailed link to migrate to Badgr, a free open-source platform from the company Concentric Sky ([Mozilla, 2019](https://medium.com/read-write-participate/the-mozilla-backpack-is-transitioning-to-badgr-c080e68d5603)).
- In a month-long study of 51 middle-schoolers using a math tutor, badge effects depended on the badge and the learner: lower performers' interest rose, but earning more *participation* badges correlated with more performance-avoidance; among higher performers, more *skill* badges correlated with higher expectancy of success ([Abramovich, Schunn, Higashi, 2013](https://www.lrdc.pitt.edu/Schunn/papers/Abramovich-Schunn-Higashi.pdf)).
- Credential Engine counted 1,076,358 unique US credentials in its 2022 report, 656,505 of them from non-academic providers (badges, certificates, licences, certifications, apprenticeships), and called for much better transparency in the credential market ([Credential Engine](https://credentialengine.org/resources/counting-u-s-secondary-and-postsecondary-credentials-report/)).
- In a pre-registered choice experiment with 1,380 German HR professionals, digital micro-credentials did not raise hiring probability and were valued below in-person certificates, mainly from lower trust in the signal ([Ehlert & Schimke, 2026 preprint](https://ideas.repec.org/p/osf/socarx/8a7h6_v1.html)).

**Streaks**
- Duolingo changed the streak in 2020 so one lesson (not the full daily goal) extends it. Reported effects: day-14 retention +3.3%, learners on a 7+ day streak +40%; the company also says fewer learners then reached their daily goals ([Duolingo, 2020](https://blog.duolingo.com/improving-the-streak)).
- Duolingo reported 6 million+ people on 7+ day streaks in Jan 2022; letting learners hold two "Streak Freezes" raised daily active learners by 0.38%. The post acknowledges that losing a streak can demotivate and that fear of losing one may stop some from starting ([Duolingo, 2022](https://blog.duolingo.com/how-duolingo-streak-builds-habit)).
- Across seven studies, people shown an intact streak in their activity log engaged more afterwards than people shown a broken one, regardless of actual past behaviour; the drop was larger when people blamed themselves and smaller when they could "repair" the streak ([Silverman & Barasch, JCR 2023](https://www.colorado.edu/business/faculty-research/2023/04/19/or-track-how-broken-streaks-affect-consumer-decisions)).
- Interviews with 25 Austrian adolescents found Snapchat streaks produced low-effort "streak snaps", password-sharing to keep streaks alive while away, nagging of partners, and relationship accounting when streaks broke ([Hristova et al., 2022](https://oars.uos.ac.uk/2901/1/Why%20did%20we%20lose%20our%20snapchat%20streak.pdf)).
- A survey of 2,483 Belgian early adolescents found streak length and number weakly correlated with fear of missing out and problematic smartphone use ([van Essen & Van Ouytsel, 2023](https://doaj.org/article/7e7e45c958c74b29ba203607b6f4a840)).

## Failure modes seen
- **Host leaves the backpack:** The original badge store was retired and holders had to migrate to a company platform ([Mozilla, 2019](https://medium.com/read-write-participate/the-mozilla-backpack-is-transitioning-to-badgr-c080e68d5603)).
- **Badge inflation / unreadable market:** Over a million distinct US credentials, with the counter itself asking for more transparency ([Credential Engine](https://credentialengine.org/resources/counting-u-s-secondary-and-postsecondary-credentials-report/)).
- **Signal not trusted by readers:** Recruiters discounted digital micro-credentials for trust reasons ([Ehlert & Schimke](https://ideas.repec.org/p/osf/socarx/8a7h6_v1.html)).
- **Badging attendance backfires for some:** More participation badges went with more performance-avoidance among weaker students ([Abramovich et al.](https://www.lrdc.pitt.edu/Schunn/papers/Abramovich-Schunn-Higashi.pdf)).
- **Counter replaces the goal:** Duolingo's own data showed fewer learners hitting daily goals once the streak got easier to keep ([Duolingo, 2020](https://blog.duolingo.com/improving-the-streak)).
- **Break-and-quit:** A visibly broken streak lowered later engagement ([Silverman & Barasch](https://www.colorado.edu/business/faculty-research/2023/04/19/or-track-how-broken-streaks-affect-consumer-decisions)).
- **Streak as social obligation:** Teens kept streaks by proxy and policed partners ([Hristova et al.](https://oars.uos.ac.uk/2901/1/Why%20did%20we%20lose%20our%20snapchat%20streak.pdf)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- A streak measures continuity; a badge measures a finished thing. Which one does each Labs threshold (attended a workshop, finished a Cycle, taught back, maintains a project) actually resemble?
- The Labs' rhythm has deliberate gaps (between Cycles, between peaks). What happened in these cases to people whose activity was healthy but discontinuous?
- Who is the reader of a Labs record: the participant, a facilitator choosing a pod, or an employer? The evidence differs sharply by reader.

## 6. Hearsay and limits
- Duolingo figures are the company's own A/B results, relative not absolute, and selected for publication.
- The JCR and hiring studies were read via abstract or summary pages only.
- Snapchat studies are about peer-to-peer streaks among teenagers, a different setting from adult learning.
- We did not find independent data on how many issued Open Badges are ever viewed by a third party.
- **Rival explanation (streak gains):** Duolingo's retention gains may come from lowering the daily bar (one lesson instead of a goal), not from the streak display itself.
- Could confirm: 1EdTech on Open Badges 3.0 adoption; Duolingo's retention team; Credential Engine on the 2025 count.

## Sources
- [The Mozilla Backpack is transitioning to Badgr](https://medium.com/read-write-participate/the-mozilla-backpack-is-transitioning-to-badgr-c080e68d5603), Mozilla (Read, Write, Participate blog), 15 Aug 2019. Retirement announcement.
- [Mozilla Open Badges](https://en.wikipedia.org/wiki/Mozilla_Open_Badges), Wikipedia, read 2026-11-05. Dates of launch and handover (secondary).
- [Are badges useful in education?](https://www.lrdc.pitt.edu/Schunn/papers/Abramovich-Schunn-Higashi.pdf), Abramovich, Schunn, Higashi, *Educational Technology Research and Development*, 2013. Classroom study of badge types.
- [Counting U.S. Secondary and Postsecondary Credentials (2022)](https://credentialengine.org/resources/counting-u-s-secondary-and-postsecondary-credentials-report/), Credential Engine, Jan 2023. National credential census.
- [The Hiring Value of Digital Micro-Credentials](https://ideas.repec.org/p/osf/socarx/8a7h6_v1.html), Ehlert & Schimke, SocArXiv preprint, 2026. Discrete choice experiment, Germany.
- [Improving the streak](https://blog.duolingo.com/improving-the-streak), Duolingo blog (Anton Yu), 19 Nov 2020. Company A/B results.
- [How Duolingo's streak builds habit](https://blog.duolingo.com/how-duolingo-streak-builds-habit), Duolingo blog (Osman Mansur), 31 Jan 2022. Streak Freeze results and stated downsides.
- [On or Off Track: How (Broken) Streaks Affect Consumer Decisions](https://www.colorado.edu/business/faculty-research/2023/04/19/or-track-how-broken-streaks-affect-consumer-decisions), Silverman & Barasch, *Journal of Consumer Research* 49(6), 2023; summary by Leeds School of Business.
- ["Why did we lose our snapchat streak?"](https://oars.uos.ac.uk/2901/1/Why%20did%20we%20lose%20our%20snapchat%20streak.pdf), Hristova et al., *Computers in Human Behavior Reports* 5, 2022. Interview study.
- [Snapchat streaks and problematic smartphone use / FOMO](https://doaj.org/article/7e7e45c958c74b29ba203607b6f4a840), van Essen & Van Ouytsel, *Telematics and Informatics Reports* 11, 2023. Survey study.
