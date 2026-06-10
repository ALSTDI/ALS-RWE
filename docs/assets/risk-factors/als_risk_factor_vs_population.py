"""
============================================================================
ALS TDI Risk Factor Survey: cohort prevalence vs. U.S. general population
============================================================================
Aim 2 of CDC R01TS000341 ("evaluate evidence in the ARC data repository to
support or refute risk factors previously associated with ALS").

This script:
  1. Computes the lifetime prevalence of every risk factor named in the grant
     (Specific Aims / B.6) plus the conditions the analyst asked us to check
     (autoimmune, asthma, Parkinson's self and family), keyed by Subject so
     repeat/longitudinal rows collapse to one person.
  2. Compares each cohort prevalence to a credible U.S. general-population
     benchmark (CDC/NCHS where available; peer-reviewed otherwise), with the
     citation stored alongside the number.
  3. Writes a tidy comparison table to CSV.

Output is fully aggregate and de-identified. No individual records, no dates,
no free text are emitted.

Cohort note: the 766 General-Information respondents all link to ALS patients
in the RRV export; median current age 65, 62.3% male. That older, male-skewed
profile matters for interpretation and is carried into the caveats below.

DESIGN CAVEAT (read before quoting any number): this is a CASE-ONLY series.
Comparing case prevalence to population prevalence is descriptive only. It does
NOT estimate risk or odds ratios (no controls, no age/sex standardization,
self-reported, recall bias, and several survey items use broader definitions
than the national benchmarks). Treat every "higher/lower" flag as
hypothesis-generating, not as evidence of causation.
============================================================================
"""

import pandas as pd
import numpy as np

SRC = "N_784_Risk_Factor_ALS_TDI_Survey_Data.xlsx"   # row-level survey export
RRV = "quantiphi_als_rrv_subject_data_rrv_2.txt"     # diagnosis / sex / onset link

# ---------------------------------------------------------------------------
# 1. COHORT PREVALENCE  (keyed by Subject; "ever" = any positive row)
# ---------------------------------------------------------------------------
xl = pd.ExcelFile(SRC, engine="calamine")

def is_yes(series):
    """Checkbox / yes-no field -> boolean True for an affirmative."""
    return series.astype(str).str.strip().str.lower().eq("yes")

def ever_by_subject(df, flag_col):
    """Collapse to one row per Subject; True if any row is affirmative."""
    tmp = df[["Subject"]].copy()
    tmp["flag"] = is_yes(df[flag_col])
    return tmp.groupby("Subject")["flag"].any()

cohort = {}   # label -> (n_positive, n_denominator)

# --- Smoking ever & vigorous activity ever  (Lifestyle 1) ---
life = xl.parse("Lifestyle 1")
smk = ever_by_subject(life,
    "Have you ever smoked one or more cigarettes per day for six months or longer?")
cohort["Smoking, ever (>=1 cig/day for 6+ months)"] = (smk.sum(), len(smk))

vig_col = [c for c in life.columns if "vigorous leisure" in c][0]
vig = ever_by_subject(life, vig_col)
cohort["Vigorous leisure-time physical activity, ever"] = (vig.sum(), len(vig))

# --- Military service  (Occupation 1) ---
occ = xl.parse("Occupation 1")
mil_df = occ[["Subject", "Member of the armed forces"]].dropna(
    subset=["Member of the armed forces"])
mil = ever_by_subject(mil_df, "Member of the armed forces")
cohort["Military service (ever member of armed forces)"] = (mil.sum(), len(mil))

# --- Head/neck injury (any) and blast exposure  (Injuries) ---
inj = xl.parse("Injuries")
head_qs = [c for c in inj.columns
           if c.startswith("Have you ever")
           and "explosion" not in c and "electrical" not in c]
blast_q = [c for c in inj.columns if "explosion or blast" in c][0]
inj["_head"] = inj[head_qs].apply(lambda r: is_yes(r).any(), axis=1)
inj["_blast"] = is_yes(inj[blast_q])
ig = inj.groupby("Subject").agg(head=("_head", "any"), blast=("_blast", "any"))
cohort["Head/neck injury, any (lifetime, self-report)"] = (ig["head"].sum(), len(ig))
cohort["Blast / explosion exposure"] = (ig["blast"].sum(), len(ig))

