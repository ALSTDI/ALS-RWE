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
-<h2>🧩 Domain Mappings</h2>

<ul>
  <li>
    <strong>🧍 Person</strong>
    (<a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#PERSON">Person Domain</a>)
    <ul>
      <li>Year of birth</li>
      <li>Sex</li>
      <li>Race</li>
      <li>Ethnicity</li>
      <li>IDs sequentialized; prefixes <code>CASE_</code>, <code>CONTROL_</code>, <code>ASYMP_</code> retained</li>
      <li>Unknown/multiple race/ethnicity/sex → <code>concept_id = 0</code></li>
    </ul>
  </li>

  <li>
    <strong>📝 Observation</strong>
    (<a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#OBSERVATION">Observation Domain</a>)
    <ul>
      <li>Validated, self-reported ALSFRS-R (mapped using custom concepts; more details in the custom concepts section of this page)
        <ul>
          <li>Speech</li>
          <li>Salivation</li>
          <li>Swallowing</li>
          <li>Handwriting</li>
          <li>Cutting Food</li>
          <li>Dressing Hygiene</li>
          <li>Turning in Bed</li>
          <li>Walking</li>
          <li>Climbing Stairs</li>
          <li>Dyspnea</li>
          <li>Orthopnea</li>
          <li>Respiratory Insufficiency</li>
          <li>Total Score</li>
        </ul>
      </li>
      <li>Self-reported ALS diagnosis (mapped using custom concepts; more details in the custom concepts section of this page)</li>
      <li>El Escorial Criteria (revised) categories
        <ul>
          <li>Definitive</li>
          <li>Possible</li>
          <li>Probable – Lab Supported</li>
          <li>Suspected</li>
        </ul>
      </li>
      <li>Medical history
        <ul>
          <li>Family medical history</li>
          <li>Personal medical history</li>
          <li>History of head injury</li>
          <li>ALS symptom onset</li>
          <li>Anatomical site of symptom onset</li>
          <li>Lifestyle: tobacco use</li>
          <li>Occupation/industry</li>
          <li>Military service</li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    <strong>🧪 Measurement</strong>
    (<a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#MEASUREMENT">Measurement Domain</a>)
    <ul>
      <li>Laboratory measurements: lab-provided measurements from blood draws, including
        <ul>
          <li>A/G Ratio</li>
          <li>Albumin (g/dL)</li>
          <li>Alkaline Phosphatase (U/L)</li>
          <li>Basophils (%)</li>
          <li>Basophils Abs (10^3/mm3)</li>
          <li>Bilirubin Total (mg/dL)</li>
          <li>BUN (mg/dL)</li>
          <li>BUN/Creatinine Ratio</li>
          <li>Calcium (mg/dL)</li>
          <li>Chloride (MM01/L)</li>
          <li>CO2 (MM01/L)</li>
          <li>Creatinine (mg/dL)</li>
          <li>EGFR (mL/min/1.3 sq m)</li>
          <li>Eosinophils (%)</li>
          <li>Eosinophils Abs (10^3/mm3)</li>
          <li>Globulin (g/dL)</li>
          <li>Glucose (mg/dL)</li>
          <li>Hematocrit (%)</li>
          <li>Hemoglobin (%)</li>
          <li>Lymphocytes (%)</li>
          <li>Lymphocytes Abs (10^3/mm3)</li>
          <li>MCH (PB)</li>
          <li>Monocytes (%)</li>
          <li>Monocytes Abs (10^3/mm3)</li>
          <li>Neutrophils (%)</li>
          <li>Neutrophils Abs (10^3/mm3)</li>
          <li>Platelet Count (10^3/mm3)</li>
          <li>Potassium (MM01/L)</li>
          <li>RDW (%)</li>
          <li>Red Blood Cell Count (10^6/mm3)</li>
          <li>SGOT (AST) (U/L)</li>
          <li>SGPT (ALT) (U/L)</li>
          <li>Sodium (MM01/L)</li>
          <li>Total Protein (g/dL)</li>
          <li>White Blood Cell Count (10^3/mm3)</li>
        </ul>
      </li>
      <li>Self-reported ALS-linked genetic mutations
        <ul>
          <li>PFN1</li>
          <li>SOD1</li>
          <li>SPG11</li>
          <li>FUS</li>
          <li>TARDBP</li>
          <li>C90RF72</li>
          <li>VCP</li>
          <li>NEK1</li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    <strong>💊 Drug Exposure</strong>
    (<a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#DRUG_EXPOSURE">Drug Exposure Domain</a>)
    <ul>
      <li>Self-reported medications and supplements</li>
      <li>Ingredient-level mapping (≥20 frequency mapped, others = 0)</li>
      <li>Dosage not calculated; source values retained</li>
      <li>Missing start date → dummy <code>1900-01-01</code></li>
      <li>Missing end date → start date reused</li>
    </ul>
  </li>

  <li>
    <strong>⚰️ Mortality</strong>
    (<a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#DEATH">Death Domain</a>)
    <ul>
      <li>Date of death (month/day set to <code>12-31</code> for privacy)</li>
    </ul>
  </li>
</ul>

<h2>🗓️ Dates and Timing</h2>

<ul>
  <li>Dates may be shifted for de-identification (<a href="https://doi.org/10.1093/jamia/ocw001">Hripcsak et al., JAMIA 2016</a>).</li>
  <li>If missing:
    <ul>
      <li>Survey date</li>
      <li>Dummy <code>1900-01-01</code></li>
      <li>Approximate date applied</li>
    </ul>
  </li>
  <li>Observation period:
    <ul>
      <li>Start = first survey date</li>
      <li>End = last event or death date</li>
    </ul>
  </li>
</ul>

<h2>❓ Missing Data</h2>

<ul>
  <li>Not collected → excluded unless required by OMOP CDM.</li>
  <li>Not all participants have complete data.</li>
  <li>Controls and asymptomatic carriers often have fewer entries.</li>
</ul>
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



