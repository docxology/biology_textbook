# Lab A — Systems Science and Emergence {#sec:lab_unit_0_systems_science .unnumbered}


*This activity accompanies \cref{sec:unit_0_systems_science} of the textbook — review that chapter before attempting the exercises below.*

**\nameref{sec:unit_0_unit_intro} · Lab A**

---

## Learning Objectives {.unnumbered}

- Identify the three canonical elements of a system (components, interactions, boundary) in concrete biological examples.
- Diagram negative- and positive-feedback loops for real physiological systems and predict their stabilizing or amplifying behavior.
- Compute response curves from the Hill equation and relate the Hill coefficient $n$ to cooperativity and switch-like behavior.
- Reason about the difference between a complicated machine and a complex system using a worked example.

---



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Label a mitochondrion boundary and two material flows.
- **Outcome 2 (LO2):** Assign every feedback-edge sign and identify a bounding mechanism.
- **Outcome 3 (LO8):** Calculate Hill occupancy and oxygen unloading with consistent units.
- **Outcome 4 (LO6):** Calculate the delay threshold and distinguish instability from bounded oscillation.
- **Chapter LO coverage:** LO1, LO2, LO6, LO8
- **Rubric dimensions (12 points total):**
  - **Evidence — 4 points (LO1, LO8):** Award 1 for a stated mitochondrial boundary with a material input and output crossing it, 2 for the three Hill curves calculated on the supplied concentration grid with labeled axes, and 1 for lung/muscle occupancies and unloading in percentage points using the separate pressure model. Do not interchange μM and mmHg inputs.
  - **Controls — 2 points (LO2, LO8):** Award 1 for removing the baroreceptor-to-vagal edge on paper while holding external pressure input fixed and explaining loss of that feedback path; award 1 for comparing n=1 with n=2.8 or 4 at the same half-response and ligand concentration, rather than changing affinity and cooperativity together.
  - **Uncertainty — 2 points (LO2, LO6):** Award 1 for explaining why a loop sign without rates/delays cannot establish stability, and 1 for distinguishing the linear delay model's instability boundary from evidence for a bounded physiological oscillation. Naming “uncertainty” without identifying the missing dynamics earns neither point.
  - **Mechanism — 2 points (LO2):** Award 1 for signs justified from every printed feedback edge, including the phase-dependent estradiol edge, and 1 for a bounding process such as Na+ channel inactivation/K+ currents rather than indefinite positive-loop runaway.
  - **Transfer — 2 points (LO6):** For the ventilator-inspired paper model, award 1 for the boundary gain 0.1571 s⁻¹ and onset period 40 s with the stated lag, and 1 for explaining how reducing gain or lag moves the model away from instability without claiming a patient-specific ventilator setting.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define a system boundary and explain why two analysts can choose different boundaries for the same problem and still produce internally consistent models. Give one short example from the parent chapter.
2. A bedroom thermostat raises the heater output when the room cools and lowers it when the room warms. Classify the dominant feedback loop in this control system and identify the variable whose deviation drives the corrective action.
3. Compare a stock (a quantity with accumulated history) and a flow (a rate that changes a stock per unit time) for the case of a small lake's water budget. Give one biological stock and one biological flow that would be appropriate to include in a model of that lake's ecology.

## Lab Context: Systems Science and Emergence {.unnumbered}

A **system** has interacting components and a stated boundary. The Hill equation describes an equilibrium dose-response; it is not by itself a stability model:

\begin{equation}
\theta \;=\; \frac{[L]^n}{K_d^n + [L]^n}
\label{eq:lab_a_hill}
\end{equation}

Here $K_d$ denotes the effective half-response concentration (not necessarily a microscopic binding constant). $n>1$ produces ultrasensitivity; the physiological hemoglobin approximation below uses $n=2.8$, not an assertion of exactly four-site concerted binding.

The tasks separate boundary choice, feedback dynamics and cooperative binding rather than treating a sigmoid as proof of bistability.

---

## Pre-Lab (to complete before class) {.unnumbered}

