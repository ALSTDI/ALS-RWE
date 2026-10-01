# :material-frequently-asked-questions: FAQ

Answers to the most common questions from past cohorts, organized by topic.

---

## OMOP CDM Fundamentals

??? question "What is the OMOP CDM and what problem does it solve?"
    The **Observational Medical Outcomes Partnership Common Data Model (OMOP CDM)** is a standardized relational database schema for health data, maintained by the OHDSI community. It maps source data (ICD codes, NDC drug codes, lab values) to common standard concepts so that the same analysis can run on data from multiple institutions and produce comparable results.

    Without it, every institution's EHR data are in a different format, and multi-site research needs a separate data transformation for each collaboration.

??? question "What is the difference between a standard and a non-standard concept?"
    A **standard concept** (`standard_concept = 'S'`) is the canonical concept used for analysis in OMOP. Every OMOP analysis tool (Atlas, HADES) operates on standard concepts. Source vocabularies such as ICD-9-CM, ICD-10-CM, and NDC contain **non-standard concepts** that map to standard ones via `Maps to` relationships. A third status, **classification** (`standard_concept = 'C'`), is used for grouping concepts such as ATC drug classes: they are not stored in the clinical tables and reach the data through their standard descendants.

    In practice, a concept set made only of ICD-10-CM codes (non-standard) will not match records in the standard concept fields. Build concept sets on standard concepts, or classification concepts with descendants, and use the **Included Source Codes** tab in ATLAS to check coverage.

??? question "Why does OMOP use SNOMED for conditions but RxNorm for drugs?"
    Standard status is assigned concept by concept, and in each domain a small number of vocabularies supply most of the standard concepts:

    - **Conditions / Diagnoses → SNOMED CT**: a rich, hierarchical ontology with broad international adoption.
    - **Drugs → RxNorm** (ingredients and clinical drug forms) / **ATC** (drug classes): RxNorm is maintained by the NLM and is the standard for US drug data; ATC provides a classification hierarchy for drugs.
    - **Measurements / Labs → LOINC**: the standard for clinical observation codes.
    - **Procedures → SNOMED CT**, **CPT4**, **HCPCS**, and **ICD-10-PCS**.

    The key insight is that OMOP normalizes across all these vocabularies into a single `concept` table, and the `concept_ancestor` table provides cross-vocabulary hierarchy traversal.

??? question "What is the `concept_ancestor` table used for?"
    `concept_ancestor` stores pre-computed transitive ancestor/descendant pairs for all concepts that have hierarchical relationships. It is what makes **"include descendants"** work in a concept set.

    Instead of listing every specific drug product for riluzole, you join `drug_exposure` to `concept_ancestor` on `ancestor_concept_id = [riluzole ingredient concept]` and the join automatically returns all products and formulations below that ingredient in the hierarchy.

??? question "What is an observation period, and why does it matter for cohort logic?"
    The `observation_period` table records the time intervals during which a person has sufficient observable data in the source system. It is the denominator for cohort analysis — a person can only be in a cohort during their observation period.

    "At least 365 days of prior observation" in a cohort inclusion rule means the person must have a continuous observation period starting at least 365 days before their index event. Without this requirement, your new-user design may accidentally include people whose *first observed* prescription is actually a refill.

---

## Atlas & Concept Sets

??? question "Why does my concept set return 0 results when I validate it with SQL?"
    The most common causes:

    1. **Non-standard concepts in the set.** Open the **Included Concepts** tab in Atlas and check the standard concept column. A concept shown as Non-Standard will not match records in the standard concept fields of the CDM.
    2. **Missing "Include Descendants."** You added the parent concept (e.g., Motor neuron disease) but did not toggle "Include Descendants," so the query only looks for that exact concept_id — not the more specific concepts below it.
    3. **Schema or CDM version mismatch.** You are querying a different schema or CDM version than Atlas generated against.
    4. **Concept_id = 0 in CDM records.** Your CDM may have a high proportion of unmapped source codes (concept_id 0), which will not match any standard concept set.

??? question "What do the Included Concepts and Included Source Codes tabs show in Atlas?"
    - **Included Concepts:** every concept the concept set expression resolves to (the concepts you added, plus their descendants where you checked Descendants), with its standard status.
    - **Included Source Codes:** the source codes (ICD-10-CM, NDC, and so on) that map to those concepts. This view lets you check that the codes your site records are covered.

    A concept set that looks complete under Included Concepts may still have gaps if the source codes at your site do not map to it. The Included Source Codes tab is where you find those gaps. The **Mapped** checkbox in the expression is a different thing: it adds mapped source concepts to the set itself. Tab labels differ a little between ATLAS versions.

??? question "What is the 'exit strategy' in a cohort definition?"
    The exit strategy defines when a person *leaves* the cohort. Common options in Atlas:

    - **End of observation period:** person stays in the cohort until their data ends.
    - **End of continuous drug exposure + gap:** useful for drug era cohorts — the person exits when a specified gap in drug supply has elapsed (e.g., 30 days without a fill).
    - **Fixed duration:** the person exits a set number of days after index.

    The choice dramatically affects cohort size and the analytic interpretation.

??? question "Can I export a cohort SQL from Atlas and run it myself?"
    Yes — this is a core skill of the program. In Atlas, open any cohort definition, open the **Export** tab, and choose SQL and your dialect. The exported SQL has parameters (CDM schema, target cohort table, cohort ID) that you fill in before running it, and it writes the cohort into the table you name. A simpler check is to count the rows ATLAS already generated in the results schema cohort table.

