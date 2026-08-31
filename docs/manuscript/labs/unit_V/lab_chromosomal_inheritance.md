# Lab — Chromosomal Inheritance and Linkage {#sec:lab_unit_V_chromosomal_inheritance .unnumbered}


*This activity accompanies \cref{sec:unit_V_chromosomal_inheritance} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate genetic linkage mapping datasets to determine gene order
- Formulate testable hypotheses about chromosomal abnormalities from karyotype data
- Identify independent, dependent, and controlled variables in cytogenetic studies
- Analyze experimental data using recombination frequencies and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Chromosomal Inheritance and Linkage.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define non-disjunction in your own words, and state the meiotic stage at which it can occur (meiosis I, meiosis II, or both). For each case, describe whether the resulting gametes are missing a chromosome, carry an extra chromosome, or both.
2. Explain why females heterozygous for an X-linked recessive allele are typically described as somatic mosaics for that trait. Reference X-inactivation (the Lyon hypothesis) and the timing of the inactivation choice during embryonic development.
3. A karyotype shows 47 chromosomes with the configuration 47,XXY. Predict the likely phenotypic syndrome, state whether the extra chromosome originated from a maternal or paternal non-disjunction event with higher prior probability, and identify the meiotic stage most often implicated.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of genetic linkage, predict how the recombination frequency between two genes would change if they were located very close together on the same chromosome versus far apart.

2. **Experimental Design**: What is the independent variable in a linkage mapping experiment? What is the dependent variable? List at least 5 variables that should be controlled to ensure accurate mapping.

3. **Scientific Context**: The chi-square test can be used to determine if observed recombination frequencies differ significantly from expected. Why is this test important in linkage analysis? What does a significant deviation tell you?

4. **Quantitative Reasoning**: If genes A and B have a recombination frequency of 12 cM, and genes B and C have 8 cM, what is the expected recombination frequency between A and C if there is no interference? How does interference affect this?

5. **Real-World Application**: Chromosomal abnormalities like Down syndrome are often caused by nondisjunction. Why does maternal age increase the risk of nondisjunction? What cellular mechanisms normally prevent this?

## Lab Context: Chromosomal Inheritance and Linkage {.unnumbered}

