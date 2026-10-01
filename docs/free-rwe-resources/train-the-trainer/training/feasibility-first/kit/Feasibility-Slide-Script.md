# Feasibility First slide script

This script goes with `Feasibility-Instructor-Deck-with-Notes.pptx`. Each slide shows only its headline, and the text below is what to say; the same text is in the speaker notes. The follow-along pages start at [Feasibility First](../../../feasibility-first/index.md).

## Slide 1: Is My Question Feasible?

This is a 30-minute walkthrough for researchers new to OMOP and OHDSI. It goes from a question to a go or no-go decision, using the public ATLAS demo so nobody needs institutional access yet. The running example is the ALS use case used across this program: motor neuron disease, riluzole, and the ALS Functional Rating Scale - Revised, the ALSFRS-R. The workflow is the same for any disease area, so invite people to keep their own question in mind.

## Slide 2: Every study starts with a question and an unfamiliar data source

Describe the position the audience is in. They have a question they care about. They do not know who runs the OMOP instance, what is in it, or how it was mapped, and they do not know whether the data can answer the question. Not knowing who to ask is where everyone starts, and the rest of the session turns that into a short list of checks.

## Slide 3: What you will be able to do by the end

State the objectives. Turn a loose idea into a specification you can test. Find who owns the OMOP instance and ask the right questions. Read the vocabulary well enough to know whether your concepts exist and are mapped. Use ATLAS to test concept presence and cohort counts, and read what the counts show. Decide whether the question is feasible here, feasible across the network, or needs reframing, before a protocol is written.

## Slide 4: The running question: motor neuron disease, riluzole, and the ALSFRS-R

Read the question aloud: Among people with motor neuron disease who start riluzole, what do the data show about their ALSFRS-R scores over the following year? Everyone who works with ALS data can reason about it. Point out now that the question has a hard part, which the next slides come back to: it needs ALSFRS-R scores as structured data.

## Slide 5: Check feasibility before you write a protocol

This is the thesis of the module. A feasibility check takes a few searches and one cohort. Finding out after the protocol is written and the review board has approved it that the data cannot answer the question costs far more. Everything else in the session is technique in service of checking first.

## Slide 6: Turn the idea into cohort logic

Walk through the specification. The target population is people with motor neuron disease, which needs diagnosis records for that concept or the terms below it, such as ALS. The exposure is a first riluzole exposure you can date, which needs drug records and enough history before them. The outcome is ALSFRS-R scores over the following year, which needs structured records with a date and a numeric score. A question becomes checkable only once it is this specific.

## Slide 7: Feasibility is a set of concrete checks

List the checks, which the later segments answer. Do the concepts exist, as standard concepts in the right domain? Are they present in your source, with record counts above zero? Does the source contain the right people? Can time be anchored on a datable index event with observation time around it? Is the outcome the kind of event this source records? Are there enough people who meet every criterion at once? Does governance allow what you want to do? Stress the difference between the first and the second: a concept can exist in the vocabulary and appear zero times in your data.

## Slide 8: The ALSFRS-R has LOINC codes and is often recorded in notes

This is the part of the question that will take real work. The scale has a LOINC code for the panel, 82954-9, for the total score, 82953-1, and for each item, so a vocabulary search finds it at every site. At many sites the scores are written in clinic notes and never reach a structured table, so a query on standard concepts finds nothing. That is not a reason to abandon the question. It is a reason to learn early where the scores are kept and what it would take to use them: text extraction, chart abstraction, or a source such as a registry that collects the scale directly.

## Slide 9: Find the people who run your OMOP instance

Suggest where to look, in rough order: the informatics core of the clinical and translational science institute, the enterprise data warehouse or research analytics team, the department of biomedical informatics, the honest broker or research data request service, and the health sciences library's data services. Tell people to ask for the OMOP CDM instance and ATLAS access by name, because institutions often have several research data platforms, such as TriNetX or Epic Cosmos, with different tools and governance. A colleague who has published a cohort study with local data is often the fastest route to a name.

## Slide 10: Ask how the ALSFRS-R is recorded at your site

