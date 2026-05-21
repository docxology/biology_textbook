<!-- render:skip-beamer -->

# Lab 8 — Cell Signalling and Communication {.unnumbered}

\label{sec:lab_unit_II_cell_signaling}

## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_II_cell_signaling} of the textbook — review that chapter before attempting the exercises below.*

- Model the three-stage cell signalling cascade (reception → transduction → response) through a physical simulation
- Analyse how signal amplification occurs through enzymatic cascades
- Evaluate the role of second messengers using a classroom analogy and data interpretation
- Design an experiment to test how a signalling inhibitor disrupts a cellular response


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Cell Signalling and Communication.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Background {.unnumbered}

Cell signalling enables cells to detect and respond to extracellular information. The three stages are: (1) **Reception** — a ligand binds its receptor (GPCR, RTK, nuclear receptor); (2) **Transduction** — signal is converted and amplified through a cascade of molecular switches; (3) **Response** — altered gene expression, enzyme activity, or cytoskeletal change. Amplification is a key feature: one activated receptor can activate hundreds of G proteins, each activating dozens of adenylate cyclase molecules, each producing thousands of cAMP molecules — giving a cascade amplification of >10⁶.

In this lab you will simulate and calculate signal amplification through a cascade model, analyse a published cell signalling dose-response dataset, and design an inhibitor experiment.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Signal cascade worksheet (instructor-provided: table with step values) | 1 |
| Calculator | 1 |
| Graph paper or laptop (for dose-response curve) | 1 |
| Coloured card tokens (representing signalling molecules): 1 "ligand" card, 10 "G protein" cards, 50 "cAMP" cards, 500 "PKA" cards | 1 set |
| 12-well plate or paper diagram of receptor → cascade → response | 1 |
| Sample dataset: β-adrenergic response (heart rate vs [adrenaline]) (instructor-provided) | 1 |

## Paper-Based Investigation {.unnumbered}

**Part A — Signal Amplification Simulation**

1. One student is the "ligand": activate one "receptor" card. Each activated receptor activates 10 G protein cards. Each G protein activates 10 "adenylate cyclase" steps (represented by producing 10 cAMP tokens). Each cAMP activates 5 PKA tokens.
2. Count total active tokens at each level. Record in the amplification table.
3. Calculate total fold amplification from ligand to PKA response.

**Part B — Dose-Response Curve Analysis**

4. Using the provided dataset of heart rate (bpm) vs [adrenaline] (nM), plot a dose-response curve on semilog paper (log [adrenaline] on x-axis, heart rate on y).
5. Identify the EC₅₀ (concentration producing 50% of maximal response) from your curve.
6. A second curve shows the same response in the presence of propranolol (a β-blocker). Plot both curves; compare EC₅₀ values and maximum responses.

**Part C — Inhibitor Experiment Design**

7. Design a controlled paper experiment to test whether blocking adenylate cyclase with SQ 22536 would prevent an adrenaline-mediated response. Use provided pathway cards and a simulated response dataset rather than cells or tissue.

## Data Recording {.unnumbered}

| Signalling level | Molecules activated | Fold amplification vs previous step |
| ---------------- | ------------------- | ------------------------------------ |
| Ligand | 1 | — |
| Receptors activated | | |
| G proteins activated | | |
| cAMP produced | | |
| PKA catalytic subunits activated | | |
| **Total amplification (ligand → PKA)** | | |

EC₅₀ without propranolol: _______ nM
EC₅₀ with propranolol: _______ nM
Shift in EC₅₀: _______ fold

Your inhibitor experiment design (brief):

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model signaling response from receptor activation to cellular output.
- **Data skill to practice:** Read pathway diagrams and infer the effect of agonists, antagonists, or mutations.
- **BioSkills emphasis:** Modeling and simulation, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Cell Signalling and Communication** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: when you score a signalling case, name the receptor, the dose or stimulus level, the timing of the readout, and any feedback or crosstalk you assumed; treat a live-cell biosensor or optogenetic perturbation trace as the evidence that would change your call. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. Calculate the fold amplification your cascade produced. How does this compare to the theoretical amplification cited in the chapter (~10⁶)? What real-world factors account for the difference?
2. Propranolol is a competitive antagonist of the β-adrenergic receptor. Based on your dose-response curves, does it shift the EC₅₀, reduce Emax, or both? What does this pattern indicate about mechanism?
3. Steroid hormones such as oestrogen can enter cells and bind nuclear receptors directly. Why is this signalling pathway typically slower (minutes to hours) than GPCR cascades (seconds)? What is the cellular destination of the hormone-receptor complex?
4. Tamoxifen is a selective oestrogen receptor modulator (SERM) that acts as an antagonist in breast tissue but a partial agonist in bone. Explain how the same molecule can produce opposite effects in different tissues.
5. A mutation makes the Gs protein GTPase-inactive (cannot hydrolyse GTP to GDP). Predict the effect on adenylate cyclase activity, cAMP levels, and PKA activity in the affected cell. What disease would this phenotype resemble?

## Safety and Ethics Notes {.unnumbered}

No hazardous chemicals in this lab. Card and paper components primarily. If a computer simulation module is used, follow data handling and privacy guidelines for any shared datasets.

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
   \cref{sec:unit_II_cell_signaling} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_II_cell_signaling} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_II_cell_signaling}`; all numerical
quantities in this lab use SI units — see Appendix D of the textbook for
unit conversions and biological-scale reference values.*
