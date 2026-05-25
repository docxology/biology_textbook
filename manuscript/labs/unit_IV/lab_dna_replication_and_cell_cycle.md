# Lab — DNA Replication and the Cell Cycle {.unnumbered}

\label{sec:lab_unit_IV_dna_replication_and_cell_cycle}

*This activity accompanies \cref{sec:unit_IV_dna_replication_and_cell_cycle} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate a mitotic staging dataset to calculate mitotic index
- Formulate testable hypotheses about how cell cycle progression varies across tissue types
- Identify independent, dependent, and controlled variables in cell biology experiments
- Analyze experimental data using statistical methods and cell biology concepts
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for DNA Replication and the Cell Cycle.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Describe the role of DNA polymerase III in chromosomal replication, focusing on its 5'→3' synthesis directionality and its requirement for a primer with a free 3'-OH. Why does this directionality force the lagging strand to be made as Okazaki fragments?
2. Name the three principal cell-cycle checkpoints and pair each with the type of cellular damage or status it monitors before allowing progression.
3. Predict how a temperature-sensitive mutation in DNA ligase would affect the lagging strand and the apparent mitotic index of a proliferating tissue once the restrictive temperature is applied. Justify your prediction in terms of replication-fork output.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of the cell cycle, predict which stage of mitosis will take the longest time. What molecular events occur during this stage that might explain its duration?

2. **Experimental Design**: What is the independent variable in a mitotic index experiment? What is the dependent variable? List at least 5 variables that should be controlled to ensure accurate staging.

3. **Scientific Context**: The mitotic index is used in cancer diagnosis. Why is a high mitotic index indicative of malignant tumors? What are the limitations of this measure?

4. **Quantitative Reasoning**: If a tissue has a mitotic index of 5%, approximately what percentage of cells are in S phase? (Assume S phase duration is about 6-8 hours in a 24-hour cycle.)

5. **Real-World Application**: Chemotherapy drugs often target rapidly dividing cells. How does the cell cycle explain why these drugs affect cancer cells more than normal cells? What are the side effects related to this mechanism?

## Lab Context: DNA Replication and the Cell Cycle {.unnumbered}