# --- Family history of neurodegeneration  (Family History) ---
fh = xl.parse("Family History")
als_q = [c for c in fh.columns if "ALS or other neuromuscular" in c][0]
dem_q = [c for c in fh.columns if "Alzheimer" in c][0]
wi_q = [c for c in fh.columns if "Other - Write In" in c][0]
fh["_als"] = is_yes(fh[als_q])
fh["_dem"] = is_yes(fh[dem_q])
fh["_park"] = fh[wi_q].astype(str).str.contains("parkin", case=False, na=False)
fg = fh.groupby("Subject").agg(als=("_als", "any"), dem=("_dem", "any"),
                               park=("_park", "any"))
cohort["Family history of ALS / other neuromuscular disease"] = (fg["als"].sum(), len(fg))
cohort["Family history of Alzheimer's / other dementia"] = (fg["dem"].sum(), len(fg))
cohort["Family history of Parkinson's disease (write-in)"] = (fg["park"].sum(), len(fg))

# --- Self-reported conditions, ever diagnosed  (Conditions 1) ---
cond = xl.parse("Conditions 1")
def cond_col(name):
    return [c for c in cond.columns if c.endswith("- " + name)][0]

autoimmune_items = ["Rheumatoid arthritis", "Systemic lupus erythematosus",
                    "Multiple sclerosis", "Psoriasis", "Crohn's disease",
                    "Ulcerative colitis", "Behcet's disease",
                    "Neuromyelitis optica",
                    "Idiopathic thrombocytopenic purpura"]
# NOTE: Asthma is deliberately NOT in the autoimmune composite. Asthma is a chronic
# Type-2 (Th2) inflammatory airway disease, not an autoimmune disease (no self-tissue
# attack / autoantibodies as the defining mechanism). It is reported on its own row.
cond["_asthma"] = is_yes(cond[cond_col("Asthma")])
cond["_thyroid"] = is_yes(cond[cond_col("Thyroid disease")])
cond["_auto"] = cond[[cond_col(x) for x in autoimmune_items]].apply(
    lambda r: is_yes(r).any(), axis=1)
cond["_auto_thy"] = cond["_auto"] | cond["_thyroid"]
cond["_park_self"] = cond[cond_col("Other - Write In")].astype(str).str.contains(
    "parkin", case=False, na=False)
cg = cond.groupby("Subject").agg(
    asthma=("_asthma", "any"), thyroid=("_thyroid", "any"),
    auto=("_auto", "any"), auto_thy=("_auto_thy", "any"),
    park=("_park_self", "any"))
cohort["Asthma, ever (physician-diagnosed)"] = (cg["asthma"].sum(), len(cg))
cohort["Autoimmune disease, any (excl. thyroid)"] = (cg["auto"].sum(), len(cg))
cohort["Autoimmune disease, any (incl. thyroid)"] = (cg["auto_thy"].sum(), len(cg))
cohort["Thyroid disease, ever"] = (cg["thyroid"].sum(), len(cg))
cohort["Parkinson's disease, self (write-in)"] = (cg["park"].sum(), len(cg))

# ---------------------------------------------------------------------------
# 2. GENERAL-POPULATION BENCHMARKS  (value as %, with source string)
#    "lower"/"upper" give the plausible range; "pop" is the headline figure.
# ---------------------------------------------------------------------------
benchmark = {
 "Smoking, ever (>=1 cig/day for 6+ months)": dict(
    pop=30.0, rng="~30% (current ~12% + former ~18-20%)",
    src="CDC NHIS / Health, United States (current cigarette smoking 11.6%, 2022)"),
 "Vigorous leisure-time physical activity, ever": dict(
    pop=np.nan, rng="no direct analog; CDC current adherence ~46% aerobic, ~24% both",
    src="CDC NCHS, Physical Activity Among Adults, NHIS 2020/2022"),
 "Military service (ever member of armed forces)": dict(
    pop=6.1, rng="6.1% of U.S. ADULTS (18+), not total population; "
                 "but ~half of veterans are 65+ and ~89% are men, so the age/sex-matched "
                 "expectation for an older, mostly-male cohort is well above 6.1%",
    src="Pew Research 2023 (6% of adults); RAND 2025 / USAFacts (6.1% of adults); U.S. Census ACS 2023"),
 "Head/neck injury, any (lifetime, self-report)": dict(
    pop=18.2, rng="12-18% (TBI with LOC); up to ~30-40% broadest 'any TBI'",
    src="Seifi et al., Neuroepidemiology 2024 (18.2%); CDC self-report review 19-29%"),
 "Blast / explosion exposure": dict(
    pop=np.nan, rng="rare in civilians; concentrated in military/occupational",
    src="No national civilian benchmark; predominantly service-related"),
 "Family history of ALS / other neuromuscular disease": dict(
    pop=8.0, rng="expected familial-ALS proportion in case series ~5-11%; general-pop ALS lifetime risk ~0.3% (1 in 300)",
    src="Ryan et al., Neurology Genetics 2023 (fALS 5-11%); Al-Chalabi, Nature 2017 (1/300)"),
 "Family history of Alzheimer's / other dementia": dict(
    pop=np.nan, rng="no standard family-history benchmark; dementia common in aging relatives",
    src="Not cleanly benchmarkable (see notes)"),
 "Asthma, ever (physician-diagnosed)": dict(
    pop=13.0, rng="~13% lifetime ('ever told'); current asthma ~7.7%",
    src="CDC Asthma Data, BRFSS/NHIS 2021-2022"),
 "Autoimmune disease, any (excl. thyroid)": dict(
    pop=4.6, rng="4.6% any of 105 autoimmune dx (EHR); older estimate 7.6-9.4%",
    src="Conrad/Fairweather et al., JCI 2025 (4.6%); NASEM 2022 (7.6-9.4%)"),
 "Autoimmune disease, any (incl. thyroid)": dict(
    pop=np.nan, rng="thyroid disease alone ~12%, so composite not comparable to 4.6%",
    src="See thyroid row"),
 "Thyroid disease, ever": dict(
    pop=12.0, rng="~12% (any thyroid disease, lifetime)",
    src="General clinical estimate; thyroid was a top-5 autoimmune dx in JCI 2025"),
 "Parkinson's disease, self (write-in)": dict(
    pop=0.5, rng="~0.3-0.5% of adults; ~1% at age 60, ~4% by 80",
    src="Parkinson's Foundation / Marras et al. 2018; CDC"),
 "Family history of Parkinson's disease (write-in)": dict(
    pop=np.nan, rng="soft benchmark; ~3-5% of adults have a relative with PD",
    src="Derived from PD prevalence (~1% at 60); no standard family-history figure"),
}

