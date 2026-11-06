# Case: Hackathons and sprints, what happens to the projects after the weekend

**Kind:** failure (most projects stop), with measured predictors of the exceptions
**Bears on:** post-cycle, cycle, activation-mobilization
**Product part:** cycle | post-between | kits
**Logged:** 2026-11-06 (desk research, sources below)

## 1. What it is
A hackathon is a time-boxed (usually 24–72 hour) event where teams form, build a prototype and present it. The research question here is whether the work survives the event, measured by commits, reuse, or organizational uptake, and what predicts survival.

## 2. Where it came from
Mainly the work of Alexander Nolte (University of Tartu / Carnegie Mellon) and colleagues: a 2020 CSCW archival study of Devpost hackathons; a 2018 study of five teams at Microsoft's company-wide hackathon; and a large-scale code-reuse study with Audris Mockus's World of Code group. Civic-side critique from Code for America (2012), Johnson and Robinson (2014), a 2017 survey of civic hackathon participants in Brazil and Australia, and a 2019 account of an Australian regional hackathon series.

## 3. When
- Data: Devpost hackathons April 11 to May 11, 2018 (GitHub data to November 2018); Microsoft One Week, summer 2017, followed four months; Devpost projects to 2021 in the reuse study.
- Sources: 2012 (Code for America), 2014 (Johnson and Robinson), 2017 (Gama), 2018 (Nolte et al.), 2019 (Hendery et al.), 2020 (Nolte, Chounta, Herbsleb), 2021 (Imam et al.), 2024 (ICTworks synopsis).

## 4. What it says

