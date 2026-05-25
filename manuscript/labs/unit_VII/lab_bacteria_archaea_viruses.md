# Lab — Bacteria, Archaea, and Viruses {#sec:lab_unit_VII_bacteria_archaea_viruses .unnumbered}


*This activity accompanies \cref{sec:unit_VII_bacteria_archaea_viruses} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate a bacterial identification case packet using Gram-stain images
- Formulate testable hypotheses about how environmental factors affect simulated bacterial growth
- Identify independent, dependent, and controlled variables in microbiology experiments
- Analyze experimental data using colony counting and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Bacteria, Archaea, and Viruses.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter on prokaryote and viral biology.*

1. Explain how Gram staining differentiates between Gram-positive and Gram-negative bacteria. Reference the role of peptidoglycan thickness and the outer membrane, and describe what color each type appears after the full stain sequence (crystal violet, iodine, ethanol, safranin).
2. Describe the lytic and lysogenic cycles of a temperate bacteriophage. For each cycle, state where the phage genome resides and one molecular event that defines that phase.
3. Prokaryotes lack membrane-bound organelles. State one process (e.g., respiration, transcription) that occurs in a different cellular location in bacteria compared to eukaryotes, and explain the implication for antibiotic targeting.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of Gram staining, predict which type of bacteria (Gram-positive or Gram-negative) would be more resistant to antibiotics that target cell wall synthesis. Explain your reasoning.

2. **Experimental Design**: What is the independent variable in a bacterial growth dataset? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid conclusions.

3. **Scientific Context**: The Gram stain is a fundamental tool in microbiology. Why is it important to classify bacteria as Gram-positive or Gram-negative? How does this classification inform treatment decisions?

4. **Quantitative Reasoning**: A printed dilution dataset shows 150 colonies on a 10⁻⁵ dilution plate, with 0.1 mL plated. What is the concentration of bacteria in the original culture? Show your calculation.

5. **Real-World Application**: Antibiotic resistance is a growing problem. How does the misuse of antibiotics in agriculture contribute to the evolution of resistant bacteria? What policies could help address this issue?

## Lab Context: Bacteria, Archaea, and Viruses {.unnumbered}

