# Lab — Chromatin and Epigenetic Mechanisms {#sec:lab_unit_IV_chromatin_and_epigenetic_mechanisms .unnumbered}


*This activity accompanies \cref{sec:unit_IV_chromatin_and_epigenetic_mechanisms} of the textbook — review that chapter before attempting the exercises below.*

*This activity accompanies \cref{sec:unit_IV_chromatin_and_epigenetic_mechanisms} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate an epigenetic data-analysis scenario to determine gene regulation
- Formulate testable hypotheses about how environmental factors affect epigenetic marks
- Identify independent, dependent, and controlled variables in epigenetic studies
- Analyze experimental data using methylation analysis and ChIP-seq interpretation
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Chromatin and Epigenetic Mechanisms.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define a CpG island and explain why dense unmethylated CpGs in a gene promoter region correlate with active transcription. What molecular property of cytosine changes when a CpG is methylated, and how does that alter transcription-factor or reader-protein binding?
2. Describe what histone deacetylase (HDAC) inhibitors do to chromatin at a structural level, and predict whether HDAC inhibition would tend to raise or lower expression of genes whose promoters carry the active mark H3K4me3.
3. Compare H3K4me3 and H3K27me3 with respect to where each tends to deposit, which reader complexes recognize each, and what transcriptional outcome each is associated with. Predict what would happen to a developmental gene that simultaneously carries both marks ("bivalent" chromatin) once one mark is removed.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of DNA methylation, predict how a gene promoter's methylation status might change in response to a high-sugar diet. Would you expect hypermethylation or hypomethylation? Why?

2. **Experimental Design**: What is the independent variable in an epigenetic diet study? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: The Horvath epigenetic clock uses DNA methylation patterns to predict biological age. Why might biological age differ from chronological age? What factors can accelerate epigenetic aging?

4. **Quantitative Reasoning**: If a methylation-sensitive PCR shows a 200 bp band in the untreated sample and a 400 bp band in the bisulphite-treated sample, what does this tell you about the methylation status of the gene?

5. **Real-World Application**: Epigenetic drugs like azacitidine are used to treat certain cancers. How do these drugs work? What are the potential side effects of globally altering epigenetic marks?

## Lab Context: Chromatin and Epigenetic Mechanisms {.unnumbered}

Epigenetic regulation controls gene expression without altering DNA sequence: DNA methylation (CpG islands; methylation = gene silencing, generally), histone modification (H3K4me3 = activation; H3K27me3 = silencing; H3K9ac = activation), and non-coding RNA (miRNA, siRNA). The lac operon is the classical model for prokaryotic transcription regulation: the lac repressor blocks transcription in the absence of lactose; allolactose (a lactose isomer) binds the repressor and releases it from the operator.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_IV_chromatin_and_epigenetic_mechanisms_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Chromatin and Epigenetic Mechanisms: genomics/database source card: reference release, sample coverage, version, clinical boundary, and refresh trigger | 1 |
| MS-PCR gel image (printed: two lanes per sample, bisulphite-treated/untreated) | 1 |
| ChIP-seq track printout (H3K4me3 signal at BRCA1 promoter: tumor vs normal) | 1 |
| Lac operon gene-expression logic table (worksheet) | 1 per student |
| "Agouti mouse" case study reading (1 page) | 1 per student |
| Colored pens | 3 |
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
   - Analyze the ChIP-seq track: compare H3K4me3 peak height at the BRCA1 promoter between tumor and normal. Does BRCA1 appear silenced in the tumor?
   - Complete the lac operon logic table for four conditions.
   - Read and analyze the agouti mouse case study.

### Part 2: Computational Biology Exercise — Epigenetic Age Prediction with Python {.unnumbered}

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

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Chromatin and Epigenetic Mechanisms before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

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
**Chromatin and Epigenetic Mechanisms** with a reproducibility pass:

: Source-Governance Checkpoint: Evidence check and Student action. {#tbl:unit_IV_chromatin_and_epigenetic_mechanisms_source_governance_checkpoint}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: epigenetic claims require causal perturbation, cell-type specificity, timing, and inheritance controls. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.
