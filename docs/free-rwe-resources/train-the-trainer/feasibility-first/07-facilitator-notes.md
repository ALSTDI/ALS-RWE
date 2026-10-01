# Facilitator Notes

*For the instructor running this live. Not part of the 30-minute clock.*

Your group will span data analytics through clinical work. The design goal is that both ends of that range stay engaged: clinical participants are not lost in the tooling, and technical participants are not bored by the vocabulary basics. The running example helps, because anyone who works with ALS data knows the ALSFRS-R, and the feasibility logic is new to nearly everyone.

## Timing and where to spend it

The clock in the module is a target, not a cage. If you have to compress, protect the ATLAS walkthrough and the go/no-go decision; those are the parts they cannot get from reading. If you have extra time, expand the steward-questions discussion, since that is where the room's institutional knowledge comes out.

## Running the live demo safely

The public ATLAS demo is reliable most of the time and occasionally is not. Protect the session:

- **Do a dry run the day before**, on the same network and browser (Chrome) you will present with.
- **Build and save the demo cohort** following the [instructor kit](../training/feasibility-first/kit/README.md) so you show a saved definition instead of typing concept sets live.
- **Capture screenshots during the dry run** of the ALS and riluzole searches with their counts, the ALSFRS-R search with zero records, the cohort definition, and the attrition after the ALSFRS-R rule. If the demo is down live, narrate from the screenshots.
- If the demo asks for a sign-in, mention it is a known intermittent behavior and fall back to screenshots rather than troubleshooting in front of the room.

## The one beat that must land

The whole module turns on Step 4 of the walkthrough: the cohort count collapsing when the ALSFRS-R requirement is added, even though every concept exists. Slow down there. Ask the room why the cohort collapsed before you tell them, and let a clinical participant and a technical participant each guess. The point they should reach on their own is that a concept can exist in the vocabulary and be absent from the data, and that for the ALSFRS-R the usual reason is that the scores are kept in notes.

## Adapting the exemplar

Participants will want to run their own questions. Encourage it, and steer them toward questions with the same shape (a target population, an exposure, an outcome, a time anchor). Point out two traps: questions that need data the source type does not hold (asking a claims database for a functional score), and questions whose outcome is recorded only in notes.

## Common questions and honest answers

- **"Can I just query the whole network for counts?"** No. Results travel, records do not. Feasibility across the network is a community process (forums, published characterizations, prior studies), not a single query.
- **"The demo has no ALSFRS-R scores, so how is it useful?"** That gap is the teaching tool. It shows infeasibility safely. The skill that transfers is telling a concept problem, a population problem, and a data capture problem apart.
- **"Do I need to learn R, HADES, and Strategus to start?"** Not for feasibility. You need ATLAS for definitions and the vocabulary basics for interpretation.
- **"How much of this needs IRB?"** Institution-specific, which is why it is a steward question and a checklist row. Do not assert a general rule; have them confirm locally.

## This module inside the ALS-RWE site

These pages already live in `docs/free-rwe-resources/train-the-trainer/feasibility-first/`, so they build and deploy with the rest of the site through the existing `mkdocs gh-deploy` workflow. Nothing extra to configure. To edit, change the Markdown through the GitHub web interface and let the Pages action rebuild. The instructor deck, its script, and the steps for building the demo cohort are in `training/feasibility-first/kit/`.
