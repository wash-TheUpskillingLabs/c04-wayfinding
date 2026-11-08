# Colour on the Journey Map, for Colour-Blind Readers

About 1 in 12 men and 1 in 200 women have some form of colour vision deficiency, mostly red–green. A map that leans on colour fails them first. This note records how the journey map's colours were chosen in November 2026, with the numbers, so the next change can be checked the same way.

## Method

- **Simulation.** Each colour was run through the Machado, Oliveira and Fernandes (2009) model of colour vision deficiency at full severity, for protanopia, deuteranopia and tritanopia, using the `colorspacious` Python library.
- **Difference.** Every pair of colours was compared in CAM02-UCS, a colour space where distance tracks how different two colours look. On lines this thick, a difference under about 10 is hard to see; the original set had a pair at 7.8.
- **Contrast.** Each line colour was checked against the paper (`#e5e7de`) for WCAG 2.2's 3:1 minimum for graphics (success criterion 1.4.11, non-text contrast).
- **Search.** The pod's blue and red are fixed by the sign system, and ink is the station colour. Candidate colours were drawn from a grid in CIECAM02, red and orange hues were excluded because red means a position on our maps, and the search kept the set whose smallest difference, across normal vision and all three deficiencies, was largest.

## Result

| Role | Before | After | Contrast with paper |
|---|---|---|---|
| Your line (brand blue) | `#0098d8` | unchanged | 2.6:1, cased in ink |
| Pod A | green `#00a160` | indigo `#4a45d3` | 5.5:1 |
| Pod C | violet `#7b4fa0` | wine `#8a3274` | 6.0:1 |
| A proposal not chosen | silver `#9aa3a6` | grey `#898081` | 3.1:1 |
| Leaves; You Are Here (brand red) | `#f54123` | unchanged | 3.0:1, and always dotted or a ring |

Smallest difference between any two map colours, in any of the four kinds of vision: **7.8 before** (your blue against pod A's green, under tritanopia), **17.6 after** (pod A against pod C, under protanopia).

## Never Colour Alone

Colour is the last clue, not the only one. On the journey map:

- every coloured line has a 1.5-pixel ink casing, so its edge clears 3:1 against the paper even where the fill doesn't, as Metro maps use keylines;
- each pod's line carries a letter in a disc, as Metro's service discs do;
- lines keep a fixed top-to-bottom order everywhere;
- planned things are dashed, leaving is a dotted line ending in a ring, and a proposal that wasn't chosen ends in a terminus bar;
- small text is always ink, never coloured.

## To Check a New Colour

Run the same simulation and keep every pair at 15 or more in CAM02-UCS under all four kinds of vision, with at least 3:1 against paper or an ink casing. Run `python3 tools/colourcheck.py` to print these numbers for the current colours.

Sources: [Machado et al. 2009](https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html), [colorspacious](https://colorspacious.readthedocs.io/), [WCAG 2.2, 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [Colour Blind Awareness](https://www.colourblindawareness.org/colour-blindness/).
