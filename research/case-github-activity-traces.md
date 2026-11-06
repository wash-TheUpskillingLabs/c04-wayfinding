# Case: GitHub and open-source activity, a public work record that hiring managers read

**Kind:** paradigmatic
**Bears on:** post-cycle, interfaces, activation-mobilization
**Field claims:** 4, 3
**Evidence:** supports 4 narrowly; complicates 4 on depth. Employers do read public activity traces and act on them, but mostly skim volume, recency and project reputation rather than the content of the work, and still require interviews ([Marlow & Dabbish 2013](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf); [Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)). A merit-based rank inside an open-source community is linked to higher wages ([Hann et al. 2013](https://econpapers.repec.org/RePEc:inm:orisre:v:24:y:2013:i:3:p:520-538)).
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
GitHub profiles make a developer's contributions, commit history and projects publicly visible. A line of research asks whether and how employers read those traces when hiring.

## 2. Where it came from
- Marlow and Dabbish (Carnegie Mellon), interview study in ACM CSCW 2013 ([PDF](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf); [dblp record](https://dblp.org/rec/conf/cscw/MarlowD13)).
- Kuttal, Chen, Wang, Balali and Sarma, task study with hiring managers, *Information and Software Technology* 2021 ([NSF PAR copy](https://par.nsf.gov/servlets/purl/10357418); [author lab copy](https://epiclab.github.io/publications/ist-kuttal.pdf)).
- Hann, Roberts and Slaughter, panel study of Apache contributors' wages, *Information Systems Research* 2013 ([RePEc](https://econpapers.repec.org/RePEc:inm:orisre:v:24:y:2013:i:3:p:520-538)).

## 3. When
- Marlow & Dabbish: CSCW conference, February 2013.
- Hann et al.: published 2013; six-year cohort.
- Kuttal et al.: 2021 (extends a 2016 conference paper).

## 4. What it says
- Marlow & Dabbish interviewed 7 employers and 6 job seekers recruited from GitHub users; employers thought aloud while looking at real candidates' profiles ([CSCW 2013](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf)).
- Employers treated contributions to other people's projects as stronger than forks, accepted contributions to high-status projects as a community endorsement, and long commit histories as hard-to-fake evidence of motivation ([CSCW 2013](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf)).
- They discounted watcher and fork counts as gameable, did not look at how candidates interacted with others, and knew profiles were partial because private and work code is invisible ([CSCW 2013](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf)).
- The study did not check whether those impressions predicted job performance ([CSCW 2013](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf)).
- Kuttal et al. gave 10 people with hiring experience five real GitHub/Stack Overflow candidates to rank. Without tool support, most relied on commit volume and recency and few opened the content of commits; followers, stars and reputation points stood in for quality ([Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)).
- Six of ten said online traces were not enough to judge collaboration or management skill and that interviews were still needed ([Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)).
- When a tool summarized quality cues (test-passing commits, centrality), participants used those cues more ([Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)).
- Hann et al. followed Apache Software Foundation contributors for six years: reaching a higher merit-based rank was associated with up to an 18% wage increase; project-management roles paid off only when the paid job was in IT management ([ISR 2013](https://econpapers.repec.org/RePEc:inm:orisre:v:24:y:2013:i:3:p:520-538)).
- Kuttal et al. note prior work that women's pull requests may be accepted less often and that women may avoid gamified badges and reputation, so the trace itself can carry bias ([Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)).

## Failure modes seen
- **Skimming the aggregate:** Readers relied on low-effort counts (activity volume, recency, stars) and rarely inspected the actual work ([Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)).
- **Invisible work reads as absence:** Private and on-the-job code does not appear, so the record is systematically partial ([Marlow & Dabbish 2013](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf)).
- **Collaboration doesn't show:** Interactions with others were not examined and were judged hard to infer from traces ([Marlow & Dabbish 2013](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf); [Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)).
- **Trace inherits community bias:** Who gets contributions accepted shapes what the profile shows ([Kuttal et al. 2021](https://par.nsf.gov/servlets/purl/10357418)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- The cue employers trusted most was a contribution accepted by someone else's project; what is the equivalent of "accepted by others" in a library-based commons?
- If readers skim counts and recency, what gets lost about collaborative or facilitation work that leaves no commit?
- When a tool summarized quality cues, readers used them; who builds and maintains such a summary, and who is it for?

## 6. Hearsay and limits
- Both reading studies are small (13 and 10 participants), self-selected, and in software only; neither measures actual hiring outcomes.
- Hann et al. is one foundation (Apache) with an unusually formal rank system; it shows correlation over time, not that employers read the rank.
- Rival explanation for the wage premium: people who reach high rank were already more skilled and would have earned more anyway; rank may proxy ability rather than act as a signal employers read.
- Who could confirm: recruiters at firms that hire from open source; GitHub's own research on profile views by recruiters (not located).

## Sources
- [Activity traces and signals in software developer recruitment and hiring](https://www.cs.cmu.edu/~xia/resources/Documents/Marlow-cscw13.pdf), Marlow & Dabbish, ACM CSCW 2013. Interview/think-aloud study of employers reading GitHub profiles.
- [dblp: conf/cscw/MarlowD13](https://dblp.org/rec/conf/cscw/MarlowD13), dblp, n.d. Bibliographic record confirming venue.
- [Visual Resume: Exploring developers' online contributions for hiring](https://par.nsf.gov/servlets/purl/10357418), Kuttal et al., *Information and Software Technology* 138, 2021. Task study with hiring managers.
- [All Are Not Equal: … Economic Returns to Different Forms of Participation in OSS Communities](https://econpapers.repec.org/RePEc:inm:orisre:v:24:y:2013:i:3:p:520-538), Hann, Roberts & Slaughter, *Information Systems Research* 24(3), 2013. Six-year wage panel of Apache contributors.
