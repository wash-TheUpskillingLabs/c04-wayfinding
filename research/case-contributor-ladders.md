# Case: Kubernetes membership ladder and Apache's meritocracy roles, published rungs and the pruning that follows

**Kind:** paradigmatic (two of the most-copied open-source role ladders)
**Bears on:** post-cycle, facilitators, activation-mobilization
**Product part:** post-between | facilitators
**Logged:** 2026-11-06 (desk research, sources below)

## 1. What it is
Both projects publish a written ladder of roles with stated requirements for climbing it. Kubernetes (member → reviewer → approver → subproject owner) sets numeric thresholds and prunes inactive members on a schedule; the Apache Software Foundation (user → developer → committer → PMC member → ASF member) grants each rung by vote on "merit," and leaves inactivity handling to individual projects.

## 2. Where it came from
Kubernetes governance documents maintained by SIG Contributor Experience and the kubernetes-dev / dev@kubernetes.io announcement lists (2020–2025); the ASF's "How it works" page; the Apache NiFi project's 2025 inactive-committer policy; a 2018 Kubernetes contributor survey instrument; and a first-person account by an Outreachy intern onboarding to Kubernetes.

## 3. When
ASF founded 1999. Kubernetes community-membership document in force since c. 2017; org cleanups May–July 2020, July 2023 (rule change), June–July 2025. NiFi policy adopted September 1, 2025.

## 4. What it says

