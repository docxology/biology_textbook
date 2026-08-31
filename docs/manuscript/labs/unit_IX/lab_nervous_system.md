# Lab — Nervous System and Neural Signaling {#sec:lab_unit_IX_nervous_system .unnumbered}


## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_IX_nervous_system} of the textbook — review that chapter before attempting the exercises below.*

- Interpret reflex arc function using a clinical timing dataset and map receptive fields from paper data
- Analyze two-point discrimination thresholds from anonymized class datasets
- Analyze an action potential recording and identify threshold, peak, undershoot, and refractory periods
- Apply the length constant equation to predict how signal decay differs in myelinated vs unmyelinated axons


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Nervous System and Neural Signaling.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. List the five components of a monosynaptic spinal reflex arc in the order a signal traverses them — sensory receptor, afferent (sensory) neuron, integrating center, efferent (motor) neuron, effector. Describe in one sentence what each component contributes to the latency of the reflex.
2. Compare the preganglionic and postganglionic neurotransmitters typically used by the sympathetic and parasympathetic divisions. Indicate which division is more likely to release noradrenaline at its target tissues and which is more likely to release acetylcholine.
3. Define myelination at the level of a single axon and state, in one sentence, why myelinated fibers conduct faster than unmyelinated fibers of the same diameter.

## Lab Context: Nervous System and Neural Signaling {.unnumbered}

