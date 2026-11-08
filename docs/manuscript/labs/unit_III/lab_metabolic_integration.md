# Lab — Metabolic Integration and Regulation {#sec:lab_unit_III_metabolic_integration .unnumbered}

*This activity accompanies \cref{sec:unit_III_metabolic_integration} of the textbook.*

## Learning Objectives {.unnumbered}

- Trace insulin signaling while distinguishing resistance from secretion evidence.
- Estimate allosteric K0.5 from supplied PFK dose data.
- Calculate a local flux-response coefficient and its limits.
- Compute energy charge and connect it to AMPK regulation.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO4):** Trace insulin signaling while distinguishing resistance from secretion evidence.
- **Outcome 2 (LO1):** Estimate baseline-corrected allosteric K0.5 from supplied PFK dose data and explain F2,6BP cross-regulation.
- **Outcome 3 (LO13):** Calculate a local flux-response coefficient and its limits.
- **Outcome 4 (LO14):** Compute energy charge and connect it to AMPK regulation.
- **Chapter LO coverage:** LO1, LO4, LO13, LO14
- **Rubric (20 points total):**
  - **Evidence — 8 points (LO1, LO4, LO13, LO14):** Award 2 for trapezoidal total AUC and baseline-subtracted iAUC for A/B/C with mM·min units, 2 for PFK means and interpolation at the baseline-corrected half-increment 42.5, 2 for both energy charges with all adenylates in the denominator, and 2 for C≈(2/50)/(10/100)=0.4. Correct method can earn half of a component after a numerical error; raw ΔJ/ΔE alone is not the normalized coefficient.
  - **Controls — 3 points (LO1, LO4):** Award 1 for comparing insulin with vehicle and insulin+inhibitor with insulin, 1 for using inhibitor alone to check an independent output effect and proposing viability/Akt measurements to test the strongest alternative, and 1 for holding enzyme amount, ATP and pH fixed in the PFK activator-dose comparison. Do not treat reduced output as proof of a single transcription-factor mechanism.
  - **Uncertainty — 3 points (LO1, LO4, LO14):** Award 1 for distinguishing one subject/five repeated times from between-subject replication and withholding diagnostic/secretion-versus-resistance claims from glucose alone, 1 for identifying the K0.5 value as an endpoint-dependent linear interpolation rather than a uniquely fitted constant, and 1 for distinguishing an adenylate-based AMPK prediction from measured kinase activity.
  - **Mechanism — 4 points (LO1, LO4, LO14):** Award 2 for explaining why the insulin/inhibitor contrasts support PI3K participation without proving sole causation, 1 for the hepatic insulin→PFK-2 dephosphorylation→F2,6BP→PFK activation link with isoform scope stated, and 1 for connecting lower energy charge to favored AMPK activation rather than to ATP concentration alone.
  - **Transfer — 2 points (LO13):** Award 1 for explaining why the local 10% enzyme perturbation cannot justify a large-perturbation or other-tissue coefficient, and 1 for explaining how steady glucose concentration can coexist with increased production when removal also increases. Flux is a rate; a metabolite pool is not a direct flux measurement.
- **Coverage limit:** The fixed-enzyme activator-dose series assesses allosteric cross-regulation (part of LO1), not the LO6 activity-time-course distinction between allosteric and transcriptional regulation. No RNA/expression or activity time-course contrast is supplied here, so this lab does not claim LO6 coverage.
<!-- lab-alignment-end -->

## Lab Context: Metabolic Integration and Regulation {.unnumbered}

All numeric observations and sequence/assay cards below are **synthetic teaching evidence**, not patient results or empirical measurements, unless a card explicitly names an official or primary source. No external packet, live lookup, equipment, or software is required.

## Paper-Based Materials {.unnumbered}

Print this complete activity; use pencil, ruler, graph paper, and calculator. Work in pairs but record independent conclusions.

## Printed Evidence Packet {.unnumbered}

### State and signal cards {.unnumbered}

Synthetic independent hepatocyte preparations n=3 per arm; normalized glucose output per hour (vehicle=100), fixed substrate supply and equal viable protein.

