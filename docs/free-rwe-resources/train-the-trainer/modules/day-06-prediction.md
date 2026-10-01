# :material-chart-bell-curve: Day 6, Part 2 · HADES: Patient-Level Prediction (Optional)

!!! info "Day 6 is taught as separate sessions"
    [Part 1](day-06-hades.md) covers the HADES environment, CohortDiagnostics, and FeatureExtraction. Part 2 (this page) covers patient-level prediction with the PatientLevelPrediction package. Each part is its own half-day session. Part 2 reuses the connection details and the dedicated cohort table from Part 1.

!!! abstract "Objectives"
    By the end of Part 2 you will be able to:

    1. State a prediction problem as a target cohort, an outcome cohort, and a time-at-risk.
    2. Explain how prediction differs from population-level estimation.
    3. Follow the PatientLevelPrediction workflow: extract data, define the study population, train a model, evaluate it.
    4. Read discrimination (AUC) and calibration output and say what each one tells you.
    5. Explain why internal validation is a minimum and what external validation adds.

---

## The prediction problem

A patient-level prediction question has a fixed shape: among a **target cohort**, who will go on to have an **outcome** during a **time-at-risk**? For this session, the target cohort is the new-user riluzole cohort from Day 3, the outcome is a cohort you define in ATLAS, and the time-at-risk is the year after cohort entry.

Prediction estimates a person's risk of an outcome. It does not estimate the effect of a treatment. A covariate that predicts the outcome well is not shown to cause it, and a prediction model cannot tell you what would happen if care were changed. Questions about effects belong to population-level estimation (CohortMethod), which this program leaves for self-study.

---

## Agenda

| Time | Topic |
|:--|:--|
| 9:30 – 9:50 | Prediction versus estimation; stating the prediction problem |
| 9:50 – 10:30 | The PatientLevelPrediction workflow: data, population, model, evaluation |
| 10:30 – 10:45 | Break |
| 10:45 – 11:15 | Live demo |
| 11:15 – 12:15 | Lab: run a model against your CDM, or use the Colab notebook with synthetic data |
| 12:15 – 12:45 | Interpreting discrimination and calibration |
| 12:45 – 1:00 | Recap and next steps |

---

## The workflow in R

!!! warning "Site-specific setup"
    This block reuses `connectionDetails`, `cdmDatabaseSchema`, `cohortDatabaseSchema`, and `cohortTable` from [Part 1](day-06-hades.md). The target cohort (ID 1) and the outcome cohort (ID 2) must already be generated in that cohort table.

```r
library(PatientLevelPrediction)
library(FeatureExtraction)

# 1. Where the data and the cohorts are
databaseDetails <- createDatabaseDetails(
  connectionDetails     = connectionDetails,
  cdmDatabaseSchema     = cdmDatabaseSchema,
  cdmDatabaseName       = "[your site name]",
  cohortDatabaseSchema  = cohortDatabaseSchema,
  cohortTable           = cohortTable,
  targetId              = 1,
  outcomeDatabaseSchema = cohortDatabaseSchema,
  outcomeTable          = cohortTable,
  outcomeIds            = 2
)

# 2. Which covariates to build (the year before cohort entry)
covariateSettings <- createCovariateSettings(
  useDemographicsGender        = TRUE,
  useDemographicsAge           = TRUE,
  useConditionGroupEraLongTerm = TRUE,
  useDrugGroupEraLongTerm      = TRUE,
  longTermStartDays            = -365,
  endDays                      = -1
)

# 3. Extract the data
plpData <- getPlpData(
  databaseDetails         = databaseDetails,
  covariateSettings       = covariateSettings,
  restrictPlpDataSettings = createRestrictPlpDataSettings()
)

# 4. Who is at risk, and for how long
populationSettings <- createStudyPopulationSettings(
  removeSubjectsWithPriorOutcome = TRUE,
  riskWindowStart   = 1,
  riskWindowEnd     = 365,
  startAnchor       = "cohort start",
  endAnchor         = "cohort start",
  requireTimeAtRisk = TRUE,
  minTimeAtRisk     = 364
)

# 5. Train a model and evaluate it on a held-out test set
plpResult <- runPlp(
  plpData            = plpData,
  outcomeId          = 2,
  analysisId         = "ttt_day6_part2",
  populationSettings = populationSettings,
  splitSettings      = createDefaultSplitSetting(
    trainFraction = 0.75, testFraction = 0.25,
    type = "stratified", nfold = 2, splitSeed = 1234
  ),
  modelSettings      = setLassoLogisticRegression(),
  saveDirectory      = "plp_output"
)

# 6. Look at the results
plotPlp(plpResult, dirPath = "plp_output/plots")
```

