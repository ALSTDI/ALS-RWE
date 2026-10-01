# Train-the-Trainer audit and corrections

Prepared for Danielle Boyce on 1 October 2026, and revised the same day after her decisions on the open questions. This file records what was found to be inaccurate in `docs/free-rwe-resources/train-the-trainer/`, what was changed in this copy of the repository, and what still needs a decision or a check before the materials are taught again.

Acronyms used here: OMOP (Observational Medical Outcomes Partnership), CDM (Common Data Model), OHDSI (Observational Health Data Sciences and Informatics), DQD (Data Quality Dashboard), HADES (Health Analytics Data-to-Evidence Suite), ETL (extract, transform, load), ATC (Anatomical Therapeutic Chemical classification), EHR (electronic health record), SynPUF (the synthetic Medicare public use file behind the public ATLAS demo), AUC (area under the receiver operating characteristic curve), ALS (amyotrophic lateral sclerosis). ATLAS and Athena are tool names.

## Scope and method

Every slide deck, speaker note, quiz, Markdown page, notebook, and the Word tutorial in the train-the-trainer folder was read. Claims were compared with OHDSI documentation where a source could be opened (listed under Sources). Where no source was opened, the correction rests on general knowledge of the tools and is marked "not re-checked" below, so you can confirm it on your own ATLAS instance or in Athena.

The text corrections were made first, in place. The decks were then rebuilt in a plain format (see the decisions below). File names are unchanged, every deck passes the Office file validation, and a sample of slides from the rebuilt decks was rendered and checked; not every rebuilt slide was viewed. The notebooks were run end to end after editing, and the site was built with MkDocs from this copy without errors.

## The Kahn framework

The Day 2 materials named the Kahn framework as the first learning objective, gave it several quiz questions, and then used only a few of its parts. The description of the framework was also inconsistent from file to file.

| What was inaccurate | Where | Correction |
|:--|:--|:--|
| DQD described as something that "operationalizes" the framework, implying full coverage | Day 2 deck, module page, FAQ | DQD labels its check types with Kahn terms and fills part of the framework. No check type is labeled uniqueness plausibility, and the validation label is used for `isRequired`, `measurePersonCompleteness`, and the plausibleGender checks |
| "Diabetes prevalence matches published national estimates" presented as a DQD validation check | Day 2 deck, workbook, exercise table, quiz | Kept as an example of validation in Kahn's sense and stated plainly as work DQD does not do |
| The two contexts defined as "the data alone" versus "a specific study" | Day 2 module page | Verification compares data with expectations from the system itself; validation compares data with an external benchmark |
| Rows with `concept_id = 0` labeled as a conformance problem | Day 2 notebook | Moved to completeness, which is how DQD labels it (`standardConceptRecordCompleteness`). The conformance step now tests that concept IDs exist and belong to the Drug domain |
| Framework taught as the headline of the day | Day 2 objectives, agenda, takeaways, quiz | Reframed as the vocabulary for reading a DQD result, presented once and completely, followed by what DQD covers |

The Day 2 slide now shows the categories with their subcategories, the contexts, and the DQD check types that hold each label. The full explanation is in the speaker notes. The labels were read from the DQD check type documentation for version 2.6.3; confirm them for the version your site runs.

## Errors that recurred across files

