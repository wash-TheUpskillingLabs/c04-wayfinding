# UX case index: wayfinding, explainers, recruiting and onboarding (logged 2026-11-06)

Eleven case files, each with sourced recognition, observable design decisions, criticism, measured effects where published, and borrowable patterns. Rules followed: every claim linked to a page opened or found via search; at most one short quote per source; no private individuals named beyond published authors; patterns stated as facts, not recommendations.

| File | Case | Kind | The one pattern it contributes |
|---|---|---|---|
| `ux-govuk-step-by-step.md` | GOV.UK step-by-step navigation and start pages | wayfinding | One ordered list of steps visible from every page in the journey, with "you are here" and explicit "and/or" branches |
| `ux-wikipedia-newcomer-homepage.md` | Wikipedia Growth features: newcomer homepage, suggested edits, mentor | onboarding | A single home to return to: next small task, a named person to ask, evidence of your effect |
| `ux-stripe-docs.md` | Stripe Docs and the 2016 interactive walkthrough | wayfinding | The page notices you did the step and advances; examples carry the reader's own context |
| `ux-pudding-scrollytelling.md` | The Pudding's published scrollytelling method | explainer | Animate only where the change is the point; hook, point, exit |
| `ux-owid-grapher.md` | Our World in Data Grapher and Explorers | explainer | Same data, several views, controls that belong to the current view; URL carries the exact state |
| `ux-nyt-you-draw-it.md` | NYT Upshot "You Draw It" and its evaluations | explainer | Ask for a guess before the reveal; the explanation step carries most of the effect |
| `ux-explorable-explanations.md` | Bret Victor's essay; Nicky Case's "Evolution of Trust" | explainer | One mechanic the reader can push on, introduced before the explanation; words separate from code |
| `ux-distill.md` | Distill.pub's survey of interactive articles and its hiatus | explainer | Details on demand; static reading complete on its own; the build cost is the bottleneck |
| `ux-zooniverse-classify.md` | Zooniverse classify page and tutorial-beside-the-task | recruiting | First task is real and easy; tutorial sits beside the work; one place to go when stuck, one when done |
| `ux-github-good-first-issues.md` | GitHub "good first issues" and its evaluation | recruiting | A first task is labelled, small, fully described, and attached to support; half go unsolved by newcomers anyway |
| `ux-duolingo-onboarding.md` | Duolingo delayed sign-up | onboarding | Do the real thing before being asked for anything; "not now" is quiet and repeated before "must" |
| `ux-snapchat-2018-redesign.md` | Snapchat 2018 redesign (counterexample) | wayfinding | A tidy conceptual map that moves learned locations and removes order cues loses frequency of return |

Not covered (time): a museum or transit web-wayfinding case with a published award write-up; a civic recruiting page (mySociety "Get involved", Code for America Brigade); Mozilla's contribute pages. The GOV.UK start-page discovery posts were only retrieved as excerpts.

## Five patterns that recur across the set (facts observed, not advice)

1. **Position is shown, not assumed.** GOV.UK marks current and next steps on every page of a journey; Stripe's walkthrough advances when the reader acts; Zooniverse's redesign added a defined "after" with counts and next projects; Wikipedia's homepage is the place a newcomer returns to. (Sources in the respective files.)
2. **The first act is small, real, and comes before any commitment.** Duolingo places a lesson before sign-up (about 20% DAU lift reported); Zooniverse/Gravity Spy makes the first classification real work on easy images; GitHub labels small first issues; Wikipedia's suggested edits are filtered by difficulty and interest.
3. **Guidance sits beside the task, not in front of it.** Zooniverse moved the tutorial into a tab next to the image; Wikipedia's help panel travels with the edit; Distill's "details on demand"; Stripe's collapsibles and checklists.
4. **Interaction is used where the change is the content, and the static reading still stands.** The Pudding stacks static charts when transitions carry no meaning; Victor's test of whether interaction is part of the argument; Distill records that only a fraction of readers interact and that evaluation is thin; You Draw It's effect depends on the explanation step, not the drawing alone.
5. **Makers publish the research and the known failures with the pattern.** GOV.UK's pattern page lists known issues and when not to use it; Wikipedia publishes which module did not move edits (help panel); GitHub's coverage figures (40% to 70%); Distill's own hiatus post names cost; Snap's 10-Q names the redesign as the cause of lost DAUs.
