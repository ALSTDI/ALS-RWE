# Day 6, Part 1 slide script: HADES cohort diagnostics and feature extraction

This script goes with `Part-1-Instructor-Deck-with-Notes.pptx`. Each slide shows only its headline, and the text below is what to say; the same text is in the speaker notes. The code is on the [Day 6, Part 1 module page](../../../modules/day-06-hades.md) and the [exercise page](../../../exercises/day-06-hades-optional.md).

## Slide 1: HADES: Cohort Diagnostics and Feature Extraction

Welcome to Day 6, Part 1. This is an optional half-day session for people who will run OHDSI analyses in R. It covers the HADES environment, checks on a cohort definition with the CohortDiagnostics package, and baseline covariates with the FeatureExtraction package. Patient-level prediction is taught separately in Part 2. The code for this session is on the Day 6, Part 1 module and exercise pages, so the slides hold only the headline for each step.

## Slide 2: What this session covers

Give the plan for the half day. 9:30 to 9:50, an overview of HADES and how the packages fit together. 9:50 to 10:30, environment setup: DatabaseConnector, schemas, and drivers. 10:30 to 10:45, break. 10:45 to 11:45, hands-on work with CohortGenerator and CohortDiagnostics on the Day 3 cohort. 11:45 to 12:30, hands-on work with FeatureExtraction. 12:30 to 1:00, reading the output together and a preview of Part 2. By the end, participants can describe the packages, connect to a CDM, generate a cohort, run the cohort checks and read their output, and build a baseline covariate summary.

## Slide 3: HADES is a set of R packages that run against an OMOP CDM

HADES stands for Health Analytics Data-to-Evidence Suite. It is a collection of open-source R packages maintained by the OHDSI community for characterization, population-level estimation, and patient-level prediction. Each package runs against data in the OMOP Common Data Model, so the same code can be used at different sites once the connection details are changed. ATLAS is where cohorts and concept sets are designed; the HADES packages are where analyses are run in code and kept under version control.

## Slide 4: The packages used today: DatabaseConnector, CohortGenerator, CohortDiagnostics, FeatureExtraction

Introduce each package by what it does in this session. DatabaseConnector connects R to the database that holds the CDM. CohortGenerator takes cohort definitions exported from ATLAS and generates them into a cohort table. CohortDiagnostics runs a set of checks on those cohorts and shows the results in a viewer. FeatureExtraction builds covariates, such as demographics, prior conditions, and prior drugs, for the people in a cohort. CohortMethod, for estimation, and PatientLevelPrediction, for prediction, build on these; prediction is the subject of Part 2.

## Slide 5: Set up R, Java, and a GitHub token before installing

Setup problems take more session time than anything else, so settle them first. Point to the HADES R setup guide at ohdsi.github.io/Hades/rSetup.html. The guide names the R version the packages are tested against (R 4.4.1 when the guide was read on 1 October 2026), asks for RTools on Windows and for Java, and asks each person to set a GitHub personal access token, because installing every HADES package anonymously runs into the GitHub download cap. Have participants run the environment check in Part A of the exercise page and report what fails. Read the setup guide again before each delivery, since these details change.

## Slide 6: Connect to the CDM with DatabaseConnector

Show the createConnectionDetails call from the module page and explain each argument: the database platform, the server, the credentials, the port, and the folder that holds the JDBC driver. Connection details are local to each site, and credentials should come from a secure store, not from text typed into a script. Test the connection with a count of the person table. If the connection fails, check Java first, then the driver folder, then the network or VPN.

## Slide 7: Name the CDM schema, the results schema, and a dedicated cohort table

Three names are needed for the rest of the session: the schema where the CDM lives, a schema where you can write, and the name of a cohort table. Use a dedicated cohort table for this lab. Do not point CohortGenerator at the cohort table that ATLAS writes to, because creating cohort tables can replace an existing table of the same name. Keep the dedicated table after the session, since Part 2 reads the target and outcome cohorts from it.

## Slide 8: Generate the Day 3 cohort with CohortGenerator

