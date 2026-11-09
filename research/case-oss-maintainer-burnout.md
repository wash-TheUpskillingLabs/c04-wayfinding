# Case: Open source maintainers, the small group left holding what everyone uses

**Kind:** extreme (very few people carrying very large user bases), with one documented failure (xz Utils, 2024)
**Bears on:** post-cycle, facilitators, activation-mobilization, interfaces
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
Much widely used open source software is maintained by one or a few mostly unpaid people. Reports, surveys and empirical studies document what that position looks like over time: thankless work, stress, people quitting or thinking about it, and the risk when a tired maintainer hands the project to someone new.

## 2. Where it came from
- Nadia Eghbal, *Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure* (Ford Foundation, 2016) and *Working in Public: The Making and Maintenance of Open Source Software* (Stripe Press, 2020). Eghbal worked on open source developer experience independently and at GitHub, 2015–2019 (Stripe Press bio).
- Tidelift (a company that pays maintainers) surveys of maintainers in 2021, 2023 and 2024.
- Courtney Miller, David Widder, Christian Kästner and Bogdan Vasilescu (Carnegie Mellon), on why contributors disengage (OSS 2019).
- Naveen Raman, Minxuan Cao, Yulia Tsvetkov, Christian Kästner and Bogdan Vasilescu, on toxicity and burnout (ICSE NIER 2020).
- The xz Utils backdoor (CVE-2024-3094), as reported by Black Duck (security vendor) and GIGAZINE (news site timeline).

## 3. When
- *Roads and Bridges*: July 14, 2016. *Working in Public*: 2020 (New Books Network interview August 12, 2020).
- Tidelift 2024 survey: fielded mid-2024, released September 17, 2024.
- Miller et al.: GHTorrent data from August 2018; IFIP OSS 2019.
- Raman et al.: ICSE 2020; toxicity measured 2012–2018.
- xz Utils: attacker's first patch October 2021; maintainership handed over during 2022; backdoor discovered March 28–29, 2024.

