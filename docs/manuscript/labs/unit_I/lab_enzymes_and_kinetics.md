# Lab — Enzymes and the Kinetics of Catalysis {#sec:lab_unit_I_enzymes_and_kinetics .unnumbered}


## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_I_enzymes_and_kinetics} of the textbook — review that chapter before attempting the exercises below.*

- Interpret enzyme activity data by tracking O₂ production as a proxy for reaction rate
- Compare temperature, pH and substrate responses without mistaking a sampled maximum for Vmax
- Construct a rate vs $[\mathrm{S}]$ curve and identify qualitative Km
- Interpret enzyme inhibition from a competitive inhibitor treatment



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO5):** Calculate replicate means/ranges across temperature and pH.
- **Outcome 2 (LO2):** Infer half-response concentration and rate saturation with explicit proxy units.
- **Outcome 3 (LO3):** Distinguish two synthetic inhibition patterns using high-substrate controls.
- **Outcome 4 (LO7):** Separate a reaction annotation from organism-specific measured kinetics.
- **Chapter LO coverage:** LO2, LO3, LO5, LO7
- **Rubric dimensions:** 12 points: replicate arithmetic and independent-unit definition (LO5, 3); kinetic estimates and proxy limitations (LO2, 3); inhibitor comparison and mechanism uncertainty (LO3, 3); provenance fields, missing empirical evidence and transfer (LO7, 3).
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define Km (the Michaelis constant) and Vmax (the maximum reaction velocity) in the Michaelis–Menten framework, and state the operational meaning of Km as the substrate concentration at which the reaction velocity is half of Vmax.
2. Sketch in words the shape of a Michaelis–Menten v-versus-$[\mathrm{S}]$ curve. Apply the equation v = Vmax · $[\mathrm{S}]$ / (Km + $[\mathrm{S}]$) to explain why the curve approaches Vmax asymptotically and why doubling $[\mathrm{S}]$ far above Km has little effect on v.
3. Compare ideal competitive and pure noncompetitive inhibition models: predict their apparent Km and Vmax changes. Explain why an allosteric binding site alone does not establish a pure noncompetitive kinetic pattern.

## Lab Context: Enzymes and the Kinetics of Catalysis {.unnumbered}

Enzymes are biological catalysts that lower activation barriers. Catalase converts hydrogen peroxide to water and oxygen: **2 H₂O₂ → 2 H₂O + O₂**. Gas production can serve as a reaction-rate proxy under controlled assay conditions; a turnover value requires an organism, enzyme preparation and specified assay, not a universal catalase constant.

In this lab you will analyze a paper dataset showing how temperature, pH, substrate concentration, and inhibition affect catalase activity. The goal is to infer mechanism from controlled comparisons rather than to run a wet reaction.

The parent chapter's DHFR example (\cref{sec:unit_I_enzymes_and_kinetics}) illustrates how apparent Km changes depend on inhibitor concentration and the chosen substrate concentration. Here E2 supplies explicit hypothetical Michaelis–Menten parameters; the exercise does not establish that real catalase follows those models or that a kinetic pattern identifies a physical binding site.

## Paper-Based Materials {.unnumbered}

