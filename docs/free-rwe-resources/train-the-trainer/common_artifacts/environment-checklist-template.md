# Environment Checklist Template

> **Trainers:** Copy this page into a shared document (Google Doc, Word, or Markdown file) and distribute to participants before Module 0. Ask participants to complete it at least 48 hours before Day 1 and send any blockers to the site support contact.

---

## Participant Information

| Field | Response |
|:--|:--|
| Name | |
| Institution / Site | |
| Role | |
| Cohort / Session | |
| Date completed | |
| Support contact | |

---

## Section 1 · Browser-Based Tools (No Installation Required)

| # | Tool | What to Verify | Status | Notes |
|:--|:--|:--|:--|:--|
| 1.1 | **Athena** | Open [athena.ohdsi.org](https://athena.ohdsi.org) and search for "Metformin" — do results appear? | ☐ Pass · ☐ Blocked | |
| 1.2 | **ATLAS** | Log in to your site's ATLAS instance · Create and delete a throwaway concept set | ☐ Pass · ☐ Blocked | ATLAS URL: |
| 1.3 | **Atlas — Cohort export** | Export a cohort SQL from any existing cohort definition (JSON button visible?) | ☐ Pass · ☐ Blocked | |
| 1.4 | **GitHub** | Open [github.com/ALSTDI/ALS-RWE](https://github.com/ALSTDI/ALS-RWE) and confirm you can view files | ☐ Pass · ☐ Blocked | |

---

## Section 2 · Database Access (CDM)

| # | Item | What to Verify | Status | Notes |
|:--|:--|:--|:--|:--|
| 2.1 | **Warehouse access** | Your site's warehouse (Databricks / Snowflake / Postgres / other) is reachable from your machine | ☐ Pass · ☐ Blocked | Warehouse type: |
| 2.2 | **SQL Client** | Open your SQL client (Databricks notebook / DBeaver / other) and connect | ☐ Pass · ☐ Blocked | Client used: |
| 2.3 | **CDM read access** | Run: `SELECT * FROM [cdm_schema].person LIMIT 5;` — does it return rows? | ☐ Pass · ☐ Blocked | CDM schema: |
| 2.4 | **Vocabulary tables** | Run: `SELECT * FROM [cdm_schema].concept LIMIT 5;` — does it return rows? | ☐ Pass · ☐ Blocked | |
| 2.5 | **Results schema write access** | Confirm you can write to the results/cohort schema (for ATLAS cohort generation) | ☐ Pass · ☐ Blocked | Results schema: |

---

## Section 3 · Local Software

| # | Tool | What to Verify | Status | Notes |
|:--|:--|:--|:--|:--|
| 3.1 | **Git** | Run `git --version` in a terminal — does it return a version number? | ☐ Pass · ☐ Blocked | Version: |
| 3.2 | **GitHub auth** | `git clone [repo URL]` completes without auth errors | ☐ Pass · ☐ Blocked | |
| 3.3 | **Text editor / IDE** | VS Code, RStudio, or preferred editor opens and displays Markdown files | ☐ Pass · ☐ Blocked | IDE used: |

---

## Section 4 · R / HADES (Required for Day 6 Optional)

| # | Tool | What to Verify | Status | Notes |
|:--|:--|:--|:--|:--|
| 4.1 | **R version** | `R.version$version.string` returns ≥ 4.2 | ☐ Pass · ☐ Blocked · ☐ Not needed | Version: |
| 4.2 | **RStudio or Posit Workbench** | Opens and console is functional | ☐ Pass · ☐ Blocked · ☐ Not needed | |
| 4.3 | **Java** | `system("java -version")` in RStudio returns a version (8 or 11 preferred) | ☐ Pass · ☐ Blocked · ☐ Not needed | Version: |
| 4.4 | **DatabaseConnector** | `library(DatabaseConnector)` loads without error | ☐ Pass · ☐ Blocked · ☐ Not needed | |
| 4.5 | **HADES (core)** | `library(CohortDiagnostics)` and `library(FeatureExtraction)` load without error | ☐ Pass · ☐ Blocked · ☐ Not needed | |
| 4.6 | **JDBC Driver** | Connection profile resolves with `createConnectionDetails(...)` | ☐ Pass · ☐ Blocked · ☐ Not needed | Driver path: |

---

## Section 5 · Extraction Tool (Site Specific — Day 4)

| # | Item | What to Verify | Status | Notes |
|:--|:--|:--|:--|:--|
| 5.1 | **Extraction method** | Identify your site's extraction path: SEARCH / exported Atlas SQL / local pipeline | ☐ Confirmed | Method: |
| 5.2 | **SEARCH access** | *(If applicable)* Log in to SEARCH and confirm a test extraction runs | ☐ Pass · ☐ Blocked · ☐ N/A | |
| 5.3 | **Output location** | Confirm where extracts are written (path, bucket, or schema) | ☐ Confirmed | Output path: |

---

## Blockers (Complete Before Day 1)

List any items marked **Blocked** above and the action you have taken:

| # | Blocked Item | Action Taken / Notes | Resolved? |
|:--|:--|:--|:--|
| | | | ☐ Yes · ☐ No |
| | | | ☐ Yes · ☐ No |
| | | | ☐ Yes · ☐ No |

---

## Trainer Use: Readiness Summary

> Fill this in after collecting completed checklists from participants.

| Participant | ATLAS | CDM SQL | GitHub | R/HADES | Ready for Day 1? |
|:--|:--|:--|:--|:--|:--|
| | ☐ | ☐ | ☐ | ☐ | ☐ |
| | ☐ | ☐ | ☐ | ☐ | ☐ |
| | ☐ | ☐ | ☐ | ☐ | ☐ |

---

> See also: [Environment Setup Handout](environment-setup-handout.md) · [Environment Setup Module](../modules/00-environment-walkthrough.md)
