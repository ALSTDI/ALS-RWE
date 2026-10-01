# Exercises · Day 2 — Concept Sets in Atlas and SQL Validation

!!! info "Primary tool: Atlas"
    These exercises use **Atlas** to build concept sets and **your site's CDM** for SQL validation.
    Open Atlas and confirm you can create a new concept set before starting.

!!! note "No CDM access? Colab fallback"
    If you don't yet have a CDM connection, a synthetic-data companion notebook is available:
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day2-Concept-Sets-and-Data-Quality.ipynb)
    or [download it](../notebooks/Day2-Concept-Sets-and-Data-Quality.ipynb).


!!! abstract "What you will do"
    1. Build a concept set in Atlas using descendants.
    2. Inspect the Included Source Codes tab to confirm coverage.
    3. Validate the concept set against the CDM with SQL.
    4. Read one Data Quality Dashboard result and decide whether it affects your study.

!!! warning "Setup and extraction are site specific"
    Every institution's environment is different. These steps use Databricks and DBeaver as the SQL client because that is what the reference site uses, but your site may use something else (for example Snowflake, Postgres, BigQuery, SQL Server, or Posit Workbench). The OMOP CDM and the SQL logic are the same everywhere. Only the connection details and the extraction tooling change. Substitute your local client, connection string, and data access steps wherever Databricks is mentioned.

---

## Step 1: Build a concept set (warm-up)
1. Open Atlas and go to **Concept Sets**, then **New Concept Set**.
2. Search for **sulfonylureas** and choose the ATC class concept (code A10BB). It is a Classification concept, not an ingredient.
3. Add it to the set, then turn on **Descendants** so the ingredients and the products below them are captured.
4. Save the set with a clear name, for example `TtT Day2 Sulfonylureas`.

## Step 2: Inspect Included Concepts and Included Source Codes
1. Open the **Included Concepts** tab. The class itself shows Classification, and its drug descendants show Standard. Nothing should show Non-Standard.
2. Open the **Included Source Codes** tab. These are the source codes that map to the concepts in your set. Skim them and ask: does this look like complete coverage for your site, or are obvious codes missing?

## Step 3: Validate against the CDM with SQL
Copy the concept ID of the class from ATLAS, then run the count yourself in your SQL client. A simple query (adjust schema and client to your site):

```sql
-- How many drug exposures fall in the sulfonylurea concept set?
SELECT COUNT(*) AS exposures,
       COUNT(DISTINCT de.person_id) AS persons
FROM cdm.drug_exposure de
JOIN cdm.concept_ancestor ca
     ON ca.descendant_concept_id = de.drug_concept_id
WHERE ca.ancestor_concept_id = :sulfonylurea_class_concept_id;
```

Compare the count with the record counts ATLAS shows for the concept (the RC and DRC columns). Those counts come from the last Achilles run, so small differences are expected when the CDM has been refreshed since then. Larger differences usually trace to a different schema, a different vocabulary version, or a set that does not include descendants.

!!! tip "Runnable practice without a CDM"
    If you do not yet have a CDM connection, the Day 1 sample notebook builds a tiny synthetic CDM in the notebook itself, so you can practice the same `concept_ancestor` join logic with no credentials.

## Step 4: Read one data quality result
1. Open a Data Quality Dashboard result for your training CDM (or a sample DQD report).
2. Find one **failed** check and note (a) its Kahn **category** (conformance, completeness, or plausibility); (b) its **subcategory** if one is shown; (c) its **context** (verification or validation); and (d) its **threshold**.
3. Decide, in one sentence, whether that failure would affect a diabetes drug study. The judgment is the goal of this step, more than the pass and fail counts.

!!! note "Kahn labels in a DQD report"
    Use this to place any check you find. DQD gives every check type a category, a subcategory where one applies, and a context.

    | Category | Subcategories | DQD check types with that label (examples) |
    | --- | --- | --- |
    | Conformance | value · relational · computational | `fkDomain` (value), `isForeignKey` (relational), `fkClass` (computational) |
    | Completeness | none | `standardConceptRecordCompleteness` (rows with `concept_id = 0`), `measureValueCompleteness` |
    | Plausibility | uniqueness · atemporal · temporal | `plausibleValueHigh` (atemporal), `plausibleAfterBirth` (temporal); none for uniqueness |

    **Verification** compares the data with expectations that come from the system itself; **validation** compares the data with an external benchmark. Most DQD check types are labeled verification. The validation label is used for `isRequired`, `measurePersonCompleteness`, and the plausibleGender checks. DQD does not compare your rates with published estimates; that kind of validation is separate work. Labels read from the [DQD check type definitions](https://ohdsi.github.io/DataQualityDashboard/articles/CheckTypeDescriptions.html), version 2.6.3, on 1 October 2026.

---

## Homework
- Build concept sets for two more drug classes of your choice and validate each with the SQL pattern above.
- Write two sentences on one data quality failure: what it is, and whether it threatens an analysis you care about.

## Instructor notes
<details>
<summary>Show facilitation notes</summary>

- Have a volunteer share their screen for the sulfonylurea build so the group sees the descendant toggle in action.
- Expect the Included Source Codes tab to surprise people. It is a quick way to show how source codes reach standard concepts and where coverage is missing.
- The SQL step is where site differences show. Ask each participant to name their own client and warehouse so the group sees the variety.
</details>
