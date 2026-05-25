# Lab — Mendelian Extensions and Human Genetics {#sec:lab_unit_V_mendelian_extensions_and_human_genetics .unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Mendelian Extensions and Human Genetics.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->

*This activity accompanies \cref{sec:unit_V_mendelian_extensions_and_human_genetics} of the textbook — review that chapter before attempting the exercises below.*

## Lab Context: Mendelian Extensions and Human Genetics {.unnumbered}

This extension lab emphasizes pedigree analysis, extensions to Mendelian ratios, and human genetics applications using paper-based inheritance scenarios.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Mendelian Extensions and Human Genetics: inheritance source card: model assumptions, sampling frame, ancestry/context boundary, and uncertainty | 1 |
| Printed datasets, cards, and worksheets referenced below | 1 set per group |
| Graph paper or plain paper for diagrams | 1 |
| Calculator | 1 |

## Paper-Based Investigation {.unnumbered}

5. **Design an Alternative Investigation**: Instead of just analyzing the provided pedigree, design a paper-based study to determine the inheritance pattern of a human genetic trait in a small population. What hypothesis would you test? What consent, privacy, and pedigree metadata would be required?

6. **Hypothesis**: Predict the inheritance pattern (autosomal dominant, autosomal recessive, X-linked) for a trait that appears in every generation, affects both males and females equally, and shows no father-to-son transmission.

## Data Recording {.unnumbered}

: Alignment and Rubric Map: Cross and Offspring genotype ratio. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map_2}
| Cross | Offspring genotype ratio | Offspring phenotype ratio |
| ----- | ------------------------ | ------------------------- |
| Aa × Aa | | |
| AaBb × AaBb | | |
| R₁R₂ × R₁R₂ (incomplete dom.) | | |

Pedigree genotypes:

: Alignment and Rubric Map. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map_3}
| | Gen I | Gen II | Gen III |
|---|---|---|---|
| Individual | | | |

Chi-square result: χ² = ___; df = ___; p < 0.05? (Y/N); Conclusion:

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Solve pedigree and extension problems with explicit assumptions.
- **Data skill to practice:** Infer inheritance mode and extension mechanism from family or cross data.
- **BioSkills emphasis:** Quantitative reasoning, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Mendelian Genetics and Heredity** with a reproducibility pass:

: Alignment and Rubric Map: Evidence check and Student action. {#tbl:unit_V_mendelian_extensions_and_human_genetics_alignment_and_rubric_map_4}
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

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Mendelian Extensions and Human Genetics before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarizing the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_V_mendelian_extensions_and_human_genetics} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_V_mendelian_extensions_and_human_genetics} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/genetics/genetics.py` for Mendelian genetics calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
