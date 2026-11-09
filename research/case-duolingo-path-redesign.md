# Case: Duolingo, replacing a branching skill tree with one linear path (2022)

**Kind:** paradigmatic (a design decision traded choice for guidance; measured consequence partly disclosed)
**Bears on:** pre-cycle, cycle, activation-mobilization, interfaces
**Product part:** kits | channels | post-between
**Logged:** 2026-11-06 (desk research, sources below)

## 1. What it is
In 2022 Duolingo removed its home screen "tree," where learners chose which skill to open and how far to level it, and replaced it with a single ordered path with review built in. The company said learners had not known the right way to use the tree.

## 2. Where it came from
Duolingo, a language app with more than 500 million registered users since 2011. Sources: Duolingo's own announcement blog post (May 2022), an NBC News interview with the CEO (2022), a UX Collective critique by a designer (November 2022), and a Change.org petition (August 2022).

## 3. When
Announcement 6 May 2022; roll-out to new users first, then all learners by 1 November 2022. Petition started 23 August 2022. NBC interview autumn 2022. UX critique 27 November 2022.

## 4. What it says

**The old design.** Lessons were grouped into skills; each skill had five "crown" levels plus a Legendary level, and learners decided which skill to open and when to review; Stories lived in a separate tab and Tips were hard to find ([Duolingo blog, May 2022](https://blog.duolingo.com/new-duolingo-home-screen-design/)). The CEO described it as a tree of units where the user picked the next lesson ([NBC News](https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655)).

**Stated reasons.** The company wrote that learners were "not sure whether they're using Duolingo the 'correct' or 'best' way," and that the path makes the previously recommended "hover" method (level each skill partly, then move on) the default, with spaced repetition built into the order ([Duolingo blog](https://blog.duolingo.com/new-duolingo-home-screen-design/)). The CEO said the aim was to simplify the app so new users understood how to use it, and that the change was rolled out to new users first to gauge engagement ([NBC News](https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655)).

**The new design.** Each circle on the path is one former crown level; levels from different skills are interleaved; stories, practice and unit guidebooks are attached to the path; Legendary applies to a whole unit; quests moved to their own tab ([Duolingo blog](https://blog.duolingo.com/new-duolingo-home-screen-design/)).

**Reported results.** The company said internal metrics showed engagement with the new interface was equivalent to the old; no figures were published and no retention data was reported; the CEO said it would not revert, calling the new system better and two systems hard to maintain, and that "people are change averse" ([NBC News](https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655)).

**Backlash.** A petition to reverse the path gathered 15,984 verified signatures; it complained the path is rigid and confusing, removed lesson previews, removed the ability to earn several crowns per circle, and asked for the old tree or a choice of layouts ([Change.org petition](https://www.change.org/p/reverse-duolingo-s-path-update)). NBC reported one-star reviews, a "Duo Is Sad" account, and the competitor Babbel offering to help users switch; one user quoted said he liked choosing easier lessons when tired ([NBC News](https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655)). A designer's critique: the French course went from about 10 units of about 10 exercises to about 200 units of 10+; scrolling from unit 130 back to unit 34 took about 20 seconds; colour signifiers for skill level were replaced by decorative characters; review tools sat in a Practice Hub "with no obvious links" to the path; and it became hard to see how much content existed or what was mastered ([UX Collective](https://uxdesign.cc/down-the-wrong-path-the-disaster-of-the-latest-duolingo-ui-update-a4cdd1e6ea1c)).

Interpretation: the company's claim is that guidance did not cost engagement; the critics' claim is that it cost navigability and self-direction for experienced users. Both can be true, since the metric cited is average engagement and the complaints come from a vocal subset.

## Failure modes seen
- **The map that nobody could read.** The company's own reason for the change was that learners did not know the right way to use the tree ([Duolingo blog](https://blog.duolingo.com/new-duolingo-home-screen-design/)).
- **Guidance costs self-pacing.** Users said they could no longer pick an easier lesson when tired or revisit a topic deliberately ([NBC News](https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655); [UX Collective](https://uxdesign.cc/down-the-wrong-path-the-disaster-of-the-latest-duolingo-ui-update-a4cdd1e6ea1c)).
- **Loss of the overview.** A linear feed of ~200 units made whole-course progress hard to see ([UX Collective](https://uxdesign.cc/down-the-wrong-path-the-disaster-of-the-latest-duolingo-ui-update-a4cdd1e6ea1c)).
- **Change aversion as a predicted cost.** The CEO expected backlash based on earlier changes and shipped anyway ([NBC News](https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655)).
- **Review split from the route.** Practice tools were placed in a separate hub with no link from the path ([UX Collective](https://uxdesign.cc/down-the-wrong-path-the-disaster-of-the-latest-duolingo-ui-update-a4cdd1e6ea1c)).

## 5. What it tells us about the problem
*Left for the pod. Questions to answer:*
- Duolingo chose newcomers over veterans and said so. Whose confusion is The Labs designing against: the first-timer or the returning maintainer?
- The "hover" method existed before the path; the path just made it the default. What is the method The Labs already recommends informally that a kit could make the default?
- A single path with built-in review removed the between-peak decision "what should I do today?" Is that the activation problem solved or the autodidact problem created?
- Engagement held but the overview was lost. Which of those does OLOS need to measure to know a route works?

## 6. Hearsay and limits
We cannot see Duolingo's internal data; "equivalent engagement" is a company statement with no number. The petition and critique measure the loud, not the many. Rival explanation for the backlash: the complaints track the simultaneous loss of features (previews, crowns, audio lessons, a reset of story progress) rather than linearity itself, so the trade of choice for guidance may not be what people objected to. Duolingo's learning science and product teams could confirm; the May 2022 blog post names its authors.

## Sources
- [The new Duolingo home screen design](https://blog.duolingo.com/new-duolingo-home-screen-design/), Duolingo blog, 6 May 2022. Company announcement with reasons and mechanics.
- [Duolingo's update and redesign: Luis von Ahn interview](https://www.nbcnews.com/tech/tech-news/duolingos-update-redesign-luis-von-ahn-interview-rcna44655), NBC News, 2022. CEO on reasons, results and backlash.
- [Down the wrong path: the disaster of the latest Duolingo UI update](https://uxdesign.cc/down-the-wrong-path-the-disaster-of-the-latest-duolingo-ui-update-a4cdd1e6ea1c), UX Collective (Tiina Golub), 27 November 2022. Designer's critique with unit counts and navigation timings.
- [Reverse Duolingo's path update](https://www.change.org/p/reverse-duolingo-s-path-update), Change.org, started 23 August 2022. Petition with signature count and complaint list.