: State and signal cards {#tbl:unit_III_metabolic_integration_alignment_and_rubric_map}
| Treatment | Replicate1 | Replicate2 | Replicate3 |
| --- | --- | --- | --- |
| Vehicle | 98 | 100 | 102 |
| Insulin | 58 | 60 | 62 |
| Insulin + PI3K inhibitor | 93 | 95 | 97 |
| Inhibitor alone | 101 | 103 | 105 |

Adenylates in one synthetic matched extract (mM): resting ATP3,ADP1,AMP0.2; stressed ATP1,ADP2,AMP1. No patient is represented. AMPK contains one α,one β,one γ subunit.

### Descriptive glucose challenge {.unnumbered}

Synthetic single-subject trajectories: n=1 per profile, five repeated measurements, 75g modeled oral glucose after overnight fasting. Labels A/B/C are profiles, not diagnosed cohorts.

: Descriptive glucose challenge {#tbl:unit_III_metabolic_integration_part_3_allosteric_regulation_modeling}
| Time min | A glucose mM | B glucose mM | C glucose mM |
| --- | --- | --- | --- |
| 0 | 4.5 | 5.7 | 7.0 |
| 30 | 6.8 | 9.2 | 12.4 |
| 60 | 5.9 | 8.5 | 13.1 |
| 90 | 5.1 | 7.3 | 11.8 |
| 120 | 4.6 | 6.4 | 10.5 |

Use total AUC=sum[(Gi+Gi+1)/2×30min]. No AUC diagnostic threshold is supplied or validated. Glucose alone does not identify insulin secretion versus resistance.

### PFK and local control {.unnumbered}

Synthetic purified hepatic PFK activity; fixed ATP,pH and enzyme concentration; three independently prepared assays per dose. Units nmol product/min/mg; fructose-2,6-BP in µM.

: PFK and local control {#tbl:unit_III_metabolic_integration_part_3_allosteric_regulation_modeling_2}
| F2,6BP µM | Replicate1 | Replicate2 | Replicate3 |
| --- | --- | --- | --- |
| 0 | 9 | 10 | 11 |
| 1 | 25 | 26 | 27 |
| 2 | 35 | 36 | 37 |
| 5 | 49 | 50 | 51 |
| 10 | 59 | 60 | 61 |

Model endpoints v0=10,vmax=75. K0.5 means half the *increment* above baseline: v=42.5. At5µM activator an enzyme-abundance perturbation E100→110 arbitrary units gives pathway steady flux J50→52 µmol/min (same tissue/condition); use finite difference C≈(ΔJ/J)/(ΔE/E).

**Energy bookkeeping inputs:** Energy charge $EC=(ATP+0.5ADP)/(ATP+ADP+AMP)$. Complete oxidation of one C16 palmitoyl-CoA gives 7 β-oxidation cycles (7 NADH and 7 FADH2) and 8 acetyl-CoA; each acetyl-CoA's TCA cycle gives 3 NADH, 1 FADH2 and 1 GTP. Count 2.5 ATP/NADH, 1.5 ATP/FADH2 and 1 ATP/GTP. Starting from free palmitate costs 2 ATP equivalents for activation. These are stipulated effective-yield assumptions, not a measured tissue ATP output.

## Paper-Based Investigation {.unnumbered}

1. Calculate total trapezoidal AUCs and baseline-subtracted incremental AUCs ($iAUC=AUC-G_0\times120$ min). State why neither between-subject SEM nor group ANOVA is supported by one subject per profile.

2. Compare insulin, inhibitor and inhibitor-alone means. Name one alternative explanation and a measurement that tests it; do not equate output with a single transcription factor.

3. Plot PFK means and interpolate K0.5 between 2 and 5 µM. Trace hepatic insulin→PFK-2 dephosphorylation→F2,6BP, and distinguish this isoform from cardiac regulation.

4. Calculate both energy charges, the finite-difference flux coefficient, and ATP yield from palmitoyl-CoA versus free palmitate at P/O2.5/1.5.

## Data Recording {.unnumbered}

Record each calculation with units, the comparison/control, and one alternative explanation. Show intermediate steps; use a separate column for observed card evidence versus inferred mechanism.

## Paper-Based Evidence Upgrade {.unnumbered}

Total AUC is descriptive and baseline-dependent, not a validated diagnosis. No secretion/resistance conclusion follows from glucose alone; paired insulin/C-peptide and controlled sensitivity measurements would help. Three purified assays estimate assay variability, not human variability. Source card: synthetic fixed-compartment teaching model; flux is not metabolite pool size and local control need not extrapolate to large perturbations.

## Analysis Questions {.unnumbered}

Explain which result supports the proposed mechanism, which result would falsify it, and what additional measurement would discriminate the strongest alternative. Apply the mechanism to a new tissue, genotype, or condition without treating synthetic observations as clinical evidence.

> **Concept Check:** How can hepatic glucose concentration remain constant while glucose production rises, and why can a glucose-only curve not identify insulin secretion?

## Instructor Key and Scoring Expectations {.unnumbered}

### Worked Results and Interpretation {.unnumbered}

<!-- SOLUTION
AUC A/B/C=670.5/931.5/1381.5 mM·min. Subtract initial glucose×120 min: incremental AUC 130.5/247.5/541.5. Timepoints are dependent repeated measurements; n=1 per profile cannot estimate between-subject SEM or perform group ANOVA. Insulin means 100→60; insulin+inhibitor 95 and inhibitor-alone 103 support PI3K participation, not sole causation; assess viability and Akt phosphorylation. PFK means 10,26,36,50,60: linear interpolation at 42.5 gives 2+(6.5/14)×3≈3.39 µM; a fitted nonlinear model could differ, so report interpolation. Hepatic insulin promotes PFK-2 dephosphorylation and increased F2,6BP. EC=(ATP+0.5ADP)/(ATP+ADP+AMP): resting 3.5/4.2=0.8333; stressed 2/4=0.5. Lower EC favors AMPK, but nucleotide pools are not kinase-activity measurements. Local C=(2/50)/(10/100)=0.4, not a universal coefficient. Palmitoyl-CoA yields 80+10.5+17.5=108; free palmitate activation subtracts 2=106 ATP. See \cref{sec:unit_III_metabolic_integration}.
SOLUTION -->

## Safety and Ethics Notes {.unnumbered}

Required work is paper-only: no cultures, reagents, biological samples, medical decisions, or participant data collection. Optional wet/equipment extensions require institutional protocols and separate approval; they are not needed to complete or score this activity.
