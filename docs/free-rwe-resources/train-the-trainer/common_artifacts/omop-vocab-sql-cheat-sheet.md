# OMOP Vocabulary & SQL Cheat Sheet

> Quick-reference SQL patterns for OMOP CDM. Adjust the schema prefix (`cdm.`) to match your site. These patterns work across Postgres, SQL Server, Snowflake, Databricks, and BigQuery — only the date functions and `LIMIT`/`TOP` syntax differ by platform.

---

## Vocabulary Tables

| Table | What it contains |
|:--|:--|
| `concept` | All standard and non-standard concepts: id, name, domain, vocabulary, class, code |
| `concept_relationship` | Directed links between concepts: `Maps to`, `Is a`, `Subsumes`, `Has ancestor` |
| `concept_ancestor` | Pre-computed transitive ancestor/descendant pairs with level-of-separation counts |
| `concept_synonym` | Alternate names for concepts |
| `vocabulary` | Vocabulary metadata and version |
| `domain` | Domain definitions |
| `concept_class` | Concept class definitions |
| `relationship` | Relationship type definitions |

---

## 1. Concept Lookup

```sql
-- Find concepts by name (partial match)
SELECT concept_id, concept_name, domain_id,
       vocabulary_id, standard_concept, concept_code
FROM cdm.concept
WHERE LOWER(concept_name) LIKE '%amyotrophic lateral sclerosis%'
ORDER BY standard_concept DESC NULLS LAST;

-- Look up a specific concept_id
SELECT * FROM cdm.concept WHERE concept_id = 4051114;

-- Find all standard concepts in a domain
SELECT concept_id, concept_name, vocabulary_id
FROM cdm.concept
WHERE domain_id = 'Condition'
  AND standard_concept = 'S'
  AND LOWER(concept_name) LIKE '%motor neuron%';
```

---

## 2. Concept Relationships

```sql
-- Find the standard concept a source code maps to
SELECT c_source.concept_code, c_source.vocabulary_id,
       c_target.concept_id, c_target.concept_name,
       c_target.standard_concept
FROM cdm.concept_relationship cr
JOIN cdm.concept c_source ON cr.concept_id_1 = c_source.concept_id
JOIN cdm.concept c_target ON cr.concept_id_2 = c_target.concept_id
WHERE c_source.concept_code = 'G12.21'     -- ALS ICD-10-CM code
  AND c_source.vocabulary_id = 'ICD10CM'
  AND cr.relationship_id = 'Maps to';

-- Find all source codes that map to a given standard concept
SELECT c_src.concept_code, c_src.vocabulary_id, c_src.concept_name
FROM cdm.concept_relationship cr
JOIN cdm.concept c_src ON cr.concept_id_1 = c_src.concept_id
WHERE cr.concept_id_2    = 4051114         -- ALS SNOMED concept
  AND cr.relationship_id = 'Maps to'
  AND cr.invalid_reason IS NULL;
```

---

## 3. Concept Ancestor (Hierarchy)

```sql
-- All descendants of a concept (for concept set coverage)
SELECT ca.descendant_concept_id, c.concept_name,
       ca.min_levels_of_separation
FROM cdm.concept_ancestor ca
JOIN cdm.concept c ON ca.descendant_concept_id = c.concept_id
WHERE ca.ancestor_concept_id = 21600381    -- Sulfonylureas
  AND ca.min_levels_of_separation >= 1
ORDER BY ca.min_levels_of_separation, c.concept_name;

-- Direct children only (level 1)
SELECT ca.descendant_concept_id, c.concept_name
FROM cdm.concept_ancestor ca
JOIN cdm.concept c ON ca.descendant_concept_id = c.concept_id
WHERE ca.ancestor_concept_id       = 1503297    -- Metformin
  AND ca.min_levels_of_separation  = 1;

-- Count descendants by level
SELECT ca.min_levels_of_separation, COUNT(*) AS n
FROM cdm.concept_ancestor ca
WHERE ca.ancestor_concept_id = 4051114
GROUP BY ca.min_levels_of_separation
ORDER BY ca.min_levels_of_separation;
```

---

## 4. Clinical Domain Queries

### Person / Demographics
```sql
SELECT COUNT(DISTINCT person_id)            AS n_persons,
       AVG(YEAR(CURRENT_DATE) - year_of_birth) AS mean_age,
       SUM(CASE WHEN gender_concept_id = 8507 THEN 1 ELSE 0 END) AS n_male,
       SUM(CASE WHEN gender_concept_id = 8532 THEN 1 ELSE 0 END) AS n_female
FROM cdm.person;
```

### Condition Occurrence
```sql
-- Patients with a specific condition (standard concept + descendants)
SELECT COUNT(DISTINCT co.person_id) AS patients_with_condition
FROM cdm.condition_occurrence co
JOIN cdm.concept_ancestor ca ON ca.descendant_concept_id = co.condition_concept_id
WHERE ca.ancestor_concept_id = 4051114;    -- ALS

-- Condition occurrence rate by year
SELECT YEAR(condition_start_date) AS year,
       COUNT(DISTINCT person_id)  AS unique_patients
FROM cdm.condition_occurrence
WHERE condition_concept_id IN (
    SELECT descendant_concept_id FROM cdm.concept_ancestor
    WHERE ancestor_concept_id = 4051114
)
GROUP BY YEAR(condition_start_date)
ORDER BY year;
```

