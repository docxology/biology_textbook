# Lab — Action Potentials and Synaptic Transmission {#sec:lab_unit_IX_action_potential_synapses .unnumbered}


## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_IX_action_potential_synapses} of the textbook — review that chapter before attempting the exercises below.*

- Analyze a compound action potential (CAP) recording from a nerve preparation to distinguish A, B, and C fiber types
- Simulate quantal neurotransmitter release and calculate mean quantal content
- Model the effect of GABA-A receptor modulation by benzodiazepines vs barbiturates
- Evaluate synaptic plasticity mechanisms using an LTP induction protocol dataset


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Action Potentials and Synaptic Transmission.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Using the Nernst equation E = (RT/zF) ln([ion]out/[ion]in), calculate the equilibrium potential for K⁺ at body temperature (T = 310 K, R = 8.314 J/mol·K, F = 96485 C/mol, z = +1) given [K⁺]in = 140 mM and [K⁺]out = 5 mM. Show the sign of the result and explain in one sentence why a resting neuron sits near (but not exactly at) this value.
2. During the rising phase of an action potential, which ion's membrane permeability changes most, and in which direction? Describe in two sentences how voltage-gated channel kinetics produce this change.
3. State one functional difference between an EPSP and an IPSP at the level of postsynaptic membrane conductance, and predict how each would shift the probability of reaching threshold at the axon hillock.

## Lab Context: Action Potentials and Synaptic Transmission {.unnumbered}

Synaptic transmission involves vesicle fusion (Ca²⁺-triggered SNARE complex assembly), neurotransmitter diffusion across the synaptic cleft, and receptor binding on the postsynaptic membrane. Release is quantal: the minimum unit is the vesicle (one quantum, ~5,000 molecules). The mean quantal content (m̄) can be estimated by the Poisson failure method: m̄ = ln(N/F₀) where N = total trials and F₀ = failures. Long-term potentiation (LTP) at Schaffer collateral → CA1 synapses requires NMDA receptor-mediated Ca²⁺ influx and CaMKII autophosphorylation.

The quantal-analysis worked example in the parent chapter (\cref{sec:unit_IX_action_potential_synapses}) derives quantal content $m = \bar{\text{EPP}} / \bar{\text{mEPP}}$ and uses Poisson statistics to compute failure probability: at $m = 2$, $P(\text{failure}) = e^{-2} \approx 13.5\%$. This lab dataset provides quantal-release trials from which students compute $m$ using both the ratio method and the Poisson failure method and then compare the two.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_IX_action_potential_synapses_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Action Potentials and Synaptic Transmission: physiology source card: baseline, perturbation, population range, clinical boundary, and evidence date | 1 |
| Compound action potential trace (printed: 3 peaks corresponding to Aα, Aδ, C fibers with time and conduction velocity axes) | 1 |
| Quantal release dataset (printed: 100 stimulus trials, number of quanta released each trial, count of failures) | 1 |
| GABA-A receptor pharmacology worksheet | 1 |
| LTP induction dataset (EPSP slope before/after high-frequency stimulation; two conditions: control and AP5-treated) | 1 |
| Calculator | 1 |
| Graph paper or spreadsheet template | 1 |

## Paper-Based Investigation {.unnumbered}

**Part A — Compound Action Potential Analysis**

1. From the CAP trace, identify the three peaks (Aα, Aδ, C fiber). Measure the latency of each peak from the stimulus artifact.
2. Given the distance from electrode to nerve (30 mm), calculate conduction velocity for each peak (velocity = distance/time).
3. Compare your calculated values to known conduction velocities (Aα: 70–120 m/s; Aδ: 5–30 m/s; C: 0.5–2 m/s).

**Part B — Quantal Analysis Simulation**

4. From the dataset (100 trials, F₀ = 8 failures): calculate m̄ by Poisson failure method (m̄ = ln(100/8) = ln(12.5)).
5. Also calculate m̄ by direct count method (m̄ = total quanta released / 100 trials).
6. Estimate release probability: p̄ = m̄/n (where n = total available release sites, given as 15).

**Part C — GABA-A Pharmacology**

7. From the worksheet, benzodiazepines increase the **frequency** of Cl⁻ channel opening; barbiturates increase **duration** of Cl⁻ channel opening (at low concentration) and open channels directly (at high concentration). On the I-V plot provided, annotate the effect of each drug class on Cl⁻ current.

**Part D — LTP Dataset**

8. Plot EPSP slope (% baseline) vs time (minutes) for control and AP5-treated groups before and after high-frequency stimulation (HFS at t=0).
9. Calculate the LTP magnitude: (mean EPSP slope 30–60 min post-HFS / mean EPSP slope 10 min pre-HFS) × 100%.
10. Reproducibility check: record the baseline window, post-HFS window, and any outlier rule before calculating LTP magnitude.

## Data Recording {.unnumbered}

