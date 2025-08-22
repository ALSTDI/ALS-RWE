---
title: ALS TDI OMOP Data Set
hide:
  - title
---

# 📦 Release Notes: Version 0.1.0

The first release of the [ALS TDI ARC Study](https://www.als.net/arc/), mapped to the [Observational Medical Outcomes Partnership Common Data Model (OMOP CDM)](https://ohdsi.github.io/CommonDataModel/), restructures a subset of the ARC Natural History Study into the OMOP CDM structure and maps a subset to standardized vocabularies.  

This is part of a larger harmonization effort with [Answer ALS](https://www.answerals.org/) and the [Critical Path Institute](https://c-path.org/program/critical-path-for-rare-neurodegenerative-diseases/).

> **Note about EHR data:** We are actively working to include electronic health record (EHR) data in future releases. Tools in use for EHR integration:  
> - [**CDAtransformer**](https://github.com/BoyceLab/CDAtransformer) — Parse C-CDA and FHIR files into structured tables.  
> - [**RWDExchange**](https://github.com/BoyceLab/RWDExchange) — Evaluate exchangeability of real-world data (EHR, registries) for external comparator trials.  

---

### 📁 Complete Data Set and Documentation  
**[Neuromine Data Portal](https://data.answerals.org/home)**  

---

### 🧮 CDM Version  
- **OMOP CDM v5.4** – [Documentation](https://ohdsi.github.io/CommonDataModel/cdm54.html)  

---

### 👥 Participant Summary  
- **Total participants**: 1,665  
  - People with ALS  
  - Asymptomatic carriers  
  - Healthy controls  

> Participant type available in **Person** table (`participant_source`).  
> *Note: not all participants answered all surveys.*  

This version includes:  
- Self-reported surveys  
- ALSFRS-R data  
- Laboratory results from blood samples  

---

### 📚 Citation
> **ALS Therapy Development Institute (ALS TDI). (2023).** *ALS Research Collaborative (ARC) [Data set].* ALS Therapy Development Institute. https://doi.org/10.71944/C3NA-9124  

---

## 🧩 Domain Mappings

- **🧍 Person** ([Person Domain](https://ohdsi.github.io/CommonDataModel/cdm54.html#PERSON))  
  - Year of birth, sex, race, ethnicity  
  - IDs sequentialized; prefixes `CASE_`, `CONTROL_`, `ASYMP_` retained  
  - Unknown/multiple race/ethnicity/sex → `concept_id = 0`  

- **📝 Observation** ([Observation Domain](https://ohdsi.github.io/CommonDataModel/cdm54.html#OBSERVATION))  
  - ALSFRS-R (12 functional items + total score)  
  - Family & personal medical history  
  - History of head/neck injuries  
  - Symptom onset & anatomical site  
  - Lifestyle: tobacco use  
  - Occupation/industry, military service  
  - El Escorial Criteria (custom concept mapping)  

- **🧪 Measurement** ([Measurement Domain](https://ohdsi.github.io/CommonDataModel/cdm54.html#MEASUREMENT))  
  - Laboratory results from blood draws:  
    - A/G Ratio, Albumin, Alkaline Phosphatase, Basophils (%/Abs), Bilirubin Total, BUN, Creatinine, Calcium, Chloride, CO2, EGFR, Eosinophils (%/Abs), Globulin, Glucose, Hematocrit, Hemoglobin, Lymphocytes (%/Abs), MCH, Monocytes (%/Abs), Neutrophils (%/Abs), Platelets, Potassium, RDW, RBC Count, SGOT, SGPT, Sodium, Total Protein, WBC Count  
  - Self-reported ALS-linked genetic mutations:  
    PFN1, SOD1, SPG11, FUS, TARDBP, C90RF72, VCP, NEK1  

- **💊 Drug Exposure** ([Drug Exposure Domain](https://ohdsi.github.io/CommonDataModel/cdm54.html#DRUG_EXPOSURE))  
  - Self-reported medications & supplements  
  - Ingredient-level mapping (≥20 frequency mapped, others = 0)  
  - Dosage not calculated; source values retained  
  - Missing start date → dummy `1900-01-01`  
  - Missing end date → start date reused  

- **⚰️ Mortality** ([Death Domain](https://ohdsi.github.io/CommonDataModel/cdm54.html#DEATH))  
  - Date of death (month/day set to `12-31` for privacy)  

---

## 🗓️ Dates and Timing

- Dates may be shifted for de-identification ([Hripcsak et al., JAMIA 2016](https://doi.org/10.1093/jamia/ocw001)).  
- If missing:  
  - Survey date, dummy `1900-01-01`, or approximate date applied.  
- Observation period:  
  - Start = first survey date  
  - End = last event or death date  

---

## ❓ Missing Data

- Not collected → excluded unless required by OMOP CDM.  
- Not all participants have complete data.  
- Controls and asymptomatic carriers often have fewer entries.  

---

## 🛠️ Custom Concepts

Some ALS-specific variables lacked standardized OMOP vocabularies; custom/local concepts (>2,000,000,000) were created.  

- **Anatomical site of symptom onset** → `2000000396`  
- **El Escorial Criteria** → `2000000061`  

### El Escorial Harmonization  
- Harmonized with Answer ALS & C-Path.  
- Self-reported, validated by ALS TDI staff.  

| El Escorial Status              | Custom Concept ID |
|---------------------------------|------------------:|
| Suspected                       | 2000000062        |
| Possible                        | 2000000058        |
| Probable Laboratory Supported   | 2000000060        |
| Probable                        | 2000000059        |
| Definite                        | 2000000057        |

---

## 📊 CDM Summary Counts 

| Domain             | Person IDs | Records | Primary Concept Field          | # Unique Concepts |
|--------------------|:----------:|:-------:|--------------------------------|:-----------------:|
| person             | 1,665      | 1,665   | N/A                            | N/A               |
| death              | 586        | 586     | N/A                            | N/A               |
| observation_period | 1,665      | 1,665   | N/A                            | N/A               |
| visit_occurrence   | 1,665      | 32,340  | visit_occurrence_concept_id    | 0                 |
| condition_occurrence| 1,410     | 1,410   | condition_concept_id           | 1                 |
| measurement        | 383        | 39,271  | measurement_concept_id         | 42                |
| observation        | 1,595      | 340,371 | observation_concept_id         | 34                |
| drug_exposure      | 872        | 4,881   | drug_exposure_concept_id       | 115               |

*(Other OMOP domains not populated in this release)*  

---

## 🧭 Guidance for Data Use

- 🔍 Review `*_source_value` and `*_source_concept_id` columns to trace original survey responses.  
- 🧠 Explore concept definitions with [OHDSI Athena](https://athena.ohdsi.org/).  

---

## 📋 Surveys Included

The dataset integrates the following surveys:  
- Enrollment  
- General Information  
- Family History  
- Geography  
- Lifestyle  
- Occupation  
- Medical History – Hospitalization  
- Medical History – Injuries  
- Medical History – Clinical Trials  
- Medical History – Conditions  
- Your ALS Experience  
- Medications  
- Supplements  

---

# 📄 Survey Questionnaires

Summaries of survey forms (*not all mapped to OMOP in this release*).  

### Enrollment  
- DOB, phone, address, gender, ethnicity, race  
- Marital status, education  
- Height/weight (current, at age 40)  

### ALS Diagnostic Status  
- Possible, Lab-Supported Probable, Probable, Definite, Asymptomatic Carrier, PLS  

### Timeline  
- First symptom date & site  
- First neurology visit  
- First possible diagnosis  
- Formal diagnosis  

### Physician Information  
- Primary care physician, neurologist  

### Health & Function  
- Devices: tracheostomy, feeding tube, CPAP, DPS  
- Comorbidities, family ALS, genetic testing, medications, trial participation, bleeding disorders  
- Functional ability: stairs, arm raise, wheelchair use  

### Emergency Contact  
- Name, relation, phone, email  

### Family History  
- Relatives, conditions (ALS, Alzheimer’s, MS, autoimmune, etc.)  

### Geography  
- Birthplace, long-term residences, farm/ranch history  

### Lifestyle  
- Smoking history  
- Physical activity history  

### Occupation  
- Employment history, industry, job titles  
- Military service, deployments  

### Your ALS Experience  
- Diagnosis details, age at diagnosis  
- Health events since onset (pneumonia, falls, clots)  
- Symptom progression (cramps, twitching, swallowing, speech, bowel/bladder)  

### Medical History – Hospitalization  
- ER visits/hospital stays past 3 months  

### Medical History – Injuries  
- Head/neck injuries by cause  
- Age, severity, associated conditions  

### Medical History – Conditions  
- Physician-diagnosed: ALS, Alzheimer’s, asthma, Crohn’s, fibromyalgia, dystrophy, neuropathy, psoriasis, rheumatoid arthritis, lupus, thyroid disease, TIA, ulcerative colitis, etc.  

### Clinical Trials  
- Trial name, start/end, Gov ID, sponsor, phase, type, treatment, enrollment size  

### Medications  
- Drug name, dosage, start/end dates, frequency  

### Supplements  
- Product name, brand, start/end dates, frequency, serving size  

---

👉 For full OMOP domain details, see the [OMOP CDM v5.4 Reference Guide](https://ohdsi.github.io/CommonDataModel/cdm54.html).



