# Lab — Genetic Drift, Gene Flow, and Speciation {.unnumbered}

\label{sec:lab_unit_VI_genetic_drift_and_speciation}

*This activity accompanies \cref{sec:unit_VI_genetic_drift_and_speciation} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate a founder effect simulation to measure genetic drift
- Formulate testable hypotheses about how population size affects genetic diversity
- Identify independent, dependent, and controlled variables in population genetics experiments
- Analyze experimental data using allele frequency calculations and Fst statistics
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Genetic Drift, Gene Flow, and Speciation.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Explain why random genetic drift has a larger per-generation effect in small populations than in large ones. Reference the variance of allele frequency change Var(Δp) = p × (1 − p) / (2 N_e) and describe how this sampling-variance scaling relates to the random outcome of allele transmission across generations.
2. State the biological species concept (BSC) in your own words, and identify one well-known limitation. Give a concrete example (such as asexual lineages, ring species, or extinct taxa) where the BSC is difficult to apply, and briefly describe an alternative species concept that handles the case more gracefully.
3. Distinguish pre-zygotic from post-zygotic reproductive isolation, and give two examples of each. For each example, describe whether the isolating mechanism would tend to be reinforced or weakened by ongoing gene flow between diverging populations.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of genetic drift, predict how the allele frequency in a small founding population (e.g., 6 individuals) would compare to the source population (100 individuals). Write a clear, testable hypothesis.

2. **Experimental Design**: What is the independent variable in a genetic drift simulation? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: The Fixation Index (Fst) quantifies genetic differentiation between populations. Why is this measure important in evolutionary biology? How does it relate to gene flow and speciation?

4. **Quantitative Reasoning**: If two populations have allele frequencies of 0.8 and 0.2 for the same gene, what would their Fst be? Show your calculation.

5. **Real-World Application**: The founder effect is thought to have played a role in the high prevalence of certain genetic disorders in isolated populations (e.g., Tay-Sachs in Ashkenazi Jews). How does the founder effect explain this pattern? What are the implications for genetic counseling?

## Lab Context: Genetic Drift, Gene Flow, and Speciation {.unnumbered}

Even without natural selection, populations evolve through random genetic drift, gene flow, and mutation. The **founder effect** (a special case of bottleneck) occurs when a small number of individuals colonise a new area, carrying primarily a subset of the original gene pool's variation. **Speciation** — the formation of new species — occurs when reproductive isolation evolves between populations, typically after geographic (allopatric) or ecological (sympatric) separation. The Fixation Index **Fst = (H_T − H_S) / H_T** quantifies genetic differentiation between populations (0 = no differentiation; 1 = complete differentiation).