Participants export the new-user riluzole cohort from ATLAS as JSON and SQL, save both in a cohorts folder, and list the cohort in a small settings file. CohortGenerator reads those files, creates the cohort tables, and generates the cohort. Have each person compare the count in the new table with the count ATLAS reported for the same definition on the same data source. A difference usually means a different schema or a different version of the definition.

## Slide 9: Run CohortDiagnostics on the generated cohort

The package name can mislead people who work in healthcare: these are checks of a cohort definition, not clinical diagnostics of patients. The executeDiagnostics function runs the checks and writes the results to a folder, and the viewer opens from those results. The run can take a while on a large database, so start it and use the wait to walk through what the output will show. The code on the module page was not run against a database when the page was corrected, so compare it with the package documentation for the version installed at your site.

## Slide 10: Included source concepts show which source codes are in your data

This output lists the source codes that were recorded in your data for the concepts in each concept set, with their counts. Ask participants which codes appear most often and whether any code they expected is missing. This is the same idea as the Included Source Codes tab from Day 2, now counted against the site's own records.

## Slide 11: Orphan concepts point to codes the concept set may have left out

Orphan concepts are concepts that are not in the concept set, appear in the data, and look related to the concepts that were chosen, found by matching concept names and relationships. A long list is a prompt to review whether the concept set is too narrow. Some of the concepts listed will be unrelated, so each one needs a judgment from someone who knows the clinical area.

## Slide 12: Incidence over time shows changes in coding and data capture

The incidence output shows how often people enter the cohort by calendar period, and it can be split by age and sex. Look for steps, spikes, and gaps. They often go along with a change in coding practice, a change in the source system, or the start or end of data capture, more than with a change in the population. Ask participants to offer an explanation for any pattern they see and to say how they would check it.

## Slide 13: Visit context shows where the index events were recorded

This output shows the kind of visit recorded around cohort entry, such as outpatient, inpatient, or emergency. Use it to check whether the entry event is being recorded in the setting the study design assumes. Ask the group what they expected for a first riluzole record at their site and whether the output agrees.

## Slide 14: Build baseline covariates with FeatureExtraction

FeatureExtraction builds covariates for the people in a cohort from the time before cohort entry. The default settings include demographics, conditions, drugs, procedures, and measurements. Asking for aggregated output gives one summary row for each covariate, with a count and a mean, which is what a baseline table needs. The same covariates are the inputs to propensity score models in CohortMethod and to prediction models in Part 2.

## Slide 15: Read the covariate summary as a description of the cohort

Sort the summary by mean value and read the most prevalent covariates. Ask whether the age and sex distribution, the prior conditions, and the prior drugs are what participants expected for new riluzole users at their site, and whether anything is surprising. This is the R counterpart of the characterization run in ATLAS on Day 3, and the two should tell a similar story for the same cohort.

## Slide 16: Lab: run the cohort checks and the covariate summary on your own cohort

Participants work through Parts B and C of the exercise page. Circulate and help with connection and driver problems first. Pair a clinician or research analyst with a data analyst for the review of the output, since each tends to notice different patterns. Ask each pair to write down one finding from the cohort checks that would change their concept set or their cohort definition.

## Slide 17: What to take from this session

Close with the main points. The HADES packages run the same code against any OMOP CDM once the connection details are set. A cohort has to be generated before it can be checked. The cohort checks show how the definition behaves in the site's own data: which codes are found, which related codes are left out, how entry changes over time, and where entry is recorded. A covariate summary describes who is in the cohort. None of the code in this session was run for you in advance against your database, so results and run times will differ by site.

## Slide 18: Next: Day 6, Part 2, patient-level prediction

Preview Part 2. It uses the same connection and the same dedicated cohort table. As homework, participants add an outcome cohort to their cohorts folder and settings file and generate it into the same table, because Part 2 uses it as the outcome to predict. Ask them not to drop the cohort table.

## Slide 19: Questions

Take questions. Point to the Day 6, Part 1 module and exercise pages for the code and to the package documentation for the versions installed at each site.
