# Sharpen the Question Into Cohort Logic

*Segment 1 · 4–9 minutes*

A research idea is not yet a feasibility question. "Does diabetes affect pregnancy outcomes?" cannot be tested against a database until you say exactly which people, over exactly which time windows, defined by exactly which recorded events. Feasibility assessment is mostly the work of making a question precise enough that you can check whether each piece is present in the data.

## From idea to specification

Take the running example and break it into the parts a database has to supply. A useful frame is target, exposure, outcome, and time.

| Component | The question needs | What the data must contain |
|:--|:--|:--|
| **Target population** | Pregnant people with a pregnancy episode you can date | Obstetric and delivery records, people of childbearing age, a pregnancy start and end |
| **Prior condition** | Pregestational type 1 or type 2 diabetes, diagnosed before the pregnancy started | Diabetes condition records with dates that precede the pregnancy start |
| **Exposure** | Metformin versus insulin in the first trimester | Drug records for those ingredients, dated within the pregnancy window |
| **Outcome** | Preeclampsia during the pregnancy | Preeclampsia condition records during the episode |
| **Covariates** | Age, prior conditions, healthcare use | Demographics and a defined observation period around the index date |

Notice that four of the five rows depend on one hard thing: being able to identify and date a pregnancy. That is the load-bearing element, and it is where this question most often fails feasibility. Hold that thought; it is the first thing you will check in the ATLAS demo and the first thing you will ask your data steward.

## The feasibility questions hiding in the specification

Once the question is specified, feasibility is a sequence of concrete checks. Each one can be answered before you ever open a protocol.

1. **Do the concepts exist in the vocabulary?** Is there a standard concept for pregestational diabetes, for preeclampsia, for metformin, for insulin? (Almost always yes. This is the easy check.)
2. **Are those concepts present in the data?** A concept can exist in the vocabulary and never appear in your instance because that source never recorded it. Record count, not concept existence, is what matters.
3. **Is the population the right one?** Childbearing-age people must actually be in the source. A geriatric claims database has diabetes in abundance and no pregnancies at all.
4. **Can you anchor time?** You need a datable index event (here, pregnancy start) and enough observation time around it to see the exposure and the outcome.
5. **Is there enough of it?** Even when everything is present, the count of people who satisfy all criteria at once may be too small to answer the comparative question. Feasibility includes rough power.
6. **Are you allowed to look?** Getting aggregate counts for feasibility is usually lighter-touch than a full study, but your institution sets that line. Know it before you run anything.

!!! warning "The part that will take real work: pregnancy episodes"
    Identifying pregnancy in observational data is a known, nontrivial problem. A single obstetric code does not give you a start date, an end date, or a trimester. The OHDSI community has published pregnancy episode algorithms that assemble episodes from many signals (prenatal visits, gestational-age observations, delivery and outcome codes) and estimate start and end. If your question depends on gestational timing, as this one does through "first trimester" and "pregestational", you will need one of these algorithms applied to your instance, or you will need to build it.

    This is not a reason to abandon the question. It is a reason to know, on day one, that the pregnancy-timing layer is the part that will take real work, so you can plan for it instead of discovering it late.

## What you carry into the rest of the module

You now have a specification, not just an idea. Every later step maps back to it:

- The [steward questions](02-find-your-data-steward.md) confirm the source can supply each row of the table above.
- The [vocabulary primer](03-vocab-and-cdm-primer.md) is how you check that concepts exist and are standard.
- The [ATLAS walkthrough](04-atlas-feasibility-walkthrough.md) tests presence and counts against real (synthetic) data.
- The [checklist](06-feasibility-checklist.md) turns all of it into a go/no-go call.