1. Copy \cref{eq:lab_a_hill} into your notebook. Compute θ for $n = 1, 2, 4$ at $[L] = K_d$, $2K_d$, $5K_d$. Tabulate.
2. Define in your own words: **system**, **emergence**, **feedback**, **homeostasis**, **modularity**.
3. Use the positive and negative feedback cases printed in Part 2; identify one of each and the variable it changes.

---

## Paper-Based Materials {.unnumbered}

- Graph paper (2 sheets per student).
- Calculator.
- Colored pens.
- Printed governance card S1 and the tables below; draw feedback diagrams and Hill-curve axes on notebook paper.

---

## Paper-Based Investigation {.unnumbered}

### Part 1 — Identifying Systems {.unnumbered}

For each of the following, identify: (a) the components, (b) the key interactions, (c) the boundary separating system from environment, and (d) one input and one output crossing the boundary.

1. A single mitochondrion.
2. The glucose-insulin-glucagon regulatory axis.
3. A coral reef.
4. A bacterial biofilm on a medical catheter.
5. A neuron's axon hillock.

### Part 2 — Feedback Loop Diagrams {.unnumbered}

For each system below, diagram the feedback loop and classify its sign. A raised blood pressure raises baroreceptor firing and vagal tone; vagal tone lowers heart rate, which lowers pressure. Contractions increase stretch and oxytocin release. LH raises estradiol, and GnRH raises LH; estradiol suppresses GnRH in the follicular case but sustained high estradiol stimulates it in the ovulatory case. Depolarization opens Na$^+$ channels, whose inward current increases depolarization. Explain why edge signs alone cannot choose between a stable fixed point, oscillation and runaway without rates, delays and bounding mechanisms.

1. Blood pressure → baroreceptor firing → vagal tone → heart rate → blood pressure.
2. Oxytocin → uterine contraction → stretch receptor → oxytocin (during labor).
3. Luteinizing hormone → ovarian estradiol → hypothalamic GnRH (follicular phase).
4. Luteinizing hormone → ovarian estradiol → hypothalamic GnRH (ovulatory phase).
5. Depolarizing Na$^+$ current → more open Na$^+$ channels → depolarization (action potential upstroke).

Why do loops 3 and 4 have different signs, and what does the switch imply for the dynamics of the menstrual cycle?
As a paper negative control, remove only the baroreceptor-firing → vagal-tone edge, keeping the external pressure perturbation fixed. Which corrective path is lost? Explain why this removes that loop's correction rather than proving that all blood-pressure regulation stops.

### Part 3 — Hill Curve by Hand {.unnumbered}

1. Using $K_d=10\,\mu\mathrm{M}$, compute θ at $[L]=1,2,5,10,20,50,100\,\mu\mathrm{M}$ for illustrative coefficients $n=1,2.8,4$. The pressure-based hemoglobin case in Analysis Question 1 is a separate model.
2. Plot the three curves on the same axes. Label the "switch zone" where small changes in $[L]$ produce large changes in θ.
3. For which $n$ is the transition sharpest? How does this cooperativity benefit an oxygen-carrying pigment?

### Part 4 — Complicated vs. Complex {.unnumbered}

A wristwatch and a live cell both contain many interacting components. Yet one is **complicated** and the other **complex**. In a table, contrast:

