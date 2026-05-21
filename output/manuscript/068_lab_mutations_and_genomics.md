<!-- render:skip-beamer -->

# Lab 14 — Mutations, CRISPR, and Genomics {.unnumbered}

\label{sec:lab_unit_IV_mutations_and_genomics}

*This activity accompanies \cref{sec:unit_IV_mutations_and_genomics} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate a CRISPR-Cas9 editing scenario using sequence cards and gel images
- Formulate testable hypotheses about mutation effects on protein function
- Identify independent, dependent, and controlled variables in genome editing experiments
- Analyze experimental data using gel electrophoresis and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Mutations, CRISPR, and Genomics.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of mutation types, predict which class of mutation (synonymous, missense, nonsense, frameshift) would be most likely to cause a loss of protein function. Explain your reasoning.

2. **Experimental Design**: What is the independent variable in a CRISPR genome-editing data analysis? What is the dependent variable? List at least 5 variables that should be controlled to ensure specific interpretation.

3. **Scientific Context**: The T7E1 assay is commonly used to detect CRISPR-induced mutations. How does this assay work? What are its limitations?

4. **Quantitative Reasoning**: If a CRISPR editing dataset reports an editing efficiency of 30%, how many cells would need to be represented to infer 10 successfully edited cells? What factors might affect this estimate?

5. **Real-World Application**: Germline genome editing raises significant ethical concerns. What are the main arguments for and against editing human embryos to eliminate genetic diseases? Where do you stand on this issue?

## Background {.unnumbered}