| Topic | What the materials said | What is documented | Files corrected |
|:--|:--|:--|:--|
| ATLAS concept sets | A "Mapped tab" and a "Standard toggle" | The tabs are Included Concepts and Included Source Codes. Mapped is a checkbox in the expression, next to Exclude and Descendants (not re-checked online) | Day 2 deck, workbook, quiz, module, exercise; FAQ; personas; feasibility walkthrough |
| Standard concepts | Every concept in a set must be standard, while the lab uses "sulfonylureas", described as an ingredient | Sulfonylureas is an ATC class and a classification concept (`standard_concept = 'C'`), added with descendants. The values of `standard_concept` (standard, classification, non-standard) are now taught on Day 1 | Day 1 deck, quiz, module, exercise, snippets, notebook; Day 2 deck, module, exercise; FAQ |
| Concept ID versus code | "SNOMED 201826" | 201826 is the OMOP concept ID; the SNOMED code is 44054006 | Day 1 deck, exercise, snippets |
| Relationships | "Has ancestor" listed as a relationship ID | Hierarchy links are "Is a" and "Subsumes"; ancestors are stored in `concept_ancestor` | Syllabus, Day 1 exercise, snippets, cheat sheet |
| Vocabulary releases | Updated "monthly or bi-monthly" | Major releases come twice a year, in February and August | Day 1 deck, module, exercise |
| Standard vocabularies by domain | HCPCS, ICD-9 procedures, ICD-O-3, and SNOMED measurement concepts listed as source vocabularies; ATC listed as a source vocabulary | Standard status is set concept by concept; the table now lists the main standard vocabularies and treats ATC as classification (not re-checked online) | Day 1 deck, FAQ |
| Person and death | Death shown as part of the person table | Death is a separate table in CDM v5.3 and v5.4 | Day 1 deck |
| ATLAS counts | "Confirm the count matches" between ATLAS and SQL | The record counts ATLAS shows come from the last Achilles run and can lag the CDM | Day 2 deck, workbook, exercise, quiz |
| Cohort Pathways | "ATLAS → Characterizations → Treatment Pathways"; select ingredients; settings for time-at-risk, minimum exposure duration, observation window, allowed gap days; Sankey view; "arrow width" | Cohort Pathways is its own menu item; inputs are a target cohort and event cohorts; settings are combination window (labeled Collapse Days in some ATLAS versions), minimum cell count, maximum path length, allow repeats; output is a sunburst plot with a Tabular view, and the end of a pathway is shown in grey. Gaps are set in each event cohort's exit rule | Day 5 kit decks, quiz, module, exercise; syllabus; personas |
| Pathway answer keys | Metformin above 50 to 70 percent; insulin 10 to 30 percent; older patients escalate earlier | No source was given for these figures. The keys now ask learners to record what their data show. The one sourced statement kept is from Hripcsak et al. (2016) | Day 5 answer keys, handouts, interpretation guide, recording script |
| Prediction code | `getPlpData(connectionDetails, cdmDatabaseSchema, targetCohortId, outcomeCohortId)`, `runPlp(plpData)`, `plotPlpPerformance()` | The package uses `createDatabaseDetails()`, `getPlpData(databaseDetails, covariateSettings)`, `runPlp()` with outcome, population, and model settings, and `plotPlp()` | Day 6 workbook and demo script |
| Prediction answer keys | AUC of 0.6 to 0.8 "typical" | No source was given; the keys now ask for the observed value and a reason | Day 6 answer keys, handout, interpretation guide |
| HADES setup | R 4.2 as a minimum; Java 8 or 11 only, with Java 17 unsupported | The HADES setup guide targets R 4.4.1 (since June 2024), does not state the Java rule the materials gave, and requires a GitHub personal access token that the materials left out | Day 0 deck, quiz; Module 0; environment handout and checklist; Day 6 module and exercise; FAQ |
| Book of OHDSI chapters | ETL as chapter 3, data quality in chapter 4, pathways under chapter 12, HADES as chapter 14, community as chapter 15 | ETL is chapter 6, data quality chapter 15, pathways chapter 11, the analytics tools chapter 8, community chapter 1; cohorts are chapter 10 | Syllabus, personas, Day 2, 4, 5, and 6 modules |
| Program naming | "Six-week core" with Weeks 5 and 6 marked optional; Day 6 kit labeled "Week 2" | Sessions are now named Day 1 to Day 6 throughout, with Day 6 taught as Part 1 and Part 2 | Syllabus, mini lab, handout, resources, Day 6 kit |
| "SEARCH" | Called an OHDSI extraction tool and listed as an extraction path | SEARCH is the NYU version of ATLAS (confirmed by Danielle), so it was removed. The extraction paths are now ATLAS-exported SQL or a local pipeline | Day 0 deck, handout, and quiz; Module 0; Day 4 module and exercise; syllabus; personas; mini lab; checklists |
| OHDSI community figures | More than 3,000 researchers in 90+ countries; about 1 billion patients | 4,833 collaborators in 88 countries; 974 million unique patient records in 54 countries (OHDSI 2025 Year in Review, December 2025) | Day 1 deck |
| ALS concept ID | 4051114 in the cheat sheet and 35748069 in the notebooks | 373182, the ID your own ALS TDI OMOP data set page uses | Cheat sheet, all notebooks |
| Feasibility demo | Deck described a pregnancy entry event and a cohort of about zero; the importable cohort uses a first diabetes record with a female, age 15 to 44 rule. Pages disagreed on the number of checks, and the appendix mapped governance to DQD | Deck now describes the importable cohort and hedges the count; the checklist, the first page, and the appendix share one list of checks; governance is mapped to the steward and review board, with DQD described as a data quality tool | Feasibility deck, pages 01, 04, 06, 07, 08, index, kit README, quiz |

