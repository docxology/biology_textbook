# Lab — Mendelian Principles and Probability {.unnumbered}

\label{sec:lab_unit_V_mendelian_principles}

*This activity accompanies \cref{sec:unit_V_mendelian_principles} of the textbook — review that chapter before attempting the exercises below.*

*This activity accompanies \cref{sec:unit_V_mendelian_principles} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate genetic cross simulations to determine inheritance patterns
- Formulate testable hypotheses about dominance, recessiveness, and linkage
- Identify independent, dependent, and controlled variables in genetic experiments
- Analyze experimental data using chi-square tests and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Mendelian Principles and Probability.
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

## Lab Context: Mendelian Principles and Probability {.unnumbered}

Gregor Mendel's experiments with pea plants (1856–1863) established the laws of segregation (allele pairs separate during gamete formation) and independent assortment (non-linked genes assort independently). Monohybrid crosses between heterozygotes (Aa × Aa) produce 3:1 phenotype ratios; dihybrid crosses produce 9:3:3:1 ratios. Deviations from these ratios suggest linkage, incomplete dominance, codominance, or epistasis.

### Example Pedigree — Autosomal Recessive Trait (Cystic Fibrosis) {.unnumbered}

Below is the three-generation pedigree you will analyse in Part B. Filled squares/circles are affected individuals; half-filled are obligate carriers; empty are unaffected. Use this as a reference for how pedigree symbols encode genotypes.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Source-governance card for Mendelian Principles and Probability: inheritance source card: model assumptions, sampling frame, ancestry/context boundary, and uncertainty | 1 |
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

### Part 2: Computational Biology Exercise — Statistical Analysis with Python {.unnumbered}

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

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Mendelian Principles and Probability before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Solve monohybrid and dihybrid crosses and test expected ratios.
- **Data skill to practice:** Use cross data to infer genotype probabilities.
- **BioSkills emphasis:** Quantitative reasoning, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade

Before answering the analysis questions, annotate the paper dataset for
**Mendelian Principles and Probability** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: Mendelian patterns are starting models that must be qualified by penetrance, linkage, environment, and sampling. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.
