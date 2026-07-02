# Facilitator Notes

*For the instructor running this live. Not part of the 30-minute clock.*

You have fellows spanning computer science and data analytics through clinical medicine. The design goal is that both ends of that range stay engaged: the clinical fellows are not lost in the tooling, and the technical fellows are not bored by the vocabulary basics. The running example does that work, because everyone can reason about diabetes and pregnancy, and the feasibility logic is new to nearly all of them regardless of background.

## Timing and where to spend it

The clock in the module is a target, not a cage. If you have to compress, protect the ATLAS walkthrough and the go/no-go decision; those are the parts they cannot get from reading. If you have extra time, expand the steward-questions discussion, since that is where the room's institutional knowledge surfaces.

## Running the live demo safely

The public ATLAS demo is reliable most of the time and occasionally is not. Protect the session:

- **Do a dry run the day before**, on the same network and browser (Chrome) you will present with.
- **Import and save the pre-built cohort** from the [instructor kit](../training/feasibility-first/kit/README.md) so you screen-share a saved definition instead of typing concept sets live.
- **Capture screenshots during the dry run** of the diabetes search with large counts, the preeclampsia search with tiny counts, the cohort definition, and the near-zero attrition after the childbearing-age rule. If the demo is down live, narrate from the screenshots and lose nothing.
- If the demo asks for a sign-in, mention it is a known intermittent behavior and fall back to screenshots rather than troubleshooting in front of the room.

## The one beat that must land

The whole module turns on Step 4 of the walkthrough: the cohort count collapsing when the childbearing-age requirement is added, even though every concept exists. Slow down there. Ask the room why the cohort is empty before you tell them. Let a clinical fellow and a technical fellow each guess. The point they should reach on their own is that concept existence and population presence are different things. If they leave with one idea, that is the one.

## Adapting the exemplar

Fellows will want to run their own questions. Encourage it, and steer them toward questions with the same shape (a target population, an exposure contrast, an outcome, a time anchor). Warn them off two traps: questions that need data the source type cannot hold (asking a claims database for a symptom only in clinical notes), and questions whose population is absent rather than rare (the SynPUF pregnancy problem).

## Common questions and honest answers

- **"Can I just query the whole network for counts?"** No. Results travel, records do not. Feasibility across the network is a community process (forums, published characterizations, prior studies), not a single query.
- **"The demo has no pregnancies, so how is it useful?"** That absence is the teaching tool. It shows infeasibility cleanly and safely. The transferable skill is telling a concept problem from a population problem.
- **"Do I need to learn R, HADES, and Strategus to start?"** Not for feasibility. You need ATLAS for definitions and the vocabulary basics for interpretation.
- **"How much of this needs IRB?"** Institution-specific, which is why it is a steward question and a checklist row. Do not assert a general rule; have them confirm locally.

## This module inside the ALS-RWE site

These pages already live in `docs/free-rwe-resources/train-the-trainer/feasibility-first/`, so they build and deploy with the rest of the site through the existing `mkdocs gh-deploy` workflow. Nothing extra to configure. To edit, change the Markdown through the GitHub web interface and let the Pages action rebuild. The instructor deck and the importable ATLAS cohort are in `training/feasibility-first/kit/`.
