# Lab C — Active Inference and Free Energy {#sec:lab_unit_0_active_inference .unnumbered}


*This activity accompanies \cref{sec:unit_0_active_inference} of the textbook — review that chapter before attempting the exercises below.*

**\nameref{sec:unit_0_unit_intro} · Lab C**

---

## Learning Objectives {.unnumbered}

- Apply core principles of active inference to concrete biological observations.
- Compute a Bayesian posterior by hand for a one-dimensional inference problem and interpret the result in terms of prior, likelihood, and evidence.
- Distinguish *perceptual* inference (updating beliefs) from *active* inference (acting to satisfy beliefs) using everyday examples.
- Quantify how sensor precision changes the trade-off between updating a belief and acting to make a belief true.

---



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO2):** Compute Gaussian posterior means, variances and sensor-precision effects.
- **Outcome 2 (LO3):** Separate belief revision, epistemic action and state-restoring action in ten cards.
- **Outcome 3 (LO4):** Explain the temperature model without claiming clinical prediction.
- **Outcome 4 (LO6):** Compare information-seeking and goal-directed policies using explicit costs.
- **Chapter LO coverage:** LO2, LO3, LO4, LO6
- **Rubric dimensions (12 points total):** Score the following five categories; correct labels without the specified work do not earn full credit.
  - **Evidence — 4 points (LO2, LO3, LO4):** Award 2 for showing prediction error, gain, posterior mean and variance for the food and temperature updates with length/temperature versus squared units distinguished, including the changed sensory variances and loose temperature prior; award 2 for coding all ten cards with reasons identifying the operation, including E then A on card 10. Credit defensible multiple codes only when separate operations are described.
  - **Controls — 2 points (LO2, LO6):** Award 1 for comparing sensory-variance cases while holding the food prior and cue location fixed, and 1 for a policy comparison that holds motor cost constant while changing cue informativeness. Merely naming a control earns no point without its held and changed variables.
  - **Uncertainty — 2 points (LO4, LO6):** Award 1 for explaining that the temperature posterior depends on assumed sensor/prior errors rather than establishing homeostatic status, and 1 for explaining why a free-energy bound at fixed data need not approach zero and why the stipulated policy score is not a validated biological model.
  - **Mechanism — 2 points (LO2, LO3, LO4):** Award 1 for connecting increased sensory precision to the larger gain and posterior shift, and 1 for distinguishing belief revision, new sampling and warming actions by what each changes. Warming must change future observations, not retrospectively change the fixed observation.
  - **Transfer — 2 points (LO6):** Award 1 for calculating the three policy scores in each information condition and explaining the warming-to-inspection switch, and 1 for using the packet's stimulus-response rival to state why the same behavior alone cannot establish active inference. A policy preference without the cost/information comparison earns no calculation credit.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Describe in your own words how Bayes' rule combines a prior belief with an observation to produce a posterior belief, and identify which term carries the "what I already thought" information.
2. A foraging mouse has a prior expectation that food is at burrow A. It sees a faint scent cue pointing to burrow B. Apply the idea of prediction error to explain how the mouse should update its belief, and identify which sensor property determines how much the cue moves the belief.
3. Compare perceptual inference (updating beliefs to match observations) with active inference (acting on the environment so observations match beliefs). Give one biological situation where each is the more efficient route to reducing prediction error.

## Lab Context: Active Inference and Free Energy {.unnumbered}

Active inference proposes that living agents minimize a quantity called **variational free energy** — an upper bound on the "surprise" of observed sensory data given the agent's internal generative model. The core equation (simplified):

\begin{equation}
F \;=\; \mathbb{E}_{Q}[\,\log Q(\mathbf{z}) - \log P(\mathbf{o}, \mathbf{z})\,]
\label{eq:lab_ai_fe}
\end{equation}

where $Q(\mathbf{z})$ is the agent's current belief about hidden causes $\mathbf{z}$, and $P(\mathbf{o}, \mathbf{z})$ is the agent's model of how those causes generate observations $\mathbf{o}$. Minimizing $F$ is achieved either by **updating beliefs** (perceptual inference) or **changing the world through action** (active inference).

Today's lab is paper-based: you will work through two hand-computed examples and one behavior-card classification exercise. No computer is required, though a calculator (or phone app) is useful for the Gaussian arithmetic.

---

## Pre-Lab (to complete before class) {.unnumbered}

1. Copy \cref{eq:lab_ai_fe} into your notebook and annotate each symbol.
2. For independent Gaussian prior and likelihood errors, use $K=\sigma_0^2/(\sigma_0^2+\sigma_o^2)$, $\mu_1=\mu_0+K(o-\mu_0)$ and $\sigma_1^2=(1-K)\sigma_0^2$. Identify the units of each quantity.
3. Choose one everyday example of *perceptual inference* and one of *active inference* that you could describe in two sentences each. You will compare them with the scenario cards during Part 3.

---

## Paper-Based Materials {.unnumbered}