**How many continue**
- Of projects from 73 co-located Devpost hackathons (1,912 participants, 592 unique projects), 35.3% had at least one GitHub commit after the event, 17.06% had commits by day 6, and 3.55% still had commits after five months; the authors summarize that about 65% were discontinued. [Nolte, Chounta and Herbsleb, CSCW 2020](https://par.nsf.gov/servlets/purl/10284449)
- At Microsoft's 2017 One Week (18,000+ employees, 4,700+ projects company-wide), 2 of 5 studied teams' projects were continued four months later, both taken over by other organizational units; no original member was involved in one of them. [Nolte et al., 2018](https://alexandernolte.github.io/download/Nolte%20et%20al.%20(2018)%20You%20Hacked%20and%20Now%20What%20-%20Exploring%20Outcomes%20of%20a%20Corporate%20Hackathon.pdf)
- Across 22,183 Devpost projects matched in World of Code, 28.8% of the 581,579 code blobs created at hackathons were later reused in other projects, 89.2% of them small; only 5.3% of blobs were created after the event, which the authors read as teams adding little afterward. Weekly reuse never exceeded 0.8% of blobs and leveled off after roughly 10–15 weeks. [Imam, Dey, Nolte, Mockus and Herbsleb, arXiv 2021](https://ar5iv.labs.arxiv.org/html/2103.01145)

**What predicts continuation**
- Short term (first six days): more technologies used (odds ratio 1.29 per technology), winning a prize weighted by field size (OR 6.43), and technical preparation before the event (OR 2.12). [Nolte et al., 2020](https://par.nsf.gov/servlets/purl/10284449)
- Long term (to five months): skill diversity (71% lower hazard of stopping), skill matching (53% lower), and intent to expand reach (users, funding, startup). Heavy commit frequency in the first six days raised the hazard of stopping. Team size, prior familiarity, prior hackathon experience and general "we intend to continue" were not significant. [Nolte et al., 2020](https://par.nsf.gov/servlets/purl/10284449)
- At Microsoft, the two continued projects had working prototypes by day two, had prepared with stakeholders beforehand, assigned tasks by skill, matched products already in planning, and presented beyond their own unit. Leader intent did not predict continuation (one leader rated intent 5/5 and the project stopped); a prior promise of developers from management did not either. [Nolte et al., 2018](https://alexandernolte.github.io/download/Nolte%20et%20al.%20(2018)%20You%20Hacked%20and%20Now%20What%20-%20Exploring%20Outcomes%20of%20a%20Corporate%20Hackathon.pdf)
- Code reuse was higher for projects with more participants, more technologies, and more code written before and during the event; co-location was marginally positive. [Imam et al., 2021](https://ar5iv.labs.arxiv.org/html/2103.01145)
- ICTworks' synopsis of the 2020 study adds that many hackathons are not designed with continuation in mind, "a major missed opportunity." [ICTworks, March 2024](https://www.ictworks.org/long-term-hackathon-success)

**Civic hackathon critiques**
- A 2012 Code for America fellow wrote that some civic hackathon projects are not pursued afterward, that reuse of earlier work "does not happen often enough," because developers prefer new code and events reward finished apps rather than reusable parts; proposed giving community organizations ownership of the apps. [Code for America via opensource.com, 2012](https://opensource.com/government/12/6/how-do-we-recycle-hackathon-code)
- Johnson and Robinson (2014) framed civic hackathons as possibly innovation, procurement, or civic engagement, and asked who takes part and why, calling for critical evaluation of outcomes rather than hype. [Johnson, Civic Map Lab, 2014](https://uwaterloo.ca/civic-map-lab/blog/civic-hackathons-innovation-procurement-or-civic-engagement)
- A survey of 123 participants at three civic hackathons (GovHack, Hackacity, Hacker Cidadão) found prizes rated least important and learning, networking and civic engagement most important; it cites earlier claims that civic apps are quickly abandoned but does not test them. [Gama, ICEIS 2017](https://www.scitepress.org/Papers/2017/63770/63770.pdf)
- Organizers of four Western Sydney weekend hackathons (2015–2017, 15–20 people each) describe a "shadow world" of projects begun and unfinished or finished without users, attributing it to missing skills, maker burnout when users contribute nothing, and funders favoring clear ROI; a linked incubator was meant to carry prototypes forward but no results are reported. [Hendery et al., 2019](https://core.ac.uk/download/351835418.pdf)

## Failure modes seen
- **Cliff after the event.** 65% of Devpost projects had no commit afterward; 3.55% were alive at five months. [Nolte et al., 2020](https://par.nsf.gov/servlets/purl/10284449)
- **Intent is not a predictor.** General continuation intent and leader intent did not predict survival in either study. [Nolte et al., 2020](https://par.nsf.gov/servlets/purl/10284449); [Nolte et al., 2018](https://alexandernolte.github.io/download/Nolte%20et%20al.%20(2018)%20You%20Hacked%20and%20Now%20What%20-%20Exploring%20Outcomes%20of%20a%20Corporate%20Hackathon.pdf)
- **Sprint burn predicts stop.** Higher commit frequency in the first week raised the hazard of discontinuation. [Nolte et al., 2020](https://par.nsf.gov/servlets/purl/10284449)
- **Survival by handover, not by team.** Both continued Microsoft projects were taken over by other units. [Nolte et al., 2018](https://alexandernolte.github.io/download/Nolte%20et%20al.%20(2018)%20You%20Hacked%20and%20Now%20What%20-%20Exploring%20Outcomes%20of%20a%20Corporate%20Hackathon.pdf)
- **Rewards shape the output.** Events reward finished apps, so reusable parts and datasets go unrecognized. [Code for America, 2012](https://opensource.com/government/12/6/how-do-we-recycle-hackathon-code)
- **No one tracks it.** Civic studies measure motivation, not whether apps live. [Gama, 2017](https://www.scitepress.org/Papers/2017/63770/63770.pdf)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- Preparation before the event and skill-matched teams predicted survival. What would "technical preparation" look like in a pre-cycle, and is it visible when pods form?
- The projects that lived were handed to someone else. What is the handover step at the end of a Cycle, and to whom: a maintainer, a lab, a partner?
- A high first-week burn predicted stopping. What does the Cycle's pacing reward, and what does the vote reward?
- Civic hackathons reward finished apps over reusable parts. What does OLOS count as a shipped project?

## 6. Hearsay and limits
- The Devpost sample is one month of co-located hackathons in 2018 with GitHub links, and "continuation" is a commit, not use. The Microsoft study is five teams inside one company with paid staff and managers who can adopt a project; the reuse study measures code copying, not project life.
- Nolte and Herbsleb appear on three of the four quantitative sources; there is little independent replication here.
- Hackathons assume what The Labs cannot in several cases: paid employees (Microsoft), prize money, and a 48-hour peak rather than twelve weeks.
- **Rival explanation:** low continuation may be the design working, not failing: participants in civic events said they came to learn and meet people, not to ship, and a weekend prototype that teaches its team and then dies may be the intended product.
- Who could confirm: the authors (Nolte, Herbsleb); Devpost; Code for America brigade organizers (see `cases-civic/case-cfa-brigade-network.md`).

## Sources
- [What Happens to All These Hackathon Projects? Identifying Factors to Promote Hackathon Project Continuation](https://par.nsf.gov/servlets/purl/10284449), Nolte, Chounta and Herbsleb, PACM HCI (CSCW) 2020. Devpost/GitHub continuation study.
- [You Hacked and Now What? Exploring Outcomes of a Corporate Hackathon](https://alexandernolte.github.io/download/Nolte%20et%20al.%20(2018)%20You%20Hacked%20and%20Now%20What%20-%20Exploring%20Outcomes%20of%20a%20Corporate%20Hackathon.pdf), Nolte et al., 2018 (author's copy). Five Microsoft teams followed four months.
- [The Secret Life of Hackathon Code](https://ar5iv.labs.arxiv.org/html/2103.01145), Imam, Dey, Nolte, Mockus and Herbsleb, arXiv 2103.01145 (2021). Code reuse across 22,183 projects.
- [Long-Term Hackathon Success](https://www.ictworks.org/long-term-hackathon-success), ICTworks, March 14, 2024. Synopsis of the 2020 study.
- [How do we recycle hackathon code?](https://opensource.com/government/12/6/how-do-we-recycle-hackathon-code), Code for America fellow via opensource.com, June 2012. Civic critique and proposed fixes.
- [Civic Hackathons: Innovation, Procurement, or Civic Engagement?](https://uwaterloo.ca/civic-map-lab/blog/civic-hackathons-innovation-procurement-or-civic-engagement), Johnson (blog on the Johnson and Robinson 2014 *Review of Policy Research* viewpoint), July 2014. Framing of civic hackathons.
- [Crowdsourced Software Development in Civic Apps: Motivations of Civic Hackathons Participants](https://www.scitepress.org/Papers/2017/63770/63770.pdf), Gama, ICEIS 2017. Survey of 123 participants.
- [Prototyping through Play: Making an Urban Satellite Region Hackathon](https://core.ac.uk/download/351835418.pdf), Hendery, Magee, Perry and Swist, *Trace* 2019. Qualitative account of four regional hackathons.
