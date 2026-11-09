# Case: Stack Overflow, a Q&A commons that admitted it was unwelcoming, then lost its askers

**Kind:** failure, and maximum variation (a question-and-answer commons, not a project community)
**Bears on:** pre-cycle, facilitators, activation-mobilization, interfaces
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
Stack Overflow is a public programming Q&A site where volunteers answer, vote on and moderate questions. Researchers documented why many would-be contributors, especially women and novices, held back; the company publicly called the site unwelcoming in 2018; a mentoring experiment improved novice questions; and after ChatGPT's release in late 2022, posting fell sharply.

## 2. Where it came from
- Denae Ford, Justin Smith, Philip J. Guo and Chris Parnin, "Paradise Unplugged: Identifying Barriers for Female Participation on Stack Overflow" (FSE 2016).
- Stack Overflow company blog posts, April 26 and June 21, 2018.
- Denae Ford, Kristina Lustig, Jeremy Banks and Chris Parnin, "'We Don't Do That Here': How Collaborative Editing with Mentors Improves Engagement in Social Q&A Communities" (CHI 2018).
- Maria del Rio-Chanona, Nadzeya Laurentsyeva and Johannes Wachs, "Large language models reduce public knowledge sharing on online Q&A platforms," *PNAS Nexus* 3, pgae400, 2024.

## 3. When
- Barrier study: 2016 (cites a 2015 Stack Overflow survey).
- Company acknowledgment: April 26, 2018; progress update June 21, 2018.
- Mentoring experiment: published April 2018 (month-long deployment).
- Posting decline: weekly posts fell 2016–2022, then faster after ChatGPT's release (November 2022); analysis window January 2022 to May 2023, paper September 11, 2024.

