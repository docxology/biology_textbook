# Lab — Cell Signaling and Communication {#sec:lab_unit_II_cell_signaling .unnumbered}


## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_II_cell_signaling} of the textbook — review that chapter before attempting the exercises below.*

- Model reception → transduction → response with the printed finite-window token rules
- Analyze how signal amplification occurs through enzymatic cascades
- Evaluate the role of second messengers using a classroom analogy and data interpretation
- Design an experiment to test how a signaling inhibitor disrupts a cellular response



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Calculate stage gains over a defined window and distinguish molecular from cell-level denominators.
- **Outcome 2 (LO2):** Interpret a receptor-antagonist dose shift with a matched vehicle control.
- **Outcome 3 (LO3):** Use inhibitor/bypass data to locate a cAMP pathway block.
- **Outcome 4 (LO5):** Predict GTPase-termination failure without claiming a unique clinical diagnosis.
- **Chapter LO coverage:** LO1, LO2, LO3, LO5
- **Rubric dimensions (12 points total):**
  - **Evidence — 3 points (LO1, LO2):** Award 1 for SG1's 1→10→100→500 counts, stage gains and 500 events per receptor per 10 s (not PKA molecules or bpm); award 1 for locating the baseline-corrected half-response at 80 bpm and EC50 values 1/10 nM; award 1 for the tenfold shift and common 100 bpm asymptote distinguished from the highest sampled responses.
  - **Controls — 3 points (LO2, LO3):** Award 1 for using vehicle/zero ligand as the SG2 baseline, 1 for comparing SG3's cAMP bypass after cyclase versus downstream-effector block, and 1 for explaining how matched viability and the inactive analog address cell loss and nonspecific inhibitor effects. Naming conditions without their discriminating purpose earns at most half credit in that component.
  - **Uncertainty — 2 points (LO1, LO2, LO3):** Award 1 for plotting SG2's triplicate ranges at the stated 60 s readout and distinguishing these preparations from SG1's deterministic finite-window counts; award 1 for explaining why a surmountable curve or successful bypass supports a model but does not uniquely establish molecular target specificity or clinical potency.
  - **Mechanism — 2 points (LO3, LO5):** Award 1 for locating the SG3 interruption upstream of the cAMP bypass under the printed pathway, and 1 for predicting prolonged cyclase/cAMP/PKA activity after loss of Gs GTP hydrolysis while retaining other termination processes. A disease name without the termination explanation earns no point.
  - **Transfer — 2 points (LO3):** In SG4's shared-cAMP comparison, award 1 for A/B ratios 10, 5/6 and 10 for WT, scaffold loss and reduced gain, and 1 for explaining why inappropriate B activation distinguishes localization loss from reduced gain whereas the fall in A alone does not. Do not infer that total cAMP uniquely fixes substrate-specific output.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define a second messenger in one sentence, then give two examples and the upstream receptor class that typically produces each.
2. A growth-factor receptor and a hormone receptor both activate downstream kinases. Distinguish how a receptor tyrosine kinase (RTK) initiates signaling from how a G-protein–coupled receptor (GPCR) initiates signaling, naming at least one molecular event unique to each pathway.
3. Two cell types express the same GPCR yet respond to the same ligand in opposite directions (one secretes, the other contracts). Propose two molecular reasons the downstream effect can differ even when the receptor and ligand are identical.

## Lab Context: Cell Signaling and Communication {.unnumbered}

Cell signaling links reception, transduction and response. Quantitative amplification depends on catalytic turnover, active lifetimes, substrate pools and the output counted; it is not a universal fixed number per ligand.

This lab uses explicitly synthetic teaching datasets and token rules, not published heart-rate measurements or actual drug experiments.

## Paper-Based Materials {.unnumbered}

