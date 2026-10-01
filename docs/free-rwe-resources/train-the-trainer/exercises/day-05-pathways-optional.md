# Exercises · Day 5 (Optional) — Treatment Pathway Analysis

!!! tip "Sample notebook"
    Run the companion notebook in Colab (synthetic data, no credentials needed): [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day5-Treatment-Pathways.ipynb)
    or [download it](../notebooks/Day5-Treatment-Pathways.ipynb).

!!! abstract "What you will do"
    1. Define a target cohort (the population to trace) and at least three event cohorts (the treatments to track).
    2. Configure a Cohort Pathways analysis in ATLAS, including the combination window.
    3. Generate the analysis and interpret the sunburst plot and its tabular view.
    4. Adjust one parameter and compare the results.

!!! warning "Setup and extraction are site specific"
    These steps require a generated cohort in your ATLAS environment and access to a training CDM. ATLAS must be connected to a CDM that has the cohorts you created. The Colab notebook uses fully synthetic data if you need a CDM-free alternative.

---

## Background: the example analysis

This exercise uses **ALS medication sequences** as the example, because:

- ALS has few medications, so the pathways are short and easy to read
- A second medication may be added to the first or started later, which shows how combinations are handled
- The Day 2 and Day 3 exercises already built the underlying concept sets and cohorts

Adapt to your own disease area by substituting your target condition and the relevant drugs.

---

## Step 1: Assemble your cohorts

You need one **target cohort** and the **event cohorts** already created in your ATLAS instance.

**Target cohort:**
- People with a motor neuron disease diagnosis (condition-based entry, using the Day 2 concept set)

**Event cohorts (create or reuse from Day 2–3):**
- Riluzole (ingredient, include descendants)
- Edaravone (ingredient, include descendants)
- Any other ALS medication your site records, one cohort per ingredient

If you already have some of these concept sets from Day 2, build cohorts from them now. Set the entry to the first exposure and the exit to the end of continuous drug exposure with a persistence window (for example 30 days), because the exit rule is where the allowed gap between fills is set.

---

## Step 2: Configure the pathway analysis

1. In ATLAS, choose **Cohort Pathways** in the left menu, then **New**.
2. Set the **name**: `TtT Day5 ALS medication pathways`.
3. Add the **target cohort** you identified in Step 1.
4. Add each **event cohort** and give it a short label (e.g., "Riluzole," "Edaravone").
5. Configure analysis settings:
    - **Combination window** (labeled Collapse Days in some ATLAS versions): 30 days (events that start within 30 days of each other are shown as a combination).
    - **Minimum cell count:** 5 (paths with fewer people are not shown).
    - **Maximum path length:** 5 (traces up to 5 steps per person).
    - **Allow repeats:** off for the first run.
6. Save and **Generate** against your training CDM.

!!! tip "Expected wait time"
    Pathway generation may take several minutes depending on cohort size and CDM complexity. Proceed with the Colab notebook while you wait.

---

## Step 3: Interpret the sunburst plot

Once generation completes, open the **Executions** tab and choose **View reports** for that run.

**Reading the Sunburst:**

- The **center circle** = your entire target cohort.
- **Ring 1 (innermost):** the first event cohort each person entered. The size of the arc is proportional to the count, and clicking an arc shows the path with its count and percentage.
- **Ring 2:** the second step, branching from each first-step arc.
- **Grey:** the end of a pathway, meaning no further event cohort was observed during follow-up.

**Questions to answer:**
1. What is the most common first step? Is it what you expected to see?
2. After the most common first-line, what is the most common switch? Is it a switch or an add-on?
3. What fraction of the cohort has only one observable treatment step?
4. Hover over any arc — record the count and percentage.

---

## Step 4: Read the tabular view

Click **Tabular** to see the same results as a table.

**Questions to answer:**
1. Which full sequence is followed by the most people, and by what percent of the target cohort?
2. Where do the sequences diverge most, at the first to second step or the second to third?
3. Identify one sequence that you did not expect. What might explain it, including data capture (for example infusions recorded as procedures, or medication supplied outside the health system)?

---

## Step 5: Adjust one parameter and compare

Return to the pathway configuration and change one setting:

- **Option A:** Change the combination window (for example from 30 days to 1 day). Regenerate and compare: do combinations appear more or less often?
- **Option B:** Add or remove one event cohort. How do the sequences change?
- **Option C:** Restrict the target cohort to new users only (if not already done). Does the sequence pattern change?

Write one sentence per change explaining what changed and how it affects interpretation.

---

## Homework

- Identify one real research question from your work that treatment pathway analysis could address.
- Write a brief (3–5 bullet) analysis plan: target cohort, event cohorts, key parameters you would choose, and what you would expect to see.
- Optional: try the Colab notebook and compare the synthetic pathway output to your ATLAS result.

---

## Instructor Notes

<details>
<summary>Show facilitation notes</summary>

- **Reuse Day 2 and Day 3 work.** A motor neuron disease cohort built from the Day 2 concept set is the target cohort; participants only need to add the event cohorts (riluzole, edaravone, and any others) before running the analysis.
- **Show sensitivity to settings.** Have the group run the analysis with two combination windows, or with event cohorts built on two persistence windows, and compare the results.
- **Interpretation.** Invite participants to comment on whether the observed sequences match what they expected, and to offer reasons for any difference, including data capture.
- **Colab notebook as fallback.** If ATLAS or CDM access fails for part of the group, the Colab notebook demonstrates the same concept set→pathway→visualization logic on synthetic data.
- **Minimum cell count.** Remind participants that small cells are suppressed for privacy, which is a design choice and not a data quality problem.

</details>

---

[:material-arrow-left: Back to module: Day 5 · Treatment Pathways](../modules/day-05-pathways.md)
