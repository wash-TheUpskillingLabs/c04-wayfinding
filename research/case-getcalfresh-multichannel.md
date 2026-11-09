# Case: Code for America's GetCalFresh, a web-and-text "front door" laid over county benefit systems, later folded into the state portal

**Kind:** extreme (very large scale) and, at its end, a case of a layer being absorbed by the system it sat on
**Bears on:** pre-cycle, activation-mobilization, facilitators, interfaces
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
GetCalFresh is a mobile-first web application assister for California's SNAP program (CalFresh), built and run by the nonprofit Code for America, that added text-message confirmations and reminders, live chat, and partner tools on top of 58 county-run eligibility systems. Code for America ran a related text-reminder service (LA'MESSAGE) in Louisiana across several benefit programs.

## 2. Where it came from
Code for America is a US civic technology nonprofit. Sources: Code for America's own retrospective and its texting playbook; a Next City news report; an NBER working paper (later published in a peer-reviewed economics journal) from a randomized trial run partly through GetCalFresh; and the California Department of Social Services (CDSS) page on the transition to the state portal BenefitsCal.

## 3. When
- Problem baseline 2014; statewide in all counties by June 2019 ([Code for America, 2024](https://codeforamerica.org/news/reflecting-on-10-years-of-getcalfresh/)).
- LA'MESSAGE pilot April–December 2019 ([Code for America, 2020](https://codeforamerica.org/news/cell-phones-as-a-safety-net-lifeline/)).
- Trial data October 2018–May 2021; working paper May 2023 ([NBER w31239](https://www.nber.org/papers/w31239); [AEA appendix](https://topcat.aeaweb.org/articles/materials/21910)).
- Transition to BenefitsCal: steps from 30 Sept 2024 to 30 Sept 2025 ([CDSS](https://cdss.ca.gov/inforesources/cdss-programs/calfresh-outreach/getcalfresh-transition)).

## 4. What it says
**The starting problem**
- In 2014 only 66% of eligible Californians received SNAP, the fourth-lowest rate in the US ([Code for America, 2024](https://codeforamerica.org/news/reflecting-on-10-years-of-getcalfresh/)).
- The old online form took close to an hour (about 200 questions over 55 screens), could not be saved or stepped back through, and a missed interview meant denial ([Next City, 2020](https://nextcity.org/urbanist-news/californias-streamlined-snap-app-pivots-to-meet-covid-19-demand)).

**What was tried, by channel**
- Web: one question per page, mobile-first, about 10 minutes to apply, in English, Spanish and traditional Chinese ([Code for America, 2024](https://codeforamerica.org/news/reflecting-on-10-years-of-getcalfresh/); [Next City](https://nextcity.org/urbanist-news/californias-streamlined-snap-app-pivots-to-meet-covid-19-demand)).
- SMS: confirmations and reminders after submission and before interviews ([Next City](https://nextcity.org/urbanist-news/californias-streamlined-snap-app-pivots-to-meet-covid-19-demand)).
- Chat and "open text" fields collected questions; the team shipped updates about every two weeks and passed daily counts and comment themes to counties and the state during the March 2020 surge ([Next City](https://nextcity.org/urbanist-news/californias-streamlined-snap-app-pivots-to-meet-covid-19-demand)).
- Tools for community organisations applying on clients' behalf, and data dashboards for partners ([CDSS](https://cdss.ca.gov/inforesources/cdss-programs/calfresh-outreach/getcalfresh-transition)).

**What happened (numbers)**
- 7 million+ Californians used it; about 73% of the state's online SNAP applications came through it ([Code for America, 2024](https://codeforamerica.org/news/reflecting-on-10-years-of-getcalfresh/)).
- 18 and 24 March 2020: over 7,000 online applications a day, almost four times normal ([Next City](https://nextcity.org/urbanist-news/californias-streamlined-snap-app-pivots-to-meet-covid-19-demand)).
- Code for America reports interview reminders made applicants 55% more likely to complete interviews, and post-submission reminders raised document submission within 48 hours by 49% ([Code for America texting playbook, 2022](https://digitalgovernmenthub.org/wp-content/uploads/2022/11/Basics-of-Texting-Safety-Net-Clients-2022.pdf)).
- Randomized trial with about 65,000 Los Angeles applicants testing applicant-initiated ("on demand") interviews: approvals rose about six percentage points, early approvals doubled, long-term participation rose over two points ([NBER w31239](https://www.nber.org/papers/w31239)). Effects on long-term participation were significant at a few county offices and not at most others ([AEA appendix](https://topcat.aeaweb.org/articles/materials/21910)).
- Louisiana: of 108,000+ clients offered reminders, about 27,000 opted in; opted-in clients beat baseline on every measure reported (e.g., WIC kept appointments 52% vs 29%; SNAP renewals 70% vs 51%). One, two or three WIC reminders gave similar show-up rates, and "professional" wording beat "friendly" wording on Medicaid renewal returns (37.6% vs 33.8%) ([Code for America, 2020](https://codeforamerica.org/news/cell-phones-as-a-safety-net-lifeline/)).
- Context reported by Code for America: nearly 30% of GetCalFresh applicants reported homelessness; more than two-thirds of CalFresh clients who did not renew did not know they had to; about 1% of opted-in recipients later opt out ([texting playbook](https://digitalgovernmenthub.org/wp-content/uploads/2022/11/Basics-of-Texting-Safety-Net-Clients-2022.pdf)).

**How it ended**
- Between Sept 2024 and Sept 2025 the application assister, document upload, renewal (SAR 7) submission, partner tools and dashboards were switched off and redirected to BenefitsCal or the county; reminder messages were phased out per applicant ([CDSS](https://cdss.ca.gov/inforesources/cdss-programs/calfresh-outreach/getcalfresh-transition)).
- What stays: the domain, ads, and text, email and live-chat support pointing people to BenefitsCal; the state page gives no reason for the move ([CDSS](https://cdss.ca.gov/inforesources/cdss-programs/calfresh-outreach/getcalfresh-transition)).

## Failure modes seen
- **Nobody tells you the next step:** Two-thirds-plus of non-renewing CalFresh clients did not know renewal was required ([texting playbook](https://digitalgovernmenthub.org/wp-content/uploads/2022/11/Basics-of-Texting-Safety-Net-Clients-2022.pdf)).
- **Losing it only when you need it:** Louisiana clients often learned they had lost benefits only when they tried to use them ([Code for America, 2020](https://codeforamerica.org/news/cell-phones-as-a-safety-net-lifeline/)).
- **Opt-in leaves most people out:** About a quarter of the Louisiana clients offered reminders opted in ([Code for America, 2020](https://codeforamerica.org/news/cell-phones-as-a-safety-net-lifeline/)); Minnesota's opt-in share rose 90% after switching to default opt-in ([texting playbook](https://digitalgovernmenthub.org/wp-content/uploads/2022/11/Basics-of-Texting-Safety-Net-Clients-2022.pdf)).
- **Legitimate text looks like a scam:** The playbook warns official texts can be mistaken for spam and advises naming the agency and using a consistent number ([texting playbook](https://digitalgovernmenthub.org/wp-content/uploads/2022/11/Basics-of-Texting-Safety-Net-Clients-2022.pdf)).
- **Two-way channel swamps staff:** The playbook advises starting one-way and auto-routing case questions to phone lines ([texting playbook](https://digitalgovernmenthub.org/wp-content/uploads/2022/11/Basics-of-Texting-Safety-Net-Clients-2022.pdf)).
- **The front door gets absorbed:** The transactional layer was retired in favour of the state-owned portal ([CDSS](https://cdss.ca.gov/inforesources/cdss-programs/calfresh-outreach/getcalfresh-transition)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- GetCalFresh's biggest measured gains came at the *gaps* (interview, documents, renewal), not the front door. Which gaps in The Labs (between sessions, before a Cycle, after a vote) have no message at all today?
- Louisiana found wording and identity of the sender mattered more than message count. Who is the recognisable "sender" for a person who belongs to a branch lab, a region and a commons at once?
- When a better-designed layer sits on top of systems owned by others, what happened to it here, and who owns The Labs' equivalent of the "county system"?

## 6. Hearsay and limits
- Most outcome figures are Code for America's own; the NBER/AEJ trial is the independent-method source but tests the interview process, not texting alone.
- Louisiana comparisons are opted-in clients vs a baseline, not randomized, so self-selection (more engaged people opt in) may explain part of the gap.
- We could not find a public statement of why the state moved the assister into BenefitsCal.
- **Rival explanation for the ending:** consolidation onto a state-procured portal (policy, procurement and data-ownership reasons) rather than any shortfall in GetCalFresh's results.
- Could confirm: CDSS CalFresh outreach staff; Code for America's program team; county eligibility offices.

## Sources
- [Reflecting on 10 Years of Food Assistance in California](https://codeforamerica.org/news/reflecting-on-10-years-of-getcalfresh/), Code for America (Fritz Jooste), 27 Aug 2024. Retrospective with scale figures.
- [California's Streamlined SNAP App Pivots to Meet COVID-19 Demand](https://nextcity.org/urbanist-news/californias-streamlined-snap-app-pivots-to-meet-covid-19-demand), Next City (Emily Nonko), 1 Apr 2020. Independent news account of channels and the 2020 surge.
- [Cell Phones as a Safety Net Lifeline](https://codeforamerica.org/news/cell-phones-as-a-safety-net-lifeline/), Code for America (Fritz Jooste), 24 Feb 2020. Louisiana LA'MESSAGE pilot results.
- [Texting Playbook: Basics of Texting Safety Net Clients](https://digitalgovernmenthub.org/wp-content/uploads/2022/11/Basics-of-Texting-Safety-Net-Clients-2022.pdf), Code for America, Nov 2022. Practitioner guide with outcome figures and cautions.
- [Administrative Burden and Procedural Denials: Experimental Evidence from SNAP](https://www.nber.org/papers/w31239), Giannella, Homonoff, Rino, Somerville, NBER WP 31239, May 2023; published in AEJ: Economic Policy 16(4), 2024. Randomized trial.
- [Online appendix, AEARCTR-0009728](https://topcat.aeaweb.org/articles/materials/21910), American Economic Association. Office-level heterogeneity and reapplication results.
- [GetCalFresh Transition to BenefitsCal](https://cdss.ca.gov/inforesources/cdss-programs/calfresh-outreach/getcalfresh-transition), California Department of Social Services, read 2026-11-05. Official sunset schedule.
