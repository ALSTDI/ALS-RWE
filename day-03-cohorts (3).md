# Day 4 · Data Extraction (Site Specific)

!!! info "White-label, fill in for your site"
    Data extraction is the one part of this program that cannot be standardized.
    How you pull OMOP data for analysis depends on your warehouse, your client,
    your access model, and your institution's governance. This page gives the
    general framework that holds everywhere and leaves the specifics for you to
    fill in, the same way the [Environment Setup module](00-environment-walkthrough.md)
    is meant to be customized per site.

!!! warning "Setup and extraction are site specific"
    There is no single correct extraction method. Some sites use the OHDSI
    SEARCH tool, some export SQL from ATLAS and run it in a client (Databricks,
    DBeaver, Snowflake, Postgres, BigQuery, SQL Server), and some have a local
    pipeline that hands back a prepared dataset. The OMOP CDM and the logic are
    the same everywhere. Only the tooling and the access steps change. Replace
    the placeholders below with your site's actual tools and contacts.

## Objectives
By the end of Day 4 you will be able to:

1. Describe what "extraction" means in an OHDSI workflow: turning a defined cohort into an analytic dataset.
2. Identify the extraction path used at your site.
3. Re-run an extraction and validate the result against ATLAS or SEARCH.
4. Recognize the common reasons a count does not reconcile.

## The general workflow (true everywhere)
Regardless of tooling, extraction follows the same shape:

1. **Start from a defined, generated cohort** (the Day 3 output). Extraction is meaningless without a cohort definition behind it.
2. **Decide what to pull:** which domains and time windows (conditions, drugs, measurements, observation periods relative to cohort entry).
3. **Run the extraction** using your site's method (SEARCH, exported SQL, or local pipeline).
4. **Validate:** independently re-count a key number (cohort size, event count) and confirm it matches the source. Reconciliation is the whole point of this day.
5. **Document** the CDM version, vocabulary version, and date, so the extract is reproducible.

## Your site's extraction setup (fill this in)
Trainers: complete this table for your institution before the session, the same
way you complete the environment checklist.

| Item | Your site's answer |
|---|---|
| Primary warehouse (Databricks, Snowflake, Postgres, BigQuery, SQL Server, other) | *(insert)* |
| SQL client or interface | *(insert)* |
| Extraction method (SEARCH, ATLAS-exported SQL, local pipeline, other) | *(insert)* |
| Where extracts are written (path, bucket, schema) | *(insert)* |
| Access or approval needed before extracting | *(insert)* |
| CDM and vocabulary version in use | *(insert)* |
| Who to contact for extraction help | *(insert)* |

## Validation: the part that is universal
Whatever the tooling, the validation logic is portable. After extracting a cohort's
drug exposures, confirm the person count matches the generated cohort:

```sql
-- Adjust schema and client to your site
SELECT COUNT(DISTINCT subject_id) AS persons_in_cohort
FROM results.cohort
WHERE cohort_definition_id = :your_cohort_id;
```

If your extracted dataset has a different person count than this, the usual
causes are a different CDM or vocabulary version, a join that dropped unmapped
records (concept_id 0), or a time window applied in one place but not the other.

---

## Materials
The hands-on lab is on the [Day 4 exercise](../exercises/day-04-extraction.md)
page and is written as a template for you to adapt to your site. Day 4 has no
fixed slide deck because the steps are local; build a short site-specific deck
from the [ALS TDI template](../resources.md) if you need one for your group.

## Further reading
- The Book of OHDSI, Chapter 3 (ETL): https://ohdsi.github.io/TheBookOfOhdsi/
- The [OMOP Vocabulary and SQL Cheat Sheet](../common_artifacts/omop-vocab-sql-cheat-sheet.md) for query patterns.
