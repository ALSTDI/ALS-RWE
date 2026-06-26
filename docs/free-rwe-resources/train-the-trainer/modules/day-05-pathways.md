# :material-chart-sankey: Day 5 · Treatment Pathway Analysis (Optional)

!!! abstract "Objectives"
    By the end of Day 5 you will be able to:

    1. Explain what treatment pathway analysis is and what research questions it answers.
    2. Identify the two required cohort types: a target cohort and one or more event cohorts.
    3. Configure a pathway analysis in ATLAS, including collapse settings and allowed gap days.
    4. Run a pathway analysis and interpret the Sunburst and Sankey visualizations.
    5. Summarize one analytical insight from a pathway result.

---

## What treatment pathway analysis is

Treatment pathway analysis describes the real-world sequence of treatments a population receives over time. Instead of asking "how many patients took drug X," it asks: "among patients with condition Y, what was the first treatment? The second? How often do patients switch? How often do they discontinue?"

The result is a visualization — typically a Sunburst diagram or Sankey flow — that shows the distribution of treatment sequences across your cohort.

This type of analysis is well-suited to OMOP data because it operates on standardized drug exposures and requires only a defined target population and a set of drugs or procedures to trace.

---

## Key concepts

### Target cohort
The population you want to study. This is typically a condition-based cohort you already built — for example, new users of any anti-diabetic medication, or patients with a first ALS diagnosis. The analysis traces treatment sequences *within* this population.

### Event cohorts
The treatments or procedures you want to track. Each event cohort defines one "step" in the sequence — for example, separate cohorts for metformin, sulfonylureas, GLP-1 agonists. ATLAS traces which event cohorts each person passes through, in order.

### Collapse settings
Exposures that are close together (within a specified gap) can be collapsed into a single episode. The **collapse gap** (allowed gap days) controls how tolerant the analysis is of short interruptions in treatment — important because pharmacy fill dates rarely align perfectly.

### Analysis parameters
- **Combination window:** whether to allow combination therapies (two event cohorts active simultaneously).
- **Minimum cell count:** suppresses small cells for privacy.
- **Max path length:** the maximum number of steps to trace per person.

---

## Agenda

| Time | Topic |
|:--|:--|
| 09:00 – 09:30 | Overview: what pathway analysis answers and when to use it |
| 09:30 – 10:15 | Concept review: target cohorts, event cohorts, collapse settings |
| 10:15 – 10:30 | Break |
| 10:30 – 11:30 | Hands-on: building a pathway analysis in ATLAS |
| 11:30 – 12:00 | Interpreting Sunburst and Sankey diagrams |
| 12:00 – 13:00 | Lunch |
| 13:00 – 14:00 | Advanced: combinations, gap settings, multi-site comparisons |
| 14:00 – 14:45 | Group discussion: interpreting a pathway result |
| 14:45 – 15:15 | Recap & homework |

---

## Slides & Materials

- :material-presentation: **Instructor deck with notes:** [Download PPTX](../training/day-05-treatment-pathways/kit/Instructor-Deck-with-Notes.pptx)
- :material-notebook: **Participant workbook:** [Download PPTX](../training/day-05-treatment-pathways/kit/Participant-Workbook.pptx)
- :material-help-circle: **Kahoot quiz (CSV):** [Download](../training/day-05-treatment-pathways/kit/Kahoot-Quiz.csv)
- :material-file-document: **Participant handout:** [Download PPTX](../training/day-05-treatment-pathways/kit/Participant-Handout.pptx)
- :material-key: **Answer key (instructor):** [Download PPTX](../training/day-05-treatment-pathways/kit/Instructor-Answer-Key.pptx)
- :material-presentation-play: **Live demo script:** [Download PPTX](../training/day-05-treatment-pathways/kit/Live-Demo-Script.pptx)
- :material-chart-donut: **Diabetes pathway interpretation guide:** [Download PPTX](../training/day-05-treatment-pathways/kit/Diabetes-Pathway-Interpretation-Guide.pptx)
- :material-flask: **Colab notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day5-Treatment-Pathways.ipynb)

---

## Interpreting the Output

### Sunburst diagram
The center represents your entire target cohort. Each ring outward represents the next treatment step. Arc width is proportional to the number of patients. Colors encode treatment groups. Hover to see counts and percentages.

**What to look for:**
- The dominant first-line treatment (the largest arc in ring 1).
- How quickly the population disperses into different sequences by ring 2 or 3.
- Whether a meaningful fraction discontinues without a second treatment ("end" arcs).

### Sankey / flow diagram
A left-to-right flow diagram where each vertical band is a treatment step and each ribbon is a group of patients moving through the same sequence. Width is proportional to patient count.

**What to look for:**
- Major flows that converge (common sequences) vs. dispersal (heterogeneous treatment).
- Switch patterns — does a particular first-line treatment predict a particular second-line?
- Loss to follow-up — how many patients have observable sequences vs. single steps only.

---

## Instructor Notes

- **Reuse Day 3 cohorts.** The new-user metformin cohort from Day 3 can serve as the target cohort here with minimal setup, letting the group focus on the pathway configuration rather than cohort building.
- **Demonstrate collapse gap sensitivity.** Show the group what changes when you set 30-day vs. 90-day allowed gaps — this is the most common source of confusion about pathway results.
- **Invite clinical interpretation.** Ask participants with clinical backgrounds whether the dominant first-line sequence matches what they would expect from guidelines. Gaps between guidelines and observed data are the point.
- **Synthetic data caveat.** The Colab notebook uses synthetic data; real pathway results will look very different. The goal of the notebook is to practice the mechanics.

---

## Further Reading

- Book of OHDSI, Chapter 12 (Estimation): [ohdsi.github.io/TheBookOfOhdsi](https://ohdsi.github.io/TheBookOfOhdsi/)
- ATLAS Treatment Pathways documentation: [OHDSI Software Tools](https://ohdsi.org/software-tools/)
- **Hripcsak G et al.** *Characterizing treatment pathways at scale using the OHDSI network.* PNAS 2016. [doi:10.1073/pnas.1510502113](https://doi.org/10.1073/pnas.1510502113)

---

:material-arrow-left: [Day 4 · Data Extraction](day-04-extraction.md) &emsp; :material-arrow-right: [Day 6 · HADES (Optional)](day-06-hades.md)
