<!-- render:skip-beamer -->

# Lab 28 — Circulation, Respiration, and Homeostasis {.unnumbered}

\label{sec:lab_unit_IX_circulation_respiration_homeostasis}

## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_IX_circulation_respiration_homeostasis} of the textbook — review that chapter before attempting the exercises below.*

- Analyze resting and post-exercise heart rate and blood pressure datasets and apply the Frank-Starling law
- Calculate cardiac output and stroke volume from anonymized case data using CO = HR × SV
- Apply Fick's principle to estimate oxygen consumption from heart rate data
- Analyse spirometry data to determine tidal volume, IRV, ERV, and FVC


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Circulation, Respiration, and Homeostasis.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Background {.unnumbered}

The cardiovascular system delivers oxygen and removes CO₂ at a rate matched to tissue demand. Cardiac output (CO) = stroke volume (SV) × heart rate (HR). The Frank-Starling law states that greater ventricular filling (preload) stretches sarcomeres to a more optimal myosin–actin overlap, increasing stroke volume. Spirometry measures lung volumes: tidal volume (TV ~500 mL), inspiratory reserve (IRV ~3,000 mL), expiratory reserve (ERV ~1,200 mL), and FVC = (TV + IRV + ERV) for healthy adults.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Calculator | 1 |
| Graph paper or spreadsheet template | 1 |
| Cardiovascular response dataset with rest, exercise, recovery, and heart-failure cases | 1 |
| Spirometry dataset printout (3 subjects: normal, asthmatic, COPD) | 1 |
| Altitude acclimatization case card with PaO2, ventilation, hematocrit, and symptom data | 1 |
| Digestive-renal balance cards: meal composition, water intake, plasma osmolality, urea, and urine concentration | 1 set |

## Paper-Based Investigation {.unnumbered}

**Part A — Cardiovascular Measurements**

1. Use the cardiovascular response dataset to compare resting HR, estimated stroke volume, and recovery time across cases.
2. Plot HR at rest, 0, 1, 2, 5, and 10 minutes post-exercise for the printed subjects. Identify the baseline control and the slowest recovery profile.
3. Calculate CO = HR × SV at rest and immediately post-exercise. Check whether the data are consistent with the Frank-Starling mechanism and autonomic regulation.

**Part B — Spirometry Analysis**

4. Use the printed spirometry dataset to calculate TV, FVC, FEV1, and FEV1/FVC where available.
5. Compare FVC and FEV1/FVC ratios for normal, asthmatic, and COPD subjects.
6. Use the altitude case card to connect PaO2 changes to ventilation, erythropoietin, hematocrit, and acclimatization.

**Part C — Digestive-Renal Homeostasis**

7. Use the digestive-renal cards to trace how a high-protein salty meal changes gut absorption, hepatic urea production, plasma osmolality, ADH release, and urine concentration.
8. Compare a freshwater fish, a desert mammal, and a bird/reptile excretory strategy. Identify whether ammonia, urea, or uric acid is the dominant nitrogen-waste solution and what water trade-off that solution implies.

## Data Recording {.unnumbered}

| Time (min) | HR (bpm) | Estimated SV (mL) | CO (L/min) |
| ---------- | -------- | ------------------ | ----------- |
| Rest | | 70 | |
| 0 (immediately post-exercise) | | 90 | |
| 1 | | | |
| 2 | | | |
| 5 | | | |
| 10 | | | |

Spirometry (from dataset):

| Subject | FVC (L) | FEV₁ (L) | FEV₁/FVC (%) | Pattern |
| ------- | ------- | --------- | ------------- | ------- |
| Normal | 4.8 | 4.3 | | |
| Asthmatic | 4.6 | 2.8 | | |
| COPD | 3.1 | 1.5 | | |

Reproducibility check: sampling interval used for recovery graph = ___; rule for classifying obstructive pattern = ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model circulation, respiration, and feedback compensation.
- **Data skill to practice:** Interpret physiological data from pressure, flow, saturation, or set-point changes.
- **BioSkills emphasis:** Modeling and simulation, Quantitative reasoning, Science and society.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Circulation, Respiration, and Homeostasis** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab, tie every cardiorespiratory claim to a flow or gas-exchange measurement and the control loop it implies: state which baseline, perturbation, and recovery values you used, and whether the apparent regulation could instead reflect reserve capacity or the resolution limit of the recording. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. Why did HR increase during exercise, and why did it remain elevated for several minutes post-exercise? Name the autonomic branch primarily responsible for the exercise-induced HR increase.
2. A reduced FEV₁/FVC ratio below the age-dependent lower limit of normal supports an obstructive pattern; a fixed 70% cutoff is a screening shortcut, not a comprehensive diagnostic boundary. The asthmatic shows reduced FEV₁ but relatively preserved FVC. Explain the structural difference in the airways that causes obstructive vs restrictive spirometry patterns.
3. Calculate the difference in cardiac output between rest and peak exercise in your data. Using Fick's principle (VO₂ = CO × (CaO₂ − CvO₂)), estimate oxygen consumption if the arterio-venous O₂ difference increases from 50 mL/L at rest to 150 mL/L during maximal exercise.
4. A patient with congestive heart failure has chronically elevated ventricular end-diastolic pressure. Explain how this shifts the Frank-Starling curve and contributes to pulmonary oedema (connect to Starling capillary forces).
5. At high altitude (3,500 m), PaO₂ drops from 100 to ~60 mmHg. Identify three physiological acclimatisation responses (acute and chronic) and for each, specify the sensing mechanism and the effector system involved.
6. A dehydrated student eats a salty, high-protein meal. Predict the direction of change for plasma osmolality, ADH, urea production, and urine concentration. Which measurements would distinguish "not enough water intake" from impaired kidney concentrating ability?

## Safety and Ethics Notes {.unnumbered}

No exercise testing, blood pressure measurement, or spirometry is required. Optional demonstrations involving human participants require consent, screening, single-use mouthpiece filters where relevant, and immediate stopping for dizziness, chest pain, or discomfort.

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
   \cref{sec:unit_IX_circulation_respiration_homeostasis} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IX_circulation_respiration_homeostasis} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_IX_circulation_respiration_homeostasis}`; all numerical
quantities in this lab use SI units — see Appendix D of the textbook for
unit conversions and biological-scale reference values.*
