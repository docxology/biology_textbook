# Lab 32 — Population Ecology and Growth Models {.unnumbered}

\label{sec:lab_unit_X_population_ecology}

## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_X_population_ecology} of the textbook — review that chapter before attempting the exercises below.*

- Fit logistic and exponential growth equations to real or simulated population data
- Calculate intrinsic rate of increase (r) and carrying capacity (K) from population time series
- Apply the mark-recapture method (Lincoln-Petersen) to estimate population size
- Evaluate density-dependent vs density-independent limiting factors from case study data


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Population Ecology and Growth Models.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Write the logistic growth equation dN/dt = rN(K − N)/K. Define each symbol and describe in two sentences what happens to dN/dt as N approaches K from below and from above.
2. Distinguish density-dependent from density-independent regulation, giving one biological example of each. State which type of regulation would more plausibly stabilise a population near its carrying capacity over time.
3. Sketch the three classic survivorship curves (Types I, II, III) and identify one organism whose life history matches each. In one sentence per type, explain how the curve's shape reflects the timing of mortality across the life cycle.

## Background {.unnumbered}

Population growth follows exponential growth (dN/dt = rN) when resources are unlimited, and logistic growth (dN/dt = rN(1 − N/K)) as populations approach the carrying capacity K. Real populations fluctuate around K due to density-dependent factors (competition, predation, disease — intensify as N increases) or may crash due to density-independent factors (storms, droughts — unrelated to N). The Lincoln-Petersen mark-recapture estimate: N̂ = (M × C) / R, where M = initial marked individuals, C = recapture sample size, R = recaptured marked individuals.

The logistic-growth projection worked example in the parent chapter (\cref{sec:unit_X_population_ecology}) shows that with $r = 0.2$/yr and $K = 1000$, a population starting at $N_0 = 100$ reaches roughly 451 at $t = 10$ and 858 at $t = 20$, illustrating the S-curve's characteristic acceleration below $K/2$ and deceleration above it. This lab generates analogous growth data so students can test which model (exponential vs. logistic) better fits observed population trajectories.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Population time series data (printed: 3 species — moth (exponential), snowshoe hare (oscillating), logistic yeast) | 1 |
| Graph paper or spreadsheet template | 1 |
| Calculator | 1 |
| Mark-recapture card deck or printed capture-history table | 1 |
| Management scenario cards for invasive species, harvested fisheries, and climate-driven range shifts | 1 set |

## Paper-Based Investigation {.unnumbered}

**Part A — Growth Curve Fitting**

1. Plot the three population time series on graph paper. For the yeast data, identify: lag phase, exponential phase, plateau (K).
2. Estimate K from the plateau of the logistic curve.
3. Estimate r from the exponential phase: r ≈ (ln N₂ − ln N₁) / (t₂ − t₁) during the period of fastest growth.

**Part B — Mark-Recapture**

4. Use the printed capture-history table: M = 50 initially marked individuals and C = 30 individuals in the recapture sample. Count the marked recaptures (R) in the table and calculate Nhat = (50 x 30) / R.
5. Repeat the calculation for the second printed sampling event. Compare both estimates with the known simulated population size and calculate percent error.

**Part C — Density Dependence Analysis**

6. Given data on white-tailed deer population growth rate (r) vs density in 4 regions: plot r vs N/K (relative density). Identify whether r decreases with increasing density (density-dependent regulation) — this confirms a logistic pattern.

## Data Recording {.unnumbered}

Logistic yeast data:

| Time (h) | Population (cells/mL) | ln N |
| -------- | --------------------- | ----- |
| 0 | 10 | |
| 6 | 80 | |
| 12 | 410 | |
| 18 | 1,200 | |
| 24 | 2,800 | |
| 36 | 3,900 | |
| 48 | 4,100 | |

Estimated K = ___; Estimated r = ___

