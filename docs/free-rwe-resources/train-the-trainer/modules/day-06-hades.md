# :material-code-braces: Day 6, Part 1 · HADES: Cohort Diagnostics and Feature Extraction (Optional)

!!! info "Day 6 is taught as separate sessions"
    Part 1 (this page) covers the HADES environment, CohortDiagnostics, and FeatureExtraction. [Part 2](day-06-prediction.md) covers patient-level prediction. Each part is its own half-day session, and Part 2 reuses the connection and the cohort table set up here.

!!! abstract "Objectives"
    By the end of Day 6 you will be able to:

    1. Describe the HADES package ecosystem and explain how individual packages relate to each other.
    2. Set up a HADES environment with DatabaseConnector and a connection profile.
    3. Run CohortDiagnostics on a generated cohort and read the output.
    4. Run FeatureExtraction to build a baseline characterization table.
    5. Name the packages used for estimation (CohortMethod) and prediction (PatientLevelPrediction) and say where Part 2 continues.

---

## What HADES is

HADES (Health Analytics Data-to-Evidence Suite) is a collection of open-source R packages maintained by OHDSI that covers the full observational study pipeline — from data characterization and cohort validation through population-level effect estimation and patient-level prediction. Every HADES package is designed to run against an OMOP CDM and to produce results that are comparable across data partners.

The key packages and their roles:

| Package | What it does |
|:--|:--|
| **DatabaseConnector** | Connects R to any OMOP CDM database (Postgres, Snowflake, SQL Server, Databricks, BigQuery, etc.) |
| **CohortGenerator** | Creates cohort tables from cohort definition JSON exported from ATLAS |
| **CohortDiagnostics** | Audits cohort quality: concept set coverage, incidence rates, time series, and visit context |
| **FeatureExtraction** | Builds covariate tables (demographics, conditions, drugs, measurements) from a cohort |
| **CohortMethod** | Population-level effect estimation with the new-user cohort design |
| **SelfControlledCaseSeries** | Population-level safety estimation using within-person exposure variation |
| **PatientLevelPrediction** | Machine learning-based patient-level prediction models |
| **EvidenceSynthesis** | Combines estimates from several databases (meta-analysis across data partners) |
| **Achilles** | CDM characterization and data quality summary (Ares viewer) |
| **DataQualityDashboard** | The DQD covered in Day 2 — also part of HADES |

