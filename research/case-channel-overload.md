# Case: Notification and channel overload, experiments in removing or batching alerts, and the Python project's four-year move off scattered channels

**Kind:** maximum variation (lab and field experiments on individuals, set beside one volunteer community's consolidation)
**Bears on:** activation-mobilization, facilitators, interfaces
**Logged:** 2026-11-05 (desk research, sources below)

## 1. What it is
Two strands. (a) Peer-reviewed experiments that interrupted people, switched their phone notifications off, or delivered them in batches, and measured stress, attention and anxiety. (b) The Python language's volunteer core developers, whose discussions had spread across mailing lists, a forum, chat and issue trackers, consolidating onto one forum between 2018 and 2022.

## 2. Where it came from
(a) A CHI 2008 lab experiment with mostly German university students; a MobileHCI 2017 field study; a 2019 field experiment in *Computers in Human Behavior* (authors include Duke researchers); Microsoft's 2023 Work Trend Index as an industry data point. (b) LWN.net reporting on the Python project, and the project's own announcement posts. Research on open-source chat (ICSE 2018 poster, FSE 2021, MSR 2019) gives context.

## 3. When
- Interruption lab study: 2008 ([Mark, Gudith, Klocke, CHI 2008](https://www.interruptions.net/literature/Mark-CHI08.pdf)).
- "Do Not Disturb Challenge": 24-hour study with a two-year follow-up, preprint posted Dec 2016, MobileHCI 2017 ([Pielot & Rello, arXiv](https://www.arxiv.org/abs/1612.02314v3)).
- Batching experiment: two weeks, published 2019 ([Springer Nature summary](https://communities.springernature.com/posts/batching-notifications-can-improve-attention-well-being-and-productivity)).
- Python: forum trial September 2018; consolidation decision September 2022 ([LWN, 2018](https://lwn.net/Articles/768487); [python-dev archive, 2022](https://mail.python.org/archives/list/python-dev@python.org/thread/NS5C6EPMNEUH7X64SSBAUKUDCWYHZGUT)).

## 4. What it says
**(a) What interruptions and notifications do**
- 48 participants answering work emails were interrupted about every two minutes. They finished *faster* than uninterrupted (about 20 vs 23 minutes) with no loss of accuracy or politeness, but reported higher stress, frustration, time pressure and effort ([Mark et al., CHI 2008](https://www.interruptions.net/literature/Mark-CHI08.pdf)).
- 30 volunteers turned off all notification alerts for 24 hours: they felt less distracted and more productive, but also anxious about not responding fast enough and less connected to their groups; about two-thirds planned to change their settings and about half were still doing so two years later ([Pielot & Rello, arXiv](https://www.arxiv.org/abs/1612.02314v3)).
- 200+ participants in India were randomised to four schedules for two weeks. Batching notifications three times a day made people happier, more attentive, more productive and less stressed than controls, with fewer phone unlocks; hourly batching gave few benefits; no alerts at all gave no benefits and *more* anxiety than usual alerts ([Fitz, Kushlev et al., via Springer Nature](https://communities.springernature.com/posts/batching-notifications-can-improve-attention-well-being-and-productivity)).
- Microsoft's 2023 survey reports 64% of employees lack the time and energy to do their work, and frames the volume of emails, chats and data as "digital debt" ([Microsoft, 2023](https://news.microsoft.com/en-xm/2023/08/02/microsofts-2023-work-trend-index-report-reveals-impact-of-digital-debt-on-innovation-emphasizes-need-for-ai-proficiency-for-every-employee/)).

**(b) Where the conversation lives**
- A 2018 sample of 400 active GitHub projects found under half listed any external channel; chat tools (Gitter, Slack, Reactiflux) were already listed more often than mailing lists ([Käfer et al., ICSE 2018 poster](https://arxiv.org/pdf/1803.09529)).
- Researchers analysing 173,000+ Gitter dialogs describe the goal of mining "knowledge embedded in the massive chat history," implying it is not otherwise reusable ([Shi et al., FSE 2021, arXiv](https://arxiv.org/abs/2107.05823v1)); a study of public Slack Q&A chats found useful content comparable to Stack Overflow's but said chat's characteristics make automatic extraction hard ([Chatterjee et al., MSR 2019](https://2019.msrconf.org/details/msr-2019-papers/27/Exploratory-Study-of-Slack-Q-A-Chats-as-a-Mining-Source-for-Software-Engineering-Tool)).
- Python, 2018: after a core sprint concluded mailing lists had reached their limits, core developers trialled a Discourse forum, planning to merge lists into one category; python-dev then had over 20,000 subscribers and it was unclear who was actually participating ([LWN, 2018](https://lwn.net/Articles/768487)).
- Python, 2022: a core developer complained that proposals were slipping by because discussion was spread across issues, pull requests, two mailing lists, Discord, Discourse and IRC; others called the split confusing and asked for one channel; objections to the forum included linear threads, accessibility, archiving and searchability ([LWN, 2022](https://lwn.net/Articles/901744)).
- September 2022: the Steering Council moved PEP announcements and the developer guide's primary channel to the forum, saying python-dev "no longer reaches the proper audience" ([python-dev archive](https://mail.python.org/archives/list/python-dev@python.org/thread/NS5C6EPMNEUH7X64SSBAUKUDCWYHZGUT)). The forum keeps an email mode for those who want it ([LWN, 2022](https://lwn.net/Articles/901744)).

## Failure modes seen
- **Speed bought with stress:** Interrupted workers kept output quality by working faster, at the cost of higher stress and effort ([Mark et al.](https://www.interruptions.net/literature/Mark-CHI08.pdf)).
- **Silence breeds anxiety:** Removing alerts entirely raised anxiety in both the 24-hour study and the batching experiment ([Pielot & Rello](https://www.arxiv.org/abs/1612.02314v3); [Fitz et al.](https://communities.springernature.com/posts/batching-notifications-can-improve-attention-well-being-and-productivity)).
- **Frequent batching is not batching:** Hourly delivery gave almost none of the benefits of three-a-day ([Fitz et al.](https://communities.springernature.com/posts/batching-notifications-can-improve-attention-well-being-and-productivity)).
- **Decisions slip between channels:** Python proposals were missed because discussion was spread over seven venues ([LWN, 2022](https://lwn.net/Articles/901744)).
- **Long half-migration:** The trial began in 2018 and the decision came in 2022, with old and new channels running in parallel throughout ([LWN, 2018](https://lwn.net/Articles/768487); [python-dev archive](https://mail.python.org/archives/list/python-dev@python.org/thread/NS5C6EPMNEUH7X64SSBAUKUDCWYHZGUT)).
- **Audience you can't see:** 20,000+ list subscribers with no way to tell who was participating ([LWN, 2018](https://lwn.net/Articles/768487)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- The batching result turns on cadence (three-a-day helped, hourly did not, none hurt). What cadence do Labs participants already live with between weekly workshops, and who sets it?
- Python's problem was not too few channels but decisions landing where the right people weren't. Where do Labs decisions (votes, project handoffs, Cycle openings) actually get announced today, and who misses them?
- "Activated" and "mobilized" imply different alert volumes. What happened in these studies when people could not tell an urgent signal from routine traffic?

## 6. Hearsay and limits
- Lab and field samples are small (30; 48) or from one country (India); they study individual phones, not community channels.
- The batching paper itself was not opened; findings are from the corresponding author's summary on Springer Nature's site.
- Microsoft sells workplace AI tools and frames its survey around them; treat as an industry data point, survey size not given on the page read.
- We did not find a study measuring whether Python participation or proposal throughput changed after the move.
- **Rival explanation (Python):** The consolidation may have been driven by moderation load and the governance change after 2018 more than by information loss; the 2018 and 2022 posts both name moderation as a reason.
- Could confirm: Python Steering Council and forum moderators; authors of the batching study.

## Sources
- [The cost of interrupted work: more speed and stress](https://www.interruptions.net/literature/Mark-CHI08.pdf), Mark, Gudith and Klocke, CHI 2008. Lab experiment.
- [Productive, Anxious, Lonely: 24 Hours Without Push Notifications](https://www.arxiv.org/abs/1612.02314v3), Pielot and Rello, arXiv / MobileHCI 2017. Field study with two-year follow-up.
- [Batching Notifications Can Improve Attention, Well-Being, and Productivity](https://communities.springernature.com/posts/batching-notifications-can-improve-attention-well-being-and-productivity), Kostadin Kushlev, Springer Nature Research Communities, 1 Aug 2019. Author summary of Fitz et al., *Computers in Human Behavior* 2019, doi 10.1016/j.chb.2019.07.016.
- [Microsoft's 2023 Work Trend Index report](https://news.microsoft.com/en-xm/2023/08/02/microsofts-2023-work-trend-index-report-reveals-impact-of-digital-debt-on-innovation-emphasizes-need-for-ai-proficiency-for-every-employee/), Microsoft News Centre, Aug 2023. Industry survey; "digital debt".
- [Communication in Open-Source Projects: End of the E-mail Era?](https://arxiv.org/pdf/1803.09529), Käfer et al., ICSE 2018 Companion. Channel census of 400 GitHub projects.
- [A First Look at Developers' Live Chat on Gitter](https://arxiv.org/abs/2107.05823v1), Shi et al., arXiv 2021 / ESEC/FSE 2021. Large-scale chat analysis.
- [Exploratory Study of Slack Q&A Chats as a Mining Source for Software Engineering Tools](https://2019.msrconf.org/details/msr-2019-papers/27/Exploratory-Study-of-Slack-Q-A-Chats-as-a-Mining-Source-for-Software-Engineering-Tool), Chatterjee et al., MSR 2019. Knowledge in chat vs Q&A sites.
- [python-committers is dead, long live discuss.python.org](https://lwn.net/Articles/768487), LWN.net reproduction of the core developers' list message, 28 Sep 2018.
- [Leaving python-dev behind](https://lwn.net/Articles/901744), Jake Edge, LWN.net, 20 Jul 2022. Debate over consolidation.
- [Moving to Discourse](https://mail.python.org/archives/list/python-dev@python.org/thread/NS5C6EPMNEUH7X64SSBAUKUDCWYHZGUT), python-dev archive, 20 Sep 2022. Steering Council decision.