## Other changes by area

**Day 1.** The slide titled "OMOP CDM Design Principles" listed features that are not the design principles in the assigned reading, so it is retitled and the notes point to section 4.1 of the Book of OHDSI. The Athena lab step now says "Mapped from" for the source codes that map to a standard concept. Claims that the same definition gives "the same cohort" at any site were reworded to say the definition runs unchanged and each site gets its own cohort.

**Day 3.** "Exclusions are inclusion rules that must be false" is now "an inclusion rule requiring exactly 0 occurrences". The characterization step points to Characterizations in the left menu, since the cohort definition has no characterization tab. The claim that type 2 diabetes "should be" the most common prior condition is now a question to answer from the data. Exported cohort SQL is described as parameterized. The tutorial document had a leftover drafting note and a sentence that put ICD codes inside a concept set; both are fixed.

**Day 5 and Day 6 pages.** The Day 5 module and exercise no longer describe allowed gap days or a Sankey view inside ATLAS, and they name the TreatmentPatterns R package as the place those come from. The Day 6 pages called `getCohortDefinitionSet` from the wrong package, skipped cohort generation, pointed at the cohort table ATLAS writes to, and used a covariate column that does not exist; the blocks were rewritten, with a dedicated cohort table so the ATLAS table is not at risk. "Network meta-analysis" for EvidenceSynthesis is now "meta-analysis across data partners". Orphan concepts are redefined.

**SQL pages.** Hard-coded concept IDs that could not be confirmed (21600381 for sulfonylureas, 45548499 for an ICD-10-CM code) were replaced with lookups by vocabulary and code. The PostgreSQL date difference entry and the "cohort attrition" label in the cheat sheet were corrected.

**Quizzes.** All quizzes now share one column layout, and every question and answer was checked against Kahoot's length limits (120 characters for a question, 75 for an answer). Questions resting on the errors above were rewritten.

**Notebooks.** Besides the Kahn and concept ID fixes, the Day 6 notebook called fifths "deciles", and the Day 1 notebook said it created five tables while creating more. Each notebook now states that its other concept IDs are teaching placeholders.

**Formatting.** The Day 5 and Day 6 kit decks showed a typed hyphen after each bullet mark; the hyphens were removed. Speaker notes in the long Day 5 ATLAS deck contained drafting artifacts ("User-provided transcript ... supplied in chat"); these were removed and the source links kept.

## Decisions made on 1 October 2026

- **SEARCH** is the NYU version of ATLAS and was removed from the materials.
- **Session length.** Every session is a half day. The agenda slides in the Day 1, Day 2, and Day 3 decks and the agendas on the Day 1, Day 5, and Day 6 pages now run 9:30 to 1:00, matching the sample schedule. The lunch rows were removed and the topics kept.
- **Day 5 decks.** `ATLAS-Treatment-Pathways-Training.pptx` is the lead instructor deck, and `Instructor-Deck-with-Notes.pptx` is the type 2 diabetes worked example that follows it. The Day 5 page and the resources page list them in that order.
- **Day 6.** Cohort diagnostics and prediction are taught as separate half-day sessions. Part 1 (`modules/day-06-hades.md`) covers the HADES environment, CohortDiagnostics, and FeatureExtraction. Part 2 (`modules/day-06-prediction.md`, new, with its own exercise page) covers PatientLevelPrediction and uses the existing slide kit, quiz, and notebook. The navigation, overview, syllabus, and personas pages were updated.
- **Repository.** The materials stay in the existing ALS TDI repository, so the clone commands, issue links, Colab badges, and branding were left as they are.
- **Stray file removed.** The repository held a one-character file named `*` in the `docs` folder. Windows cannot create a file with that name, which stops a pull in GitHub Desktop with the error "invalid path 'docs/*'". The file is not in this copy; it also has to be deleted from the repository on GitHub before a Windows machine can pull.

