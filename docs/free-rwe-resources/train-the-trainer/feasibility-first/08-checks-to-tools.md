# Appendix: Which OHDSI Tool Answers Each Check

*Reference. Not part of the 30-minute clock.*

Each feasibility check on the [checklist](06-feasibility-checklist.md) is answered by a specific tool in the OHDSI stack, or by a conversation with your data steward. This appendix maps them, using the same numbering as the checklist.

## The mapping

| # | Feasibility check | Primary tool | What you do with it |
|:--|:--|:--|:--|
| 1 | Concepts exist (and are standard) | **Athena** and **ATLAS → Search** | Search the vocabularies; confirm a standard concept, its domain, and its class before you build anything |
| 2 | Concepts are present in the data | **Achilles** and **ATLAS concept set → Included Concepts** | Achilles profiles record and person counts per concept in a source; the concept set panel shows what your rules resolve to, with those counts |
| 3 | Population fits | **Achilles** (age, sex, and observation profiles), shown in **ATLAS → Data Sources** | Read the age and sex distribution and the domain reports for the source; the domain reports show which kinds of records a source holds |
| 4 | Time can be anchored | **ATLAS → Cohort Definition**, then **Cohort Diagnostics** | Define the index event and windows; Cohort Diagnostics breaks down index-event timing and observation time |
| 5 | Outcome is capturable | **ATLAS → Search** counts for the outcome concepts, and your data steward | Check that the outcome is recorded as structured data in this type of source and in which domain; for the ALSFRS-R, count the records and ask where the scores are kept |
| 6 | Sample size is sufficient | **ATLAS cohort generation** (attrition), then **Cohort Diagnostics** (incidence, cohort counts) | Generate to see counts and attrition locally; Cohort Diagnostics is a common check before a network study |
| 7 | Governance clears | Your data steward, the IRB, and any data use agreement | Governance is a question for people and policy, not for a tool |

Data quality is a separate question that runs alongside these checks. The **Data Quality Dashboard (DQD)** reports whether the CDM meets a set of conformance, completeness, and plausibility checks, which informs how much weight to put on the counts you see.

## Notes on the workhorses

**Achilles** is the one that answers the most feasibility questions before you build anything. It is a characterization run over a data source that produces counts by domain, concept, age, sex, and calendar time. If your steward has run it and can show you the results, checks 2 and 3 can often be answered from those reports.

**Cohort Diagnostics** is the bridge from a single-site feasibility check to a network study. It runs a battery of diagnostics on one or more cohort definitions (incidence, index-event breakdown, cohort characterization, concept overlap) and is commonly reviewed before a network study is distributed. When you are ready to move from "feasible here" to "feasible across the network", this is the tool.

**The Data Quality Dashboard (DQD)** does not tell you whether your question is answerable. It reports whether the CDM passes a library of data quality checks. A source can contain your population and still fail checks that would undermine the study, so read the DQD results for the tables your question uses. DQD is not a governance tool, and it does not compare your counts with outside benchmarks.

## How this connects to the curriculum

- Concept and vocabulary work (checks 1–2): [Day 1 · OMOP CDM](../modules/day-01-omop-cdm.md) and [Day 2 · Vocabulary & Data Quality](../modules/day-02-vocab-dqd.md).
- Cohort definition and characterization (checks 4 to 6): [Day 3 · Cohort Definition](../modules/day-03-cohorts.md).
- Network execution with HADES/Strategus (check 6 at scale): [Day 6 · HADES](../modules/day-06-hades.md).

The daily curriculum teaches each of these tools in depth. This module's contribution is the discipline of reaching for them in the right order, before a protocol exists, so a dead end costs minutes instead of months.