Prokaryotes — Bacteria and Archaea — are the most abundant life forms on Earth (~10³¹ cells). Gram staining differentiates bacteria based on cell wall composition: Gram-positive (thick peptidoglycan layer retains crystal violet — purple) vs Gram-negative (thin peptidoglycan + outer membrane — loses crystal violet, appears pink after safranin counterstain). Viruses are acellular entities that replicate primarily inside host cells; bacteriophages infect bacteria and follow either lytic (immediate replication and lysis) or lysogenic (DNA integration, dormancy) cycles.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_VII_bacteria_archaea_viruses_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Bacteria, Archaea, and Viruses: pathogen-surveillance source card: organism-resistance pair, official guidance date, setting, and intervention limit | 1 |
| Gram-stain image cards with metadata removed | 1 set |
| Known Gram-positive and Gram-negative control image cards | 1 set |
| Printed serial-dilution plate images (10⁻⁴ to 10⁻⁶, three replicates) | 1 set |
| Bacterial growth curve data under temperature, pH, and salt scenarios | 1 |
| Phage life-cycle decision cards | 1 set |
| AMR treatment decision matrix | 1 |
| Horizontal-gene-transfer map cards: plasmid, transposon, integron, phage, transformation, wastewater, and hospital ward | 1 set |
| *Candida auris* clinical triage card: colonization vs infection, identification method, surface persistence, susceptibility result | 1 |
| Calculator or optional Python REPL with this project installed | 1 |
| Ruler or transparent counting grid | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Gram-Stain Image Classification {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how the Gram stain results will differ between *E. coli* and *Bacillus* species.

2. **Identify Variables**:
   - Independent variable: Bacterial species
   - Dependent variable: Gram stain result (purple vs pink) and cell morphology
   - Controlled variables: image source, colorcalibration note, scale label, scoring key, scorer training, and blind-card order.

3. **Set Up Controls**: Score the known Gram-positive and Gram-negative control cards first. What other controls could you include to ensure accurate identification, such as a mixed-species image, a low-quality image, or a blinded duplicate?

4. **Data Collection**:
   - Classify each blinded image card as Gram-positive, Gram-negative, mixed, or uninterpretable.
   - Record: color (purple = Gram+, pink = Gram-), cell shape (coccus, bacillus, spirillum), arrangement (single, pairs, chains, clusters), and confidence score (1-5).
   - Compare independent scorers. Resolve disagreements primarily after recording the original calls.

### Part 2: Computational Biology Exercise — Bacterial Growth Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Use the microbiology module to check growth and MIC calculations.

```python
from biology.microbiology import bacterial_growth_curve, doubling_time, mic_fold_dilution

growth = bacterial_growth_curve(N0=1_000, doubling_time_hr=0.5, t_end_hr=4.0)
print("final population:", int(growth.populations[-1]))
print("doubling time from counts:", round(doubling_time(1_000, 16_000, 2.0), 2))
print("MIC dilution series:", mic_fold_dilution(128.0, dilution_factor=2, n_tubes=5))
```
### Part 3: Serial Dilution and Colony Counting from Plate Images {.unnumbered}

5. **Design an Alternative Investigation**: Instead of performing a standard dilution series, design a data-card investigation to test how different environmental conditions (temperature, pH, salt concentration) affect bacterial growth rates. What hypothesis would you test? Which printed curve or plate-image evidence would measure growth?

6. **Hypothesis**: Predict how increasing salt concentration would affect the growth of *E. coli*. Would you expect a linear decrease in growth rate, or a threshold effect? Why?

### Part 4: AMR Network and Fungal Triage Cards {.unnumbered}

7. Build an AMR transfer map from the provided cards. For each arrow, label whether it represents selection, horizontal gene transfer, environmental persistence, or surveillance.
8. Use the *Candida auris* card to decide whether the scenario calls for treatment, infection-control action, both, or neither. Justify your answer using colonization status, clinical infection evidence, identification method, and susceptibility data.
9. Compare the bacterial AMR map with the fungal triage card. Identify one shared One Health principle and one difference between bacterial resistance-gene transfer and healthcare-associated fungal persistence.

## Data Recording {.unnumbered}

: Sample data for Part 4: AMR Network and Fungal Triage Cards. {#tbl:unit_VII_bacteria_archaea_viruses_part_4_amr_network_and_fungal_triage_cards}
| Species | Gram stain result | Cell shape | Cell arrangement |
| ------- | ----------------- | ---------- | ---------------- |
| *E. coli* | | | |
| *Bacillus sp.* | | | |

: Part 4: AMR Network and Fungal Triage Cards: Dilution and Colonies counted. {#tbl:unit_VII_bacteria_archaea_viruses_part_4_amr_network_and_fungal_triage_cards_2}
| Dilution | Colonies counted | CFU/mL |
| -------- | ---------------- | ------- |
| 10⁻⁴ | | |
| 10⁻⁵ | | |
| 10⁻⁶ | | |

Best estimate of original concentration: _______ CFU/mL
Blinded duplicate agreement: _______%; plate images excluded, with reason: _______
AMR transfer pathway most supported: _______; *Candida auris* action selected: _______; surveillance evidence needed: _______

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Measure growth and compare microbial life strategies.
- **Data skill to practice:** Interpret microbial observations from growth, sequence, or structural evidence.
- **BioSkills emphasis:** Science and society, Process of science, Modeling and simulation.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Bacteria, Archaea, and Viruses** with a reproducibility pass:

: Part 4: AMR Network and Fungal Triage Cards: Evidence check and Student action. {#tbl:unit_VII_bacteria_archaea_viruses_part_4_amr_network_and_fungal_triage_cards_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab, treat each microbe as an evidence claim built from a Gram-stain phenotype, a colony or plaque count, and a wall-structure or phage-genetics inference, and state for every conclusion whether it rests on a cultured isolate or on a sequence/diagram on paper. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Exponential growth of an E. coli culture {.unnumbered}

**Problem:** A flask of *E. coli* starts at N₀ = 10⁵ cells/mL with a doubling time of t_d = 20 min. Using N = N₀ × 2^(t/t_d), estimate the cell density after t = 2 h, the number of doublings, and the final density in scientific notation.

**Solution:** First, convert time to a consistent unit: t = 2 h = 120 min. The number of doublings is t / t_d = 120 / 20 = 6. Apply the formula: N = 10⁵ × 2⁶ = 10⁵ × 64 = 6.4 × 10⁶ cells/mL. Six doublings multiply the population by 64, producing a final density of about 6.4 × 10⁶ cells/mL.

**Interpretation:** This estimate presumes exponential growth with nutrients and space not limiting; in a closed flask the culture tends to enter stationary phase before the simple model holds for many more doublings. A typical mid-log *E. coli* culture saturates near 10⁹ cells/mL, so the 6.4 × 10⁶ value is consistent with early-to-mid log phase rather than late-stationary phase.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Bacteria, Archaea, and Viruses before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. Why does *E. coli* stain Gram-negative? Describe the structural difference between the cell walls of Gram-positive and Gram-negative bacteria, and explain why ethanol decolourises Gram-negative but not Gram-positive cells.

2. Calculate the CFU/mL from your best printed plate count. Assuming exponential growth at a doubling time of 20 minutes, estimate how many cells would be present after 4 hours if starting from 100 CFU/mL.

3. Penicillin inhibits transpeptidase (cross-links peptidoglycan). Based on cell wall structure, predict whether penicillin is more effective against *E. coli* or *Bacillus subtilis*, and why Gram-negative bacteria often require higher doses.

4. A bacteriophage follows a lysogenic cycle for 200 generations, then enters the lytic cycle. What molecular signal might trigger the switch from lysogeny to lysis? Name the specific protease involved and the CI repressor it degrades.

5. SARS-CoV-2 is a single-stranded, positive-sense RNA virus with an envelope. Compare its replication cycle to a lytic bacteriophage: identify two key differences in where replication occurs, the host enzyme used, and the method of exiting the host cell.
6. A carbapenemase gene appears in related *Klebsiella* isolates on two hospital wards and in a wastewater sample. Use plasmid, integron, and clonal-spread evidence to decide what additional data would distinguish horizontal transfer from one expanding clone.

## Extension Analysis Questions {.unnumbered}

7. **Statistical Analysis**: If the dataset includes three replicate plate images, how would you analyze the variation in CFU/mL estimates? What statistical test would you use to determine if differences between species are significant?

8. **Experimental Error Analysis**: What are three potential sources of error in bacterial colony counting from images? How could you modify the scoring rules or image set to reduce each source of error?

9. **Experimental Design**: If you wanted to test the effectiveness of different antibiotics on bacterial growth without culturing, how would you design the dataset? What controls would you include? How would you measure the effect from growth curves, MIC tables, or inhibition-zone images?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Study of Antibiotic Resistance Evolution**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How does sub-lethal antibiotic concentration affect the rate of resistance evolution in bacteria?
- Formulate a hypothesis about the relationship between antibiotic concentration and resistance development
- Design a simulation using provided *E. coli* growth curves and different antibiotic concentrations

**Session 2**: Data Collection and Analysis
- Analyze printed growth curves collected under antibiotic gradients
- Measure resistance levels from minimum inhibitory concentration tables
- Analyze allele-frequency changes using provided PCR or sequencing summaries

**Session 3**: Data Interpretation and Presentation
- Compare resistance evolution across different antibiotic concentrations
- Calculate selection coefficients for resistant vs sensitive bacteria
- Create a scientific poster or presentation

## Real-World Problem Solving: Microbial Ethics {.unnumbered}

**Case Study: Antibiotic Use in Agriculture**

1. **Research Task**: Investigate the use of antibiotics as growth promoters in livestock. What percentage of antibiotics sold in the US are used for this purpose? What are the most common antibiotics used?

2. **Ethical Consideration**: Should the routine use of antibiotics for growth promotion in agriculture be banned? What are the potential economic impacts on farmers vs the public health benefits?

3. **Policy Proposal**: Design a policy to reduce antibiotic use in agriculture while ensuring animal health and farmer livelihoods. Consider: alternatives to antibiotics, monitoring systems, and transition assistance for farmers.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Antibiotics such as penicillin and vancomycin act on peptidoglycan biosynthesis, and they tend to be well tolerated by humans even at therapeutic doses.
>
> (a) Explain why a drug class that disrupts peptidoglycan cross-linking is selectively toxic to bacteria relative to eukaryotic cells, with reference to the structural component the drug targets and where it is found.
> (b) *Mycoplasma* species lack a cell wall altogether. Predict whether a peptidoglycan-targeting antibiotic would be effective against *Mycoplasma* and propose an antibiotic class likely to be more useful, justifying your choice by referencing a target the bacterium does still possess (for example, a ribosomal subunit or a nucleic-acid enzyme).

## Safety and Ethics Notes {.unnumbered}

Default lab work uses printed image cards, growth curves, and decision matrices primarily. No cultures, plates, antibiotic discs, or environmental samples are required. Optional wet microbiology demonstrations must use approved BSL-1 organisms under instructor supervision and local disposal rules. When discussing antibiotic resistance, emphasize following current prescriber instructions, avoiding unnecessary antibiotic starts, using diagnostics when available, and protecting access to effective treatment.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarizing the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_VII_bacteria_archaea_viruses} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VII_bacteria_archaea_viruses} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/microbiology/microbiology.py` for bacterial growth calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
