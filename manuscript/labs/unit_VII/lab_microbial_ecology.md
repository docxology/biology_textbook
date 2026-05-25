# Lab — Microbial Ecology and the Microbiome {#sec:lab_unit_VII_microbial_ecology .unnumbered}


*This activity accompanies \cref{sec:unit_VII_microbial_ecology} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and evaluate a microbial community analysis using printed culture-independent datasets
- Formulate testable hypotheses about how environmental factors affect microbial diversity
- Identify independent, dependent, and controlled variables in microbial ecology experiments
- Analyze experimental data using diversity indices and network analysis
- Write a brief scientific report with hypothesis, methods, results, and conclusion



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Microbial Ecology and the Microbiome.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Why is the 16S rRNA gene used to identify and classify bacteria rather than a protein-coding gene?
2. Describe nitrogen fixation — what chemical transformation occurs, which type of organisms perform it, and why is this process ecologically important?
3. Define the Shannon diversity index H′ and explain what a higher value indicates about a microbial community.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of microbial ecology, predict which provided community dataset (soil, skin, tap water, or gut) will have the highest microbial diversity. Write a clear, testable hypothesis.

2. **Experimental Design**: What is the independent variable in a microbial diversity study? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: The Shannon diversity index (H') incorporates both richness and evenness. Why is this measure important in microbial ecology? How does it differ from simply counting species?

4. **Quantitative Reasoning**: If a community has three species with relative abundances of 0.5, 0.3, and 0.2, what is its Shannon diversity index? Show your calculation.

5. **Real-World Application**: The human gut microbiome is linked to health and disease. How might antibiotic treatment reduce microbial diversity, and what are the potential health consequences of this reduction?

## Lab Context: Microbial Ecology and the Microbiome {.unnumbered}

The human gut microbiome contains ~3.8 × 10¹³ bacteria from hundreds of species; the ratio of microbial to human cells is approximately 1:1 (revised from earlier overestimates). Culture-based methods recover about 1% of environmental microbes (the "great plate count anomaly"). Metagenomics and 16S rRNA gene sequencing (amplifying the hypervariable V3–V4 region) now allow culture-independent assessment of community composition. The **Shannon diversity index H' = −Σ(p_i × ln p_i)** integrates species richness and evenness.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_VII_microbial_ecology_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Microbial Ecology and the Microbiome: pathogen-surveillance source card: organism-resistance pair, official guidance date, setting, and intervention limit | 1 |
| Printed community case packet (soil, skin, tap water, gut) with metadata cards | 1 |
| Printed colony-image panel from archived BSL-1 teaching plates | 1 |
| Printed 16S rRNA OTU table (two samples: healthy gut vs antibiotic-treated gut — 10 taxa, abundance data) | 1 |
| Calculator | 1 |
| Colored pencils | 3 |
| Interaction network diagram template (printed) | 1 |
| Calculator or optional Python REPL with this project installed | 1 |
| Replicate read-count table and rarefaction checklist | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Community Diversity from Case Packets {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how the provided community datasets will differ in microbial diversity.

2. **Identify Variables**:
   - Independent variable: Community source represented in the case packet
   - Dependent variable: Taxon richness, Shannon diversity index, and network connectance
   - Controlled variables: sequencing depth, primer region, read-quality threshold, rarefaction rule, metadata completeness, and replicate count.

3. **Set Up Controls**: Why is it important to use the same sequencing-depth rule for most samples? What other controls could you include, such as a mock community, a blank extraction control, or a duplicate sample?

4. **Data Collection**:
   - Use the printed OTU table to calculate total reads, relative abundance, richness, Shannon diversity, and evenness for each sample.
   - Use the archived colony-image panel primarily as a comparison for why morphology underestimates molecular diversity.
   - Check whether each sample has enough reads for fair comparison; if not, apply the rarefaction rule provided in the case packet.
   - Compare at least three replicate rows per sample type before drawing conclusions.

### Part 2: Computational Biology Exercise — Diversity Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Calculate diversity from table counts and compare named reference organisms.

```python
from biology.ecology import biodiversity_indices
from biology.microbiology import REFERENCE_ORGANISMS

counts = [42, 18, 15, 9, 6]
diversity = biodiversity_indices(counts)
print("Shannon:", round(diversity.shannon_index, 3))
print("evenness:", round(diversity.evenness, 3))
print("reference domains:", sorted({organism.domain for organism in REFERENCE_ORGANISMS}))
```
### Part 3: Microbial Interaction Network Analysis {.unnumbered}

5. **Design an Alternative Investigation**: Instead of collecting microbiome samples, design a paper-based analysis to test how antibiotic treatment affects microbial interaction networks. What hypothesis would you test? How would you construct the network from co-occurrence or time-series data?

6. **Hypothesis**: Predict how the connectance (number of interactions) in a microbial network would change with reduced diversity. Would you expect more or fewer interactions? Why?

## Data Recording {.unnumbered}

: Part 3: Microbial Interaction Network Analysis: Sample source and Taxon richness. {#tbl:unit_VII_microbial_ecology_part_3_microbial_interaction_network_analysis}
| Sample source | Taxon richness | Shannon H' | Evenness | Read depth |
| ------------- | -------------- | ---------- | -------- | ---------- |
| Soil | | | | |
| Skin | | | | |
| Tap water | | | | |
| Gut | | | | |

: Part 3: Microbial Interaction Network Analysis: Taxon and Healthy sample reads. {#tbl:unit_VII_microbial_ecology_part_3_microbial_interaction_network_analysis_2}
| Taxon | Healthy sample reads | p_i (healthy) | p_i × ln(p_i) | Antibiotic sample reads | p_i (antibiotic) |
| ----- | -------------------- | ------------- | ------------- | ----------------------- | ----------------- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

H' (healthy): ____; H' (antibiotic): ____

Keystone taxon in network: ___; Rationale: ___
Rarefaction or exclusion decision: ___; Reproducibility concern: ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Compare microbial communities and infer interaction hypotheses.
- **Data skill to practice:** Compute or interpret community metrics from abundance data.
- **BioSkills emphasis:** Science and society, Process of science, Modeling and simulation.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Microbial Ecology and the Microbiome** with a reproducibility pass:

: Part 3: Microbial Interaction Network Analysis: Evidence check and Student action. {#tbl:unit_VII_microbial_ecology_part_3_microbial_interaction_network_analysis_13}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab, separate community-composition correlations from mechanistic claims by recording the diversity index or count, the host or environmental context, and the perturbation, and state the experiment that would be needed to move a correlation toward causation. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Shannon Diversity Index for a Microbial Community {.unnumbered}

**Problem:** A soil sample yields four bacterial genera with the following relative abundances: Genus A = 45%, B = 30%, C = 15%, D = 10%. Calculate H′ = −Σ(pᵢ ln pᵢ).

**Solution:** H′ = −[(0.45 × ln 0.45) + (0.30 × ln 0.30) + (0.15 × ln 0.15) + (0.10 × ln 0.10)] = −[(0.45 × −0.799) + (0.30 × −1.204) + (0.15 × −1.897) + (0.10 × −2.303)] = −[−0.360 − 0.361 − 0.285 − 0.230] = 1.236. Maximum possible H′ for 4 equally abundant taxa = ln(4) = 1.386.

**Interpretation:** H′ = 1.236 out of a maximum 1.386, giving evenness J = 1.236/1.386 = 0.892. The community is moderately uneven — dominated by genera A and B — but retains relatively high diversity compared to its species-rich potential.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Microbial Ecology and the Microbiome before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. The soil dataset likely shows higher richness than the skin or tap-water dataset. Why are soils among the most microbially diverse environments on Earth? What physical and chemical habitat heterogeneity drives this?

2. Antibiotic treatment usually reduces H'. What does low H' indicate about community stability? Name one specific clinical consequence of reduced microbiome diversity following broad-spectrum antibiotic use.

3. The "great plate count anomaly" refers to the fact that about 1% of environmental microbes form colonies on standard media. Propose three reasons why the remaining 99% are "unculturable" and describe one molecular technique that can characterize them without culturing.

4. *Akkermansia muciniphila* (a gut commensal) degrades mucin and produces acetate and propionate consumed by other bacteria. If *Akkermansia* is lost, predict the cascade effects on adjacent taxa in your interaction network.

5. A patient receives a faecal microbiota transplant (FMT) to treat recurrent *C. difficile* infection. Using the concept of competitive exclusion and microbiome diversity, explain the mechanism by which FMT suppresses *C. difficile* and describe what the ideal donor microbiome looks like.

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: If the dataset includes three replicate OTU tables per source, how would you analyze the variation in Shannon diversity? What statistical test would you use to determine if differences between sample types are significant?

7. **Experimental Error Analysis**: What are three potential sources of error in microbial diversity measurements? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you wanted to test whether a specific environmental factor (e.g., pH, moisture) affects microbial diversity, how would you design the experiment? What data would you collect? How would you analyze it?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Study of Microbiome and Health**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How does diet affect gut microbiome diversity?
- Formulate a hypothesis about the relationship between fiber intake and microbial diversity
- Design a study plan using dietary data and public microbiome datasets

**Session 2**: Data Collection and Analysis
- Use dietary surveys and public microbiome datasets
- Analyze 16S rRNA sequencing data to calculate diversity indices
- Compare diversity across different diet groups

**Session 3**: Data Interpretation and Presentation
- Correlate diversity with specific dietary components
- Discuss the implications for human health
- Create a scientific poster or presentation

## Real-World Problem Solving: Microbial Ethics {.unnumbered}

**Case Study: Microbiome Biobanks**

1. **Research Task**: Investigate the ethical, legal, and social implications (ELSI) of collecting and storing human microbiome samples. What privacy concerns exist? How is microbiome data different from genetic data?

2. **Ethical Consideration**: Should individuals have property rights over their microbiome? What are the potential benefits and risks of commercialising microbiome-based therapies?

3. **Policy Proposal**: Design a policy for the ethical collection and use of human microbiome samples. Consider: informed consent, data privacy, benefit-sharing, and commercialisation.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A broad-spectrum antibiotic course dramatically reduces gut microbial diversity from H′ ≈ 3.2 to H′ ≈ 0.8.
>
> (a) Predict how reduced microbial diversity would affect short-chain fatty acid (SCFA) production, specifically butyrate, propionate, and acetate, and explain the downstream effects on colonocyte metabolism.
> (b) Evaluate whether the nitrogen-cycling functions of the gut microbiome would be disrupted proportionally to the diversity loss — consider functional redundancy among taxa.
> (c) Propose two ecological principles (from community ecology) that predict how and when microbial community recovery might occur after the antibiotic course ends.

## Safety and Ethics Notes {.unnumbered}

Default lab work uses printed OTU tables, archived colony images, metadata cards, and network diagrams primarily. No environmental sampling, swabbing, agar plates, incubation, or culturing is required. Optional sampling demonstrations must be instructor-supervised and follow local biosafety rules. When discussing microbiome data, respect participant privacy and follow data protection guidelines.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarizing the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_VII_microbial_ecology} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VII_microbial_ecology} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/microbiology/microbiology.py` for microbial ecology calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
