# UX case: Wikipedia Growth features, the newcomer homepage as a wayfinding system
**Kind:** onboarding
**Recognition:** Built and evaluated with controlled experiments by the Wikimedia Foundation's Growth team; deployed across Wikipedia language editions; results published on MediaWiki.org and by the Foundation. Sources below. (Outcomes research on the Teahouse was covered in earlier research; this file is about the interface.)
**Logged:** 2026-11-06

## What it is and who made it
A set of features for new Wikipedia editors made by the Wikimedia Foundation's Growth team: a **newcomer homepage** (a special page that hosts task modules, a named mentor, help links, an "impact" module showing pageviews on articles the newcomer edited, and prompts to confirm an email address), a **suggested edits** feed, a **help panel** shown while editing, and **mentorship** tools that match newcomers to experienced editors ([Growth/Feature summary, MediaWiki](https://www.mediawiki.org/wiki/Growth/Feature_summary)). The Foundation describes the homepage as the starting-point dashboard for new editors, and the suggested-edits feed as machine-learning-assisted recommendations of simple first tasks based on stated interests ([Wikimedia Foundation on Medium, 6 Dec 2022](https://medium.com/freely-sharing-the-sum-of-all-knowledge/new-wikipedia-editor-features-make-it-easy-for-everyone-to-contribute-e09135ce9275)).

## What it does well (specific, observable design decisions)
- **One landing place after sign-up.** The homepage collects everything a newcomer might need (tasks, mentor, help, impact) on one page rather than scattering it; most newcomers visit it and many return on later days ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)).
- **Tasks are filterable by type and by topic.** Newcomers filter suggested edits by edit type (derived from maintenance templates) and by topic (derived from ORES models) ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)).
- **Guidance travels with the task.** Once a newcomer opens an article from the feed, the help panel guides them through the edit; "structured" tasks such as "add a link" suggest the specific words to link ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)).
- **A named human is attached to the route.** The mentorship module assigns each newcomer a mentor and makes it easy to post a question on the mentor's talk page; communities opt in and set their own mentor criteria ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)).
- **Feedback on effect.** The impact module shows pageviews on the articles the newcomer edited ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)).
- **Per-community configuration.** Language editions can turn modules on or off; Portuguese and Spanish Wikipedia are given as examples of differing homepages ([WMF Medium, 2022](https://medium.com/freely-sharing-the-sum-of-all-knowledge/new-wikipedia-editor-features-make-it-easy-for-everyone-to-contribute-e09135ce9275)).

## Where it fails or was criticized (sourced)
- The help panel alone did not increase newcomer edits: about 20% of newcomers who see it open it and about half of those interact with it; it is retained because it supports the task flow ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)).
- The feature-summary page claims suggested edits are the main driver of first edits and retention but does not give numbers or dates on that page ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)). The detailed experiment-analysis pages (November 2020; "Add a link", December 2021) could not be retrieved at the time of logging; treat the exact per-experiment figures as **unverified** here.

## Measured effects, if any (sourced)
- Newcomers with the features are 16% more likely to make a first edit and to return to keep editing, from controlled experiments; since piloting began in 2019, about 700,000 edits by about 85,000 people were made with the features, and about 80,000 questions were asked of mentors ([WMF Medium, 2022](https://medium.com/freely-sharing-the-sum-of-all-knowledge/new-wikipedia-editor-features-make-it-easy-for-everyone-to-contribute-e09135ce9275)).
- As of November 2020, 14,228 mentor questions had been asked by 11,785 users; the homepage increases the share of newcomers with confirmed email addresses (no figure given) ([Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary)).

## What we can borrow without copying (patterns, not visuals)
- A single "home" that a newcomer returns to, holding the next small task, a named person to ask, and evidence of effect.
- Filter tasks by difficulty and by interest, and keep the guidance inside the task rather than on a separate help page.
- Let each local community switch modules on or off rather than shipping one fixed flow.
- Measure "first contribution" and "return" separately, and publish which module moved which.

## Sources
- [Growth/Feature summary](https://www.mediawiki.org/wiki/Growth/Feature_summary), MediaWiki.org, undated (data to Nov 2020). Team's own feature-by-feature summary with results.
- [New Wikipedia editor features make it easy for everyone to contribute](https://medium.com/freely-sharing-the-sum-of-all-knowledge/new-wikipedia-editor-features-make-it-easy-for-everyone-to-contribute-e09135ce9275), Wikimedia Foundation (Medium), 6 Dec 2022. Interview-based write-up with headline numbers.
