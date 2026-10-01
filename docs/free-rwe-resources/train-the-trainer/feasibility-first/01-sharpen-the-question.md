# Sharpen the Question Into Cohort Logic

*Segment 1 · 4–9 minutes*

A research idea is not yet a feasibility question. "Does riluzole change how ALS progresses?" cannot be tested against a database until you say which people, over which time windows, defined by which recorded events. Feasibility assessment is mostly the work of making a question precise enough that you can check whether each piece is present in the data.

## From idea to specification

Take the running example and break it into the parts a database has to supply. A useful frame is target, exposure, outcome, and time.

| Component | The question needs | What the data must contain |
|:--|:--|:--|
| **Target population** | People with motor neuron disease | Diagnosis records for motor neuron disease or the terms below it, such as ALS |
| **Exposure** | A first riluzole exposure you can date | Drug records for riluzole, with enough history before them to call the exposure new |
| **Outcome** | ALSFRS-R scores over the following year | Structured ALSFRS-R records with a date and a numeric score |
| **Covariates** | Age, sex, other ALS medications | Demographics, drug records, and an observation period around the index date |

The outcome row is where this question most often fails. The ALSFRS-R has LOINC codes, and at many sites the scores are recorded in clinic notes and not as structured data. Keep that in mind; it is the first thing you will check in the ATLAS demo and the first thing you will ask your data steward.

## The feasibility questions inside the specification

Once the question is specified, feasibility is a sequence of concrete checks. Each one can be answered before you open a protocol.

1. **Do the concepts exist in the vocabulary?** Is there a standard concept for motor neuron disease, for riluzole, for the ALSFRS-R? (Yes for all of them. This is the easy check.)
2. **Are those concepts present in the data?** A concept can exist in the vocabulary and never appear in your instance because that source never recorded it as structured data. The record count in your source decides this check, not the existence of the concept.
3. **Is the population the right one?** People with motor neuron disease must be in the source, and in a setting that records what you need. ALS is uncommon, so even a large source may hold few people.
4. **Can you anchor time?** You need a datable index event (here, the first riluzole exposure) and enough observation time around it to see prior history and follow-up.
5. **Is the outcome the kind of event this source records?** Claims data hold no assessment scores at all. An EHR may hold the ALSFRS-R only in notes. A registry may collect it directly.
6. **Is there enough of it?** Even when everything is present, the count of people who satisfy all criteria at once may be too small to describe change over time.
7. **Are you allowed to look?** Getting aggregate counts for feasibility is usually lighter-touch than a full study, but your institution sets that line. Know it before you run anything.

!!! warning "The part that will take real work: ALSFRS-R scores kept in notes"
    If the scores at your site are in clinic notes, a query on standard concepts will not find them. The choices are to extract them from the notes (the CDM has `NOTE` and `NOTE_NLP` tables for the text and for what is extracted from it), to abstract them by hand for a sample, or to use a source that collects the scale as structured data, such as a registry. Each choice has a cost, and it is better to know on day one which one the question needs.

    The [ALS use case](../als-use-case.md) page has queries that count structured ALSFRS-R records and notes that mention the scale.

## What you take into the rest of the module

You now have a specification, not only an idea. Every later step maps back to it:

- The [steward questions](02-find-your-data-steward.md) confirm the source can supply each row of the table above.
- The [vocabulary primer](03-vocab-and-cdm-primer.md) is how you check that concepts exist and are standard.
- The [ATLAS walkthrough](04-atlas-feasibility-walkthrough.md) tests presence and counts against real (synthetic) data.
- The [checklist](06-feasibility-checklist.md) turns all of it into a go/no-go call.