## 4. What it says
**Barriers before the first post**
- In a 2015 Stack Overflow survey cited by the authors, 5.8% of active contributors identified as female, against about 20% of female visitors. [Ford et al. 2016, PDF](https://pg.ucsd.edu/publications/stackoverflow-female-participation_FSE-2016.pdf)
- From 22 interviews and a 1,470-person survey, the authors named 14 barriers in three groups: unclear sense of how to take part (e.g. seeing nothing left to answer, fear of adding clutter), impersonal interactions (fear of negative feedback, discomfort with strangers, intimidating community size), and on-ramp roadblocks (time, qualifications, onboarding hoops). [Ford et al. 2016](https://pg.ucsd.edu/publications/stackoverflow-female-participation_FSE-2016.pdf)
- Women rated five barriers significantly higher than men, including fear of negative feedback and intimidating community size. [Ford et al. 2016](https://pg.ucsd.edu/publications/stackoverflow-female-participation_FSE-2016.pdf)

**The company's acknowledgment**
- In April 2018 Stack Overflow wrote that many newer coders, women, people of color and others found the site hostile or elitist, that it had under-resourced the problem, and that its evidence was user feedback ("We know because they tell us"). It cited snarky comments, unexplained downvotes and scolding of people who answered weaker questions. [Stack Overflow blog, Apr 26, 2018](https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change)
- Planned changes included a new code of conduct shown to all users, deleting unkind comments, a guided "beginner" question form, and no longer penalizing duplicates. [Stack Overflow blog, Apr 26, 2018](https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change)
- By June 2018 it had prototyped an Ask a Question wizard, had 57 employees rate 13,742 comments as fine, unwelcoming or abusive, and queued 67 further initiatives; no outcome numbers were given. [Stack Overflow blog, Jun 21, 2018](https://stackoverflow.blog/2018/06/21/rolling-out-the-welcome-wagon-june-update/)

**A mentoring experiment**
- For a month, novices about to post were routed to a "Help Room" where experienced mentors gave feedback on their draft; mentored questions scored 50% higher on average than non-mentored ones. [Microsoft Research record, CHI 2018](https://www.microsoft.com/en-us/research/?p=617610); date and authors: [MSR item](https://www.microsoft.com/en-us/research/wp-json/wp/v2/msr-research-item/617610)

**The decline**
- Weekly posts fell from about 110,000 to 60,000 between 2016 and 2022, then to about 40,000 within six months of ChatGPT's release. Relative to comparison platforms, activity dropped about 25% by six months, which the authors treat as a lower bound. [del Rio-Chanona et al. 2024, PDF](https://discovery.ucl.ac.uk/10202775/1/Large%20language%20models%20reduce%20public%20knowledge%20sharing%20on%20online%20Q%26A%20platforms.pdf)
- The drop was smallest for brand-new users and similar (about a fifth) for inexperienced and experienced users. [del Rio-Chanona et al. 2024](https://discovery.ucl.ac.uk/10202775/1/Large%20language%20models%20reduce%20public%20knowledge%20sharing%20on%20online%20Q%26A%20platforms.pdf)

## Failure modes seen
- **No visible place to contribute.** People saw no unanswered space where they could contribute. [Ford et al. 2016](https://pg.ucsd.edu/publications/stackoverflow-female-participation_FSE-2016.pdf)
- **Public correction of beginners.** Norms were enforced through visible downvotes and comments on novice posts. [MSR record](https://www.microsoft.com/en-us/research/?p=617610); [Stack Overflow blog](https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change)
- **Lurkers who never post.** Women were about 20% of visitors but 5.8% of active contributors. [Ford et al. 2016](https://pg.ucsd.edu/publications/stackoverflow-female-participation_FSE-2016.pdf)
- **A private alternative front door.** After a chatbot could answer privately, public posting fell faster than in years of prior decline. [del Rio-Chanona et al. 2024](https://discovery.ucl.ac.uk/10202775/1/Large%20language%20models%20reduce%20public%20knowledge%20sharing%20on%20online%20Q%26A%20platforms.pdf)
- **Acknowledgment without reported outcomes.** The 2018 welcome initiatives were announced with plans and inputs but no published results in the posts we found. [Stack Overflow blog, Jun 2018](https://stackoverflow.blog/2018/06/21/rolling-out-the-welcome-wagon-june-update/)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- If people can ask an AI agent privately instead of asking a person or a public channel, what happens to the commons and to the relationships that normally form through asking?
- Where in The Labs is a newcomer's first question or first piece of work seen, judged or corrected in public?
- Who is the equivalent of a "Help Room" mentor at the moment just before someone posts, presents or ships something?
- Which of the 14 barriers would someone in a library branch name before their first workshop?

## 6. Hearsay and limits
- The 2016 participation figure comes from a company survey cited in the paper; we did not open the survey. The 2018 blog posts are company statements, not independent evaluations, and we did not find published results of those initiatives.
- The mentoring study ran one month; we could not see mentor or novice counts.
- **Rival explanation:** the post-2022 decline may reflect the site's maturity (most common questions already answered, a decline visible since 2016) as much as hostility or AI substitution; the PNAS Nexus authors measure the AI effect against comparison sites but cannot rule out other changes.
- Who could confirm: Stack Overflow's community team; the Ford et al. authors (NC State at the time of the 2016 paper) and the PNAS Nexus authors.

## Sources
- [Paradise Unplugged: Identifying Barriers for Female Participation on Stack Overflow](https://pg.ucsd.edu/publications/stackoverflow-female-participation_FSE-2016.pdf), FSE 2016. Interviews and survey.
- [Stack Overflow Isn't Very Welcoming. It's Time for That to Change.](https://stackoverflow.blog/2018/04/26/stack-overflow-isnt-very-welcoming-its-time-for-that-to-change), Stack Overflow blog, April 26, 2018.
- [Rolling out the welcome wagon: June update](https://stackoverflow.blog/2018/06/21/rolling-out-the-welcome-wagon-june-update/), Stack Overflow blog, June 21, 2018.
- ["We Don't Do That Here": How Collaborative Editing with Mentors Improves Engagement in Social Q&A Communities](https://www.microsoft.com/en-us/research/?p=617610), CHI 2018 (Microsoft Research record).
- [Large language models reduce public knowledge sharing on online Q&A platforms](https://discovery.ucl.ac.uk/10202775/1/Large%20language%20models%20reduce%20public%20knowledge%20sharing%20on%20online%20Q%26A%20platforms.pdf), *PNAS Nexus*, September 11, 2024 (UCL repository copy).
