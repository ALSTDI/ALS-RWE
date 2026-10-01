# The ALS Use Case: Motor Neuron Disease, ALS Medications, and the ALSFRS-R

Every session in this program uses the same ALS example, so that learners follow one question from the vocabulary through to an analysis. This page defines the example and lists the concepts behind it. The maternal and child health edition of the curriculum, with diabetes and pregnancy examples, is kept in a separate repository.

## The running question

> Among people with motor neuron disease who start riluzole, what do the data show about their ALS Functional Rating Scale - Revised (ALSFRS-R) scores over the following year?

The question has a diagnosis, a medication, and a functional score, and each one teaches something different about the OMOP Common Data Model (CDM).

| Part of the question | Domain | How it is defined in this program | Where it is taught |
|:--|:--|:--|:--|
| Motor neuron disease | Condition | The SNOMED concept "Motor neuron disease" (code 37340000) with its descendants, which include amyotrophic lateral sclerosis (ALS, concept_id 373182) | Day 1 hierarchy, Day 2 concept sets, Day 3 inclusion rule |
| ALS medications | Drug | The RxNorm ingredients riluzole and edaravone with their descendants, plus other ALS medications your site records | Day 2 concept sets, Day 3 entry event, Day 5 pathways |
| ALSFRS-R | Observation or Measurement, depending on the site | The LOINC codes for the scale, the total score, and the items | Day 1 domains, Day 2 data quality, Feasibility First |

Confirm every concept ID and code in [Athena](https://athena.ohdsi.org/) for the vocabulary version your site runs. The lookup queries below do that inside your own CDM.

## Motor neuron disease and the terms below it

Using the broad concept with descendants picks up ALS and the other motor neuron disease terms in one concept set, which is how diagnoses are usually pulled for this example.

```sql
-- Find the concept, then list what sits below it
SELECT concept_id, concept_name, standard_concept
FROM cdm.concept
WHERE vocabulary_id = 'SNOMED' AND concept_code = '37340000';   -- Motor neuron disease

SELECT c.concept_id, c.concept_name, ca.min_levels_of_separation
FROM cdm.concept_ancestor ca
JOIN cdm.concept c ON c.concept_id = ca.descendant_concept_id
WHERE ca.ancestor_concept_id = :motor_neuron_disease_concept_id
ORDER BY ca.min_levels_of_separation, c.concept_name;
```

The ICD-10-CM code G12.21 (amyotrophic lateral sclerosis) is a non-standard source code that maps to the standard ALS concept, which makes it a good code for the "Maps to" exercise on Day 1.

## ALS medications

Riluzole and edaravone are RxNorm ingredients, and adding each one with descendants captures its products. Add other ALS medications your site records in the same way. Two points about data capture come up in the labs:

- A medication given by infusion in a clinic may be recorded as a procedure, or not at all, and will then be missing from `drug_exposure`.
- Medications supplied outside the health system may not appear in an EHR-derived CDM.

```sql
SELECT concept_id, concept_name
FROM cdm.concept
WHERE vocabulary_id = 'RxNorm'
  AND concept_class_id = 'Ingredient'
  AND LOWER(concept_name) IN ('riluzole', 'edaravone');
```

Riluzole also sits under the ATC class N07XX (other nervous system drugs). That class is a classification concept and is too broad to use as an ALS medication set, which is why the labs list ingredients.

## The ALSFRS-R: coded in LOINC, often recorded in notes

The ALSFRS-R has LOINC codes for the scale as a whole, for the total score, and for each item, so the concepts exist in the OMOP vocabulary.

| LOINC code | Name |
|:--|:--|
| 82954-9 | Amyotrophic lateral sclerosis functional rating scale - revised [ALSFRS-R] (the panel) |
| 82953-1 | Total score [ALSFRS-R] |
| 82940-8 | Speech [ALSFRS-R] |
| 82941-6 | Salivation [ALSFRS-R] |
| 82948-1 | Walking [ALSFRS-R] |

The remaining items have their own codes in the same panel, including an alternate "cutting food" item for people with a gastrostomy. LOINC describes the scale as twelve items, each rated 0 to 4, for a total of 0 to 48.

At many sites the scores are written in clinic notes and never reach a structured table. That makes the ALSFRS-R the example this program uses for the difference between a concept that **exists** in the vocabulary and a concept that is **present** in the data. A search in Athena finds the codes at every site. A count in your CDM may find few records or none.

```sql
-- 1. The ALSFRS-R concepts in your vocabulary, with the domain each one is assigned to
SELECT concept_id, concept_code, concept_name, domain_id, standard_concept
FROM cdm.concept
WHERE vocabulary_id = 'LOINC' AND concept_name LIKE '%ALSFRS-R%'
ORDER BY concept_code;

-- 2. Are structured scores present? Check both tables.
SELECT 'observation' AS source_table, COUNT(*) AS n_rows, COUNT(DISTINCT o.person_id) AS persons
FROM cdm.observation o
JOIN cdm.concept c ON c.concept_id = o.observation_concept_id
WHERE c.vocabulary_id = 'LOINC' AND c.concept_name LIKE '%ALSFRS-R%'
UNION ALL
SELECT 'measurement', COUNT(*), COUNT(DISTINCT m.person_id)
FROM cdm.measurement m
JOIN cdm.concept c ON c.concept_id = m.measurement_concept_id
WHERE c.vocabulary_id = 'LOINC' AND c.concept_name LIKE '%ALSFRS-R%';

-- 3. If your CDM has a NOTE table, do the notes mention the scale?
SELECT COUNT(*) AS notes, COUNT(DISTINCT person_id) AS persons
FROM cdm.note
WHERE LOWER(note_text) LIKE '%alsfrs%';
```

When the first query returns concepts and the second returns nothing, the data are not missing because of a mapping error. The scores were never captured as structured data. The options are then to extract them from notes (the CDM has `NOTE` and `NOTE_NLP` tables for this), to abstract them by hand, or to take the question to a source that records the scale directly.

## How the ALS TDI OMOP data set records these

The [ALS TDI OMOP data set](../../als-tdi-omop-data-set.md) is an example of a source that does hold structured ALSFRS-R scores. As documented on that page and in the [2026 data refresh](../../omop-2026-refresh.md):

- **ALSFRS-R** is in the `observation` table, on concept IDs `42529071` to `42529084` (the items and the total score), with the score in `value_as_number` and one row per item per assessment. The rows are participant self-report (`observation_type_concept_id = 32862`), and the ALSFRS-R is the one survey instrument in the release that is longitudinal.
- **Diagnosis** is in `condition_occurrence` as the ALS concept `373182`, one row per participant.
- **Medications** are in `drug_exposure`, from participant self-report, mapped at the ingredient level.

A registry that collects the scale directly and an EHR that keeps it in notes will give very different answers to the presence queries above, and comparing the two is a useful exercise for a group that has access to both.

## Sources

- LOINC, ALSFRS-R panel: <https://loinc.org/82954-9>
- LOINC, ALSFRS-R total score: <https://loinc.org/82953-1/>
- ALS TDI OMOP data set documentation on this site: [overview](../../als-tdi-omop-data-set.md) and [2026 data refresh](../../omop-2026-refresh.md)
- OMOP CDM v5.4 table reference (NOTE and NOTE_NLP): <https://ohdsi.github.io/CommonDataModel/cdm54.html>
