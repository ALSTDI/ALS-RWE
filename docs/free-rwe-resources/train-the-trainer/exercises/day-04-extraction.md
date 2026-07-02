# Exercises · Day 4 — Data Extraction (Adapt to Your Site)

!!! info "This lab is a template"
    Because extraction differs by institution, this lab is written as a fill-in
    framework rather than fixed steps. Replace the bracketed parts with your
    site's tools. See the [Day 4 module](../modules/day-04-extraction.md) for the
    general workflow and the site setup table.

!!! warning "Setup and extraction are site specific"
    These steps assume you have a generated cohort from Day 3 and read access to
    your CDM. The method (SEARCH, ATLAS-exported SQL, or a local pipeline) and
    the client (Databricks, DBeaver, Snowflake, Postgres, BigQuery, SQL Server,
    other) are whatever your site uses. Not everyone uses Databricks.

---

## Step 1: Pick a cohort
Use the new-user metformin cohort generated in Day 3 (or any small generated
cohort you have access to). Record its `cohort_definition_id`.

## Step 2: Extract using your site's method
Choose the path that matches your site:

- **SEARCH:** run a cohort-based extraction and save the output to your working location.
- **Exported SQL:** export the cohort and feature SQL from ATLAS and run it in your client.
- **Local pipeline:** request or trigger the extract through your site's process.

Pull, at minimum, the cohort's drug exposures and condition occurrences within a
defined window around cohort entry.

## Step 3: Validate the count
Independently re-count the cohort size and compare it to what ATLAS reported when
the cohort was generated:

```sql
-- Adjust schema and client to your site
SELECT COUNT(DISTINCT subject_id) AS persons
FROM results.cohort
WHERE cohort_definition_id = :your_cohort_id;
```

Write down both numbers. If they match, your extraction path is trustworthy. If
not, work through the reconciliation checklist below.

## Step 4: Reconcile (if numbers disagree)
- Same CDM and vocabulary version in both places?
- Did a join silently drop unmapped records (concept_id 0)?
- Was a time window applied in one query but not the other?
- Did you extract from the same results schema the cohort was generated into?

---

## Homework
- Document your site's extraction path in two or three sentences so a new team
  member could reproduce it.
- Extract one additional domain (for example measurements) and validate a count.

## Instructor notes
<details>
<summary>Show facilitation notes</summary>

- Before the session, fill in the site setup table in the Day 4 module so the
  group is working from your real tools, not generic examples.
- The learning objective is reconciliation, not a specific tool. Have each
  participant state their warehouse and client out loud so the group sees how
  much the environment varies while the logic stays the same.
- If participants are on different stacks, pair them so they compare how the
  same cohort extracts differently in each.
</details>
