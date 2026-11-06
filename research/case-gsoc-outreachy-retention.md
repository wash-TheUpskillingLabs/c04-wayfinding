# Case: Google Summer of Code and Outreachy, paid mentored cohorts and who stays after

**Kind:** failure (the post-program cliff), with a partial counter-example
**Bears on:** pre-cycle, post-cycle, facilitators
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
Google Summer of Code (GSoC) and Outreachy run fixed-length (about three-month), stipended, mentored internships in which newcomers work on open source projects. Both are measured, implicitly or explicitly, on whether participants keep contributing after the stipend stops.

## 2. Where it came from
- GSoC: Google's program. Studied by Jefferson O. Silva, Igor Wiese, Daniel German, Christoph Treude, Marco A. Gerosa and Igor Steinmacher (ICSME 2017; *Journal of Systems and Software* preprint 2019/2020), and earlier by Andreas Schilling, Sven Laumer and Tim Weitzel at the University of Bamberg (ICIS 2011, KDE data).
- Outreachy: internships for people from groups underrepresented in tech, run under Software Freedom Conservancy. Retention analysis for OpenStack by Bitergia (an open source analytics company); Outreachy's own 2023 review.

## 3. When
- KDE GSoC cohorts 2009 and 2010, data collected August 26, 2011.
- GSoC survey covers 2010–2015 cohorts; ICSME paper September 2017; motivations paper arXiv October 2019, JSS preprint June 2020.
- Outreachy in OpenStack: interns from 2013 through end of 2017; post likely 2018 (undated).
- Outreachy 2023 review: January 11, 2024.

## 4. What it says
**GSoC**
- GSoC is a three-month program. In the studied projects, 82% merged at least one GSoC commit, but only about 54% did when only newcomers were counted; about 23% of newcomers had contributed before learning they were accepted. [NAU record, ICSME 2017](https://experts.nau.edu/en/publications/how-long-and-how-much-what-to-expect-from-summer-of-code-particip/)
- Students' commits and code before GSoC were strongly correlated with how much they produced and how long they stayed, during and after. [NAU record, ICSME 2017](https://experts.nau.edu/en/publications/how-long-and-how-much-what-to-expect-from-summer-of-code-particip/)
- The same authors later wrote that only about 16% of students kept contributing "after a few months," citing their 2017 study. [Silva et al., JSS preprint](https://par.nsf.gov/servlets/purl/10158681)
- Surveyed students (141) mainly sought technical challenge (about 67% rated essential) and career building; few said they wanted to become frequent contributors. Mentors (53) rated the stipend as the top student motivator (about 91%); only about 30% of students did. [Silva et al., arXiv 2019](https://arxiv.org/pdf/1910.05798.pdf)
- About 57% of students intended to keep contributing. Asked later, 17.0% said they had not, 21.3% rarely, 32.6% occasionally, 12.8% frequently, 16.3% became core members (self-report, self-selected sample). [Silva et al., arXiv 2019](https://arxiv.org/pdf/1910.05798.pdf); [JSS preprint](https://par.nsf.gov/servlets/purl/10158681)
- Stipends ran roughly US$3,000–6,600 depending on country. [Silva et al., arXiv 2019](https://arxiv.org/pdf/1910.05798.pdf)
- In KDE (80 GSoC students, 2009–2010), prior commits correlated with days of continued participation after GSoC, and students the team had ranked higher at selection stayed somewhat longer. [Schilling, Laumer & Weitzel, ICIS 2011](https://core.ac.uk/download/301352604.pdf)

**Outreachy**
- In OpenStack, 38 Outreachy interns across about 17 projects had aggregate retention of 13% (still contributing in the last six months), against a general community newcomer rate that stayed under 10% until 2016. [Bitergia](https://bitergia.com/blog/analysis-of-the-retention-rate-of-the-outreachy-program-in-openstack/)
- Bitergia stated the data cannot show Outreachy retains better than other programs, only that it performs at least at community level. [Bitergia](https://bitergia.com/blog/analysis-of-the-retention-rate-of-the-outreachy-program-in-openstack/)
- In 2023, Outreachy had 121 interns and passed 1,000 interns total in 14 years; 30 of that year's mentors were past Outreachy interns. The review gives no alumni retention figures. [Outreachy 2023 in review](https://www.outreachy.org/blog/2024-01-11/outreachy-2023-in-review/)

## Failure modes seen
- **Cliff after the stipend ends.** About 16% of GSoC students kept contributing after a few months. [Silva et al.](https://par.nsf.gov/servlets/purl/10158681)
- **Intent outruns behavior.** About 57% of students intended to continue, far above the measured rate. [Silva et al., arXiv](https://arxiv.org/pdf/1910.05798.pdf)
- **Program selects people who were already in.** Prior commits predicted staying, in both GSoC-wide and KDE data. [ICSME 2017](https://experts.nau.edu/en/publications/how-long-and-how-much-what-to-expect-from-summer-of-code-particip/); [ICIS 2011](https://core.ac.uk/download/301352604.pdf)
- **Mentors misread motives.** Mentors put money first; students put challenge and career first. [Silva et al., arXiv](https://arxiv.org/pdf/1910.05798.pdf)
- **No one measures the after.** Outreachy's own annual review reports intake and mentor counts but no alumni retention. [Outreachy](https://www.outreachy.org/blog/2024-01-11/outreachy-2023-in-review/)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- For people finishing a Build Cycle, what is the equivalent of "still contributing six months later," and who would count it?
- If prior involvement predicts staying, what does someone's pre-cycle history in The Labs look like, and is it visible to anyone?
- What happens to the relationship with a mentor or facilitator on the day the cycle ends?
- Outreachy reports past interns becoming mentors. What is the route from finishing a Cycle to facilitating one, and how many take it?

## 6. Hearsay and limits
- We could not open the full ICSME 2017 paper; the 16% figure and its "few months" window come from the authors' later citation of it, not from the primary table.
- Survey samples are small and self-selected (141 of 1,000 invited students; 112 of the respondents male). Outreachy figures are for one community (OpenStack) and small per-edition counts.
- **Rival explanation:** a low post-program rate may be the program working as students intended, as a career credential and paid learning experience, rather than a failure of retention; students said little about wanting to become regular contributors.
- Who could confirm: Google's GSoC program office; Outreachy organizers at Software Freedom Conservancy (who mention a 2019 longitudinal study we could not find); Bitergia.

## Sources
- [How Long and How Much: What to Expect from Summer of Code Participants?](https://experts.nau.edu/en/publications/how-long-and-how-much-what-to-expect-from-summer-of-code-particip/), ICSME 2017. Abstract record.
- [Google Summer of Code: Student Motivations and Contributions](https://arxiv.org/pdf/1910.05798.pdf), arXiv, October 2019. Survey of students and mentors.
- [Google Summer of Code: Student Motivations and Contributions (JSS preprint)](https://par.nsf.gov/servlets/purl/10158681), NSF PAR, June 2020. Source of the ≈16% statement and Table 6.
- [Is the Source Strong with You? A Fit Perspective to Predict Sustained Participation of FLOSS Developers](https://core.ac.uk/download/301352604.pdf), ICIS 2011. KDE GSoC retention.
- [Analysis of the retention rate of the Outreachy program in OpenStack](https://bitergia.com/blog/analysis-of-the-retention-rate-of-the-outreachy-program-in-openstack/), Bitergia, undated (c. 2018). Retention data.
- [Outreachy 2023: Year in Review](https://www.outreachy.org/blog/2024-01-11/outreachy-2023-in-review/), Outreachy, January 11, 2024. Program counts.
