# Case: Outreachy, a mandatory contribution period before selection

**Kind:** paradigmatic (a pre-program trial that doubles as the selection filter)
**Bears on:** pre-cycle, facilitators, activation-mobilization
**Product part:** pre-cycle | facilitators
**Logged:** 2026-11-06 (desk research, sources below)

## 1. What it is
Outreachy runs paid three-month open-source internships for people from groups underrepresented in tech. Before anyone is selected, every approved applicant must spend a multi-week "contribution period" making small, real contributions to a project while volunteer mentors review them; only applicants who record a contribution can be chosen.

## 2. Where it came from
Outreachy is a program of Software Freedom Conservancy (US nonprofit), descended from the GNOME Outreach Program for Women. This file draws on Outreachy's own mentor documentation, its organizer blog (2017 statistics post and the 2019 schedule-change post), two announcement-list emails (2019, 2021), an intern-advice post, Conservancy's 2023 year-in-review, and a JupyterHub mentor guide.

## 3. When
Program running since 2010 under GNOME, as Outreachy since 2015. Sources date from 2017 to 2024. The two-phase application design (initial application, then contribution period) dates from the December 2019 round.

## 4. What it says

**How it works today**
- Applicants submit an initial eligibility application; only those approved move on to the contribution period, where they "contact mentors and complete project tasks." Mentors are not assigned; applicants pick a project and approach the mentor themselves. [Changes to application process, 2019](https://lists.outreachy.org/pipermail/announce/2019-July/000029.html); [Dec 2021 application results](https://lists.outreachy.org/pipermail/announce/2021-October/000054.html)
- The contribution is mandatory for selection: only applicants who complete a contribution are considered. Mentors are told the strongest applicants make several small contributions consistently rather than one. [Outreachy mentor page](https://outreachy.org/mentor)
- Mentor commitment during the period: 5–10 hours a week reviewing applicant contributions; volunteer helpers 1–5 hours a week. Each community must bring funding for at least one intern ($8,000 listed). [Outreachy mentor page](https://outreachy.org/mentor)
- The stated purpose on the mentor side is to let mentors "accurately evaluate their skills"; the JupyterHub mentor guide adds a second purpose on the applicant side — the period lets applicants decide whether to submit a final application at all, and lets mentors rescope projects after seeing real work. [Outreachy mentor page](https://outreachy.org/mentor); [JupyterHub Outreachy mentor guide](https://jupyterhub-outreachy.readthedocs.io/en/latest/mentors/contribution-period/)

**The funnel**
- December 2017 round: roughly 250 applicants (derived from country percentages); 42% made a contribution; 30–50 interns accepted per round depending on funding. The organizers attributed much of the drop-off to applicants who were ineligible (full-time students), who misunderstood the form, or who stopped filling it in once they read the rules. [Outreachy statistics, Dec 2017 applicants](https://www.outreachy.org/blog/outreachy-statistics-december-march-2017-applicants/)
- December 2021 round: 2,865 initial applications; 745 approved for the contribution period; 97 projects. [Dec 2021 application results](https://lists.outreachy.org/pipermail/announce/2021-October/000054.html)
- 2023 (two cohorts): 1,936 approved applicants; 764 made contributions (3,439 merged); 121 interns; 191 mentors, 30 of them former interns; $847,000 in stipends. Conservancy argues more funding would let them accept more of the 764 contributors. [Outreachy 2023 year in review](https://sfconservancy.org/news/2024/jan/11/outreachy-2023-year-in-review/)

**The 2019 redesign and what drove it**
- Before 2019, applicants could apply at any point in a six-week window and saw only the projects listed so far; week-one applicants saw "about 25% of the total projects." A small team reviewed over a thousand initial applications per round, taking up to ten business days, so some applicants were approved only in the last two weeks. [Outreachy schedule changes, 2019](https://outreachy.org/blog/2019-07-23/outreachy-schedule-changes)
- Mentors reported being overwhelmed by six weeks of applicant traffic; some stopped responding and some delayed listing projects. The organizers cut the period to five weeks as a compromise: mentors said a shorter period would stop them judging skills accurately. [Outreachy schedule changes, 2019](https://outreachy.org/blog/2019-07-23/outreachy-schedule-changes)
- The organizers ran a regression on December 2018 data (controlling for education, prior free-software experience, gender, race) relating week of approval to the chance of recording a contribution: week 1 −5.6%, week 4 +17.6%, week 6 −12.6%. They did not state the sample size or whether the figures are percentage points. [Outreachy schedule changes, 2019](https://outreachy.org/blog/2019-07-23/outreachy-schedule-changes)
- The fix: a single finalized project list visible to all approved applicants on the same day, one uniform final deadline, and the ability for mentors to close a project to new applicants at any time. [Outreachy schedule changes, 2019](https://outreachy.org/blog/2019-07-23/outreachy-schedule-changes)

**Applicant-side time**
- Outreachy's own advice post says a first contribution "may take a week or more" including environment setup; one intern described a contribution process of over a month and a half; the post says the experience is useful whether or not you are selected. [Outreachy interns talk about the application process](https://www.outreachy.org/blog/outreachy-interns-talk-about-application-process)
- Outreachy restructured intern stipend payments in 2018 (initial payment $500 → $1,000) because stretching $500 over ten weeks was a hardship for financially independent interns — evidence that a meaningful share of applicants are not students with other support. [Changes to intern payments](https://www.outreachy.org/blog/changes-to-intern-payments)

**Retention and mentor pipeline**
- 30 of 191 mentors in 2023 were former interns. [Outreachy 2023 year in review](https://sfconservancy.org/news/2024/jan/11/outreachy-2023-year-in-review/)
- No published Outreachy data was found on whether contribution-period work predicts intern completion or post-internship retention in the project. Unverified.

**Critique: unpaid labor**
- No published critique specifically calling Outreachy's contribution period unpaid labor was found in this round. The closest is a 2017 RedMonk post on open source's "unpaid intern" problem, which names Outreachy as a *counterexample* because the internship itself is paid ($5,500 at the time). [RedMonk, open source and the unpaid intern problem](https://redmonk.com/jgovernor/open-source-and-the-unpaid-intern-problem-whats-really-up-for-grabs-outreachy). The arithmetic is still visible in Outreachy's own numbers: in 2023, 764 people made 3,439 merged contributions and 121 were paid.

## Failure modes seen
- **Mentor overwhelm at the gate:** mentors facing six weeks of applicant traffic stopped responding or delayed listing projects, which the organizers named as a reason for the 2019 redesign. [Outreachy schedule changes, 2019](https://outreachy.org/blog/2019-07-23/outreachy-schedule-changes)
- **Uneven visibility by arrival time:** early applicants saw a quarter of the projects; late-approved applicants had little time to contribute; both groups were less likely to record a contribution. [Outreachy schedule changes, 2019](https://outreachy.org/blog/2019-07-23/outreachy-schedule-changes)
- **Leak at the eligibility form:** in 2017 a large share of applicants dropped out at the form itself (ineligible, misread the questions, or quit on reading the rules) before any contribution. [Outreachy statistics, Dec 2017](https://www.outreachy.org/blog/outreachy-statistics-december-march-2017-applicants/)
- **Funding-capped funnel:** the number of interns is set by sponsor money, not by the number of qualified contributors (764 contributed, 121 placed in 2023). [Outreachy 2023 year in review](https://sfconservancy.org/news/2024/jan/11/outreachy-2023-year-in-review/)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- Outreachy's pre-program trial doubles as both a self-selection device (applicants decide whether to apply) and a mentor's evaluation device. Which of those two jobs would a Labs pre-cycle be doing, and who bears the cost?
- Outreachy's redesign was driven by mentor load, not applicant experience. What would the signal be that volunteer facilitators at a branch are reaching the "stopped responding" point?
- The 2019 data say *when* you are let in changes whether you contribute. Does a rolling pre-cycle have the same arrival-time problem, and does a fixed start date fix it or just move the cliff?
- What assumptions here can't The Labs make: a paid stipend at the end, a small number of selection slots, and a mentor who is a project maintainer with a defined task list.

## 6. Hearsay and limits
From outside we cannot see per-project applicant counts, how many applicants quit mid-period, or whether contribution-period intensity predicts internship completion. The 2018 regression is organizer-run, unpublished beyond a blog post, and reports no sample size. **Rival explanation:** the 2019 improvement in mentor experience may owe more to the earlier initial-application cutoff (fewer, pre-screened people reaching mentors) than to shortening the period from six weeks to five. Outreachy organizers and Conservancy staff hold the data; the CHAOSS project has published mentorship handbooks that may hold comparative numbers.

## Sources
- [Outreachy mentor page](https://outreachy.org/mentor), Outreachy, undated (current). Official mentor duties, hours, and selection rules.
- [Changes to Outreachy application process](https://lists.outreachy.org/pipermail/announce/2019-July/000029.html), Outreachy announce list, July 25, 2019. Two-phase application announcement with dates.
- [2019 internship schedule changes](https://outreachy.org/blog/2019-07-23/outreachy-schedule-changes), Outreachy blog, July 23, 2019. Rationale for the redesign and the week-of-approval regression.
- [Outreachy December to March 2017 applicants](https://www.outreachy.org/blog/outreachy-statistics-december-march-2017-applicants/), Outreachy blog, 2017. Applicant funnel statistics.
- [Application results for Dec 2021 cohort](https://lists.outreachy.org/pipermail/announce/2021-October/000054.html), Outreachy announce list, October 2021. Applicant and approval counts.
- [Outreachy 2023 year in review](https://sfconservancy.org/news/2024/jan/11/outreachy-2023-year-in-review/), Software Freedom Conservancy, January 11, 2024. Annual counts of applicants, contributors, interns, mentors.
- [Outreachy interns talk about the application process](https://www.outreachy.org/blog/outreachy-interns-talk-about-application-process), Outreachy blog, c. 2018–19. Intern advice on time required.
- [Changes to intern payments](https://www.outreachy.org/blog/changes-to-intern-payments), Outreachy blog, 2018. Stipend restructuring and the hardship rationale.
- [The Outreachy contribution period](https://jupyterhub-outreachy.readthedocs.io/en/latest/mentors/contribution-period/), JupyterHub mentor guide, undated. A community's own mentor playbook.
- [Open source and the unpaid intern problem](https://redmonk.com/jgovernor/open-source-and-the-unpaid-intern-problem-whats-really-up-for-grabs-outreachy), RedMonk, October 23, 2017. Analyst post on unpaid contribution; treats Outreachy as the paid alternative.
