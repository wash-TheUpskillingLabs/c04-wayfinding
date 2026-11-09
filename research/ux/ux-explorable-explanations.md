# UX case: Explorable Explanations (Bret Victor) and "The Evolution of Trust" (Nicky Case), play first, then explain
**Kind:** explainer
**Recognition:** Victor's 2011 essay named the genre; Case's 2017 piece was covered by Kotaku and Kotaku Australia on release, has about 45 fan translations, and its repository has about 6.3k GitHub stars. Sources below. No formal award located for either.
**Logged:** 2026-11-06

## What it is and who made it
Bret Victor's essay (10 March 2011, postscript February 2024) argues that text should be an environment for thinking rather than information to consume, and describes three forms: **reactive documents** (prose with embedded adjustable models), **explorable examples** (interactive demonstrations where the interactivity is part of the explanation, not a side sandbox), and **contextual information** (look things up without losing your place) ([Victor, Explorable Explanations](http://worrydream.com/ExplorableExplanations/)). Nicky Case's *The Evolution of Trust* (2017) is an interactive guide to the game theory of cooperation that uses a prisoner's-dilemma-like game to explain the Christmas truce and the decline of trust, then adds mistakes and repeated interaction ([Wikipedia, Nicky Case](https://en.wikipedia.org/wiki/Nicky_Case)); it is dedicated to the public domain under CC0 ([ncase/trust README](https://github.com/ncase/trust)).

## What it does well (specific, observable design decisions)
- **Models are visible, so claims can be checked.** Victor: making the model visible forces the author to be transparent and lets readers examine and refute weak reasoning; readers weigh curiosity against effort, so lowering effort invites more questions ([Victor, 2011](http://worrydream.com/ExplorableExplanations/)).
- **Interactivity inside the argument, not beside it.** Victor's digital-filter example shows how varying parameters builds intuition and exposes approximations the author did not mention ([Victor, 2011](http://worrydream.com/ExplorableExplanations/)).
- **Play before the lesson, with a single mechanic.** Case's piece is one game (cooperate or cheat) whose rules are extended chapter by chapter; the text layer is about 3,300 words in a single `words.html` file, separate from the code ([ncase/trust README](https://github.com/ncase/trust)).
- **Built to be copied.** CC0 licence, a documented translation procedure (claim an issue, fork with a `gh-pages` branch, translate three HTML files, email the author), and a list of translations on the live page ([ncase/trust README](https://github.com/ncase/trust); [ncase.me/trust](https://ncase.me/trust/)).
- **Plain stack.** PIXI.js, Howler.js, Tween.js, Balloon.css and a handwritten font; no framework ([ncase/trust README](https://github.com/ncase/trust)).

## Where it fails or was criticized (sourced)
- Victor's own 2024 postscript: the term has come to mean any article with interactive graphics, whereas he meant persuasive arguments backed by editable models; he has since moved toward physical, spatial environments ([Victor, 2011/2024](http://worrydream.com/ExplorableExplanations/)).
- Case's piece carries no published design write-up or play counts in the sources opened; the README lists resources only ([ncase/trust README](https://github.com/ncase/trust)). The live page's content loads via script and could not be described from a fetch ([ncase.me/trust](https://ncase.me/trust/)).
- The genre's cost problem is documented separately by Distill (see `ux-distill.md`).

## Measured effects, if any (sourced)
- None published for either work in the sources opened.

## What we can borrow without copying (patterns, not visuals)
- One mechanic the reader can push on, introduced before the explanation, extended one rule at a time.
- Keep the words in one file and the behaviour in another so the piece can be translated or re-skinned.
- Release terms and a contribution path stated on the page itself.
- Victor's test: is the interaction part of the argument, or decoration?

## Sources
- [Explorable Explanations](http://worrydream.com/ExplorableExplanations/), Bret Victor, 10 Mar 2011, postscript Feb 2024. Author's essay.
- [ncase/trust](https://github.com/ncase/trust), GitHub, undated. Licence, stack, translation procedure.
- [The Evolution of Trust](https://ncase.me/trust/), Nicky Case, 2017. Live piece (metadata and translation list only retrievable).
- [Nicky Case](https://en.wikipedia.org/wiki/Nicky_Case), Wikipedia. Release-year and press coverage (Kotaku, 2017).