### Drug Exposure
```sql
-- Drug exposures via ancestor (captures all formulations)
SELECT COUNT(*)                     AS total_exposures,
       COUNT(DISTINCT de.person_id) AS unique_patients
FROM cdm.drug_exposure de
JOIN cdm.concept_ancestor ca ON ca.descendant_concept_id = de.drug_concept_id
WHERE ca.ancestor_concept_id = 1503297;   -- Metformin

-- Drug era (pre-computed continuous exposure periods)
SELECT person_id, drug_concept_id,
       drug_era_start_date, drug_era_end_date,
       drug_exposure_count
FROM cdm.drug_era
WHERE drug_concept_id IN (
    SELECT descendant_concept_id FROM cdm.concept_ancestor
    WHERE ancestor_concept_id = 1503297
);
```

### Measurement
```sql
-- Find standard measurement concepts (e.g., HbA1c)
SELECT m.person_id,
       c.concept_name,
       m.value_as_number,
       m.unit_source_value,
       m.measurement_date
FROM cdm.measurement m
JOIN cdm.concept c ON m.measurement_concept_id = c.concept_id
WHERE c.concept_name LIKE '%Hemoglobin A1c%'
  AND c.standard_concept = 'S'
ORDER BY m.measurement_date;
```

### Visit Occurrence
```sql
-- Visit counts by type
SELECT c.concept_name AS visit_type, COUNT(*) AS n_visits,
       COUNT(DISTINCT vo.person_id) AS n_patients
FROM cdm.visit_occurrence vo
JOIN cdm.concept c ON vo.visit_concept_id = c.concept_id
GROUP BY c.concept_name
ORDER BY n_visits DESC;
```

---

## 5. Cohort Validation Patterns

### Count a generated cohort
```sql
SELECT COUNT(DISTINCT subject_id) AS cohort_size
FROM results.cohort
WHERE cohort_definition_id = [your_cohort_id];
```

### Cohort attrition (simple)
```sql
-- Persons in cohort vs. total persons in CDM
SELECT
    (SELECT COUNT(DISTINCT person_id) FROM cdm.person)      AS total_cdm,
    (SELECT COUNT(DISTINCT subject_id) FROM results.cohort
     WHERE cohort_definition_id = [your_cohort_id])          AS cohort_size;
```

### Validate concept set coverage against a domain table
```sql
-- Drug exposures captured by your concept set (ancestor-based)
SELECT COUNT(*) AS exposures_in_set,
       COUNT(DISTINCT de.person_id) AS persons_in_set
FROM cdm.drug_exposure de
JOIN cdm.concept_ancestor ca ON ca.descendant_concept_id = de.drug_concept_id
WHERE ca.ancestor_concept_id = [your_ingredient_concept_id];
```

---

## 6. Data Quality Spot Checks

```sql
-- Records with unmapped concepts (concept_id = 0)
SELECT 'condition_occurrence' AS domain, COUNT(*) AS n
FROM cdm.condition_occurrence WHERE condition_concept_id = 0
UNION ALL
SELECT 'drug_exposure',                  COUNT(*)
FROM cdm.drug_exposure      WHERE drug_concept_id = 0
UNION ALL
SELECT 'measurement',                    COUNT(*)
FROM cdm.measurement        WHERE measurement_concept_id = 0;

-- Persons without any observation period
SELECT COUNT(*) AS orphaned_persons
FROM cdm.person p
WHERE NOT EXISTS (
    SELECT 1 FROM cdm.observation_period op
    WHERE op.person_id = p.person_id
);

-- Future birth years (implausible)
SELECT year_of_birth, COUNT(*) AS n
FROM cdm.person
WHERE year_of_birth > YEAR(CURRENT_DATE)
GROUP BY year_of_birth;
```

---

## Platform Syntax Notes

| Function | PostgreSQL | SQL Server | Spark / Databricks | BigQuery |
|:--|:--|:--|:--|:--|
| Date difference (days) | `AGE()` / `DATEDIFF` | `DATEDIFF(day,…)` | `DATEDIFF(…)` | `DATE_DIFF(…, DAY)` |
| Current date | `CURRENT_DATE` | `CAST(GETDATE() AS DATE)` | `CURRENT_DATE` | `CURRENT_DATE` |
| Row limit | `LIMIT n` | `TOP n` | `LIMIT n` | `LIMIT n` |
| String search | `ILIKE` (case-insensitive) | `LIKE` (case-insensitive by default) | `LIKE` with `LOWER()` | `LIKE` with `LOWER()` |

---

> :material-arrow-left: [Day 1 Code Snippets](../exercises/code_snippets/day-01-snippets.md) · [SQL Validation Mini Lab](sql-validation-mini-lab.md) · [Back to Resources](../resources.md)
