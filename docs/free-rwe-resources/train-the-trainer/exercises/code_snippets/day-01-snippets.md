# Day 1 · SQL Code Snippets

> Ready-to-run queries for exploring the OMOP CDM and standardized vocabularies. Adjust schema prefixes (`cdm.`) to match your site's configuration.

---

## 1. Explore the `concept` table

### Find a concept by name
```sql
SELECT concept_id,
       concept_name,
       domain_id,
       vocabulary_id,
       concept_class_id,
       standard_concept,
       concept_code
FROM cdm.concept
WHERE LOWER(concept_name) LIKE '%type 2 diabetes%'
ORDER BY standard_concept DESC, concept_name;
```
> `standard_concept = 'S'` → standard concept; `NULL` → non-standard (source) concept.

---

### Find a concept by exact concept_id
```sql
SELECT *
FROM cdm.concept
WHERE concept_id = 201826;   -- Type 2 diabetes mellitus (SNOMED)
```

---

### List all vocabularies in your CDM
```sql
SELECT vocabulary_id,
       vocabulary_name,
       vocabulary_reference,
       vocabulary_version
FROM cdm.vocabulary
ORDER BY vocabulary_id;
```

---

### Count concepts by domain and standard flag
```sql
SELECT domain_id,
       standard_concept,
       COUNT(*) AS concept_count
FROM cdm.concept
GROUP BY domain_id, standard_concept
ORDER BY domain_id, standard_concept;
```

---

## 2. Explore the `concept_relationship` table

### Find how a non-standard code maps to a standard concept
```sql
-- Replace 45548499 with any non-standard concept_id (e.g., an ICD-10-CM code)
SELECT cr.concept_id_1,
       c1.concept_name  AS source_concept,
       c1.vocabulary_id AS source_vocab,
       cr.relationship_id,
       cr.concept_id_2,
       c2.concept_name  AS target_concept,
       c2.standard_concept
FROM cdm.concept_relationship cr
JOIN cdm.concept c1 ON cr.concept_id_1 = c1.concept_id
JOIN cdm.concept c2 ON cr.concept_id_2 = c2.concept_id
WHERE cr.concept_id_1 = 45548499
  AND cr.relationship_id = 'Maps to'
  AND cr.invalid_reason IS NULL;
```

---

### See all relationships for a standard concept
```sql
SELECT cr.relationship_id,
       c2.concept_id,
       c2.concept_name,
       c2.vocabulary_id,
       c2.domain_id
FROM cdm.concept_relationship cr
JOIN cdm.concept c2 ON cr.concept_id_2 = c2.concept_id
WHERE cr.concept_id_1 = 201826   -- Type 2 diabetes mellitus
  AND cr.invalid_reason IS NULL
ORDER BY cr.relationship_id;
```
> Common `relationship_id` values: `'Maps to'`, `'Is a'`, `'Subsumes'`, `'Has ancestor'`, `'Maps to value'`.

---

### Find all ICD-10-CM codes that map to a given SNOMED concept
```sql
SELECT c_source.concept_id,
       c_source.concept_code,
       c_source.concept_name,
       c_source.vocabulary_id
FROM cdm.concept_relationship cr
JOIN cdm.concept c_source ON cr.concept_id_1 = c_source.concept_id
WHERE cr.concept_id_2    = 201826          -- target SNOMED concept
  AND cr.relationship_id = 'Maps to'
  AND c_source.vocabulary_id IN ('ICD10CM', 'ICD9CM')
  AND cr.invalid_reason IS NULL;
```

---

## 3. Explore the `concept_ancestor` table

### Find all descendants of a concept (for concept set building)
```sql
SELECT ca.descendant_concept_id,
       c.concept_name,
       c.vocabulary_id,
       c.standard_concept,
       ca.min_levels_of_separation,
       ca.max_levels_of_separation
FROM cdm.concept_ancestor ca
JOIN cdm.concept c ON ca.descendant_concept_id = c.concept_id
WHERE ca.ancestor_concept_id = 21600381   -- Sulfonylureas (SNOMED ingredient class)
ORDER BY ca.min_levels_of_separation, c.concept_name;
```

