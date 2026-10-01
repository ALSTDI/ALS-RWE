# Feasibility First — Instructor Kit

Materials for the "Is My Question Feasible?" exemplar module, built on the [ALS use case](../../../als-use-case.md).

## Contents

| File | What it is |
|:--|:--|
| `Feasibility-Instructor-Deck-with-Notes.pptx` | Headline-only slides for the 30-minute session, with the presenter script in the speaker notes. Plain black-and-white slides on standard layouts. |
| `Feasibility-Slide-Script.md` | The same script as a page, slide by slide. |
| `Kahoot-Quiz.csv` | A Kahoot quiz on the feasibility workflow. Kahoot's spreadsheet import uses its own template, so paste these columns into that template before importing. |

## Building the ATLAS demo cohort (do this once, before class)

This kit does not ship an importable cohort file. The concept IDs for motor neuron disease, riluzole, and the ALSFRS-R should be picked in the ATLAS vocabulary search, so that they match the vocabulary version on the instance you use.

1. Open [https://atlas-demo.ohdsi.org](https://atlas-demo.ohdsi.org) in Chrome.
2. Go to **Concept Sets** and build the sets below, each with **Descendants** checked:
    - **Motor neuron disease:** search `motor neuron disease` and add the SNOMED Condition concept (SNOMED code 37340000). Amyotrophic lateral sclerosis (concept_id 373182) is one of its descendants.
    - **Riluzole:** search `riluzole` and add the RxNorm ingredient.
    - **ALSFRS-R:** search `ALSFRS-R` and add the LOINC total score (code 82953-1), or all of the scale's concepts. If the demo vocabulary does not list them, note that and show them in [Athena](https://athena.ohdsi.org/) during the session.
3. Go to **Cohort Definitions → New Cohort** and define:
    - **Entry event:** a drug exposure from the Riluzole set, limited to the earliest event per person.
    - **Inclusion rule 1:** at least 1 condition occurrence from the Motor neuron disease set, any time before and up to the index date.
    - **Inclusion rule 2:** at least 1 ALSFRS-R record between 1 and 365 days after the index date. Use an observation or a measurement criterion to match the domain of the concepts you added.
4. Give the cohort a name (for example, "Feasibility Demo: riluzole, motor neuron disease, ALSFRS-R") and **Save**.
5. Open the **Generation** tab and **Generate** against the SynPUF source.

What to look for, and to write down with the date:

- The count after the entry event.
- The count after the motor neuron disease rule.
- The count after the ALSFRS-R rule. SynPUF is synthetic Medicare claims, and claims do not record assessment scores, so this count is expected to be zero.

These counts were not checked on the public demo when this kit was written. If the riluzole or motor neuron disease counts are too small to show a clear drop, make the entry event the motor neuron disease diagnosis and keep the ALSFRS-R rule, which shows the same lesson.

## The same check at your own site

At your own instance the ALSFRS-R count may be low for a different reason: the scores are in clinic notes. The [ALS use case](../../../als-use-case.md) page has queries that count structured ALSFRS-R records and notes that mention the scale.