# Per-component autoimmune benchmarks (for the breakdown table)
component_benchmark = {
 "Rheumatoid arthritis": (1.0, "~0.5-1% clinical (CDC/NHANES)"),
 "Systemic lupus erythematosus": (0.1, "~0.1% (CDC/Lupus Foundation)"),
 "Multiple sclerosis": (0.3, "~0.3% (Nat'l MS Society)"),
 "Psoriasis": (3.0, "~3% of adults (CDC/AAD)"),
 "Crohn's disease": (0.6, "Crohn ~0.6% (CDC IBD; IBD combined ~1.3%)"),
 "Ulcerative colitis": (0.7, "UC ~0.7% (CDC IBD; IBD combined ~1.3%)"),
 "Thyroid disease": (12.0, "~12% any thyroid disease"),
}

# ---------------------------------------------------------------------------
# 3. BUILD COMPARISON TABLE
# ---------------------------------------------------------------------------
rows = []
for label, (npos, ntot) in cohort.items():
    pct = round(100 * npos / ntot, 1)
    b = benchmark.get(label, {})
    pop = b.get("pop", np.nan)
    if np.isnan(pop):
        direction = "not directly comparable"
        ratio = np.nan
    else:
        ratio = round(pct / pop, 1)
        if pct >= 1.5 * pop:
            direction = "HIGHER than population"
        elif pct <= 0.67 * pop:
            direction = "lower than population"
        else:
            direction = "similar to population"
    rows.append(dict(
        risk_factor=label,
        cohort_pct=pct, cohort_n=f"{npos}/{ntot}",
        population_pct=("" if np.isnan(pop) else pop),
        ratio_cohort_to_pop=("" if np.isnan(ratio) else ratio),
        direction=direction,
        population_range=b.get("rng", ""),
        source=b.get("src", ""),
    ))

table = pd.DataFrame(rows)
table.to_csv("risk_factor_vs_population.csv", index=False)

pd.set_option("display.max_colwidth", 44)
pd.set_option("display.width", 200)
print(table[["risk_factor", "cohort_pct", "cohort_n",
             "population_pct", "ratio_cohort_to_pop", "direction"]].to_string(index=False))

# Autoimmune component breakdown
print("\n--- Autoimmune components (self-report, Conditions module) ---")
comp_rows = []
for item, (pop, src) in component_benchmark.items():
    col = cond_col(item)
    sub = ever_by_subject(cond, col)
    pct = round(100 * sub.sum() / len(sub), 1)
    comp_rows.append(dict(condition=item, cohort_pct=pct,
                          cohort_n=f"{sub.sum()}/{len(sub)}",
                          population_pct=pop, source=src))
comp = pd.DataFrame(comp_rows)
comp.to_csv("autoimmune_components.csv", index=False)
print(comp.to_string(index=False))