: Alignment and Rubric Map: Fiber type and Latency (ms). {#tbl:unit_IX_action_potential_synapses_alignment_and_rubric_map_2}
| Fiber type | Latency (ms) | Conduction velocity (m/s) | Expected range |
| ---------- | ------------ | -------------------------- | -------------- |
| Peak 1 (Aα) | | | 70–120 m/s |
| Peak 2 (Aδ) | | | 5–30 m/s |
| Peak 3 (C) | | | 0.5–2 m/s |

Quantal analysis: F₀ = 8; N = 100
m̄ (Poisson) = ln(100/8) = ___
m̄ (direct count) from data = ___
p̄ = m̄/n (n=15) = ___

LTP magnitude: Control = ___%; AP5-treated = ___%

Reproducibility check: baseline window = ___; post-HFS window = ___; outlier rule = ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model excitability and synaptic response under changed ion or channel conditions.
- **Data skill to practice:** Interpret voltage traces, conductance changes, and synaptic perturbations.
- **BioSkills emphasis:** Modeling and simulation, Quantitative reasoning, Science and society.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Action Potentials and Synaptic Transmission** with a reproducibility pass:

: Alignment and Rubric Map: Evidence check and Student action. {#tbl:unit_IX_action_potential_synapses_alignment_and_rubric_map_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab, treat each excitability or transmission claim as a timing argument: ask which trace, latency, or quantal statistic supports it, and whether the conduction-velocity or release estimate would survive a change in fiber type, temperature, or release-probability heterogeneity. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Nernst Potential for Na+ at 37 C {.unnumbered}

**Problem:** A neuron rests near -70 mV. During the rising phase of an action potential, voltage-gated Na⁺ channels open and Na⁺ conductance rises roughly 500-fold relative to K⁺ conductance. Using the Nernst equation E = (RT/zF) ln([ion]out/[ion]in), calculate the equilibrium potential for Na⁺ given [Na⁺]in = 15 mM, [Na⁺]out = 145 mM, T = 310 K, R = 8.314 J/mol·K, F = 96485 C/mol, z = +1. Then explain in Goldman-equation terms why peak depolarization approaches — but does not quite reach — E_Na.

**Solution:** The prefactor RT/F at 310 K equals (8.314 × 310)/96485 ≈ 0.0267 V, or about 26.7 mV. The natural log of (145/15) is ln(9.667) ≈ 2.269. Multiplying gives E_Na ≈ 26.7 mV × 2.269 ≈ 60.6 mV. Reported as approximately +60 to +62 mV depending on rounding.

**Interpretation:** The Goldman–Hodgkin–Katz equation weights each ion's contribution to Vm by its relative permeability. When Na⁺ permeability dominates, Vm shifts toward E_Na; residual K⁺ and Cl⁻ permeabilities pull Vm back somewhat, so peak depolarization typically reaches roughly +30 to +40 mV rather than +60 mV. Membrane voltage approaches the equilibrium potential of the dominant ion, weighted by the other permeabilities that remain non-zero.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Action Potentials and Synaptic Transmission before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. C fibers (unmyelinated) have much slower conduction velocities than Aα fibers (myelinated). Using your cable property knowledge from Lab 29, explain the molecular basis for this difference.
2. The two methods for calculating m̄ gave similar but not identical answers. Which method is more reliable when there is heterogeneity in release probabilities across synapses? Explain the statistical assumption violated by each method.
3. A patient given a benzodiazepine (e.g., diazepam) overdose can be treated with flumazenil (a competitive benzodiazepine antagonist). Explain why flumazenil doesn't cause seizures on its own even though it fully blocks GABA-A modulation, while complete GABA-A inhibition by bicuculline does cause seizures.
4. AP5 (an NMDA receptor antagonist) blocked LTP induction. Explain the molecular events from NMDA receptor opening to CaMKII autophosphorylation to AMPA receptor insertion (at least 5 steps).
5. Ketamine is an NMDA receptor open-channel blocker used as an anaesthetic and, at sub-anaesthetic doses, as a rapid antidepressant. Propose a mechanism by which blocking NMDA receptors could relieve depression — consider what happens to synaptic strength in GABAergic interneurons when their NMDA receptors are blocked.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Evaluate how a toxin that prevents voltage-gated K⁺ channels from opening during the repolarization phase would reshape neuronal signaling.
>
> (a) Predict how the action potential waveform itself would change — describe expected effects on peak amplitude, repolarization rate, and absolute refractory period, and tie each prediction to the underlying conductance change.
> (b) Trace the downstream consequence at a chemical synapse: how would prolonged depolarization at the presynaptic terminal affect voltage-gated Ca²⁺ channel inactivation, vesicle release probability, and the magnitude of the postsynaptic response? Identify one prediction that could be empirically tested with the lab's quantal-analysis approach.

## Safety and Ethics Notes {.unnumbered}

Data-analysis and simulation primarily — no chemical or biological hazards. Discussions of neuropharmacology (drug mechanisms) should be factual and clinical in tone.

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
   \cref{sec:unit_IX_action_potential_synapses} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IX_action_potential_synapses} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_IX_action_potential_synapses}`; all numerical
quantities in this lab use SI units — see \nameref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