The complete package list and documentation live at [ohdsi.github.io/Hades](https://ohdsi.github.io/Hades/).

---

## Setting Up the Environment

!!! warning "Site-specific setup"
    Connection details (server, schema, port, driver) are local to your institution.
    Substitute your actual credentials wherever `[placeholder]` appears below.

### 1. Install HADES packages

First follow the [HADES R setup guide](https://ohdsi.github.io/Hades/rSetup.html): install the R version it names (R 4.4.1 when the guide was read on 1 October 2026), RTools on Windows, and Java, and set a GitHub personal access token. Without the token, installing every HADES package runs into the GitHub download cap.

```r
install.packages("remotes")
remotes::install_github("OHDSI/Hades")
```

Or install individual packages:

```r
install.packages(c("DatabaseConnector", "FeatureExtraction", "CohortGenerator"))  # on CRAN
remotes::install_github("OHDSI/CohortDiagnostics")
```

### 2. Create a connection profile

```r
library(DatabaseConnector)

connectionDetails <- createConnectionDetails(
  dbms     = "[your dbms: postgresql / sql server / spark / bigquery / etc.]",
  server   = "[your server / host]",
  user     = "[your username]",
  password = "[your password or keyring reference]",
  port     = [your port],
  pathToDriver = "[path to JDBC driver folder]"
)

# Test the connection
conn <- connect(connectionDetails)
querySql(conn, "SELECT COUNT(*) FROM [cdm_schema].person;")
disconnect(conn)
```

### 3. Define your schemas

```r
cdmDatabaseSchema    <- "[cdm_schema]"       # where the CDM lives
cohortDatabaseSchema <- "[results_schema]"   # where cohort tables are written
cohortTable          <- "ttt_day6_cohort"    # a dedicated table for this lab, not the ATLAS cohort table
```

---

## Agenda

| Time | Topic |
|:--|:--|
| 9:30 – 9:50 | HADES overview: the packages and how they fit together |
| 9:50 – 10:30 | Environment setup: DatabaseConnector, schemas, driver installation |
| 10:30 – 10:45 | Break |
| 10:45 – 11:45 | Hands-on: CohortGenerator and CohortDiagnostics on a training cohort |
| 11:45 – 12:30 | Hands-on: FeatureExtraction, building a baseline table |
| 12:30 – 1:00 | Reading the output together; recap and preview of Part 2 |

---

## CohortDiagnostics: Auditing a Cohort

CohortDiagnostics is a common next step after you build a cohort. It helps you judge whether the cohort captures what you intended. The cohorts have to be generated first, which the block below does with CohortGenerator.

```r
library(CohortGenerator)
library(CohortDiagnostics)

# Use a dedicated cohort table for this lab. Do not point CohortGenerator at the
# cohort table ATLAS writes to, because createCohortTables() can replace a table.
cohortTable     <- "ttt_day6_cohort"
cohortTableNames <- getCohortTableNames(cohortTable = cohortTable)

cohortDefinitionSet <- getCohortDefinitionSet(
  settingsFileName = "cohorts/CohortsToCreate.csv",
  jsonFolder       = "cohorts/",
  sqlFolder        = "cohorts/"
)

# Generate the cohorts into the dedicated table
createCohortTables(
  connectionDetails    = connectionDetails,
  cohortDatabaseSchema = cohortDatabaseSchema,
  cohortTableNames     = cohortTableNames
)
generateCohortSet(
  connectionDetails    = connectionDetails,
  cdmDatabaseSchema    = cdmDatabaseSchema,
  cohortDatabaseSchema = cohortDatabaseSchema,
  cohortTableNames     = cohortTableNames,
  cohortDefinitionSet  = cohortDefinitionSet
)

executeDiagnostics(
  cohortDefinitionSet       = cohortDefinitionSet,
  exportFolder              = "diagnostics_output",
  databaseId                = "[your site ID]",
  connectionDetails         = connectionDetails,
  cdmDatabaseSchema         = cdmDatabaseSchema,
  cohortDatabaseSchema      = cohortDatabaseSchema,
  cohortTableNames          = cohortTableNames,
  runInclusionStatistics    = TRUE,
  runIncludedSourceConcepts = TRUE,
  runOrphanConcepts         = TRUE,
  runTimeSeries             = TRUE,
  runVisitContext           = TRUE,
  runBreakdownIndexEvents   = TRUE,
  runIncidenceRate          = TRUE,
  minCellCount              = 5
)

# Merge the results and open the viewer
createMergedResultsFile("diagnostics_output", sqliteDbPath = "diagnostics.sqlite")
launchDiagnosticsExplorer(sqliteDbPath = "diagnostics.sqlite")
```

!!! note "Check the function names against your installed version"
    This block follows the CohortGenerator and CohortDiagnostics 3.x interface. It was not run against a database or re-checked against the package documentation when these pages were corrected on 1 October 2026, and the viewer functions have changed between releases. Before the session, compare it with the [CohortDiagnostics documentation](https://ohdsi.github.io/CohortDiagnostics/) for the version you have installed.

**Key diagnostics to review:**

- **Included source concepts:** which source codes actually appear in your CDM for this cohort's concept sets. Gaps here mean your concept set may be missing coverage.
- **Orphan concepts:** concepts that are not in your concept set, appear in the data, and look related to the concepts you chose (found by matching concept names and relationships). A long list is a prompt to review whether the concept set is too narrow.
- **Incidence rate time series:** spikes or gaps in when people enter the cohort — often signal coding changes, site-level data issues, or event-driven data collection.
- **Visit context:** proportion of index events in inpatient vs. outpatient vs. ED. Useful for assessing whether your entry event means what you intended clinically.

---

## FeatureExtraction: Building a Covariate Table

```r
library(FeatureExtraction)

covariateSettings <- createDefaultCovariateSettings()

covariateData <- getDbCovariateData(
  connectionDetails        = connectionDetails,
  cdmDatabaseSchema        = cdmDatabaseSchema,
  cohortDatabaseSchema     = cohortDatabaseSchema,
  cohortTable              = cohortTable,
  cohortIds                = c([your_cohort_id]),
  covariateSettings        = covariateSettings,
  aggregated               = TRUE     # one summary row per covariate
)

summary(covariateData)
```

With `aggregated = TRUE` the result is a summary per covariate (count and mean). Without it, the result has one row per person and covariate. Common uses:

- **Baseline characterization:** describe the cohort at index (demographics, conditions, drugs, lab values).
- **Propensity score model input:** feed into CohortMethod as predictors.
- **Predictive model features:** feed into PatientLevelPrediction.

---

## Slides & Materials

- :material-presentation: **Instructor deck with notes (headline-only slides):** [Download PPTX](../training/day-06-hades/kit/Part-1-Instructor-Deck-with-Notes.pptx)
- :material-script-text: **Slide-by-slide script:** [Open](../training/day-06-hades/kit/Part-1-Slide-Script.md)
- The code and the lab are on this page and the [Part 1 exercise](../exercises/day-06-hades-optional.md).

- :material-database-settings: **Databricks setup guide (placeholder template, used in both parts):** [Download PPTX](../training/day-06-hades/kit/Databricks-Setup-Placeholder-Guide.pptx)

The prediction slide kit, quiz, and notebook belong to [Part 2](day-06-prediction.md).

---

## Instructor Notes

- **Java and JDBC drivers are frequent setup blockers.** Plan time for troubleshooting before the session. The Databricks setup guide in the kit is a placeholder template: it lists what to ask your site for and has no driver-specific instructions.
- **Prioritize CohortDiagnostics if time is short.** Participants who will never run an estimation or prediction study can still use diagnostics on their own cohorts.
- **Keep the cohort table.** Part 2 reads the target and outcome cohorts from the dedicated cohort table created here, so ask participants not to drop it.
- **CohortMethod is left for self-study.** Point participants who need population-level estimation to Chapter 12 of the Book of OHDSI.

---

## Further Reading

- [HADES Package Documentation](https://ohdsi.github.io/Hades/)
- Book of OHDSI, Chapter 8 (OHDSI Analytics Tools) and Chapter 11 (Characterization, section 11.8 on cohort characterization in R): [ohdsi.github.io/TheBookOfOhdsi](https://ohdsi.github.io/TheBookOfOhdsi/)
- Book of OHDSI, Chapter 12 (Population-Level Estimation): [ohdsi.github.io/TheBookOfOhdsi](https://ohdsi.github.io/TheBookOfOhdsi/)
- [CohortDiagnostics vignette](https://ohdsi.github.io/CohortDiagnostics/)
- [FeatureExtraction vignette](https://ohdsi.github.io/FeatureExtraction/)

---

:material-arrow-left: [Day 5 · Treatment Pathways (Optional)](day-05-pathways.md) &emsp; :material-arrow-right: [Day 6, Part 2 · Patient-Level Prediction (Optional)](day-06-prediction.md)
