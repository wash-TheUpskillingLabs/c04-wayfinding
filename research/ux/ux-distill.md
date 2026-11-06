# UX case: Distill.pub, a peer-reviewed journal of interactive explanations, and its own account of why it stopped
**Kind:** explainer
**Recognition:** A registered scientific journal (ISSN 2476-0757) with a steering committee including Yoshua Bengio, Mike Bostock, Amanda Cox, Ian Goodfellow, Andrej Karpathy, Shakir Mohamed, Michael Nielsen and Fernanda Viégas; its 2020 article "Communicating with Interactive Articles" is the standard survey of the form. Sources below.
**Logged:** 2026-11-06

## What it is and who made it
A machine-learning research journal, 2016–2021, that published web-native articles with interactive diagrams instead of PDFs; aims included clearer explanations, new notations and visual mental models, credit for non-traditional artifacts such as playgrounds, and reducing "research debt"; editors Shan Carter and Chris Olah ([Distill, About](https://distill.pub/about/)). Its survey of the form, by Fred Hohman, Matthew Conlen, Jeffrey Heer and Duen Horng Chau (11 Sep 2020, DOI 10.23915/distill.00028), sets out five affordances and three challenges ([Communicating with Interactive Articles](https://distill.pub/2020/communicating-with-interactive-articles/)). In July 2021 the editorial team announced an indefinite hiatus ([Distill Hiatus, 2 Jul 2021](https://distill.pub/2021/distill-hiatus/)).

## What it does well (specific, observable design decisions)
The 2020 survey's five affordances, each tied to cited evidence ([Hohman et al., 2020](https://distill.pub/2020/communicating-with-interactive-articles/)):
- **Connecting people and data:** animation and unit visualisations (one mark per person).
- **Making systems playful:** sandboxed in-browser simulations with adjustable parameters, no software setup.
- **Prompting self-reflection:** prediction prompts (You Draw It), quizzes, spaced repetition.
- **Personalising reading:** content adapted to location or input; segmented, non-linear content paced by the reader.
- **Reducing cognitive load:** details-on-demand such as tooltips, expandable text, labelled illustrations.
It also reports layout evidence: slideshow layouts beat vertical scrolling for comprehension in one study (Zhi et al.), and readers preferred step or scroll layouts to static articles with no significant engagement difference between the two (McKenna et al.) ([Hohman et al., 2020](https://distill.pub/2020/communicating-with-interactive-articles/)).

## Where it fails or was criticized (sourced)
- **Authoring cost.** Making an interactive article is closer to building a website than writing a post; tools are immature; funding is scarce; archiving, accessibility and cross-device performance add work ([Hohman et al., 2020](https://distill.pub/2020/communicating-with-interactive-articles/)).
- **Thin evaluation.** The survey states there is limited empirical evaluation of interactive articles' effectiveness; large publishers rarely share metrics, and a NYT observation that only a fraction of readers engage with interactives became a rule of thumb the authors say lacks context ([Hohman et al., 2020](https://distill.pub/2020/communicating-with-interactive-articles/)).
- **The journal itself burned out.** Editors cite the effort to produce articles and the rare mix of scientific and design skill as the primary bottleneck; early articles sometimes received more than 50 hours of editor help; volunteers burned out; editor-written articles created an appearance of conflict; the "credibility through journal publication" theory no longer seemed right ([Distill Hiatus, 2021](https://distill.pub/2021/distill-hiatus/)).

## Measured effects, if any (sourced)
- The hiatus post gives no article or view counts, only "positive informal comments" ([Distill Hiatus, 2021](https://distill.pub/2021/distill-hiatus/)). The survey reports few effect sizes beyond the cited studies ([Hohman et al., 2020](https://distill.pub/2020/communicating-with-interactive-articles/)).

## What we can borrow without copying (patterns, not visuals)
- Details on demand: the default page carries the least; the reader pulls more.
- Segment the piece so a reader can stop and resume without losing place.
- Budget the interactive as a build, not a post, and plan who maintains it.
- Treat "only a fraction interact" as a reason to make the static reading complete on its own.

## Sources
- [About](https://distill.pub/about/), Distill. Journal description, aims, editors, ISSN.
- [Communicating with Interactive Articles](https://distill.pub/2020/communicating-with-interactive-articles/), Hohman, Conlen, Heer, Chau, Distill 5(9), 11 Sep 2020. Peer-reviewed survey.
- [Distill Hiatus](https://distill.pub/2021/distill-hiatus/), Distill Editorial Team, 2 Jul 2021. Makers' account of stopping.