- Source-governance card for Active Inference and Free Energy: model-validation source card: boundary, observable, uncertainty, rival explanation, and evidence limit.
- Printed worksheet with two Bayesian inference problems (provided).
- Behavior scenario-card set with ten animal and human examples.
- Calculator or phone.
- Colored pens.

---

## Paper-Based Investigation {.unnumbered}

### Part 1 — Hand-computed Bayesian Update {.unnumbered}

A bird forages for seeds hidden under two snow patches. Its prior belief about the location of food is a Gaussian centered at position $\mu_0 = 10$ m (where food was yesterday) with variance $\sigma_0^2 = 4\,\mathrm{m}^2$. A partial snow melt gives a noisy visual cue that food is at position $o = 16$ m with likelihood variance $\sigma_o^2 = 12\,\mathrm{m}^2$.

1. Compute the **prediction error**: $\varepsilon = o - \mu_0$.
2. Compute the **Kalman gain**: $K = \sigma_0^2 / (\sigma_0^2 + \sigma_o^2)$.
3. Compute the **posterior mean**: $\mu_1 = \mu_0 + K \, \varepsilon$.
4. Compute the **posterior variance**: $\sigma_1^2 = (1 - K) \, \sigma_0^2$.
5. Re-compute $\mu_1$ under the assumption that the cue is *very* noisy ($\sigma_o^2 = 100$) and *very* precise ($\sigma_o^2 = 0.5$). Explain in words how the bird's final belief depends on sensor precision.

### Part 2 — Perceptual vs. Active Inference {.unnumbered}

A person wakes up cold. Their generative model has a tight prior on body temperature ($\mu = 37$ °C, $\sigma = 0.5$). Their interoceptive sensor reports 34.5 °C with $\sigma = 1.0$.

1. Compute the posterior belief about their body temperature (same formulae as Part 1).
2. List three hypothetical warming actions and explain how they would change future observations. A bound evaluated at fixed data need not approach zero, and changing the observation changes the evidence; no numerical free-energy calculation is required for this case.
3. Explain why prior precision affects the posterior but does not alone determine the best action: movement costs, safety and alternative models also matter. This is not advice for treating hypothermia.

### Part 3 — Behavior Scenario Classification {.unnumbered}

Use the ten printed cards below. Code P for belief updating at fixed data, E for epistemic action that samples new data, and A for state-restoring action. More than one code is acceptable only when separate operations are identified. A behavior description does not prove that an organism implements active inference.

### Part 4 — Explicit Policy Comparison {.unnumbered}

Use a dimensionless synthetic score $G=\text{cost}-\text{information}$, choosing the lowest value: waiting (cost 2, information 0), inspecting (2.5, 1), warming (0.5, 0). Calculate all scores, then change only inspection information to 3 and compare again. Propose a control holding motor cost constant while cue informativeness changes. This stipulated score is not a fitted biological policy or a complete derivation of expected free energy.

---

## Data Tables {.unnumbered}

