# Lab — Evolution — Theory, Natural Selection, and Adaptation {#sec:lab_unit_VI_evolution_and_selection .unnumbered}


*This activity accompanies \cref{sec:unit_VI_evolution_and_selection} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate a natural selection simulation to measure selection coefficients
- Formulate testable hypotheses about how environmental change affects allele frequencies
- Identify independent, dependent, and controlled variables in evolutionary experiments
- Analyze experimental data using fitness calculations and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Evolution — Theory, Natural Selection, and Adaptation.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define relative fitness w and the selection coefficient s for a single locus with two alleles. Show how the two are related (s = 1 − w for the less-fit genotype), and describe how each quantity is estimated empirically from survival or reproductive data in a controlled experiment.
2. Distinguish directional selection from stabilizing selection, and give one biological example of each. For each, describe the expected change over time in the population mean and variance of the affected trait, and identify the conditions under which the mode of selection might shift from one to the other.
3. Describe how standing genetic variation differs from new mutation as a source of adaptive change. Explain why standing variation can drive a faster response when the environment shifts, and identify at least one population-genetic signature (such as a soft sweep) that tends to accompany this mode of adaptation.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of natural selection, predict how a change in environment (e.g., from green to brown background) would affect the survival of different colored prey. Write a clear, testable hypothesis.

2. **Experimental Design**: What is the independent variable in a natural selection simulation? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: The selection coefficient (s) quantifies the fitness cost of a genotype. Why is this measure important in evolutionary biology? How does it relate to the rate of evolutionary change?

4. **Quantitative Reasoning**: If a genotype has a relative fitness of 0.8, what is its selection coefficient? If the initial frequency of this genotype is 0.3, what would you expect its frequency to be after one generation of selection?

5. **Real-World Application**: Antibiotic resistance is a classic example of natural selection. How does the overuse of antibiotics create selection pressure for resistant bacteria? What can be done to slow this process?

## Lab Context: Evolution — Theory, Natural Selection, and Adaptation {.unnumbered}

Natural selection operates when three conditions are met: (1) heritable variation exists; (2) variation affects survival/reproduction (fitness); (3) traits are inherited. Over generations, favorable alleles increase in frequency (directional selection), multiple phenotypes are maintained (balancing/disruptive selection), or variation is reduced around an optimum (stabilizing selection). The selection coefficient *s* quantifies fitness cost: a lethal allele has s = 1.0; a neutral allele has s = 0.

