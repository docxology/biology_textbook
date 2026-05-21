<!-- render:skip-beamer -->

# Lab 15 — Epigenetics and Gene Regulation {.unnumbered}

\label{sec:lab_unit_IV_epigenetics_and_gene_regulation}

*This activity accompanies \cref{sec:unit_IV_epigenetics_and_gene_regulation} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate an epigenetic data-analysis scenario to determine gene regulation
- Formulate testable hypotheses about how environmental factors affect epigenetic marks
- Identify independent, dependent, and controlled variables in epigenetic studies
- Analyze experimental data using methylation analysis and ChIP-seq interpretation
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Epigenetics and Gene Regulation.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of DNA methylation, predict how a gene promoter's methylation status might change in response to a high-sugar diet. Would you expect hypermethylation or hypomethylation? Why?

2. **Experimental Design**: What is the independent variable in an epigenetic diet study? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: The Horvath epigenetic clock uses DNA methylation patterns to predict biological age. Why might biological age differ from chronological age? What factors can accelerate epigenetic ageing?

4. **Quantitative Reasoning**: If a methylation-sensitive PCR shows a 200 bp band in the untreated sample and a 400 bp band in the bisulphite-treated sample, what does this tell you about the methylation status of the gene?

5. **Real-World Application**: Epigenetic drugs like azacitidine are used to treat certain cancers. How do these drugs work? What are the potential side effects of globally altering epigenetic marks?

## Background {.unnumbered}

Epigenetic regulation controls gene expression without altering DNA sequence: DNA methylation (CpG islands; methylation = gene silencing, generally), histone modification (H3K4me3 = activation; H3K27me3 = silencing; H3K9ac = activation), and non-coding RNA (miRNA, siRNA). The lac operon is the classical model for prokaryotic transcription regulation: the lac repressor blocks transcription in the absence of lactose; allolactose (a lactose isomer) binds the repressor and releases it from the operator.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| MS-PCR gel image (printed: two lanes per sample, bisulphite-treated/untreated) | 1 |
| ChIP-seq track printout (H3K4me3 signal at BRCA1 promoter: tumour vs normal) | 1 |
| Lac operon gene-expression logic table (worksheet) | 1 per student |
| "Agouti mouse" case study reading (1 page) | 1 per student |
| Coloured pens | 3 |
| Calculator or optional Python REPL with this project installed | 1 |
| Epigenetic age calculator worksheet | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Epigenetic Data Analysis {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how a specific environmental factor (diet, stress, toxins) might affect DNA methylation patterns at a particular gene.

2. **Identify Variables**:
   - Independent variable: Environmental exposure (e.g., high-fat diet, pollutant)
   - Dependent variable: DNA methylation level at specific CpG sites
   - Controlled variables: Age, sex, genetic background, sample processing, etc.

3. **Set Up Controls**: Why is it important to include both treated and untreated control samples in epigenetic studies? What other controls could you include to validate your results?

4. **Data Collection**:
   - Interpret the MS-PCR gel: determine which gene is methylated in cancer vs normal cells.
   - Analyze the ChIP-seq track: compare H3K4me3 peak height at the BRCA1 promoter between tumour and normal. Does BRCA1 appear silenced in the tumour?
   - Complete the lac operon logic table for four conditions.
   - Read and analyze the agouti mouse case study.

### Part 2: Computational Biology Exercise - Epigenetic Age Prediction with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Model maintenance methylation and classify histone marks without external files.

```python
from biology.genetics import cpg_methylation_remaining, histone_modification_state

for efficiency in (0.95, 0.85, 0.60):
    remaining = cpg_methylation_remaining(0.8, divisions=4, maintenance_efficiency=efficiency)
    print(efficiency, round(remaining, 3))

for mark in ("H3K27me3", "H3K27ac", "H3K4me2"):
    print(mark, histone_modification_state(mark))
```
### Part 3: Advanced Epigenetic Analysis {.unnumbered}

5. **Design an Alternative Investigation**: Instead of just analyzing provided data, design a paper-based study plan to test how a specific nutrient (e.g., folate, B12) affects DNA methylation patterns in a model organism. What hypothesis would you test? Which tissue datasets, controls, and metadata fields would you require?

6. **Hypothesis**: Predict the direction and magnitude of methylation changes you might observe with nutrient supplementation.

## Data Recording {.unnumbered}

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

- **Primary evidence goal:** Compare regulatory perturbations and predicted expression outputs.
- **Data skill to practice:** Interpret chromatin or expression evidence from simple regulatory datasets.
- **BioSkills emphasis:** Process of science, Science and society, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Epigenetics and Gene Regulation** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: When interpreting methylation, chromatin, or gene-silencing datasets, demand a causal perturbation, a matched cell type, and a control for timing or inheritance before reading a pattern as a regulatory mechanism. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. The lac repressor is an allosteric protein. How does allolactose binding change the shape of the repressor so that it can no longer bind the operator? Relate this to the induced fit model.

2. In catabolite repression, high glucose causes low cAMP because glucose inhibits adenylate cyclase. Trace: high glucose → [cAMP] → CAP-cAMP binding → lac promoter activity. Why does the cell preferentially use glucose over lactose?

3. A cancer cell has methylation of a tumour suppressor gene promoter but no mutation in the coding sequence. Is this a genetic or epigenetic mutation? Why is this clinically important for therapy selection (hint: methyltransferase inhibitors vs traditional chemotherapy)?

4. The agouti mouse model showed that maternal diet (methyl-group-rich foods) changes offspring coat colour and obesity risk through epigenetic marks. Name the methyl donors involved (from diet) and the epigenetic writing enzyme that places the mark on CpG islands.

5. Design an experiment using induced pluripotent stem cell (iPSC) technology to test whether erasing epigenetic marks (global demethylation) is sufficient to reprogram a differentiated skin fibroblast. What control groups would you include?

## Extension Analysis Questions {.unnumbered}

6. Methylation-sensitive restriction enzymes (e.g., HpaII) and methyl-insensitive isoschizomers (e.g., MspI) cut the same sequence but primarily MspI cuts methylated DNA. Describe one experimental use of this enzyme pair for mapping genome-wide methylation without bisulphite conversion.

7. Transgenerational epigenetic inheritance in humans remains controversial. What *specific* molecular evidence would convince you it is real? (Address confounding: shared environment, germline reprogramming.)

8. The textbook introduces CRISPR-dCas9 epigenome editing. Design a dCas9-based experiment to re-activate the silenced tumour-suppressor gene you identified in the ChIP-seq analysis, and predict one off-target risk.

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

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_IV_epigenetics_and_gene_regulation} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IV_epigenetics_and_gene_regulation} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/genetics/genetics.py` for epigenetic calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