**Kubernetes: the rungs**
- Member: at least one merged PR, multiple contributions showing "ongoing and long-term commitment" rather than one burst, sponsorship by two reviewers/approvers from different companies, 2FA, list subscription. Members get `/lgtm`, `/ok-to-test`, and automatic CI on their PRs. [Kubernetes community membership](https://github.com/kubernetes/community/blob/master/community-membership.md)
- Reviewer: member for 3+ months, primary reviewer on 5+ PRs, reviewed or merged 20+ substantial PRs, sponsored by an approver. Approver: reviewer for 3+ months, primary reviewer on 10+, reviewed or merged 30+, nominated by a subproject owner. Subproject owner: no numeric threshold; "demonstrated responsibility and excellent technical judgement." [Kubernetes community membership](https://github.com/kubernetes/community/blob/master/community-membership.md)
- Stated rationale: membership carries elevated permissions that should not sit with people unfamiliar with the current state of the project; the aim is to keep the community healthy by encouraging active participation. [Kubernetes community membership](https://github.com/kubernetes/community/blob/master/community-membership.md)

**Kubernetes: pruning**
- May 2020 proposal: remove org members with no activity across any Kubernetes org in 18 months, measured by CNCF DevStats; about 150 people, roughly 35 of them in OWNERS files. Concerns raised in the thread: bots and well-known names appearing on the list (explained as DevStats gaps), what happens when a team is left with no owners (it bubbles up to the parent OWNERS file or the SIG), and the need to credit non-code work such as organizing meetups. [RFC: GitHub org clean up, May 2020](https://groups.google.com/g/kubernetes-sig-contribex/c/4Q40cgYdnCU/m/QQn8u94UCAAJ)
- July 2020 execution: 146 of 1,335 members slated for removal; one-third had been owners in April. The announcer's line: "We cannot expect people to actively contribute to and help maintain the project forever." Non-code contributors could be exempted case by case. [Kubernetes GitHub org clean up, July 2020](https://groups.google.com/g/kubernetes-dev/c/AvCa-sGx9Jw)
- July 2023: the inactivity window was cut from 18 to 12 months after an audit found over 600 org members with no contributions in the past year; the membership guide gained examples of what counts as a contribution. [Updates to Kubernetes org membership requirements, July 2023](https://groups.google.com/a/kubernetes.io/g/dev/c/X6zDzaDRYaU)
- June 2025: 300 of 1,532 members slated for removal or emeritus status, with a one-month window to claim contributions DevStats does not capture. [2025 Kubernetes GitHub org membership audit, June 2025](https://groups.google.com/a/kubernetes.io/g/dev/c/8u2a3KF37AU)
- Removed members must go through the membership process again; the membership document itself defines no emeritus status, though the 2025 audit email mentions moving people to emeritus "as applicable." [Kubernetes community membership](https://github.com/kubernetes/community/blob/master/community-membership.md); [2025 audit](https://groups.google.com/a/kubernetes.io/g/dev/c/8u2a3KF37AU)

**Kubernetes: the bottom rung from below**
- An Outreachy intern working full time on Kubernetes described the onboarding problem as scale: too much code and too many docs before one can be useful, almost 40 SIGs with different styles, setup instructions buried in one of ~70 files in the community repo until SIG ContribEx wrote a new guide, and a maintainer's dilemma that a newcomer "may as well disappear tomorrow." [Onboarding issues in large open source projects, part 1](https://medium.com/defectivego/onboarding-issues-in-large-scale-open-source-projects-lets-talk-kubernetes-part-1-a1a64c9c9cfe)
- The 2018 SIG ContribEx contributor survey asked respondents their ladder level and whether they wanted to advance, and asked them to rate review, CI, and PR rejection as barriers; the published README lists the questions but not the results. [Kubernetes contribex survey 2018 README](https://gitea.cncfstack.com/kubernetes/community/src/commit/7f4d6f5b4f9ef76f24e9f016f7a57041640b8bbb/sig-contributor-experience/contribex-survey-2018.md)

**Apache: the rungs**
- Roles: user; developer (contributes code or docs, active on the dev list); committer (write access, signed CLA); PMC member (a committer "elected due to merit," with binding votes and the power to propose new committers); PMC chair (appointed by the board); ASF member (nominated and elected by existing members). Decisions run on lazy consensus; a negative vote must carry an alternative. The ASF has grown "from 200 committers to around 10100." The page does not mention emeritus status or inactivity. [ASF, How it works](https://www.apache.org/foundation/how-it-works)
- Inactivity is handled project by project. Apache NiFi's policy (adopted Sept. 1, 2025): a non-PMC committer with no publicly observable activity (PRs, reviews, issues, list mail) for one year becomes inactive and loses access, can ask for it back within a year, and after a second year becomes emeritus, after which return requires renomination and a PMC vote. [Apache NiFi, Policy for inactive committers](https://cwiki.apache.org/confluence/display/NIFI/Policy+for+Inactive+Committers)

**What the case assumes that The Labs can't**
- Contributions that leave an automatic trace (GitHub events) so that activity can be audited by machine; a codebase as the shared object; mostly employer-paid contributors (Kubernetes requires sponsors from different companies); and a permission model where the rung *is* access.

## Failure modes seen
- **Ladder fills with ghosts:** 11% of Kubernetes org members in 2020, over 600 in 2023, and 300 of 1,532 in 2025 had gone inactive and had to be pruned by hand. [July 2020 cleanup](https://groups.google.com/g/kubernetes-dev/c/AvCa-sGx9Jw); [July 2023 notice](https://groups.google.com/a/kubernetes.io/g/dev/c/X6zDzaDRYaU); [2025 audit](https://groups.google.com/a/kubernetes.io/g/dev/c/8u2a3KF37AU)
- **The meter can't see non-code work:** DevStats ignores organizing, moderation, and summit volunteering, so each cleanup needs an exception process and an appeal window. [RFC May 2020](https://groups.google.com/g/kubernetes-sig-contribex/c/4Q40cgYdnCU/m/QQn8u94UCAAJ); [Kubernetes community membership](https://github.com/kubernetes/community/blob/master/community-membership.md)
- **Owners vanish, leaving empty teams:** a third of those removed in 2020 had been owners; the thread had to define what happens when a team has no owners left. [RFC May 2020](https://groups.google.com/g/kubernetes-sig-contribex/c/4Q40cgYdnCU/m/QQn8u94UCAAJ); [July 2020 cleanup](https://groups.google.com/g/kubernetes-dev/c/AvCa-sGx9Jw)
- **First rung is the steepest:** a full-time intern with a mentor still found the pre-member stage dominated by scale and fragmentation. [Onboarding issues, part 1](https://medium.com/defectivego/onboarding-issues-in-large-scale-open-source-projects-lets-talk-kubernetes-part-1-a1a64c9c9cfe)
- **"Merit" without a definition:** Apache's rungs are granted by vote on merit with no published thresholds, leaving each PMC to decide what counts. [ASF, How it works](https://www.apache.org/foundation/how-it-works)

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- Kubernetes counts PRs reviewed; Apache counts votes. What would a Labs ladder count for a facilitator or maintainer, given that a workshop taught leaves no GitHub event?
- Kubernetes needed three pruning rounds in five years and shortened the window each time. If OLOS records roles, who runs the audit, and what does "emeritus" mean for a volunteer who taught two workshops last year?
- Both ladders equate a rung with *permissions*. Which Labs rungs are permissions (can approve a project into OLOS) and which are only recognition?
- The thread that designed the pruning had to answer "what if a team has no owners left." What is the Labs equivalent of an orphaned OWNERS file — a maintained project with no maintainer?

## 6. Hearsay and limits
We cannot see how many people who were pruned came back, how long it takes a typical member to reach reviewer, or the 2018 survey results. The intern's account is one person's. **Rival explanation:** the growing count of inactive members may reflect employer churn (people reassigned off Kubernetes work by their companies) rather than any property of the ladder, which would mean the ladder is measuring corporate staffing, not individual commitment. SIG ContribEx, the CNCF (DevStats), and ASF's Community Development project could confirm.

## Sources
- [Kubernetes community membership](https://github.com/kubernetes/community/blob/master/community-membership.md), kubernetes/community on GitHub, current. The governing ladder document.
- [RFC: GitHub org clean up](https://groups.google.com/g/kubernetes-sig-contribex/c/4Q40cgYdnCU/m/QQn8u94UCAAJ), kubernetes-sig-contribex list, May 7, 2020. The design discussion with objections.
- [[ANNOUNCE] Kubernetes GitHub org clean up](https://groups.google.com/g/kubernetes-dev/c/AvCa-sGx9Jw), kubernetes-dev list, July 14, 2020. First execution, with counts.
- [[Notice] Updates to Kubernetes org membership requirements](https://groups.google.com/a/kubernetes.io/g/dev/c/X6zDzaDRYaU), dev@kubernetes.io, July 14, 2023. Window cut to 12 months; 600+ inactive.
- [[Action Required] 2025 Kubernetes GitHub org membership audit & cleanup](https://groups.google.com/a/kubernetes.io/g/dev/c/8u2a3KF37AU), dev@kubernetes.io, June 26, 2025. Third round, 300 of 1,532.
- [Kubernetes contribex survey 2018 README](https://gitea.cncfstack.com/kubernetes/community/src/commit/7f4d6f5b4f9ef76f24e9f016f7a57041640b8bbb/sig-contributor-experience/contribex-survey-2018.md), kubernetes/community mirror, 2018. Survey instrument (no results).
- [Onboarding issues in large-scale open source projects, part 1](https://medium.com/defectivego/onboarding-issues-in-large-scale-open-source-projects-lets-talk-kubernetes-part-1-a1a64c9c9cfe), Medium, undated (c. 2018). First-person newcomer account.
- [How the ASF works](https://www.apache.org/foundation/how-it-works), Apache Software Foundation, current. The canonical meritocracy roles page.
- [Policy for inactive committers](https://cwiki.apache.org/confluence/display/NIFI/Policy+for+Inactive+Committers), Apache NiFi wiki, adopted Sept. 1, 2025. One project's inactivity and emeritus rules.
