# Exercises · Day 3 — Cohorts in ATLAS

!!! abstract "What you will do"
    1. Build a new-user metformin cohort in ATLAS.
    2. Add an inclusion rule with a temporal window.
    3. Generate the cohort and read the attrition.
    4. Export the cohort SQL and re-run a count yourself.

!!! warning "Setup and extraction are site specific"
    These steps use Databricks as the warehouse and a generic SQL client, because that is what the reference site uses. Your site may use something else (for example Snowflake, Postgres, BigQuery, SQL Server, or Posit Workbench). The cohort logic and the exported SQL are the same everywhere. Only the connection details and the client change. Substitute your local tools wherever Databricks is mentioned.

---

## Step 1: Define the entry event
1. In ATLAS, open **Cohort Definitions**, then **New Cohort**.
2. Add an entry event of **drug exposure** using a metformin concept set (build one if needed, with descendants).
3. Restrict to the **first** exposure per person so this is a new-user design.

## Step 2: Add an inclusion rule with a window
1. Add a new inclusion criterion: **at least 365 days of continuous observation before the entry event.** This makes "new use" meaningful.
2. Optionally add a second rule: **no sulfonylurea exposure in the 365 days before entry.** Note that this exclusion is written as an inclusion rule that must be satisfied (count of prior sulfonylurea exposures equals zero).

## Step 3: Generate and read attrition
1. Define the exit (for example, end of continuous metformin exposure).
2. Save and **generate** against your training CDM.
3. Open the **attrition** report. Note how many people each inclusion rule removed. A rule that removes almost everyone, or no one, is usually a window or logic error.

## Step 4: Export and validate the SQL
1. Export the cohort definition SQL from ATLAS.
2. Run it (or a simplified count) in your own SQL client and confirm the person count matches what ATLAS generated.

```sql
-- Sanity count of generated cohort (adjust schema/client to your site)
SELECT COUNT(DISTINCT subject_id) AS persons
FROM results.cohort
WHERE cohort_definition_id = :your_cohort_id;
```

If the counts disagree, check that you generated against the same CDM and vocabulary version you are querying.

---

## Homework
- Rebuild the cohort with a different prior-observation window (for example 180 days) and compare the attrition.
- Write one sentence on how the window changed the cohort size and why.

## Instructor notes
<details>
<summary>Show facilitation notes</summary>

- The metformin new-user cohort is the canonical example in the written tutorial, so learners can follow along step for step.
- Spend time on the attrition report. It is the single best tool for teaching that cohort definitions are logic, not code lists.
- When learners export SQL, have each name their warehouse and client. This reinforces that the definition is portable but the execution environment is local.
</details>