DNA replication is semiconservative (Meselson–Stahl, 1958): each daughter double helix retains one original strand and one newly synthesised strand. Replication proceeds bidirectionally from origins of replication; DNA polymerase extends DNA in the 5'→3' direction, requiring the lagging strand to be synthesised discontinuously as Okazaki fragments. The cell cycle (G₁ → S → G₂ → M) is driven by cyclin-CDK complexes and monitored by checkpoints (G₁/S, G₂/M, spindle assembly checkpoint). The mitotic index (fraction of cells in mitosis) reflects proliferative activity and is elevated in tumours.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Source-governance card for DNA Replication and the Cell Cycle: genomics/database source card: reference release, sample coverage, version, clinical boundary, and refresh trigger | 1 |
| Printed cell-cycle image cards from root tip, embryo, and tumour tissue datasets | 1 set |
| Mitotic stage decision key with example features | 1 |
| Meselson-Stahl simulation dataset (printed) | 1 |
| Cell cycle timeline diagram (printed) | 1 per student |
| Checkpoint perturbation cards (untreated, DNA polymerase inhibitor, spindle poison) | 1 set |
| Transparent grid overlay or printed counting frame | 1 |
| Calculator | 1 |
| Calculator or optional Python REPL with this project installed | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Mitotic Index Determination from Image Cards {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how the mitotic index might differ among root tip, embryo, and tumour image datasets.

2. **Identify Variables**:
   - Independent variable: Tissue dataset type
   - Dependent variable: Mitotic index (% cells in mitosis)
   - Controlled variables: image source, magnification label, counting frame size, staging key, scorer training, and exclusion rules.

3. **Set Up Controls**: Use the instructor-provided answer-key subset as a positive control for each mitotic stage and a non-dividing tissue card as a negative control. Before scoring the unknown cards, each group must reach at least 80% agreement on the control cards.

4. **Apply the Staging Key**:
   - Place the transparent grid over each printed image card.
   - Classify exactly 100 consecutive visible cells per card as interphase, prophase, metaphase, anaphase, telophase, or "uncertain."
   - Record uncertain cells separately; do not force a stage call unless the chromosome features match the decision key.

5. **Data Collection**:
   - Score three cards per tissue dataset, with two students independently scoring one shared card to estimate inter-rater reliability.
   - Calculate mitotic index = (cells in mitosis ÷ total cells counted) × 100%.
   - Report the mean, range, and standard error across replicate cards; flag any card whose uncertain-cell count exceeds 10%.

### Part 2: Computational Biology Exercise — Cell Cycle Modeling with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Check template-strand logic before interpreting replication and cell-cycle data.

```python
from biology.genetics import cpg_methylation_remaining, dna_complement, transcribe_dna_to_mrna

template = "TACGGA"
print("complement:", dna_complement(template))
print("mRNA:", transcribe_dna_to_mrna(template))
print("methylation after 3 divisions:", round(cpg_methylation_remaining(0.9, 3, 0.85), 3))
```
### Part 3: Semiconservative Replication Analysis {.unnumbered}

6. **Design an Alternative Investigation**: Using the checkpoint perturbation cards, design a paper simulation to test the effect of a drug that inhibits DNA polymerase on cell cycle progression. What hypothesis would you test? Which stage proportions would be your evidence?

7. **Hypothesis**: Predict how inhibiting DNA polymerase would affect the duration of S phase and the overall cell cycle time.

## Data Recording {.unnumbered}

| Stage | Number of cells | Proportion (%) | Estimated time in stage (min)* |
| ----- | --------------- | -------------- | ------------------------------ |
| Interphase | | | |
| Prophase | | | |
| Metaphase | | | |
| Anaphase | | | |
| Telophase | | | |
| **Total** | 100 | 100% | 24 h total |

Mitotic index: _______ %  
Inter-rater agreement on shared card: _______ %  
Cards excluded or flagged, with reason: ____________________

Generation 2 Meselson-Stahl prediction (sketch):

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model replication dynamics and checkpoint outcomes.
- **Data skill to practice:** Interpret replication or cell-cycle data from timing, labeling, or checkpoint perturbations.
- **BioSkills emphasis:** Process of science, Science and society, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**DNA Replication and the Cell Cycle** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: When scoring mitotic stages, Meselson-Stahl bands, or replication-fidelity cards, tie every classification to the molecular event it claims to show and to a stated counting or banding rule another group could reproduce. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Replicon Size and S-Phase Timing in Humans {.unnumbered}

**Problem:** The human diploid genome contains roughly 3.2 × 10⁹ base pairs and is replicated from approximately 50,000 origins of replication. Each replication fork moves at about 1,000 bp per second, and forks travel bidirectionally from each origin. Estimate the average replicon size, the time required to finish one replicon, and assess whether these numbers are consistent with an observed S-phase duration of about 8 hours.

**Solution:**

- Average replicon size = 3.2 × 10⁹ bp ÷ 50,000 origins ≈ 6.4 × 10⁴ bp per replicon.
- Because two forks diverge from each origin, each fork covers half of the replicon, or about 3.2 × 10⁴ bp.
- Time per fork = 3.2 × 10⁴ bp ÷ 1,000 bp s⁻¹ = 32 s, so one replicon finishes in about 32 seconds of fork travel.
- The full genome could in principle finish in well under an hour if every origin fired at once; the measured S phase of ~8 hours (~28,800 s) is far longer than the per-replicon time, which fits a model in which origins fire in temporally staggered clusters rather than synchronously.

**Interpretation:** Replicon-level kinetics are not the rate-limiting feature of S phase; origin firing schedules, replication-timing programs, and fork stalling at hard-to-replicate regions tend to set the overall duration. This reframes "how long does replication take?" as a question about origin regulation rather than polymerase speed.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for DNA Replication and the Cell Cycle before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. Which stage of mitosis took the longest (highest proportion)? Which was shortest? Explain in terms of the molecular events occurring in each stage.

2. Your mitotic index suggests what fraction of cells are actively dividing. Would you expect a higher or lower mitotic index in: (a) a tumour; (b) a mature neuron; (c) a healing wound? Explain for each.

3. In the Meselson-Stahl simulation, after two rounds of replication in light medium: (a) what fraction of DNA molecules are hybrid (¹⁵N/¹⁴N)? (b) What fraction are light-light? How do these proportions distinguish semiconservative from conservative replication?

4. DNA polymerase requires a primer and extends DNA in the 5'→3' direction. Explain why the lagging strand is initiated multiple times as Okazaki fragments, and name the enzyme that seals these fragments.

5. A drug (e.g., taxol) stabilises microtubules and prevents spindle disassembly. At which checkpoint would cells arrest, and what specific checkpoint protein detects unattached kinetochores? Why is this drug effective against rapidly dividing cancer cells?


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A research team identifies a tumor cell line carrying a loss-of-function mutation in Wee1 kinase, which normally inhibits the CDK1-cyclin B complex until DNA replication is complete. The cells display elevated mitotic index, frequent chromosome bridges in anaphase, and signs of incomplete DNA replication at the time of mitotic entry. Evaluate the consequences of this perturbation by integrating cell-cycle control with genome integrity.
>
> (a) Explain mechanistically how loss of Wee1 activity weakens the G2/M checkpoint, and predict the order in which CDK1 activation, DNA replication completion, and nuclear envelope breakdown would occur in these cells relative to wild-type cells.
> (b) Connect the observed anaphase bridges and chromosome mis-segregation to the inferred biochemical defect, and propose two independent measurements (one molecular, one cytological) that would test whether the elevated mitotic index reflects faster cycling or premature mitotic entry with unreplicated DNA.

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: Calculate the standard error of the mean (SEM) for your mitotic index across replicate cards. Construct a 95% confidence interval. How precise is your estimate?

7. **Experimental Error Analysis**: What are three potential sources of error in image-based mitotic staging? How could you modify the scoring rules or dataset design to reduce each source of error?

8. **Experimental Design**: If you wanted to test the effect of a new chemotherapy drug on cell cycle progression, what would you measure? How would you distinguish between drugs that affect DNA synthesis vs. those that affect mitosis?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Cancer Cell Detection Tool Using Machine Learning**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- Can we distinguish cancer cells from normal cells based on cell cycle abnormalities?
- What features (size, shape, staining intensity, mitotic index) are most predictive?
- Write a reproducible sampling plan for choosing public image datasets and metadata fields

**Session 2**: Data Collection and Analysis
- Use public image datasets of normal and cancer cells
- Extract features using image analysis software
- Train a simple machine learning classifier (e.g., logistic regression)

**Session 3**: Tool Development and Testing
- Test your classifier on unseen data
- Calculate sensitivity, specificity, and accuracy
- Create a scientific poster or presentation

## Real-World Problem Solving: Cancer Diagnostics {.unnumbered}

**Case Study: Liquid Biopsy for Cancer Detection**

Liquid biopsies detect circulating tumor DNA (ctDNA) or circulating tumor cells (CTCs) in blood samples. 

1. **Research Task**: Investigate the advantages and limitations of liquid biopsies compared to traditional tissue biopsies.

2. **Ethical Consideration**: Should liquid biopsy screening be offered to asymptomatic individuals? What are the potential benefits and risks of early detection?

3. **Policy Proposal**: Design a screening program for a specific cancer type using liquid biopsy technology. Consider cost-effectiveness, accessibility, and follow-up procedures.

## Safety and Ethics Notes {.unnumbered}

Default lab work uses printed datasets primarily, with no biological or chemical hazards. When using machine learning on human data, ensure privacy, use de-identified public datasets, and obtain proper consent for any non-public images. Any wet-lab root-tip squash should be treated as an optional instructor-supervised extension with local safety approval, not as a required activity.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_IV_dna_replication_and_cell_cycle} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IV_dna_replication_and_cell_cycle} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/genetics/genetics.py` for DNA replication calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
