# Your Go/No-Go Feasibility Decision

*Segment 6 · 29–30 minutes*

This is the artifact fellows keep. Fill it in for your own question. If any row in the first table is a hard no, you have your answer before you write a protocol, and that is a win, not a failure.

## The seven checks

| # | Check | What proves it |
|:--|:--|:--|
| 1 | **Concepts exist** | Standard concepts found in ATLAS Search for each element (condition, drug, outcome), in the right domain |
| 2 | **Concepts are present in the data** | Nonzero record and person counts in your target source, not just in the vocabulary |
| 3 | **Population fits** | The source contains the right people (here: childbearing age, with obstetric encounters) |
| 4 | **Time can be anchored** | A datable index event exists (pregnancy start), with enough observation period around it |
| 5 | **Outcome is capturable** | The outcome is the kind of event this data type actually records (claims vs EHR differ) |
| 6 | **Sample size is sufficient** | The count meeting all criteria at once is large enough for the comparison you want |
| 7 | **Governance clears** | You know whether feasibility counts and the full study need IRB, DUA, or training |

For which OHDSI tool answers each check, see the [checks-to-tools appendix](08-checks-to-tools.md).

## Reading your result

- **All seven yes:** feasible at your site. Move to a formal cohort definition and pilot it locally.
- **1–5 yes but 6 no:** feasible only across the network. The question is sound; scope it as a network study and engage the [community](05-network-feasibility.md) early.
- **3 no (population absent):** not feasible in this source. Do not try to fix it with mapping; take the question to a database that has the population.
- **1 or 2 no (concepts absent or unmapped):** possibly a mapping or ETL issue. Ask your steward before concluding the question is dead.
- **7 no or unknown:** stop and resolve governance before generating anything, even counts.

## One-page worksheet

Copy this into your notes and complete it for your question.

```text
RESEARCH QUESTION (one sentence):
_______________________________________________________________

SPECIFICATION
  Target population:        ______________________________________
  Prior condition:          ______________________________________
  Exposure(s):              ______________________________________
  Outcome:                  ______________________________________
  Index / time anchor:      ______________________________________
  Observation window:       ______________________________________

CONCEPTS (from ATLAS Search)
  Element            Standard concept?   Present in my source?   Count
  ________________   _______________     ___________________     _____
  ________________   _______________     ___________________     _____
  ________________   _______________     ___________________     _____

INSTANCE FACTS (from your data steward)
  Steward name / contact:   ______________________________________
  Source (EHR / claims):    ______________________________________
  CDM + vocab version:      ______________________________________
  Childbearing-age pop?:    ______________________________________
  Pregnancy episode avail?: ______________________________________
  Access path:              ______________________________________
  Counts allowed pre-IRB?:  ______________________________________

DECISION
  [ ] Feasible here
  [ ] Feasible via network only
  [ ] Not feasible as posed  ->  reframe: __________________________
  Next action:              ______________________________________
```

## The habit to leave with

Every real study starts with a version of this page. The fellows who finish with a running network study are not the ones with the cleverest questions. They are the ones who checked feasibility first, found the dead ends in minutes, and spent their real time on the question that survived. Make this worksheet the first thing you do, every time.
