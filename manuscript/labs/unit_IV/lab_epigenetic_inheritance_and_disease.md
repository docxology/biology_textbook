# Lab — Epigenetic Inheritance and Disease {#sec:lab_unit_IV_epigenetic_inheritance_and_disease .unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Epigenetic Inheritance and Disease.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->

*This activity accompanies \cref{sec:unit_IV_epigenetic_inheritance_and_disease} of the textbook — review that chapter before attempting the exercises below.*

## Lab Context: Epigenetic Inheritance and Disease {.unnumbered}

This extension lab focuses on three-dimensional genome organization, transgenerational inheritance claims, and disease-linked epigenetic dysregulation using printed datasets rather than live database queries.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_IV_epigenetic_inheritance_and_disease_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Epigenetic Inheritance and Disease: genomics/database source card: reference release, sample coverage, version, clinical boundary, and refresh trigger | 1 |
| Printed datasets, cards, and worksheets referenced below | 1 set per group |
| Graph paper or plain paper for diagrams | 1 |
| Calculator | 1 |

## Paper-Based Investigation {.unnumbered}

5. **Design an Alternative Investigation**: Instead of just analyzing provided data, design a paper-based study plan to test how a specific nutrient (e.g., folate, B12) affects DNA methylation patterns in a model organism. What hypothesis would you test? Which tissue datasets, controls, and metadata fields would you require?

6. **Hypothesis**: Predict the direction and magnitude of methylation changes you might observe with nutrient supplementation.

## Data Recording {.unnumbered}

