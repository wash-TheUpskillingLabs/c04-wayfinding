# UX case: Our World in Data Grapher, one chart grammar and the "explorer" pattern
**Kind:** explainer
**Recognition:** Grapher powers almost every chart on Our World in Data, a site whose charts are embedded and cited across media and education; the makers published a redesign write-up (2023) and keep the code public. No award located for the chart tool itself. Sources below.
**Logged:** 2026-11-06

## What it is and who made it
Grapher is Our World in Data's client-side charting library; chart configurations and data live in one database so that charts update when data changes, and the organisation runs one codebase for all charts to keep them consistent and changeable at scale ([owid-grapher README](https://github.com/owid/owid-grapher)). An **Explorer** is a Grapher-based tool for more complex interfaces, configured in the admin client ([owid-grapher README](https://github.com/owid/owid-grapher)); the COVID-19 Data Explorer added a sort-by dropdown (population density, age, GDP, hospital beds), region aggregates, and a "hide controls" chromeless embed in mid-2020 ([OWID, June & July 2020 product updates](https://ourworldindata.org/whats-new-june-july-2020)). The 2023 redesign was written up by Marwa Boukarim, Christian Swinehart and Sophia Mersmann ([Redesigning our interactive data visualizations, 18 Oct 2023](https://ourworldindata.org/redesigning-our-interactive-data-visualizations)).

## What it does well (specific, observable design decisions)
- **Three views of the same data, each with only its own controls.** Chart / map / table buttons sit top-left; each view's settings appear top-right and show only what applies to that view ([OWID redesign, 2023](https://ourworldindata.org/redesigning-our-interactive-data-visualizations)).
- **Tables that read.** Higher row contrast, consistent alignment, sortable columns, summary statistics for a chosen year range ([OWID redesign, 2023](https://ourworldindata.org/redesigning-our-interactive-data-visualizations)).
- **Sources made prominent.** A "Learn more about this data" overlay; the stated reason is that the statisticians and institutions producing the data need recognition to keep producing it ([OWID redesign, 2023](https://ourworldindata.org/redesigning-our-interactive-data-visualizations)).
- **Share links reproduce the exact configuration**, with previews that match ([OWID redesign, 2023](https://ourworldindata.org/redesigning-our-interactive-data-visualizations)).
- **Features built to apply across all tools**, not to one chart; the chromeless embed exists for hosts with limited space ([OWID product updates, 2020](https://ourworldindata.org/whats-new-june-july-2020)).
- **One grammar, one database.** Rationale: consistency at scale, long-lived visualisations that stay current, and no dependence on external services that may shut down ([owid-grapher README](https://github.com/owid/owid-grapher)).

## Where it fails or was criticized (sourced)
- The repository is public but **not open source**: it is no longer under MIT, external pull requests are not accepted, and reuse needs written permission; the README also says the code is not designed for reuse as a library ([owid-grapher README](https://github.com/owid/owid-grapher)).
- The redesign post states no formal design principles and reports no user research or metrics; it invites feedback calls instead ([OWID redesign, 2023](https://ourworldindata.org/redesigning-our-interactive-data-visualizations)).

## Measured effects, if any (sourced)
- None published in the sources opened.

## What we can borrow without copying (patterns, not visuals)
- Same data, several views, and controls that belong to the view you are in.
- A URL that carries the exact state so a shared link lands the next person where you were.
- Credit the source of every number, visibly, as a design element.
- Build the small set of features once and let every page use them.

## Sources
- [Redesigning our interactive data visualizations](https://ourworldindata.org/redesigning-our-interactive-data-visualizations), Our World in Data, 18 Oct 2023. Makers' redesign write-up.
- [June & July 2020 product updates](https://ourworldindata.org/whats-new-june-july-2020), Our World in Data, 24 Jul 2020. Explorer feature notes.
- [owid/owid-grapher](https://github.com/owid/owid-grapher), GitHub, undated. README: purpose, licence, Explorer definition.