Mutations — heritable changes in DNA sequence — can be neutral (synonymous), harmful (loss-of-function missense or nonsense), or beneficial (gain-of-function). CRISPR-Cas9 (Clustered Regularly Interspaced Short Palindromic Repeats) is a programmable nuclease: the guide RNA (gRNA; ~20 nt complementary to the target) directs Cas9 to create a blunt-ended double-strand break 3 bp upstream of the PAM sequence (5'-NGG-3'). Repair by NHEJ creates indel mutations (disruptive); HDR with a template creates precise edits.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Wild-type and mutant DNA sequences (printed cards: WT, SNP1, SNP2, frameshift) | 1 set |
| Codon table | 1 |
| CRISPR guide RNA design worksheet (target region provided) | 1 |
| Gel electrophoresis image (T7E1 assay: uncut control, CRISPR-treated) (printed) | 1 |
| Off-target candidate sequence cards with mismatch positions marked | 1 set |
| Editing-efficiency replicate dataset | 1 |
| Pangenome path cards: linear reference, alternate insertion path, inversion path, and read-alignment summaries | 1 set |
| Prime-editing gamma-globin promoter case card with pegRNA, intended edits, donor variability, and HbF readout | 1 |
| Ruler (mm) | 1 |
| Ethical debate scenario cards (4 scenarios) | 1 set |
| Calculator or optional Python REPL with this project installed | 1 |
| DNA ladder image (printed) | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Mutation Classification and Analysis {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how different mutation types (missense vs nonsense vs frameshift) affect protein function in a specific disease context (e.g., cystic fibrosis).

2. **Identify Variables**:
   - Independent variable: Mutation type (synonymous, missense, nonsense, frameshift)
   - Dependent variable: Predicted effect on protein function (neutral, mild, severe, lethal)
   - Controlled variables: Gene context, protein domain, evolutionary conservation, etc.

3. **Set Up Controls**: Why is it important to have a wild-type (WT) control sequence? What other controls could you include in a mutation classification experiment?

4. **Data Collection**:
   - Compare SNP1, SNP2, and frameshift sequences with the WT. For each: identify the nucleotide change, classify the mutation type, determine the amino acid change, and assess likely functional impact.
   - Use the provided codon table and protein domain information to inform your assessment.

### Part 2: Computational Biology Exercise - CRISPR gRNA Design and Efficiency Analysis {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Quantify sequence change with the same distance functions used in the chapter.

```python
from biology.genetics import gc_content, hamming_distance, jukes_cantor_distance

reference = "ATGCGTAC"
variant = "ATGAGTTC"
p_distance = hamming_distance(reference, variant) / len(reference)

print("GC reference:", round(gc_content(reference), 2))
print("Hamming distance:", hamming_distance(reference, variant))
print("Jukes-Cantor distance:", round(jukes_cantor_distance(p_distance), 3))
```
### Part 3: Gel Electrophoresis Interpretation {.unnumbered}

5. **Design an Alternative Investigation**: Instead of proposing a live genome-editing experiment, design a blinded analysis of printed gRNA-design scenarios. What hypothesis would you test about seed-region mismatches, GC content, and editing efficiency? Which sequence-card controls would you include?

6. **Hypothesis**: Predict the relationship between gRNA binding affinity and editing efficiency in the dataset. Would it be linear, saturating, or something else? Why?

### Part 4: Pangenome and Prime-Editing Decision Cards {.unnumbered}

7. Sort the pangenome path cards into three evidence classes: confidently represented by a single linear reference, better represented by an alternate graph path, and unresolved without long-read or phased evidence.
8. For the gamma-globin promoter prime-editing card, identify the intended regulatory effect, the difference between editing a coding sequence and editing an enhancer/promoter motif, and the donor-to-donor variability that would limit a comprehensive claim.
9. Build a decision matrix comparing Casgevy-style BCL11A enhancer disruption, base editing of an *HBB* point mutation, and prime editing of *HBG1/HBG2* promoter motifs. Score each for target logic, double-strand-break risk, validation burden, and current clinical maturity.

## Data Recording {.unnumbered}

| Sequence | Nucleotide change | Mutation type | AA change | Functional impact prediction |
| -------- | ----------------- | ------------- | --------- | ---------------------------- |
| SNP1 | | | | |
| SNP2 | | | | |
| Frameshift | | | | |

gRNA spacer sequences identified: (list most with PAM)

Gel band sizes: Control: _______ bp; Lane 2 bands: _______ bp, _______ bp  
Indel efficiency estimate = (cleavage bands / total DNA) × 100%: _______%
Off-target risk score for selected gRNA: _______; highest-risk mismatch pattern: _______
Replicate editing efficiencies: ___%, ___%, ___%; mean ± SEM: _______
Pangenome path selected: _______; graph evidence needed: _______; prime-editing validation readout: _______

Ethics summary (2–3 sentences per group position):

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Evaluate genome-editing or variant-calling scenarios.
- **Data skill to practice:** Classify variants and predict likely molecular effect from sequence evidence.
- **BioSkills emphasis:** Process of science, Science and society, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Mutations, CRISPR, and Genomics** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: When classifying variants from the paper dataset, separate the act of calling a variant from interpreting its pathogenicity, and record the ancestry coverage and evidence threshold behind any clinical claim. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. Why does a frameshift mutation typically have a more severe effect on protein function than a missense mutation? Under what circumstance could a frameshift mutation be silent (no effect on protein)?

2. A gRNA with sequence mismatches at positions 1–4 from the PAM distal end is less likely to cause cutting than mismatches at the seed region (positions 1–12 from PAM-proximal end). Why? What does this imply about gRNA design strategy to minimise off-target effects?

3. The T7E1 enzyme cleaves primarily at mismatched positions in heteroduplex DNA. Explain why NHEJ-induced indels would create mismatches and thus be detectable by T7E1, whereas HDR edits with perfect template would not be.

4. In 2018, He Jiankui used CRISPR to edit the CCR5 gene in human embryos, which were then implanted and brought to term. The stated goal was to confer HIV resistance. Using your ethical framework from Part D: name two distinct ethical objections to this experiment beyond the scientific accuracy concerns.

5. A patient with Duchenne muscular dystrophy (DMD) has a frameshift in exon 51 causing a premature stop codon. Propose a CRISPR-based strategy (exon skipping via splice site disruption) to restore the reading frame. What are the limitations of this approach?
6. A short-read sample maps poorly to a disease locus because one haplotype contains a 3-kb insertion absent from the linear reference. Explain how a pangenome graph could represent the evidence more fairly, and name one validation step before using the call clinically.

## Extension Analysis Questions {.unnumbered}

7. **Statistical Analysis**: If the printed dataset includes three replicate editing-efficiency estimates for each gRNA, how would you analyze the variation? What statistical test would you use to determine if differences between gRNAs are significant?

8. **Experimental Error Analysis**: What are three potential sources of error in T7E1 gel analysis? How could you modify the procedure to reduce each source of error?

9. **Experimental Design**: If you wanted to test the effect of a specific mutation on protein function, how would you design a paper-based evidence plan before any wet work? What sequence controls, phenotype readouts, and off-target checks would be required?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a CRISPR-based Diagnostic Tool for Infectious Disease**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- Can CRISPR-Cas12a (Cpf1) be used to detect viral DNA (e.g., SARS-CoV-2) with high specificity?
- What are the advantages of CRISPR diagnostics over PCR?
- Write a detailed decision workflow for a CRISPR-based diagnostic assay using provided sequences and fluorescence traces

**Session 2**: Data Collection and Analysis
- Design gRNAs specific for a viral target from printed sequence alignments
- Simulate detection by classifying provided fluorescence-output traces
- Analyze detection thresholds, false positives, and false negatives over time

**Session 3**: Tool Development and Testing
- Optimize assay conditions in a decision matrix (gRNA concentration, reaction time, detection threshold)
- Test specificity against related viral strains
- Create a scientific poster or presentation

## Real-World Problem Solving: Genome Editing Ethics {.unnumbered}

**Case Study: Somatic vs Germline Editing**

1. **Research Task**: Investigate the current regulatory landscape for somatic vs germline genome editing in two different countries (e.g., USA vs China).

2. **Ethical Consideration**: Should there be a global moratorium on germline editing? What are the arguments for and against international regulation?

3. **Policy Proposal**: Design a policy framework for the responsible use of germline genome editing. Consider: which diseases would qualify, who would have access, how would long-term effects be monitored?

## Safety and Ethics Notes {.unnumbered}

No biological or chemical hazards in this lab (paper/card based). Most CRISPR discussion is theoretical. When discussing patient/human scenarios, maintain respectful, evidence-based discourse. Follow institutional guidelines for ethical discussions.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_IV_mutations_and_genomics} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IV_mutations_and_genomics} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/genetics/genetics.py` for mutation analysis calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
