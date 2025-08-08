---
title: OMOP/OHDSI Resources
---

This chapter contains practical resources for working with Observational Health Data Science and Informatics (OHDSI) community resources and Observational Medical Outcomes Partnership (OMOP) data, including an interactive OMOP data dictionary, code snippets for common analytic tasks using a variety of software, and examples of observational research projects suited to OMOP/OHDSI frameworks.  For a good overview of OHDSI/OMOP, please see the resources in the chapter, "Free RWE Resources."

Resources include:

- **Interactive OMOP CDM Data Dictionary**
- **Analytic Use Cases and Research Examples**
- **OMOP Code Snippets (SQL, R, Python)**

---

## 📊 OMOP CDM Basic Data Dictionary

For a sample interactive OMOP data dictionary detailing the fields in the OMOP CDM, please click on the thumbnail below. For the specific ARC study data dictionary, visit the [Neuromine Data Portal](https://data.answerals.org/home).

[![OMOP Data Dictionary Thumbnail](assets/DDthumbnail.png)](assets/OMOPDD.html)

## 📈 Projects Best Suited for Observational Research and OHDSI Network Studies

---

<h3>🧪 Analytic Use Cases and Examples</h3>

<style>
  table.use-case-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1em;
  }

  table.use-case-table th,
  table.use-case-table td {
    border: 1px solid #aaa;
    padding: 8px;
    text-align: left;
    vertical-align: top;
  }

  table.use-case-table th {
    background-color: #f2f2f2;
  }
</style>

<table class="use-case-table">
  <thead>
    <tr>
      <th>Analytic Use Case</th>
      <th>Type</th>
      <th>Structure</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3"><strong>Clinical Characterization</strong></td>
      <td>Disease Natural History</td>
      <td>Amongst patients who are diagnosed with &lt;insert your disease of interest&gt;, what are the patient’s characteristics from their medical history?</td>
      <td>Amongst patients with rheumatoid arthritis, what are their demographics (age, gender), prior conditions, medications, and health service utilization behaviors?</td>
    </tr>
    <tr>
      <td>Treatment Utilization</td>
      <td>Amongst patients who have &lt;insert your disease of interest&gt;, which treatments were patients exposed to amongst &lt;list of treatments for disease&gt; and in which sequence?</td>
      <td>Amongst patients with depression, which treatments were patients exposed to SSRI, SNRI, TCA, bupropion, esketamine and in which sequence?</td>
    </tr>
    <tr>
      <td>Outcome Incidence</td>
      <td>Amongst patients who are new users of &lt;insert your drug of interest&gt;, how many patients experienced &lt;insert your known adverse event of interest from the drug profile&gt; within &lt;time horizon following exposure start&gt;?</td>
      <td>Amongst patients who are new users of methylphenidate, how many patients experienced psychosis within 1 year of initiating treatment?</td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Population-level Effect Estimation</strong></td>
      <td>Safety Surveillance</td>
      <td>Does exposure to &lt;insert your drug of interest&gt; increase the risk of experiencing &lt;insert an adverse event&gt; within &lt;time horizon following exposure start&gt;?</td>
      <td>Does exposure to ACE inhibitor increase the risk of experiencing Angioedema within 1 month after exposure start?</td>
    </tr>
    <tr>
      <td>Comparative Effectiveness</td>
      <td>Does exposure to &lt;insert your drug of interest&gt; have a different risk of experiencing &lt;insert any outcome (safety or benefit)&gt; within &lt;time horizon following exposure start&gt;, relative to &lt;insert your comparator treatment&gt;?</td>
      <td>Does exposure to ACE inhibitor have a different risk of experiencing acute myocardial infarction while on treatment, relative to thiazide diuretic?</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>Patient-level Prediction</strong></td>
      <td>Disease Onset and Progression</td>
      <td>For a given patient who is diagnosed with &lt;insert your disease of interest&gt;, what is the probability that they will go on to have &lt;another disease or related complication&gt; within &lt;time horizon from diagnosis&gt;?</td>
      <td>For a given patient who is newly diagnosed with atrial fibrillation, what is the probability that they will go on to have ischemic stroke in next 3 years?</td>
    </tr>
    <tr>
      <td>Treatment Response</td>
      <td>For a given patient who is a new user of &lt;insert your chronically-used drug of interest&gt;, what is the probability that they will &lt;insert desired effect&gt; in &lt;time window&gt;?</td>
      <td>For a given patient with T2DM who starts on metformin, what is the probability that they will maintain HbA1C &lt;6.5% after 3 years?</td>
    </tr>
    <tr>
      <td>Treatment Safety</td>
      <td>For a given patient who is a new user of &lt;insert your drug of interest&gt;, what is the probability that they will experience &lt;insert adverse event&gt; within &lt;time horizon following exposure&gt;?</td>
      <td>For a given patient who is a new user of warfarin, what is the probability that they will have GI bleed in 1 year?</td>
    </tr>
  </tbody>
