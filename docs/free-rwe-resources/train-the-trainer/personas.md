# Personas & Learning Paths

Not everyone arrives at this program with the same background or goal. Use this page to find the track that best matches your role, then follow the recommended sequence. The core four days are required for everyone; the persona-based guidance shapes *how* you engage and which extras to prioritize.

---

## At a Glance

| Persona | Start Here | Key Tools | Skip / Skim |
|:--|:--|:--|:--|
| :material-translate: Vocabulary & Terminology Expert | Day 1 → Day 2 → Day 3 | Athena, Atlas Concept Sets | Day 4 SQL depth, Day 6 R |
| :material-chart-line: Statistician / Design Analyst | Day 3 → Day 4 → Day 5 | Atlas Pathways, HADES, SQL review | Environment deep-dives |
| :material-database-cog: Data Analyst / Engineer | Module 0 → Day 2 → Day 4 | Databricks, DBeaver, SEARCH, GitHub | Atlas GUI portions |
| :material-stethoscope: Clinician / Research Analyst | Day 1 → Day 3 | Athena, Atlas Cohort Editor | SQL labs (participate lightly) |

---

## :material-translate: Persona 1 — Vocabulary & Terminology Expert

**Who you are:** Clinical coders, medical informaticists, clinical terminology leads, or anyone whose primary responsibility is understanding and curating medical vocabularies and code sets.

**Your goal:** Build reliable, reproducible concept sets that capture the clinical phenomenon you care about — and understand how vocabulary structure affects every downstream analysis.

### Recommended Path

=== "Core Sequence"

    1. **Module 0 — Environment Setup** · Verify Athena access and Atlas login.
    2. **Day 1 — OMOP CDM** · Focus on vocabulary tables (`concept`, `concept_relationship`, `concept_ancestor`). The table overview matters less than the vocabulary deep-dive.
    3. **Day 2 — Vocabulary & Data Quality** · This is your primary session. Spend extra time on the Standard/Mapped toggle and the DQD concept-set vs. data-quality distinction.
    4. **Day 3 — Cohort Definition** · Understand how concept sets plug into cohort entry events and inclusion rules. You don't need to build pipelines, but you need to validate what analysts build.
    5. **Day 4 — Data Extraction** · Participate lightly; focus on how extraction counts reflect your concept set choices.

