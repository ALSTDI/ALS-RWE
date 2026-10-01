# Day 2 · Concept Sets and Data Quality

!!! abstract "Objectives"
    By the end of Day 2 you will be able to:

    1. Explain what a concept set is and why it is the reusable building block for analysis.
    2. Read the Included Concepts and Included Source Codes tabs of an ATLAS concept set and say what each one tells you.
    3. Use the Kahn framework's terms (category, subcategory, context) to read a DQD result, and name the parts of the framework that DQD does not check.
    4. Describe what the Data Quality Dashboard (DQD) checks and how thresholds are used.
    5. Tell the difference between a true data quality problem and a concept set or cohort definition problem.

Day 2 has two halves. The first is **data quality**, the discipline of deciding whether the data are fit for the question you want to ask. The second is **concept sets**, the reusable concept expressions that every cohort and analysis is built from.

---

## Part 1: Data quality

### Why it comes first
Source data are collected for care and billing, not research. Before any analysis you need a structured way to ask whether the data can support your question. The OHDSI Data Quality Dashboard organizes its checks with the terms of the Kahn framework, so this page introduces the framework first and then shows how much of it DQD covers.

### The Kahn framework
Kahn and colleagues (2016) proposed a harmonized vocabulary for data quality checks, made of categories and contexts.

**Categories** say what kind of expectation a check tests:

- **Conformance:** do values follow the expected format, type, and relational rules? Subcategories: value, relational, and computational conformance. (For example, is every `drug_concept_id` a concept that exists and belongs to the Drug domain?)
- **Completeness:** are values present where you expect them, whatever the values are? This category has no subcategories. (For example, what percent of condition records have a concept_id of 0?)
- **Plausibility:** are the values believable? Subcategories: uniqueness, atemporal, and temporal plausibility. (For example, are there birth years in the future, or events dated before birth?)

**Contexts** say what the data are compared with:

- **Verification** compares the data with expectations that come from the system itself: metadata, constraints, and local knowledge.
- **Validation** compares the data with a relevant external benchmark, such as a published prevalence.

### The Data Quality Dashboard (DQD)
DQD labels each of its check types with a Kahn context, category, and subcategory, and those labels appear as columns in the report. DQD fills only part of the framework:

| Kahn label | DQD check types with that label (examples) |
|:--|:--|
| Conformance, value | `cdmDatatype`, `fkDomain` |
| Conformance, relational | `cdmField`, `isPrimaryKey`, `isForeignKey`, `isRequired` |
| Conformance, computational | `fkClass` |
| Completeness | `measureValueCompleteness`, `standardConceptRecordCompleteness`, `sourceValueCompleteness`, `measurePersonCompleteness` |
| Plausibility, atemporal | `plausibleValueLow`, `plausibleValueHigh`, `plausibleUnitConceptIds`, `plausibleGenderUseDescendants` |
| Plausibility, temporal | `plausibleAfterBirth`, `plausibleBeforeDeath`, `plausibleStartBeforeEnd` |
| Plausibility, uniqueness | none |

Most check types are labeled verification. The validation label is used for `isRequired`, `measurePersonCompleteness`, and the plausibleGender checks. Comparing your rates with a published estimate is validation in Kahn's sense, and it is work a study team does outside DQD. The labels above were read from the [DQD check type definitions](https://ohdsi.github.io/DataQualityDashboard/articles/CheckTypeDescriptions.html) for version 2.6.3 on 1 October 2026; open that page to confirm them for the version your site runs.

DQD runs its checks against an OMOP CDM and reports each as a pass or fail against a **threshold**: the percent of failing rows a site will accept for that check. Defaults differ by check and can be changed for your data and your study.

A useful habit is to run DQD early, read the failures, and decide which ones threaten your analysis. A failed check is not always fatal, and a passing dashboard does not guarantee the data answer your question.

### Data quality, or your concept set?
A recurring lesson is that an unexpected result is often not a data problem at all. It is frequently a concept set that is too narrow, too broad, or built on non-standard concepts. Before blaming the data, confirm that your concept set captures what you intended. That is the bridge into Part 2.

---

## Part 2: Concept sets

### What a concept set is
A concept set is a named, reusable expression that defines a clinical idea, for example "all sulfonylureas" or "type 2 diabetes." The expression is a list of concepts, each with options to include descendants, include mapped source concepts, or exclude. You build it once and reuse it in cohort entry events, inclusion rules, and characterization.

### Standard, classification, and non-standard concepts
Clinical tables store standard concepts (`standard_concept = 'S'`), so a concept set should resolve to standard concepts. A classification concept (`standard_concept = 'C'`), such as the ATC class "Sulfonylureas," is not stored in the clinical tables; it reaches the data through its standard descendants, which is why a class is added together with its descendants. A non-standard source concept (an ICD-10-CM or NDC code) will not match records in the standard concept fields.

### Descendants
A concept set entry can include descendants. Selecting the class "Sulfonylureas" with descendants pulls in the ingredients and every product below them in the hierarchy, so you do not have to list each one. The `concept_ancestor` table is what makes this work.

### Included Concepts and Included Source Codes
In ATLAS, a concept set has tabs that show what the expression resolves to:

- **Included Concepts** lists every concept the expression resolves to, with its standard status (Standard, Classification, or Non-Standard).
- **Included Source Codes** lists the source codes that map to those concepts, which is how you check that the codes your site records are covered and find gaps.

The expression itself has checkboxes for each concept: Exclude, Descendants, and Mapped. The Mapped checkbox adds mapped source concepts to the set itself, which is different from viewing the Included Source Codes tab. Tab and column labels differ a little between ATLAS versions, so check them on your site's instance.

### Building concept sets in Atlas
Atlas is the graphical interface for this work. You search the vocabulary, add concepts to a set, choose the options for each concept, and then reuse the set across cohorts. The Day 2 lab walks through building concept sets and checking them against the CDM.

---

## Slides and materials

| File | Description |
|:--|:--|
| [Instructor Deck](../training/day-02-vocab-dqd/kit/Instructor-Deck-with-Notes.pptx) | Full slide deck with speaker notes |
| [Participant Workbook](../training/day-02-vocab-dqd/kit/Participant-Workbook.pptx) | Workbook with fill-in exercises |
| [Kahoot Quiz](../training/day-02-vocab-dqd/kit/Kahoot-Quiz.csv) | Concept sets and DQD quiz |

See the [Day 2 exercise](../exercises/day-02-vocab-dqd.md) for the hands-on lab.

## Further reading
- The Book of OHDSI, Chapter 5 (Standardized Vocabularies), section 10.3 (Concept Sets), and Chapter 15 (Data Quality): https://ohdsi.github.io/TheBookOfOhdsi/
- Kahn MG, Callahan TJ, Barnard J, et al. A Harmonized Data Quality Assessment Terminology and Framework for the Secondary Use of Electronic Health Record Data. *EGEMS.* 2016;4(1):1244: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5051581/
- DQD check type definitions: https://ohdsi.github.io/DataQualityDashboard/articles/CheckTypeDescriptions.html
- Athena vocabulary browser: https://athena.ohdsi.org/