---

### Find all ancestors of a concept (traverse upward)
```sql
SELECT ca.ancestor_concept_id,
       c.concept_name,
       c.vocabulary_id,
       ca.min_levels_of_separation
FROM cdm.concept_ancestor ca
JOIN cdm.concept c ON ca.ancestor_concept_id = c.concept_id
WHERE ca.descendant_concept_id = 1503297   -- Metformin
  AND ca.min_levels_of_separation > 0
ORDER BY ca.min_levels_of_separation;
```

---

## 4. Explore clinical domain tables

### Count patients in the `person` table
```sql
SELECT COUNT(DISTINCT person_id) AS total_persons
FROM cdm.person;
```

---

### Demographics summary
```sql
SELECT year_of_birth,
       gender_concept_id,
       g.concept_name   AS gender,
       race_concept_id,
       r.concept_name   AS race,
       COUNT(*)         AS n
FROM cdm.person p
LEFT JOIN cdm.concept g ON p.gender_concept_id = g.concept_id
LEFT JOIN cdm.concept r ON p.race_concept_id   = r.concept_id
GROUP BY year_of_birth, gender_concept_id, g.concept_name, race_concept_id, r.concept_name
ORDER BY year_of_birth DESC;
```

---

### Count condition occurrences by standard concept
```sql
SELECT co.condition_concept_id,
       c.concept_name,
       COUNT(*) AS occurrence_count,
       COUNT(DISTINCT co.person_id) AS person_count
FROM cdm.condition_occurrence co
JOIN cdm.concept c ON co.condition_concept_id = c.concept_id
WHERE c.standard_concept = 'S'
GROUP BY co.condition_concept_id, c.concept_name
ORDER BY person_count DESC
LIMIT 25;
```

---

### Find drug exposures for a drug (using ancestor join)
```sql
-- Count metformin exposures (includes all descendants via concept_ancestor)
SELECT COUNT(*)                       AS total_exposures,
       COUNT(DISTINCT de.person_id)   AS unique_patients
FROM cdm.drug_exposure de
JOIN cdm.concept_ancestor ca
     ON ca.descendant_concept_id = de.drug_concept_id
WHERE ca.ancestor_concept_id = 1503297;   -- Metformin ingredient
```

---

### Observation period summary
```sql
SELECT
    COUNT(DISTINCT person_id)           AS persons_with_obs,
    ROUND(AVG(
        DATEDIFF(observation_period_end_date, observation_period_start_date)
    ))                                  AS avg_obs_days,
    MIN(observation_period_start_date)  AS earliest_start,
    MAX(observation_period_end_date)    AS latest_end
FROM cdm.observation_period;
```

---

## 5. Quick data quality spot checks

### Find records with concept_id = 0 (unmapped / non-standard)
```sql
-- Condition occurrences with no standard concept
SELECT COUNT(*) AS unmapped_conditions
FROM cdm.condition_occurrence
WHERE condition_concept_id = 0;

-- Drug exposures with no standard concept
SELECT COUNT(*) AS unmapped_drugs
FROM cdm.drug_exposure
WHERE drug_concept_id = 0;
```

---

### Check for implausible birth years
```sql
SELECT year_of_birth, COUNT(*) AS n
FROM cdm.person
WHERE year_of_birth < 1900 OR year_of_birth > YEAR(CURRENT_DATE)
GROUP BY year_of_birth
ORDER BY year_of_birth;
```

---

### Check observation period coverage
```sql
-- Persons with no observation period (should be 0)
SELECT COUNT(*) AS persons_without_obs
FROM cdm.person p
WHERE NOT EXISTS (
    SELECT 1
    FROM cdm.observation_period op
    WHERE op.person_id = p.person_id
);
```

---

> :material-arrow-left: [Back to Day 1 module](../../modules/day-01-omop-cdm.md) · [Back to Day 1 exercise](../day-01-athena-cdm.md) · [OMOP SQL Cheat Sheet](../../common_artifacts/omop-vocab-sql-cheat-sheet.md)
