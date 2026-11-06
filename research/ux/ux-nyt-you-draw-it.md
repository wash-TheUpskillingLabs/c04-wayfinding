# UX case: The New York Times "You Draw It", predict first, then see the data
**Kind:** explainer
**Recognition:** The pattern was taken up as a research object: a CHI 2017 Best Paper (Kim, Reinecke, Hullman) built its study on it, a statistics methods paper (Robinson, Howard, VanderPlas) adapted it as a testing tool, and Distill's 2020 survey of interactive articles cites it as the canonical "prompting self-reflection" example. Sources below.
**Logged:** 2026-11-06

## What it is and who made it
A 2015 Upshot interactive in which readers draw their expectation of a trend on an empty chart before the actual line is revealed; the first used parental income and college attendance ([Kim, Reinecke & Hullman, CHI 2017, PDF](https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf); [Robinson, Howard & VanderPlas](https://unl-statistics.github.io/stat349/instructions/methods-papers/Eye-Fitting-Straight-Lines-in-the-Modern-Era.html)). The NYT page itself could not be fetched for this file (site blocked), so the interface description comes from the research papers that reproduce it.

## What it does well (specific, observable design decisions)
- **Prediction before reveal.** The reader commits a guess, then is shown the real line with accuracy feedback; the CHI paper calls it a rare example of asking readers to draw expectations before showing data ([Kim et al., 2017](https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf)).
- **Freehand line in a bounded region.** The research adaptation has participants draw inside a highlighted band on a D3 scatterplot, unconstrained to straight lines, so curvature can be observed ([Robinson et al.](https://unl-statistics.github.io/stat349/instructions/methods-papers/Eye-Fitting-Straight-Lines-in-the-Modern-Era.html)).
- **The gap is the lesson.** Distill lists the pattern under "prompting self-reflection": prediction prompts encourage self-explanation, which supports recall ([Hohman et al., Distill 2020](https://distill.pub/2020/communicating-with-interactive-articles/)).

## Where it fails or was criticized (sourced)
- Prediction alone is weaker than prediction plus explanation: in the CHI study, Predict-Only reduced recall error least among the techniques, and on the low-familiarity replication it had no effect ([Kim et al., 2017](https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf)).
- On high-familiarity data (fast-food calories) no technique helped ([Kim et al., 2017](https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf)).
- Participants anchor slightly to their own predictions; with text presentation, prediction had no effect ([Kim et al., 2017](https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf)).
- Drawn lines are systematically biased: people fit closer to the principal-axis line than to least squares, most strongly on noisy data, and the authors note mouse-to-screen indirection as a possible cause ([Robinson et al.](https://unl-statistics.github.io/stat349/instructions/methods-papers/Eye-Fitting-Straight-Lines-in-the-Modern-Era.html)).

## Measured effects, if any (sourced)
- CHI 2017, 373 analysed Mechanical Turk participants, nine between-subject conditions: with visual presentation, Predict-Explain cut absolute recall error by about 4.1 percentage points versus baseline, Predict-Feedback and Explain-Only by about 3.5, Predict-Only by about 2.3; only Predict-Explain and Predict-Feedback reduced trend error ([Kim et al., 2017](https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf)).
- Robinson et al.: 35 participants, 131 plots, data collected May 2021 ([Robinson et al.](https://unl-statistics.github.io/stat349/instructions/methods-papers/Eye-Fitting-Straight-Lines-in-the-Modern-Era.html)).

## What we can borrow without copying (patterns, not visuals)
- Ask for a guess before showing the answer; show the gap, not just the answer.
- Pair the reveal with a one-line "why" prompt; the explanation step carries most of the effect.
- Expect it to work on unfamiliar material and to do nothing on material people already know.

## Sources
- [Explaining the Gap: Visualizing One's Predictions Improves Recall and Comprehension of Data (PDF)](https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf), Kim, Reinecke, Hullman, CHI 2017. Peer-reviewed study; Best Paper per [IDL page](https://idl.uw.edu/papers/explaining-the-gap).
- [Eye Fitting Straight Lines in the Modern Era](https://unl-statistics.github.io/stat349/instructions/methods-papers/Eye-Fitting-Straight-Lines-in-the-Modern-Era.html), Robinson, Howard, VanderPlas, course mirror of a methods paper (year not stated on page). Adapts You Draw It as a test instrument.
- [Communicating with Interactive Articles](https://distill.pub/2020/communicating-with-interactive-articles/), Hohman, Conlen, Heer, Chau, Distill, 11 Sep 2020. Cites the pattern as the self-reflection example.