!!! note "Check the function names against your installed version"
    This block follows the PatientLevelPrediction vignette "Building patient-level predictive models" as read on 1 October 2026. It was not run against a database when this page was written, and the package interface has changed between major versions. Compare it with the [PatientLevelPrediction documentation](https://ohdsi.github.io/PatientLevelPrediction/) for the version you have installed.

---

## Reading the results

- **Discrimination (AUC):** how well the model ranks people who have the outcome above people who do not. An AUC of 0.5 means no discrimination, and 1.0 means perfect ranking. The value depends on the outcome, the covariates, and the database, so no fixed range is expected.
- **Calibration:** whether predicted risk agrees with observed risk across the range of predictions. A model can rank people well and still give risks that are too high or too low.
- **Internal validation:** performance on the held-out test set, which guards against judging a model on the data it was trained on.
- **External validation:** performance on a different database. A model that performs well at one site can perform differently elsewhere because populations and data capture differ.

---

## Slides & Materials

- :material-presentation: **Instructor deck:** [Download PPTX](../training/day-06-hades/kit/Instructor-Deck.pptx)
- :material-notebook: **Participant workbook:** [Download PPTX](../training/day-06-hades/kit/Participant-Workbook.pptx)
- :material-help-circle: **Kahoot quiz (CSV):** [Download](../training/day-06-hades/kit/Kahoot-Quiz.csv)
- :material-file-document: **Participant handout:** [Download PPTX](../training/day-06-hades/kit/Participant-Handout.pptx)
- :material-key: **Instructor answer key:** [Download PPTX](../training/day-06-hades/kit/Instructor-Answer-Key.pptx)
- :material-presentation-play: **Live demo script:** [Download PPTX](../training/day-06-hades/kit/Live-Demo-Script.pptx)
- :material-chart-bar: **Prediction interpretation guide:** [Download PPTX](../training/day-06-hades/kit/Prediction-Interpretation-Guide.pptx)
- :material-database-settings: **Databricks setup guide (placeholder template):** [Download PPTX](../training/day-06-hades/kit/Databricks-Setup-Placeholder-Guide.pptx)
- :material-flask: **Colab notebook (synthetic data, no credentials):** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day6-Patient-Level-Prediction.ipynb)

The hands-on lab is on the [Part 2 exercise](../exercises/day-06-prediction-optional.md) page.

---

## Instructor Notes

- **Confirm the cohorts first.** Before the session, check that the target and outcome cohorts exist in the cohort table from Part 1 and that the outcome is not too rare to model in your training CDM.
- **Use the Colab notebook when access is incomplete.** It uses synthetic data and Python to show the same sequence of steps (cohort, covariates, train and test split, AUC, calibration), so participants without a working R connection can still follow the session.
- **Keep prediction and effect apart.** Return to the difference between risk and effect whenever a participant reads a coefficient as a cause.

---

## Further Reading

- Book of OHDSI, Chapter 13 (Patient-Level Prediction): [ohdsi.github.io/TheBookOfOhdsi/PatientLevelPrediction.html](https://ohdsi.github.io/TheBookOfOhdsi/PatientLevelPrediction.html)
- [PatientLevelPrediction documentation](https://ohdsi.github.io/PatientLevelPrediction/)
- [HADES package documentation](https://ohdsi.github.io/Hades/)
- [Network Study Paint By Numbers](https://www.boycedatascience.com/network-study-paint-by-numbers){target="_blank"}, for planning a study that runs across sites
- [Manuscript Paint by Numbers](https://www.boycedatascience.com/manuscript-paint-by-numbers){target="_blank"}, for writing up the results

---

:material-arrow-left: [Day 6, Part 1 · HADES: Cohort Diagnostics and Feature Extraction (Optional)](day-06-hades.md)
