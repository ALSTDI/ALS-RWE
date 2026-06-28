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
    2. Inspect the "mapped" view to confirm coverage.
    3. Validate the concept set against the CDM with SQL.
    4. Read one Data Quality Dashboard result and decide whether it matters.

!!! warning "Setup and extraction are site specific"
    Every institution's environment is different. These steps use Databricks and DBeaver as the SQL client because that is what the reference site uses, but your site may use something else (for example Snowflake, Postgres, BigQuery, SQL Server, or Posit Workbench). The OMOP CDM and the SQL logic are the same everywhere. Only the connection details and the extraction tooling change. Substitute your local client, connection string, and data access steps wherever Databricks is mentioned.

---

## Step 1: Build a concept set (warm-up)
1. Open Atlas and go to **Concept Sets**, then **New Concept Set**.
2. Search Athena for the ingredient **sulfonylureas**.
3. Add it to the set, then turn on **Include Descendants** so all products and doses are captured.
4. Save the set with a clear name, for example `TtT Day2 Sulfonylureas`.

## Step 2: Inspect standard and mapped
1. Open the **Included Concepts** tab and confirm every concept is standard.
2. Open the **Mapped** view. These are the source codes that map into your standard concepts. Skim them and ask: does this look like complete coverage for your site, or are obvious codes missing?

## Step 3: Validate against the CDM with SQL
Export the concept set expression SQL from Atlas, then run the count yourself in your SQL client. A simple validation query (adjust schema and client to your site):

```sql
-- How many drug exposures fall in the sulfonylurea concept set?
SELECT COUNT(*) AS exposures,
       COUNT(DISTINCT de.person_id) AS persons
FROM cdm.drug_exposure de
JOIN cdm.concept_ancestor ca
     ON ca.descendant_concept_id = de.drug_concept_id
WHERE ca.ancestor_concept_id = :sulfonylurea_ingredient_concept_id;
```

Compare the count to what Atlas reports. If they differ, the usual culprits are a non-standard concept in the set, a missing "include descendants" toggle, or a schema or vocabulary version mismatch.

!!! tip "Runnable practice without a CDM"
    If you do not yet have a CDM connection, the Day 1 sample notebook builds a tiny synthetic CDM in the notebook itself, so you can practice the same `concept_ancestor` join logic with no credentials.

## Step 4: Read one data quality result
1. Open a Data Quality Dashboard result for your training CDM (or a sample DQD report).
2. Find one **failed** check and note its category (conformance, completeness, or plausibility) and its threshold.
3. Decide, in one sentence, whether that failure would affect a diabetes drug study. This judgment, not the pass/fail count, is the point.

---

## Homework
- Build concept sets for two more drug classes of your choice and validate each with the SQL pattern above.
- Write two sentences on one data quality failure: what it is, and whether it threatens an analysis you care about.

## Instructor notes
<details>
<summary>Show facilitation notes</summary>

- Have a volunteer share their screen for the sulfonylurea build so the group sees the descendant toggle in action.
- Expect the "mapped" view to surprise people. It is the fastest way to teach why non-standard concepts cause silent data loss.
- The SQL validation step is where the site-specific reality lands. Ask each participant to name their own client and warehouse out loud so the group sees the variety.
</details>
