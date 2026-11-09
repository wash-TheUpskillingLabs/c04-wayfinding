# Case: Open source projects, getting newcomers to a first accepted contribution

**Kind:** paradigmatic (the standard model of newcomer barriers in open source), with documented failures
**Bears on:** pre-cycle, cycle, facilitators, interfaces
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
A decade of software-engineering research on why people who want to contribute to open source projects stall before or just after their first contribution, and on two common fixes: a guided newcomer portal (FLOSScoach) and the "good first issue" label on GitHub.

## 2. Where it came from
- Igor Steinmacher, Marco Aurélio Gerosa and colleagues (publications indexed by Northern Arizona University): systematic review of barriers (OSS 2014; journal version *Information and Software Technology* 59, 2015); FLOSScoach portal (ICSE 2016); "quasi-contributors" (ICSE 2018).
- Xin Tan, Minghui Zhou and colleagues (Peking University, Beihang University): good first issues (ESEC/FSE 2020; arXiv 2023).

## 3. When
- Barrier review: conference version 2014; journal version March 2015.
- FLOSScoach evaluation: ICSE 2016.
- Quasi-contributors: ICSE 2018 (Gothenburg).
- Good first issues: ESEC/FSE 2020; follow-up preprint 2023.

## 4. What it says
**Barrier model**
- The review of 21 studies sorted newcomer barriers into five categories: finding a way to start, social interactions, code issues, documentation problems, and newcomers' own knowledge. The barriers with most evidence were prior technical skill, getting a response from the community, depending on social contacts, and finding a suitable first task. [NAU record, OSS 2014](https://experts.nau.edu/en/publications/barriers-faced-by-newcomers-to-open-source-projects-a-systematic-/)
- The expanded journal version appeared in *Information and Software Technology* vol. 59, pp. 67–85, March 2015. [UCI ISR record](https://isr.uci.edu/node/2204.html)

**FLOSScoach (portal for newcomers)**
- Built on that barrier model and tested with 65 students using diaries, self-efficacy questionnaires and a technology-acceptance survey. [NAU record, ICSE 2016](https://experts.nau.edu/en/publications/overcoming-open-source-project-entry-barriers-with-a-portal-for-n/)
- It reduced orientation and contribution-process barriers and raised confidence, but did not reduce technical barriers. [NAU record, ICSE 2016](https://experts.nau.edu/en/publications/overcoming-open-source-project-entry-barriers-with-a-portal-for-n/)

**Quasi-contributors (contributions that never land)**
- In 21 popular GitHub projects, 10,099 people had pull requests that were never accepted, about 70% as many as the actual contributors; in five projects they outnumbered actual contributors. 12,367 pull requests were not accepted. [NAU record, ICSE 2018](https://experts.nau.edu/en/publications/almost-there-a-study-on-quasi-contributors-in-open-source-softwar/)
- Around 30% of surveyed quasi-contributors said non-acceptance demotivated them or stopped them from submitting again. Main reasons given: the work was superseded or duplicated, or it did not match the team's vision. [NAU record, ICSE 2018](https://experts.nau.edu/en/publications/almost-there-a-study-on-quasi-contributors-in-open-source-softwar/)

**Good first issues (GFIs)**
- Across 9,368 GFIs in 816 popular GitHub projects, use of the label grew over the decade, GFIs took longer to resolve than ordinary issues, and nearly half were never resolved by a newcomer. Problems named: mislabeled GFIs, too few GFIs, mismatched newcomer skill. [ESEC/FSE 2020 page](https://2020.esec-fse.org/details/fse-2020-papers/172/A-First-Look-at-Good-First-Issues-on-GitHub)
- In 48,402 closed GFIs from 964 repositories, experienced contributors took part in about 70%. Expert involvement was associated with a 71% higher newcomer success rate. The authors identified 14 newcomer challenges (including understanding the issue, setting up environments, getting no response) and 18 kinds of expert mentoring. [Tan et al. 2023, arXiv](https://ar5iv.labs.arxiv.org/html/2302.05058)
- Their conclusion, in their words: "just recommending tasks to newcomers may not be enough." [Tan et al. 2023](https://ar5iv.labs.arxiv.org/html/2302.05058)

## Failure modes seen
- **Contribution submitted, never accepted.** Quasi-contributors were about 70% as numerous as actual contributors in the 21 projects studied. [ICSE 2018](https://experts.nau.edu/en/publications/almost-there-a-study-on-quasi-contributors-in-open-source-softwar/)
- **Silence after the first ask.** "Receiving responses from the community" is among the most evidenced barriers. [OSS 2014](https://experts.nau.edu/en/publications/barriers-faced-by-newcomers-to-open-source-projects-a-systematic-/)
- **Labeled starter tasks taken by insiders.** Nearly half of good first issues were never resolved by a newcomer. [ESEC/FSE 2020](https://2020.esec-fse.org/details/fse-2020-papers/172/A-First-Look-at-Good-First-Issues-on-GitHub)
- **Orientation without technical help.** FLOSScoach helped newcomers find their way but not past technical setup. [ICSE 2016](https://experts.nau.edu/en/publications/overcoming-open-source-project-entry-barriers-with-a-portal-for-n/)
- **Duplicated or off-vision work.** The most-cited reasons for rejection were that someone else had already done it or that it did not match the team's plan. [ICSE 2018](https://experts.nau.edu/en/publications/almost-there-a-study-on-quasi-contributors-in-open-source-softwar/)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- In OLOS projects, how would anyone know how many people tried to contribute and did not land anything?
- Who decides what counts as a "first task," and does anything stop experienced people from taking them?
- Which of the five barrier categories (finding a start, social, code, documentation, own knowledge) show up when someone moves from a workshop to a Cycle, and which only show up when joining a maintained project?
- A portal helped with orientation but not technical setup. Which threshold problems in The Labs are orientation problems and which are not?

## 6. Hearsay and limits
- Most studies sample popular GitHub projects, which are not typical of small or civic projects. FLOSScoach was tested with students, not self-directed adults.
- We could not open the ICSE 2016 PDF (the redirect to the author's server was blocked) or the full 2015 journal abstract; numbers above come from the 2014 conference version and the publisher-indexed abstracts.
- The 2023 GFI preprint finds expert help is associated with success but negatively associated with retention; the authors read this as stronger newcomers needing less help, which we cannot check.
- **Rival explanation:** low newcomer conversion may reflect newcomer intent (one-off fixes, résumé building) more than project barriers; the barrier studies largely survey people who did try, not why most never meant to stay.
- Who could confirm: the Steinmacher/Gerosa group at Northern Arizona University; maintainers of large projects that use GFI labels.

## Sources
- [Barriers Faced by Newcomers to Open Source Projects: A Systematic Review](https://experts.nau.edu/en/publications/barriers-faced-by-newcomers-to-open-source-projects-a-systematic-/), OSS 2014 (Springer IFIP AICT 427). Abstract record.
- [A Systematic Literature Review on the Barriers Faced by Newcomers to OSS Projects](https://isr.uci.edu/node/2204.html), UC Irvine ISR, 2015. Bibliographic record for the IST journal version.
- [Overcoming Open Source Project Entry Barriers with a Portal for Newcomers](https://experts.nau.edu/en/publications/overcoming-open-source-project-entry-barriers-with-a-portal-for-n/), ICSE 2016. Abstract record of the FLOSScoach evaluation.
- [Almost There: A Study on Quasi-Contributors in Open Source Software Projects](https://experts.nau.edu/en/publications/almost-there-a-study-on-quasi-contributors-in-open-source-softwar/), ICSE 2018. Abstract record.
- [A First Look at Good First Issues on GitHub](https://2020.esec-fse.org/details/fse-2020-papers/172/A-First-Look-at-Good-First-Issues-on-GitHub), ESEC/FSE 2020. Conference abstract page.
- [Is It Enough to Recommend Tasks to Newcomers?](https://ar5iv.labs.arxiv.org/html/2302.05058), arXiv 2302.05058, 2023. Analysis of 48,402 closed GFIs.