## 4. What it says
**Who does the work**
- *Roads and Bridges* argues that public code underpinning digital systems is maintained mostly by unpaid volunteers, which leaves it underfunded and exposed; the report's summary calls it "built and maintained almost exclusively by unpaid volunteers." [Ford Foundation](https://www.fordfoundation.org/work/learning/research-reports/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure/)
- *Working in Public* describes a shift from open source as broad collaboration to ongoing maintenance by solo, often unseen developers, drawing on hundreds of developer interviews. [Stripe Press](https://press.stripe.com/working-in-public)
- Eghbal sorts projects by contributor growth and user growth: federations (many of both), clubs (many contributors, fewer users), toys (few of either), and stadiums (one or a few maintainers, very many users). In stadiums the scarce resource is the maintainer's attention. [a16z podcast transcript, 2022](https://a16z.com/podcast/learning-from-open-source-communities/)
- She contrasts casual "drive-by" contributors who make one contribution with active contributors who, for example, answer other people's questions. [a16z](https://a16z.com/podcast/learning-from-open-source-communities/)

**What maintainers report**
- In Tidelift's 2024 survey of 400+ maintainers, 60% were unpaid hobbyists and 60% had quit or considered quitting. [Business Wire, Sept 17, 2024](https://www.businesswire.com/news/home/20240917030299/en)
- 48% felt underappreciated or that the work was thankless (40% in 2021); 43% said it added to personal stress (54% in 2023, 45% in 2021). The top-rated dislike was not being paid enough (50%). [Tidelift on DEV, Oct 10, 2024](https://dev.to/tidelift/almost-half-of-maintainers-feel-underappreciated-and-like-the-work-is-thankless-j0i)
- Paid maintainers were 55% more likely on average to follow key security and maintenance practices. [Business Wire](https://www.businesswire.com/news/home/20240917030299/en)

**Why contributors stop**
- Of 151 recently inactive GitHub contributors surveyed, the most common reasons were occupational (new job without open source time, role change, leaving school or job); social reasons (lost interest, no time, lack of peer support) came second. Job or school transition more than doubled the hazard of disengaging (hazard ratio 2.48). [Miller et al. 2019](https://cmustrudel.github.io/papers/miller19dropout.pdf)
- People who contributed mostly during office hours were more likely to disengage than those who contributed nights and weekends (hazard ratio 2.20). [Miller et al. 2019](https://cmustrudel.github.io/papers/miller19dropout.pdf)
- Developers report stress from constant feature and fix requests, often in harsh language; a classifier found toxicity varied across GitHub communities and declined from 2012 to 2018. [Raman et al., ICSE 2020](https://2020.icse-conferences.org/details/icse-2020-New-Ideas-and-Emerging-Results/13/Stress-and-Burnout-in-Open-Source-Toward-Finding-Understanding-and-Mitigating-Unhe)

**When handover goes wrong (xz Utils)**
- A new account began contributing harmless patches to xz Utils in October 2021. From April 2022, other accounts on the mailing list complained that patches went unreviewed and pushed for a new maintainer. The sole long-time maintainer replied that his capacity was limited, and by mid-2022 described the newcomer as effectively a co-maintainer. [GIGAZINE timeline](https://gigazine.net/gsc_news/en/20240403-timeline-of-xz-open-source-attack)
- The new co-maintainer inserted a backdoor in early 2024; it was disclosed March 29, 2024. Black Duck describes the original maintainer handing over oversight while citing overwork and burnout. [Black Duck, April 8, 2024](https://www.blackduck.com/blog/xz-utils-backdoor-supply-chain-attack.html)

## Failure modes seen
- **Stadium shape.** A few maintainers serve many users whose questions consume the maintainers' attention. [a16z](https://a16z.com/podcast/learning-from-open-source-communities/)
- **Quiet exit on life change.** A job or school transition more than doubled the hazard of disengaging. [Miller et al.](https://cmustrudel.github.io/papers/miller19dropout.pdf)
- **Thankless upkeep.** Nearly half of maintainers felt the work was thankless in 2024. [Tidelift](https://dev.to/tidelift/almost-half-of-maintainers-feel-underappreciated-and-like-the-work-is-thankless-j0i)
- **Handover under pressure, without vetting.** In xz Utils, public pressure about slow maintenance preceded handing commit rights to a newcomer who turned out to be an attacker. [GIGAZINE](https://gigazine.net/gsc_news/en/20240403-timeline-of-xz-open-source-attack); [Black Duck](https://www.blackduck.com/blog/xz-utils-backdoor-supply-chain-attack.html)
- **Hostile demand from users.** Harsh feature and fix requests are a reported source of stress. [Raman et al.](https://2020.icse-conferences.org/details/icse-2020-New-Ideas-and-Emerging-Results/13/Stress-and-Burnout-in-Open-Source-Toward-Finding-Understanding-and-Mitigating-Unhe)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- When a Cycle project becomes a "maintained project" in OLOS, which of Eghbal's four shapes is it likely to take, and who carries the attention cost?
- What happens to a maintained project when its maintainer changes job or school, or moves away, and who would notice?
- How does someone become a maintainer of an existing project, and what vetting or handover exists?
- Who in The Labs is a "stadium" for questions today (one facilitator or organizer everyone asks)?

## 6. Hearsay and limits
- Tidelift sells maintainer-payment services, so its surveys are not neutral; sample is 400+ self-selected maintainers. *Working in Public* and *Roads and Bridges* are interview-based, not statistical; the four-type taxonomy here comes from an interview transcript and the publisher's description, not the book text, which we did not open.
- The xz Utils account is reconstructed from mailing-list posts by secondary sources; we did not open the mailing list or CISA's alert directly. Individuals involved are not named here.
- **Rival explanation:** maintainer attrition may mostly track ordinary life transitions (Miller et al.'s strongest predictor) rather than burnout or toxicity specifically; quitting a hobby after a job change is not necessarily a failure of the project.
- Who could confirm: Tidelift's survey team; Carnegie Mellon STRUDEL lab; distribution security teams (Debian, Red Hat) for xz.

## Sources
- [Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure](https://www.fordfoundation.org/work/learning/research-reports/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure/), Ford Foundation, July 14, 2016. Report summary page.
- [Working in Public](https://press.stripe.com/working-in-public), Stripe Press, 2020. Publisher description and author bio.
- [Nadia Eghbal, "Working in Public"](https://newbooksnetwork.com/nadia-eghbal-working-in-public-the-making-and-maintenance-of-open-source-software-stripe-press-2020), New Books Network, August 12, 2020. Interview page (dates the book).
- [Learning from Open Source Communities](https://a16z.com/podcast/learning-from-open-source-communities/), a16z podcast, August 11, 2022. Eghbal describes the four project types.
- [Tidelift 2024 State of the Open Source Maintainer Report release](https://www.businesswire.com/news/home/20240917030299/en), Business Wire, September 17, 2024.
- [Almost half of maintainers feel underappreciated](https://dev.to/tidelift/almost-half-of-maintainers-feel-underappreciated-and-like-the-work-is-thankless-j0i), Tidelift on DEV Community, October 10, 2024. Year-over-year survey figures.
- [Why do People Give Up FLOSSing?](https://cmustrudel.github.io/papers/miller19dropout.pdf), Miller et al., OSS 2019. Survey and survival model of disengagement.
- [Stress and Burnout in Open Source](https://2020.icse-conferences.org/details/icse-2020-New-Ideas-and-Emerging-Results/13/Stress-and-Burnout-in-Open-Source-Toward-Finding-Understanding-and-Mitigating-Unhe), ICSE 2020 NIER. Abstract.
- [What is the Xz Utils Backdoor](https://www.blackduck.com/blog/xz-utils-backdoor-supply-chain-attack.html), Black Duck, April 8, 2024.
- [Timeline summary of the backdoor attack on XZ Utils](https://gigazine.net/gsc_news/en/20240403-timeline-of-xz-open-source-attack), GIGAZINE, April 3, 2024.