: Gaussian food-location update and sensory-variance worksheet. {#tbl:unit_0_active_inference_part_3_behaviour_scenario_classification}
| Step | Quantity | Symbol | Computed value | Units |
| ---- | -------- | ------ | -------------- | ----- |
| 1 | Prediction error | $\varepsilon$ | | m |
| 2 | Kalman gain | $K$ | | — |
| 3 | Posterior mean | $\mu_1$ | | m |
| 4 | Posterior variance | $\sigma_1^2$ | | m² |
| 5a | $\mu_1$ with very noisy cue | | | m |
| 5b | $\mu_1$ with very precise cue | | | m |

: Classification worksheet for all ten synthetic behavior cards. {#tbl:unit_0_active_inference_part_3_behaviour_scenario_classification_2}
| Observation # | Behavior described | P, E or A | Brief reasoning |
| ------------- | ------------------- | --------- | --------------- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

Temperature worksheet: $K=$ ____; posterior mean ____ °C; posterior variance ____ °C². Record the loose-prior comparison separately.
---

## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model sensing and action as coupled inference in a simple organism.
- **Data skill to practice:** Read a small probability table and update a prediction after new evidence.
- **BioSkills emphasis:** Modeling and simulation, Process of science, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Active Inference and Free Energy** with a reproducibility pass:

: Evidence and reproducibility decisions for inference models and behavior cards. {#tbl:unit_0_active_inference_part_3_behaviour_scenario_classification_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: When you annotate the Bayesian-update and perceptual-versus-active-inference datasets, the load-bearing numbers are the prior variance, the sensory variance, and the resulting Kalman gain: check that the posterior shift is reproducible from those three values alone, and that each behavior-classification verdict cites the specific prediction-error a sceptic could recompute. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Source-Governance Checkpoint {.unnumbered}

**Printed governance card A1:** Synthetic illustrative scenarios and Gaussian models, one specified case per card; no measured participants or biological replicates. Baseline = unchanged prior and no action; rival = a stimulus-response controller. Model inputs and likelihood assumptions, not a clinical diagnosis, determine the numerical key. Refresh trigger = biased or correlated sensory errors.

**Ten behavior cards:** 1. A bird revises food position after viewing a fixed photograph. 2. A bird turns its head to view a concealed patch. 3. A cold mouse enters a warm nest. 4. A person revises an estimate after reading an already available thermometer. 5. A person takes a second temperature measurement. 6. A robot moves to a charger to raise battery level. 7. A robot scans two rooms to locate a charger. 8. A moth updates its location estimate after a fixed odor pulse. 9. A mouse approaches two equally accessible food patches to learn which is replenished. 10. A person first tests bath water with a finger, then adds warm water. These are synthetic descriptions, not observations of real individuals.

**Instructor key:** Cards 1,4,8=P; 2,5,7,9=E; 3,6=A; 10=E then A. Information sampling is action, not passive belief revision. Part 1: error 6 m, gain 0.25, mean 11.5 m, variance 3 m^2; with variance 100 the mean is 10.2308 m, and with variance 0.5 it is 15.3333 m. Part 2: mean 36.5 degrees C, variance 0.20 degrees C^2; a loose prior variance 25 gives mean 34.5962 degrees C. Neither is evidence of an organism's homeostatic status. For policy comparison use synthetic G=cost-information: waiting (2-0=2), inspecting (2.5-1=1.5), warming (0.5-0=0.5); warming wins only under those stated costs. If inspection information becomes 3, inspection gives -0.5 and wins. A fair control holds motor cost constant while changing cue informativeness.

### Worked Example: Bayesian update of a discrete food-location belief {.unnumbered}

**Problem:** A bird has a discrete prior probability of 0.3 that food is under patch A (the complement, 0.7, is patch B). It receives a noisy visual cue. The likelihood that this cue appears when food is at A is 0.8; the likelihood the cue appears when food is at B is 0.2. Compute the posterior probability that food is at patch A.

**Solution:** Apply Bayes' rule, P(A | cue) = P(cue | A) · P(A) / P(cue), where the evidence P(cue) = P(cue | A)·P(A) + P(cue | B)·P(B).

- Numerator: 0.8 × 0.3 = 0.24.
- Evidence: (0.8 × 0.3) + (0.2 × 0.7) = 0.24 + 0.14 = 0.38.
- Posterior: 0.24 / 0.38 ≈ 0.632.

**Interpretation:** The cue raises P(A) from 0.3 to about 0.632; using likelihoods 0.95 and 0.05 instead gives 0.890625. This is an explicit Bayesian statistical model. Its resemblance to predictive-processing accounts motivates experiments, but the calculation does not establish that every sensory neuron implements this update.


## Analysis Questions {.unnumbered}

1. Explain in one paragraph how the Kalman gain can be read as "precision-weighted uncertainty reduction" — why $K$ depends on the ratio of prior variance to total variance.
2. Recalculate Part 2 with prior sigma=5 degrees C. Explain why a different statistical prior is not by itself evidence that an organism lacks homeostatic regulation.
3. Explain how biased sensing and a precise threat prior could produce similar choices in a toy anxiety model. Propose a reliability manipulation that distinguishes them without claiming the model establishes a treatment mechanism.
4. Scientists have attempted to build artificial life — robots that minimize free energy with respect to a battery-level sensor. Describe what the agent's **prior** on battery state and **action repertoire** would need to be so that the robot "feels hungry" at low charge and seeks a charging pad.
5. The textbook chapter notes that evolution itself can be cast as free-energy minimization at the population scale: organisms whose generative models fail are eliminated. Argue for or against this framing by contrasting it with the Modern Synthesis's emphasis on fitness differentials.

## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A neuroscientist studies a deep-sea fish that lives in near-total darkness and rarely encounters novel visual stimuli. The fish has unusually large lateral-line organs (which detect water displacement) and a small optic tectum.
>
> (a) Using the active-inference framework, predict which sensory channel will carry the higher precision-weighting in this animal's generative model, and explain how you would test that prediction with a behavioral assay rather than neural recording.
> (b) A traditional stimulus–response account would describe the fish as "tuned" to mechanical cues by selection. Contrast that explanation with an active-inference account that emphasizes ongoing belief updating. Which framework yields the more falsifiable prediction for what happens when the fish is moved into a visually rich tank?
> (c) Design one follow-up experiment that would distinguish a population-level adaptation (a fixed generative model shaped by selection) from a within-lifetime adjustment (the animal re-weighting precision as it gathers evidence in the new environment).

---

## Discussion Questions {.unnumbered}

1. Is "surprise" a purely mathematical quantity, or does it have phenomenal correlates? Consider how a newborn infant's surprise differs from an adult's when encountering the same stimulus.
2. Could two agents with identical sensory input hold different beliefs and both be rational under active inference? If yes, what determines each?
3. Does the free-energy principle predict that living things should seek complexity or simplicity in their environments? Justify using the trade-off between epistemic and instrumental value.

---

## Safety and Ethics Notes {.unnumbered}

This lab is entirely paper-based and computational — no reagents, no instruments, no risk. Optional observations outside class must not disturb animals. If recording human behavior, obtain consent and preserve anonymity.

*Module: `src/biology/neuroscience/neuroscience.py` (Bayesian update illustrations).*
