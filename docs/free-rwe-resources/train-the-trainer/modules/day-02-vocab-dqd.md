# Day 2 · Concept Sets and Data Quality

!!! abstract "Objectives"
    By the end of Day 2 you will be able to:

    1. Explain what a concept set is and why it is the reusable building block for analysis.
    2. Read the "standard" and "mapped" fields and say why they matter.
    3. Describe the Kahn framework categories for data quality (conformance, completeness, plausibility).
    4. Describe what the Data Quality Dashboard (DQD) checks and how thresholds are used.
    5. Tell the difference between a true data quality problem and a concept set or cohort definition problem.

Day 2 has two halves. The first is **data quality**, the discipline of deciding whether the data are fit for the question you want to ask. The second is **concept sets**, the reusable lists of standard concepts that every cohort and analysis is built from.

---

## Part 1: Data quality

### Why it comes first
Source data are collected for care and billing, not research. Before any analysis you need a structured way to ask whether the data can support your question. The OHDSI community uses the Kahn framework as that structure.

### The Kahn framework
The framework sorts data quality checks into three intrinsic categories, each of which can be assessed against the data alone or in the context of a specific study:

- **Conformance:** do values follow the expected format, type, and relational rules? (For example, is every `drug_concept_id` a valid concept in a Drug domain?)
- **Completeness:** are values present where you expect them? (For example, what fraction of condition records have a valid, non-zero concept?)
- **Plausibility:** are the values believable? (For example, are there birth dates in the future, or drug eras that start before birth?)

### The Data Quality Dashboard (DQD)
DQD operationalizes the Kahn framework. It runs a large library of checks against an OMOP CDM and reports each as a pass or fail against a **threshold**. A threshold is the tolerance you accept (for example, "no more than 5 percent of `condition_occurrence` rows may have a concept_id of 0"). Thresholds are defaults you can adjust to your data and your study.

A useful habit: run DQD early, read the failures, and decide which ones actually threaten your analysis. Not every failed check is fatal, and a passing dashboard does not guarantee the data answer your question.

### Data quality, or your concept set?
A recurring lesson is that an unexpected result is often not a data problem at all. It is frequently a concept set that is too narrow, too broad, or built on non-standard concepts. Before blaming the data, confirm that your concept set captures what you intended. That is the bridge into Part 2.

---

## Part 2: Concept sets

### What a concept set is
A concept set is a named, reusable collection of standard concepts that defines a clinical idea, for example "all sulfonylureas" or "type 2 diabetes." You build it once and reuse it in concept set expressions, cohort entry events, inclusion rules, and characterization.

### The power of descendants
A concept set entry can include descendants. Selecting the ingredient "sulfonylureas" with "include descendants" pulls in every product and dose below it in the hierarchy, so you do not have to list each one. This is what makes concept sets robust to the specific codes recorded in any one site's data.

### Standard and mapped
Two fields decide whether a concept set behaves correctly:

- **Standard:** analyses run on standard concepts. A concept set built on non-standard source codes will silently miss data.
- **Mapped:** the "mapped" view shows which source codes map into your standard concepts, which is how you confirm coverage and spot gaps.

### Building concept sets in Atlas
Atlas is the graphical interface for this work. You search Athena vocabularies, add concepts to a set, toggle descendants and mapped, and then reuse the set across cohorts. The Day 2 lab walks through building several concept sets and validating them.

---

## Slides and materials

| File | Description |
|:--|:--|
| [Instructor Deck](../training/day-02-vocab-dqd/kit/Instructor-Deck-with-Notes.pptx) | Full slide deck with speaker notes |
| [Participant Workbook](../training/day-02-vocab-dqd/kit/Participant-Workbook.pptx) | Workbook with fill-in exercises |
| [Kahoot Quiz](../training/day-02-vocab-dqd/kit/Kahoot-Quiz.csv) | 10-question concept sets and DQD quiz |

See the [Day 2 exercise](../exercises/day-02-vocab-dqd.md) for the hands-on lab.

## Further reading
- The Book of OHDSI, Chapter 4 (Common Data Model) and the data quality material: https://ohdsi.github.io/TheBookOfOhdsi/
- Athena vocabulary browser: https://athena.ohdsi.org/