</table>

**Source:** OHDSI. *(2023).* [Save Our Sisyphus Challenge Slides (PDF)](https://www.ohdsi.org/wp-content/uploads/2023/01/SOS-challenge-intro-24jan2023.pdf)
---
---

## 🧭 Current CDM

![CDM54 Image](assets/cdm54.png)

*Source: [OHDSI Common Data Model](https://ohdsi.github.io/CommonDataModel/index.html)*



- 🔗 **Interactive (Select) OMOP Data Dictionary**  
  https://github.com/DBJHU/DBJHU.github.io/blob/main/SelectOMOPDataDictionaryInteractivev2.html



---

## 🗂️ Commonly Used CDM Tables Overview

The OMOP common data model (CDM) is a relational database made up of different tables that relate to each other by foreign keys (XXXX_ID values; e.g., PERSON_ID or PROVIDER_ID). The OMOP tables in your data export are as follows:

| Table                | Description |
|----------------------|-------------|
| **Person**           | Contains basic demographic information describing a participant, including biological sex, birth date, race, and ethnicity. |
| **Visit_occurrence** | Captures encounters with healthcare providers or similar events. Contains the type of visit a person has (outpatient care, inpatient care, or long-term care), as well as the date and duration information. Rows in other tables can reference this table, for example, condition_occurrences related to a specific visit. |
| **Condition_occurrence** | Indicates the presence of a disease or medical condition stated as a diagnosis, a sign, or symptom, which is either observed by a provider or reported by the patient. |
| **Drug_exposure**    | Captures records about the utilization of a medication. Drug exposures include prescription and over-the-counter medicines, vaccines, and large-molecule biologic therapies. Radiological devices ingested or applied locally do not count as drugs. Drug exposure is inferred from clinical events associated with orders, prescriptions written, pharmacy dispensing, procedural administrations, and other patient-reported information. |
| **Measurement**      | Contains both orders and results of a systematic and standardized examination or testing of a participant or participant's sample, including laboratory tests, vital signs, quantitative findings from pathology reports, etc. |
| **Procedure_occurrence** | Contains records of activities or processes ordered by or carried out by a healthcare provider on the patient to have a diagnostic or therapeutic purpose. |
| **Observation**      | Captures clinical facts about a person obtained in the context of an examination, questioning, or a procedure. Any data that cannot be represented by another domain, such as social and lifestyle facts, medical history, and family history, are recorded here. |
| **Device_exposure**  | Captures information about a person's exposure to a foreign physical object or instrument which is used for diagnostic or therapeutic purposes. Devices include implantable objects, blood transfusions, medical equipment and supplies, other instruments used in medical procedures, and material used in clinical care. |
| **Death**            | Contains the clinical events surrounding how and when a participant dies. |



---

## ✅ OMOP Data Quality

- [The Book of OHDSI — Chapter 15: Data Quality](https://ohdsi.github.io/TheBookOfOhdsi/DataQuality.html)  
- [Kahn et al. (2016): A Harmonized Data Quality Assessment Terminology and Framework](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5051581/)

---

## 🔧 ETL Basics
- [📄 PDF: OMOP Common Data Model — Extract, Transform, Load](https://www.ohdsi.org/wp-content/uploads/2019/09/OMOP-Common-Data-Model-Extract-Transform-Load.pdf)  
- [📘 Book: The Book of OHDSI — Extract, Transform, Load](https://ohdsi.github.io/TheBookOfOhdsi/ExtractTransformLoad.html)


---

### 🛠️ ETL Steps

1. **Dataset profiling and documentation**
   - Create data model documentation, sample data, data dictionaries, code lists, and other relevant information (23-Aug)
   - Execute database profiling scan (WhiteRabbit) on source database
   - Prepare mapping approach/documents based on scan reports from database profiling scan

2. **Generation of the ETL Design**
   - Mapping workshop with all relevant parties to:
     1. Understand the source
     2. Define the scope of source data to be transformed
     3. Define acceptance criteria for OMOP output  
     **Output:** draft mapping document
   - Finalize mapping document:
     - Integrate all notes/documentation from workshop
     - Work through mappings and verify, update, fill in gaps
     - Meetings/emails with data contact/technical contact (TC) as needed

3. **Source Data Integrations and Semantic Mapping**
   - Source Code mapping:
     - Identify which codes are already mapped to standard vocabulary
     - Identify code types for codes that need to be mapped
     - Translation of code description/phrases to English, if/as needed
     - Create proposed code mappings
   - Generate mappings for data coming out of flowsheets (together with consortium)
   - Review/approval of code mappings (often by medical experts with the Data Owner)
   - Identify imaging & waveform data; map using consortium-defined guidelines
   - Use OHNLP to extract OMOP data from unstructured sources

4. **Technical architecture design**
   - CI/CD strategy & version control
   - OHDSI ecosystem needs & infrastructure design

5. **Technical ETL Development**
   - Implement ETL (preferred language/structure)
   - Update ETL based on testing/QA/feedback (8, 9)

6. **Setting up Infrastructure**
   - Deploy core servers and services based on (4)

7. **Install OHDSI tools**
   - Database server, Achilles/DQD/Ares, Atlas/WebAPI, RStudio Server, HADES, notebooks & other site-specific tools

8. **ETL Testing and Validation**
   - Test ETL on sample/dev data, then DO data
   - Verify & document QA
   - Submit Achilles/DQD/AresIndexer results regularly
   - Plan & manage ETL development

9. **Data Quality Assessment**
   - QA/Acceptance testing for mapping accuracy & completeness
   - Review & approval by Data Owner

10. **Documentation**
    - Mapping Documentation, Themis checks, and technical/transform documentation

11. **Project Management Throughout**
    - Organize tasks, milestones, and follow-up

---

## 🧪 OHDSI Analysis Tools

R, SQL, Python, or any preferred data analysis software.  
**Reference:** [The Book of OHDSI — Chapter 9: SQL and R](https://ohdsi.github.io/TheBookOfOhdsi/SqlAndR.html)


---

## 📘 Data Science Handbook

[Open, rigorous and reproducible research: A practitioner’s handbook](https://datascience.stanford.edu/programs/stanford-data-science-scholars-program/data-science-handbook) — Stanford Data Science



---

## 🧰 Data Management Tools & Resources

- DMP Tool:  https://dmptool.org/  
- NIH DMS Policy Planning: https://sharing.nih.gov/data-management-and-sharing-policy/planning-and-budgeting-for-data-management-and-sharing/writing-a-data-management-and-sharing-plan#after

---

## 💻 Programming Resources (Jupyter, Python, SQL, R)

- [Project Jupyter](https://jupyter.org/)
- [What is the Jupyter Notebook?](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)
- [NIAID NIH Informatics resources](https://bioinformatics.niaid.nih.gov/resources)

**Software Carpentry (free lessons):**
- [Programming with Python](http://swcarpentry.github.io/python-novice-inflammation/)
- [Programming with R](http://swcarpentry.github.io/r-novice-inflammation/)
- [Databases and SQL](http://swcarpentry.github.io/sql-novice-survey/)

**Additional resources:**
- [DataCamp](http://www.datacamp.com/)
- [Khan Academy — SQL Basics](https://www.khanacademy.org/computing/computer-programming/sql/sql-basics/v/welcome-to-sql)
- [Codecademy — Learn Python 2](https://www.codecademy.com/learn/learn-python)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [R for Data Science](https://r4ds.had.co.nz/)
- NIH “All of Us” documentation:  
  [Jupyter & programming](https://support.researchallofus.org/hc/en-us/articles/360039690191-Jupyter-Notebooks-and-programming)



---

## 🌐 OHDSI Resources

- [OHDSI Forums](https://forums.ohdsi.org/) — *Introduce yourself on the “Welcome to OHDSI” thread!*  
- [The Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/)  
- [OMOP CDM FAQ](https://ohdsi.github.io/CommonDataModel/faq.html)  
- [OHDSI Microsoft Teams](https://forms.office.com/Pages/ResponsePage.aspx?id=lAAPoyCRq0q6TOVQkCOy1ZyG6Ud_r2tKuS0HcGnqiQZUQ05MOU9BSzEwOThZVjNQVVFGTDNZRENONiQlQCN0PWcu)  
- [MIMIC-IV demo OMOP dataset](https://physionet.org/content/mimic-iv-demo-omop/0.9/1_omop_data_csv/)  
- [EHDEN Academy](https://academy.ehden.eu/)  
- [Atlas Demo](https://atlas-demo.ohdsi.org/) and [Athena](https://athena.ohdsi.org/search-terms/start)  
- [OHDSI YouTube: tutorials & workshops](https://youtube.com/playlist?list=PLpzbqK7kvfeXRQktX0PV-cRpb3EFA2e7Z)  
- [OHDSI Community Dashboard](https://dash.ohdsi.org/)  
- [OMOP Common Data Model (docs)](https://ohdsi.github.io/CommonDataModel/index.html)  
- [Learn GitHub](https://docs.github.com/en/get-started/quickstart/hello-world)  
- [Community Calls](https://ohdsi.org/community-calls/) and [Workgroups](https://ohdsi.org/upcoming-working-group-calls/)  
- Follow OHDSI: [Twitter](https://twitter.com/OHDSI) • [LinkedIn](https://www.linkedin.com/company/ohdsi)  
- [Subscribe to the OHDSI Newsletter](https://ohdsi.org/subscribe-to-our-newsletter/)  
- [OHDSI software](https://ohdsi.org/software-tools/)  
- [NIH All of Us — OMOP documentation](https://support.researchallofus.org/hc/en-us/articles/360039585391-How-the-Observational-Medical-Outcomes-Partnership-OMOP-vocabulary-are-structured)



---

## ⭐ Special Topic: Clinical Registries Using OHDSI

[![OHDSI and Clinical Registries: Sanity for Health Systems (Aug. 22 Community Call)](http://img.youtube.com/vi/DPatSxFkIpI/0.jpg)](https://youtu.be/DPatSxFkIpI?si=VOqE4VTlzIcxuWdP)

- Slides: [Clinical Registries in OHDSI — September 2022 (PDF)](https://www.ohdsi.org/wp-content/uploads/2022/09/OHDSI-Clinical_Registries.pdf)



## 💻 OMOP Code Snippets

We provide a publicly available set of OMOP code snippets used in the [I-LEARN Course](https://ilearn.tuftsctsi.org/product?catalog=D1RS_2025_18) to help learners explore and analyze OMOP Common Data Model datasets using tools like **R**, **SQL**, and **Python**.

🔗 **Repository**: [BoyceLab/OMOP-Code-Snippets-for-I-LEARN-Course](https://github.com/BoyceLab/OMOP-Code-Snippets-for-I-LEARN-Course)

### 🧰 What You'll Find in this Repository
The repository contains example scripts and templates to:

- Query OMOP data using **SQL**
- Analyze OMOP-mapped data using **R**
- Connect and run queries via **RPostgreSQL**
- Explore how standard concepts relate to source codes

### 📂 Folder Highlights

- SQL/: Ready-to-use SQL queries for common OMOP domains (e.g., drug exposure, observation).
- R/: R scripts that demonstrate how to load, analyze, and visualize OMOP data.
- concepts/: Examples for working with concept_id and concept_relationship tables.

### 📘 Use Cases

These snippets are designed for:
- Learners in the **Tufts CTSI I-LEARN course**
- Researchers new to **OHDSI/OMOP**
- Analysts working with **OMOP-formatted ALS datasets**

---
