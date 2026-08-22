---
title: 2026 Data Refresh
---

# 2026 Data Refresh: Changes, Vocabulary and Known Limitations

Companion to the [ALS TDI OMOP Data Set](als-tdi-omop-data-set.md) release notes. This page documents what changed in the 2026 refresh, which vocabulary edition it was built against, what is known to be incomplete, and how to reproduce the result.

Read this page before comparing this release against any earlier extract.

---

## 1. Scope of this release

The release covers ARC participants with linked biological samples, filtered out of a full registry extract of 2,014 participants. Concept identifiers, primary keys and `person_id` values are identical between the full extract and the released subset, so a subset and its parent concatenate without renumbering.

A small number of participants omitted from the primary delivery list were issued afterwards as an addendum. The addendum is a slice of the same extract rather than a separate derivation, verified field by field against the released files, so it concatenates onto the primary delivery without renumbering.

**Scope stability.** The mapped field and form footprint is unchanged from version 0.1.0. No new survey instruments, question sets or measurement analytes were added. The registry measurement concept set is identical, 43 concepts with none added and none removed, as is the registry condition concept set. Two personal medical history concepts appear in this release that were absent from version 0.1.0, transient ischemic attack and ulcerative colitis; both are checkbox items on the same Medical History Conditions round 1 form that version 0.1.0 already mapped, and both simply had no respondents at that time.

**Domains not populated.** `procedure_occurrence`, `device_exposure`, `specimen`, `note` and the remaining CDM domains are not populated in this release.

**Extraction dates**

| Component | Extracted |
|---|---|
| Registry survey drop | 2026-07-05 |
| Central-laboratory results | 2026-07-05 |
| EHR document drop | 2026-08-05 |
| ETL run | 2026-08-12 |

---

## 2. Vocabulary edition

The vocabulary bundle moved from the Athena v5.0 release of 30 August 2024 to the Athena v5.0 release of **27 February 2026**.

| | Version 0.1.0 | Version 0.2.0 |
|---|---|---|
| Athena release | v5.0, 30-AUG-2024 | **v5.0, 27-FEB-2026** |
| Vocabularies | 59 | 131, with 72 added and none removed |
| Concepts | 6,140,322, of which 2.71M standard | 10,005,299, of which 3.52M standard |
| SNOMED | 2024 editions | 2025 editions |
| LOINC | 2.77 | 2.80 |
| RxNorm | 20240506 | 20260105 |
| RxNorm Extension | 20240701 | 2026-01-14 |
| ICD-10-CM | FY2025 | FY2026 |
| ATC, HCPCS, NDC, SPL, NUCC | 2024 releases | 2026 releases |
| CPT4 | Not imported | **Not imported** |
| OMOP Genomic | Absent | **Present** |
| PPI | Absent | **Present** |

!!! warning "CPT4 is not imported"
    CPT4 requires a licensed post-download step against the UMLS API, which has not been run for either edition. If you need CPT resolution, run the CPT4 import against your own Athena download using your own UMLS licence.

### Where the vocabulary edition does and does not apply

This distinction governs how to read everything below.

- **Registry concept identifiers are not remapped at ETL time.** They are carried forward from version 0.1.0's crosswalks. Upgrading the vocabulary therefore changes nothing in the registry-side output. What it changes is whether those identifiers are still valid, still standard, and resolvable in a consumer's vocabulary tables.
- **EHR concept identifiers are mapped against the vocabulary at ETL time.** The EHR extraction for this release was mapped against the 2026 edition, so EHR concept assignments genuinely moved.

### Concept drift on the registry side

301 concept identifiers in use on the registry side were checked against both editions. Three changed. None was deleted and no domain changed.

