# When One Site Is Not Enough: Network Feasibility

*Segment 5 · 26–29 minutes*

Rare exposures, uncommon outcomes, and small subgroups often defeat a single institution simply on numbers. A maternal-child question restricted to pregestational diabetes with a specific medication contrast can run out of people fast, even at a large center. This is what the OHDSI network is for, and understanding how it moves information is itself part of feasibility.

## The core idea: results travel, records do not

There is no button that reaches into every hospital and returns a live count. The network works the other way around. You define a study once, as a cohort or an analysis package. Each participating site runs it locally, behind its own firewall, against its own OMOP instance. Only **aggregate results** come back: counts, summary characteristics, effect estimates. No person-level data ever leaves any site.

That design is why the network can span dozens of databases and hundreds of millions of people while staying inside each institution's governance. It is also why network feasibility is a community process, not a query.

## How to gauge feasibility across the network

In rough order of effort:

1. **Read published data-source characterizations.** Many OHDSI databases publish Achilles profiles and characterization results. If you can see that a database holds a large childbearing-age obstetric population, you already know it is a candidate for your question.
2. **Learn which databases carry your population.** Claims and EHR databases with commercial or general populations (rather than Medicare) are where pregnancies live. Prior OHDSI pregnancy and medication-safety studies name the databases they used; those citations are a shortcut.
3. **Ask the community.** The [OHDSI Forums](https://forums.ohdsi.org) are the standard place to post a feasibility question. Describe your cohort and ask which network databases have the population and the obstetric detail. People who run those databases answer.
4. **Look at prior network studies with similar cohorts.** If a pregnancy-safety study has already run across the network, its results and its site list tell you the question is feasible and roughly how large it can get.

## How a network study actually runs

When you move from feasibility to execution, the mechanics are:

- You build the cohort definitions in ATLAS, the same skill from the [walkthrough](04-atlas-feasibility-walkthrough.md).
- You package the full analysis using the OHDSI R tooling (the **HADES** analytics library, orchestrated by **Strategus**). See [Day 6 · HADES](../modules/day-06-hades.md) for the deeper treatment.
- Participating sites run the package locally and return only aggregate results.
- Results are pooled and reviewed, often through a shared results viewer.

You do not need to master HADES or Strategus to assess feasibility. You need to know they exist, so that "how would this ever run across sites?" has a concrete answer.

## What this means for your go/no-go

Bring the network into your feasibility decision explicitly. Three outcomes are common:

- **Feasible at your site.** Your instance has the population and enough of it. Run locally first.
- **Feasible only across the network.** Your site has the population but too few people for the comparison. The question is alive, but it is a network study from the start, and you should engage the community early.
- **Not feasible as posed anywhere accessible.** No reachable database carries the population or the required detail. Reframe the question before writing a protocol.

## The honest limits

Be candid about what the network is not. It is not instantaneous, it is not a single sign-on to everyone's raw data, and it does not remove the need for local governance at each site. What it is: a disciplined way to answer a question across many populations without any of them exposing their people. For maternal-child research, where the relevant subgroups are frequently too small at one site, that tradeoff is often the only path to an answer with enough power to trust.