- **Slide format.** Every deck was rebuilt as plain black-and-white slides on standard PowerPoint layouts (title, title and content, two content, section header, title only), in Calibri, with gray table lines and no color fills. Because the text sits in real placeholders, a site can apply its own theme from the Design tab. The rebuild carried over the slide text and the speaker notes; a word-by-word comparison found only the intended removals: the quotation slides, the small labels above titles, the running footers and page numbers, the logo images on the Day 5 and Day 6 kit slides, and one illustrative chart with example values in the Day 5 lead deck. `templates/Plain-Template.pptx` is the empty template for new decks.
- **Quotations.** The quotation slides (Lincoln, Newton, Deming, Churchill) were removed from the Module 0 and Day 1 to Day 3 decks.
- **Day 6, Part 1 deck.** A new instructor deck, `Part-1-Instructor-Deck-with-Notes.pptx`, has headline-only slides with the detail in the speaker notes, and `Part-1-Slide-Script.md` holds the same text as a slide-by-slide script.

One correction to the first version of this audit: it treated "grey segments" as something ATLAS does not show. The FinnGen ATLAS guide states that the end of a pathway is shown in grey, so the grey statements in the Day 5 kit were restored, with the wording "end of the pathway".

## The ALS use case and the maternal and child health edition

Added on 1 October 2026 at Danielle's request.

- **Separate repository.** The curriculum with its diabetes, metformin, and pregnancy examples was copied into a standalone repository for maternal and child health (delivered as `MCH-train-the-trainer.zip`). It has its own MkDocs configuration, README, and notebooks ported to a diabetes and metformin example.
- **This repository now uses one ALS example.** The running question is about people with motor neuron disease who start riluzole and their ALSFRS-R scores. The new page `als-use-case.md` defines it, lists the concepts and lookup queries, and summarizes how the ALS TDI OMOP data set records the ALSFRS-R, the diagnosis, and medications, drawing on the data set and 2026 refresh pages.
- **What was converted.** Module 0 and Days 1 to 3 (decks, workbooks, quizzes, pages, exercises, snippets, and the Day 3 tutorial), the Day 5 kit and pages (now ALS medications; two decks were renamed to `ALS-Medication-Concept-Sets.pptx` and `ALS-Pathway-Interpretation-Guide.pptx`), the Day 6 pages and Part 1 deck, the cheat sheet, and the FAQ.
- **Feasibility First.** The pages were rewritten around the ALS question. The lesson is that the ALSFRS-R has LOINC codes and is often recorded in notes, so a concept can exist and still be absent from the structured data. The deck was rebuilt with headline-only slides and a script. The importable diabetes cohort file was removed from this repository (it remains in the maternal and child health edition), and the kit README gives build steps for the ALS demo cohort.
- **ALSFRS-R in the sessions.** Day 1 covers which table holds it, Day 2 treats it as a completeness problem that DQD does not show and adds a notebook step comparing structured scores with scores in notes, and Day 3 adds it to the characterization discussion.

Statements about where ALSFRS-R scores are kept, about infusions recorded as procedures, and about medication supplied outside a health system are written as things that happen at many sites, not as rules. Adjust them to what you see in practice.

## Decisions and checks that remain