Neural signaling depends on the passive spread of graded potentials and, for long-distance signaling, the most-or-nothing action potential (AP). The **two-point discrimination threshold** (Weber's two-point test) reveals the density of somatosensory receptors in the skin: fingertips (2–3 mm threshold) vs upper back (40–70 mm). The patellar reflex is monosynaptic: stretching the patellar tendon activates Ia afferents in the quadriceps → synapse on α motor neurons in the spinal cord → quadriceps contraction. The entire arc takes <50 ms.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_IX_nervous_system_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Nervous System and Neural Signaling: physiology source card: baseline, perturbation, population range, clinical boundary, and evidence date | 1 |
| Patellar reflex case dataset with baseline, Jendrassik, and neuropathy scenarios | 1 |
| Two-point discrimination dataset for fingertip, palm, forearm, and upper back | 1 |
| Action potential recording trace (printed: one AP at scale with time axis in ms, voltage axis in mV) | 1 |
| Cable properties worksheet (with λ formula: λ = √(r_m/r_i)) | 1 |
| Calculator | 1 |
| Body surface map (printed outline of human figure) | 1 |
| Behavioral ethogram and neural-prosthesis evidence cards | 1 set |

## Paper-Based Investigation {.unnumbered}

**Part A — Patellar Reflex**

1. Use the reflex dataset to compare baseline, Jendrassik maneuver, peripheral neuropathy, and upper motor neuron scenarios. Record reflex magnitude and latency.
2. Identify the baseline control and the positive comparison that confirms the arc can increase with descending facilitation.
3. Map the likely lesion location for each abnormal case using the reflex arc diagram.

**Part B — Two-Point Discrimination**

4. Analyze the anonymized two-point dataset at various spacings (1, 2, 5, 10, 20, 40 mm) for the fingertip, palm, forearm, and upper back. Record the minimum spacing perceived as two points on each body area.

**Part C — Action Potential Trace Analysis**

5. From the printed AP trace: measure (a) resting membrane potential (mV); (b) threshold voltage; (c) amplitude (peak mV); (d) duration of absolute refractory period (ms); (e) relative refractory period (ms); (f) undershoot (afterhyperpolarisation) level (mV).

**Part D — Cable Properties Calculation**

6. Calculate the length constant λ for two axons: (a) unmyelinated 0.5 µm diameter axon (r_m = 10,000 Ω·cm, r_i = 80 MΩ/cm); (b) myelinated 10 µm diameter axon (r_m = 800,000 Ω·cm, r_i = 4 MΩ/cm). Determine V(x)/V₀ at a distance of 1 mm.

**Part E — Behavior and Neural Prosthesis Evidence**

7. Sort each behavior card into Tinbergen's four questions: mechanism, development, function, and evolutionary history.
8. Use the neural-prosthesis cards to separate what implanted recordings directly show (decodable neural activity) from the clinical claims that require longer-term evidence (implant stability, calibration, safety, and generalisation).

## Data Recording {.unnumbered}

Patellar reflex: extension observed? (Y/N) ___; Jendrassik effect: ___

Two-point discrimination thresholds:

: Alignment and Rubric Map: Body area and Minimum two-point distance (mm). {#tbl:unit_IX_nervous_system_alignment_and_rubric_map_2}
| Body area | Minimum two-point distance (mm) |
| --------- | -------------------------------- |
| Fingertip | |
| Palm | |
| Forearm | |
| Upper back | |

Action potential measurements from trace:

: Alignment and Rubric Map: Parameter and Value. {#tbl:unit_IX_nervous_system_alignment_and_rubric_map_3}
| Parameter | Value |
| --------- | ----- |
| Resting membrane potential | mV |
| Threshold | mV |
| Peak | mV |
| AP amplitude (threshold→peak) | mV |
| Absolute refractory period | ms |
| Relative refractory period | ms |
| Undershoot | mV |

Cable properties — length constant λ:
Unmyelinated: λ = ___ mm; V(1mm)/V₀ = ___
Myelinated: λ = ___ mm; V(1mm)/V₀ = ___

Reproducibility check: number of trials per body area = ___; threshold rule used (for example, two correct responses in a row) = ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Map circuit structure onto predicted information flow.
- **Data skill to practice:** Interpret neural data from anatomy, timing, or lesion evidence.
- **BioSkills emphasis:** Modeling and simulation, Quantitative reasoning, Science and society.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Nervous System and Neural Signaling** with a reproducibility pass:

: Alignment and Rubric Map: Evidence check and Student action. {#tbl:unit_IX_nervous_system_alignment_and_rubric_map_4}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab, keep the level of evidence explicit for every neural claim: separate what the structural or anatomical data show from what the recorded activity or behavior shows, and state the scale (cell, circuit, system) at which the inference is licensed before generalizing. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Median Nerve Conduction Velocity {.unnumbered}

**Problem:** A physician records median nerve conduction velocity by stimulating at the wrist and recording at the elbow. The distance between stimulating and recording electrodes is 24 cm and the measured onset latency is 2.4 ms. Calculate the conduction velocity in m/s and compare with the expected range for myelinated Aβ fibers (roughly 30–70 m/s). Then comment on whether the result is consistent with carpal-tunnel-related demyelination.

**Solution:** Convert units before dividing: 24 cm = 0.24 m and 2.4 ms = 0.0024 s. Conduction velocity v = distance / time = 0.24 m / 0.0024 s = 100 m/s. This is faster than the typical Aβ range, suggesting the measurement either (i) used a relatively long inter-electrode segment that averages over fast proximal fibers or (ii) reflects a healthy nerve with rapid saltatory conduction. A value substantially below 30 m/s in this segment would have been more consistent with focal demyelination from carpal tunnel compression.

**Interpretation:** Conduction velocity is one of the most sensitive electrophysiological signs of demyelination, because saltatory conduction depends on intact myelin between nodes of Ranvier. Slowing on the order of 30–50% below the expected range, particularly when localized to the segment under the carpal ligament, supports the clinical suspicion. A normal or supra-normal velocity makes focal demyelination unlikely on its own.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Nervous System and Neural Signaling before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. The fingertip had a much shorter two-point discrimination threshold than the upper back. Relate this to somatotopic mapping in the somatosensory cortex — which area of the sensory homunculus represents fingers vs trunk, and what is the neural basis for this high-density representation?
2. The Jendrassik maneuver increased the patellar reflex. Explain this using the concept of motor neuron excitability and descending facilitation from the cortex/brainstem.
3. The action potential's absolute refractory period prevents reversed signal propagation (backward re-excitation). Explain how sodium channel inactivation (h-gate closed) creates this period and why this is essential for unidirectional propagation.
4. Your cable property calculation showed much higher λ in the myelinated axon. Relate this to saltatory conduction: why does an action potential jump between nodes of Ranvier rather than regenerate continuously along the axon?
5. In multiple sclerosis, the myelin sheath is destroyed. Using your λ calculations, predict what happens to action potential propagation in demyelinated axons, and explain why patients might experience increased sensitivity to heat (Uhthoff's phenomenon).
6. A speech BCI card reports high decoding accuracy from one participant during attempted speech. Which conclusion is directly supported, and which conclusions would require additional controls or longitudinal data?


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Compare the sensory consequences of damage to the dorsal columns of the spinal cord with damage to the spinothalamic tract on the same side of the cord.
>
> (a) For each tract, identify the modalities it predominantly carries (e.g., fine touch and proprioception versus pain and temperature) and the side of the body on which a unilateral lesion would produce a deficit at a level below the lesion. Justify the laterality using what you know about where each tract decussates relative to its entry into the cord.
> (b) Predict the clinical picture a patient would present with if they had a hemisection of the cord at the mid-thoracic level (a Brown–Séquard pattern). Specify which modalities would be lost on which side below the lesion, and explain how a careful bedside sensory exam could distinguish this pattern from a complete cord transection.

## Safety and Ethics Notes {.unnumbered}

No touch-based neurological testing is required. If an instructor offers an optional demonstration, student consent is required, taps must be gentle, discriminator tips must be blunted, and students may opt out without explanation.

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
   \cref{sec:unit_IX_nervous_system} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IX_nervous_system} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `docs/manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_IX_nervous_system}`; all numerical
quantities in this lab use SI units — see \nameref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
