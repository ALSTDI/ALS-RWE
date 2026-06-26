# 🗓️ Day 1 · OMOP Common Data Model and Standardized Vocabularies

Welcome to **Day 1 of the OHDSI Training Series**!  
Today we introduce the **OMOP Common Data Model (CDM)** — the foundation for all OHDSI analytics.  
You’ll learn how data are organized, standardized, and queried using the OMOP vocabulary tables.

---

## 🎯 Objectives
By the end of this session, you should be able to:
- Explain the purpose of the OMOP CDM and its standardized structure.  
- Identify and describe **core CDM tables** (`person`, `condition_occurrence`, `drug_exposure`, etc.).  
- Understand the **role of vocabulary tables** (`concept`, `concept_relationship`, `concept_ancestor`).  
- Distinguish between **standard vs non-standard concepts**.  
- Write basic **SQL queries** to explore OMOP data.  
- Use the **Athena vocabulary browser** to find standard concepts.

---

## 🧩 Agenda

| Time | Topic |
|:--|:--|
| 09:00 – 09:30 | Welcome & Overview of OMOP CDM |
| 09:30 – 10:30 | Core Tables & Relationships |
| 10:30 – 11:00 | Break |
| 11:00 – 12:00 | Exploring the OMOP Vocabulary |
| 12:00 – 13:00 | Lunch |
| 13:00 – 14:00 | Hands-on: Querying Concepts with SQL |
| 14:00 – 14:45 | Demo: Using Athena |
| 14:45 – 15:15 | Recap & Discussion |
| 15:15 – 15:30 | Homework & Next Steps |

---

## 🧠 Slides & Materials
- 📑 **Lecture slides:** [Download Day 1 Slides (PPTX)](../training/day1-omop-cdm/Day1.pptx)
- 🧩 **SQL Examples:** [Day 1 · Code Snippets](../exercises/code_snippets/day-01-snippets.md)  
- 📘 **Cheat Sheet:** [OMOP Vocabulary and SQL Cheat Sheet](../common_artifacts/omop-vocab-sql-cheat-sheet.md)

---

## 🧭 Hands-on Activities
- The full in-class exercise lives here: **[Day 1 · Exercises](../exercises/day-01-athena-cdm.md)**.
- Need queries? See **[Day 1 · Code Snippets](../exercises/code_snippets/day-01-snippets.md)**.
- Slides: **[PPTX](../training/day1-omop-cdm/Day1.pptx)**.

---

### 2️⃣ Query the `concept` Table
```sql
SELECT concept_id,
       concept_name,
       vocabulary_id,
       standard_concept
FROM concept
WHERE concept_name LIKE 'Major depressive disorder%';
```
➡ Identify which are standard (`'S'`) vs non-standard (`NULL`).

---

### 3️⃣ Map a Non-Standard Code to a Standard Concept
```sql
SELECT *
FROM concept_relationship
WHERE concept_id_1 = <nonstandard_id>
  AND relationship_id = 'Maps to';
```
➡ Find the standard `concept_id_2`.

---

### 4️⃣ Explore Concept Relationships
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
## 🧮 Homework / Quiz Highlights
!!! tip "Check your understanding"
    The Day 1 self-check quiz and practice tasks are included in  
    **[Day 1 · Exercises](../exercises/day-01-athena-cdm.md)**.  
    Use the **[Cheat Sheet](../common_artifacts/omop-vocab-sql-cheat-sheet.md)** and  
    **[Day 1 Slides](../training/day1-omop-cdm/Day1.pptx)** for reference.
 
> See the slides and cheat sheet for full practice queries.

---

## 📚 Suggested Reading
- [**Book of OHDSI** – Common Data Model chapter](https://ohdsi.github.io/TheBookOfOhdsi/CommonDataModel.html)  
- [**Book of OHDSI** – Standardized Vocabulary chapter](https://ohdsi.github.io/TheBookOfOhdsi/StandardizedVocabularies.html)  
- [**OMOP CDM Reference**](https://ohdsi.github.io/CommonDataModel/)  
- [**Athena Vocabulary Browser**](https://athena.ohdsi.org/)  
- [**OHDSI Forum**](https://forums.ohdsi.org/) – discussion & support  

---

## 🏁 Instructor Notes
- Demonstrate basic SQL queries live.  
- Encourage use of Athena to confirm concept IDs.  
- Remind learners that vocabularies update frequently — document versions.  
- Optional challenge: map ICD codes to SNOMED standards and compare results.

---

:material-arrow-left: [Module 0 · Environment Setup](00-environment-walkthrough.md) &emsp; :material-arrow-right: [Day 2 · Vocabulary & Data Quality](day-02-vocab-dqd.md)

*Day 1 lays the foundation for querying and interpreting standardized OMOP data. Day 2 will focus on concept sets, data quality, and SQL validation.*
