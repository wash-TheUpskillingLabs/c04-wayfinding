# UX case: Zooniverse, the classify page and tutorial-on-first-task
**Kind:** recruiting
**Recognition:** The largest citizen-science web platform (Galaxy Zoo, 2007, onward; a project builder that roughly doubled project count in its first year); the 2018 classify-interface redesign was documented by the platform's designer from a survey of about 1,200 volunteers; the tutorial-then-work pattern is studied in NSF-funded research (Crowston, Østerlund, Lee). Sources below.
**Logged:** 2026-11-06

## What it is and who made it
Zooniverse is a platform where volunteers classify images and other data for research projects; researchers build their own projects with the project builder. In June 2018 its designer, Becky Rother, published a three-part account of redesigning the classify interface, the page where the work happens ([Part one, 4 Jun 2018](https://blog.zooniverse.org/2018/06/04/whats-going-on-with-the-classify-interface-part-one/); [Part three, 11 Jun 2018](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/)). Gravity Spy, a Zooniverse project classifying LIGO detector glitches, is the test bed for a proposal to blend training with real work from the first classification ([Crowston, Østerlund & Lee, NSF PAR](https://par.nsf.gov/servlets/purl/10026452)).

## What it does well (specific, observable design decisions)
- **Research before pixels.** A site-wide audit, an audit of all 79 live projects (question word counts, answer counts, image sizes, field-guide content) to target median values, and a beta-tester survey (~1,200 responses from a ~100,000-person list) ([Part one](https://blog.zooniverse.org/2018/06/04/whats-going-on-with-the-classify-interface-part-one/)).
- **Tutorial opens once, then lives in a tab beside the task** so volunteers can compare examples with the image without reopening a box that covers it ([Part three](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/)).
- **Help that stays open.** The field guide moved from a spot the scrollbar could hide to a larger toolbar button, and its modal (like keyboard shortcuts, favourites, metadata, "Need help?") can stay open and be dragged ([Part three](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/)).
- **Layout templates by subject shape.** Wide images get the toolbar below; tall images keep the task box fixed while the image scrolls ([Part three](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/)).
- **A defined "after".** A statistics section under the classifier with your past classifications, personal and community counts, links to similar projects and to Talk; a tentative "done for today" step offering to share or find another project. Rationale from the survey: project-wide stats ranked most important, and volunteers felt disconnected from research teams ([Part three](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/)).
- **First task is real work, chosen to be easy.** Gravity Spy shows newcomers a reduced interface (two classes plus "none of the above") on images a model is highly confident about, and advances them as they succeed; a simulation reaches the 0.95 mastery threshold after about 3–4 classifications ([Crowston et al.](https://par.nsf.gov/servlets/purl/10026452)).

## Where it fails or was criticized (sourced)
- Survey findings on the old interface: no clear destination when unsure how to complete a task; too many different destinations after finishing; too much scrolling and mouse movement; keyboard shortcuts existed but nobody knew; one volunteer called the classifier a "carpal-tunnel torturing device" ([Part one](https://blog.zooniverse.org/2018/06/04/whats-going-on-with-the-classify-interface-part-one/); [Part three](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/)).
- Crowston et al. is a proposal, not a results paper; whether trained volunteers perform better and contribute more is left open ([Crowston et al.](https://par.nsf.gov/servlets/purl/10026452)).

## Measured effects, if any (sourced)
- None published for the redesign in the posts opened; the 2018 posts describe the changes as "coming soon" with completion expected early 2019 ([Part three](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/)).

## What we can borrow without copying (patterns, not visuals)
- Make the first task real and easy, and let the tutorial sit beside the work rather than in front of it.
- Give one obvious place to go when stuck, and one obvious place to go when done.
- Show the person their own count and the community's count on the same screen.
- Audit what the real content looks like (lengths, sizes) and design for the median.

## Sources
- [What's going on with the classify interface? Part One](https://blog.zooniverse.org/2018/06/04/whats-going-on-with-the-classify-interface-part-one/), Becky Rother, Zooniverse blog, 4 Jun 2018. Designer's write-up: audits and survey.
- [What's going on with the classify interface? Part three](https://blog.zooniverse.org/2018/06/11/whats-going-on-with-the-classify-interface-part-three/), Becky Rother, Zooniverse blog, 11 Jun 2018. Designer's write-up: decisions.
- [Blending Machine and Human Learning Processes](https://par.nsf.gov/servlets/purl/10026452), Crowston, Østerlund, Lee, NSF Public Access Repository, c. 2016–17. Proposal for tutorial-as-real-work.