: Printed materials for cascade, dose-response and pathway-bypass models. {#tbl:unit_II_cell_signaling_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Cell Signaling and Communication: cell-atlas or imaging source card: sample, assay, cell-state call, perturbation evidence, and uncertainty | 1 |
| Printed cascade count rules, included below | 1 |
| Calculator | 1 |
| Graph paper | 1 |
| Count tokens drawn on paper; no special card deck required | 1 sheet |
| Receptor -> cascade -> response diagram, included below | 1 |
| Synthetic dose-response and pathway-bypass datasets, included below | 1 |

## Paper-Based Investigation {.unnumbered}

**Part A — Signal Amplification Simulation**

1. Use a generic three-stage catalytic model over a fixed 10 s window: one receptor activates 10 relays; each relay produces 10 messenger tokens; each messenger triggers 5 effector-activation events under the supplied counting rule. Record 1,10,100,500. The last rule is an abstract gain, not literal cAMP-to-PKA stoichiometry.
2. Count total active tokens at each level. Record in the amplification table.
3. Calculate total effector events per active receptor per 10 s window; do not reinterpret the generic token count as a literal PKA-molecule count.

**Part B — Dose-Response Curve Analysis**

4. Plot SG2's synthetic heart-rate-like means and replicate ranges against free ligand concentration. Put nonzero doses on a logarithmic axis and zero-dose controls in a separate baseline column.
5. Identify the response halfway between the 60 bpm baseline and 100 bpm model asymptote, then read EC₅₀ at that response.
6. Plot the antagonist-model curve, compare EC₅₀ and asymptotes using SG2's explicit equation, and distinguish the asymptote from the highest sampled response. No actual propranolol potency is measured.

**Part C — Inhibitor Experiment Design**

7. Design a controlled paper experiment to test an illustrative adenylyl-cyclase inhibitor using SG3. The name SQ22536 can motivate the question, but the synthetic card does not establish that drug's potency or specificity.

## Data Recording {.unnumbered}

: Generic cascade counts and stage gains over a ten-second window. {#tbl:unit_II_cell_signaling_alignment_and_rubric_map_2}
| Signaling level | Count (tokens or events as stated) | Gain versus previous stage |
| --------------- | ---------------------------------- | -------------------------- |
| Active receptor | 1 | — |
| Relay tokens | | |
| Messenger tokens | | |
| Effector-activation events | | |
| **Total events per receptor per window** | | |

EC₅₀ untreated model: _______ nM
EC₅₀ antagonist model: _______ nM
Shift in EC₅₀: _______ fold

Your inhibitor experiment design (brief):

## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model signaling response from receptor activation to cellular output.
- **Data skill to practice:** Read pathway diagrams and infer the effect of agonists, antagonists, or mutations.
- **BioSkills emphasis:** Modeling and simulation, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Cell Signaling and Communication** with a reproducibility pass:

: Evidence and reproducibility decisions for signaling models. {#tbl:unit_II_cell_signaling_alignment_and_rubric_map_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: when you score a signaling case, name the receptor, the dose or stimulus level, the timing of the readout, and any feedback or crosstalk you assumed; treat a live-cell biosensor or optogenetic perturbation trace as the evidence that would change your call. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Signal Amplification in a Four-Step Kinase Cascade {.unnumbered}

**Problem:** A kinase cascade contains four sequential amplification steps. At each step, one active upstream kinase phosphorylates and activates 10 downstream substrate molecules before being inactivated. A single hormone–receptor binding event launches one active kinase at the top of the cascade. How many active terminal effector molecules result from that single binding event, and what fold-change does this represent relative to the input?

**Solution:** Each step multiplies the active-molecule count by 10. Starting from one active kinase:

- After step 1: 1 × 10 = 10 active molecules
- After step 2: 10 × 10 = 100 active molecules
- After step 3: 100 × 10 = 1,000 active molecules
- After step 4: 1,000 × 10 = 10,000 active molecules

Total amplification = 10⁴ = 10,000-fold. One ligand-binding event produces roughly 10,000 active terminal effectors.

**Interpretation:** This fixed-window model has gain 10^4 only under its stated assumptions. A G protein with reduced GTP hydrolysis can prolong upstream activity; a kinase does not generally hydrolyze GTP to turn itself off. Converting extracellular concentration to intracellular concentration requires compartment volumes and molecule numbers, not gain alone.


### Source-Governance Checkpoint {.unnumbered}

**Printed packet SG — synthetic teaching data; no patients, animal experiments or measured drug effects.** All displayed response triplicates are independent model preparations; time of readout is 60 s after exposure.

**SG1 token diagram:** receptor -> 10 relays -> 100 messengers -> 500 effector events over 10 s. Baseline no-ligand card=0 events; complete relay-block card=0; a half-active-relay card gives 250 events. Generic counts do not represent literal cAMP molecules activating five PKA enzymes each.

**SG2 dose cards:** Free ligand concentrations 0,0.1,1,10,100 nM; modeled heart-rate-like readout baseline=60 bpm and saturating increment=40 bpm. Untreated means are 60,63.636,80,96.364,99.604; antagonist-model means are 60,60.396,63.636,80,96.364. Each nonzero-dose triple is mean-1,mean,mean+1 bpm; at zero both have 59,60,61. Underlying model R=60+40L/(EC50+L), EC50=1 nM untreated and 10 nM antagonist, common asymptote 100 bpm. Zero ligand must be plotted separately from the logarithmic axis. Vehicle matches untreated. These are model values, not observations in people or a validated propranolol dose.

**SG3 pathway/bypass card:** GPCR -> Gs -> adenylyl cyclase -> cAMP -> PKA -> output. Response triples in arbitrary units: vehicle without agonist 4,5,6; agonist 98,100,102; agonist+cyclase-block model 8,10,12; agonist+block+membrane-permeant cAMP bypass 93,95,97; agonist+downstream-effector block+cAMP bypass 8,10,12. Viability is 95,96,97% for all conditions. An inactive inhibitor analog gives 98,100,102. These are independent model preparations; n=3 per condition.

**SG4 specificity card:** At matched total cAMP, targeted output A/B (arbitrary units) is WT 100/10, scaffold-loss 50/60, and reduced-gain control 50/5. Values are deterministic stipulated states, not replicate means. A fall in A alone cannot distinguish loss of gain from altered localization; B differentiates these two model hypotheses.

**Instructor key:** SG1 total gain=500 events/receptor/window; a generic four-step tenfold model instead gives 10,000 and is not the same pathway. SG2 half-maximal increment is 20 bpm above the 60 bpm baseline, giving an absolute response of 80 bpm, not half of the raw asymptote (50 bpm); EC50 shifts tenfold, common Emax is 100 even though the finite 100 nM dose has not reached it. SG3 cyclase block is bypassed by cAMP but a downstream block is not; this supports pathway order under the model, not drug specificity. Viability/inactive-analog controls reduce alternative explanations but do not exclude all off-target effects. SG4 scaffold loss increases inappropriate B output while reducing A; gain reduction scales both down. A Gs GTPase defect predicts prolonged cAMP signaling, not one uniquely identified disease. Governance: authored SG snapshot, no empirical atlas accession or clinical approval claim; refresh if receptor number, timing, desensitization or assay calibration differs.

## Analysis Questions {.unnumbered}

1. Calculate SG1's total event gain and compare it with the separate four-step worked example. Explain the different counting rules rather than interpreting their difference as an experimentally measured biological amplification deficit.
2. SG2 stipulates a tenfold EC₅₀ shift and common asymptote. Is that compatible with a surmountable competitive-antagonist model? Explain why this curve pattern alone neither proves a unique molecular mechanism nor measures propranolol's potency in patients.
3. Steroid hormones such as estrogen can enter cells and bind nuclear receptors directly. Why is this signaling pathway typically slower (minutes to hours) than GPCR cascades (seconds)? What is the cellular destination of the hormone-receptor complex?
4. Tamoxifen is a selective estrogen receptor modulator (SERM) that acts as an antagonist in breast tissue but a partial agonist in bone. Explain how the same molecule can produce opposite effects in different tissues.
5. If Gs cannot hydrolyze GTP, predict signaling duration through cyclase, cAMP and PKA, assuming other termination processes remain. Explain why this pathway phenotype does not uniquely identify a disease.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Many distinct ligands converge on the same second messenger (for example, both glucagon and epinephrine raise hepatic cAMP), yet their downstream physiological effects can be sharply distinguishable. Using evidence from this investigation and the chapter:
>
> (a) Identify at least three mechanisms cells use to maintain signaling specificity despite sharing second messenger molecules (consider receptor expression, scaffolding, spatial restriction, kinetics, and crosstalk).
> (b) Predict what happens to specificity if a cell loses one of those mechanisms — for example, if a scaffolding protein that tethers PKA to a particular substrate is deleted. Describe one observable phenotype.
> (c) Use SG4's A/B outputs at matched total cAMP to distinguish scaffold-loss from reduced-gain hypotheses. Calculate the A/B ratio for each card and explain why SG2's single-output response curve alone is insufficient.

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
   summarizing the lab's take-home message, suitable for a tweet. Compare
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
  definition is in `docs/manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_II_cell_signaling}`; all numerical
quantities in this lab use SI units — see \nameref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
