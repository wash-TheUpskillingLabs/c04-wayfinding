# Colour on the Journey Map, for Colour-Blind Readers

About 1 in 12 men and 1 in 200 women have some form of colour vision deficiency, mostly red–green. A map that leans on colour fails them first. This note records how the journey map's colours were chosen in November 2026, with the numbers, so the next change can be checked the same way. A first pass picked colours by science alone (indigo, wine, grey); they passed every test and looked wrong for the pod, so the second pass draws only from the pod's own palette and follows the Metro's line colours.

## Method

- **Simulation.** Each colour was run through the Machado, Oliveira and Fernandes (2009) model of colour vision deficiency at full severity, for protanopia, deuteranopia and tritanopia, using the `colorspacious` Python library.
- **Difference.** Every pair of colours was compared in CAM02-UCS, a colour space where distance tracks how different two colours look. On lines this thick, a difference under about 10 is hard to see; the original set had a pair at 7.8.
- **Contrast.** Each line colour was checked against the paper (`#e5e7de`) for WCAG 2.2's 3:1 minimum for graphics (success criterion 1.4.11, non-text contrast).
- **Search.** The pod's blue and red are fixed by the sign system, and ink is the station colour. Candidates were every green, yellow, orange and silver in the [Swiss Style Color Picker](https://fabianburghardt.de/swisscolors/)'s eighteen schemes, the palette the pod's scheme 14 comes from, standing in for the Metro's Green, Yellow, Orange and Silver lines. The search kept the set whose smallest difference between lines, across normal vision and all three deficiencies, was largest. Every orange fell under 9 against our red under deuteranopia, so the Orange line has no place on our maps.

## Result

| Role | First set | Now | Swiss scheme | Contrast with paper |
|---|---|---|---|---|
| Your line (brand blue) | `#0098d8` | unchanged | 14 | 2.6:1 |
| Pod A (Metro Green) | indigo `#4a45d3` | green `#007500` | 11 | 4.7:1 |
| Pod C (Metro Yellow) | wine `#8a3274` | yellow `#e6c700` | 11 | 1.3:1 |
| A proposal not chosen (Metro Silver) | grey `#898081` | silver `#a5a6a9` | 3 | 2.0:1 |
| Leaves; You Are Here (brand red) | `#f54123` | unchanged | 14 | 3.0:1, and always dotted or a ring |

Scheme 11 is red, yellow, green and blue, very nearly the Metro's own set. Smallest difference between any two lines, in any of the four kinds of vision: **7.8** in the original set, **17.6** in the first pass, **21.0** now (pod C against red, under deuteranopia).

One pair is told apart by form, not colour: under protanopia our green and our red sit only 3.1 apart. Red never appears as a solid line on the map, only as a dotted drop ending in a hollow ring, or a ring around where you are, so a protanope never has to tell a green line from a red one by colour. `tools/colourcheck.py` prints this pair separately.

## Never Colour Alone

Colour is the last clue, not the only one. On the journey map:

- lines are flat colour with no outline, as on the Metro map, which runs its pale Yellow and Silver lines on white the same way. An ink casing was tried and dropped: it made the map read as a diagram rather than the Metro. Yellow, silver and blue fall under WCAG's 3:1 for graphics, so the map never asks colour alone to carry a line; the cues below do, and every line is also named in text;
- each pod's line carries a letter in a disc, as Metro's service discs do;
- lines keep a fixed top-to-bottom order everywhere;
- planned things are dashed, leaving is a dotted line ending in a ring, and a proposal that wasn't chosen ends in a terminus bar;
- small text is always ink, never coloured.

## To Check a New Colour

Run the same simulation and keep every pair at 15 or more in CAM02-UCS under all four kinds of vision, and keep a second cue (a letter, an order, a label) for any line under 3:1 against paper. Run `python3 tools/colourcheck.py` to print these numbers for the current colours.

Sources: [Machado et al. 2009](https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html), [colorspacious](https://colorspacious.readthedocs.io/), [WCAG 2.2, 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [Colour Blind Awareness](https://www.colourblindawareness.org/colour-blindness/).