: Part 4 — Complicated vs. Complex: Feature and Wristwatch. {#tbl:unit_0_systems_science_part_4_complicated_vs_complex}
| Feature | Wristwatch | Live cell |
| ------- | ---------- | --------- |
| Component count | ~100 | ~10⁹ molecules |
| Predictability | High (mechanistic) | Statistical |
| Repairability | External | Self-repair |
| Adaptation | None | Evolutionary |
| Failure mode | Component breakage | Network dysregulation |
| Emergent properties | Timekeeping arises from organized parts; designed | Metabolism, identity and division arise from interacting parts |

Discuss in your group one additional feature that distinguishes complex from complicated, and one case where the distinction is blurry (e.g., a modern autopilot with adaptive learning).

---

## Data Tables {.unnumbered}

: System boundaries, components and material-flow worksheet. {#tbl:unit_0_systems_science_part_4_complicated_vs_complex_2}
| System | Components | Interactions | Boundary | Input | Output |
| ------ | ---------- | ------------ | -------- | ----- | ------ |
| Mitochondrion | | | | | |
| Glucose axis | | | | | |
| Coral reef | | | | | |
| Biofilm | | | | | |
| Axon hillock | | | | | |

: Signed feedback loops and limits on dynamical predictions. {#tbl:unit_0_systems_science_part_4_complicated_vs_complex_3}
| Feedback loop | +/− | Predicted behavior |
| ------------- | --- | ------------------- |
| Baroreceptor reflex | | |
| Oxytocin-uterus | | |
| GnRH follicular | | |
| GnRH ovulatory | | |
| Na$^+$ action potential | | |

: Hill-response sample values for ligand concentration and fractional occupancy. {#tbl:unit_0_systems_science_part_4_complicated_vs_complex_4}
| $[L]\,(\mu\mathrm{M})$ | θ at $n=1$ | θ at $n=2.8$ | θ at $n=4$ |
| ---------------------- | ----------------- | ------------------- | ----------------- |
| 1 | | | |
| 2 | | | |
| 5 | | | |
| 10 | | | |
| 20 | | | |
| 50 | | | |
| 100 | | | |

---

## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Build and critique a feedback model for a familiar living system.
- **Data skill to practice:** Translate a verbal biological system into variables, links, and testable predictions.
- **BioSkills emphasis:** Modeling and simulation, Process of science, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Systems Science and Emergence** with a reproducibility pass:

: Evidence and reproducibility decisions for the systems models. {#tbl:unit_0_systems_science_part_4_complicated_vs_complex_5}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: For the feedback-diagram and Hill-curve datasets, the reproducible quantities are the sign assigned to each loop edge and the Hill coefficient $n$ used for the saturation calculation: state the system boundary you drew, justify every $+$ or $-$ sign from the dataset, and report the O$_2$-saturation numbers another group must be able to regenerate from your stated $n$. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Source-Governance Checkpoint {.unnumbered}

**Printed governance card S1 (synthetic teaching model, authored for this packet):** Boundary = circulating oxygen carrier; observable = fractional occupancy; fixed inputs = $p_{50}=26$ mmHg, $n=2.8$; no independent biological replicates. Baseline = $n=1$ at the same half-response pressure; rival = altered affinity rather than cooperativity. Refresh trigger = using a different pH, temperature or species; this toy curve is not an individualized clinical prediction.

**Instructor key:** At L=K, 2K, 5K, n=1 gives 0.500, 0.667, 0.833; n=2.8 gives 0.500, 0.874, 0.989; n=4 gives 0.500, 0.941, 0.998. For hemoglobin, lung saturation is about 0.9775 and muscle saturation 0.3242, so unloading is about 65.3 percentage points. Feedback signs: baroreflex negative; oxytocin positive; follicular ovarian feedback negative under the stated phase; sustained high estradiol around ovulation positive; sodium upstroke positive but bounded by channel inactivation and K+ currents. A negative sign does not guarantee stability with delay. For Analysis Question 4's explicit model dx/dt=-k x(t-10 s), the first linear boundary is k=π/(2×10 s)=0.1571 s^-1 and onset period 4×10 s=40 s; real controllers need their own equations. Accept alternative boundaries if crossings are explicit. The wristwatch/cell contrast is heuristic: a watch also has collective properties, and cells are mechanistically constrained.

**Edge-removal benchmark:** Without the baroreceptor-to-vagal link, increased pressure cannot use this printed path to lower heart rate and pressure. The open path no longer supplies this feedback correction; other unmodelled regulatory paths are not ruled out.

### Worked Example: Stock-and-flow projection of a small mammal population {.unnumbered}

**Problem:** A field site has 200 deer mice at the start of the year. The per-capita birth rate is 0.020 per month and the per-capita death rate is 0.015 per month, with no immigration or emigration. Assume both rates stay constant for one month. Compute the net inflow into the population stock, the population at the end of the month, and the doubling time implied by the net per-capita rate.

**Solution:**

- Net per-capita rate = 0.020 − 0.015 = 0.005 per month.
- Net monthly inflow = 0.005 × 200 = 1.0 mice per month.
- End-of-month stock = 200 + 1 = 201 mice.
- Doubling time using the continuous-rate approximation t_double ≈ ln(2) / r = 0.693 / 0.005 ≈ 138.6 months (about 11.5 years).

**Interpretation:** The stock barely shifts in one month, yet the small positive net rate accumulates into a doubling time of roughly a decade — a feature of pure stock dynamics that surprises students who expect proportional intuitions to track short time-scale observations. A density-dependent term (a balancing loop tied to food, predators, or disease) would slow growth before doubling and is the kind of negative-feedback structure a richer model needs once the population approaches habitat capacity.


## Analysis Questions {.unnumbered}

1. For hemoglobin use $p_{50}=26$ mmHg, $n=2.8$ and $Y=p^{2.8}/(26^{2.8}+p^{2.8})$. Calculate saturation at lung $p=100$ mmHg and active-muscle $p=20$ mmHg, then report unloading in percentage points. This pressure-unit model is separate from Part 3's illustrative micromolar ligand model.
2. In Part 2, the ovarian-pituitary loop reverses sign across the menstrual cycle. What does this imply for the stability of the overall system, and what biological mechanism produces the sign reversal?
3. Modular design makes biological systems easier to evolve (new modules can be added without breaking old ones). Give one counter-example — a domain where modularity *constrains* evolution rather than freeing it.
4. For a ventilator-inspired synthetic model, let the deviation $x$ obey $dx/dt=-k x(t-\tau)$, with $k>0$ in s$^{-1}$ and lag $\tau=10$ s. The first stability boundary is $k\tau=\pi/2$, with onset period $4\tau$. Calculate both values. Explain why increasing gain can destabilize this negative loop, suggest reducing gain or lag, and distinguish linear instability from a demonstrated bounded physiological oscillation.
5. Design a paper-based experiment to test whether a bacterial-population model exhibits emergent collective behavior distinct from isolated-cell behavior. What is the null hypothesis and what observation card would refute it?

## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A regional hospital network observes that emergency-department wait times rise sharply during winter respiratory-virus seasons. Administrators propose adding bed capacity; clinicians propose a faster discharge pathway to free beds; the public-health team proposes upstream vaccination outreach.
>
> (a) Draw a causal loop sketch (in words) of the stocks and flows linking community infections, hospital admissions, available beds, and wait times. Mark each proposed intervention with the leverage point category from the parent chapter that best matches it (for example, parameter change, feedback strength, system goal).
> (b) Predict the qualitative behavior of the system under each proposed intervention over one winter season, and explain which intervention is most likely to shift the long-run behavior rather than the immediate symptom. Ground the prediction in the dominant feedback loops you sketched.
> (c) Design a short measurement plan (three variables to track and one indicator of unintended consequences) that would tell the administration whether the chosen intervention reduced wait times without shifting the burden to a downstream subsystem such as primary care or home recovery.

---

## Discussion Questions {.unnumbered}

1. A reductionist insists that knowing everything about every molecule in a cell is sufficient to understand cellular behavior. Where does systems science push back?
2. Are there systems in biology that are *not* adaptive? Propose a candidate and defend your choice.
3. In a hypothetical surge, admissions exceed discharges for several weeks. Use the resulting bed-occupancy stock to explain why spare capacity and upstream prevention could alter waiting times. Do not infer actual city-level pandemic outcomes from this model.

---

## Safety and Ethics Notes {.unnumbered}

Paper-based lab — no reagents or instruments, no physical risk. Discussion of the menstrual cycle, labor, and ventilator management should be inclusive and accurate; seek clarification from the instructor if terminology feels unfamiliar. The Covid-19 example should be grounded in public-health data rather than anecdote.

*Module: `src/biology/cell/cell_biology.py` (`hill_equation`, `receptor_occupancy`); `src/biology/ecology/ecology.py` (`logistic_growth`).*
