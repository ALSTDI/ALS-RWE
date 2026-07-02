# Environment Setup Handout

A one-page participant handout to confirm you are ready before Week 1. For the full walkthrough see the [Environment Setup module](../modules/00-environment-walkthrough.md), and track your status with the [Environment Checklist Template](environment-checklist-template.md).

!!! warning "Setup and extraction are site specific"
    There is no single correct environment. Institutions differ in their data warehouse, their SQL client, their security model, and how data are extracted. The examples in this program use Databricks and DBeaver because that is what the reference site uses, but **not everyone uses Databricks.** Your site may use Snowflake, Postgres, BigQuery, SQL Server, Posit Workbench, or another stack. The OMOP CDM and the OHDSI tools (Athena, ATLAS, HADES) are the same everywhere. Only the connection details and the extraction tooling change. Wherever you see Databricks in these materials, substitute your local equivalent.

---

## What you need access to

| Item | What to confirm | Site specific? |
|---|---|---|
| **ATLAS** | You can log in, and create, save, and export a cohort definition (JSON). | URL is local to your site |
| **OMOP CDM database** | You have read access to a training or sandbox CDM (synthetic or de-identified). | Warehouse and schema are local |
| **Athena** | You can browse vocabularies at https://athena.ohdsi.org. | No, shared by everyone |
| **SQL client** | You can connect to the CDM and run `SELECT`. | Your client (Databricks, DBeaver, or other) |
| **Extraction tool** | You know how your site pulls cohort data (SEARCH, exported SQL, or a local pipeline). | Yes, varies widely |
| **R and HADES** (advanced) | R 4.2 or later, and you can install OHDSI packages. | Local install |
| **Git / GitHub** | You can clone, pull, and push to the program repository. | Repo URL is local |
| **Support contacts** | You know who to ask for data access, ATLAS admin, and IT help. | Yes, always local |

---

## Quick verification (do these before Week 1)

1. Log in to ATLAS and create one throwaway concept set, then delete it.
2. Run `SELECT * FROM person LIMIT 5;` against your training CDM in your own SQL client.
3. Open Athena and look up one concept (for example metformin).
4. Confirm you can reach the program repository on GitHub.
5. Record any blockers in the checklist and send them to your site support contact.

If all five work, you are ready. If extraction at your site does not use Databricks, note your actual tool in the checklist so your trainer can adapt the labs for you.
