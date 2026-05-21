<!-- render:skip-beamer -->

# Lab C — Active Inference and the Free Energy Principle {.unnumbered}

\label{sec:lab_unit_0_active_inference}

*This activity accompanies \cref{sec:unit_0_active_inference} of the textbook — review that chapter before attempting the exercises below.*

**Unit 0 · Lab C**

---

## Learning Objectives {.unnumbered}

- Apply core principles of active inference to concrete biological observations.
- Compute a Bayesian posterior by hand for a one-dimensional inference problem and interpret the result in terms of prior, likelihood, and evidence.
- Distinguish *perceptual* inference (updating beliefs) from *active* inference (acting to satisfy beliefs) using everyday examples.
- Quantify how sensor precision changes the trade-off between updating a belief and acting to make a belief true.

---


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Active Inference and the Free Energy Principle.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Background {.unnumbered}

Active inference proposes that living agents minimise a quantity called **variational free energy** — an upper bound on the "surprise" of observed sensory data given the agent's internal generative model. The core equation (simplified):

\begin{equation}
F \;=\; \mathbb{E}_{Q}[\,\log Q(\mathbf{z}) - \log P(\mathbf{o}, \mathbf{z})\,]
\label{eq:lab_ai_fe}
\end{equation}

where $Q(\mathbf{z})$ is the agent's current belief about hidden causes $\mathbf{z}$, and $P(\mathbf{o}, \mathbf{z})$ is the agent's model of how those causes generate observations $\mathbf{o}$. Minimising $F$ is achieved either by **updating beliefs** (perceptual inference) or **changing the world through action** (active inference).

Today's lab is paper-based: you will work through two hand-computed examples and one behaviour-card classification exercise. No computer is required, though a calculator (or phone app) is useful for the Gaussian arithmetic.

---

## Pre-Lab (to complete before class) {.unnumbered}

1. Copy \cref{eq:lab_ai_fe} into your notebook and annotate each symbol.
2. For a Gaussian prior $\mathcal{N}(\mu_0, \sigma_0^2)$ and Gaussian likelihood $\mathcal{N}(o, \sigma_o^2)$, write the closed-form posterior mean and variance.
3. Choose one everyday example of *perceptual inference* and one of *active inference* that you could describe in two sentences each. You will compare them with the scenario cards during Part 3.

---

## Paper-Based Materials {.unnumbered}

- Printed worksheet with two Bayesian inference problems (provided).
- Behaviour scenario-card set with ten animal and human examples.
- Calculator or phone.
- Coloured pens.

---

## Paper-Based Investigation {.unnumbered}

### Part 1 — Hand-computed Bayesian Update {.unnumbered}

A bird forages for seeds hidden under two snow patches. Its prior belief about the location of food is a Gaussian centred at position $\mu_0 = 10$ m (where food was yesterday) with variance $\sigma_0^2 = 4\,\mathrm{m}^2$. A partial snow melt gives a noisy visual cue that food is at position $o = 16$ m with likelihood variance $\sigma_o^2 = 12\,\mathrm{m}^2$.

1. Compute the **prediction error**: $\varepsilon = o - \mu_0$.
2. Compute the **Kalman gain**: $K = \sigma_0^2 / (\sigma_0^2 + \sigma_o^2)$.
3. Compute the **posterior mean**: $\mu_1 = \mu_0 + K \, \varepsilon$.
4. Compute the **posterior variance**: $\sigma_1^2 = (1 - K) \, \sigma_0^2$.
5. Re-compute $\mu_1$ under the assumption that the cue is *very* noisy ($\sigma_o^2 = 100$) and *very* precise ($\sigma_o^2 = 0.5$). Explain in words how the bird's final belief depends on sensor precision.

### Part 2 — Perceptual vs. Active Inference {.unnumbered}

A person wakes up cold. Their generative model has a tight prior on body temperature ($\mu = 37$ °C, $\sigma = 0.5$). Their interoceptive sensor reports 34.5 °C with $\sigma = 1.0$.

