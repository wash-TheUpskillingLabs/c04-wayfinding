# UX case: GitHub "good first issues", labelling and recommending a newcomer's first task
**Kind:** recruiting
**Recognition:** A platform-wide convention across open source (about 300 synonymous label names curated by GitHub), a GitHub-built recommendation feature with a makers' engineering write-up (2020), and a peer-reviewed evaluation at ESEC/FSE 2020 (Tan, Zhou, Sun). Sources below.
**Logged:** 2026-11-06

## What it is and who made it
A convention in which maintainers label issues suitable for newcomers, and a GitHub feature (launched May 2019 on labels, later extended with machine learning) that recommends such issues in projects matching a newcomer's interests; written up by Tiferet Gazit, a principal ML engineer at GitHub ([How we built the good first issues feature, 22 Jan 2020](https://github.blog/open-source/maintainers/how-we-built-good-first-issues)). The label practice itself was studied across 9,368 labelled issues in 816 popular projects plus surveys of newcomers and project members ([Tan, Zhou & Sun, ESEC/FSE 2020](https://2020.esec-fse.org/details/fse-2020-papers/172/A-First-Look-at-Good-First-Issues-on-GitHub)).

## What it does well (specific, observable design decisions)
- **Accepts the vocabulary people already use.** About 300 label names ("beginner friendly", "easy bug fix", "low-hanging-fruit") are treated as synonyms; label-based detections get higher confidence than model-based ones, and documentation issues rank below beginner-tagged ones ([GitHub blog, 2020](https://github.blog/open-source/maintainers/how-we-built-good-first-issues)).
- **Does not depend on maintainers doing extra work.** The model learns from issues closed by a first-time contributor or by a small single-file pull request, so unlabelled projects still surface entry points ([GitHub blog, 2020](https://github.blog/open-source/maintainers/how-we-built-good-first-issues)).
- **Precision over recall**, because only a tiny minority of issues are good first issues ([GitHub blog, 2020](https://github.blog/open-source/maintainers/how-we-built-good-first-issues)).
- **Coverage is measured.** Labels alone surfaced easy issues in about 40% of recommended repositories; labels plus ML, about 70% ([GitHub blog, 2020](https://github.blog/open-source/maintainers/how-we-built-good-first-issues)).

## Where it fails or was criticized (sourced)
- Almost half of labelled good first issues are not solved by newcomers, and they usually take more days to resolve than ordinary issues ([Tan et al., 2020](https://2020.esec-fse.org/details/fse-2020-papers/172/A-First-Look-at-Good-First-Issues-on-GitHub)).
- The study names problems at three levels: inappropriate issues (mechanism), too few issues (project), uneven skill (newcomer); it recommends issues with informative descriptions, available support, and limited scope and skill ([Tan et al., 2020](https://2020.esec-fse.org/details/fse-2020-papers/172/A-First-Look-at-Good-First-Issues-on-GitHub)).

## Measured effects, if any (sourced)
- Coverage figures above (40% to 70% of recommended repositories) ([GitHub blog, 2020](https://github.blog/open-source/maintainers/how-we-built-good-first-issues)). No published effect on newcomer retention in the sources opened.

## What we can borrow without copying (patterns, not visuals)
- A first task is a thing you label, keep small, describe fully, and attach a person to.
- Accept many names for the same thing rather than enforcing one.
- Measure what share of places a newcomer could land actually have a visible first task.
- Expect that labelling alone does not get tasks done; support does.

## Sources
- [How we built the good first issues feature](https://github.blog/open-source/maintainers/how-we-built-good-first-issues), Tiferet Gazit, GitHub Blog, 22 Jan 2020 (updated 16 Apr 2020). Makers' write-up.
- [A First Look at Good First Issues on GitHub](https://2020.esec-fse.org/details/fse-2020-papers/172/A-First-Look-at-Good-First-Issues-on-GitHub), Tan, Zhou, Sun, ESEC/FSE 2020. Peer-reviewed evaluation (abstract page; exact rates not on page).
