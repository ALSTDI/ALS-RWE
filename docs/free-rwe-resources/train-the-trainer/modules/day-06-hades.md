# :material-code-braces: Day 6 · Advanced Analytics with HADES (Optional)

!!! abstract "Objectives"
    By the end of Day 6 you will be able to:

    1. Describe the HADES package ecosystem and explain how individual packages relate to each other.
    2. Set up a HADES environment with DatabaseConnector and a connection profile.
    3. Run CohortDiagnostics on a generated cohort and read the output.
    4. Run FeatureExtraction to build a baseline characterization table.
    5. Identify where to find CohortMethod and PatientLevelPrediction and what each does.
    6. Interpret key diagnostics (propensity score distribution, calibration plot) at a conceptual level.

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
| **CohortMethod** | Population-level comparative effectiveness (new-user active-comparator design) |
| **SelfControlledCaseSeries** | Population-level safety estimation using within-person exposure variation |
| **PatientLevelPrediction** | Machine learning-based patient-level prediction models |
| **EvidenceSynthesis** | Combines estimates across data partners in a network meta-analysis |
| **Achilles** | CDM characterization and data quality summary (Ares viewer) |
| **DataQualityDashboard** | The DQD covered in Day 2 — also part of HADES |

The complete package list and documentation live at [ohdsi.github.io/Hades](https://ohdsi.github.io/Hades/).

---

## Setting Up the Environment

!!! warning "Site-specific setup"
    Connection details (server, schema, port, driver) are local to your institution.
    Substitute your actual credentials wherever `[placeholder]` appears below.

### 1. Install HADES packages

```r
install.packages("remotes")
remotes::install_github("OHDSI/Hades")
```

Or install individual packages:

```r
remotes::install_github("OHDSI/DatabaseConnector")
remotes::install_github("OHDSI/CohortDiagnostics")
remotes::install_github("OHDSI/FeatureExtraction")
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
cohortTable          <- "cohort"             # table name for cohorts
```

---

## Agenda

| Time | Topic |
|:--|:--|
| 09:00 – 09:30 | HADES overview: packages, roles, and how they chain together |
| 09:30 – 10:15 | Environment setup: DatabaseConnector, schemas, driver installation |
| 10:15 – 10:30 | Break |
| 10:30 – 11:30 | Hands-on: CohortDiagnostics on a training cohort |
| 11:30 – 12:00 | Hands-on: FeatureExtraction — building a covariate table |
| 12:00 – 13:00 | Lunch |
| 13:00 – 14:00 | Demo: CohortMethod or PatientLevelPrediction (choose one based on group interest) |
| 14:00 – 14:45 | Interpreting diagnostics: propensity score overlap, calibration, model performance |
| 14:45 – 15:15 | Recap, next steps, and how to contribute to the OHDSI network |

---

## CohortDiagnostics: Auditing a Cohort

CohortDiagnostics is the first step after you build a cohort — it tells you whether the cohort actually captures what you intended.

```r
library(CohortDiagnostics)

cohortDefinitionSet <- getCohortDefinitionSet(
  settingsFileName   = "cohorts/CohortsToCreate.csv",
  jsonFolder         = "cohorts/",
  sqlFolder          = "cohorts/"
)

executeDiagnostics(
  cohortDefinitionSet     = cohortDefinitionSet,
  exportFolder            = "diagnostics_output/",
  databaseId              = "[your site ID]",
  connectionDetails       = connectionDetails,
  cdmDatabaseSchema       = cdmDatabaseSchema,
  cohortDatabaseSchema    = cohortDatabaseSchema,
  cohortTable             = cohortTable,
  runInclusionStatistics  = TRUE,
  runIncludedSourceConcepts = TRUE,
  runOrphanConcepts       = TRUE,
  runTimeSeries           = TRUE,
  runVisitContext         = TRUE,
  runBreakdownIndexEvents = TRUE,
  runIncidenceRate        = TRUE,
  minCellCount            = 5
)

# Launch the Shiny viewer
launchDiagnosticsExplorer("diagnostics_output/")
```

**Key diagnostics to review:**

- **Included source concepts:** which source codes actually appear in your CDM for this cohort's concept sets. Gaps here mean your concept set may be missing coverage.
- **Orphan concepts:** standard concepts that are close descendants of your concept set but not included. A large orphan list often means your concept set is too narrow.
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
  covariateSettings        = covariateSettings
)

summary(covariateData)
```

The result is a sparse covariate matrix. Common uses:

- **Baseline characterization:** describe the cohort at index (demographics, conditions, drugs, lab values).
- **Propensity score model input:** feed into CohortMethod as predictors.
- **Predictive model features:** feed into PatientLevelPrediction.

---

## Slides & Materials

- :material-presentation: **Instructor deck:** [Download PPTX](../training/day-06-hades/kit/Instructor-Deck.pptx)
- :material-notebook: **Participant workbook:** [Download PPTX](../training/day-06-hades/kit/Participant-Workbook.pptx)
- :material-help-circle: **Kahoot quiz (CSV):** [Download](../training/day-06-hades/kit/Kahoot-Quiz.csv)
- :material-file-document: **Participant handout:** [Download PPTX](../training/day-06-hades/kit/Participant-Handout.pptx)
- :material-key: **Instructor answer key:** [Download PPTX](../training/day-06-hades/kit/Instructor-Answer-Key.pptx)
- :material-presentation-play: **Live demo script:** [Download PPTX](../training/day-06-hades/kit/Live-Demo-Script.pptx)
- :material-chart-bar: **Prediction interpretation guide:** [Download PPTX](../training/day-06-hades/kit/Prediction-Interpretation-Guide.pptx)
- :material-database-settings: **Databricks setup guide:** [Download PPTX](../training/day-06-hades/kit/Databricks-Setup-Placeholder-Guide.pptx)
- :material-flask: **Colab notebook (Patient-Level Prediction):** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day6-Patient-Level-Prediction.ipynb)

---

## Instructor Notes

- **JAVA and JDBC drivers are the most common setup blocker.** Budget 30–45 minutes for troubleshooting before the session. The Databricks setup guide in the kit has driver-specific instructions.
- **Choose one advanced demo.** CohortMethod (population-level estimation) and PatientLevelPrediction (patient-level ML) both take an hour to do properly. Pick the one more relevant to your group and leave the other for self-study.
- **CohortDiagnostics is the highest-ROI exercise.** Even participants who will never run CohortMethod will benefit from running diagnostics on their own cohorts. Prioritize this if time is short.
- **Use the Colab notebook for the prediction portion.** It uses synthetic data and requires no CDM connection, which keeps the group moving even if database setup is incomplete.

---

## Further Reading

- [HADES Package Documentation](https://ohdsi.github.io/Hades/)
- Book of OHDSI, Chapter 13 (Prediction): [ohdsi.github.io/TheBookOfOhdsi](https://ohdsi.github.io/TheBookOfOhdsi/)
- Book of OHDSI, Chapter 12 (Estimation): [ohdsi.github.io/TheBookOfOhdsi](https://ohdsi.github.io/TheBookOfOhdsi/)
- [CohortDiagnostics vignette](https://ohdsi.github.io/CohortDiagnostics/)
- [FeatureExtraction vignette](https://ohdsi.github.io/FeatureExtraction/)
- [PatientLevelPrediction vignette](https://ohdsi.github.io/PatientLevelPrediction/)

---

:material-arrow-left: [Day 5 · Treatment Pathways (Optional)](day-05-pathways.md)