| Concept | Change | Rows affected | Action |
|---|---|---:|---|
| `4268549` "Education received in the past - finding", SNOMED | Promoted to Standard | 459 observation | None required for validity. Separately, see the caution below |
| `38004259` visit concept, NUCC | Renamed from "Ambulatory Research Clinic / Center" to "Research Clinic/Center". Identifier unchanged | 878 visit plus 1 care_site | None. Join on identifiers, not names |
| `19125046` "sitagliptin 25 MG [Januvia]", RxNorm | **Deprecated.** Standard flag cleared, invalid reason set to `D` | 5 drug_exposure | Remap required. No automatic "Maps to" or "replaced by" relationship exists |

!!! warning "Concept `4268549` and the word education"
    This concept carries **occupational industry** in this dataset, not education, despite its name. The mapping is carried forward from version 0.1.0 and is retained for comparability rather than corrected mid-series. The 2026 promotion to Standard makes the mismatch more visible, not worse.

    Read `value_as_string` and `value_source_value`.

### Concept drift across the merged extract, including EHR

4,249 vocabulary identifiers in use across the merged extract were checked. 174 changed, none was deleted.

**Eight were deprecated or de-standardized.** Five have clean replacements:

| Concept | Content | Replacement | Rows |
|---:|---|---:|---:|
| `3002888` | RDW | `3002385` | 35 |
| `3015182` | RDW | `3019897` | 232 |
| `3022356` | CSF polymorphonuclear cells | `3042847` | 6 |
| `4193704` | Type 2 diabetes mellitus | `201826` | 4 |
| `4229881` | Weight loss | `4134010` | 1 |

One has no automatic mapping available: `19125046`, sitagliptin 25 MG, Januvia, 16 rows across the merged extract. Two are source-field only and low priority: `4039434` NSAID agent and `4273087` penicillin antibacterial agent.

**Thirty-six changed domain.** Most are in `*_source_concept_id` fields, which is harmless. A handful sit in primary concept fields and would move table under domain-based routing, all from Observation to Condition: `436235` taste sense altered, `437038` blood in urine, and `42873170` and `46273390` dependence on supplemental oxygen or respirator.

**Eleven were promoted to Standard and 120 were renamed only.** Identifiers remain valid. No action needed.

### Gaps closed by the new edition

19 concept identifiers this ETL emits were absent from the 2024 bundle, because it did not include the OMOP Genomic and PPI vocabularies. 18 of the 19 resolve in the 2026 edition:

| Gene | Concept |
|---|---:|
| `SOD1` | `35948140` |
| `C9orf72` | `35954626` |
| `TARDBP` | `35964178` |
| `FUS` | `19643404` |
| `NEK1` | `35957944` |
| `PFN1` | `35949229` |
| `SPG11` | `35950925` |
| `VCP` | `35958302` |

The self-reported ALS gene measurement rows are joinable to concept names, domains and hierarchy for the first time. The PPI personal medical history topics and three drug concepts also now resolve. One concept, `1304562`, on a single `drug_exposure` row, resolves in neither edition.

!!! danger "This is a hard requirement on consumers"
    The gene-variant and PPI concepts need the **27 February 2026 vocabulary release or later** loaded. Against a 2024 vocabulary they resolve to nothing, and the ALS genetics content of this release becomes invisible.

### Backward-compatibility hazard

Cohort logic pinned to older concept identifiers will silently under-match rather than error. The clearest case is `4272032`, "PSA measurement", which will not match rows now mapped to more specific abnormal-finding concepts. Saved cohort definitions or concept sets referencing `19125046` or any of the eight deprecated identifiers above need updating.

The six ARC custom concepts, `2000000057` through `2000000062` and `2000000396`, are local by design and appear in no Athena edition. That is intentional and is not a gap, but it does mean they must be loaded separately.

---

## 3. Content changes since the previous release

### Items that resolve to a current value

Participants' recorded answers change over time as they complete successive follow-up surveys. Version 0.1.0 emitted a row for each surveyed instance, so a participant could carry several rows for the same item that disagreed with each other. This release resolves three items to a **single current value per participant** instead.

