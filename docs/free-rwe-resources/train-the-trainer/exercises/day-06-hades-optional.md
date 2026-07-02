# Exercises · Day 6 (Optional) — HADES

!!! tip "Sample notebook"
    Run the companion notebook in Colab (synthetic data, no credentials needed): [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day6-Patient-Level-Prediction.ipynb)
    or [download it](../notebooks/Day6-Patient-Level-Prediction.ipynb).

!!! abstract "What you will do"
    1. Set up a DatabaseConnector connection to your training CDM.
    2. Run CohortDiagnostics on a cohort from Day 3 and read three key diagnostic outputs.
    3. Run FeatureExtraction to build a baseline characterization table.
    4. (Optional) Run a minimal PatientLevelPrediction or CohortMethod workflow and interpret one output.

!!! warning "Setup and extraction are site specific"
    HADES requires R (≥ 4.2), RStudio or Posit Workbench, Java, JDBC drivers, and database credentials. Connection details are entirely local to your site. The module page has the connection setup template; use the Colab notebook as a fallback if CDM access is not yet functional.

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

# If any library() call fails, install the missing package:
# remotes::install_github("OHDSI/<PackageName>")
```

If `library(DatabaseConnector)` fails, install it:
```r
install.packages("remotes")
remotes::install_github("OHDSI/DatabaseConnector")
```

Fill in the [Environment Checklist Template](../common_artifacts/environment-checklist-template.md) with your R/Java/HADES status before proceeding.

---

## Part B: CohortDiagnostics

### Step B1: Prepare cohort definition files

Export your Day 3 metformin cohort from ATLAS:
1. In ATLAS, open your cohort definition.
2. Click **Export** → download the JSON and the SQL (choose your dialect).
3. Save to a local project folder, e.g., `cohorts/` with a `CohortsToCreate.csv` index file.

The `CohortsToCreate.csv` format:
```
cohortId,cohortName,fileName
1,MetforminNewUsers,MetforminNewUsers.json
```

### Step B2: Run diagnostics

```r
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
cohortTable          <- "cohort"

cohortDefinitionSet <- getCohortDefinitionSet(
  settingsFileName = "cohorts/CohortsToCreate.csv",
  jsonFolder       = "cohorts/",
  sqlFolder        = "cohorts/"
)

executeDiagnostics(
  cohortDefinitionSet       = cohortDefinitionSet,
  exportFolder              = "diagnostics_output/",
  databaseId                = "[your_site_id]",
  connectionDetails         = connectionDetails,
  cdmDatabaseSchema         = cdmDatabaseSchema,
  cohortDatabaseSchema      = cohortDatabaseSchema,
  cohortTable               = cohortTable,
  runIncludedSourceConcepts = TRUE,
  runOrphanConcepts         = TRUE,
  runTimeSeries             = TRUE,
  runBreakdownIndexEvents   = TRUE,
  runIncidenceRate          = TRUE,
  minCellCount              = 5
)

launchDiagnosticsExplorer("diagnostics_output/")
```

### Step B3: Read the diagnostics output

In the Shiny viewer, navigate to each section and answer these questions:

**Included Source Concepts:**
- Which source codes appear most frequently in your CDM for this cohort?
- Are there codes you expected to see that are missing?

**Orphan Concepts:**
- Are there standard concepts close to your concept set that are not included?
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
  covariateSettings     = covariateSettings
)

summary(covariateData)
```

### Step C2: Summarize and inspect

```r
# Top 20 most prevalent conditions in the cohort (prior 365 days)
tidyCovariates <- tidyCovariateData(covariateData, normalize = FALSE)
head(tidyCovariates$covariates[order(-tidyCovariates$covariates$meanValue), ], 20)
```

**Questions to answer:**
1. What are the three most prevalent prior conditions? Are they clinically expected for new metformin users?
2. What is the mean age and sex distribution of the cohort?
3. Do any covariate values surprise you?

---

## Part D: Optional — PatientLevelPrediction (Colab Notebook Path)

If CDM access is not yet fully functional, or if you want to see the full prediction workflow end-to-end without site-specific setup, use the [Colab notebook](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day6-Patient-Level-Prediction.ipynb).

The notebook demonstrates:
1. Building a synthetic target cohort and outcome cohort.
2. Creating a covariate table with FeatureExtraction (simulated).
3. Training a LASSO logistic regression model.
4. Evaluating performance: AUC-ROC, calibration, precision-recall.
5. Interpreting variable importance.

**After completing the notebook, answer:**
- What AUC-ROC did the model achieve? What does that mean in practice?
- Name one covariate with high importance. Why might it predict the outcome?
- What would you need to change to adapt this model for your own research question?

---

## Homework

- Read one CohortDiagnostics output section that surprised you and write two sentences explaining what it means for your analysis.
- Identify one question from your research area that is better suited to **population-level estimation** (CohortMethod) vs. **patient-level prediction** (PatientLevelPrediction), and explain the distinction.
- Optional: install and run Achilles on your training CDM and browse the Ares viewer output.

---

## Instructor Notes

<details>
<summary>Show facilitation notes</summary>

- **Java is the most common blocker.** Before the session, confirm each participant has Java 8 or 11 installed and that `system("java -version")` returns a clean result from within RStudio. The Databricks setup guide in the kit has platform-specific instructions.
- **CohortDiagnostics first.** Even if the group never runs CohortMethod or PatientLevelPrediction, running CohortDiagnostics on a cohort they built in Day 3 is high-value. The "Included Source Concepts" and "Orphan Concepts" tabs directly reinforce Day 2 vocabulary lessons.
- **Colab as the reliable fallback.** The Day 6 notebook runs entirely in the browser with no credentials and covers the full PLP workflow. If CDM setup is still incomplete for part of the group, route them to the notebook so no one sits idle.
- **Let the group choose Part D.** CohortMethod (comparative effectiveness) and PatientLevelPrediction (ML prediction) appeal to different personas — ask the group which they want to demo, then spend 45 minutes on that one. Leave the other for self-study with the module page as reference.
- **Interpret diagnostics clinically.** Pair a clinician or research analyst with a data analyst for the CohortDiagnostics review — the clinical person will spot patterns the data person won't, and vice versa.

</details>

---

[:material-arrow-left: Back to module: Day 6 · HADES](../modules/day-06-hades.md)
