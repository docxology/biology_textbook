# Lab 16 — Mendelian Genetics and Heredity {.unnumbered}

\label{sec:lab_unit_V_mendelian_genetics}

*This activity accompanies \cref{sec:unit_V_mendelian_genetics} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate genetic cross simulations to determine inheritance patterns
- Formulate testable hypotheses about dominance, recessiveness, and linkage
- Identify independent, dependent, and controlled variables in genetic experiments
- Analyze experimental data using chi-square tests and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Mendelian Genetics and Heredity.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. State Mendel's law of segregation in your own words, then connect the law to the cellular events of meiosis. At which stage do the two alleles of a heterozygous parent physically separate into different gametes, and why does this generate the 1:1 gamete ratio that underlies a 3:1 monohybrid offspring ratio?
2. Distinguish incomplete dominance from codominance, and give a concrete biological example of each. In your explanation, describe how the molecular product of each allele combines in the heterozygote to produce the observed phenotype, and identify a test cross or phenotypic assay that could differentiate the two patterns.
3. Define the chi-squared test in the context of testing a Mendelian ratio. Identify the null hypothesis, the role of the degrees of freedom, and the meaning of a p-value below 0.05 for a hypothesized 9:3:3:1 dihybrid ratio.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of Mendelian inheritance, predict the outcome of a test cross between a dominant phenotype individual (unknown genotype) and a homozygous recessive individual. What phenotypic ratio would you expect if the dominant individual is homozygous vs heterozygous?

2. **Experimental Design**: What is the independent variable in a Mendelian inheritance experiment? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: The chi-square test is used to determine if observed ratios fit expected Mendelian ratios. Why is this test important in genetics? What does a significant deviation from expected ratios tell you?

4. **Quantitative Reasoning**: If you perform a monohybrid cross (Aa × Aa) and observe 450 round seeds and 130 wrinkled seeds (total 580), what is the χ² value? With 1 degree of freedom, is this significantly different from the expected 3:1 ratio at p = 0.05?

5. **Real-World Application**: Many human genetic disorders are recessive. Why are recessive disorders more common than dominant disorders? What are the implications for genetic counseling?

## Background {.unnumbered}

Gregor Mendel's experiments with pea plants (1856–1863) established the laws of segregation (allele pairs separate during gamete formation) and independent assortment (non-linked genes assort independently). Monohybrid crosses between heterozygotes (Aa × Aa) produce 3:1 phenotype ratios; dihybrid crosses produce 9:3:3:1 ratios. Deviations from these ratios suggest linkage, incomplete dominance, codominance, or epistasis.

### Example Pedigree — Autosomal Recessive Trait (Cystic Fibrosis) {.unnumbered}