=== "Key Tools"

    | Tool | Why it matters for you |
    |:--|:--|
    | [Athena](https://athena.ohdsi.org) | Primary workspace — search, compare, inspect vocabularies |
    | Atlas Concept Sets | Build and validate the reusable concept sets used everywhere |
    | SQL Client (Databricks / DBeaver) | Confirm your sets against the CDM with the [SQL Cheat Sheet](common_artifacts/omop-vocab-sql-cheat-sheet.md) |
    | [EHDEN Academy](https://academy.ehden.eu) | Deep-dives on standardized vocabularies and ETL |

=== "Recommended Extras"

    - **Day 5 (Optional):** See how concept sets directly drive treatment pathway results — a powerful feedback loop for refining your sets.
    - **White Rabbit / Usagi:** Tools for source code mapping; relevant if your institution is doing an ETL.
    - **Oncology-Specific Resources** on the [Resources page](resources.md): key if your work involves cancer registries.

---

## :material-chart-line: Persona 2 — Statistician / Design Analyst

**Who you are:** Epidemiologists, biostatisticians, outcomes researchers, or study designers who understand observational study design and need to operationalize it in OHDSI tools.

**Your goal:** Translate a study protocol into a cohort definition, run the analysis in ATLAS or HADES, and interpret the results with appropriate caution about confounding and data quality.

### Recommended Path

=== "Core Sequence"

    1. **Module 0 — Environment Setup** · Confirm R, RStudio, and HADES install if you plan to do Day 6.
    2. **Day 1 — OMOP CDM** · Focus on how OMOP domains map to study design constructs (exposure, outcome, covariate).
    3. **Day 2 — Vocabulary & Data Quality** · Focus on concept set validity and DQD as a study-fitness check.
    4. **Day 3 — Cohort Definition** · This is your primary session — build the new-user cohort with careful temporal logic.
    5. **Day 4 — Data Extraction** · Understand what the extracted dataset looks like and how to validate counts.
    6. **Day 5 (Optional) — Treatment Pathways** · Directly applicable to treatment utilization and sequencing research questions.
    7. **Day 6 (Optional) — HADES** · Essential if you will run characterization, estimation, or prediction pipelines.

=== "Key Tools"

    | Tool | Why it matters for you |
    |:--|:--|
    | Atlas Cohort Editor | Operationalize inclusion/exclusion criteria with temporal logic |
    | Atlas Pathways | Treatment sequence visualization |
    | HADES (R) | CohortMethod, PatientLevelPrediction, FeatureExtraction |
    | [RWD Guide](https://rwd.guide) | Bias, confounding, and study design for observational data |

=== "Recommended Extras"

    - **Book of OHDSI Ch. 12–14:** Estimation, Prediction, and HADES — your primary reference.
    - **OHDSI Community Calls:** Great for hearing real-world study design trade-offs.
    - **Day 6 HADES kit** from [Resources](resources.md): includes patient-level prediction notebook and interpretation guide.

---

## :material-database-cog: Persona 3 — Data Analyst / Engineer (SQL-First)

**Who you are:** Data engineers, SQL developers, BI analysts, or ETL developers whose primary workflow is the command line, SQL editors, and code repositories — not GUIs.

**Your goal:** Understand the OMOP CDM well enough to build reliable extraction pipelines, validate results programmatically, and maintain reproducible analysis code.

### Recommended Path

=== "Core Sequence"

    1. **Module 0 — Environment Setup** · Set up Git, confirm SQL client connectivity, and confirm GitHub repo access. This is your most important session.
    2. **Day 1 — OMOP CDM** · Focus on schema, table relationships, and SQL queries. Use the [Day 1 Code Snippets](exercises/code_snippets/day-01-snippets.md) throughout.
    3. **Day 2 — Vocabulary & Data Quality** · Focus on the SQL validation steps. The Atlas GUI is secondary; the SQL behind it is what matters.
    4. **Day 3 — Cohort Definition** · Export cohort SQL from Atlas and run it yourself. The [SQL Validation Mini Lab](common_artifacts/sql-validation-mini-lab.md) is key.
    5. **Day 4 — Data Extraction** · Your primary session — work through every step in your actual SQL client.
    6. **Day 6 (Optional) — HADES** · Run HADES R packages via DatabaseConnector; relevant if you support statistical workflows.

=== "Key Tools"

    | Tool | Why it matters for you |
    |:--|:--|
    | Databricks / DBeaver / SQL Client | Primary workspace — run and validate every Atlas export |
    | GitHub | Version-control cohort definitions, SQL scripts, and notebooks |
    | SEARCH Tool | Site-specific extraction pipeline |
    | [OMOP SQL Cheat Sheet](common_artifacts/omop-vocab-sql-cheat-sheet.md) | Quick reference for every CDM query pattern |
    | [SQL Validation Mini Lab](common_artifacts/sql-validation-mini-lab.md) | Step-by-step export → validate → reconcile workflow |

=== "Recommended Extras"

    - **DatabaseConnector (HADES):** Connects R directly to your CDM — highly relevant if you support analysts.
    - **White Rabbit / Rabbit-in-a-Hat:** Profiling and ETL design tools.
    - **[OHDSI on GitHub](https://github.com/OHDSI):** Explore the CDM DDLs, HADES packages, and community pipelines.
    - **Capstone Module (Optional, Module 10 in Syllabus):** End-to-end mini study — build in your SQL client.

---

## :material-stethoscope: Persona 4 — Clinician / Research Analyst

**Who you are:** Physicians, nurses, clinical research coordinators, or patient advocates who need to understand how EHR data is organized and how to interpret OHDSI analyses — without necessarily writing code.

**Your goal:** Develop enough OMOP/OHDSI literacy to collaborate effectively with data teams, review cohort definitions for clinical accuracy, and interpret analytic results.

### Recommended Path

=== "Core Sequence"

    1. **Module 0 — Environment Setup** · Focus on ATLAS login and Athena access. SQL client setup is optional.
    2. **Day 1 — OMOP CDM** · Focus on conceptual understanding: how EHR data maps to OMOP domains. The SQL exercises are optional for you.
    3. **Day 2 — Vocabulary & Data Quality** · Use Athena to explore concepts relevant to your clinical area. Focus on the Standard/Mapped distinction and what bad concept sets look like clinically.
    4. **Day 3 — Cohort Definition** · Your most important session. Review cohort logic for clinical accuracy — are the criteria capturing the right patients? Review characterization outputs.
    5. **Day 4 — Data Extraction** · Attend for context; extraction validation is primarily for the data team.

=== "Key Tools"

    | Tool | Why it matters for you |
    |:--|:--|
    | [Athena](https://athena.ohdsi.org) | Explore concepts and hierarchies in your clinical domain |
    | Atlas Cohort Editor | Review cohort definitions for clinical face validity |
    | Atlas Characterization | Interpret who is in a cohort — demographics, prior conditions, medications |
    | [EHDEN Academy](https://academy.ehden.eu) | Self-paced intro modules for non-technical learners |

=== "Recommended Extras"

    - **"Introduction to OMOP" course** (Tufts CTSI iLEARN) — accessible overview, no coding required. See [Resources](resources.md).
    - **[RWD Guide](https://rwd.guide)** — written for clinicians and researchers new to real-world data.
    - **Characterization outputs from Day 3:** Bring a real clinical question and review the output with the data team.

---

## Not Sure Which Persona Fits?

Start with **Day 1** regardless of background — the OMOP CDM is the foundation everything else depends on. After Day 1, reassess: if you found yourself most interested in the vocabulary tables, you're probably Persona 1; if you were most engaged by the study design implications, you're Persona 2; if you immediately wanted to write the SQL yourself, you're Persona 3; if the clinical accuracy of concept sets was your primary concern, you're Persona 4.

Most participants end up combining elements of multiple personas. The paths above are starting points, not rigid rules.