- **Module 0 length.** The Module 0 deck agenda adds up to two hours, and the sample schedule shows one hour. Both fit in a half day and were left as written.
- **Day 3 prior observation.** The tutorial sets the 365-day requirement in the entry event section, as the Book of OHDSI does. The deck, workbook, and exercise teach it as an inclusion rule so that it appears in attrition. The text now explains both; choose one for the lab.
- **Day 3 structure.** The deck teaches concept sets as their own part; the tutorial and the Book of OHDSI use entry events, inclusion criteria, and exit, with concept sets as building blocks. The section slide and its notes now say this.
- **Day 5 lead deck.** Its tab names now follow the documented Design and Executions tabs and the View reports link. The "View SQL" item, the Versions and Messages tabs, and the description of the tabular summaries were not confirmed against a current ATLAS release.
- **Day 6, Part 1.** The CohortGenerator and CohortDiagnostics code was not run against a database and was not re-checked against the package documentation.
- **Day 6, Part 2.** The code on the new page follows the PatientLevelPrediction vignette and was not run against a database. The lab needs an outcome cohort, which Part 1 now assigns as homework.
- **Concept IDs and codes.** Confirm in Athena: the ALS concept 373182, the SNOMED code 37340000 for motor neuron disease, the mapping of ICD-10-CM G12.21, the LOINC codes for the ALSFRS-R, and which ID in the range 42529071 to 42529084 is the total score (the Day 2 notebook assumes the last one). Riluzole, edaravone, and motor neuron disease are looked up by name or code in the pages, so no concept ID is hard-coded for them. The other notebook IDs are labeled as placeholders.
- **Feasibility demo counts.** The ALS demo cohort (first riluzole exposure, a motor neuron disease diagnosis, an ALSFRS-R record) was not built or run on the public ATLAS demo. Claims data hold no assessment scores, so the last rule is expected to empty the cohort; the riluzole and motor neuron disease counts in SynPUF are unknown. Build it before class and write the dated counts into the deck notes. The kit README gives a fallback if those counts are too small.
- **Community pages.** Office hours, the weekly meeting time, and the statement that sessions are recorded read as facts about a running program. Confirm them or mark the pages as templates.
- **Resources page.** Two different talks by Asieh Golozar link to the same video, and the note about lecture decks in Google Drive has no link.
- **Quiz import.** Kahoot imports its own spreadsheet template, so the CSV columns need to be pasted into that template.
- **Syllabus introduction.** It says the program "bridges Epic Clarity experience"; nothing else in the materials mentions Epic Clarity.
- **Rebuilt slides.** The rebuild was automated, so open each deck once before teaching from it. Slides that were laid out as cards or diagrams are now lists or tables, and a few may read better with a manual touch.
- **House style and slide density.** Only the text that was rewritten follows your house style. Untouched text still has em dashes, "data is", "matters", and headings with counts. Apart from the new Day 6, Part 1 deck, the decks still hold their full text on the slides; moving them to headline-only slides with the detail in the notes would be a separate piece of work.
- **Athena screenshots.** The Day 1 exercise screenshots still show a type 2 diabetes search; a caption says so. Replace them with ALS screenshots when convenient.
- **Stub file.** `training/day1-omop-cdm/Day1.pptx` is a one-byte file that PowerPoint cannot open. It was left in place and can be deleted.
- **Pages outside this folder.** `free-rwe-resources.md` and `stardustt-approach.md` mention the program and the Kahn paper and were not audited.

## Sources

- DQD check type definitions (version 2.6.3): https://ohdsi.github.io/DataQualityDashboard/articles/CheckTypeDescriptions.html
- DQD check page for measurePersonCompleteness: https://ohdsi.github.io/DataQualityDashboard/articles/checks/measurePersonCompleteness.html
- OHDSI forum, DQD questions on validation checks: https://forums.ohdsi.org/t/dqd-faqs/14068
- Kahn et al. (2016), harmonized data quality framework: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5051581/
- The Book of OHDSI, table of contents and chapters: https://ohdsi.github.io/TheBookOfOhdsi/
- HADES R setup guide: https://ohdsi.github.io/Hades/rSetup.html
- OHDSI Standardized Vocabularies release schedule (HL7 Terminology entry): https://terminology.hl7.org/NamingSystem-OMOP.xml.html
- OHDSI 2025 Year in Review (collaborator and network figures): https://www.ohdsi.org/wp-content/uploads/2025/12/OHDSI-2025-year-in-review-Ryan-9dec2025.pdf
- Cohort Pathways guide (FinnGen ATLAS documentation): https://docs.finngen.fi/working-in-the-sandbox/which-tools-are-available/atlas/detailed-guide/cohort-pathways
- OHDSI forum, Cohort Pathways settings: https://forums.ohdsi.org/t/cohort-pathways-in-atlas-faq/9511
- PatientLevelPrediction vignette code: https://rdrr.io/cran/PatientLevelPrediction/src/inst/doc/BuildingPredictiveModels.R
- Hripcsak et al. (2016), treatment pathways across the OHDSI network: https://doi.org/10.1073/pnas.1510502113
- LOINC, ALSFRS-R panel and total score: https://loinc.org/82954-9 and https://loinc.org/82953-1/
