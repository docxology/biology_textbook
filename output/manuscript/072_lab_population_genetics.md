<!-- render:skip-beamer -->

# Lab 18 — Population Genetics and Hardy-Weinberg Equilibrium {.unnumbered}

\label{sec:lab_unit_V_population_genetics}

## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_V_population_genetics} of the textbook — review that chapter before attempting the exercises below.*

- Apply Hardy-Weinberg equations to calculate allele and genotype frequencies from population data
- Test for deviations from HWE using chi-square analysis
- Simulate the effect of genetic drift on small vs large populations using a bead model
- Evaluate the effect of natural selection on allele frequencies across generations


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Population Genetics and Hardy-Weinberg Equilibrium.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Background {.unnumbered}

The Hardy-Weinberg principle states that in a large, randomly mating population with no selection, mutation, migration, or drift, allele frequencies (p, q) and genotype frequencies (p², 2pq, q²) remain constant across generations. Deviations from HWE indicate one or more of these forces is acting. Genetic drift — random changes in allele frequency — is most powerful in small populations, causing loss of variation and potentially fixing or eliminating alleles by chance alone.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Two colours of beads (representing A and a alleles): 50 of each colour | 100 total |
| Opaque bag or cup (for random sampling) | 2 |
| Population genetics data table (printed: real MN blood group data) | 1 |
| Calculator | 1 |
| Chi-square critical value table | 1 |
| Graph paper | 1 |

## Paper-Based Investigation {.unnumbered}

**Part A — Hardy-Weinberg Calculation**

1. Using the provided MN blood group data (genotype counts **MM = 298, MN = 489, NN = 213**, from a sample of *n* = 1000; classic combined US-Caucasian MN blood-group survey, as reproduced in standard population-genetics texts): calculate allele frequencies *p* (M) and *q* (N). *(Check: p(M) ≈ 0.5425, q(N) ≈ 0.4575.)*
2. Calculate expected genotype frequencies under HWE (p², 2pq, q²) and expected counts.
3. Perform chi-square test to determine whether the population is in HWE.

**Part B — Genetic Drift Simulation**

4. Place 50 red (A) and 50 blue (a) beads in the bag: this represents a population of 100 with p = q = 0.5.
5. Without looking, draw 10 beads (simulating a bottleneck to N=10). Record the frequency of red (A) beads drawn. Then **discard the old bag and rebuild a fresh 100-bead pool at the drawn allele ratio**: multiply the observed red fraction by 100, round to the nearest whole bead, and use that many red beads with the remainder blue (e.g. 6/10 red → 60 red + 40 blue). Repeat the draw–rebuild cycle for 5 generations, recording *p* (red fraction) each generation.
6. A second group runs the same simulation with N=50 (draw 50 beads, then rebuild a 100-bead pool at the drawn allele ratio by the same rounding rule) for 5 generations.

**Part C — Selection Simulation (Optional)**

7. In generation 1 of the drift simulation, designate aa (2 blue drawn) as lethal — remove any drawn aa pairs and resample. Track p over 3 generations.

## Data Recording {.unnumbered}

MN blood group HWE test (observed counts from the *n* = 1000 sample: MM = 298, MN = 489, NN = 213; source: classic combined US-Caucasian MN blood-group survey reproduced in standard population-genetics texts):

| Genotype | Observed | p or q | Expected | (O−E)²/E |
| -------- | -------- | ------ | -------- | --------- |
| MM | 298 | p² = | | |
| NN | 213 | q² = | | |
| MN | 489 | 2pq = | | |
| **Total** | **1000** | — | **1000** | χ² = ___ |

Fill the *Expected* column using your calculated *p* and *q* (Part A), then χ² = Σ (O−E)²/E.

χ² = ___; df = 1; HWE at α = 0.05? (Y/N) — compare χ² to the critical value 3.841.

Drift simulation:

| Generation | p (N=10 group) | p (N=50 group) |
| ---------- | -------------- | -------------- |
| 0 | 0.5 | 0.5 |
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Test equilibrium and model allele-frequency change.
- **Data skill to practice:** Estimate genotype or allele frequencies from population data.
- **BioSkills emphasis:** Quantitative reasoning, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Population Genetics and Hardy-Weinberg Equilibrium** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab the simulated allele-frequency series across generations are the evidence — compare observed genotype counts against the Hardy-Weinberg expectation and contrast small versus large N to attribute change to drift, selection, or sampling. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. Was the MN blood group population in HWE? Which of the HWE assumptions might be violated in a real human population, and how would each violation shift allele frequencies over generations?
2. Was there more variation in allele frequency across generations in the N=10 or N=50 group? Define genetic drift in terms of sampling error and explain why population size affects drift magnitude.
3. Founder effect: a group of 20 individuals colonises a new island. By chance, the founding group contains no aa individuals. Even without selection against aa, will this condition persist? Explain using HWE and the concept that mutation-selection equilibrium is absent if frequency starts at zero.
4. Heterozygote advantage: sickle-cell anaemia (aa) is lethal, but carriers (Aa) are more resistant to malaria than AA homozygotes. With the heterozygote Aa as the fittest genotype, let *s* be the selection coefficient against AA and *t* the selection coefficient against aa (relative fitnesses 1−*s* : 1 : 1−*t*). The stable equilibrium allele frequency of *a* is **q̂ = s / (s + t)**. For a malarious region with *s* = 0.2 (AA disadvantage) and *t* = 1 (aa lethal), compute q̂ and interpret why the *a* allele persists in the population despite being lethal in homozygotes.
5. A conservation biologist studying a population of 25 cheetahs finds they are almost completely genetically homogeneous (very low heterozygosity). Explain two consequences of this for: (a) short-term disease resistance; (b) long-term adaptive capacity. What management intervention would restore genetic variation?

## Safety and Ethics Notes {.unnumbered}

No chemical hazards. Beads present a swallowing hazard — do not use with young children. When discussing human population genetics data (e.g., blood groups by ethnicity), maintain scientific objectivity and avoid discriminatory interpretation.

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
   \cref{sec:unit_V_population_genetics} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_V_population_genetics} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_V_population_genetics}`; all numerical
quantities in this lab use SI units — see Appendix D of the textbook for
unit conversions and biological-scale reference values.*