Give the questions to ask the steward. On source and scope: which EHR or claims sources feed the CDM, which facilities and dates, and whether a neuromuscular or ALS clinic is included. On the outcome: are ALSFRS-R scores recorded as structured data, in flowsheets, or in notes, and are notes loaded into the CDM. On model and mapping: the CDM version, the vocabulary release, which domains are well populated, and the unmapped rate for conditions and drugs. On quality: whether Achilles and the Data Quality Dashboard have been run. On access: how researchers query the data, what training or approvals are needed, and whether aggregate counts are allowed before full review.

## Slide 11: A concept can exist in the vocabulary and be absent from your data

This is the idea the demo depends on. Existence is a property of the vocabulary and is the same at every site. Presence is a property of one instance. Cohorts are built from standard concepts, such as SNOMED, RxNorm, and LOINC concepts, and source codes are mapped to them when the data are loaded. A record that was never captured as structured data cannot be found by any concept query.

## Slide 12: The domain tells you which table to look in

A short point for people new to the model. Motor neuron disease is in the Condition domain and its records are in the condition occurrence table. Riluzole is in the Drug domain and its records are in drug exposure. ALSFRS-R scores, where they are structured, are in observation or measurement, depending on how the site mapped them; the ALS TDI data set stores them in observation. Looking in the wrong table and finding nothing is a common false alarm, so identify the domain first.

## Slide 13: The public ATLAS demo runs on synthetic Medicare claims

Set expectations before opening the tool. The demo at atlas-demo.ohdsi.org runs on SynPUF, synthetic Medicare claims meant for demonstration. Claims record diagnoses, procedures, and dispensed drugs. They do not record assessment scores. So the demo will show the diagnosis and the drug as present and the ALSFRS-R as absent. Run the saved cohort before class and write the dated counts into these notes, because the counts on the public demo were not checked when this deck was written.

## Slide 14: Search, build concept sets, define the cohort, generate

Describe the sequence, and show a cohort that was built and saved before class. In Search, look up amyotrophic lateral sclerosis, riluzole, and ALSFRS-R, and read the record counts for each. Build concept sets for motor neuron disease with descendants, riluzole with descendants, and the ALSFRS-R. Define the cohort: entry is the first riluzole exposure, the first inclusion rule requires a motor neuron disease diagnosis on or before index, and the second requires at least one ALSFRS-R record in the following year. Then generate against SynPUF.

## Slide 15: Every concept exists and the cohort is empty

Slow down here. Read the attrition report: the count after the entry event, the count after the diagnosis rule, and the count after the ALSFRS-R rule, which is zero or close to it. Before explaining, ask the group why the cohort collapsed, and let a clinical participant and a technical participant each guess. The answer to reach: the concepts exist, and this source does not record the score.

## Slide 16: Work out which kind of empty it is

Three causes look the same on screen and call for different next steps. A concept problem: the codes are in the source and were left unmapped, which a steward may be able to fix. A population problem: the people are not in this source, so the question goes elsewhere. A data capture problem: the people are there and the information exists, but it was never recorded as structured data, which is the ALSFRS-R at many sites. For that one, find out where the scores are kept and what extraction would take.

## Slide 17: The definition can be exported and run where the data are

The public demo cannot run the study, and the work done there is not wasted. Export the cohort definition as JSON and import it into your institution's ATLAS. The exported JSON and SQL can also be run with the HADES R packages in any environment with a CDM. The Book of OHDSI describes designing an analysis in a public ATLAS and running the exported code where the data are.

## Slide 18: When one site is not enough, the study runs at each site and returns results

ALS is uncommon, so one site may hold too few people. In an OHDSI network study the definition is written once, each site runs it behind its own firewall, and only aggregate results are returned. To gauge feasibility across the network, read published descriptions of data sources, look for sources that record functional scores, such as disease registries, and ask on the OHDSI Forums. You do not need to know HADES or Strategus to assess feasibility, only that they are how a network study is packaged and run.

## Slide 19: Decide before you write a protocol

State the possible decisions. Feasible here: the population and the outcome are present and sufficient, so pilot locally. Feasible only across the network: present but too few, so scope it as a network study and engage early. Feasible with extraction: the scores are in notes, so plan for text extraction or abstraction. Not feasible as posed: no reachable source records what is needed, so reframe the question. A clear no found at this stage saves the cost of the study.

## Slide 20: Check feasibility first

Close on the habit. Point to the take-home pages: the checks, the steward questions and email, the ATLAS walkthrough, and the one-page worksheet. Encourage each person to run their own question through the worksheet.
