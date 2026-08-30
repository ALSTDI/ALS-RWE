---
title: ALS TDI OMOP Data Set
hide:
  - title
---

# ALS TDI OMOP Data Set

## Release notes: version 0.2.0, 2026 refresh

The [ALS TDI ARC Study](https://www.als.net/arc/) mapped to the [Observational Medical Outcomes Partnership Common Data Model (OMOP CDM)](https://ohdsi.github.io/CommonDataModel/). This release restructures the ARC Natural History Study into OMOP CDM v5.4 and maps it to standardized vocabularies.

Version 0.2.0 is the first release to include **linked electronic health record data** alongside the self-reported registry surveys and central-laboratory results that made up version 0.1.0.

This is part of a larger harmonization effort with [Answer ALS](https://www.answerals.org/) and the [Critical Path Institute](https://c-path.org/program/critical-path-for-rare-neurodegenerative-diseases/).

!!! info "EHR data is produced by Registry Forge ALS"
    The EHR component of this release is built with [**Registry Forge ALS**](https://alstdi.github.io/RegistryForgeALS/), ALS TDI's open-source pipeline for turning raw C-CDA and FHIR exports into research-ready, OMOP-mapped data. Registry Forge reads C-CDA XML, FHIR R4 bundles, clinical notes and chunked CSV exports, maps source codes to standard concepts through Athena, and routes them into the CDM.

    Project site and documentation: [alstdi.github.io/RegistryForgeALS](https://alstdi.github.io/RegistryForgeALS/)

    Preprint: Boyce D, et al. *Registry Forge: an open-source pipeline for transforming patient-mediated electronic health record exports into research-ready OMOP data.* medRxiv 2026.06.02.26354637. <https://doi.org/10.1101/2026.06.02.26354637>

---

## At a glance

| | |
|---|---|
| **Release** | 0.2.0, 2026 refresh |
| **CDM version** | OMOP CDM v5.4, full column set on every table ([reference](https://ohdsi.github.io/CommonDataModel/cdm54.html)) |
| **Vocabulary** | Athena OMOP Standardized Vocabularies **v5.0, release 27-FEB-2026** |
| **Participants released** | 708, the ARC participants with linked biological samples |
| **Parent extract** | 2,014 participants in the full registry extract, of whom 80 have linked EHR data |
| **Data types** | Self-reported surveys, ALSFRS-R, central-laboratory blood chemistry and haematology, self-reported ALS gene results, linked EHR diagnoses, medications, laboratory results, vital signs and encounters, mortality |
| **Access** | ARC Data Commons, at no cost to academic and nonprofit researchers under a Data Use Agreement. [Request access](https://www.als.net/arc/data-commons/) |
| **Portal** | [Neuromine Data Portal](https://data.answerals.org/home) |

**Citation**

> ALS Therapy Development Institute (ALS TDI). (2023). *ALS Research Collaborative (ARC) [Data set].* ALS Therapy Development Institute. <https://doi.org/10.71944/C3NA-9124>

For background on the ARC resource itself, see the preprint [Boyce et al., *The ALS Research Collaborative: A Long Running Multimodal ALS Natural History Resource*](https://www.researchsquare.com/article/rs-8272744/v1).

---

## What changed since version 0.1.0

| | Version 0.1.0 | Version 0.2.0 |
|---|---|---|
| Vocabulary edition | Athena v5.0, 30-AUG-2024 | Athena v5.0, **27-FEB-2026** |
| EHR data | Not included | **Included**, 80 participants in the parent extract |
| ALS diagnosis and El Escorial certainty | One row per surveyed instance | **One row per participant**, resolved to the participant's current recorded status |
| Anatomical site of symptom onset | Repeated across follow-up survey rounds | **One row per site per participant** |
| Self-reported medications | Each participant's full medication list repeated at every survey submission | **Deduplicated**, one row per distinct medication record |
| `year_of_birth` completeness | 83.2% | **98.6%** |
| `death_date` completeness | 79.7% | **92.6%** |
| Column conformance | Populated columns only | **Full CDM v5.4 column set** in canonical order on every table |
| ALS gene concepts | Not resolvable against the bundled vocabulary | **Resolvable**, the 2026 edition adds OMOP Genomic |

The mapped field and form footprint is unchanged from version 0.1.0. No new survey instruments or question sets were added. See [scope](#surveys-mapped-in-this-release).

Detailed change documentation, including row-level deltas, is available to data recipients on request.

!!! warning "Replace any earlier extract with this release"
    Participants' recorded answers change over time as they complete follow-up surveys, and this release resolves several items to a single current value per participant rather than carrying every historical response. Diagnosis, El Escorial certainty and anatomical site of symptom onset are affected.

    An extract issued before August 2026 therefore reports different values for those items. **Replace it with this release rather than pooling the two.**

---

## Participant summary

Participants fall into three groups, identified by the prefix on `person.person_source_value`:

| Prefix | Group |
|---|---|
| `CASE_` | People with ALS |
| `ASYMP_` | Asymptomatic carriers of an ALS-linked variant |
| `CONTROL_` | Healthy controls |

The trailing integer of `person_source_value` is the ARC subject identifier. This is the supported route from a CDM row back to a participant. The subject identifier is deliberately not carried as a column inside the CDM tables, so that the tables stay strictly CDM-conformant.

Not all participants answered all surveys, and coverage varies sharply by group. Controls and asymptomatic carriers generally have fewer records than people with ALS.

---

## CDM summary counts

Counts below are for the **full registry extract**. The released subset is a filtered copy of it, so concept identifiers, primary keys and `person_id` values are identical in both.

The extract is assembled in three layers. `person_id` is consistent across all three, and EHR primary keys are offset above the registry maxima, so the merged layer is a clean union with no key collisions and no renumbering.

| Table | Survey and central lab | EHR | Merged |
|---|---:|---:|---:|
| `person` | 2,001 | 80 | 2,014 |
| `observation` | 410,550 | 7,794 | 418,344 |
| `measurement` | 54,951 | 81,353 | 136,304 |
| `visit_occurrence` | 4,552 | 9,797 | 14,349 |
| `condition_occurrence` | 1,702 | 1,545 | 3,247 |
| `drug_exposure` | 9,049 | 3,082 | 12,131 |
| `observation_period` | 1,903 | 81 | 1,984 |
| `death` | 734 | 0 | 734 |
| `care_site` | 1 | 0 | 1 |

The merged layer equals the sum of the other two in every table.

**Other OMOP domains, including `procedure_occurrence`, are not populated in this release.**

The EHR person count of 80 comes from 107 EHR records. 94 records carry a link to a registry participant and collapse onto 67 distinct participants, because 27 records are duplicate enrolments of someone already enrolled. The remaining 13 records have no link and appear in the merged layer as EHR-only persons. Those 13 are a crosswalk gap rather than a genuine EHR-only cohort: every EHR patient is by construction a registry participant.

### Telling EHR rows from registry rows

The merged tables do not carry a source flag column, because CDM v5.4 has no such field and adding one would break tooling that expects a conformant schema. Use the standard type concept instead:

| `*_type_concept_id` | Meaning |
|---|---|
| `32817` | EHR |
| `32856` | Central-laboratory blood draw |
| `32862` | Participant self-report, including ALSFRS-R and gene results |
| `32879` | Registry-derived observation period |

Alternatively, EHR rows in the merged tables are exactly those whose primary key exceeds the registry maximum for that table.

---

## Domain mappings

### person

- `year_of_birth`, sex, race and ethnicity.
- Sequential `person_id`. The `CASE_`, `CONTROL_` and `ASYMP_` prefixes are retained on `person_source_value`.
- Unknown, multiple or unselected race, ethnicity or sex maps to `concept_id = 0`.

!!! note "Reading `ethnicity_concept_id` in this data set"
    A participant who selects Hispanic or Latino in the race question receives `38003563`. Everyone else receives `0`.

    The OMOP concept for "Not Hispanic or Latino", `38003564`, is deliberately not used, because this instrument asks a single combined race question. A participant who did not select Hispanic or Latino has not asserted that they are not Hispanic, so coding them as `38003564` would record a negative answer they did not give.

    Treat `0` here as unknown, not as non-Hispanic, in any network study that expects standard ethnicity coding.

### observation

`observation_type_concept_id = 32862` for all registry-sourced observations.

| Content | Concept | Notes |
|---|---|---|
| ALSFRS-R, 12 items plus total score | `42529071` through `42529084` | `value_as_number` carries the score |
| Self-reported ALS diagnosis and El Escorial certainty | `2000000061` | Custom concept. One row per participant |
| Anatomical site of symptom onset | `2000000396` | Custom concept. One row per site |
| Family medical history | `4167217` plus per-condition standard concepts | One row per reported condition, per relative |
| Personal medical history | Per-condition standard concepts | One row per reported condition |
| History of head or neck injury | `1340204` | Screening question only |
| Lifestyle, tobacco use | `3012697` | Flag only |
| Military service | `37162399` | Flag |

`observation_date` is the survey or assessment date. `value_source_value` preserves the raw response verbatim.

!!! warning "ALSFRS-R observations carry a blank `visit_occurrence_id` by design"
    This matches version 0.1.0. An inner join from `observation` to `visit_occurrence` silently drops every ALSFRS-R row, which is the large majority of the observation table. Use a left join, or filter on the concept range before joining.

#### El Escorial criteria

Harmonized with Answer ALS and the Critical Path Institute. Self-reported, then validated by ALS TDI staff.

| El Escorial status | Custom concept |
|---|---:|
| Definite | `2000000057` |
| Possible | `2000000058` |
| Probable | `2000000059` |
| Probable, laboratory supported | `2000000060` |
| Suspected | `2000000062` |

Distribution in this release: Definitive 1,369, Probable 207, Possible 85, Suspected 41.

`2000000060`, laboratory-supported probable, is defined in the vocabulary and has no rows in this release.

#### Anatomical site of symptom onset

Fine anatomy rolls up for concept assignment, so a hand becomes an arm and a foot becomes a leg. The verbatim site is always retained in `value_source_value`.

| Site | `value_as_concept_id` |
|---|---:|
| Left arm | `4215746` |
| Right arm | `4286959` |
| Left leg | `4136825` |
| Right leg | `4268743` |
| Bulbar and other sites, including tongue, swallowing, breathing, head or neck, trunk | `0` |

Bulbar and other sites map to `0` because no suitable standard concept was identified for them. Read `value_source_value` to recover the site. Participants reporting more than one site have one row per site.

### measurement

Two sources of registry measurement data, plus EHR.

**Central-laboratory blood draws**, `measurement_type_concept_id = 32856`. 35 analytes covering a comprehensive metabolic panel and complete blood count with differential:

A/G Ratio, Albumin, Alkaline Phosphatase, Basophils and Basophils Abs, Bilirubin Total, BUN, BUN/Creatinine Ratio, Calcium, Chloride, CO2, Creatinine, EGFR, Eosinophils and Eosinophils Abs, Globulin, Glucose, Hematocrit, Hemoglobin, Lymphocytes and Lymphocytes Abs, MCH, Monocytes and Monocytes Abs, Neutrophils and Neutrophils Abs, Platelet Count, Potassium, RDW, Red Blood Cell Count, SGOT (AST), SGPT (ALT), Sodium, Total Protein, White Blood Cell Count.

Seven further analytes are present in the source but are not mapped, matching version 0.1.0: MCV, MCHC, Mean Platelet Volume, IMM Grans and IMM Grans Abs, Nucleated RBC and Nucleated RBC Abs.

**Self-reported ALS-linked gene results**, `measurement_type_concept_id = 32862`, covering `C9orf72`, `SOD1`, `TARDBP`, `FUS`, `NEK1`, `PFN1`, `SPG11` and `VCP`. These use OMOP Genomic concepts, which require the 2026 vocabulary edition or later. Against a 2024 vocabulary they resolve to nothing.

**EHR laboratory results and vital signs**, `measurement_type_concept_id = 32817`.

The registry measurement concept set is identical to version 0.1.0: 43 concepts, none added and none removed.

!!! note "Join registry blood draws and EHR labs on analyte name"
    Registry blood-draw concepts are SNOMED-lineage and EHR lab concepts are LOINC, so a `concept_id` join between the two matches only 7 of 40 concepts. **Join on analyte name instead.** Analyte-level name matching recovers all 35 panel analytes.

!!! note "Harmonize registry unit labels before pooling"
    Registry unit labels are carried verbatim from the source instrument. Convert them to standard units before pooling values with any other source.

    | Source label | Standard interpretation |
    |---|---|
    | `10^3/mm3` on absolute differential counts | Values are cells/uL, so divide by 1,000 to compare against K/uL |
    | `%` on Hemoglobin | Unit is g/dL |
    | `MM01/L` | Denotes mmol/L. Affects Chloride, CO2, Potassium and Sodium |
    | `SGPT (AST)` | The analyte is ALT |

`unit_concept_id` is `0` throughout, including on rows that carry a clean unit string in `unit_source_value`. Unit mapping is out of scope for this release. Harmonize units yourself before pooling values.

### drug_exposure

- Self-reported medications. Supplements are not included in this release.
- `drug_concept_id` comes from an ingredient-level lookup.
- 18.1% of rows carry `drug_concept_id = 0`. These are brand names, combination products and free text with no exact ingredient match. `0` is the standard OMOP value for unmapped.
- Dosage is not calculated. Source values are retained.
- Missing start date becomes `1900-01-01`.
- Missing end date reuses the start date.

The source re-exports each participant's complete medication list at every survey submission, across more than 16,000 distinct submission timestamps. This release deduplicates on participant, active ingredient, drug name, reference drug, start date, end date, dosage form, dosage and frequency. Without that step, roughly three quarters of rows are duplicates.

**Medication counts in this release are therefore much lower than in version 0.1.0, and the earlier counts were inflated by that repetition.** Do not compare medication row counts across the two releases.

### condition_occurrence

Registry side: the participant's ALS diagnosis only, `condition_concept_id = 373182`, one row per participant. `condition_source_value` records the self-reported diagnosis status.

EHR side: coded problem-list and encounter diagnoses.

### visit_occurrence

Registry side: one visit per participant per date, `visit_concept_id = 38004259`, "Research Clinic/Center". EHR side: encounters as recorded in the source. EHR visit-type mapping coverage is 24.8%, because the source codes are vendor-proprietary. A newer vocabulary does not improve this.

### death

One row per deceased participant. `death_date` is set to 31 December of the year of death, so that no day or month of death is disclosed. 54 deceased participants, 7.4%, have no death year in any source and carry a blank date.

31 December rather than 1 January is deliberate: a 1 January placeholder would sit before events recorded later in the same year and break plausibility checking.

---

## Dates and timing

- Dates may be shifted for de-identification, following [Hripcsak et al., *JAMIA* 2016](https://doi.org/10.1093/jamia/ocw001).
- Where a date is missing, the survey date is used if available, otherwise an approximate date, otherwise the placeholder `1900-01-01`.
- `observation_period` spans the earliest to the latest observed date per participant, `period_type_concept_id = 32879`.
- Registry dates are written in US format. EHR dates are ISO 8601. Parse the two explicitly if you combine them.

---

## Missing data

Content not collected is excluded unless OMOP requires the field. The gaps below are inherent to the source and cannot be closed without fabricating values.

| Field | Blank or unmapped | Reason |
|---|---:|---|
| `year_of_birth` | 1.4%, 29 participants | No birth year in any available source |
| `death_date` | 7.4%, 54 deceased participants | No death year in any available source |
| `drug_concept_id` | 18.1% of rows | No exact ingredient match for brand names, combinations and free text |
| `unit_concept_id`, measurement | 100% of rows | Unit mapping is out of scope for this release |
| `visit_concept_id`, EHR encounters | 75.2% unmapped | Source codes are vendor-proprietary |
| `value_as_concept_id`, onset site | Bulbar and other sites | No suitable standard concept identified |

A modified implementation of the [OHDSI Data Quality Dashboard](https://github.com/OHDSI/DataQualityDashboard), following the Kahn et al. conformance, completeness and plausibility framework, runs 130 checks against this extract. All plausibility checks pass. The three failures are the first three rows of the table above. A zero-failure result is not achievable on this source.

---

## Custom concepts

Some ALS-specific variables have no standardized OMOP vocabulary, so local concepts above 2,000,000,000 were created:

| Concept | Content |
|---:|---|
| `2000000061` | El Escorial criteria, the question |
| `2000000057` | El Escorial: Definite |
| `2000000058` | El Escorial: Possible |
| `2000000059` | El Escorial: Probable |
| `2000000060` | El Escorial: Probable, laboratory supported. Defined but not populated |
| `2000000062` | El Escorial: Suspected |
| `2000000396` | Anatomical site of symptom onset, the question |

!!! warning "Custom concepts do not exist in Athena"
    These are local by design and appear in no Athena vocabulary release, present or future. They will not resolve if you load only the standard vocabulary tables. Load the supplied local concept definitions alongside your Athena tables, or handle the range above 2,000,000,000 explicitly in your queries.

---

## Guidance for data use

- Read `*_source_value` and `*_source_concept_id` to trace any row back to the original survey response or EHR code. Every table carries them.
- Explore concept definitions with [OHDSI Athena](https://athena.ohdsi.org/). Use the **27-FEB-2026 release or later**, otherwise the ALS gene concepts and several medical-history concepts will not resolve.
- Recover the ARC subject identifier from the trailing integer of `person.person_source_value`.
- Distinguish EHR from registry rows using `*_type_concept_id`, as described above.
- Left-join, do not inner-join, from `observation` to `visit_occurrence`, because ALSFRS-R rows carry no visit.
- Join registry and EHR laboratory data on analyte name, never on `concept_id`.
- Treat `ethnicity_concept_id = 0` as unknown, not as non-Hispanic.
- Do not compare medication row counts against version 0.1.0.
- Replace any pre-August-2026 extract with this release rather than pooling the two.

Detailed ETL documentation, the vocabulary edition and concept drift analysis, the person-level accounting of which participants are included, and the data quality results are available to data recipients on request.

---

## Surveys mapped in this release

The ARC study fields far more instruments than this release maps. The OMOP release deliberately reproduces the content footprint of version 0.1.0, refreshed from current source data, so that the two remain comparable. **No new survey instruments, question sets or measurement analytes were added in version 0.2.0.**

**Mapped:** Enrollment and general information, Your ALS Experience, New Enrollee Survey, Family History, Medical History Conditions round 1, Medical History Injuries round 1, Lifestyle round 1 tobacco flag, Occupation round 1 military service, ALSFRS-R, Medications, blood draw results, gene results, mortality.

**Collected by ARC but not mapped in this release:** education, marital status, employment status, smoking sub-detail such as age started and cigarettes per day, physical activity, hospitalization and emergency visits, clinical trial participation, geography and residential history, diet, supplements, anthropometrics, handedness and footedness, military deployment arenas, age at diagnosis, ALS complications, free-text "other" write-in fields, and the swallowing, speech, bladder and bowel symptom items. Follow-up rounds 2 through 4 of the lifestyle, occupation and conditions modules are also out of scope.

These are available through ARC Data Commons outside the OMOP release. See the [ARC preprint](https://www.researchsquare.com/article/rs-8272744/v1) for the complete picture of what ARC collects, and the [data dictionary](ga4gh.md#search-the-als-tdi-data-dictionary) for select surveys.

---

## Caution

- These data are **participant self-report plus central-laboratory results plus patient-mediated EHR extracts.** They are not a clinician-adjudicated chart review. `condition_occurrence` on the registry side carries the participant's own account of their ALS diagnosis status, not an adjudicated diagnosis.
- Treat `ethnicity_concept_id = 0` as unknown, not as non-Hispanic. See the note above before using it in a network study.
- Registry and EHR laboratory concepts are drawn from different vocabularies, so join them on analyte name rather than `concept_id`.
- Convert registry unit labels to standard units before pooling values.
- A participant with more than one EHR enrolment may carry duplicated EHR rows. Person rows are deduplicated to a single identifier, but domain rows are not.
- Diagnosis, El Escorial certainty and onset site are resolved differently than in version 0.1.0. Replace earlier extracts rather than pooling.

Problems with the data, or questions about a specific row, can be sent to [dboyce@als.net](mailto:dboyce@als.net).

---

For full OMOP domain details, see the [OMOP CDM v5.4 Reference Guide](https://ohdsi.github.io/CommonDataModel/cdm54.html).
