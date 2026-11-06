# UX case: Stripe Docs, developer documentation that behaves like a guided route
**Kind:** wayfinding
**Recognition:** Widely treated as the benchmark for API documentation in developer-experience writing (e.g., API Evangelist in 2016 called the interactive walkthrough the most sophisticated advance in API docs since Swagger UI; Moesif's 2022 teardown treats it as the reference). Makers' own write-up exists for the authoring system (Markdoc, 2022). Sources below. No formal award located.
**Logged:** 2026-11-06

## What it is and who made it
Stripe's documentation site for developers integrating payments. Stripe's Docs Product team describes the docs as meant to feel like an application rather than a static manual, built on a Markdown extension (Markdoc) that Stripe open-sourced under MIT in 2022 ([Ryan Paul, Stripe engineering blog, 13 Sep 2022](https://stripe.dev/blog/markdoc)). An earlier generation (2016) was an interactive walkthrough that stepped the reader through accepting a card, creating a customer, charging, creating a plan and subscribing ([API Evangelist, 26 Aug 2016](https://apievangelist.com/2016/08/26/i-am-digging-stripes-new-interactive-api-documentation-walkthrough/index.md)).

## What it does well (specific, observable design decisions)
- **The route advances when you act.** In the 2016 walkthrough, running the curl command in a terminal and returning to the browser advanced the page to the next step; it worked without being logged in ([API Evangelist, 2016](https://apievangelist.com/2016/08/26/i-am-digging-stripes-new-interactive-api-documentation-walkthrough/index.md)).
- **Examples are personalised to the reader.** Code samples can carry the reader's own test API key, and content is conditionally shown by the reader's location or the Stripe features they use ([Stripe, Markdoc post](https://stripe.dev/blog/markdoc)).
- **Small, consistent interactive parts.** Checklists, collapsible sections and tab switchers are the client-side components; interactive diagrams are built from a few Markdoc tags and support clickable links ([Stripe, Markdoc post](https://stripe.dev/blog/markdoc)).
- **Content and code kept separate, and validated.** Markdoc content parses to an AST that is validated in CI, with editor feedback and automated refactoring; a Webpack loader is five lines ([Stripe, Markdoc post](https://stripe.dev/blog/markdoc)).
- **Three columns, code synced to prose.** Navigation, prose and runnable code side by side, with hover-highlight linking between prose and code; the left column lists product areas each with its own quickstart and topic tree ([Moesif teardown, 2022/2026](https://www.moesif.com/blog/best-practices/api-product-management/the-stripe-developer-experience-and-docs-teardown/)).

## Where it fails or was criticized (sourced)
- The Markdoc post does not discuss site navigation at all and reports no usage or outcome data ([Stripe, Markdoc post](https://stripe.dev/blog/markdoc)).
- Moesif notes the full Stripe stack is unrealistic for most teams and that the visible polish is the expensive part; that article also promotes its own product, so weigh its praise accordingly ([Moesif teardown](https://www.moesif.com/blog/best-practices/api-product-management/the-stripe-developer-experience-and-docs-teardown/)).
- The live docs home page was not fetched for this file (access required approval); observations above come from the makers' and third-party write-ups, not from direct inspection.

## Measured effects, if any (sourced)
- None published. The makers' post gives counts of pages and code size only ([Stripe, Markdoc post](https://stripe.dev/blog/markdoc)).

## What we can borrow without copying (patterns, not visuals)
- Let the page notice that the reader did the thing and move them on, rather than asking them to click "next".
- Put the reader's own context (their key, their region, their chosen path) into the example so the example is already theirs.
- Keep the vocabulary of interactive parts tiny (checklist, collapsible, tabs) and reuse it everywhere.
- Validate the content structure automatically so a long-lived guide does not quietly rot.

## Sources
- [How Stripe builds interactive docs with Markdoc](https://stripe.dev/blog/markdoc), Stripe engineering blog, 13 Sep 2022. Makers' write-up of the authoring system and docs behaviours.
- [I Am Digging Stripe's New Interactive API Documentation Walkthrough](https://apievangelist.com/2016/08/26/i-am-digging-stripes-new-interactive-api-documentation-walkthrough/index.md), API Evangelist, 26 Aug 2016. Contemporary review of the step-advancing walkthrough.
- [Stripe Developer Experience Teardown](https://www.moesif.com/blog/best-practices/api-product-management/the-stripe-developer-experience-and-docs-teardown/), Moesif, first published 11 Aug 2022, modified 2026. Third-party description of layout; vendor content.
