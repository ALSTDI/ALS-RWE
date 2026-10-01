# ATLAS Feasibility Walkthrough

*Segment 4 · 18–26 minutes. This page is both the follow-along guide and the live-demo script.*

We now test the running question using the public ATLAS demo. You do not need an account at your institution for this.

## What you are working with

- **Tool:** the public ATLAS demo at **[https://atlas-demo.ohdsi.org](https://atlas-demo.ohdsi.org)** (Chrome is the supported browser).
- **Data:** a synthetic data set called **SynPUF**, built from CMS Medicare claims. The data are synthetic and meant for demonstration, not research.

That data choice is part of the lesson. Claims record diagnoses, procedures, and dispensed drugs. They do not record assessment scores such as the ALSFRS-R. So the demo lets you watch a feasibility check pass for the diagnosis and the drug and fail for the outcome, which is the failure you most need to catch early at your own site, where the cause is more often scores kept in notes.

!!! tip "Build the cohort once before class"
    Build and save the demo cohort ahead of time, following the steps in the [instructor kit](../training/feasibility-first/kit/README.md), so you show a saved definition instead of typing concept sets in front of the room. Generate it against SynPUF and write down the dated counts, because the counts on the public demo were not checked when this page was written.

## Step 1 — Confirm the concepts exist (Search)

Open **Search** in the left menu and type `amyotrophic lateral sclerosis`.

- A standard concept appears (SNOMED, domain **Condition**).
- Read the record count columns for this source. People with ALS qualify for Medicare, so some records are expected; check what the demo shows.
- Open the hierarchy and find the parent **Motor neuron disease**. That broader concept, with its descendants, is the one the cohort will use.

Now search `riluzole`. The RxNorm ingredient is standard and belongs to the **Drug** domain. Read its record counts.

Now search `ALSFRS-R`. The LOINC concepts for the scale appear, so the concept **exists**. Look at the record counts: in a claims source they are zero. If the demo's vocabulary does not list the concepts, show them in [Athena](https://athena.ohdsi.org/) instead.

Name what just happened for the group: the diagnosis and the drug exist and are present, and the score exists and is not present.

## Step 2 — Build concept sets

Go to **Concept Sets → New Concept Set**. Build and name three:

- **Motor neuron disease:** add the parent concept and check Descendants.
- **Riluzole:** add the RxNorm ingredient and check Descendants.
- **ALSFRS-R:** add the LOINC total score concept (code 82953-1), or all of the scale's concepts.

For each, use the **Included Concepts** tab to see what the expression resolves to, and the **Included Source Codes** tab to check what you are capturing.

## Step 3 — Define the cohort

Go to **Cohort Definitions** and open the cohort you built before class, or build it step by step so the group sees each requirement narrow the count:

1. **Entry event:** the first riluzole drug exposure.
2. **Inclusion rule 1:** a motor neuron disease diagnosis on or before the index date.
3. **Inclusion rule 2:** at least one ALSFRS-R record in the year after the index date. Check the domain of the concepts first, since it decides whether the rule is an observation or a measurement criterion.

## Step 4 — Generate and read the counts

Open the **Generation** tab and generate against the SynPUF source. Then read the **attrition report**:

- First riluzole exposure: the starting count.
- Add the motor neuron disease diagnosis: the count narrows.
- Add the ALSFRS-R requirement: the count falls to zero, or close to it.

Pause here and name the result. Every concept in the definition exists in the vocabulary. The cohort is empty. Nothing is broken. The source does not record the outcome the question needs.

## Step 5 — Work out which kind of empty it is

When a cohort comes back empty, three causes look the same on screen and call for different next steps:

- **A concept problem.** The codes are in the source and were left unmapped, so a query on standard concepts misses them. Ask your steward about mapping.
- **A population problem.** The people are not in this source, or are too few. Take the question to a source that has them.
- **A data capture problem.** The people are there and the information exists, but it was never recorded as structured data. This is the ALSFRS-R at many sites. The next step is to find out where the scores are kept (often clinic notes) and what it would take to extract them.

In the demo the cause is the third one in its plainest form: claims never hold the score. At your own site, run the queries on the [ALS use case](../als-use-case.md) page to count structured ALSFRS-R records and notes that mention the scale.

## Step 6 — Take the definition with you

The public ATLAS demo cannot run your study, and the definition you built there can be used elsewhere:

- **Export the cohort definition** (JSON) and import it into your institution's ATLAS, where it runs against your data.
- Use the exported JSON and SQL with the **HADES R packages** (for example CohortGenerator), which run the definition in any environment with a CDM, with no local ATLAS required. The Book of OHDSI (chapter 8) describes designing an analysis in a public ATLAS and running the exported code where the data are.

## What you showed in this walkthrough

- You can confirm concept existence and standard status from Search.
- You can tell concept existence from concept presence by reading counts.
- You can build a cohort and see each requirement narrow it.
- You can tell a concept problem, a population problem, and a data capture problem apart, and act differently on each.

Next: when your own instance has the population but not enough of it, you go to the [network](05-network-feasibility.md). To see which OHDSI tool answers each feasibility check, see the [checks-to-tools appendix](08-checks-to-tools.md).
