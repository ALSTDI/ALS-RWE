# Exercises · Day 6, Part 1 (Optional): HADES Cohort Diagnostics and Feature Extraction

!!! abstract "What you will do"
    1. Set up a DatabaseConnector connection to your training CDM.
    2. Run CohortDiagnostics on a cohort from Day 3 and read three key diagnostic outputs.
    3. Run FeatureExtraction to build a baseline characterization table.

!!! warning "Setup and extraction are site specific"
    HADES requires R (the [setup guide](https://ohdsi.github.io/Hades/rSetup.html) targets R 4.4.1 as of 1 October 2026), RStudio or Posit Workbench, Java, a GitHub personal access token for installation, JDBC drivers, and database credentials. Connection details are entirely local to your site. The module page has the connection setup template. Patient-level prediction is a separate session with its own exercise: [Day 6, Part 2](day-06-prediction-optional.md).

---

## Part A: Environment Check

Before running any HADES code, verify your setup. Run this block in RStudio:

```r
# Check R version
R.version$version.string

# Check Java
system("java -version")

# Attempt to load key packages
library(DatabaseConnector)
library(CohortDiagnostics)
library(FeatureExtraction)

library(CohortGenerator)

# If any library() call fails, install the missing package:
# install.packages("<PackageName>")  for packages on CRAN, or
# remotes::install_github("OHDSI/<PackageName>")
```

If `library(DatabaseConnector)` fails, install it:
```r
install.packages("DatabaseConnector")
```

Fill in the [Environment Checklist Template](../common_artifacts/environment-checklist-template.md) with your R/Java/HADES status before proceeding.

---

## Part B: CohortDiagnostics

### Step B1: Prepare cohort definition files

Export your Day 3 metformin cohort from ATLAS:
1. In ATLAS, open your cohort definition.
2. Click **Export** → download the JSON and the SQL (choose your dialect).
3. Save to a local project folder, e.g., `cohorts/` with a `CohortsToCreate.csv` index file.

Save the JSON as `cohorts/MetforminNewUsers.json` and the SQL as `cohorts/MetforminNewUsers.sql`, so the file names match the cohort name. The `CohortsToCreate.csv` format:
```
cohortId,cohortName
1,MetforminNewUsers
```

### Step B2: Run diagnostics

```r
library(CohortGenerator)
library(CohortDiagnostics)

# Fill in your connection details (from the module page setup template)
connectionDetails <- createConnectionDetails(
  dbms     = "[your dbms]",
  server   = "[your server]",
  user     = "[your user]",
  password = "[your password]",
  port     = [your port],
  pathToDriver = "[path to JDBC driver]"
)

cdmDatabaseSchema    <- "[cdm_schema]"
cohortDatabaseSchema <- "[results_schema]"

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

### Step B3: Read the diagnostics output

In the Shiny viewer, navigate to each section and answer these questions:

**Included Source Concepts:**
- Which source codes appear most frequently in your CDM for this cohort?
- Are there codes you expected to see that are missing?

**Orphan Concepts:**
- Are there concepts in the data that look related to your concept set and are not included?
- Does the list suggest your concept set is too narrow?

**Incidence Rate Time Series:**
- Is the incidence rate stable over time, or are there spikes or gaps?
- Can you explain any unusual patterns (e.g., a data collection artifact, a coding change)?

**Visit Context:**
- What proportion of index events occur in outpatient vs. inpatient settings?
- Does this match what you would expect for a new metformin prescription?

Record your answers in a brief notes file: `diagnostics_output/notes.md`.

---

## Part C: FeatureExtraction

### Step C1: Build a default covariate table

```r
library(FeatureExtraction)

# Use default covariate settings (demographics, conditions, drugs, measurements)
covariateSettings <- createDefaultCovariateSettings()

covariateData <- getDbCovariateData(
  connectionDetails     = connectionDetails,
  cdmDatabaseSchema     = cdmDatabaseSchema,
  cohortDatabaseSchema  = cohortDatabaseSchema,
  cohortTable           = cohortTable,
  cohortIds             = c(1),   # your metformin cohort ID
  covariateSettings     = covariateSettings,
  aggregated            = TRUE    # one summary row per covariate
)

summary(covariateData)
```

### Step C2: Summarize and inspect

```r
# The 20 covariates with the highest mean value in the cohort
library(dplyr)
covariateData$covariates %>%
  inner_join(covariateData$covariateRef, by = "covariateId") %>%
  arrange(desc(averageValue)) %>%
  select(covariateName, averageValue) %>%
  head(20) %>%
  collect()
```

**Questions to answer:**
1. Which prior conditions are most prevalent? Are they what you expected for new metformin users at your site?
2. What is the mean age and sex distribution of the cohort?
3. Do any covariate values surprise you?

---

## Homework

- Read one CohortDiagnostics output section that surprised you and write two sentences explaining what it means for your analysis.
- Add an outcome cohort to your `cohorts/` folder and `CohortsToCreate.csv` (cohortId 2), and generate it into the same cohort table. Part 2 uses it as the outcome to predict.
- Optional: install and run Achilles on your training CDM and browse the Ares viewer output.

---

## Instructor Notes

<details>
<summary>Show facilitation notes</summary>

- **Java is a frequent blocker.** Before the session, confirm that `system("java -version")` returns a version from within RStudio for each participant, and follow the Java step in the HADES R setup guide if it does not. The Databricks setup guide in the kit is a placeholder template without platform-specific instructions.
- **CohortDiagnostics first.** Even if the group never runs CohortMethod or PatientLevelPrediction, running CohortDiagnostics on a cohort they built in Day 3 is useful. The "Included Source Concepts" and "Orphan Concepts" tabs directly reinforce Day 2 vocabulary lessons.
- **Keep the cohort table.** Part 2 reads the target and outcome cohorts from the cohort table created in Part B, so ask participants not to drop it.
- **Pair different backgrounds.** Pair a clinician or research analyst with a data analyst for the CohortDiagnostics review, since each tends to notice different patterns.

</details>

---

[:material-arrow-left: Back to module: Day 6, Part 1](../modules/day-06-hades.md) &emsp; [:material-arrow-right: Day 6, Part 2 exercise](day-06-prediction-optional.md)