: Alignment and Rubric Map: Condition and Repressor bound to operator?. {#tbl:unit_IV_epigenetic_inheritance_and_disease_alignment_and_rubric_map_2}
| Condition | Repressor bound to operator? | CAP-cAMP at promoter? | lac genes expressed? |
| --------- | ---------------------------- | --------------------- | -------------------- |
| No lactose, no glucose | Yes | No | No |
| Lactose present, no glucose | | | |
| No lactose, glucose present | | | |
| Lactose + glucose | | | |

MS-PCR result — BRCA1: Methylated? (Y/N)  Normal: ___  Cancer: ___  
ChIP-seq — BRCA1 H3K4me3 peak height: Normal: ___ Cancer: ___ Interpretation: ___

Agouti mouse case study: Methyl donor involved: ___; Epigenetic enzyme: ___; Phenotypic consequence: ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Compare inheritance models and predict disease consequences of regulatory disruption.
- **Data skill to practice:** Interpret Hi-C, imprinting, or transgenerational datasets with causal caution.
- **BioSkills emphasis:** Process of science, Science and society, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Epigenetics and Gene Regulation** with a reproducibility pass:

: Alignment and Rubric Map: Evidence check and Student action. {#tbl:unit_IV_epigenetic_inheritance_and_disease_alignment_and_rubric_map_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: When interpreting methylation, chromatin, or gene-silencing datasets, demand a causal perturbation, a matched cell type, and a control for timing or inheritance before reading a pattern as a regulatory mechanism. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Estimating Methylated CpG Sites in Cancer vs Normal {.unnumbered}

**Problem:** A tumor suppressor gene has a CpG island promoter containing 15 CpG dinucleotides. Bisulfite sequencing reports an average methylation level of 85% across these sites in cancer cells and 12% in matched normal cells. Assume the silencing threshold for this promoter is methylation of at least 80% of CpGs. Estimate how many CpG sites are methylated in each condition and judge whether the gene is likely active in each.

**Solution:**

- Cancer cells: 0.85 × 15 ≈ 12.75, round to 13 of 15 sites methylated. The fraction methylated (13/15 ≈ 0.87) exceeds the 0.80 threshold.
- Normal cells: 0.12 × 15 ≈ 1.8, round to about 2 of 15 sites methylated. The fraction methylated (2/15 ≈ 0.13) sits well below the 0.80 threshold.

**Interpretation:** In the tumor sample the promoter has crossed the silencing threshold and the gene is expected to be transcriptionally repressed; in the matched normal tissue the same promoter is hypomethylated and the gene is expected to be expressed. This pattern — promoter hypermethylation of a tumor suppressor — is consistent with epigenetic loss of function of a single allele or both alleles without any change to the protein-coding DNA sequence.

## Analysis Questions {.unnumbered}

1. The lac repressor is an allosteric protein. How does allolactose binding change the shape of the repressor so that it can no longer bind the operator? Relate this to the induced fit model.

2. In catabolite repression, high glucose causes low cAMP because glucose inhibits adenylate cyclase. Trace: high glucose → [cAMP] → CAP-cAMP binding → lac promoter activity. Why does the cell preferentially use glucose over lactose?

3. A cancer cell has methylation of a tumor suppressor gene promoter but no mutation in the coding sequence. Is this a genetic or epigenetic mutation? Why is this clinically important for therapy selection (hint: methyltransferase inhibitors vs traditional chemotherapy)?

4. The agouti mouse model showed that maternal diet (methyl-group-rich foods) changes offspring coat color and obesity risk through epigenetic marks. Name the methyl donors involved (from diet) and the epigenetic writing enzyme that places the mark on CpG islands.

5. Design an experiment using induced pluripotent stem cell (iPSC) technology to test whether erasing epigenetic marks (global demethylation) is sufficient to reprogram a differentiated skin fibroblast. What control groups would you include?


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A clinical team is debating how to treat two patients whose tumors both show loss of expression of the same tumor suppressor gene. Tumor A carries a frameshift coding mutation that truncates the protein at amino acid 87 (full length 451). Tumor B carries no coding mutation but shows 90% promoter CpG methylation and a strong H3K27me3 signal across the gene body. Evaluate whether the epigenetic silencing in Tumor B is functionally equivalent to the truncating mutation in Tumor A.
>
> (a) Compare the two lesions across three dimensions — reversibility in principle, heritability through mitosis and (where relevant) meiosis, and feasibility of therapeutic reactivation — and identify at least one experiment that could distinguish a fully epigenetic lesion from a small undetected coding lesion.
> (b) Recommend a treatment strategy for each tumor that follows from your analysis (for example, a DNA methyltransferase inhibitor or an EZH2 inhibitor for one tumor, a synthetic-lethal partner for the other), and state one piece of evidence that would make you change the recommendation.

## Extension Analysis Questions {.unnumbered}

6. Methylation-sensitive restriction enzymes (e.g., HpaII) and methyl-insensitive isoschizomers (e.g., MspI) cut the same sequence but primarily MspI cuts methylated DNA. Describe one experimental use of this enzyme pair for mapping genome-wide methylation without bisulphite conversion.

7. Transgenerational epigenetic inheritance in humans remains controversial. What *specific* molecular evidence would convince you it is real? (Address confounding: shared environment, germline reprogramming.)

8. The textbook introduces CRISPR-dCas9 epigenome editing. Design a dCas9-based experiment to re-activate the silenced tumor-suppressor gene you identified in the ChIP-seq analysis, and predict one off-target risk.

9. **Statistical Analysis**: If you performed three replicates of an MS-PCR experiment, how would you analyze the variation in methylation status? What statistical test would you use to determine if differences between groups are significant?

10. **Experimental Error Analysis**: What are three potential sources of error in epigenetic data analysis? How could you modify the procedure to reduce each source of error?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design an Epigenetic Diet Intervention Study**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- Can dietary methyl donors (folate, B12, choline) alter DNA methylation patterns in humans?
- What genes might be most responsive to such changes?
- Write a detailed protocol for a dietary intervention study

**Session 2**: Data Collection and Analysis
- Collect dietary intake data and DNA samples (or use public datasets)
- Analyze methylation at candidate genes using bisulphite sequencing
- Compare methylation changes between intervention and control groups

**Session 3**: Data Interpretation and Presentation
- Correlate methylation changes with health outcomes
- Create a scientific poster or presentation
- Discuss limitations and future directions

## Real-World Problem Solving: Epigenetic Ethics {.unnumbered}

**Case Study: Epigenetic Discrimination**

1. **Research Task**: Investigate the current legal protections against genetic discrimination (e.g., GINA in the US). Do these laws cover epigenetic information? Why or why not?

2. **Ethical Consideration**: Should employers or insurance companies be allowed to use epigenetic age estimates to make decisions? What are the potential benefits and risks?

3. **Policy Proposal**: Design a policy framework for the ethical use of epigenetic information. Consider: consent, privacy, access, and potential for discrimination.

## Safety and Ethics Notes {.unnumbered}

Data-analysis primarily lab — no reagents, no risk. Discussions of patient cancer data should respect privacy principles (de-identification; aggregate reporting). Agouti mouse studies involve animal experimentation — students should briefly discuss the 3Rs framework (Replacement, Reduction, Refinement) and when mouse models are (and are not) scientifically justified. Epigenetic age clocks have attracted commercial wellness-industry interest; discuss the limits of current evidence before drawing lifestyle conclusions from a single patient's clock.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Epigenetic Inheritance and Disease before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarizing the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_IV_epigenetic_inheritance_and_disease} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IV_epigenetic_inheritance_and_disease} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/genetics/genetics.py` for epigenetic calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
