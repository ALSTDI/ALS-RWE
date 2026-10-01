# Syllabus: OHDSI Train-the-Trainer (Core Sessions and Optional Modules)

This master syllabus outlines the **required readings, tools, and assignments** for the OHDSI Train-the-Trainer program: a required core (environment setup, then Days 1 to 4), optional sessions on treatment pathways (Day 5) and HADES (Day 6, taught as Part 1 and Part 2), with every session a half day, and **optional advanced modules** for continued professional development.  
The program bridges Epic Clarity experience with OMOP/OHDSI skills through both GUI-based (Atlas, Athena) and SQL-based (Databricks, DBeaver) learning.

---

## A) Session Syllabus (Days 1 to 4 required; Days 5 and 6 optional)

> Tip: Chapters refer to the [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/).  
> For broader context on data sources and study design, see the [RWD Guide](https://rwd.guide/).

| **Week / Day** | **Focus** | **Primary Readings / Viewings** | **Tools & Docs** | **Homework / Follow-up** |
|-----------------|------------|---------------------------------|------------------|---------------------------|
| **Day 0 – Environment Setup** | Verify access and installations | OHDSI.org – [Who We Are](https://www.ohdsi.org/who-we-are/) · OHDSI Forum “Introduce Yourself” | [Environment Checklist Template](common_artifacts/environment-checklist-template.md) · ATLAS login · SQL client setup (Databricks / DBeaver) | Complete environment checklist · Test CDM connection and ATLAS login |
| **Day 1 – OMOP CDM & Athena Vocabulary Exploration** | Understand CDM structure and vocabularies | *Book of OHDSI* Ch. 4 **The Common Data Model** (§ 4.1 Design Principles · 4.2 Data Model Conventions · 4.3 CDM Standardized Tables); Ch. 5 **Standardized Vocabularies** (§ 5.1 Why Vocabularies, and Why Standardizing · 5.2 Concepts · 5.3 Relationships · 5.4 Hierarchy) | [Athena Browser](https://athena.ohdsi.org/) · Example CDM entity–relationship diagram (ERD) | Identify standard and non-standard concepts in Athena · Document mappings (`Maps to`, `Is a`) and the hierarchy shown in `concept_ancestor` |
| **Day 2 – Concept Sets in Atlas & Introduction to Data Quality Concepts (with SQL Validation)** | Build concept sets in Atlas and validate them using SQL tools | *Book of OHDSI* Ch. 15 **Data Quality**; Ch. 10 § 10.3 Concept Sets; Ch. 5 § 5.2.8 Classification Concepts | Atlas Concept Sets · SQL Clients (Databricks / DBeaver) · [OMOP SQL Examples](common_artifacts/omop-vocab-sql-cheat-sheet.md) | Export Atlas SQL for concept sets · Run and validate logic in Databricks/DBeaver · Reflect on vocabulary mapping and data quality concepts |
| **Day 3 – Cohort Definition & Characterization with ATLAS (SQL Exploration)** | Design and characterize cohorts; explore cohort SQL | *Book of OHDSI* Ch. 10 **Defining Cohorts**; Ch. 11 **Characterization** (§ 11.2 and § 11.7) | ATLAS Cohort Editor · Characterization Module · SQL Clients | Export cohort SQL from Atlas · Annotate key joins and logic in SQL client · Compare table usage across OMOP domains |
| **Day 4 – Data Extraction & SQL Validation (site specific)** | Retrieve OMOP data for analysis and cross-check results | *Book of OHDSI* Ch. 9 **SQL and R** | ATLAS SQL export · Databricks / DBeaver · [OMOP SQL Examples](common_artifacts/omop-vocab-sql-cheat-sheet.md) | Re-run the extraction SQL manually in your SQL client · Validate counts and compare results |
| **Day 5 – Treatment Pathway Analysis (Optional)** | Sequence treatments and visualize pathways | *Book of OHDSI* Ch. 11 **Characterization** (§ 11.3 Treatment Pathways and § 11.9 Cohort Pathways in ATLAS) | ATLAS Cohort Pathways | Generate and interpret pathway plots · Summarize one analytical insight |
| **Day 6, Part 1 – HADES: Cohort Diagnostics and Feature Extraction (Optional)** | Set up the R environment, run diagnostics on a cohort, build baseline covariates | *Book of OHDSI* Ch. 8 **OHDSI Analytics Tools**; Ch. 11 § 11.8 Cohort Characterization in R | [HADES R Packages](https://ohdsi.github.io/Hades/) · CohortGenerator · CohortDiagnostics · FeatureExtraction | Run diagnostics on your Day 3 cohort and note what each output shows |
| **Day 6, Part 2 – HADES: Patient-Level Prediction (Optional)** | State a prediction problem, train a model, read discrimination and calibration | *Book of OHDSI* Ch. 13 **Patient-Level Prediction** | PatientLevelPrediction · Colab notebook (synthetic data) | Run the prediction workflow or the notebook and report the AUC and calibration |

---

## B) Optional / Advanced Modules (After the Sessions)

These modules are not part of the session sequence and can be assigned for continued self-study.

| **Module #** | **Topic** | **Primary Readings** | **Key Tools / Docs** | **Optional Context / Use Case** |
|---------------|-----------|----------------------|----------------------|----------------------------------|
| **7. Team Building & Project Management** | Cross-functional teamwork in OHDSI | *Book of OHDSI* Ch. 1 (The OHDSI Community) & Ch. 20 (OHDSI Network Research) | GitHub best practices · Agile boards | Managing multi-site collaborations |
| **8. Advanced Topics** | ML, NLP, FHIR, unstructured data | *Book of OHDSI* Ch. 8 (OHDSI Analytics Tools) | NOTE_NLP · FHIR mapping guides | Extending OMOP to AI and interoperability |
| **9. Train-the-Trainer Skills** | Adult learning and facilitation | Adult learning primers · Presentation skills | EXCELERATE TtT materials | Designing your own institutional training program |
| **10. Capstone Project** | End-to-end practice study | Revisit Ch. 12, 13, 19 | ATLAS export → SQL / R | Present a mini reproducible study |
| **11. Wrap-Up & Next Steps** | Sustaining engagement | *Book of OHDSI* Ch. 1 (The OHDSI Community) & Ch. 2 (Where to Begin) | OHDSI Workgroups Directory | Join or lead community workgroups |
| **12. Refresher (3-Month Post-Course)** | Review and updates | *Book of OHDSI* Ch. 19 (Study Steps) | Latest OHDSI release notes | Continuing learning & updates |

---

## C) Persona-Based Study Paths (Quick Reference)

| **Persona** | **Core Modules** | **Key Tools** | **Suggested Extras** |
|--------------|------------------|---------------|----------------------|
| **Vocabulary / Terminology Experts** | Days 1–3 | Athena · Atlas Concept Sets · SQL Clients (Databricks/DBeaver) | White Rabbit / Rabbit-in-a-Hat |
| **Statisticians / Data Analysts** | Days 3–6 (Days 5 and 6 optional) | ATLAS Cohort Pathways · HADES · SQL review of outputs | RWD Guide (bias/confounding) |
| **Data Engineers (SQL-first)** | Days 2–4 | Databricks · DBeaver · DatabaseConnector | Build reproducible pipelines in GitHub |
| **Clinicians / Analysts** | Days 1–3 | Athena · Atlas Cohort Editor | Explore cohort outputs and characterization summaries |

---

## D) Key Supplemental Resources

| **Resource** | **Purpose / Description** |
|---------------|---------------------------|
| [The ALS Use Case](als-use-case.md) | The running example for every session: motor neuron disease, ALS medications, and the ALSFRS-R, with the concepts and lookup queries. |
| [Environment Checklist Template](common_artifacts/environment-checklist-template.md) | Validate all required system access before Day 1. |
| [OMOP SQL Examples](common_artifacts/omop-vocab-sql-cheat-sheet.md) | Common SQL patterns for exploring concepts, ancestors, and cohort logic in Databricks or DBeaver. |
| [SQL Validation Mini Lab](common_artifacts/sql-validation-mini-lab.md) | Step-by-step guide to export Atlas SQL, run validation queries, and compare outputs. |
| [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/) | Core text for OMOP CDM and OHDSI methods. |
| [RWD Guide](https://rwd.guide/) | Companion text for understanding bias, confounding, and data quality. |

---

## E) How to Use

- **Before class:** Read the assigned *Book of OHDSI* chapters and open the listed tools.  
- **During class:** Use both **Atlas/Athena** and your **SQL client** for guided exercises.  
- **After class:** Complete the homework for the session and the optional SQL validation tasks.  
- **As a trainer:** Bookmark these core references and update your repo with local connection instructions.

---

*This syllabus supports the OHDSI Train-the-Trainer program and connects the graphical and SQL-based workflows. Chapter and section numbers were checked against the online Book of OHDSI on 1 October 2026.*