Below is the three-generation pedigree you will analyse in Part B. Filled squares/circles are affected individuals; half-filled are obligate carriers; empty are unaffected. Use this as a reference for how pedigree symbols encode genotypes.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Punnett square worksheets (3: monohybrid, dihybrid, incomplete dominance) | 1 set |
| Pedigree chart (printed: 3-generation autosomal recessive trait) | 1 |
| Coin or random number table (to simulate gamete formation) | 2 |
| Chi-square table (critical values) | 1 |
| Calculator | 1 |
| Coloured counters (2 colours × 20) for simulating gametes | 1 set |
| Calculator or optional Python REPL with this project installed | 1 |
| Statistical analysis worksheet | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Punnett Square Analysis {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how the inheritance pattern of a specific trait (e.g., pea seed shape) follows Mendelian ratios.

2. **Identify Variables**:
   - Independent variable: Parental genotypes
   - Dependent variable: Offspring genotype/phenotype ratios
   - Controlled variables: Cross design, counting method, environmental conditions, etc.

3. **Set Up Controls**: Why is it important to use true-breeding parental lines? What other controls could you include in a Mendelian inheritance experiment?

4. **Data Collection**:
   - Complete monohybrid crosses: Aa × Aa; AA × Aa; Aa × aa. Record genotype and phenotype ratios.
   - Complete a dihybrid cross: AaBb × AaBb. Record the 9:3:3:1 phenotype ratio.
   - Complete an incomplete dominance cross: R₁R₁ (red) × R₂R₂ (white). What is the F₁ phenotype? F₂ ratios?

### Part 2: Computational Biology Exercise - Statistical Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Validate the paper Punnett-square and chi-square calculations.

```python
from biology.genetics import chi_squared_test, punnett_square

cross = punnett_square("Aa", "Aa")
observed = [450.0, 130.0]
expected = [0.75 * sum(observed), 0.25 * sum(observed)]
chi = chi_squared_test(observed, expected)

print("genotype ratios:", cross.genotype_ratios)
print("phenotype ratios:", cross.phenotype_ratios)
print("χ²:", round(chi.chi_squared, 2), "reject?", chi.reject_null)
```
### Part 3: Pedigree Analysis {.unnumbered}

5. **Design an Alternative Investigation**: Instead of just analyzing the provided pedigree, design a paper-based study to determine the inheritance pattern of a human genetic trait in a small population. What hypothesis would you test? What consent, privacy, and pedigree metadata would be required?

6. **Hypothesis**: Predict the inheritance pattern (autosomal dominant, autosomal recessive, X-linked) for a trait that appears in every generation, affects both males and females equally, and shows no father-to-son transmission.

## Data Recording {.unnumbered}

| Cross | Offspring genotype ratio | Offspring phenotype ratio |
| ----- | ------------------------ | ------------------------- |
| Aa × Aa | | |
| AaBb × AaBb | | |
| R₁R₂ × R₁R₂ (incomplete dom.) | | |

Pedigree genotypes:

| | Gen I | Gen II | Gen III |
|---|---|---|---|
| Individual | | | |

Chi-square result: χ² = ___; df = ___; p < 0.05? (Y/N); Conclusion:

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Solve inheritance patterns and test expected ratios.
- **Data skill to practice:** Use family or cross data to infer genotype probabilities.
- **BioSkills emphasis:** Quantitative reasoning, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Mendelian Genetics and Heredity** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Equity and consent | Mark any genetic information that could reveal risk to relatives, change insurance or employment concerns, or require counseling before disclosure. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab the cross results and offspring counts are the evidence — use a chi-square goodness-of-fit test against the expected ratio before deciding whether a deviation signals linkage, penetrance, or sampling noise. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Chi-Squared Test on a Dihybrid Cross {.unnumbered}

**Problem:** A dihybrid cross AaBb × AaBb produces 160 offspring. The hypothesized Mendelian ratio is 9:3:3:1 for the phenotypic classes A_B_, A_bb, aaB_, and aabb. Calculate the expected count for each class, then perform a chi-squared test using the observed counts 92 A_B_, 28 A_bb, 29 aaB_, and 11 aabb. With three degrees of freedom and a critical value of 7.815 at alpha = 0.05, is the result consistent with independent assortment?

**Solution:** Compute expected counts by multiplying the total 160 by each ratio fraction: 9/16 × 160 = 90 for A_B_, 3/16 × 160 = 30 for A_bb, 3/16 × 160 = 30 for aaB_, and 1/16 × 160 = 10 for aabb. The chi-squared statistic uses the formula chi-squared = sum of (observed − expected)^2 / expected across the four phenotypic classes. The four class contributions are (92 − 90)^2 / 90 = 4/90 ≈ 0.0444, (28 − 30)^2 / 30 = 4/30 ≈ 0.1333, (29 − 30)^2 / 30 = 1/30 ≈ 0.0333, and (11 − 10)^2 / 10 = 1/10 = 0.1000. The total is approximately 0.0444 + 0.1333 + 0.0333 + 0.1000 ≈ 0.311. Degrees of freedom = number of classes minus one = 4 − 1 = 3. The critical chi-squared at alpha = 0.05 with df = 3 is 7.815.

**Interpretation:** Because 0.311 is much smaller than 7.815, the null hypothesis of a 9:3:3:1 ratio is not rejected at alpha = 0.05; the data are consistent with independent assortment of the two loci. A small chi-squared value reflects a close agreement between observed and expected counts and does not prove independent assortment — it indicates the data provide no statistical evidence against it. Sources of deviation in real crosses include linkage, differential viability, and sampling variation, any of which can inflate chi-squared in larger experiments.

## Analysis Questions {.unnumbered}

1. In the AaBb × AaBb dihybrid cross, what fraction of offspring are aabb (homozygous recessive for both traits)? Show your Punnett square logic.

2. The pedigree shows two unaffected parents who produce an affected child. What does this tell you about dominance? Can you determine whether the trait is autosomal or X-linked from this generation alone? What additional information would resolve this?

3. Your chi-square test: did the observed ratio significantly deviate from 3:1? What biological reasons could cause deviation from the expected ratio (give at least two sources of biological deviation other than statistical sampling error)?

4. Blood types in humans follow codominance (A and B antigens) and simple recessive inheritance (O). A type AB mother and type O father have two children — one type A, one type B. What genotype does each family member have? Is this consistent with Mendelian inheritance?

5. A gene controls tail length in cats: T (tailless, Manx) is dominant but homozygous TT is lethal. Set up the cross Tt × Tt. What are the observed genotype and phenotype ratios among the LIVING offspring? How does this illustrate the concept of a lethal allele modifying a Mendelian ratio?

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: If you performed three replicates of a genetic cross, how would you analyze the variation in offspring ratios? What statistical test would you use to determine if differences between crosses are significant?

7. **Experimental Error Analysis**: What are three potential sources of error in Mendelian inheritance experiments? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you wanted to test whether two genes are linked or assort independently, how would you design the experiment? What data would you collect? How would you analyze it?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Population Genetics Study of a Human Trait**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- Choose a human Mendelian trait (e.g., attached earlobes, tongue rolling, hitchhiker's thumb)
- Formulate a hypothesis about its inheritance pattern in your population
- Design a survey to collect pedigree data from families

**Session 2**: Data Collection and Analysis
- Collect pedigree data from volunteers (with consent)
- Analyze inheritance patterns using Punnett squares and chi-square tests
- Compare your results to expected Mendelian ratios

**Session 3**: Data Interpretation and Presentation
- Create a report with your findings
- Discuss any deviations from expected ratios and possible explanations
- Create a scientific poster or presentation

## Real-World Problem Solving: Genetic Counseling {.unnumbered}

**Case Study: Carrier Screening for Cystic Fibrosis**

1. **Research Task**: Investigate the prevalence of cystic fibrosis carrier status in different populations. Why is the carrier rate higher in people of Northern European descent?

2. **Ethical Consideration**: Should carrier screening for recessive disorders be routinely offered to prospective parents in high-prevalence or high-risk contexts? What are the potential benefits, risks, consent requirements, and equity concerns?

3. **Policy Proposal**: Design a policy for responsible use of genetic screening in reproductive healthcare. Consider: access, counseling, privacy, data retention, secondary use, family implications, and follow-up options.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Genetic ratios observed in large laboratory populations tend to conform closely to Mendelian predictions, even when individual small crosses appear to deviate. Evaluate why this convergence occurs and explain how chi-squared testing bridges the gap between a finite sample and the underlying population-level theory.
>
> (a) Use the law of large numbers to explain why the observed phenotypic ratio in a dihybrid cross approaches 9:3:3:1 as the offspring count grows. Describe how sampling variance scales with sample size and predict, qualitatively, how a cross of 40 offspring and a cross of 4,000 offspring would differ in the typical absolute deviation from the expected ratio.
> (b) Explain the role of the chi-squared test as a formal decision rule for connecting a finite sample to a population-level Mendelian hypothesis. Identify what the null and alternative hypotheses represent biologically, and discuss why failing to reject the null is not equivalent to proving the Mendelian model — it indicates that the data do not provide sufficient evidence against it at the chosen alpha.
> (c) Consider a case where a large dataset produces a statistically significant deviation (p < 0.01) from the expected 9:3:3:1 ratio. Propose at least two biological explanations (such as linkage, epistasis, or differential viability) and outline an experimental follow-up that would distinguish between them.

## Safety and Ethics Notes {.unnumbered}

This lab involves primarily paper-based activities and discussions. When discussing patient genetic data, maintain confidentiality and respect for individual privacy. Treat pedigrees and PRS examples as potentially identifiable family information: do not infer ancestry, parentage, or disease status beyond the evidence given, and separate biological risk estimates from policy decisions about disclosure, insurance, employment, or family notification.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_V_mendelian_genetics} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_V_mendelian_genetics} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/genetics/genetics.py` for Mendelian genetics calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
