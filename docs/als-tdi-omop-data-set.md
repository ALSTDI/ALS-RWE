---
title: ALS TDI OMOP Data Set
---

# ALS TDI OMOP Data Set

**Release notes: version 0.2.0, 2026 refresh**

The ALS TDI ARC Study mapped to the Observational Medical Outcomes Partnership Common Data Model (OMOP CDM). This release restructures the ARC Natural History Study into OMOP CDM v5.4 and maps it to standardized vocabularies.

Version 0.2.0 is the first release to include linked electronic health record laboratory data alongside the self-reported registry surveys and central-laboratory results that made up version 0.1.0.

This is part of a larger harmonization effort with Answer ALS and the Critical Path Institute.

!!! note "EHR data is produced by Registry Forge ALS"
    The EHR component of this release is built with Registry Forge ALS, ALS TDI's open-source pipeline for turning raw C-CDA and FHIR exports into research-ready, OMOP-mapped data.

    Project site and documentation: [alstdi.github.io/RegistryForgeALS](https://alstdi.github.io/RegistryForgeALS/)

    Preprint: Boyce D, et al. *Registry Forge: an open-source pipeline for transforming patient-mediated electronic health record exports into research-ready OMOP data.* medRxiv 2026.06.02.26354637. <https://doi.org/10.1101/2026.06.02.26354637>

## At a glance

| | |
|---|---|
| Release | 0.2.0, 2026 refresh |
| CDM version | OMOP CDM v5.4, full column set on every table ([reference](https://ohdsi.github.io/CommonDataModel/cdm54.html)) |
| Vocabulary | Athena OMOP Standardized Vocabularies v5.0, release 27-FEB-2026 |
| Participants | 708 — the ARC participants with linked biological samples, drawn from a registry of 2,014 |
| Data types | Self-reported surveys, ALSFRS-R, central-laboratory blood chemistry and haematology, self-reported ALS gene results, linked EHR laboratory results, mortality |
| Access | ARC Data Commons, at no cost to academic and nonprofit researchers under a Data Use Agreement |
| Portal | Neuromine Data Portal |

**Citation:** ALS Therapy Development Institute (ALS TDI). (2023). ALS Research Collaborative (ARC) [Data set]. ALS Therapy Development Institute. <https://doi.org/10.71944/C3NA-9124>

For background on the ARC resource itself, see the preprint *Boyce et al., The ALS Research Collaborative: A Long Running Multimodal ALS Natural History Resource.*

## What changed since version 0.1.0

| | Version 0.1.0 | Version 0.2.0 |
|---|---|---|
| Vocabulary edition | Athena v5.0, 30-AUG-2024 | Athena v5.0, 27-FEB-2026 |
| EHR data | Not included | EHR laboratory results for 47 participants, on the registry analyte concepts |
| ALS diagnosis and El Escorial certainty | One row per surveyed instance | One row per participant, resolved to the current recorded status |
| Anatomical site of symptom onset | Repeated across follow-up rounds | One row per site per participant |
| Personal medical history (conditions) | Round 1 only | Affirmatives from all four survey rounds, dated to first report |
| Self-reported medications | Full list repeated at every submission | Deduplicated, one row per distinct medication record |
| Visit linkage | Partial | Every measurement and observation row resolves to a visit |
| Units | Source labels carried verbatim, unit concepts unmapped | Corrected unit labels and mapped unit concepts |
| ALS gene concepts | Not resolvable against the bundled vocabulary | Resolvable — the 2026 edition adds OMOP Genomic |

No new survey instruments or measurement analytes were added; see the [2026 Data Refresh](omop-2026-refresh.md) page for details and known limitations.

!!! warning "Replace any earlier extract with this release"
    Diagnosis, El Escorial certainty and onset site now resolve to a single current value per participant, and measurements, medications and visit structure all differ. Version 0.1.0 reports different values. Replace it rather than pooling the two.

## Participant summary

Participants fall into three groups, identified by the prefix on `person.person_source_value`:

| Prefix | Group | Participants |
|---|---|---:|
| `CASE_` | People with ALS | 604 |
| `ASYMP_` | Asymptomatic carriers of an ALS-linked variant | 48 |
| `CONTROL_` | Healthy controls | 56 |

The trailing integer of `person_source_value` is the ARC subject identifier — the supported route from a CDM row back to a participant. It is deliberately not carried as a column inside the CDM tables. Not all participants answered all surveys; controls and asymptomatic carriers generally have fewer records than people with ALS.

## Table counts

| Table | Rows |
|---|---:|
| person | 708 |
| observation | 230,364 |
| measurement | 73,459 |
| visit_occurrence | 22,969 |
| condition_occurrence | 606 |
| drug_exposure | 3,142 |
| observation_period | 698 |
| death | 268 |
| care_site | 2 |

Other OMOP domains, including `procedure_occurrence`, are not populated.

## Telling EHR rows from registry rows

Use the standard type concepts:

| `*_type_concept_id` | Meaning |
|---|---|
| `32817` | EHR |
| `32856` | Central-laboratory blood draw |
| `32862` | Participant self-report, including ALSFRS-R and gene results |
| `32879` | Registry-derived observation period |

EHR-derived visits additionally carry `care_site_id` 21; all registry-side visits carry 20.

## Domain mappings

### person

`year_of_birth`, sex, race and ethnicity, with sequential `person_id` and the group prefix retained on `person_source_value`. Unknown, multiple or unselected race, ethnicity or sex maps to `concept_id = 0`.

!!! warning "Reading ethnicity_concept_id in this data set"
    A participant who selects Hispanic or Latino receives `38003563`. Everyone else receives `0`. The concept for "Not Hispanic or Latino" is deliberately not used, because the instrument asks a single combined race question — a participant who did not select Hispanic or Latino has not asserted that they are not Hispanic. **Treat `0` as unknown, not as non-Hispanic**, in any network study that expects standard ethnicity coding.

### observation

`observation_type_concept_id = 32862` on all rows. Every row links to a visit.

| Content | Concept | Notes |
|---|---|---|
| ALSFRS-R, 12 items plus total score | `42529071`–`42529084` | `value_as_number` carries the score; one row per item per assessment |
| ALS diagnosis and El Escorial certainty | `2000000061` | Custom concept, one row per participant |
| Anatomical site of symptom onset | `2000000396` | Custom concept, one row per site |
| Family medical history | `4167217` plus per-condition standard concepts | One row per reported condition, per relative |
| Personal medical history | Per-condition standard concepts | One row per participant per condition, from all survey rounds |
| History of head or neck injury | `1340204` | Screening question only |
| Lifestyle, tobacco use | `3012697` | Lifetime-history flag only |
| Military service | `37162399` | Flag |
| Occupational industry | `36204389` | One row per reported industry |

`observation_date` is the survey or assessment date (conditions: the date of the round that first reported the condition). `value_source_value` preserves the raw response verbatim.

**El Escorial criteria** — harmonized with Answer ALS and the Critical Path Institute; self-reported, then validated by ALS TDI staff. Custom concepts: Definite `2000000057`, Possible `2000000058`, Probable `2000000059`, Probable laboratory-supported `2000000060` (defined but unpopulated), Suspected `2000000062`.

**Anatomical site of symptom onset** — fine anatomy rolls up (hand becomes arm, foot becomes leg); the verbatim site is always in `value_source_value`. Left arm `4215746`, right arm `4286959`, left leg `4136825`, right leg `4268743`; bulbar and other sites map to `0` because no suitable standard concept was identified — read `value_source_value` to recover the site.

### measurement

Three sources, partitioned by `measurement_type_concept_id`:

**Central-laboratory blood draws** (`32856`) — 35 analytes covering a comprehensive metabolic panel and complete blood count with differential: A/G Ratio, Albumin, Alkaline Phosphatase, Basophils and Basophils Abs, Bilirubin Total, BUN, BUN/Creatinine Ratio, Calcium, Chloride, CO2, Creatinine, EGFR, Eosinophils and Eosinophils Abs, Globulin, Glucose, Hematocrit, Hemoglobin, Lymphocytes and Lymphocytes Abs, MCH, Monocytes and Monocytes Abs, Neutrophils and Neutrophils Abs, Platelet Count, Potassium, RDW, Red Blood Cell Count, SGOT (AST), SGPT (ALT), Sodium, Total Protein, White Blood Cell Count. Seven further analytes are present in the source but not mapped, matching version 0.1.0: MCV, MCHC, Mean Platelet Volume, IMM Grans and IMM Grans Abs, Nucleated RBC and Nucleated RBC Abs.

**EHR laboratory results** (`32817`) — restricted to the same 35 analytes and mapped onto the same registry concepts, with the original LOINC code preserved in `measurement_source_value`. Deduplicated; the only rows with `measurement_datetime` populated. Join registry and EHR laboratory data directly on `measurement_concept_id`.

**Self-reported ALS-linked gene results** (`32862`) — C9orf72, SOD1, TARDBP, FUS, NEK1, PFN1, SPG11 and VCP, one row per participant per gene, on OMOP Genomic concepts (2026 vocabulary edition or later required).

### drug_exposure

Self-reported medications; supplements are not included. `drug_concept_id` comes from an ingredient-level lookup, and every released row is mapped to a standard concept. Dosage is not calculated; source values are retained. Missing start dates use the placeholder 1900-01-01; a missing end date reuses the start date. The source re-exports each participant's full list at every survey submission, so this release deduplicates on participant, ingredient, drug name, reference drug, dates, form, dosage and frequency — **medication counts are not comparable with version 0.1.0.**

### condition_occurrence

The participant's ALS diagnosis only, `condition_concept_id = 373182`, one row per participant. `condition_source_value` records the self-reported diagnosis status.

### visit_occurrence

Five visit classes: survey submissions, ALSFRS-R self-assessments, participant-data submissions, central-laboratory blood draws, and EHR laboratory extract dates. Registry survey-derived visits carry `visit_concept_id = 38004259` ("Research Clinic/Center"); laboratory visits carry `32036`. EHR-derived visits are date-based extract visits (one per participant per date), not reconstructions of source encounters, and carry `care_site_id` 21.

### death

One row per deceased participant. `death_date` is set to 31 December of the year of death, so that no day or month of death is disclosed, and is capped at the extraction date. Nine rows carry the placeholder **1900-01-01** — a death with an unknown date, not an event in 1900.

## Dates and timing

- Dates may be shifted for de-identification, following Hripcsak et al., JAMIA 2016.
- Where a date is missing, the survey date is used if available, otherwise an approximate date, otherwise the placeholder 1900-01-01.
- `observation_period` spans each participant's earliest to latest recorded event date, deliberately including retrospective self-reported dates such as symptom onset; see the [2026 Data Refresh](omop-2026-refresh.md) page before using it for person-time.
- Registry dates are written in US format; EHR dates are ISO 8601. Parse the two explicitly if you combine them.

## Custom concepts

ALS-specific variables with no standardized OMOP vocabulary use local concepts above 2,000,000,000: `2000000061` (El Escorial question), `2000000057`–`2000000060` and `2000000062` (El Escorial statuses), `2000000396` (onset-site question).

!!! warning "Custom concepts do not exist in Athena"
    These are local by design and appear in no Athena release. Load the supplied local concept definitions alongside your Athena tables, or handle the range above 2,000,000,000 explicitly.

## Guidance for data use

- Read `*_source_value` and `*_source_concept_id` to trace any row back to the original survey response or EHR code.
- Explore concept definitions with [OHDSI Athena](https://athena.ohdsi.org/); use the 27-FEB-2026 release or later.
- Recover the ARC subject identifier from the trailing integer of `person.person_source_value`.
- Distinguish EHR from registry rows using `*_type_concept_id`.
- Join registry and EHR laboratory data on `measurement_concept_id`; the EHR rows' LOINC detail is in `measurement_source_value`.
- Treat `ethnicity_concept_id = 0` as unknown, not as non-Hispanic.
- Do not compare medication row counts against version 0.1.0, and replace any pre-2026 extract with this release rather than pooling.

Detailed ETL documentation, the person-level accounting of which participants are included, and the data quality results are available to data recipients on request.

## Surveys mapped in this release

The ARC study fields far more instruments than this release maps; the OMOP release deliberately keeps the version 0.1.0 content footprint so the two remain comparable.

**Mapped:** enrollment and general information, Your ALS Experience, New Enrollee Survey, Family History, Medical History Conditions rounds 1–4, Medical History Injuries round 1, Lifestyle round 1 tobacco flag, Occupation round 1 (military service and occupational industry), ALSFRS-R, medications, blood draw results, gene results, mortality.

**Collected by ARC but not mapped in this release:** education, marital status, employment status, smoking sub-detail, current smoking status from follow-up rounds, physical activity, hospitalization and emergency visits, clinical trial participation, geography and residential history, diet, supplements, anthropometrics, handedness and footedness, military deployment arenas, age at diagnosis, ALS complications, free-text "other" write-in fields, the swallowing, speech, bladder and bowel symptom items, and follow-up rounds 2–4 of the lifestyle and occupation modules. These are available through ARC Data Commons outside the OMOP release; see the ARC preprint and the data dictionary for the complete picture.

## Caution

- These data are participant self-report plus central-laboratory results plus patient-mediated EHR laboratory extracts. They are not a clinician-adjudicated chart review, and `condition_occurrence` carries the participant's own account of their ALS diagnosis status.
- Treat `ethnicity_concept_id = 0` as unknown, not as non-Hispanic.
- Diagnosis, El Escorial certainty and onset site resolve differently than in version 0.1.0. Replace earlier extracts rather than pooling.

Problems with the data, or questions about a specific row: [dboyce@als.net](mailto:dboyce@als.net).

For full OMOP domain details, see the [OMOP CDM v5.4 Reference Guide](https://ohdsi.github.io/CommonDataModel/cdm54.html).