: Printed enzyme investigation materials. {#tbl:unit_I_enzymes_and_kinetics_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Enzymes and the Kinetics of Catalysis: BRENDA enzyme-entry card with EC number, organism, kinetic field, ligand, reference, and release date | 1 |
| Pathway provenance cards comparing one KEGG pathway map and one BioCyc pathway/genome entry for the same catalase or peroxide-detoxification reaction | 1 set |
| Catalase activity dataset with three replicates per condition | 1 |
| Enzyme-structure and active-site cards | 1 set |
| Michaelis-Menten curve worksheet | 1 |
| Inhibitor scenario cards | 1 set |
| Ruler (mm) | 1 |
| Calculator and graph paper | 1 each |

## Paper-Based Investigation {.unnumbered}

**Part A — Temperature Effect**

1. Plot the provided catalase-rate data for 0°C, 22°C, 37°C, 50°C, and denatured enzyme conditions.
2. Calculate the mean and range for each condition. Identify the denatured enzyme as a negative control and the 37°C condition as a reference comparison.
3. Use the active-site cards to explain why low temperature and denaturation reduce activity for different reasons.

**Part B — pH Effect**

4. Graph the printed pH series (2.5, 5, 7, 8.5, 11) and identify its sampled maximum.
5. Use E3 to distinguish possible catalytic-protonation, substrate and folding explanations. State why rate data alone cannot select among them and name a discriminating control.

**Part C — Substrate Concentration Effect**

6. Plot rate versus [H₂O₂] for 0%, 1%, 3%, and 6% substrate.
7. Using E2's stipulated models, identify half-Vmax and calculate the fraction of Vmax reached at 6%. Does the printed series demonstrate a plateau? Compare both inhibitor curves and specify additional substrate concentrations and controls needed before inferring an asymptote without supplied parameters.

## Data Recording {.unnumbered}

: Recording sheet for the synthetic temperature, pH and substrate series. {#tbl:unit_I_enzymes_and_kinetics_alignment_and_rubric_map_2}
| Condition | Temperature (°C) | pH | [H₂O₂] (%) | Simulated O₂ proxy at 60 s |
| --------- | ----------------- | -- | ----------- | ------------------------- |
| Ice bath | 0 | 7 | 3 | |
| Room temp | 22 | 7 | 3 | |
| Reference temperature | 37 | 7 | 3 | |
| Warm bath | 50 | 7 | 3 | |
| Denatured enzyme | 22 | 7 | 3 | |
| Acid (pH 2.5) | 22 | 2.5 | 3 | |
| Mild acid (pH 5) | 22 | 5 | 3 | |
| Neutral (pH 7) | 22 | 7 | 3 | |
| Alkaline (pH 8.5) | 22 | 8.5 | 3 | |
| Alkaline (pH 11) | 22 | 11 | 3 | |
| $[\mathrm{S}]$ 0% | 22 | 7 | 0 | |
| $[\mathrm{S}]$ 1% | 22 | 7 | 1 | |
| $[\mathrm{S}]$ 3% | 22 | 7 | 3 | |
| $[\mathrm{S}]$ 6% | 22 | 7 | 6 | |

## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Measure reaction-rate proxies and compare inhibition scenarios.
- **Data skill to practice:** Fit or interpret enzyme-rate data and identify which parameter changed.
- **BioSkills emphasis:** Quantitative reasoning, Interdisciplinary nature of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Enzymes and the Kinetics of Catalysis** with a reproducibility pass:

: Evidence, controls and reproducibility decisions. {#tbl:unit_I_enzymes_and_kinetics_alignment_and_rubric_map_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: treat the activity-versus-temperature series as a dose-response curve whose optimum and denaturation endpoints are the claims; the denatured-enzyme and no-enzyme conditions are the controls that decide whether a low signal means lost catalysis or a failed assay. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Michaelis–Menten rate at two substrate levels {.unnumbered}

**Problem:** In a stipulated Michaelis–Menten teaching model, Vmax = 120 nmol·min⁻¹ and Km = 2.5 mM. These are assigned parameters, not assay measurements. Compute the initial velocity v at $[\mathrm{S}]$ = 5 mM and at $[\mathrm{S}]$ = Km. Then estimate the fold change in v as substrate rises from Km to 5·Km.

**Solution:** Apply v = Vmax · $[\mathrm{S}]$ / (Km + $[\mathrm{S}]$).

- At $[\mathrm{S}]$ = 5 mM: v = 120 · 5 / (2.5 + 5) = 120 · 5 / 7.5 = 80 nmol·min⁻¹.
- At $[\mathrm{S}]$ = Km = 2.5 mM: v = 120 · 2.5 / (2.5 + 2.5) = 120 · 0.5 = 60 nmol·min⁻¹ (exactly half of Vmax, as expected).
- At $[\mathrm{S}]$ = 5·Km = 12.5 mM: v = 120 · 12.5 / (2.5 + 12.5) = 120 · 12.5 / 15 = 100 nmol·min⁻¹. Going from $[\mathrm{S}]$ = Km to $[\mathrm{S}]$ = 5·Km raises v from 60 to 100 nmol·min⁻¹, a 1.67-fold increase — modest compared with the fivefold rise in substrate.

**Interpretation:** In this stipulated Michaelis–Menten model, fractional rate responds to substrate concentration, while far above Km further substrate additions have diminishing effects. This does not establish a biological rule that cells maintain $[\mathrm{S}]$=Km or identify which enzymes control cellular flux. For the printed parameters, reaching 90% of Vmax requires $[\mathrm{S}]$=9·Km=22.5 mM; reaching within 10% requires at least this concentration.


### Source-Governance Checkpoint {.unnumbered}

**Printed packet E1 — synthetic teaching data, not measured catalase kinetics.** Each triple represents three independently prepared model assays, not three timepoints in one tube. Fixed enzyme amount and 60 s initial-rate window; readout is O2-equivalent proxy units/min with resolution 1 unit. Means/ranges are descriptive only. At pH7 and 3% substrate, temperature triples are 0 degrees C: 14,15,16; 22:59,60,61; 37:89,90,91; 50:29,30,31; pre-denatured at 22:0,0,0; no enzyme:0,0,0. At 22 degrees C/3% substrate, pH triples are 2.5:2,3,4; 5:29,30,31; 7:59,60,61; 8.5:39,40,41; 11:1,2,3.

**Substrate card E2:** Percent means g H2O2 per 100 mL in this illustration, not molarity. At substrate 0,1,3,6%, untreated mean rates are 0,30,60,80; competitive-model inhibitor means 0,12,30,48; reduced-capacity-model inhibitor means 0,15,30,40. For every nonzero mean the triplicates are mean-1,mean,mean+1; zero is 0,0,0. Underlying models are untreated Vmax=120, Km=3%; competitive Vmax=120, apparent Km=9%; reduced capacity Vmax=60, Km=3%. These are hypothetical enzymes with MM-like kinetics, not validated catalase inhibitor identities. Catalase may depart from this model at high peroxide.

**Active-site cards E3:** Cold assay: folded enzyme retained, slower reaction; pre-denatured: altered fold, inactive pocket; extreme-pH low signal: either altered catalytic protonation or fold/substrate effects, not distinguishable from rate alone. A separate fold or recovery assay is needed.

**Provenance cards E4 (authored summaries, not fabricated database exports):** BRENDA-style record: EC1.11.1.6 catalase; reaction 2H2O2 -> 2H2O+O2; E1 has no empirical organism, accession or source paper and cannot be entered as a measured kinetic value. KEGG-style pathway view places peroxide removal in a network but does not supply flux. BioCyc-style organism/genome view links a reaction to an annotated gene only for a specified organism/release. Neither view establishes the E1 rates. These source roles are discussed in \citep{hauenstein2026brenda,kegg2026,biocyc2026}; no live lookup is required.

**Instructor key:** Temperature means are 15,60,90,30,0; ranges are 2 except denatured 0. The observed optimum is 37 among sampled conditions, not a universal optimum. pH means 3,30,60,40,2 with ranges 2. Untreated half-Vmax=60 occurs at 3%; 6% gives only 2/3 Vmax, so a true plateau has not been demonstrated. At 3% both inhibitor models yield 30 and cannot be distinguished; at 6% the 48 versus 40 comparison helps, but broader substrate range and uncertainty estimates are required. A competitive model is not proof of physical active-site binding. In synthesis, doubling Km at S=Km changes v from Vmax/2 to Vmax/3 (one-third reduction); S=2Km restores Vmax/2, or 1.5-fold enzyme abundance restores the original rate at fixed S. Governance: E1–E4 are authored synthetic teaching cards, no database release of measured numbers; refresh if assay window, proxy calibration or organism changes.

## Analysis Questions {.unnumbered}

1. Compare the synthetic temperature means and ranges. Identify the sampled optimum and distinguish the cold folded-enzyme card from the pre-denatured control. The packet contains no observations above 50°C; do not infer an unmeasured high-temperature trajectory.
2. Explain why the denatured-enzyme condition showed no activity using the concept of protein denaturation and active site geometry.
3. Compare the largest observed rate with E2's stipulated Vmax. Calculate the fraction reached at 6% and explain why an increasing, flattening curve is not itself evidence that a plateau has been reached.
4. Compare the two explicit E2 inhibition models. State their apparent Km and Vmax, the substrate condition where their predictions coincide, and which printed high-substrate comparison distinguishes them. Do not infer binding location from these curves alone.
5. Explain what the synthetic packet illustrates about peroxide-clearance capacity and what biochemical or patient evidence would be needed to connect it to catalase deficiency. The printed model assays are not clinical observations or proof of a patient's disease mechanism.

## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Assume an illustrative MM-like cellular enzyme model with substrate held at $[\mathrm{S}]\approx K_m$. A candidate-drug response is modeled by doubling apparent Km without changing Vmax. This is a stipulated competitive-model pattern, not a measured cellular condition or proof of physical binding location.
>
> (a) Compute the predicted fractional change in v caused by the drug at the normal cellular $[\mathrm{S}]$ (use v = Vmax·$[\mathrm{S}]$/(Km+$[\mathrm{S}]$) before and after the Km doubling), and interpret why an enzyme operating at $[\mathrm{S}]$ ≈ Km is particularly sensitive to a Km-shifting inhibitor.
> (b) Predict how the cell could partly compensate metabolically. Evaluate two routes: a homeostatic rise in $[\mathrm{S}]$ that restores the original v, and a compensatory increase in enzyme expression that raises effective Vmax. Quantify the $[\mathrm{S}]$ that would restore the original v under the doubled Km, and discuss which compensation is more plausible on a short time scale.
> (c) Design a paper-data experiment using the lab's rate-versus-substrate format to distinguish this competitive model from a reduced-capacity model that lowers Vmax without changing Km. State the diagnostic comparison and an uncertainty criterion; those kinetic patterns alone do not identify an allosteric binding site.

## Optional Wet-Lab Extension {.unnumbered}

An instructor may demonstrate catalase activity with approved materials after a safety briefing. The required lab remains the paper dataset and the mechanistic interpretation of controls, rate curves, and inhibition.

## Safety and Ethics Notes {.unnumbered}

Paper-based lab — no hydrogen peroxide, heating, or biological samples are required. Optional wet demonstrations require instructor supervision and appropriate eye and skin protection.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group
comparing results and discussing the following prompts. Each member should
contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to
   the textbook's predictions. Where they diverge, suggest at least one
   mechanistic explanation before concluding "experimental error."
2. **What would change the outcome** — propose one modification to the
   procedure that would sharpen the measurement or extend the result to a
   new biological context, and predict what you would observe.
3. **One-sentence headline** — each student composes a single sentence
   summarizing the lab's take-home message, suitable for a tweet. Compare
   sentences across groups; good headlines are short, quantitative, and
   mechanistic.
4. **Connection back to the textbook** — identify one section of
   \cref{sec:unit_I_enzymes_and_kinetics} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_I_enzymes_and_kinetics} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `docs/manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_I_enzymes_and_kinetics}`; all numerical
quantities in this lab use SI units — see \nameref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
