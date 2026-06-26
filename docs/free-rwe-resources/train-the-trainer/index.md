# OHDSI/OMOP Train-the-Trainer

**A hands-on, multi-session curriculum for analysts, researchers, and trainers** building expertise in the OHDSI ecosystem — from data model fundamentals to advanced analytics.

[Start with Environment Setup :material-arrow-right:](modules/00-environment-walkthrough.md){ .md-button .md-button--primary }
[Jump to Syllabus :material-book-open-variant:](syllabus.md){ .md-button }
[Find Your Learning Path :material-map-marker-path:](personas.md){ .md-button }

---

## Program at a Glance

<div class="grid cards" markdown>

-   :material-school:{ .lg .middle } **6 Core Sessions + 2 Optional**

    ---

    Build from OMOP CDM fundamentals through cohort building, data extraction, treatment pathways, and HADES analytics.

    [:material-arrow-right: View full syllabus](syllabus.md)

-   :material-flask-outline:{ .lg .middle } **Hands-On Labs**

    ---

    Every session includes guided SQL exercises, Atlas walkthroughs, and Colab-ready Python notebooks with synthetic data.

    [:material-arrow-right: Browse exercises](exercises/day-01-athena-cdm.md)

-   :material-account-group:{ .lg .middle } **Community & Support**

    ---

    Weekly community meetings, open office hours, and a growing FAQ to support learners and trainers alike.

    [:material-arrow-right: Join the community](community/weekly-meeting.md)

-   :material-download:{ .lg .middle } **All Materials Included**

    ---

    Slide kits, Jupyter notebooks, SQL cheat sheets, environment templates, and ALS TDI branded PowerPoint decks.

    [:material-arrow-right: Downloads & Resources](resources.md)

</div>

---

## The Curriculum

The program is organized in a deliberate sequence. Each session builds on the previous one — start at Day 0 (environment) and progress through the core four, then continue with the optional advanced sessions.

### Core Track (Required)

| Session | Focus | Module | Exercise |
|:--|:--|:--|:--|
| :material-wrench: **Module 0** — Environment Setup | Verify access to all tools and data | [Module](modules/00-environment-walkthrough.md) | [Handout](common_artifacts/environment-setup-handout.md) |
| :material-database: **Day 1** — OMOP Common Data Model | CDM structure, tables, Athena vocabularies | [Module](modules/day-01-omop-cdm.md) | [Exercise](exercises/day-01-athena-cdm.md) · [SQL Snippets](exercises/code_snippets/day-01-snippets.md) |
| :material-tag-multiple: **Day 2** — Vocabulary & Data Quality | Concept sets in Atlas, DQD, SQL validation | [Module](modules/day-02-vocab-dqd.md) | [Exercise](exercises/day-02-vocab-dqd.md) |
| :material-account-filter: **Day 3** — Cohort Definition | Building and characterizing cohorts in ATLAS | [Module](modules/day-03-cohorts.md) | [Exercise](exercises/day-03-cohorts.md) |
| :material-export: **Day 4** — Data Extraction | Site-specific extraction and validation | [Module](modules/day-04-extraction.md) | [Exercise](exercises/day-04-extraction.md) |

### Optional / Advanced Track

| Session | Focus | Module | Exercise |
|:--|:--|:--|:--|
| :material-chart-sankey: **Day 5** — Treatment Pathways | Sequence-of-care analysis in ATLAS | [Module](modules/day-05-pathways.md) | [Exercise](exercises/day-05-pathways-optional.md) |
| :material-code-braces: **Day 6** — HADES | R-based analytics: characterization, estimation, prediction | [Module](modules/day-06-hades.md) | [Exercise](exercises/day-06-hades-optional.md) |

---

## How to Use This Site

!!! tip "For Participants"

    1. **Complete Module 0** before anything else — verify your tool access at least 48 hours before Day 1.
    2. **Follow the core track in order.** Each day's module has an agenda, objectives, slides, and a matching exercise.
    3. **Use the Common Artifacts** for cheat sheets, SQL templates, and the environment checklist.
    4. **Notebooks are always available.** Each exercise page has a Colab badge — run it with synthetic data even without CDM access.

!!! tip "For Trainers"

    1. **Fork this repository** and fill in site-specific details (warehouse, SQL client, ATLAS URL) in the Day 4 module and Environment pages.
    2. **Use the branded templates** from the [Downloads & Resources](resources.md) page for any new decks.
    3. **Instructor notes** are embedded (collapsed) in each exercise page — expand them before your session.
    4. **Host community meetings** using the [Community](community/weekly-meeting.md) pages as a template.

---

## Sample Schedule

This schedule reflects one delivery of the program. Sessions run approximately 3.5 hours each.

| Session | Suggested Date | Focus |
|:--|:--|:--|
| Environment Walk-through | Fri, Oct 31 · 12:00–1:00 | Access check for data and tools |
| Day 1 — OMOP Common Data Model | Fri, Nov 7 · 9:30–1:00 | Schema, key tables, Athena |
| Day 2 — Vocabulary & Data Quality | Fri, Nov 14 · 9:30–1:00 | Concept sets, DQD principles |
| Day 3 — Cohort Definition w/ ATLAS | Fri, Nov 21 · 9:30–1:00 | Cohorts and characterization |
| Day 4 — Data Extraction Tools | Mon, Dec 1 · 9:30–1:00 | Build analytic datasets |
| Post-training Q&A | Fri, Dec 12 · 11:30–1:00 | Q&A, next steps |
| Day 5 (Optional) — Treatment Pathways | Fri, Jan 9 · 9:30–1:00 | Sequences of care |
| Day 6 (Optional) — HADES | Fri, Jan 16 · 9:30–1:00 | R-based analytics framework |

---

## Common Artifacts

These shared resources are used across multiple sessions:

<div class="grid cards" markdown>

-   :material-file-document:{ .lg .middle } **Environment Setup Handout**

    ---

    One-page pre-session participant checklist.

    [:material-arrow-right: View handout](common_artifacts/environment-setup-handout.md)

-   :material-code-tags:{ .lg .middle } **OMOP Vocabulary & SQL Cheat Sheet**

    ---

    Key queries for concepts, ancestors, cohort counts, and more.

    [:material-arrow-right: View cheat sheet](common_artifacts/omop-vocab-sql-cheat-sheet.md)

-   :material-test-tube:{ .lg .middle } **SQL Validation Mini Lab**

    ---

    Step-by-step guide: export Atlas SQL, validate in your client, compare outputs.

    [:material-arrow-right: Open lab](common_artifacts/sql-validation-mini-lab.md)

-   :material-checkbox-multiple-marked:{ .lg .middle } **Environment Checklist Template**

    ---

    Trainer-ready checklist to track participant readiness per tool.

    [:material-arrow-right: Download template](common_artifacts/environment-checklist-template.md)

</div>

---

All content in `docs/` is version-controlled. Updates and new contributions are tracked automatically via the GitHub repository.
