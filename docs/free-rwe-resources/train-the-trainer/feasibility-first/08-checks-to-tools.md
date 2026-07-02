# Appendix: Which OHDSI Tool Answers Each Check

*Reference. Not part of the 30-minute clock.*

The six feasibility checks are not abstract. Each one is answered by a specific tool in the OHDSI stack. This appendix maps them so you know exactly where to look, and it is where the demo's habits connect to the daily curriculum.

## The mapping

| # | Feasibility check | Primary tool | What you do with it |
|:--|:--|:--|:--|
| 1 | Concepts exist (and are standard) | **Athena** and **ATLAS → Search** | Search the vocabularies; confirm a standard concept, its domain, and its class before you build anything |
| 2 | Concepts are present in the data | **Achilles** and **ATLAS concept set → Included Concepts** | Achilles profiles record and person counts per concept in a source; the concept-set panel shows what your rules resolve to |
| 3 | Population fits | **Achilles** (age/sex/observation profiles), surfaced in **ATLAS → Data Sources** | Read the age and sex distribution of the source; this is what tells you SynPUF is 65+ |
| 4 | Time can be anchored | **ATLAS → Cohort Definition**, then **Cohort Diagnostics** | Define the index event and windows; Cohort Diagnostics breaks down index-event timing and observation time; pregnancy needs a pregnancy episode algorithm |
| 5 | Sample size is sufficient | **ATLAS cohort generation** (attrition), then **Cohort Diagnostics** (incidence, cohort counts) | Generate to see counts and attrition locally; Cohort Diagnostics is the standard pre-network check across databases |
| 6 | Governance clears | **Data Quality Dashboard (DQD)** for data trust, plus institutional IRB/DUA | DQD tells you whether the data are trustworthy enough to act on; governance itself is a steward and IRB question, not a tool |

## Notes on the workhorses

**Achilles** is the one that answers the most feasibility questions before you build anything. It is a characterization run over a data source that produces counts by domain, concept, age, sex, and calendar time. If your steward has run it and can show you the results, checks 2 and 3 are often answered in a single browse.

**Cohort Diagnostics** is the bridge from a single-site feasibility check to a network study. It runs a battery of diagnostics on one or more cohort definitions (incidence, index-event breakdown, cohort characterization, concept overlap) and is the standard artifact reviewers expect before a network study is distributed. When you are ready to move from "feasible here" to "feasible across the network", this is the tool.

**The Data Quality Dashboard (DQD)** does not tell you whether your question is answerable; it tells you whether the answers can be trusted. A source can contain your population and still fail data-quality checks that would undermine the study. DQD sits behind check 6 for that reason: governance is partly about permission and partly about whether the data are fit for the purpose.

## How this connects to the curriculum

- Concept and vocabulary work (checks 1–2): [Day 1 · OMOP CDM](../modules/day-01-omop-cdm.md) and [Day 2 · Vocabulary & Data Quality](../modules/day-02-vocab-dqd.md).
- Cohort definition and characterization (checks 4–5): [Day 3 · Cohort Definition](../modules/day-03-cohorts.md).
- Network execution with HADES/Strategus (check 5 at scale): [Day 6 · HADES](../modules/day-06-hades.md).

The daily curriculum teaches each of these tools in depth. This module's contribution is the discipline of reaching for them in the right order, before a protocol exists, so a dead end costs minutes instead of months.
