---
title: ALS TDI OMOP Data Set
hide:
  - title
---

# 📦 Release Notes: Version 0.1.0

The first release of the [ALS TDI ARC Study](https://www.als.net/arc/), mapped to the [Observational Medical Outcomes Partnership Common Data Model (OMOP CDM)](https://ohdsi.github.io/CommonDataModel/), restructures a subset of the ARC Natural HIstory Study into the OMOP CDM structure and maps a subset to standardized vocabularies.

This is part of a larger harmonization effort with [Answer ALS](https://www.answerals.org/) and the [Critical Path Institute](https://c-path.org/program/critical-path-for-rare-neurodegenerative-diseases/).

> **Note about EHR data:** We are actively working to include electronic health record (EHR) data in our next release.  Tools that we use for EHR data and related analytics include:
> - [**CDAtransformer**](https://github.com/BoyceLab/CDAtransformer) — This R Shiny application allows users to upload and parse C-CDA and FHIR text files. It extracts relevant elements and presents them in a tabular format for easy viewing and download.  
> - [**RWDExchange**](https://github.com/BoyceLab/RWDExchange) — RWDExchange is an R Shiny application designed to evaluate the exchangeability potential of your real-world data (RWD) including electronic health records and patient registries for use as external comparators in clinical trials.

---

---

### 📁 Complete Data Set and Documentation Location  
**[Neuromine Data Portal](https://data.answerals.org/home)**

---

### 🧮 CDM Version  
- **OMOP CDM Version 5.4** – [View Documentation](https://ohdsi.github.io/CommonDataModel/cdm54.html)


### 👥 Participant Summary  
- **Total number of participants**: 1,676  
  > *Note: not all participants answered all surveys*

The dataset contains data from the following participant types:
- People with ALS
- Asymptomatic carriers
- Healthy controls  

> Participant type can be found in the **Person** table, under the participant_source column.

This version of the ALS TDI dataset includes:
- Self-reported surveys and ALSFRS-R (ALS Functional Rating Scale – Revised) data
- Laboratory results from analyzed blood samples

---

### 📚 Citation

> **ALS Therapy Development Institute (ALS TDI). (2023).**  *ALS Research Collaborative (ARC) [Data set].*  Amyotrophic Lateral Sclerosis Therapy Development Institute.   https://doi.org/10.71944/C3NA-9124

---

## 🧩 Mappings

- **🧍 Person**:  
  Demographics including year of birth, sex, race, and ethnicity.  
  See accepted concepts [here](https://ohdsi.github.io/CommonDataModel/cdm54.html).

- **🗒️ Observation**:  
  - ALSFRS-R (individual items and total score)  
  - Family and personal medical history  
  - Site of onset  
  - Injury history  
  - Military service  
  - Tobacco use

- **💊 Drug Exposure**:  
  Medications and select supplements

- **⚰️ Mortality**:  
  Date of death

- **🧪 Measurement**:  
  - Laboratory data from blood draws  
  - Self-reported genetic mutations

- **📌 Other Variables**:  
  - Military service  
  - Industry of employment  
  - Injury history

---

## 📌 Notes on Mapping Decisions

### 🗓️ Dates and Timing

Dates may be shifted for deidentification purposes using the method described in:

> Hripcsak G, Mirhaji P, Low AF, Malin BA.  *Preserving temporal relations in clinical data while maintaining privacy.*  J Am Med Inform Assoc. 2016 Nov;23(6):1040-1045.  
> [Link to publication](https://doi.org/10.1093/jamia/ocw001)  

In the **Observation Period** OMOP domain:
- observation_period_start_date = first event date (usually first survey)  
- observation_period_end_date = last event date or date of death

---

### ❓ Missing Data

If a data point was not collected, it is excluded unless required by OMOP CDM.  
See the "Required" column in the [CDM v5.4 guidance](https://ohdsi.github.io/CommonDataModel/cdm54.html)

**Examples:**
- If **ethnicity** is unknown → concept_id = 0  
- If **race** is unknown or multiple → concept_id = 0

---

### 🛠️ Custom Concepts
> **What are custom concepts?**  
In the OMOP Common Data Model, most clinical information is standardized using concept IDs from shared vocabularies (like SNOMED, RxNorm, LOINC, etc.). However, sometimes source data includes important information that **doesn’t have an existing standardized concept** in these vocabularies.

In those cases, researchers define **custom (or local) concepts** with unique concept IDs (usually starting above 2,000,000,000). These custom concepts allow valuable variables — such as ALS symptom onset patterns, survey-specific fields, or patient-reported values — to be included in the dataset in a structured, queryable way.

In the ALS TDI OMOP data set, custom concepts were created for:
- **ALS symptom onset**
- **Anatomical site of symptom onset**
- Additional variables unique to the ARC study

> These custom concepts are stored and referenced just like standard concepts, allowing them to be queried and analyzed using the same OMOP framework.


---

### 💊 Medications

- Mapped to **ingredient level** wherever possible  
- **Dose not calculated**  
- **All source values retained**  
- If the drug or supplement was **unmapped**:
  - concept_id = 0
  - Source data included in the appropriate source column

---

## 🧭 Guidance for Using This Data Set

- 🔍 **Review the *_source_value or *_source_concept_id columns** in each OMOP table to understand how data were originally captured. These often contain verbatim responses or terms from the source survey.

- 🧠 **Explore concept definitions** and standardized codes using the [OHDSI Athena](https://athena.ohdsi.org/) tool. You can look up concept IDs used throughout the dataset and understand their relationships and domains.

## 📋 List of Surveys

The ALS TDI ARC dataset contains the following participant surveys:

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

Below are summaries of the survey forms. Click a section to expand the full question set.

## **Enrollment**

- Date of Birth*
- Primary Phone*
- Address* (Street, City, State, Country, Postal Code)
- Gender*: Male / Female / Other / Prefer not to say
- Ethnicity*: Caucasian/White, Hispanic, African American/Black, Asian, Native American, Middle Eastern, Other (specify)

## **ALS Diagnostic Status:**
- Possible*, Lab-Supported Probable*, Probable*, Definitive*, Asymptomatic Carrier, PLS  
  *Per El Escorial diagnostic criteria.*

## **Timeline:**
- First Symptom Date (Month/Year) and location (e.g., Left Hand, Right Foot, Swallowing, Breathing, etc.)
- First Neurology Visit Date (Month/Year)
- First Possible ALS Diagnosis Date (Month/Year)
- Formal ALS Diagnosis Date (Month/Year)

## **Physician Information:**
- Primary Care Physician*
- Neurologist*

## **Health & Function:**
- Active infections? Tracheostomy? Feeding tube? CPAP use? DPS device? Major comorbidities? Relatives with ALS? Genetic screening? ALS-related medications? Clinical trial participation? Bleeding disorders? Functional abilities (stairs, arm raise, wheelchair use)

## **Emergency Contact:**
- Name*, Relation*, Phone*, Email*

## **Free Text:**
- Open comments on health or survey items

## **Demographics:**
- Race/ethnic group (select all)
- Marital status
- Education level

## **Anthropometrics:**
- Current height and weight
- Height and weight at age 40 (if applicable)

## **Family History**

- Relation (parents, siblings, children, grandparents)
- Living status
- Physician-diagnosed conditions (ALS, Alzheimer’s, MS, autoimmune disorders, etc.)

## **Geography**

- Birth country/state/region, city*
- Residences (≥6 months), years moved in/out
- Ever lived on a farm/ranch?*

## **Lifestyle**

- Smoking history
- Vigorous physical activity by age range (frequency per week/month/year)

## **Occupation**

- Current employment, job title, industry
- Previous jobs/industries
- Military service, deployment history

## **Your ALS Experience**

- Diagnosis details and age at diagnosis
- Health events since ALS onset (pneumonia, falls, blood clots)
- Symptom timelines (muscle cramps, twitching, swallowing, speech, bowel/bladder control)


## **>Medical History – Hospitalization**

- ER visits and hospitalizations in past 3 months
- Number of visits/days

## **Medical History – Injuries**

- Head/neck injury history by cause (vehicle, falls, sports, assault, blast exposure, electrical shock)
- Age at first/worst injury, loss of consciousness, hospitalization, associated conditions (fracture, seizure, memory loss)

## **Medical History – Conditions**

- List of physician-diagnosed conditions (ALS, Alzheimer’s, MS, autoimmune diseases, thyroid disease, etc.)

## **Clinical Trials**

- Trial name, start/end dates, Gov ID, sponsor, phase, type, treatment type, enrollment size

## **Medications**

- Drug name, dosage form, dosage, start/end dates, frequency

## **Supplements**

- Product name, brand, start/end dates, frequency, net contents, serving size