**ALS diagnosis and El Escorial certainty.** One `observation` row and one `condition_occurrence` row per participant, taken from the participant's most recent informative answer across the ALS Experience survey rounds. An answer of "No Change" carries the most recently stated status forward. The row is dated to the submission date of that answer. Participants who have not completed an ALS Experience survey take their status from the New Enrollee Survey, dated to the possible-diagnosis date. Certainty matching is case-insensitive and accepts the "Definite" spelling variant.

**Anatomical site of symptom onset.** Taken from the New Enrollee Survey, where the registry records onset at enrolment, rather than from the follow-up rounds that re-ask the question. Fine anatomy rolls up for concept assignment, so hand becomes arm and foot becomes leg. Bulbar and other sites map to concept `0` with the verbatim site retained. Participants reporting several sites have one row per site. Rows are dated to the participant's onset date.

| | Version 0.1.0 | Version 0.2.0 |
|---|---|---|
| Diagnosis observations | 1,820, several per participant | **1,702, exactly one per participant** |
| Participants with a diagnosis | 1,368 | **1,702** |
| Diagnosis source split | Not tracked | 1,327 from the ALS Experience survey, 375 from the New Enrollee Survey |
| Onset-site rows | 12,952, repeated across rounds | **2,401, one per site per participant** |
| Participants with an onset site | 891 | **1,645** |

372 participants have a different resolved diagnosis. 351 gained one through the New Enrollee Survey, 17 no longer carry one because their only recorded answer was uninformative, and 4 changed value because the current-value rule now reflects a progression in recorded certainty.

`condition_occurrence` rose from 1,368 to 1,702 rows because the ALS diagnosis row follows the same one-per-participant resolution. `visit_occurrence` rose from 4,327 to 4,552 because New-Enrollee-dated diagnosis and onset rows introduce dates that previously had no visit.

!!! warning "Replace earlier extracts rather than pooling"
    Because these three items now resolve to a current value, an extract issued before August 2026 reports different values for them. Replace it with this release.

### Medication deduplication

The medication source re-exports each participant's complete list at every survey submission, across 16,509 distinct submission timestamps, and version 0.1.0 emitted one row per source row. Roughly 75% of `drug_exposure` rows were therefore repetitions of the same medication record.

Deduplication on participant, active ingredient, drug name, reference drug, start date, end date, dosage form, dosage and frequency takes `drug_exposure` to **9,049 rows over 1,317 participants** in the full extract. A residual few per cent of apparent duplicates are genuinely distinct: the same ingredient at a different dose on the same date.

**Medication counts in this release are not comparable with version 0.1.0.** The earlier counts were inflated by the re-export artefact.

### Birth year and death date completeness

A registry subject-level file supplied birth years and death years that were absent from version 0.1.0.

| Field | Version 0.1.0 | Version 0.2.0 | Residual |
|---|---|---|---|
| `year_of_birth` blank | 16.8% | **1.4%** | 29 participants absent from every source |
| `death_date` blank | 20.3% | **7.4%** | 54 participants absent from every source |

Imputed death dates use 31 December of the death year, capped at the extraction date so a death in the current year is never written as a future date.

### CDM v5.4 conformance

Every table is now reindexed to the full CDM v5.4 column set in canonical order before writing, with empty strings where a field is not populated, so that Achilles, the Data Quality Dashboard and ATLAS accept the files directly.

The same step integer-formats every identifier, concept identifier and year column, which removed a defect where `ethnicity_concept_id` was written as the float `38003564.0`. It also corrects a `visit_occurence_id` misspelling inherited from version 0.1.0's `measurement` table, and adds the v5.4-only `measurement_event_id` and `meas_event_field_concept_id`.

### EHR measurement dates

The EHR pipeline previously did not parse two date formats present in the source documents, a compact `YYYYMMDD` form and HL7 timestamps, and had no fallback when a laboratory result or vital sign carried no date of its own.

Both were addressed for this release, the second by falling back to the containing organizer's effective time.

| | Before | After |
|---|---|---|
| Blank `measurement_date` on EHR rows | 39,356 rows, 48.4% | **3 rows, 0.00%** |
| EHR measurements resolving to a visit | 42% | **91.7%** |

### EHR provenance and the FHIR-only view

