---
title: The STARDUSTT Framework -- Addressing the Curse of Knowledge in OMOP Implementation
hide:
  - title
---

## 🎥 Presentation

Watch Dr. Danielle Boyce present **STARDUSTT-ALS** — a new approach to capturing, managing, and analyzing “big data” in ALS natural history studies.  
[![Presentation](https://img.youtube.com/vi/9h89iHEiIPs/0.jpg)](https://youtu.be/9h89iHEiIPs?feature=shared)

---

## 📄 White Paper

**The STARDUSTT Framework: Addressing the Curse of Knowledge in OMOP Implementation**

**Authors:** Danielle Boyce<sup>1,2,3</sup>, Pavel Goriacko<sup>4</sup>, William M Garneau<sup>2</sup>, Pamela Dasher<sup>5</sup>, William Roddy<sup>5</sup>, Wesley Anderson<sup>5</sup>, Smith F. Heavner<sup>5,6</sup>  

**Corresponding Author:** [Danielle Boyce](mailto:dboyce3@als.net)  

**Affiliations:**  
1. ALS Therapy Development Institute  
2. Johns Hopkins University School of Medicine  
3. Tufts University School of Medicine  
4. Montefiore Einstein, Center for Health Data Innovations  
5. Critical Path Institute  
6. Clemson University, Department of Public Health Sciences  
---

### Executive Summary

Adopting the Observational Medical Outcomes Partnership (OMOP) Common Data Model (CDM) requires collaboration across diverse stakeholders—executives, clinical informaticists, and technical teams—each with different expertise. Too often, the **curse of knowledge** impedes effective communication, slowing progress.

The **STARDUSTT Framework**—**S**ecure Data, **T**echnology Awareness, **A**ctive Clinical Representation, **R**elational Databases, **D**ata Quality, **U**tilization of Git, **S**tandardized Vocabularies, **T**raining & Documentation, **T**ranslation & Communication—offers a structured approach to build readiness and overcome these barriers.

---

### Background

Large-scale OMOP CDM projects such as the National COVID Cohort Collaborative (N3C), All of Us, and EHDEN have created unprecedented opportunities for observational research. Yet, many sites face challenges due to:
- Limited technical readiness
- Gaps in shared understanding
- Lack of role-specific training

One important contributor to these challenges is the **curse of knowledge**—a cognitive bias first described by Camerer, Loewenstein, and Weber (1989) in *The Curse of Knowledge in Economic Settings: An Experimental Analysis*. This bias occurs when individuals with expertise find it difficult to imagine what it is like for others not to possess that knowledge, often leading to overestimations of others’ understanding and ineffective communication.

In OMOP projects, this bias can manifest when experienced informaticists, engineers, or OHDSI community members assume that all team members are familiar with prerequisites such as relational databases, GitHub workflows, or the OHDSI tool stack. Without intentional, role-specific onboarding, new participants can become overwhelmed and disengaged.

Our work on the **CURE ID** project provided direct, practical experience with these challenges and informed the development of the **STARDUSTT Framework** as a structured approach to address them.


### The STARDUSTT Framework

![STARDUSTT Framework](assets/STARDUSTT.png)  
*Figure 1: Overview of the STARDUSTT Framework*

#### STARDUSTT Components
1. **Secure Data** — De-identification, privacy protection, and regulatory compliance.
2. **Technology Awareness** — Familiarity with Docker, SQL, and OHDSI tools.
3. **Active Clinical Representation** — Inclusion of clinicians in decision-making and workflow mapping.
4. **Relational Databases** — Understanding schema, joins, and OMOP table relationships.
5. **Data Quality** — Processes for completeness, accuracy, and plausibility.
6. **Utilization of Git** — Version control, collaboration, and issue tracking.
7. **Standardized Vocabularies** — SNOMED, LOINC, RxNorm, and use of Athena for mapping.
8. **Training & Documentation** — SOPs, MOPs, and curated learning paths.
9. **Translation & Communication** — Plain-language messaging, feedback loops, and artifacts for different personas.

---

### Implementation Insights

The framework emerged from interviews with both successful and hesitant OMOP adopters. Three key findings shaped its design:

- **Tailor training by role**: Executives, clinicians, and engineers have different needs.
- **Focus on prerequisites**: Don’t assume baseline skills in databases, GitHub, or coding.
- **Use shared language**: Maintain glossaries and avoid unnecessary jargon.

---

### Common Problems and Strategies

| Problem | Impact | Strategy |
|---|---|---|
| Varying expertise levels | Poor decision-making | Start with foundational training |
| Overwhelming resources | Loss of engagement | Curated, role-specific materials |
| Technical jargon | Miscommunication | Accessible language + shared glossary |
| Complex topics too soon | Frustration | Incremental learning |
| Passive learning | Low retention | Active exercises and case studies |
| Infrequent feedback | Persistent gaps | Regular check-ins |
| One-size-fits-all | Uneven outcomes | Diverse teaching methods |
| Poor documentation | Limited autonomy | Clear, versioned resources |
| Isolated learning | Slow problem-solving | Mentorship and peer learning |
| Theory without practice | Weak skill transfer | Real-world application |
| Static programs | Outdated skills | Continuous updates |

---

### Applying STARDUSTT to Personas

| Component | C-Suite Executives | Clinical Informaticists | Data Engineers |
|---|---|---|---|
| **Secure Data** | Compliance and strategic value | IRB/PHI safeguards | Advanced security techniques |
| **Technology Awareness** | ROI of tools | OHDSI tools in clinical workflows | Deep technical training |
| **Active Clinical Representation** | Sponsor collaboration | Bridge to technical teams | Integrate clinical context |
| **Relational Databases** | Decision-making role | Basic querying | Dialect-specific scripting |
| **Data Quality** | Impact on trust | Use of DQD/Achilles | Automated DQ pipelines |
| **Utilization of Git** | Governance | Simplified workflows | Advanced branching & CI |
| **Standardized Vocabularies** | Interoperability strategy | Vocabulary use in practice | Mapping & Athena mastery |
| **Training & Documentation** | Executive dashboards | Guides & glossaries | Tutorials & peer reviews |
| **Translation & Communication** | Strategic framing | Clinical translation | Technical action from requirements |

---

### Personas in Practice

**C-Suite Executives** need strategic summaries, compliance implications, and ROI metrics.  
**Clinical Informaticists** benefit from practical workflow examples and clear connections to patient care.  
**Data Engineers** require technical depth and context to align builds with project goals.

---

### Conclusion

The STARDUSTT Framework bridges gaps in knowledge, builds shared understanding, and accelerates OMOP adoption. By addressing role-specific needs and the curse of knowledge, it improves efficiency, reduces frustration, and increases sustainability in data harmonization projects.

---

### Acknowledgements

We thank **Irina Titkova, PhD** (Show-cell.com, Barts Cancer Institute, Queen Mary University of London) for graphic design and **Grace Zaikoski** for editorial support.

---

### References

1. Heavner SF, Anderson W, Kashyap R, Dasher P, Mathé EA, Merson L, Guerin PJ, Weaver J, Robinson M, Schito M, Kumar VK, Nagy P. A Path to Real-World Evidence in Critical Care Using Open-Source Data Harmonization Tools. *Crit Care Explor.* 2023;5(4):e0893. doi:10.1097/CCE.0000000000000893.  
2. Camerer C, Loewenstein G, Weber M. The curse of knowledge in economic settings: An experimental analysis. *J Polit Econ.* 1989;97(5):1232–1254.  
3. Hripcsak G, Mirhaji P, Low AF, Malin BA. Preserving temporal relations in clinical data while maintaining privacy. *J Am Med Inform Assoc.* 2016;23(6):1040–1045. doi:10.1093/jamia/ocw001.  
4. Kahn MG, Callahan TJ, Barnard J, et al. A Harmonized Data Quality Assessment Terminology and Framework for the Secondary Use of Electronic Health Record Data. *EGEMS.* 2016;4(1):1244.  
5. Observational Health Data Sciences and Informatics (OHDSI). *The Book of OHDSI.* 2023. https://ohdsi.github.io/TheBookOfOhdsi/
