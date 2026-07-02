# ATLAS Feasibility Walkthrough

*Segment 4 · 18–26 minutes. This page is both the follow-along guide and the live-demo script.*

We now test the running question against real data using the public ATLAS demo. You do not need an account at your institution for this. Everyone can follow along.

## What you are working with

- **Tool:** the public ATLAS demo at **[https://atlas-demo.ohdsi.org](https://atlas-demo.ohdsi.org)** (Chrome is the supported browser).
- **Data:** a synthetic dataset called **SynPUF**, built from CMS Medicare claims. Read that twice. Medicare is a program for people who are mostly 65 and older, and it is synthetic, and it is for demonstration, not research.

That data choice is deliberate here, and it is the lesson. SynPUF is full of diabetes and has essentially no pregnancies, because its population is old. So the demo lets you watch a feasibility check succeed on the concept level and fail on the population level, which is precisely the failure mode you most need to catch early against your own instance.

!!! tip "Pre-built definition — import once, screen-share instead of typing live"
    The instructor kit includes a ready-to-import cohort, `Demo-Cohort-Diabetes-Childbearing-Age.json`. It is built to collapse cleanly on SynPUF using only concepts that are guaranteed present, so you never type concept sets live in front of the room.

    1. Open [atlas-demo.ohdsi.org](https://atlas-demo.ohdsi.org) → **Cohort Definitions → New Cohort**.
    2. Open the **Export** tab → **JSON** sub-tab, paste the file's contents, and **Import**.
    3. Name it and **Save**.
    4. Open **Generation** → **Generate** against SynPUF, and confirm the counts before class.

    Get the file and full instructions from the [instructor kit](../training/feasibility-first/kit/README.md).

## Step 1 — Confirm a concept exists (Search)

Open **Search** in the left menu and type `type 2 diabetes mellitus`.

You are checking three things from the [primer](03-vocab-and-cdm-primer.md):

- A standard concept appears (SNOMED, domain **Condition**, class Standard).
- Click it. The record-count and person-count columns show it is abundant in this source. Diabetes is everywhere in a Medicare population.
- Note the hierarchy tab: this concept has many descendants you will want to include.

Say out loud what just happened: the concept exists, it is standard, and it is present in large numbers. Two of your three feasibility checks pass for diabetes.

Now search `preeclampsia`. The concept exists in the vocabulary (it is a valid SNOMED Condition), but look at the record and person counts in this source. They are negligible. First hint of trouble, and it is a population problem, not a vocabulary problem.

## Step 2 — Build concept sets

Go to **Concept Sets → New Concept Set**. Build and name a few:

- **Diabetes mellitus:** add the parent concept, include descendants (this covers type 1 and type 2).
- **Preeclampsia:** add the preeclampsia concept, include descendants.
- **Metformin** and **Insulin:** add the ingredient-level RxNorm concept, include descendants.
- **Pregnancy or delivery:** add obstetric and delivery concepts you can find.

For each, use the **Included Concepts** tab to see how many concepts your rules resolve to, and the source-code tab to sanity-check what you are capturing. This is where you feel the difference between a concept that exists and a concept set that is defined well.

## Step 3 — Define the cohort

Go to **Cohort Definitions**. If you imported the pre-built definition, open it now. If you are building live, create the target step by step so the class sees each requirement narrow the count:

1. **Entry event:** a diabetes condition occurrence (the pre-built demo), or a pregnancy event at a real instance.
2. **Inclusion rule 1:** the childbearing-age filter (female, age 15–44 at index). At a real instance this is where "pregestational diabetes before a pregnancy" would go.
3. **Inclusion rule 2 (optional):** a metformin or insulin exposure, to preview the exposure arm.

## Step 4 — Generate and read the counts (the moment)

Open the **Generation** tab and generate against the SynPUF source. Then watch what the counts do as the definition builds up, using the **attrition report**:

- Diabetes alone: large.
- Add the childbearing-age requirement: the count falls off a cliff.
- (At a real instance, requiring pregestational diabetes before a pregnancy does the same thing for the same reason.)

Stop here and name it. Every concept in your definition exists in the vocabulary. The cohort is nearly empty. Nothing is broken. The data source simply does not contain the population your question needs. **This is what infeasibility looks like, and you found it in about eight minutes instead of eight months.**

## Step 5 — Diagnose why, so the lesson generalizes

Use characterization to prove the cause rather than guess it. View the age distribution of anyone the definition captured. It is overwhelmingly elderly, because the source is Medicare. Childbearing-age people are barely present, so pregnancies cannot be.

The transferable habit: when a cohort comes back empty, ask whether the concepts are missing or the population is missing. They lead to completely different next moves. Missing concepts might mean a mapping problem you can fix. A missing population means this source can never answer the question, and you take it elsewhere.

## Step 6 — Take the definition with you

The public ATLAS demo cannot run your study, but it can hand you the definition to run where the data live. Two paths:

- **Export the cohort definition** (JSON) and import it into your institution's ATLAS, where it runs against real obstetric data.
- ATLAS can **generate the R code** for a full study from a definition built on the public instance, which then runs in any environment with a CDM, no local ATLAS required. The Book of OHDSI documents this as an explicit design goal of the public instance.

So the demo is not a dead end even though its data cannot answer the question. It is where you design and validate the logic for free, then point that logic at data that can.

## What you proved in this walkthrough

- You can confirm concept existence and standard status from Search.
- You can distinguish concept existence from concept presence by reading counts.
- You can build a real phenotype and see requirements narrow a cohort in real time.
- You can tell a concept problem from a population problem, and act differently on each.
- You can carry the definition to a capable data source.

Next: when your own instance has the population but not enough of it, you go to the [network](05-network-feasibility.md). To see which OHDSI tool answers each feasibility check, see the [checks-to-tools appendix](08-checks-to-tools.md).
