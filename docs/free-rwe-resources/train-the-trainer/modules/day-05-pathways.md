# :material-chart-sankey: Day 5 · Treatment Pathway Analysis (Optional)

!!! abstract "Objectives"
    By the end of Day 5 you will be able to:

    1. Explain what treatment pathway analysis is and what research questions it answers.
    2. Identify the two required cohort types: a target cohort and one or more event cohorts.
    3. Configure a Cohort Pathways analysis in ATLAS: combination window, minimum cell count, maximum path length, and allow repeats.
    4. Run the analysis and interpret the sunburst plot and its tabular view.
    5. Summarize one analytical insight from a pathway result.

---

## What treatment pathway analysis is

Treatment pathway analysis describes the real-world sequence of treatments a population receives over time. Instead of asking "how many patients took drug X," it asks: "among patients with condition Y, what was the first treatment? The second? How often do patients switch? How often do they discontinue?"

In ATLAS the feature is named Cohort Pathways, and the result is a sunburst plot with a tabular view that shows the distribution of treatment sequences across your cohort. Sankey diagrams of pathways come from the separate TreatmentPatterns R package, not from ATLAS.

This type of analysis is well-suited to OMOP data because it operates on standardized drug exposures and requires only a defined target population and a set of drugs or procedures to trace.

---

## Key concepts

### Target cohort
The population you want to study, for example new users of any anti-diabetic medication, or patients with a first ALS diagnosis. The analysis traces treatment sequences *within* this population.

### Event cohorts
The treatments or procedures you want to track. Each event cohort defines one "step" in the sequence — for example, separate cohorts for metformin, sulfonylureas, GLP-1 agonists. ATLAS traces which event cohorts each person passes through, in order.

### Where exposure length and gaps are set
Cohort Pathways has no gap or persistence setting of its own. How long an exposure lasts, and how many days without supply are tolerated before the exposure ends, are set in each **event cohort's exit rule** (for example, end of continuous drug exposure with a 30-day persistence window). Follow-up time comes from the target cohort's entry and exit.

### Analysis settings
- **Combination window** (labeled Collapse Days in some ATLAS versions): events whose start dates fall within this number of days of each other are given the earliest date and shown as one combined step. It is about how close the dates are, not how long the exposures overlap.
- **Minimum cell count:** paths followed by fewer people than this are not shown.
- **Maximum path length:** the maximum number of steps to trace per person.
- **Allow repeats:** whether the same event (or combination) can appear more than once in a path.

---

## Agenda

| Time | Topic |
|:--|:--|
| 9:30 – 9:50 | Overview: what pathway analysis answers and when to use it |
| 9:50 – 10:30 | Cohort Pathways in ATLAS: target cohorts, event cohorts, settings (lead deck) |
| 10:30 – 10:45 | Break |
| 10:45 – 11:15 | Worked example: type 2 diabetes (worked example deck and live demo) |
| 11:15 – 12:15 | Hands-on: build and run a pathway analysis |
| 12:15 – 12:45 | Reading the sunburst plot and the Tabular view; group discussion |
| 12:45 – 1:00 | Recap and homework |

Day 5 is a half-day session. The times follow the sample schedule on the program overview page; shift them to suit your group.

---

## Slides & Materials

- :material-presentation: **Lead instructor deck (Cohort Pathways in ATLAS):** [Download PPTX](../training/day-05-treatment-pathways/kit/ATLAS-Treatment-Pathways-Training.pptx)
- :material-presentation: **Worked example deck (type 2 diabetes), with notes:** [Download PPTX](../training/day-05-treatment-pathways/kit/Instructor-Deck-with-Notes.pptx)
- :material-notebook: **Participant workbook:** [Download PPTX](../training/day-05-treatment-pathways/kit/Participant-Workbook.pptx)
- :material-help-circle: **Kahoot quiz (CSV):** [Download](../training/day-05-treatment-pathways/kit/Kahoot-Quiz.csv)
- :material-file-document: **Participant handout:** [Download PPTX](../training/day-05-treatment-pathways/kit/Participant-Handout.pptx)
- :material-key: **Answer key (instructor):** [Download PPTX](../training/day-05-treatment-pathways/kit/Instructor-Answer-Key.pptx)
- :material-presentation-play: **Live demo script:** [Download PPTX](../training/day-05-treatment-pathways/kit/Live-Demo-Script.pptx)
- :material-chart-donut: **Diabetes pathway interpretation guide:** [Download PPTX](../training/day-05-treatment-pathways/kit/Diabetes-Pathway-Interpretation-Guide.pptx)
- :material-flask: **Colab notebook:** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ALSTDI/ALS-RWE/blob/main/docs/free-rwe-resources/train-the-trainer/notebooks/Day5-Treatment-Pathways.ipynb)

---

## Interpreting the Output

### Sunburst plot
The center represents the target cohort. Each ring outward represents the next step in the sequence, and the size of an arc is proportional to the number of people on that path. Colors identify the event cohorts and their combinations, and clicking an arc shows the path details with counts and percentages. The Tabular button shows the same results as a table.

**What to look for:**
- The largest arcs in the first ring, which are the most common first steps.
- How quickly the population spreads across different sequences by the second or third ring.
- How many paths stop after one step. The end of a pathway is shown in grey, which means no further event cohort was observed during follow-up.

People in the target cohort who never enter any event cohort are left out of the analysis, so read the count of people with a pathway next to the size of the target cohort.

### If you need a Sankey diagram
ATLAS does not draw one. The TreatmentPatterns R package computes pathways outside ATLAS and offers Sankey and sunburst output, with its own settings for era collapse and minimum era duration. Those settings are not part of ATLAS Cohort Pathways.

---

## Instructor Notes

- **Reuse Day 3 cohorts.** The new-user metformin cohort from Day 3 can serve as the target cohort here with minimal setup, letting the group focus on the pathway configuration rather than cohort building.
- **Demonstrate sensitivity to the event cohort exit rule.** Build one event cohort twice, with a 30-day and a 90-day persistence window, and show the group how the pathway changes. Then change the combination window and compare again.
- **Invite interpretation.** Ask participants whether the most common first step matches what they expected, and discuss possible reasons for any difference, including data capture.
- **Synthetic data caveat.** The Colab notebook uses synthetic data; real pathway results will look very different. The goal of the notebook is to practice the mechanics.

---

## Further Reading

- Book of OHDSI, Chapter 11 (Characterization), sections 11.3 (Treatment Pathways) and 11.9 (Cohort Pathways in ATLAS): [ohdsi.github.io/TheBookOfOhdsi/Characterization.html](https://ohdsi.github.io/TheBookOfOhdsi/Characterization.html)
- OHDSI forum thread on Cohort Pathways settings: [Cohort Pathways in Atlas FAQ](https://forums.ohdsi.org/t/cohort-pathways-in-atlas-faq/9511)
- **Hripcsak G et al.** *Characterizing treatment pathways at scale using the OHDSI network.* PNAS 2016. [doi:10.1073/pnas.1510502113](https://doi.org/10.1073/pnas.1510502113)

---

:material-arrow-left: [Day 4 · Data Extraction](day-04-extraction.md) &emsp; :material-arrow-right: [Day 6, Part 1 · HADES: Cohort Diagnostics (Optional)](day-06-hades.md)
