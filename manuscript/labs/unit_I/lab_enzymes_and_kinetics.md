# Lab — Enzymes and the Kinetics of Catalysis {.unnumbered}

\label{sec:lab_unit_I_enzymes_and_kinetics}

## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_I_enzymes_and_kinetics} of the textbook — review that chapter before attempting the exercises below.*

- Interpret enzyme activity data by tracking O₂ production as a proxy for reaction rate
- Determine how temperature, pH, and substrate concentration affect enzyme rate (Vmax approximation)
- Construct a rate vs [S] curve and identify qualitative Km
- Interpret enzyme inhibition from a competitive inhibitor treatment



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Enzymes and the Kinetics of Catalysis.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define Km (the Michaelis constant) and Vmax (the maximum reaction velocity) in the Michaelis–Menten framework, and state the operational meaning of Km as the substrate concentration at which the reaction velocity is half of Vmax.
2. Sketch in words the shape of a Michaelis–Menten v-versus-[S] curve. Apply the equation v = Vmax · [S] / (Km + [S]) to explain why the curve approaches Vmax asymptotically and why doubling [S] far above Km has little effect on v.
3. Compare competitive inhibition (where an inhibitor binds the active site) and allosteric (non-competitive) inhibition that reduces effective enzyme activity by binding elsewhere. For each, predict the qualitative effect on the apparent Km and apparent Vmax measured from a v-versus-[S] curve.

## Lab Context: Enzymes and the Kinetics of Catalysis {.unnumbered}

Enzymes are biological catalysts that lower activation energy. The enzyme catalase converts hydrogen peroxide (H₂O₂) to water and oxygen: **2 H₂O₂ → 2 H₂O + O₂**. This reaction is often monitored by counting O₂ bubbles per minute or by measuring the height of foam produced. Catalase is one of the fastest known enzymes (k_cat ~40,000,000 s⁻¹) and is found in most aerobic organisms.

In this lab you will analyse a paper dataset showing how temperature, pH, substrate concentration, and inhibition affect catalase activity. The goal is to infer mechanism from controlled comparisons rather than to run a wet reaction.

The quantitative DHFR inhibition worked example in the parent chapter (\cref{sec:unit_I_enzymes_and_kinetics}) shows how competitive-inhibitor binding reduces apparent reaction rate: at [MTX] = 10$\times$ its $K_i$, the apparent $K_m$ rises 11-fold, cutting velocity by about 62%. This lab applies the same kinetic reasoning to catalase: students extract a qualitative $K_m$ and predict inhibition from competition.

## Paper-Based Materials {.unnumbered}

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

4. Graph catalase rate across pH 2.5, 5, 7, 8.5, and 11. Mark the pH optimum and one condition where enzyme structure is likely disrupted.
5. Decide whether pH changes primarily affect enzyme shape, substrate charge, or both. Support the claim with one pattern in the dataset.

**Part C — Substrate Concentration Effect**

6. Plot rate versus [H₂O₂] for 0%, 1%, 3%, and 6% substrate.
7. Estimate the concentration where the curve begins to plateau and label it as a qualitative Vmax region. Use the inhibitor cards to predict how a competitive inhibitor would change apparent Km and Vmax.

## Data Recording {.unnumbered}

| Condition | Temperature (°C) | pH | [H₂O₂] (%) | Simulated O₂ proxy at 60 s |
| --------- | ----------------- | -- | ----------- | ------------------------- |
| Ice bath | 0 | 7 | 3 | |
| Room temp | 22 | 7 | 3 | |
| Warm bath | 50 | 7 | 3 | |
| Denatured enzyme | 22 | 7 | 3 | |
| Acid (pH 2.5) | 22 | 2.5 | 3 | |
| Neutral (pH 7) | 22 | 7 | 3 | |
| Alkaline (pH 8.5) | 22 | 8.5 | 3 | |
| [S] 0% | 22 | 7 | 0 | |
| [S] 1% | 22 | 7 | 1 | |
| [S] 3% | 22 | 7 | 3 | |
| [S] 6% | 22 | 7 | 6 | |

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Measure reaction-rate proxies and compare inhibition scenarios.
- **Data skill to practice:** Fit or interpret enzyme-rate data and identify which parameter changed.
- **BioSkills emphasis:** Quantitative reasoning, Interdisciplinary nature of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Enzymes and the Kinetics of Catalysis** with a reproducibility pass:

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