---

## Data Quality

??? question "What does the Data Quality Dashboard check?"
    DQD runs a library of checks against the CDM and labels each check type with the terms of the Kahn framework: a category, a subcategory where one applies, and a context.

    - **Conformance:** do values follow the expected format, type, and relational rules? (For example, all `drug_concept_id` values exist in the `concept` table and belong to the Drug domain.)
    - **Completeness:** are values present where expected? (For example, what percent of `condition_occurrence` rows have a concept_id of 0?)
    - **Plausibility:** are values believable? (For example, no birth years in the future and no events dated before birth.)

    Most DQD check types are labeled verification, meaning the data are compared with expectations that come from the system itself. DQD covers part of the framework: no check type is labeled uniqueness plausibility, and DQD does not compare your rates with published benchmarks, which is validation work a study team does separately. See the [Day 2 module](../modules/day-02-vocab-dqd.md) for the table of labels.

    Each check has a **threshold**, the percent of failing rows a site will accept. A failed check means the failure rate exceeds the threshold. A failure is not always fatal to an analysis, and the task is to judge which failures threaten *your specific study question*.

??? question "If my DQD has failures, should I stop my analysis?"
    Not necessarily. The question is whether the specific failures affect the analysis you want to run. A high rate of unmapped conditions (concept_id = 0) may have little effect on a drug utilization study that uses no condition data. The same failure can undermine a cohort whose entry event is built on conditions.

    The process: read the failure → identify what it affects → decide if it threatens your specific question → document your decision in the study protocol.

---

## Environment & Technical Setup

??? question "Why can't I connect DatabaseConnector to my database?"
    The most common causes, in order of frequency:

    1. **Java not installed, or not found by R.** Run `system("java -version")` inside RStudio (not a terminal). If it returns an error, follow the Java step in the [HADES R setup guide](https://ohdsi.github.io/Hades/rSetup.html) and restart RStudio.
    2. **JDBC driver not downloaded.** Run `downloadJdbcDrivers("[your dbms]")` to get the right driver file.
    3. **Wrong `pathToDriver` in `createConnectionDetails`.** The path must point to the folder *containing* the `.jar` file, not the `.jar` file itself.
    4. **Firewall or VPN.** Your institution's network may block the database port from outside the VPN. Connect to VPN first.
    5. **Wrong `dbms` string.** Accepted values: `"postgresql"`, `"sql server"`, `"oracle"`, `"bigquery"`, `"spark"`, `"snowflake"`. Check the DatabaseConnector documentation for the exact string.

??? question "My Atlas cohort count doesn't match my SQL count. Why?"
    Common reconciliation checklist:

    1. **Same CDM and vocabulary version?** Atlas generates against the CDM it is connected to; your SQL client may be pointing to a different schema or snapshot.
    2. **Same results schema?** The cohort table is in a *results* schema, not the CDM schema. Confirm both Atlas and your query target the same results schema and cohort table.
    3. **Different things being counted.** A cohort count is persons (or cohort entries), and a query on a domain table counts records. Compare persons with persons and records with records.
    4. **Date window mismatch.** A cohort inclusion rule with a temporal window (e.g., "365 days prior observation") may apply differently in Atlas-generated SQL vs. a simplified manual query.

??? question "What is the difference between Databricks and DBeaver?"
    - **Databricks** is a cloud data platform / SQL warehouse — it's where your CDM data lives and where SQL queries execute *against the database*. It has a built-in notebook interface.
    - **DBeaver** is a SQL client application you install locally — it connects to any JDBC-compatible database (including Databricks, Postgres, Snowflake, SQL Server) and lets you write and run SQL. DBeaver doesn't store data; it just queries it.

    Many sites use both: Databricks hosts the CDM, and analysts use DBeaver (or Databricks notebooks) to query it.

---

## Program Logistics

??? question "Can I use the materials from this program at my institution?"
    Yes. All website content and materials are licensed for reuse and adaptation. The recommended path:

    1. Fork the [ALSTDI/ALS-RWE repository](https://github.com/ALSTDI/ALS-RWE) on GitHub.
    2. Fill in site-specific details in the Day 4 module and Environment Setup pages.
    3. Replace placeholder ATLAS URLs and connection strings with your institution's values.
    4. Use the plain template from the [Resources page](../resources.md) as the starting point for any new slide decks, and apply your own theme if you want one.

??? question "Are sessions recorded?"
    Yes — each cohort session is recorded and shared in the program's shared drive. Links are distributed through your cohort's communication channel within 24 hours of the session.

??? question "I missed a session. How do I catch up?"
    1. Watch the recording for the session you missed.
    2. Read through the module page and complete the associated exercise.
    3. If you have questions after reviewing the recording and materials, bring them to the next weekly meeting or drop into office hours.

??? question "How do I report a bug or suggest an improvement to the site?"
    Open an issue on the [ALSTDI/ALS-RWE GitHub repository](https://github.com/ALSTDI/ALS-RWE/issues). Include a brief description of what you found or what you'd like to see.

---

> [Weekly Meeting :material-arrow-left:](weekly-meeting.md) · [Office Hours :material-arrow-left:](office-hours.md) · [Resources :material-arrow-right:](../resources.md)
