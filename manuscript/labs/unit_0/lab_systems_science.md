# Lab A — Systems Science and the Logic of Emergence {.unnumbered}

\label{sec:lab_unit_0_systems_science}

*This activity accompanies \cref{sec:unit_0_systems_science} of the textbook — review that chapter before attempting the exercises below.*

**\nameref{sec:unit_0_unit_intro} · Lab A**

---

## Learning Objectives {.unnumbered}

- Identify the three canonical elements of a system (components, interactions, boundary) in concrete biological examples.
- Diagram negative- and positive-feedback loops for real physiological systems and predict their stabilising or amplifying behaviour.
- Compute response curves from the Hill equation and relate the Hill coefficient $n$ to cooperativity and switch-like behaviour.
- Reason about the difference between a complicated machine and a complex system using a worked example.

---



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Systems Science and the Logic of Emergence.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define a system boundary and explain why two analysts can choose different boundaries for the same problem and still produce internally consistent models. Give one short example from the parent chapter.
2. A bedroom thermostat raises the heater output when the room cools and lowers it when the room warms. Classify the dominant feedback loop in this control system and identify the variable whose deviation drives the corrective action.
3. Compare a stock (a quantity with accumulated history) and a flow (a rate that changes a stock per unit time) for the case of a small lake's water budget. Give one biological stock and one biological flow that would be appropriate to include in a model of that lake's ecology.

## Background {.unnumbered}

A **system** is a set of interacting components, bounded against its surroundings, whose behaviour depends on the interactions as much as on the parts. The central mathematical tool for stability is the **Hill equation**:

\begin{equation}
\theta \;=\; \frac{[L]^n}{K_d^n + [L]^n}
\label{eq:lab_a_hill}
\end{equation}

