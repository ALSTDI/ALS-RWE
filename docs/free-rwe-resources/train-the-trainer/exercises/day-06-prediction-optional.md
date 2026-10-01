# Exercises · Day 6, Part 2 (Optional): Patient-Level Prediction

!!! tip "Sample notebook"
    Run the companion notebook in Colab (synthetic data, no credentials needed): [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day6-Patient-Level-Prediction.ipynb)
    or [download it](../notebooks/Day6-Patient-Level-Prediction.ipynb).

!!! abstract "What you will do"
    1. State a prediction problem as a target cohort, an outcome cohort, and a time-at-risk.
    2. Run the PatientLevelPrediction workflow against your training CDM, or follow the same steps in the Colab notebook.
    3. Read the AUC and the calibration output.
    4. Change one design choice and compare the results.

!!! warning "Setup is site specific"
    This lab reuses the R environment, the connection details, and the dedicated cohort table from [Day 6, Part 1](day-06-hades-optional.md). If your CDM connection is not working yet, do Path B with the Colab notebook.

---

## Step 1: State the prediction problem

Write one sentence in this form before you run anything:

> Among **[target cohort]**, who will have **[outcome]** within **[time-at-risk]** of cohort entry?

For the guided lab, the target cohort is the new-user metformin cohort (cohort ID 1) and the outcome is the cohort you added as homework in Part 1 (cohort ID 2), with a time-at-risk of 1 to 365 days after cohort entry.

---

## Step 2, Path A: Run the workflow in R

Use the code block on the [Part 2 module page](../modules/day-06-prediction.md). Work through it in order:

1. `createDatabaseDetails()` names the CDM schema, the cohort table, the target cohort ID, and the outcome cohort ID.
2. `createCovariateSettings()` chooses the covariates.
3. `getPlpData()` extracts the data.
4. `createStudyPopulationSettings()` sets the time-at-risk and the handling of people who had the outcome before entry.
5. `runPlp()` splits the data, trains a lasso logistic regression, and evaluates it on the test set.
6. `plotPlp()` writes the evaluation plots.

After each step, note what the step returned and how long it took.

## Step 2, Path B: Follow the Colab notebook

The notebook uses a synthetic CDM and Python to show the same sequence: a target cohort, an outcome, covariates, a train and test split, a model, AUC, and calibration. It teaches the sequence of steps in a prediction study and does not run the PatientLevelPrediction package itself.

---

## Step 3: Read the results

Answer these from your output:

1. What is the AUC on the test set? What does that value say about how well the model ranks people?
2. In the calibration output, where do predicted and observed risk agree, and where do they differ?
3. Which covariates have the largest coefficients? Why would it be a mistake to read them as causes of the outcome?
4. How many people in the target cohort had the outcome during the time-at-risk? Is that enough to trust the evaluation?

---

## Step 4: Change one design choice

Change one thing, rerun, and compare:

- **Time-at-risk:** change `riskWindowEnd` from 365 to 180.
- **Covariates:** add or remove one group of covariates.
- **Prior outcomes:** switch `removeSubjectsWithPriorOutcome`.

Write one sentence on what changed in the population size, the AUC, and the calibration, and why.

---

## Homework

- Identify one question from your research area that calls for **patient-level prediction** and one that calls for **population-level estimation**, and explain the difference.
- Write a short plan for external validation: which other database could the model be tested on, and what would you expect to differ?

---

## Instructor Notes

<details>
<summary>Show facilitation notes</summary>

- **Check the cohorts before the session.** The lab needs the target and outcome cohorts in the cohort table from Part 1. An outcome that is very rare in the training CDM will make the evaluation unstable; choose a more common outcome for teaching if needed.
- **Route by access.** Participants with a working connection do Path A; everyone else does Path B. Bring both groups together for Step 3 so the interpretation is shared.
- **No fixed answers.** The AUC and the calibration depend on the database and the outcome. Ask for the value and a reason, and avoid presenting a range as expected.
- **Risk is not effect.** When a participant reads a covariate as a cause, return to the difference between prediction and estimation.

</details>

---

[:material-arrow-left: Back to module: Day 6, Part 2](../modules/day-06-prediction.md)