**Problem:** An enzyme has Vmax = 120 nmol·min⁻¹ and Km = 2.5 mM, measured under standard assay conditions. Compute the initial velocity v at [S] = 5 mM and at [S] = Km. Then estimate the fold change in v as [S] rises from Km to 5·Km.

**Solution:** Apply v = Vmax · [S] / (Km + [S]).

- At [S] = 5 mM: v = 120 · 5 / (2.5 + 5) = 120 · 5 / 7.5 = 80 nmol·min⁻¹.
- At [S] = Km = 2.5 mM: v = 120 · 2.5 / (2.5 + 2.5) = 120 · 0.5 = 60 nmol·min⁻¹ (exactly half of Vmax, as expected).
- At [S] = 5·Km = 12.5 mM: v = 120 · 12.5 / (2.5 + 12.5) = 120 · 12.5 / 15 = 100 nmol·min⁻¹. Going from [S] = Km to [S] = 5·Km raises v from 60 to 100 nmol·min⁻¹, a 1.67-fold increase — modest compared with the fivefold rise in substrate.

**Interpretation:** Near Km, the enzyme is sensitive to substrate availability and small shifts in [S] move v sharply; far above Km, the enzyme is approaching saturation and additional substrate buys progressively less rate. Cells exploit this by keeping many regulated enzymes at [S] ≈ Km, where small allosteric or feedback signals can produce meaningful changes in flux. The same arithmetic tells you that to reach within 10% of Vmax in this enzyme you would need [S] ≈ 9·Km = 22.5 mM.


### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Enzymes and the Kinetics of Catalysis before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. Plot the simulated O₂ proxy vs temperature. Identify the approximate optimal temperature. Explain the molecular basis for activity loss at 0°C and above 50°C.
2. Explain why the denatured-enzyme condition showed no activity using the concept of protein denaturation and active site geometry.
3. Plot the simulated O₂ proxy vs [H₂O₂]. Describe the shape of the curve. At what concentration does activity appear to plateau? How does this relate to the concept of Vmax and enzyme saturation?
4. If you added a competitive inhibitor (e.g., a molecule structurally similar to H₂O₂), predict how the rate vs [S] curve would change in apparent Km and Vmax relative to uninhibited enzyme.
5. Catalase deficiency is a human genetic condition (acatalasia) associated with recurrent oral infections. Using your experimental results, explain why catalase is biologically important in protecting cells from H₂O₂ produced during oxidative metabolism.

## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A cell-biology team studies an enzyme E whose normal substrate concentration in the cytoplasm is held by upstream regulation at [S] ≈ Km. A candidate drug binds E and doubles its apparent Km without changing Vmax (a hallmark of pure competitive inhibition).
>
> (a) Compute the predicted fractional change in v caused by the drug at the normal cellular [S] (use v = Vmax·[S]/(Km+[S]) before and after the Km doubling), and interpret why an enzyme operating at [S] ≈ Km is particularly sensitive to a Km-shifting inhibitor.
> (b) Predict how the cell could partly compensate metabolically. Evaluate two routes: a homeostatic rise in [S] that restores the original v, and a compensatory increase in enzyme expression that raises effective Vmax. Quantify the [S] that would restore the original v under the doubled Km, and discuss which compensation is more plausible on a short time scale.
> (c) Design a paper-data experiment, using the same v-versus-[S] dataset format as today's lab, that would distinguish this competitive inhibitor from an allosteric inhibitor that lowers Vmax without changing Km. State the diagnostic comparison and the threshold of effect at which you would call the difference convincing.

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
   summarising the lab's take-home message, suitable for a tweet. Compare
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
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_I_enzymes_and_kinetics}`; all numerical
quantities in this lab use SI units — see \cref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