The effective-population-size worked example in the parent chapter (\cref{sec:unit_VI_genetic_drift_and_speciation}) shows how sex-ratio skew reduces genetic drift from $N_e = N$ toward $N_e = 4 N_m N_f / (N_m + N_f)$: a 10:90 male-to-female ratio with $N = 100$ gives $N_e = 36$. This lab simulates drift empirically using dice rolls across replicate populations and then compares the observed variance in allele frequency to the theoretical expectation under different $N_e$ values.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Source-governance card for Genetic Drift, Gene Flow, and Speciation: evolutionary-evidence source card: alternative hypotheses, sampling, calibration, and confidence boundary | 1 |
| 100 beads (50 red, 50 blue — representing two alleles) in a bag | 1 |
| Second bag for "new island" | 1 |
| Speciation case study cards (allopatric: Hawaiian honeycreepers; sympatric: cichlid fish in Lake Victoria) | 1 set |
| Galapagos mockingbird morphological data (printed: beak length, body mass per island) | 1 |
| Calculator | 1 |
| Graph paper | 1 |
| Calculator or optional Python REPL with this project installed | 1 |
| Population genetics worksheet | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Founder Effect Simulation {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how the size of a founding population affects the rate of genetic drift.

2. **Identify Variables**:
   - Independent variable: Founder population size (6 vs 20 individuals)
   - Dependent variable: Change in allele frequency from source population
   - Controlled variables: Source population allele frequency, number of generations, etc.

3. **Set Up Controls**: Why is it important to start with a known source population allele frequency? What other controls could you include in a genetic drift simulation?

4. **Data Collection**:
   - Start: 100 beads at p = 0.5. Draw 6 beads randomly (founder population) — do not replace.
   - Record allele frequencies in the founder group; use these to repopulate to 100 (multiply founder frequencies × 100).
   - Repeat sampling: draw 20 from the new population to simulate a moderate founding event.
   - Compare p values: original, 6-founder, 20-founder.
   - Perform at least 3 replicates for each founder size.

### Part 2: Computational Biology Exercise — Population Genetics Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Run deterministic drift simulations by fixing the random seed.

```python
from biology.evolution import isolation_index, simulate_drift

small = simulate_drift(p=0.5, N=20, generations=10, rng_seed=7)
large = simulate_drift(p=0.5, N=500, generations=10, rng_seed=7)

print("small-population final p:", round(small[-1], 3))
print("large-population final p:", round(large[-1], 3))
print("isolation example:", round(isolation_index(gene_flow_rate=0.01, mutation_rate=0.001), 3))
```
### Part 3: Morphological Divergence Analysis {.unnumbered}

5. **Design an Alternative Investigation**: Instead of just analyzing provided morphological data, design a paper-based comparison to test how geographic isolation affects trait divergence in a natural population. What hypothesis would you test? Which archived measurements, sample sizes, and map distances would you need?

6. **Hypothesis**: Predict the relationship between geographic distance and morphological divergence. Would you expect a linear relationship, or something else? Why?

## Data Recording {.unnumbered}

| Founding event | Sample size | p (red allele) | q (blue allele) |
| -------------- | ----------- | -------------- | --------------- |
| Original | 100 | 0.5 | 0.5 |
| 6-founder | 6 | | |
| 20-founder | 20 | | |

Mockingbird data summary (fill from provided table):

| Island | Mean beak length (mm) | Mean body mass (g) | Distinct from others? |
| ------ | --------------------- | ------------------- | ---------------------- |
| Santa Cruz | | | |
| Genovesa | | | |
| Española | | | |
| Fernandina | | | |

Fst calculation: H_T = ___; H_S = ___; Fst = ___; Interpretation:

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model drift and speciation scenarios with repeated trials.
- **Data skill to practice:** Distinguish stochastic from directional change in allele-frequency data.
- **BioSkills emphasis:** Modeling and simulation, Quantitative reasoning, Communication and collaboration.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Genetic Drift, Gene Flow, and Speciation** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this founder-event and $F_{ST}$ lab, distinguish allele-frequency change caused by sampling in small colonising groups (drift) from differentiation maintained by restricted gene flow, and state which reproductive-isolation barrier each cichlid or mockingbird comparison would require before calling the populations distinct species. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Effective Population Size with Unequal Sex Ratio {.unnumbered}

**Problem:** A population contains 100 individuals (50 male, 50 female), but breeding success is highly skewed — 10 males father about 90 percent of the offspring while the other 40 males contribute negligibly. Treating the breeding males as N_m = 10 and the breeding females as N_f = 50, calculate the effective population size using N_e = 4 × N_m × N_f / (N_m + N_f), and compare it with a random-mating population of 100.

**Solution:** Substitute N_m = 10 and N_f = 50 into the formula. The numerator is 4 × 10 × 50 = 2000. The denominator is N_m + N_f = 10 + 50 = 60. Dividing, N_e ≈ 2000 / 60 ≈ 33.3 — roughly one-third of the census size. For a random-mating population of the same census size 100 with equal breeding success, N_e would be much closer to 100, although seldom exactly equal because of generational and reproductive variance.

**Interpretation:** Reducing the breeding sex ratio from 50:50 to 10:50 cuts the effective population size from near 100 to about 33. The per-generation loss of heterozygosity is governed by 1 / (2 N_e), so this skew triples the rate of drift compared with the random-mating case. Two consequences follow: rare alleles are lost more readily, and the inbreeding coefficient F accumulates faster. In a conservation context, this is why a census count alone can give an overly optimistic view of a population's genetic health — the relevant quantity for diversity loss is N_e, not N.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Genetic Drift, Gene Flow, and Speciation before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. How did the allele frequencies in the 6-founder event compare to the original population? What does this demonstrate about why small colonising populations often show low genetic diversity compared to mainland populations?

2. The mockingbird populations on different Galapagos islands show morphological divergence. What mechanism prevented gene flow between islands, and what type of speciation does this represent? What reproductive isolation mechanisms would need to evolve for them to become separate species?

3. Fst = 0 indicates populations are identical (freely exchanging genes). Fst = 1 indicates complete isolation. How would you interpret Fst = 0.15 — is there gene flow? Use your calculated Fst to describe the degree of isolation between cichlid populations A, B, and C.

4. Lake Victoria cichlids underwent adaptive radiation in ~15,000 years, producing >500 species. What does this rapid speciation suggest about the speed at which reproductive isolation can evolve? What kind of speciation (allopatric, parapatric, or sympatric) is most consistent with this pattern?

5. Ring species (like Larus gulls circling the Arctic) demonstrate speciation in action: adjacent populations can interbreed, but the two ends of the ring cannot. Explain what this demonstrates about the continuity of the speciation process and why ring species challenge a strict definition of "species."

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: If you performed three replicates of the founder effect simulation, how would you analyze the variation in allele frequency change? What statistical test would you use to determine if differences between founder sizes are significant?

7. **Experimental Error Analysis**: What are three potential sources of error in the bead simulation? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you wanted to test whether two populations are diverging due to genetic drift or natural selection, how would you design the experiment? What data would you collect? How would you analyze it?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Study of Human Population Differentiation**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How does geographic distance affect genetic differentiation in human populations?
- Formulate a hypothesis about the relationship between distance and Fst
- Design a study using publicly available genetic data (e.g., 1000 Genomes Project)

**Session 2**: Data Collection and Analysis
- Download genetic data for multiple populations
- Calculate Fst between population pairs
- Plot Fst against geographic distance

**Session 3**: Data Interpretation and Presentation
- Analyze the correlation between distance and genetic differentiation
- Discuss the implications for understanding human migration history
- Create a scientific poster or presentation

## Real-World Problem Solving: Conservation Genetics {.unnumbered}

**Case Study: Genetic Rescue of Endangered Populations**

1. **Research Task**: Investigate the Florida panther bottleneck. How did genetic drift and inbreeding depression affect the population? What was the outcome of the genetic rescue program?

2. **Ethical Consideration**: Should we introduce individuals from other populations to increase genetic diversity in endangered species? What are the potential benefits and risks (e.g., outbreeding depression)?

3. **Policy Proposal**: Design a policy for managing genetic diversity in small, isolated populations. Consider: when to intervene, how to select individuals for translocation, and how to monitor success.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A peripheral isolate of 40 individuals has split off from a large continental source population and become geographically isolated. Evaluate whether this isolate is more likely to undergo speciation predominantly via genetic drift or via natural selection, and predict the genomic signatures that would distinguish the two modes in a follow-up sequencing study.
>
> (a) Compare the expected per-generation magnitudes of drift and selection in the isolate. Estimate the drift scale as 1 / (2 N_e) ≈ 1/80 ≈ 0.0125 per generation, and discuss when this exceeds the selection coefficient s on a candidate adaptive locus. Describe the conditions (low s, low N_e, novel environment) under which drift would tend to dominate the divergence, and the conditions (moderate s, distinct selective regime) under which selection would.
> (b) Predict the genomic signatures for each mode. Drift-dominated divergence tends to produce a broadly uniform increase in differentiation across the genome (elevated genome-wide F_ST), an excess of rare and lineage-private alleles, and few sharp peaks of divergence. Selection-driven divergence tends to produce localized peaks of high F_ST around loci tied to the new environment, reduced diversity in those windows, and extended haplotype homozygosity consistent with recent sweeps. Note that gene flow can blur both signatures.
> (c) Outline a sequencing study that would discriminate the two modes. Recommend whole-genome resequencing of about 20 individuals from each population, computation of windowed F_ST and nucleotide diversity, and a genome-wide scan for selective sweeps. Predict the expected outcome under each hypothesis and identify at least one confound (such as recent admixture, low-recombination regions, or background selection) that could mimic a drift or selection signature and complicate the interpretation.

## Safety and Ethics Notes {.unnumbered}

Bead simulation: ensure beads are not ingested. Discussions of speciation based on genetic data should be careful not to conflate genetic population differences with outdated racial taxonomic thinking. Consider the ethical implications of conservation genetics.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_VI_genetic_drift_and_speciation} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VI_genetic_drift_and_speciation} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/evolution/evolution.py` for population genetics calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