Mark-recapture: M = 50; C = 30; R = ___; N̂ = ___
Second sampling estimate: R = ___; N̂ = ___; percent error from known simulated N = ___%

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model population trajectories and compare sampling methods.
- **Data skill to practice:** Use abundance or age-structure data to estimate growth and risk.
- **BioSkills emphasis:** Modeling and simulation, Science and society, Communication and collaboration.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Population Ecology and Growth Models** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: for this population lab, state the demographic model behind each printed estimate (exponential, logistic, or mark-recapture), check whether its assumptions about density dependence, closure, and detection hold for the simulated capture histories, and tie any harvest or recovery conclusion to an explicit management objective. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Logistic Growth Rate Below Carrying Capacity {.unnumbered}

**Problem:** A population growing under logistic dynamics has intrinsic growth rate r = 0.18/yr and carrying capacity K = 1,200. The current population size is N = 300. (a) Calculate the instantaneous growth rate dN/dt. (b) Estimate N after one year using the Euler approximation N_1 ≈ N_0 + (dN/dt) × Δt with Δt = 1 yr. (c) Compute (K − N)/K and interpret what fraction of the logistic "brake" is currently engaged.

**Solution:** (a) dN/dt = r × N × (K − N)/K = 0.18 × 300 × (1,200 − 300)/1,200 = 0.18 × 300 × 0.75 = 40.5 individuals/yr. (b) N_1 ≈ 300 + 40.5 × 1 = 340.5 individuals — round down to 340 for a discrete count. (c) (K − N)/K = 900/1,200 = 0.75, so the population is at 25% of K and the density-dependent brake (1 − N/K) is still 0.75 of its maximum.

**Interpretation:** The population is in its near-exponential phase: most of the logistic term (K − N)/K is still close to 1, so growth is fast relative to the rate it will show near K. As N rises toward K, the brake term shrinks toward zero and dN/dt falls smoothly to zero at N = K. The Euler step is acceptable for one-year projections at low N relative to K, but it overshoots the true logistic trajectory when N grows enough within the year to change the brake substantially.

## Analysis Questions {.unnumbered}

1. Why does the yeast population growth slow as it approaches K? Use the term "intraspecific competition" and identify two specific density-dependent resources that become limiting.
2. Snowshoe hare populations cycle with ~10-year periodicity (tied to lynx cycles). Is this best explained as: (a) density-dependent predation; (b) density-independent weather events; or (c) a two-species coupled oscillator? Describe the evidence.
3. Your two mark-recapture estimates probably differed slightly. List three assumptions of the Lincoln-Petersen method and explain which assumption is most likely violated in the printed capture-history simulation.
4. Invasive species often exhibit exponential growth in new habitats. Name a specific invasive species, identify what density-dependent factor is absent in the new habitat, and predict when/how logistic behaviour will eventually emerge.
5. Apply a fisheries management scenario: a cod population has K = 500,000 tonnes and r = 0.2/year. Using the maximum sustainable yield formula (MSY = rK/4), calculate the MSY and the population size at MSY (N = K/2). If fishing reduces the population below K/4, explain why the population will continue to decline even if fishing stops.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A species with a Type III survivorship curve produces many offspring but has high juvenile mortality and relatively high adult survival once individuals reach reproductive age. A manager must choose between two interventions: (i) protecting juveniles (e.g., headstarting hatchlings, predator exclusion at nurseries) or (ii) protecting adults (e.g., reducing bycatch of reproductive individuals).
>
> (a) Using reproductive-value theory, predict which intervention is likely to produce faster population recovery in a Type III species. Explain why the reproductive value of an adult, particularly a prime-aged breeder, tends to outweigh that of an individual juvenile, and tie the argument to how reproductive value typically peaks near the age of first reproduction.
> (b) Identify one situation in which the juvenile-protection strategy would still be the preferred choice — for example, when adult mortality is already low and juvenile survival is the demographic bottleneck. Propose one measurement from the lab's life-table analysis that would help a manager decide between the two strategies in practice.

## Safety and Ethics Notes {.unnumbered}

No hazardous materials or living specimens are required. When discussing harvested or invasive species, maintain ecological objectivity and identify uncertainty in population estimates.

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
   \cref{sec:unit_X_population_ecology} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_X_population_ecology} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_X_population_ecology}`; all numerical
quantities in this lab use SI units — see \cref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
