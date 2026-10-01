# Module 0 · Environment Setup and Access

!!! info "White-Label Program"
    This module is designed for **Train-the-Trainer programs** built around the OHDSI ecosystem.  
    It intentionally avoids site-specific branding so it can be **cloned and customized** by any institution or trainer team.  
    Replace placeholders and add links for your local environment as needed.

!!! warning "Setup and extraction are site specific"
    There is no single correct environment. Institutions differ in their data warehouse, SQL client, and extraction tooling. These materials use Databricks and DBeaver as examples, but not everyone uses Databricks. Your site may use Snowflake, Postgres, BigQuery, SQL Server, Posit Workbench, or another stack. The OMOP CDM and OHDSI tools are the same everywhere; only the connection details change. See the [Environment Setup Handout](../common_artifacts/environment-setup-handout.md) for the participant quick guide.

---

## Overview

This module ensures all participants have **functional access** to the systems, tools, and data sources required before the start of Day 1.  
Each participant should complete the environment checklist and verify all access points work correctly.

---

## Objectives

By the end of this module, participants will be able to:

1. Access all required tools and environments (ATLAS and the CDM database).
2. Verify permissions for data connections and tool execution.
3. Install and test required local software (R, RStudio, Git, SQL client).
4. Document readiness using the provided **Environment Checklist Template**.

---

## Systems & Tools Setup

### :material-compass: ATLAS
- Confirm **login credentials** and ability to create/edit cohorts.
- Test saving and exporting a cohort definition (JSON).
- Verify cohort characterization jobs can run successfully.

### :material-database: OMOP CDM Access
- Confirm **read access** to a sandbox or training CDM database (synthetic or de-identified).
- Ensure network permissions and ODBC/connection strings are functional.
- Optional: Test a basic `SELECT * FROM PERSON LIMIT 5;` query via SQL client (`SELECT TOP 5 *` on SQL Server).

### :material-chart-bar: HADES Environment (Optional — Day 6 Track)
- Verify R, RStudio (or Posit Workbench), Java, and (on Windows) RTools. The [HADES R setup guide](https://ohdsi.github.io/Hades/rSetup.html) names the R version the packages are tested against (R 4.4.1 when the guide was read on 1 October 2026).
- Set a GitHub personal access token before installing, as the setup guide describes; installing every HADES package anonymously runs into the GitHub download cap.
- Confirm ability to install and load OHDSI packages:

```r
install.packages("remotes")
remotes::install_github("OHDSI/Hades")
library(Hades)
```

- Optional: Test Achilles or DQD on a small sample CDM if permissions allow.

### :material-laptop: Local Tools
- **Git/GitHub:** ability to clone, pull, and push to this repository.
- **SQL client:** Databricks, DBeaver, or similar with CDM connectivity.
- **Text editor:** VS Code, RStudio, or preferred IDE.

---

## :material-checkbox-multiple-marked: Environment Checklist Template

Trainers may clone and adapt this checklist for local use.  
A downloadable Markdown version is available here:  
[Download environment-checklist-template.md](../common_artifacts/environment-checklist-template.md)

| Area | Task | Verified (Y/N) | Notes |
|:--|:--|:--|:--|
| ATLAS | Login successful and can save cohorts | | |
| CDM Database | Confirmed SQL read access | | |
| HADES | R environment installed and packages load | | |
| GitHub | Repo cloned and permissions confirmed | | |
| SQL Client | Connected to CDM successfully | | |

> Trainers: copy this table to your local documentation or export it as CSV for tracking participant readiness.

---

## Slides & Kit Materials

| File | Description |
|:--|:--|
| [Instructor Deck](../training/day-00-environment/kit/Instructor-Deck-with-Notes.pptx) | Full slide deck with speaker notes |
| [Participant Handout](../training/day-00-environment/kit/Participant-Handout.pptx) | Abbreviated handout for participants |
| [Kahoot Quiz](../training/day-00-environment/kit/Kahoot-Quiz.csv) | Environment setup quiz |

---

## Deliverables

- Completed **Environment Checklist** uploaded or shared with instructors.
- Verified tool access and functional test results (ATLAS and the CDM).

---

## Tips for Trainers

- Keep setup **tool-agnostic** and **site-neutral**. Replace institutional URLs and connection details in your fork.
- Encourage participants to complete setup **at least 48 hours before Day 1**.
- Maintain a shared support document or channel for troubleshooting access issues.

---

:material-arrow-right: **Next:** [Day 1 · OMOP Common Data Model](day-01-omop-cdm.md) — once all environment checks are complete.
