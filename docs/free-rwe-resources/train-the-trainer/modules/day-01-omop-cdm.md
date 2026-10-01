# Day 1 · OMOP Common Data Model and Standardized Vocabularies

Welcome to **Day 1 of the OHDSI Training Series**!  
Today we introduce the **OMOP Common Data Model (CDM)** — the foundation for all OHDSI analytics.  
You’ll learn how data are organized, standardized, and queried using the OMOP vocabulary tables.

---

## Objectives
By the end of this session, you should be able to:
- Explain the purpose of the OMOP CDM and its standardized structure.  
- Identify and describe **core CDM tables** (`person`, `condition_occurrence`, `drug_exposure`, etc.).  
- Understand the **role of vocabulary tables** (`concept`, `concept_relationship`, `concept_ancestor`).  
- Distinguish between **standard vs non-standard concepts**.  
- Write basic **SQL queries** to explore OMOP data.  
- Use the **Athena vocabulary browser** to find standard concepts.

---

## Agenda

| Time | Topic |
|:--|:--|
| 9:30 – 9:45 | Welcome and OHDSI / OMOP overview |
| 9:45 – 10:25 | CDM architecture: clinical tables |
| 10:25 – 10:40 | Break |
| 10:40 – 11:10 | Vocabulary tables and standardization |
| 11:10 – 11:35 | Live demo: Athena vocabulary browser |
| 11:35 – 12:25 | SQL lab: explore CDM and vocabulary tables |
| 12:25 – 12:45 | Discussion: standard vs non-standard concepts |
| 12:45 – 1:00 | Recap, homework, Day 2 preview |

Each session is a half day. The times follow the sample schedule on the program overview page; shift them to suit your group.

---

## Slides & Materials

| File | Description |
|:--|:--|
| [Instructor Deck](../training/day-01-omop-cdm/kit/Instructor-Deck-with-Notes.pptx) | Full slide deck with speaker notes |
| [Participant Workbook](../training/day-01-omop-cdm/kit/Participant-Workbook.pptx) | Workbook with fill-in exercises |
| [Kahoot Quiz](../training/day-01-omop-cdm/kit/Kahoot-Quiz.csv) | OMOP CDM quiz |

- **SQL Examples:** [Day 1 · Code Snippets](../exercises/code_snippets/day-01-snippets.md)  
- **Cheat Sheet:** [OMOP Vocabulary and SQL Cheat Sheet](../common_artifacts/omop-vocab-sql-cheat-sheet.md)

---

## Hands-on Activities
- The full in-class exercise lives here: **[Day 1 · Exercises](../exercises/day-01-athena-cdm.md)**.
- Need queries? See **[Day 1 · Code Snippets](../exercises/code_snippets/day-01-snippets.md)**.
- Slides: **[Instructor Deck](../training/day-01-omop-cdm/kit/Instructor-Deck-with-Notes.pptx)** · **[Participant Workbook](../training/day-01-omop-cdm/kit/Participant-Workbook.pptx)**.

---

### 1. Query the `concept` Table
```sql
SELECT concept_id,
       concept_name,
       vocabulary_id,
       standard_concept
FROM concept
WHERE concept_name LIKE 'Amyotrophic lateral sclerosis%';
```
Identify which are standard (`'S'`), classification (`'C'`), or non-standard (`NULL`).

---

### 2. Map a Non-Standard Code to a Standard Concept
```sql
SELECT *
FROM concept_relationship
WHERE concept_id_1 = <nonstandard_id>
  AND relationship_id = 'Maps to';
```
Find the standard `concept_id_2`.

---

### 3. Explore Concept Relationships
```sql
SELECT cr.relationship_id,
       c.concept_name AS related_concept,
       c.domain_id
FROM concept_relationship cr
JOIN concept c ON cr.concept_id_2 = c.concept_id
WHERE cr.concept_id_1 = <standard_concept_id>;
```
- Look for “Is a,” “Subsumes,” and “Mapped from” relationships.  
- Note hierarchical links for concept set creation.

---
## Homework / Quiz Highlights
!!! tip "Check your understanding"
    The Day 1 self-check quiz and practice tasks are included in  
    **[Day 1 · Exercises](../exercises/day-01-athena-cdm.md)**.  
    Use the **[Cheat Sheet](../common_artifacts/omop-vocab-sql-cheat-sheet.md)** and  
    **[Day 1 Instructor Deck](../training/day-01-omop-cdm/kit/Instructor-Deck-with-Notes.pptx)** for reference.
 
> See the slides and cheat sheet for full practice queries.

---

## Suggested Reading
- [**Book of OHDSI** – Common Data Model chapter](https://ohdsi.github.io/TheBookOfOhdsi/CommonDataModel.html)  
- [**Book of OHDSI** – Standardized Vocabulary chapter](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html)  
- [**OMOP CDM Reference**](https://ohdsi.github.io/CommonDataModel/)  
- [**Athena Vocabulary Browser**](https://athena.ohdsi.org/)  
- [**OHDSI Forum**](https://forums.ohdsi.org/) – discussion & support  

---

## Instructor Notes
- Demonstrate basic SQL queries live.  
- Encourage use of Athena to confirm concept IDs.  
- Remind learners that major vocabulary releases come twice a year (February and August) and that each site loads them on its own schedule, so the version in use should be documented.  
- Optional challenge: map ICD codes to SNOMED standards and compare results.

---

:material-arrow-left: [Module 0 · Environment Setup](00-environment-walkthrough.md) &emsp; :material-arrow-right: [Day 2 · Vocabulary & Data Quality](day-02-vocab-dqd.md)

*Day 1 lays the foundation for querying and interpreting standardized OMOP data. Day 2 will focus on concept sets, data quality, and SQL validation.*
