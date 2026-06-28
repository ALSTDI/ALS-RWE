# Exercises · Day 5 (Optional) — Treatment Pathway Analysis

!!! tip "Sample notebook"
    Run the companion notebook in Colab (synthetic data, no credentials needed): [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day5-Treatment-Pathways.ipynb)
    or [download it](../notebooks/Day5-Treatment-Pathways.ipynb).

!!! abstract "What you will do"
    1. Define a target cohort (the population to trace) and at least three event cohorts (the treatments to track).
    2. Configure a treatment pathway analysis in ATLAS, including collapse gap and combination settings.
    3. Generate the analysis and interpret the Sunburst and Sankey visualizations.
    4. Adjust one parameter and compare the results.

!!! warning "Setup and extraction are site specific"
    These steps require a generated cohort in your ATLAS environment and access to a training CDM. ATLAS must be connected to a CDM that has the cohorts you created. The Colab notebook uses fully synthetic data if you need a CDM-free alternative.

---

## Background: the example analysis

This exercise uses **type 2 diabetes treatment sequences** as the clinical example, because:

- Multiple first-line treatments exist (metformin, sulfonylureas, DPP-4 inhibitors, GLP-1 agonists, insulin)
- Switching and add-on patterns are clinically meaningful
- The Day 2 and Day 3 exercises already built the underlying concept sets and cohorts

Adapt to your own disease area by substituting your target condition and relevant drug classes.

---

## Step 1: Assemble your cohorts

You need one **target cohort** and at least three **event cohorts** already created in your ATLAS instance.

**Target cohort (one of the following):**
- New users of any anti-diabetic medication (broad — good for showing diverse pathways)
- Patients newly diagnosed with type 2 diabetes (condition-based entry)

**Event cohorts (create or reuse from Day 2–3):**
- Metformin (ingredient, include descendants)
- Sulfonylureas (ingredient class, include descendants)
- DPP-4 inhibitors (e.g., sitagliptin — ingredient class)
- GLP-1 receptor agonists (e.g., semaglutide, liraglutide — ingredient class)
- Insulin (ingredient class)

If you already have some of these concept sets from Day 2, build cohorts from them now (entry = first exposure, exit = end of observation).

---

## Step 2: Configure the pathway analysis

1. In ATLAS, navigate to **Pathways** → **New Pathway Analysis**.
2. Set the **name**: `TtT Day5 T2D Pathways`.
3. Add the **target cohort** you identified in Step 1.
4. Add each **event cohort** and give it a short label (e.g., "Metformin," "Sulfonylurea").
5. Configure analysis settings:
    - **Combination window:** 30 days (allow treatments active within 30 days of each other to count as a combination).
    - **Minimum cell count:** 5 (suppresses tiny cells for privacy).
    - **Max path length:** 5 (traces up to 5 treatment steps per person).
    - **Allowed gap days:** 30 (exposures separated by ≤30 days are considered the same episode).
6. Save and **Generate** against your training CDM.

!!! tip "Expected wait time"
    Pathway generation may take several minutes depending on cohort size and CDM complexity. Proceed with the Colab notebook while you wait.

---

## Step 3: Interpret the Sunburst diagram

Once generation completes, open the **Results** tab.

**Reading the Sunburst:**

- The **center circle** = your entire target cohort.
- **Ring 1 (innermost):** the first treatment each person received. The arc width is proportional to the count. The label shows the treatment name and the percentage of the cohort.
- **Ring 2:** the second treatment, branching from each first-line treatment arc.
- **"End" arcs:** patients with no further observable treatment in the data.

**Questions to answer:**
1. What is the most common first-line treatment? Does it match your clinical expectation?
2. After the most common first-line, what is the most common switch? Is it a switch or an add-on?
3. What fraction of the cohort has only one observable treatment step?
4. Hover over any arc — record the count and percentage.

---

## Step 4: Interpret the Sankey / flow diagram

Switch to the **Sankey** view.

**Reading the Sankey:**
- Left columns = treatment steps (1, 2, 3…).
- Each ribbon = a group of patients following the same sequence.
- Ribbon width = patient count.
- "End" at any step = no further treatment observed.

**Questions to answer:**
1. Is there a dominant pathway that a large proportion of patients follow?
2. Where does the most divergence happen — at step 1→2 or 2→3?
3. Identify one pathway that surprises you clinically. What might explain it?

---

## Step 5: Adjust one parameter and compare

Return to the pathway configuration and change one setting:

- **Option A:** Change the allowed gap days from 30 to 90. Regenerate and compare — does the first-line dominant treatment change? Do combinations appear more or less frequently?
- **Option B:** Add or remove one event cohort. Does the distribution of "Other" category change?
- **Option C:** Restrict the target cohort to new users only (if not already done). Does the sequence pattern change?

Write one sentence per change explaining what changed and why it matters for interpretation.

---

## Homework

- Identify one real research question from your work that treatment pathway analysis could address.
- Write a brief (3–5 bullet) analysis plan: target cohort, event cohorts, key parameters you would choose, and what you would expect to see.
- Optional: try the Colab notebook and compare the synthetic pathway output to your ATLAS result.

---

## Instructor Notes

<details>
<summary>Show facilitation notes</summary>

- **Reuse Day 3 cohorts.** The metformin new-user cohort is an ideal target cohort; participants only need to add the additional event cohorts (sulfonylurea, DPP-4, etc.) before running the analysis.
- **Collapse gap sensitivity is the most teachable moment.** Have the group run the analysis once at 30 days and once at 90 days and compare. The change in combination therapy rates is usually dramatic and immediately intuitive.
- **Clinical vs. data interpretation.** Invite participants with clinical backgrounds to comment on whether the observed sequences match clinical guidelines or patient experience. The gap is the interesting finding.
- **Colab notebook as fallback.** If ATLAS or CDM access fails for part of the group, the Colab notebook demonstrates the same concept set→pathway→visualization logic on synthetic data.
- **Minimum cell count.** Remind participants that small cells are suppressed for privacy — this is not a data quality problem, it is a feature.

</details>

---

[:material-arrow-left: Back to module: Day 5 · Treatment Pathways](../modules/day-05-pathways.md)
