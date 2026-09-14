---
title: 2026 Data Refresh
---

# 2026 Data Refresh

Companion to the [ALS TDI OMOP Data Set](als-tdi-omop-data-set.md) release notes. This page covers what a recipient needs to work with the 2026 release and how it differs from the 2025 release (version 0.1.0). Read it before comparing the two.

---

## 1. Scope

The release covers **708 ARC participants with linked biological samples**, drawn from a registry of 2,014. The mapped instruments and concept sets are unchanged from version 0.1.0: 43 measurement concepts (35 laboratory analytes and 8 self-reported ALS gene concepts) and the same condition concept set. The personal medical history grid is now taken from all four survey rounds rather than round 1 only (see Section 3).

`procedure_occurrence`, `device_exposure`, `specimen`, `note` and the remaining CDM domains are not populated. Tables conform to the CDM v5.4 column set and are accepted directly by Achilles, the Data Quality Dashboard and ATLAS.

**Data vintage:** registry surveys 2026-07-05 · central-laboratory results 2026-09-11 · EHR documents 2026-08-05 · release assembled 2026-09-13.

## 2. Vocabulary

Built against the **Athena v5.0 release of 27 February 2026** (version 0.1.0 used 30-AUG-2024). Load that edition or later; earlier bundles lack OMOP Genomic and PPI, so the ALS gene concepts will not resolve. Vocabularies in use: SNOMED, LOINC (in `measurement_source_value` on EHR rows), RxNorm, NUCC, UCUM, OMOP Genomic, PPI.

The six ARC custom concepts (`2000000057`–`2000000062`, `2000000396`) are local by design and must be loaded alongside the standard tables.

ALS gene concepts: SOD1 `35948140` · C9orf72 `35954626` · TARDBP `35964178` · FUS `19643404` · NEK1 `35957944` · PFN1 `35949229` · SPG11 `35950925` · VCP `35958302`.

## 3. Structure and semantics

**Three measurement sources, machine-distinguishable.** `measurement_type_concept_id` partitions the table: `32856` central laboratory (56,445 rows, 420 participants), `32817` EHR-derived (16,934 rows, 47 participants; new in this release), `32862` self-reported gene results (80 rows, 75 participants). EHR rows carry the registry analyte concepts with the original LOINC code in `measurement_source_value`, are already deduplicated, and are the only rows with `measurement_datetime` populated. EHR-derived visits carry `care_site_id` 21; all others carry 20.

**Every event links to a visit.** `visit_occurrence` (22,969 rows) spans five classes — survey, ALSFRS-R, participant data, blood draw, EHR lab — and 100% of `measurement` and `observation` rows resolve to a visit of the matching class. Every event date falls within its participant's observation period.

**Observation periods span all recorded event dates**, deliberately including retrospective self-reported dates such as symptom onset and medication history — the prodrome interval matters in ALS. No period ends after the extraction date. Participants with no dated event (10 of 708) carry no period. If your person-time method requires data-capture contact only, derive spans by filtering events on the type concepts above.

**Survey items are current-value; ALSFRS-R is longitudinal.** Apart from ALSFRS-R and conditions, each survey item carries one current instance per participant — the most recent informative answer. Diagnosis, El Escorial certainty and onset site resolved this way for the first time in this release, so version 0.1.0 reports different values for them: **replace it rather than pooling**. Multi-select items (family history, occupational industry, onset site) carry one row per selected value. Interval-anchored follow-up questions ("hospitalized in the past 3 months?") are outside the mapped footprint of both releases. ALSFRS-R is the longitudinal record: one row per scale item per assessment, 17,313 assessments over 670 participants; same-day duplicate assessments are retained.

**Conditions take affirmatives from all rounds:** one row per participant per condition, dated to the round that first reported it (485 rows, 304 participants). A later blank is silence, not retraction — the module contains no explicit negations. Note the lifestyle smoking item maps round 1's lifetime-history question only; the follow-up rounds ask a different question (current smoking) that is not mapped.

**Medications are deduplicated** (3,142 rows, 529 participants); version 0.1.0 emitted one row per source re-export, so its counts are inflated roughly fourfold and are not comparable. Imputed death dates use 31 December of the death year, capped at the extraction date.

## 4. Known limitations

- Nine `death` rows carry the placeholder date **1900-01-01** — a death with an unknown date, not an event in 1900.
- `unit_concept_id` is `0` on dimensionless ratios by design (A/G, BUN/creatinine); elsewhere it is populated on 94.3% of central-laboratory and 90.1% of EHR rows. Rows whose source unit could not be established are excluded rather than delivered unitless.
- Bulbar and trunk onset sites map to `value_as_concept_id = 0` with the verbatim site in `value_source_value`.
- Free-text "other" write-in fields are not mapped (family history and personal medical history forms).
- A small number of participants carry no diagnosis row (only recorded answer was uninformative) or no onset site (onset is taken from the New Enrollee Survey only).
- EHR encounter structure is not imported; EHR-derived visits are date-based extract visits.

## 5. Working with these data

| Situation | What to know | What to do |
|---|---|---|
| Joining registry blood draws to EHR labs | Both carry the same 35 registry analyte concepts; LOINC is in `measurement_source_value` | Join on `measurement_concept_id` |
| Distinguishing data sources | Type concepts partition sources: `32856` lab, `32817` EHR, `32862` self-report | Filter on the type concept |
| Person-time or incidence | Periods include retrospective self-reported dates by design | Derive contact-based spans via type concepts if needed |
| Longitudinal history of a survey item | Only ALSFRS-R is longitudinal | Other items reflect the most recent informative answer |
| `ethnicity_concept_id = 0` | Means unknown, by design | Treat `0` as unknown |
| Units vs. version 0.1.0 | Unit labels and concepts were corrected in this release (hemoglobin g/dL, mmol/L electrolytes, cells/uL differentials, ALT labelling) | See the DIVERGENCES documentation before cross-release comparison |
| Date formats | Registry dates are US format, EHR dates are ISO 8601 | Parse explicitly |
| Any comparison with version 0.1.0 | Diagnosis, certainty, onset site, measurements, medications and visit structure all differ | Replace it with this release |
| Loading vocabularies | Gene and custom concepts need the 27-FEB-2026 release plus the supplied local concepts | Load both |

Working from the raw survey exports instead: yes/no columns sometimes carry an HTML checkmark instead of "Yes", and free text mixes three apostrophe encodings — normalize both.

## 6. Provenance

The registry-side transform and the EHR side (built with the open-source **[Registry Forge ALS](https://alstdi.github.io/RegistryForgeALS/)**; preprint: Boyce D, et al., medRxiv [2026.06.02.26354637](https://doi.org/10.1101/2026.06.02.26354637)) are documented in the METHODS and QC files that accompany the delivery. Documents containing participant names are excluded by policy and are never a pipeline input. Detailed documentation and person-level inclusion accounting are available to data recipients on request.

## 7. Caution

These data are participant self-report plus central-laboratory results plus patient-mediated EHR extracts — not a clinician-adjudicated chart review.

Questions and data problem reports: [dboyce@als.net](mailto:dboyce@als.net).