Each EHR measurement is traced to the document it came from and to whether that document was FHIR or C-CDA. A provenance-filtered view containing only FHIR-sourced measurements is available alongside the full table, at 41,999 of 81,353 rows, 51.6%.

The finding behind it: clinically duplicate measurement rows fall from **29.1% to 5.6%** when C-CDA is excluded, because cross-document repetition in C-CDA is the source of the duplication. All 35 panel analytes survive the filter, and an agreement analysis against the registry blood draws is statistically indistinguishable between the full and FHIR-only sets.

For laboratory work the FHIR-only view is analytically sufficient and much cleaner. For maximum coverage use the full table and apply your own duplicate policy.

---

## 4. Data quality results

Two independent checks run against every release.

**Structural and reconciliation QC.** An eight-tier check covering referential integrity, primary-key uniqueness, orphan person identifiers, visit resolution, schema parity against the CDM v5.4 column set, source reconciliation per domain, and structural equality of the merged layer against the sum of its parts. **Zero failures on this release.**

**Modified Data Quality Dashboard.** A file-based implementation of a subset of the [OHDSI Data Quality Dashboard](https://github.com/OHDSI/DataQualityDashboard), following the conformance, completeness and plausibility framework of Kahn et al. 130 checks. All plausibility checks pass. Three failures, all inherent source gaps:

| Check | Result |
|---|---|
| `year_of_birth` completeness | 1.4% null |
| `death_date` completeness | 7.4% null |
| `drug_concept_id` mapped | 18.1% unmapped |

A literal zero-failure result is not achievable on this source without fabricating values.

---

## 5. Known limitations

### Coverage gaps

- **13 participants report laboratory-supported probable ALS.** The custom concept `2000000060` exists for this category but has never been populated. These participants are currently not emitted.
- **2 participants report primary lateral sclerosis**, not ALS. Currently not emitted.
- **17 participants do not carry a diagnosis row**, because their only recorded answer was uninformative.
- **40 participants have a follow-up-survey onset site but no New Enrollee Survey onset**, and so carry no onset site in this release.

### Mapping limitations

- **Concept `4268549`** is used for occupational industry although the concept means education. Carried forward from version 0.1.0 and retained for comparability. 459 rows.
- **Concept `19125046`**, sitagliptin, is deprecated in the 2026 vocabulary with no automatic replacement. The affected rows still carry the deprecated identifier. 5 rows on the registry side, 16 across the merged extract.
- **`unit_concept_id` is `0` on every measurement row**, including 32,855 EHR rows that carry a clean UCUM string in `unit_source_value`. Unit mapping is out of scope for this release.
- **EHR visit-type mapping coverage is 24.8%.** The source codes are vendor-proprietary and a newer vocabulary does not help.
- **Onset sites in the bulbar and trunk regions map to `value_as_concept_id = 0`.** Whether suitable standard concepts exist for these regions has not been settled. This matches version 0.1.0's design.
- **One `drug_exposure` row carries the literal source value `???`.** A participant reported an injected medication but the ingredient name did not save. Not recoverable without returning to the original survey response.
- **Free-text "other" write-in fields are not mapped**, on either the family history or the personal medical history forms. This matches version 0.1.0.

### Linkage and duplication

- **13 EHR records have no crosswalk link to a registry participant.** Since every EHR patient is by construction a registry participant, this is a crosswalk gap, not an EHR-only cohort. They appear in the merged extract as EHR-only persons.
- **27 of 107 EHR records are duplicate enrolments** of an already-enrolled participant. Person rows are deduplicated onto the canonical participant identifier, but domain rows are not, so a participant with two enrolments can carry duplicated measurements, conditions or medications.
- **Clinically duplicate EHR measurement rows run at 29.1%** in the full table, mostly the same timestamp repeated across documents. The FHIR-only view reduces this to 5.6%.

### Formatting artefacts

- **The merged extract writes integer-valued numerics with a trailing `.0` where the registry-only extract writes them bare.** `value_as_number` is `34` in one and `34.0` in the other, and the same applies to `drug_exposure.quantity`. Values are numerically identical. Cast to numeric before diffing or joining across the two layers, because a string-level comparison will not match.
- **74 measurement rows have a `value_source_value` longer than the CDM's varchar(50).** These are free-text laboratory comments.

---

## 6. Working with this data

Traps that have cost real analysis time, collected in one place.

| Trap | What happens | What to do |
|---|---|---|
| Joining registry blood draws to EHR labs on `concept_id` | Only 7 of 40 concepts match, so most of the data silently disappears | Join on analyte name |
| Inner-joining `observation` to `visit_occurrence` | Every ALSFRS-R row drops, and that is most of the table | Left join, or filter concepts first |
| Treating `ethnicity_concept_id = 0` as non-Hispanic | Wrong for this dataset by design | Treat `0` as unknown |
| Reading concept `4268549` by its name | You will think it is education. It is occupational industry | Read `value_as_string` |
| Trusting registry unit labels | Absolute differential counts are cells/uL despite a `10^3/mm3` label, hemoglobin is g/dL despite a `%` label, `MM01/L` means mmol/L, and `SGPT (AST)` is actually ALT | Correct units before pooling |
| Parsing all dates with one format | Registry dates are US format, EHR dates are ISO 8601 | Parse explicitly, or pass a mixed-format flag |
| Comparing medication counts against version 0.1.0 | This release deduplicates, the earlier one did not, so counts fall by roughly 75% | Do not compare across releases |
| Pooling an older extract with this one | Diagnosis, certainty and onset site resolve differently | Replace the older extract |
| String-diffing the merged layer against the registry-only layer | Trailing `.0` on integer-valued numerics makes identical values look different | Cast to numeric first |
| Loading only Athena standard vocabularies | ALS gene concepts and the six ARC custom concepts will not resolve | Load the 27-FEB-2026 release or later, plus the supplied local concepts |

If you go back to the raw ARC survey exports rather than using the OMOP output, two source-level artefacts will bite:

- Yes/no columns sometimes carry an HTML checkmark element instead of the string "Yes". A parser that tests for "Yes" will undercount these columns to zero. The ETL normalizes this across 25 columns in 12 files.
- Free text mixes plain, backslash-escaped and curly apostrophes, so one term can split into up to three apparently distinct values. Normalize apostrophes in any string handling.

---

## 7. Provenance and reproducibility

The registry-side ETL is a set of Python scripts covering the survey and central-laboratory transform, the EHR merge, CDM v5.4 column conformance, and the QC suite. Every table is written through the same conformance step, and the QC suite reconciles each domain independently against its source rather than against the ETL's own intermediate state.

The EHR side is built with **Registry Forge ALS**, which is open source:

- Project site and documentation: [alstdi.github.io/RegistryForgeALS](https://alstdi.github.io/RegistryForgeALS/)
- Preprint: Boyce D, et al. *Registry Forge: an open-source pipeline for transforming patient-mediated electronic health record exports into research-ready OMOP data.* medRxiv 2026.06.02.26354637. <https://doi.org/10.1101/2026.06.02.26354637>

Documents containing participant names are excluded by policy and are never an ETL input. Administrative roster files holding names are not read by any pipeline stage.

Detailed ETL documentation, the concept drift analysis, the person-level accounting of which participants are included and why, and the data quality results are available to data recipients on request.

---

## 8. Caution

- These data are participant self-report plus central-laboratory results plus patient-mediated EHR extracts. They are not a clinician-adjudicated chart review.
- Diagnosis, El Escorial certainty and onset site resolve to a current value in this release. Any extract issued before August 2026 reports different values. Replace it rather than pooling.
- The registry-side concept identifiers were carried forward, not re-derived against the 2026 vocabulary. They were checked for validity, which is a weaker guarantee than remapping.
- The limitations in section 5 are published here rather than resolved silently, so that an analysis can account for them.

Questions and data problem reports: [dboyce@als.net](mailto:dboyce@als.net).