1. Compute the posterior belief about their body temperature (same formulae as Part 1).
2. The posterior free energy is reduced but still positive. List **three actions** the person could take that would drive free energy further toward zero by *changing the observation* rather than the belief.
3. Argue in one paragraph why active inference is more effective than perceptual inference when the prior precision is tight (small $\sigma_0$) — i.e., when the organism is "committed" to a particular internal state.

### Part 3 — Behaviour Scenario Classification {.unnumbered}

Use the ten printed behaviour scenario cards. For each behaviour, annotate whether it is perceptual (sampling information) or active (imposing prediction on the environment). Record the evidence phrase that made your classification reproducible. As an optional extension outside class, you may compare the cards with a respectful observation of an animal or consenting human, but the scenario cards are the required dataset.

---

## Data Tables {.unnumbered}

| Step | Quantity | Symbol | Computed value | Units |
| ---- | -------- | ------ | -------------- | ----- |
| 1 | Prediction error | $\varepsilon$ | | m |
| 2 | Kalman gain | $K$ | | — |
| 3 | Posterior mean | $\mu_1$ | | m |
| 4 | Posterior variance | $\sigma_1^2$ | | m² |
| 5a | $\mu_1$ with very noisy cue | | | m |
| 5b | $\mu_1$ with very precise cue | | | m |

| Observation # | Behaviour described | Perceptual or active? | Brief reasoning |
| ------------- | ------------------- | --------------------- | --------------- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model sensing and action as coupled inference in a simple organism.
- **Data skill to practice:** Read a small probability table and update a prediction after new evidence.
- **BioSkills emphasis:** Modeling and simulation, Process of science, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Active Inference and the Free Energy Principle** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: When you annotate the Bayesian-update and perceptual-versus-active-inference datasets, the load-bearing numbers are the prior variance, the sensory variance, and the resulting Kalman gain: check that the posterior shift is reproducible from those three values alone, and that each behaviour-classification verdict cites the specific prediction-error a sceptic could recompute. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. Explain in one paragraph how the Kalman gain can be read as "precision-weighted uncertainty reduction" — why $K$ depends on the ratio of prior variance to total variance.
2. The generative model in Part 2 uses a *tight* prior (low variance) on body temperature. How would the calculation change if the prior were loose ($\sigma = 5$ °C)? Which regime corresponds to a pre-homeostatic organism; which to a strictly regulated endotherm?
3. In humans, chronic anxiety is sometimes described as a "tight prior on safety." Using your computation from Part 2, explain why normal day-to-day sensory noise becomes persistently surprising to an anxious agent and what "widening the prior" (via exposure therapy or pharmacology) is doing mathematically.
4. Scientists have attempted to build artificial life — robots that minimise free energy with respect to a battery-level sensor. Describe what the agent's **prior** on battery state and **action repertoire** would need to be so that the robot "feels hungry" at low charge and seeks a charging pad.
5. The textbook chapter notes that evolution itself can be cast as free-energy minimisation at the population scale: organisms whose generative models fail are eliminated. Argue for or against this framing by contrasting it with the Modern Synthesis's emphasis on fitness differentials.

---

## Discussion Questions {.unnumbered}

1. Is "surprise" a purely mathematical quantity, or does it have phenomenal correlates? Consider how a newborn infant's surprise differs from an adult's when encountering the same stimulus.
2. Could two agents with identical sensory input hold different beliefs and both be rational under active inference? If yes, what determines each?
3. Does the free-energy principle predict that living things should seek complexity or simplicity in their environments? Justify using the trade-off between epistemic and instrumental value.

---

## Safety and Ethics Notes {.unnumbered}

This lab is entirely paper-based and computational — no reagents, no instruments, no risk. Optional observations outside class must not disturb animals. If recording human behaviour, obtain consent and preserve anonymity.

*Module: `src/biology/neuroscience/neuroscience.py` (Bayesian update illustrations).*