Genes on the same chromosome are linked and tend to be inherited together (violating independent assortment). The **recombination frequency** between linked genes — measured as the percentage of recombinant offspring among total — is proportional to map distance (1% recombination = 1 centimorgan, cM). X-linked traits are carried on the X chromosome; since males are hemizygous (XY), a single recessive allele is expressed. Nondisjunction during meiosis (failure of chromosomes to separate) produces aneuploid gametes, leading to conditions such as trisomy 21 (Down syndrome).

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_V_chromosomal_inheritance_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Chromosomal Inheritance and Linkage: inheritance source card: model assumptions, sampling frame, ancestry/context boundary, and uncertainty | 1 |
| Linkage mapping dataset (3 genes, pairwise recombination frequencies) (printed) | 1 |
| Karyotype images (4 cases: normal, trisomy 21, Turner syndrome 45,X, translocation) (printed) | 1 set |
| Scissors and paste (for karyotype sorting exercise) | 1 set |
| X-linked pedigrees (2 cases: color blindness, haemophilia) (printed) | 1 |
| Ruler | 1 |
| Chromosome pair cards (22 homologous pairs, numbered) | 1 set |
| Calculator or optional Python REPL with this project installed | 1 |
| Statistical analysis worksheet | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Genetic Linkage Mapping {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about the order of three genes given their pairwise recombination frequencies.

2. **Identify Variables**:
   - Independent variable: Gene order (which gene is in the middle)
   - Dependent variable: Recombination frequencies between gene pairs
   - Controlled variables: Population size, crossover detection method, etc.

3. **Set Up Controls**: Why is it important to have a large sample size in linkage mapping? What other controls could you include to ensure accurate recombination frequency measurements?

4. **Data Collection**:
   - Given pairwise recombination frequencies: genes A–B = 12 cM, B–C = 8 cM, A–C = 20 cM.
   - Draw the linear linkage map. Which gene is in the middle? Indicate the distances between each adjacent pair.
   - Calculate the expected coefficient of coincidence (observed double crossovers / expected double crossovers) and interference (1 - coefficient of coincidence).

### Part 2: Computational Biology Exercise — Linkage Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Infer a simple three-point map from pairwise recombination distances.

```python
from biology.genetics import genetic_distance, infer_three_point_order

distances = {("A", "B"): 12.0, ("B", "C"): 8.0, ("A", "C"): 20.0}
order = infer_three_point_order(distances)

print("gene order:", " - ".join(order.order))
print("adjacent distances:", order.adjacent_distances_cM)
print("24 recombinants among 200 progeny:", genetic_distance(24, 200), "cM")
```
### Part 3: Karyotype Analysis {.unnumbered}

5. **Design an Alternative Investigation**: Instead of just analyzing provided karyotype images, design a paper-based case-control study using archived karyotype datasets to investigate the effect of a spindle-disrupting condition on chromosome segregation. What hypothesis would you test? How would you analyze the resulting karyotype calls?

6. **Hypothesis**: Predict how exposure to a microtubule-disrupting agent (like colchicine) would affect chromosome number and structure in dividing cells.

## Data Recording {.unnumbered}

Linkage map sketch:

`A —[___cM]— B —[___cM]— C`

: Part 3: Karyotype Analysis: Karyotype Case and # chromosomes. {#tbl:unit_V_chromosomal_inheritance_part_3_karyotype_analysis}
| Karyotype Case | # chromosomes | Abnormality | Syndrome (if any) |
| -------------- | ------------- | ----------- | ----------------- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

X-linked pedigree genotypes:

: Part 3: Karyotype Analysis: Individual and Phenotype. {#tbl:unit_V_chromosomal_inheritance_part_3_karyotype_analysis_2}
| Individual | Phenotype | Genotype |
| ---------- | --------- | -------- |
| Gen I male | Unaffected | X^B Y |
| Gen I female | | |
| Gen II affected male | | |
| Gen III carrier female | | |

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Map linked genes and reason from chromosomal anomalies.
- **Data skill to practice:** Infer gene order or chromosomal mechanism from offspring counts.
- **BioSkills emphasis:** Quantitative reasoning, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Chromosomal Inheritance and Linkage** with a reproducibility pass:

: Part 3: Karyotype Analysis: Evidence check and Student action. {#tbl:unit_V_chromosomal_inheritance_part_3_karyotype_analysis_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab the paper karyotypes, three-point cross data, and pedigrees are the evidence — score recombination frequencies, gene order, and nondisjunction division from the dataset itself rather than from the expected ratio. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: X-linked Hemophilia A Carrier Cross {.unnumbered}

**Problem:** A woman is a carrier for hemophilia A with genotype X^H X^h. Her partner has hemophilia A with genotype X^h Y. Construct a Punnett square and calculate the probability that (a) a son has hemophilia, (b) a daughter is a carrier, and (c) a daughter has hemophilia. Express each result as a fraction and a percentage.

**Solution:** The mother produces two gamete types, X^H and X^h, with equal probability. The father produces X^h and Y gametes with equal probability. The 2 × 2 Punnett square yields four offspring genotypes, each at 1/4 expected frequency: X^H X^h (carrier daughter), X^H Y (unaffected son), X^h X^h (affected daughter), and X^h Y (affected son). Conditioning on sex, sons inherit Y from the father and either X^H or X^h from the mother, giving 1/2 unaffected and 1/2 affected sons; daughters inherit X^h from the father and either X^H or X^h from the mother, giving 1/2 carrier and 1/2 affected daughters.

(a) P(son has hemophilia) = 1/2 of sons = 50%. Among offspring, 1/4 are affected sons = 25%.
(b) P(daughter is a carrier, X^H X^h) = 1/2 of daughters = 50%. Among offspring, 1/4 = 25%.
(c) P(daughter has hemophilia, X^h X^h) = 1/2 of daughters = 50%. Among offspring, 1/4 = 25%.

**Interpretation:** Because the father is hemizygous and affected, half of his daughters inherit the recessive allele on his X and the other half inherit it from the carrier mother as well — an unusually high rate of affected daughters compared with a more typical carrier mother × unaffected father cross, where affected daughters are rare. The expected ratios assume Mendelian segregation and equal viability, which can be perturbed by selection or sampling variation in small families.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Chromosomal Inheritance and Linkage before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. In linkage mapping, why does the A–C recombination frequency (20 cM) not simply equal A–B + B–C (12 + 8 = 20 cM) in real experiments? Explain the concept of double crossovers and interference.

2. A woman is a carrier of haemophilia A (X^H X^h) and is also heterozygous for an autosomal trait (Aa). She marries a normal man (X^H Y; AA). Calculate the probability their first-born son is affected with haemophilia. Show most steps using the product rule.

3. Karyotype Case 3 showed trisomy 21. During which meiotic division is nondisjunction most commonly occurring in cases of Down syndrome, and what is the evidence supporting this conclusion (hint: consider maternal age effects and the stage vulnerable to cohesin loss)?

4. An individual with Turner syndrome (45,X) is phenotypically female. Explain why the presence of a single X chromosome leads to infertility and why males (46,XY) with a single X chromosome are not similarly affected.

5. Philadelphia chromosome (a translocation between chromosomes 9 and 22, creating BCR-ABL fusion oncogene) causes chronic myeloid leukaemia (CML). Explain: (a) why a translocation creates a fusion gene; (b) what the BCR-ABL kinase does biochemically; (c) why imatinib (a tyrosine kinase inhibitor) is effective.

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: If you performed three replicates of a linkage mapping experiment, how would you analyze the variation in recombination frequencies? What statistical test would you use to determine if differences between gene pairs are significant?

7. **Experimental Error Analysis**: What are three potential sources of error in karyotype analysis? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you wanted to test whether two genes are linked or assort independently, how would you design the experiment? What data would you collect? How would you analyze it?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Cytogenetic Study of Environmental Mutagens**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- Choose an environmental mutagen (e.g., tobacco smoke, pesticides, radiation)
- Formulate a hypothesis about its effect on chromosome structure or number
- Design an experiment using model organisms (e.g., onion root tip, fruit fly)

**Session 2**: Data Collection and Analysis
- Expose organisms to different concentrations of mutagen
- Prepare and analyze chromosome spreads
- Quantify chromosome abnormalities (breaks, fragments, aneuploidy)

**Session 3**: Data Interpretation and Presentation
- Compare abnormality rates between control and treated groups
- Calculate statistical significance
- Create a scientific poster or presentation

## Real-World Problem Solving: Genetic Counseling {.unnumbered}

**Case Study: Prenatal Screening for Chromosomal Abnormalities**

1. **Research Task**: Investigate the different methods for prenatal screening and diagnosis (ultrasound, serum markers, NIPT, amniocentesis). What are the advantages and limitations of each?

2. **Ethical Consideration**: Should most pregnant women be offered prenatal screening for chromosomal abnormalities? What are the potential psychological and social implications of such testing?

3. **Policy Proposal**: Design a policy for responsible use of prenatal genetic testing. Consider: informed consent, access, counseling, and follow-up options.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Carrier females for X-linked recessive disorders such as hemophilia A and Duchenne muscular dystrophy often show milder or variable phenotypes compared with affected males. Use X-inactivation (the Lyon hypothesis) and somatic mosaicism to evaluate the cellular and developmental reasons for this pattern.
>
> (a) Explain why each somatic cell in a heterozygous female typically expresses just one of her two X chromosomes as the result of random X-inactivation, and why the choice of which X to inactivate is random and clonally inherited. What proportion of cells, on average, expresses the mutant allele in a carrier female, and what is the expected variance around that mean across tissues and individuals?
> (b) Describe how somatic mosaicism produces a patchwork of normal and mutant cells in a carrier female. For a clotting-factor disorder such as hemophilia A, evaluate why circulating factor levels in carrier females tend to fall within a wide range rather than at a fixed intermediate value, and identify at least one factor (such as skewed X-inactivation) that can shift a carrier toward the affected end of the spectrum.
> (c) Predict how the severity distribution would differ for an X-linked disorder whose phenotype depends on a local tissue (for example, a retinal cell-autonomous trait such as red-green color vision) versus one that depends on a circulating product. Identify which scenario is more likely to show patchy or sectoral phenotypes in carrier females, and justify the prediction in mechanistic terms.

## Safety and Ethics Notes {.unnumbered}

No chemical hazards. Karyotype analysis using real patient images: most should be de-identified. Discussion of chromosomal conditions should use person-first language and be conducted respectfully. Consider the ethical implications of genetic testing and counseling.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarizing the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_V_chromosomal_inheritance} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_V_chromosomal_inheritance} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `docs/manuscript/glossary.md`.
- Explore the Python code in `src/biology/genetics/genetics.py` for chromosomal inheritance calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
