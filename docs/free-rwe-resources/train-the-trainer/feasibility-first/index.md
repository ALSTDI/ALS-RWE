# Feasibility First — Is My Question Feasible?

**A 30-minute exemplar for researchers new to OMOP/OHDSI.** It takes the position of a fellow who has a real question but does not yet know who to contact, what to ask, or whether the data can answer it, and walks from zero to a defensible go/no-go decision using the public ATLAS demo.

!!! note "About the running example"
    This module was developed as a use case for the **JHU OHDSI MCH Fellowship**, so the running example is a pregnancy question (pregestational diabetes and preeclampsia). The **workflow is disease-agnostic** — the steps, checks, and tools are identical for any condition. Swap in your own target population, exposure, and outcome wherever the pregnancy example appears; nothing else changes.

[Start the walkthrough :material-arrow-right:](04-atlas-feasibility-walkthrough.md){ .md-button .md-button--primary }
[Jump to the go/no-go checklist :material-checkbox-multiple-marked:](06-feasibility-checklist.md){ .md-button }
[Instructor kit & slides :material-download:](../training/feasibility-first/kit/README.md){ .md-button }

!!! abstract "Objectives"
    By the end of this module you will be able to:

    1. Turn a loose research idea into a feasibility-testable specification (a cohort you could build).
    2. Identify who owns your institution's OMOP instance and ask the right questions.
    3. Read a standardized vocabulary well enough to tell whether your concepts exist and are mapped.
    4. Use ATLAS to test concept presence and cohort counts, and read what those counts do and do not prove.
    5. Decide whether the question is feasible here, feasible via the network, or needs reframing, before you write a protocol.

## Why this module sits at the front

The daily curriculum (Days 1–6) teaches you to build. This module teaches you to check first. Feasibility assessment is cheap; running a study on the wrong data is expensive. The whole point is to move the moment you discover a question cannot be answered from month six to minute five.

The public ATLAS demo makes that vivid. It runs on synthetic Medicare data (SynPUF), so diabetes concepts are abundant but pregnancies are absent. Watching a healthy cohort count collapse the instant you add a childbearing-age requirement is the lesson. That same collapse, caught early against your real instance, is a saved year.

## The running example

> Among pregnant people with pregestational diabetes (type 1 or type 2, diagnosed before the pregnancy), how often does preeclampsia occur, and does that differ by first-trimester glucose-lowering medication (metformin versus insulin)?

Swap in your own question wherever you like. The steps do not change.

## The 30-minute path

| Time | Segment | Page |
|:--|:--|:--|
| 0–4 min | Framing and the feasibility mindset | this page |
| 4–9 min | Sharpen the question into cohort logic | [Sharpen the question](01-sharpen-the-question.md) |
| 9–14 min | Who to contact and what to ask | [Find your data steward](02-find-your-data-steward.md) |
| 14–18 min | Vocabulary and CDM essentials | [Vocabulary & CDM primer](03-vocab-and-cdm-primer.md) |
| 18–26 min | Live ATLAS demo: test feasibility | [ATLAS feasibility walkthrough](04-atlas-feasibility-walkthrough.md) |
| 26–29 min | When one site is not enough: the network | [Network feasibility](05-network-feasibility.md) |
| 29–30 min | Your go/no-go decision | [Feasibility checklist](06-feasibility-checklist.md) |

Facilitators should also read the [Facilitator notes](07-facilitator-notes.md) and the [checks-to-tools appendix](08-checks-to-tools.md).

## How this connects to the rest of the curriculum

This module is a fast, self-contained on-ramp. When you are ready to go deeper on any step, the core curriculum has the full treatment:

- Vocabulary and concepts in depth: [Day 1 · OMOP CDM](../modules/day-01-omop-cdm.md) and [Day 2 · Vocabulary & Data Quality](../modules/day-02-vocab-dqd.md).
- Cohort definition mechanics: [Day 3 · Cohort Definition](../modules/day-03-cohorts.md).
- Extraction and site-specific validation: [Day 4 · Data Extraction](../modules/day-04-extraction.md).

---

## Slides and materials

| File | Description |
|:--|:--|
| [Instructor Deck with Notes](../training/feasibility-first/kit/Feasibility-Instructor-Deck-with-Notes.pptx) | Full 30-minute deck with the presenter script in the speaker notes |
| [Importable ATLAS cohort (JSON)](../training/feasibility-first/kit/Demo-Cohort-Diabetes-Childbearing-Age.json) | Ready-to-import demo cohort; import into atlas-demo and save |
| [Kahoot Quiz (CSV)](../training/feasibility-first/kit/Kahoot-Quiz.csv) | 10-question quiz on the feasibility workflow |
| [Kit README](../training/feasibility-first/kit/README.md) | Setup steps, concept IDs, and the full-clinical-cohort notes |
