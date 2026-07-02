# Vocabulary and CDM Essentials

*Segment 3 · 14–18 minutes*

You do not need to master the OMOP CDM to assess feasibility. You need enough of the vocabulary model to answer two questions: does a standard concept exist for the thing I care about, and is it actually present in the data. This page gives you that much, oriented toward feasibility. For the full treatment, see [Day 1 · OMOP CDM](../modules/day-01-omop-cdm.md) and [Day 2 · Vocabulary & Data Quality](../modules/day-02-vocab-dqd.md).

## The CDM in one paragraph

The OMOP Common Data Model reshapes any source data (an EHR, a claims feed) into a fixed set of tables with a fixed meaning. People live in the `PERSON` table. Their coverage over time lives in `OBSERVATION_PERIOD`. Clinical events are sorted by type into domain tables: diagnoses go to `CONDITION_OCCURRENCE`, medications to `DRUG_EXPOSURE`, labs and vitals to `MEASUREMENT`, procedures to `PROCEDURE_OCCURRENCE`, and everything else to `OBSERVATION`. Because the shape is identical at every site, a cohort definition written once runs unchanged everywhere. That portability is the whole reason the network exists.

## Concepts, standard and non-standard

Every clinical idea in OMOP is a **concept** with a numeric `concept_id`. The critical distinction for feasibility is standard versus non-standard.

- A **standard concept** is the one canonical representation OMOP uses for a clinical idea. Conditions are standardized to SNOMED CT, drugs to RxNorm and its extension, measurements largely to LOINC. When you build a cohort, you build it from standard concepts.
- A **non-standard (source) concept** is a code from the original source, such as an ICD-10-CM diagnosis or an NDC drug code. These are mapped to standard concepts through the vocabulary's "Maps to" relationships during ETL.

Why this matters for feasibility: your source might record diabetes as an ICD-10-CM code, but you query for the SNOMED standard concept. If the ETL mapped ICD-10 to SNOMED correctly, your query finds those people. If a code was left unmapped, those records are invisible to a standard-concept query even though the information is sitting in the source. That is why "what is the unmapped rate?" is a steward question, not a technicality.

## Domains decide where to look

A concept belongs to a **domain**, and the domain tells you which table holds its records. Check it before you count:

| Idea | Domain | Table |
|:--|:--|:--|
| Preeclampsia | Condition | `CONDITION_OCCURRENCE` |
| Metformin, insulin | Drug | `DRUG_EXPOSURE` |
| Hemoglobin A1c | Measurement | `MEASUREMENT` |
| Pregnancy / gestational age | Observation or Measurement | depends how it was recorded |

If you look for a drug in the condition table you will find nothing and wrongly conclude the data is missing. Always confirm the domain first.

## Concept sets and hierarchies

You rarely want a single concept. "Type 2 diabetes mellitus" has dozens of more specific descendants. OMOP vocabularies are hierarchical, so you can select a parent concept and include its descendants in one move. A **concept set** is a named, reusable bundle of concepts plus rules like "include descendants" or "exclude" a branch. You will build concept sets in ATLAS for diabetes, pregnancy, preeclampsia, metformin, and insulin, and reuse them across every cohort.

## The three checks this primer enables

When you open ATLAS in the next section, you are looking for exactly three things:

1. **Existence.** Search returns a standard concept for your idea, in the expected domain.
2. **Standard status.** The concept is marked standard, so a cohort query will use it directly.
3. **Presence and count.** The concept has a nonzero record count in this data source, and enough of it to matter.

!!! note "Keep two ideas apart and most confusion disappears"
    **Existence** is a property of the vocabulary and is the same everywhere. **Presence and count** are properties of the specific instance and are the whole game. A concept can exist in the vocabulary and appear zero times in your data.

## Terms you will hear, briefly

- **Phenotype** — the definition that identifies people with a condition or characteristic from CDM data. A cohort definition is an executable phenotype.
- **Cohort** — the set of people who meet a phenotype's entry and qualifying rules over specified time.
- **Achilles** — a tool that profiles a data source: counts by domain, concept, age, and so on.
- **Vocabulary version** — the dated release of the OMOP vocabularies loaded in your instance. Two instances on different versions can map the same source code differently.
