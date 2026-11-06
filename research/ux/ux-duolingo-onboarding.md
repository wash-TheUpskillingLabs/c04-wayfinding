# UX case: Duolingo onboarding, try a lesson first, sign up later
**Kind:** onboarding
**Recognition:** The "delayed sign-up" experiment is one of the most-cited A/B results in consumer onboarding, described first-hand by Duolingo's then VP of Growth in a First Round Review interview (2017) and repeated in onboarding literature. Sources below. Note: the numbers come from an interview, not a published experiment report.
**Logged:** 2026-11-06

## What it is and who made it
Duolingo's new-user flow lets a person pick a language and complete a first lesson before being asked to create an account. Gina Gotthilf, VP of Growth at Duolingo, described the experiments in an interview published 17 July 2017, with product manager Kai Loh credited on the tests ([First Round Review](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)). A secondary write-up repeats the account and notes the original test predated Gotthilf's tenure ([Taplytics](https://taplytics.com/blog/duolingo-ab-test-onboarding)).

## What it does well (specific, observable design decisions)
- **Sign-up moved later in the flow**, after a lesson, so the first thing a stranger does is the thing the product is for ([First Round Review, 2017](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)).
- **"Soft walls" before a "hard wall".** The large red "Discard my progress" button (which in effect meant "don't sign up") was replaced by a subtle "Later"; the team settled on three skippable prompts followed by one required one ([First Round Review, 2017](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)).
- **A goal set during setup.** Users choose a daily goal during account creation (no separate metric given) ([First Round Review, 2017](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)).
- **Small, measured changes.** Other reported tests: encouraging in-lesson messages, a notification dot, streak copy, badges, each with a stated effect ([First Round Review, 2017](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)).

## Where it fails or was criticized (sourced)
- Hard walls performed significantly worse without soft walls first, i.e., the pattern depends on the sequence, not the delay alone ([First Round Review, 2017](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)).
- The evidence is self-reported in an interview; no methodology, sample sizes or confidence intervals are given ([First Round Review, 2017](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)).

## Measured effects, if any (sourced)
- Moving sign-up later: about a 20% increase in daily active users. Optimising soft and hard walls together, measured about three years after the original test: an 8.2% DAU increase. Growth-mindset coaching messages: D14 retention up 7.2% ([First Round Review, 2017](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)).

## What we can borrow without copying (patterns, not visuals)
- Let the stranger do the real thing before asking for anything.
- When you do ask, make "not now" quiet and reversible, and ask more than once before you require.
- Name the one small ask ("later", "set a goal") in plain words.

## Sources
- [The Tenets of A/B Testing from Duolingo's Master Growth Hacker](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker), First Round Review, 17 Jul 2017. First-hand interview with numbers.
- [How Duolingo A/B tested delayed sign-ups to drive growth](https://taplytics.com/blog/duolingo-ab-test-onboarding), Taplytics, undated. Secondary account citing the interview.
