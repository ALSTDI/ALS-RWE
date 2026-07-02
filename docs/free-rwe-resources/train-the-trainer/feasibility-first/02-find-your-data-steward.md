# Find Your Data Steward and Ask the Right Questions

*Segment 2 · 9–14 minutes*

This is the page people ask for most and find hardest. You do not know who at your institution runs the OMOP instance, and you do not want to send a vague email that gets forwarded four times. Here is how to find the right person and exactly what to ask them.

## Who owns an OMOP instance, usually

The instance lives with one of these groups. Try them in roughly this order.

- **The CTSA / CTSI informatics or biomedical informatics core.** At most academic medical centers with an OMOP instance, this is the owner. Search your CTSI site for "OMOP", "common data model", "cohort discovery", or "ATLAS".
- **The enterprise data warehouse or research analytics team.** Sometimes the OMOP CDM is a research-facing copy maintained alongside the clinical warehouse.
- **The department of biomedical informatics.** Especially if your institution is an active OHDSI collaborator.
- **The honest broker or research data request service.** They may not run it, but they know who does and what the access path is.
- **The health sciences library's data services.** Increasingly a front door for "how do I get research data" questions.

!!! tip "Two shortcuts that beat the org chart"
    Ask whether your institution is listed as an OHDSI collaborator (the OHDSI community and its forums can point you to your local node), and ask a colleague who has published a cohort study using your institution's data who they worked with. A name is faster than an org chart.

## Distinguish OMOP from the lookalikes

Institutions often have several data platforms, and people conflate them. For a network study you specifically want the OMOP CDM instance, because that is what ATLAS and the OHDSI tools run on. Be explicit, because these are different things:

- **OMOP CDM instance** — your institution's data mapped to the OMOP common data model, queryable with ATLAS and the OHDSI R packages. This is what you want.
- **TriNetX, Epic Cosmos, All of Us, PCORnet CDM** — other networks or models with their own tools and governance. Useful, but not the same instance and not driven by ATLAS.

If you ask for "the research database" you may be handed one of the lookalikes. Ask for "the OMOP CDM instance and ATLAS access" by name.

## The questions to ask, grouped

Bring this list to your first conversation. You will not need every answer to start, but each one closes off a way the study could fail later.

=== "Source & scope"

    - What source data feed the OMOP CDM: EHR, claims, or both? Which EHR (Epic, Cerner/Oracle Health, other)?
    - Inpatient, outpatient, or both? Which facilities and service lines are included?
    - What calendar period does the data cover, and how far back is it reliable?
    - **Does the source include people of childbearing age, and are obstetric and delivery encounters captured?** (Your load-bearing question for this exemplar.)
    - Is there any mother–infant linkage?

=== "Model & vocabulary"

    - Which CDM version (5.3 or 5.4)?
    - Which vocabulary release, and how often is it updated?
    - Which domains are populated well: condition, drug, measurement, observation, procedure, device?
    - Is there a pregnancy episode table or a pregnancy episode algorithm applied?

=== "Mapping quality"

    - What share of source records map to standard concepts, by domain?
    - What is the unmapped rate for the domains you care about (conditions and drugs here)?
    - Are lab measurements mapped with standard units, or only as text?

=== "Quality & access"

    - Has Achilles been run? Can you see the results?
    - Has the Data Quality Dashboard been run, and can you see it?
    - How do researchers query it: ATLAS, R with the OHDSI packages, direct SQL, or a request-and-return service?
    - What is required for access: training, IRB determination, a data use agreement?
    - **Are aggregate feasibility counts allowed before full IRB approval, or do counts also require review?**

## A first-contact email you can adapt

Keep it short, name the instance precisely, and ask for a short call rather than a long written answer.

```text
Subject: OMOP CDM instance and ATLAS access for a feasibility check

Hi [name],

I'm a research fellow in the maternal and child health OMOP/OHDSI
program. I'm scoping a study and want to check feasibility against
our OMOP CDM instance before I write anything up.

Could you point me to whoever maintains the OMOP instance and ATLAS,
or let me know if that's you? I have a short, specific list of
questions (source data, CDM and vocabulary version, whether obstetric
and childbearing-age data are captured, mapping coverage, and how to
get read access for cohort feasibility counts).

A 20-minute call would be ideal. I'm flexible [days/times].

Thanks,
[name, program, contact]
```

## What "done" looks like for this step

You have a name, a way to reach them, and answers to at least the source, population, CDM version, and access questions. That is enough to interpret everything you see in the ATLAS demo and to know whether your real instance can carry the target population. If the answer to the childbearing-age question is no, you have just saved yourself the entire study, and you move to the [network](05-network-feasibility.md) instead.
