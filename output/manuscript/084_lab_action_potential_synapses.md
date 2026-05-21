<!-- render:skip-beamer -->

# Lab 30 — Action Potentials and Synaptic Transmission {.unnumbered}

\label{sec:lab_unit_IX_action_potential_synapses}

## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_IX_action_potential_synapses} of the textbook — review that chapter before attempting the exercises below.*

- Analyse a compound action potential (CAP) recording from a nerve preparation to distinguish A, B, and C fibre types
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
## Background {.unnumbered}

Synaptic transmission involves vesicle fusion (Ca²⁺-triggered SNARE complex assembly), neurotransmitter diffusion across the synaptic cleft, and receptor binding on the postsynaptic membrane. Release is quantal: the minimum unit is the vesicle (one quantum, ~5,000 molecules). The mean quantal content (m̄) can be estimated by the Poisson failure method: m̄ = ln(N/F₀) where N = total trials and F₀ = failures. Long-term potentiation (LTP) at Schaffer collateral → CA1 synapses requires NMDA receptor-mediated Ca²⁺ influx and CaMKII autophosphorylation.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Compound action potential trace (printed: 3 peaks corresponding to Aα, Aδ, C fibres with time and conduction velocity axes) | 1 |
| Quantal release dataset (printed: 100 stimulus trials, number of quanta released each trial, count of failures) | 1 |
| GABA-A receptor pharmacology worksheet | 1 |
| LTP induction dataset (EPSP slope before/after high-frequency stimulation; two conditions: control and AP5-treated) | 1 |
| Calculator | 1 |
| Graph paper or spreadsheet template | 1 |

## Paper-Based Investigation {.unnumbered}

**Part A — Compound Action Potential Analysis**

1. From the CAP trace, identify the three peaks (Aα, Aδ, C fibre). Measure the latency of each peak from the stimulus artefact.
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

| Fibre type | Latency (ms) | Conduction velocity (m/s) | Expected range |
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

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab, treat each excitability or transmission claim as a timing argument: ask which trace, latency, or quantal statistic supports it, and whether the conduction-velocity or release estimate would survive a change in fibre type, temperature, or release-probability heterogeneity. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. C fibres (unmyelinated) have much slower conduction velocities than Aα fibres (myelinated). Using your cable property knowledge from Lab 29, explain the molecular basis for this difference.
2. The two methods for calculating m̄ gave similar but not identical answers. Which method is more reliable when there is heterogeneity in release probabilities across synapses? Explain the statistical assumption violated by each method.
3. A patient given a benzodiazepine (e.g., diazepam) overdose can be treated with flumazenil (a competitive benzodiazepine antagonist). Explain why flumazenil doesn't cause seizures on its own even though it fully blocks GABA-A modulation, while complete GABA-A inhibition by bicuculline does cause seizures.
4. AP5 (an NMDA receptor antagonist) blocked LTP induction. Explain the molecular events from NMDA receptor opening to CaMKII autophosphorylation to AMPA receptor insertion (at least 5 steps).
5. Ketamine is an NMDA receptor open-channel blocker used as an anaesthetic and, at sub-anaesthetic doses, as a rapid antidepressant. Propose a mechanism by which blocking NMDA receptors could relieve depression — consider what happens to synaptic strength in GABAergic interneurons when their NMDA receptors are blocked.

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
   summarising the lab's take-home message, suitable for a tweet. Compare
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
quantities in this lab use SI units — see Appendix D of the textbook for
unit conversions and biological-scale reference values.*
