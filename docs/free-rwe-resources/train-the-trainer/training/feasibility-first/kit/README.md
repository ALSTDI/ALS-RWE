# Feasibility First — Instructor Kit

Materials for the "Is My Question Feasible?" exemplar module.

## Contents

| File | What it is |
|:--|:--|
| `Feasibility-Instructor-Deck-with-Notes.pptx` | The ~30-minute slide deck. Full presenter script is in the speaker notes on every slide. ALS TDI purple house palette. |
| `Demo-Cohort-Diabetes-Childbearing-Age.json` | A ready-to-import ATLAS cohort definition for the live demo. Import it into the public ATLAS demo and save it so you screen-share a saved definition instead of typing live. |
| `Kahoot-Quiz.csv` | A 10-question Kahoot quiz on the feasibility workflow. Import via Kahoot's "Add question → Import from spreadsheet". |

## Pre-building the ATLAS demo (do this once, before class)

The importable cohort is built to demonstrate the collapse cleanly on the public demo's synthetic Medicare data (SynPUF), using only concepts that are guaranteed present. It does **not** depend on obstetric concepts, which SynPUF lacks. The collapse trigger is a demographic rule: female, age 15–44 at the first diabetes record. On a 65+ Medicare population that rule empties the cohort, which is exactly the population-problem lesson.

1. Open [https://atlas-demo.ohdsi.org](https://atlas-demo.ohdsi.org) in Chrome.
2. Go to **Cohort Definitions → New Cohort**.
3. Open the **Export** tab, then the **JSON** sub-tab.
4. Paste the full contents of `Demo-Cohort-Diabetes-Childbearing-Age.json` and click **Import** (or **Reload**).
5. Give it a name (for example, "Feasibility Demo — diabetes, childbearing age") and **Save**.
6. Open the **Generation** tab and **Generate** against the SynPUF source. Confirm the counts before class.

What you should see, and narrate live:

- Diabetes alone (the entry event): a large count.
- After the female-childbearing-age inclusion rule: the attrition report drops the count to near zero.
- The optional metformin rule is there to show how an exposure arm attaches; it is not needed for the collapse.

The **attrition report** in the Generation tab is the visual you want on screen at the moment of collapse. It shows exactly how many people each rule removed.

## Concept IDs used (all verified standard concepts)

| Concept | concept_id | Vocabulary | Domain |
|:--|:--|:--|:--|
| Diabetes mellitus (+descendants) | 201820 | SNOMED | Condition |
| metformin (+descendants) | 1503297 | RxNorm | Drug |
| FEMALE | 8532 | Gender | Gender |

## The full clinical cohort (build at your own instance)

The demo cohort above is intentionally simple so it works on synthetic data. The full research question (pregestational diabetes → preeclampsia, by metformin vs insulin) needs obstetric data your institution's OMOP instance has and SynPUF does not. Build those concept sets at your instance by searching [Athena](https://athena.ohdsi.org). Suggested standard-concept searches, each with **include descendants**:

- **Preeclampsia** — search "Preeclampsia", Condition domain, SNOMED. Confirm the standard concept before use.
- **Insulin** — search "insulin", Drug domain, RxNorm ingredient level.
- **Pregnancy / delivery** — pregnancy identification needs a **pregnancy episode algorithm**, not a single code. See the OHDSI Pregnancy work; do not approximate it with one obstetric concept.

Resolve these at your instance rather than copying IDs, so the concepts match your vocabulary version.