where θ is the fraction of receptors bound, $[L]$ the ligand concentration, $K_d$ the dissociation constant, and $n$ the Hill coefficient. For $n = 1$ the curve is hyperbolic (graded response); for $n = 4$ it is steep and switch-like (as in haemoglobin's O$_2$ binding).

Today's lab trains three intuitions: what counts as "the system", how feedback loops behave, and how cooperativity converts graded chemistry into binary biology.

---

## Pre-Lab (to complete before class) {.unnumbered}

1. Copy \cref{eq:lab_a_hill} into your notebook. Compute θ for $n = 1, 2, 4$ at $[L] = K_d$, $2K_d$, $5K_d$. Tabulate.
2. Define in your own words: **system**, **emergence**, **feedback**, **homeostasis**, **modularity**.
3. Bring one example of a biological positive feedback loop and one example of a biological negative feedback loop (not from the textbook).

---

## Paper-Based Materials {.unnumbered}

- Graph paper (2 sheets per student).
- Calculator.
- Coloured pens.
- Worksheet with blank feedback diagrams and Hill-curve axes.

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

For each system below, diagram the feedback loop and classify it as positive or negative. Predict the steady-state behaviour (stable fixed point, oscillation, or runaway).

1. Blood pressure → baroreceptor firing → vagal tone → heart rate → blood pressure.
2. Oxytocin → uterine contraction → stretch receptor → oxytocin (during labour).
3. Luteinising hormone → ovarian oestradiol → hypothalamic GnRH (follicular phase).
4. Luteinising hormone → ovarian oestradiol → hypothalamic GnRH (ovulatory phase).
5. Depolarising Na$^+$ current → more open Na$^+$ channels → depolarisation (action potential upstroke).

Why do loops 3 and 4 have different signs, and what does the switch imply for the dynamics of the menstrual cycle?

### Part 3 — Hill Curve by Hand {.unnumbered}

1. Using $K_d = 10\,\mu\mathrm{M}$, compute θ at $[L] = 1, 2, 5, 10, 20, 50, 100\,\mu\mathrm{M}$ for three values of $n$: 1, 2.8 (physiological Hb), and 4.
2. Plot most three curves on the same axes. Label the "switch zone" where small changes in $[L]$ produce large changes in θ.
3. For which $n$ is the transition sharpest? How does this cooperativity benefit an oxygen-carrying pigment?

### Part 4 — Complicated vs. Complex {.unnumbered}

A wristwatch and a live cell both contain many interacting components. Yet one is **complicated** and the other **complex**. In a table, contrast:

| Feature | Wristwatch | Live cell |
| ------- | ---------- | --------- |
| Component count | ~100 | ~10⁹ molecules |
| Predictability | High (mechanistic) | Statistical |
| Repairability | External | Self-repair |
| Adaptation | None | Evolutionary |
| Failure mode | Component breakage | Network dysregulation |
| Emergent properties | None (function designed in) | Many (metabolism, identity, division) |

Discuss in your group one additional feature that distinguishes complex from complicated, and one case where the distinction is blurry (e.g., a modern autopilot with adaptive learning).

---

## Data Tables {.unnumbered}

| System | Components | Interactions | Boundary | Input | Output |
| ------ | ---------- | ------------ | -------- | ----- | ------ |
| Mitochondrion | | | | | |
| Glucose axis | | | | | |
| Coral reef | | | | | |
| Biofilm | | | | | |
| Axon hillock | | | | | |

| Feedback loop | +/− | Predicted behaviour |
| ------------- | --- | ------------------- |
| Baroreceptor reflex | | |
| Oxytocin-uterus | | |
| GnRH follicular | | |
| GnRH ovulatory | | |
| Na$^+$ action potential | | |

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

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Build and critique a feedback model for a familiar living system.
- **Data skill to practice:** Translate a verbal biological system into variables, links, and testable predictions.
- **BioSkills emphasis:** Modeling and simulation, Process of science, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Systems Science and the Logic of Emergence** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: For the feedback-diagram and Hill-curve datasets, the reproducible quantities are the sign assigned to each loop edge and the Hill coefficient $n$ used for the saturation calculation: state the system boundary you drew, justify every $+$ or $-$ sign from the dataset, and report the O$_2$-saturation numbers another group must be able to regenerate from your stated $n$. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Stock-and-flow projection of a small mammal population {.unnumbered}

**Problem:** A field site has 200 deer mice at the start of the year. The per-capita birth rate is 0.020 per month and the per-capita death rate is 0.015 per month, with no immigration or emigration. Assume both rates stay constant for one month. Compute the net inflow into the population stock, the population at the end of the month, and the doubling time implied by the net per-capita rate.

**Solution:**

- Net per-capita rate = 0.020 − 0.015 = 0.005 per month.
- Net monthly inflow = 0.005 × 200 = 1.0 mice per month.
- End-of-month stock = 200 + 1 = 201 mice.
- Doubling time using the continuous-rate approximation t_double ≈ ln(2) / r = 0.693 / 0.005 ≈ 138.6 months (about 11.5 years).

**Interpretation:** The stock barely shifts in one month, yet the small positive net rate accumulates into a doubling time of roughly a decade — a feature of pure stock dynamics that surprises students who expect proportional intuitions to track short time-scale observations. A density-dependent term (a balancing loop tied to food, predators, or disease) would slow growth before doubling and is the kind of negative-feedback structure a richer model needs once the population approaches habitat capacity.


## Analysis Questions {.unnumbered}

1. For haemoglobin ($n \approx 2.8$), compute the difference in O$_2$ saturation between lung capillaries ($[\mathrm{O}_2] = 100\,\mathrm{mmHg}$) and active muscle capillaries ($[\mathrm{O}_2] = 20\,\mathrm{mmHg}$). Why is the steepness of the Hill curve a life-preserving property?
2. In Part 2, the ovarian-pituitary loop reverses sign across the menstrual cycle. What does this imply for the stability of the overall system, and what biological mechanism produces the sign reversal?
3. Modular design makes biological systems easier to evolve (new modules can be added without breaking old ones). Give one counter-example — a domain where modularity *constrains* evolution rather than freeing it.
4. The textbook notes that biological delays destabilise feedback. A surgical patient on a mechanical ventilator has a CO$_2$-sensing feedback loop with a built-in 10-second measurement lag. Predict what happens as you increase the loop gain; suggest one design fix.
5. Design a paper-based experiment to test whether a bacterial-population model exhibits emergent collective behaviour distinct from isolated-cell behaviour. What is the null hypothesis and what observation card would refute it?

## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A regional hospital network observes that emergency-department wait times rise sharply during winter respiratory-virus seasons. Administrators propose adding bed capacity; clinicians propose a faster discharge pathway to free beds; the public-health team proposes upstream vaccination outreach.
>
> (a) Draw a causal loop sketch (in words) of the stocks and flows linking community infections, hospital admissions, available beds, and wait times. Mark each proposed intervention with the leverage point category from the parent chapter that best matches it (for example, parameter change, feedback strength, system goal).
> (b) Predict the qualitative behaviour of the system under each proposed intervention over one winter season, and explain which intervention is most likely to shift the long-run behaviour rather than the immediate symptom. Ground the prediction in the dominant feedback loops you sketched.
> (c) Design a short measurement plan (three variables to track and one indicator of unintended consequences) that would tell the administration whether the chosen intervention reduced wait times without shifting the burden to a downstream subsystem such as primary care or home recovery.

---

## Discussion Questions {.unnumbered}

1. A reductionist insists that knowing everything about every molecule in a cell is sufficient to understand cellular behaviour. Where does systems science push back?
2. Are there systems in biology that are *not* adaptive? Propose a candidate and defend your choice.
3. The Covid-19 pandemic exposed how hospital systems behave under extreme input. Which systems-science principles explain why ICU capacity failed in some cities and not others?

---

## Safety and Ethics Notes {.unnumbered}

Paper-based lab — no reagents or instruments, no physical risk. Discussion of the menstrual cycle, labour, and ventilator management should be inclusive and accurate; seek clarification from the instructor if terminology feels unfamiliar. The Covid-19 example should be grounded in public-health data rather than anecdote.

*Module: `src/biology/cell/cell_biology.py` (`hill_equation`, `receptor_occupancy`); `src/biology/ecology/ecology.py` (`logistic_growth`).*