The breeder's equation ($R = h^2 S$) worked example in the parent chapter (\cref{sec:unit_VI_evolution_and_selection}) provides a quantitative framework for predicting selection response: with $h^2 = 0.4$ and $S = 10$ bristles, the predicted response is roughly 4 bristles per generation, decelerating as additive genetic variance depletes. This lab uses the selection coefficient $s$ to track allele-frequency change — a complementary population-level view of the same process.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_VI_evolution_and_selection_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Evolution — Theory, Natural Selection, and Adaptation: evolutionary-evidence source card: alternative hypotheses, sampling, calibration, and confidence boundary | 1 |
| Colored paper squares (30 each of: green, red, brown, on green and brown backgrounds) | 1 set |
| Forceps (one per student, simulating different beak types) | 4 |
| 60-second timer | 1 |
| Ruler | 1 |
| Darwin's finch beak data table (printed: beak depth vs seed hardness across 14 species) | 1 |
| Selection data table (survival rates by genotype in two environments) | 1 |
| AMR allele-frequency dataset across simulated antibiotic gradients | 1 |
| Resistance policy decision matrix | 1 |
| Calculator | 1 |
| Calculator or optional Python REPL with this project installed | 1 |
| Graph paper | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Predator-Prey Selection Simulation {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how different colored prey will survive on different colored backgrounds.

2. **Identify Variables**:
   - Independent variable: Prey color and background color
   - Dependent variable: Survival rate (% of prey consumed or surviving)
   - Controlled variables: Foraging time, number of prey, predator type, etc.

3. **Set Up Controls**: Why is it important to have a control background (e.g., green prey on green background)? What other controls could you include in a predation simulation?

4. **Data Collection**:
   - Scatter 90 colored squares randomly across a green (grassy) background table.
   - Students "forage" for 30 seconds using forceps, prioritizing whatever they can pick up fastest (competitive foraging).
   - Count survivors in each color category. Calculate % survival per color on the green background.
   - Repeat on a brown paper background.
   - Perform at least 3 replicates for each background type.

### Part 2: Computational Biology Exercise — Selection Coefficient Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Compare a hand-calculated allele-frequency change with the selection simulator.

```python
from biology.evolution import Population, simulate_selection

start = Population(name="demo", p=0.3, q=0.7, fitness_AA=1.0, fitness_Aa=0.9, fitness_aa=0.6)
history = simulate_selection(start, generations=10)

print("starting p:", start.p)
print("final p:", round(history[-1].p, 3))
print("generations recorded:", len(history))
```
### Part 3: Finch Beak Analysis {.unnumbered}

5. **Design an Alternative Experiment**: Instead of just analyzing provided data, design an experiment to test how seed availability affects beak morphology in a bird population over multiple generations. What hypothesis would you test? How would you measure beak depth?

6. **Hypothesis**: Predict the relationship between seed hardness and average beak depth. Would you expect a linear relationship, or something else? Why?

## Data Recording {.unnumbered}

: Part 3: Finch Beak Analysis: Color and Starting #. {#tbl:unit_VI_evolution_and_selection_part_3_finch_beak_analysis}
| Color | Starting # | # Surviving (green) | % Survival (green) | # Surviving (brown) | % Survival (brown) |
| ------ | ---------- | ------------------- | ------------------- | ------------------- | ------------------- |
| Green | 30 | | | | |
| Red | 30 | | | | |
| Brown | 30 | | | | |

Selection coefficients:

: Part 3: Finch Beak Analysis: Genotype and Habitat A fitness (w). {#tbl:unit_VI_evolution_and_selection_part_3_finch_beak_analysis_2}
| Genotype | Habitat A fitness (w) | s (A) | Habitat B fitness (w) | s (B) |
| -------- | --------------------- | ----- | --------------------- | ----- |
| AA | | | | |
| Aa | | | | |
| aa | | | | |

Finch graph trend description:

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Simulate selection across generations under alternative fitness assumptions.
- **Data skill to practice:** Interpret fitness data and distinguish selection from other forces.
- **BioSkills emphasis:** Modeling and simulation, Quantitative reasoning, Communication and collaboration.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Evolution — Theory, Natural Selection, and Adaptation** with a reproducibility pass:

: Part 3: Finch Beak Analysis: Evidence check and Student action. {#tbl:unit_VI_evolution_and_selection_part_3_finch_beak_analysis_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this background-survival and finch-beak lab, treat each generation's surviving color or beak counts as a measured fitness differential, and separate selection acting on heritable variation from within-generation plasticity before claiming adaptation. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Allele Frequency Change Under Selection {.unnumbered}

**Problem:** A beneficial dominant allele starts at frequency p_0 = 0.02 in a large population. The recessive genotype has a selection coefficient s = 0.08 against it (relative fitnesses 1, 1, 1 − s for AA, Aa, aa). Using the approximation for a rare dominant beneficial allele, Δp ≈ s × p × (1 − p) × (1 − p) ≈ s × p × (1 − p)^2, estimate the allele frequency after 20 generations of recursive selection.

**Solution:** At each generation, update p_{t+1} = p_t + s × p_t × (1 − p_t)^2 with s = 0.08. Starting at p_0 = 0.02, the per-generation increments are small while p is rare and grow as p increases. Iterating the recursion gives approximately p_1 ≈ 0.02154, p_5 ≈ 0.02893, p_10 ≈ 0.04075, p_15 ≈ 0.05625, and p_20 ≈ 0.07585. The trajectory is concave-up in the rare-allele regime and accelerates as the favored allele becomes more common.

**Interpretation:** Over 20 generations, the allele frequency rises from 0.02 to roughly 0.076 — a near-fourfold increase, but the allele remains far from fixation. Two features of the trajectory are characteristic of selection on a rare dominant: the initial increase is slow because (1 − p)^2 is near 1 and p is small, and the rate of change is governed by the product s × p. As p grows past about 0.5, the (1 − p)^2 factor pulls Δp back down, producing the familiar sigmoid sweep. The approximation neglects drift, which becomes important when N_e × s × p is below about 1 — in small populations this trajectory would show much greater stochastic variation.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Evolution — Theory, Natural Selection, and Adaptation before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. On the green background, which color survived best? Explain in terms of camouflage and predator visual system. How does this simulate directional selection in a real habitat?

2. If the green background was then "burned" and replaced with brown substrate (environmental change), predict how allele frequencies for "green color" would change over generations. Which type of selection would now operate?

3. The finch beak data showed that species with deep beaks eat harder seeds. Explain how this pattern could arise through: (a) individual phenotypic plasticity within one generation; (b) natural selection across many generations. How would you distinguish these mechanisms with an experimental test?

4. Antibiotics are not "mutagens" — they do not create resistant mutants. They primarily *select for* pre-existing resistant mutants. Explain why this distinction matters for how we should use antibiotics clinically, and how the selection coefficient for resistance changes with antibiotic presence vs absence.

5. Compare the evidence supporting the gradual-change model of evolution (phyletic gradualism) vs the punctuated equilibrium model. What does the fossil record actually show, and what is the current consensus about the pace of evolutionary change?

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: If you performed three replicates of the selection simulation, how would you analyze the variation in survival rates? What statistical test would you use to determine if differences between prey colors are significant?

7. **Experimental Error Analysis**: What are three potential sources of error in the predator-prey simulation? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you wanted to test whether a particular trait is under directional, stabilizing, or disruptive selection, how would you design the experiment? What data would you collect? How would you analyze it?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design an Evolutionary Study of Antibiotic Resistance**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How does antibiotic concentration affect the rate of resistance evolution in bacteria?
- Formulate a hypothesis about the relationship between selection pressure and resistance development
- Design a simulation using provided allele-frequency and MIC datasets across different antibiotic concentrations

**Session 2**: Data Collection and Analysis
- Analyze printed time-series data showing resistant and sensitive genotypes over generations
- Estimate resistance levels from provided minimum inhibitory concentration tables
- Compare allele-frequency changes against a no-antibiotic baseline and a high-dose scenario

**Session 3**: Data Interpretation and Presentation
- Compare resistance evolution across different antibiotic concentrations
- Calculate selection coefficients for resistant vs sensitive bacteria
- Evaluate whether each scenario is reproducible by checking sample size, replicate count, and starting allele frequency
- Create a scientific poster or presentation

## Real-World Problem Solving: Evolution and Medicine {.unnumbered}

**Case Study: Evolution of Virulence**

1. **Research Task**: Investigate the trade-off hypothesis for the evolution of virulence. Under what conditions would a pathogen evolve to be more or less virulent?

2. **Ethical Consideration**: Should we use anti-evolution drugs (e.g., "anti-evolution" compounds that reduce mutation rates or horizontal gene transfer) to slow the evolution of resistance? What are the potential benefits and risks?

3. **Policy Proposal**: Design a policy for the responsible use of antibiotics in agriculture. Consider: growth promotion vs disease prevention, alternatives to antibiotics, and monitoring of resistance.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Antibiotic resistance in bacterial pathogens illustrates natural selection acting on either standing genetic variation or new mutations. Evaluate how to distinguish the two modes empirically, then design a treatment protocol that would slow resistance evolution in a pathogen with a generation time near 30 minutes.
>
> (a) Compare the two modes of adaptation. Describe the population-genetic signatures expected for selection on standing variation (a soft sweep, with multiple resistant haplotypes rising together) versus selection on a new mutation (a hard sweep, with a single haplotype rising and reducing local diversity). Identify at least one sequencing or phylogenetic observation that could discriminate the two scenarios in a clinical or environmental sample.
> (b) Estimate the within-host evolutionary potential of a pathogen with a 30-minute generation time. Calculate the number of generations per day (48), and describe how a population size of roughly 10^9 cells provides many opportunities for resistance mutations to arise. Discuss why monotherapy at a sub-therapeutic dose tends to favor stepwise resistance evolution.
> (c) Design a treatment protocol intended to slow resistance evolution. Include at least three components, such as (i) combination therapy targeting multiple pathways to raise the effective number of independent mutations required for resistance, (ii) high-dose short-course dosing aimed at suppressing the pathogen population below the threshold where resistant variants can establish, and (iii) cycling or rotational use of antibiotics to lower the steady selective pressure on any single mechanism. Identify at least one trade-off (such as toxicity, cost, or compliance) for each component, and explain why the protocol would tend to reduce, rather than fully prevent, the emergence of resistance.

## Safety and Ethics Notes {.unnumbered}

Forceps (plastic or blunt-tip) are low risk. Ensure fairness in simulation — most students forage simultaneously. Small colored squares: keep away from young children (swallowing hazard). Antibiotic-resistance work in this lab is paper-based primarily; do not culture bacteria or handle antibiotics. When discussing antibiotic resistance, emphasize following current prescriber instructions, avoiding unnecessary antibiotic starts, using diagnostics when available, and protecting access to effective treatment.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarizing the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_VI_evolution_and_selection} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VI_evolution_and_selection} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/evolution/evolution.py` for evolutionary calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
