# Lab — Gene Expression {#sec:lab_unit_IV_gene_expression .unnumbered}


## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_IV_gene_expression} of the textbook — review that chapter before attempting the exercises below.*

- Transcribe and translate a provided DNA template sequence manually to produce an amino acid sequence
- Identify the effect of point mutations (silent, missense, nonsense) on the final protein
- Analyze a polysome electron micrograph to determine relative transcription and translation rates
- Interpret a Northern blot and a Western blot to determine gene expression changes


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Gene Expression.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Describe what a promoter is at the DNA-sequence level for a typical eukaryotic gene, and explain how a sequence-specific transcription factor recognizes its target promoter or enhancer through protein-DNA contacts. Why does mutation of a single base in a binding site sometimes abolish recognition while a base change elsewhere has little effect?
2. Distinguish transcriptional regulation from post-transcriptional regulation. Give one concrete molecular example of each, and explain which step of the DNA → mRNA → protein flow each example acts on.
3. Predict the effect on steady-state mRNA level if (a) the transcription initiation rate doubles while mRNA degradation stays constant, and (b) the transcription rate stays constant while the mRNA half-life is cut in half. Justify each prediction quantitatively before doing any arithmetic.

## Lab Context: Gene Expression {.unnumbered}

Gene expression flows from DNA → mRNA (transcription, in the nucleus) → protein (translation, by ribosomes in the cytoplasm). The genetic code is triplet (3 nucleotides = 1 codon), non-overlapping, comprehensive, and degenerate (multiple codons = one amino acid). A **polysome** (polyribosome) consists of multiple ribosomes simultaneously translating the same mRNA; the number of ribosomes per mRNA is proportional to protein production demand and mRNA length.

In this lab you will perform manual transcription/translation using codon tables, predict the effect of mutations, and interpret blot data to determine whether gene expression changes are occurring at the transcriptional or translational level.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_IV_gene_expression_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Gene Expression: genomics/database source card: reference release, sample coverage, version, clinical boundary, and refresh trigger | 1 |
| DNA template sequence cards (instructor-provided: 3 sequences — original, missense mutant, nonsense mutant) | 1 set |
| mRNA codon table (standard genetic code) | 1 per student |
| Polysome TEM image (printed) | 1 |
| Northern blot image (printed, 2 lanes: untreated vs treated sample) | 1 |
| Western blot image (printed, 2 lanes: untreated vs treated sample) | 1 |
| Ruler | 1 |
| Colored pens | 3 |

## Paper-Based Investigation {.unnumbered}

**Part A — Transcription and Translation Simulation**

1. Using Cards A (original), B (missense), C (nonsense): Transcribe each DNA template to mRNA (3'→5' template → 5'→3' mRNA), then translate using the codon table to produce an amino acid sequence.
2. For Cards B and C, identify: which codon was changed, what type of mutation (silent/missense/nonsense/frameshift), and what effect on the final protein.

**Part B — Polysome Analysis**

3. Examine the polysome TEM image. Count the number of ribosomes on the longest visible mRNA strand. Measure the approximate length of the mRNA strand (mm). Calculate ribosome density (ribosomes per mm of mRNA).

**Part C — Blot Interpretation**

4. The Northern blot shows mRNA levels (bands). The Western blot shows protein levels (bands). Compare band intensities between untreated (lane 1) and treated (lane 2) samples. Complete the interpretation table.

## Data Recording {.unnumbered}

: Alignment and Rubric Map: Card and Mutation type. {#tbl:unit_IV_gene_expression_alignment_and_rubric_map_2}
| Card | Mutation type | Mutated codon | Amino acid change | Effect on protein |
| ---- | ------------- | ------------- | ----------------- | ----------------- |
| A | — | — | — | Normal |
| B | | | | |
| C | | | | |

mRNA length: ________ mm; Ribosomes counted: ________; Ribosome density: ________ per mm

: Alignment and Rubric Map. {#tbl:unit_IV_gene_expression_alignment_and_rubric_map_3}
| Sample | Northern band (strong/weak/absent) | Western band | Interpretation |
| ------ | ----------------------------------- | ------------ | -------------- |
| Untreated | | | |
| Treated | | | |

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Trace expression from DNA template to protein or regulatory RNA.
- **Data skill to practice:** Convert DNA/RNA sequence data into predicted molecular products.
- **BioSkills emphasis:** Process of science, Science and society, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Gene Expression** with a reproducibility pass:

: Alignment and Rubric Map: Evidence check and Student action. {#tbl:unit_IV_gene_expression_alignment_and_rubric_map_4}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: When reading transcription, splicing, or translation datasets, keep the regulatory steps separate and ask which step the evidence actually measures, since mRNA level, isoform choice, and protein output can move independently. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Steady-State mRNA Levels Under Promoter Repression {.unnumbered}

**Problem:** A gene has a 1,200-nucleotide coding sequence and is transcribed at a basal rate of 3 mRNAs per minute. The mRNA is degraded with rate constant k = 0.08 per minute. Treat transcription as zero-order and degradation as first-order, so at steady state mRNA level equals transcription rate divided by k. Calculate the steady-state mRNA count in the basal state. Then calculate the new steady state if a repressor reduces transcription to 0.5 mRNAs per minute, and report the fold change in mRNA level.

**Solution:**

- Basal steady state = 3 mRNAs min⁻¹ ÷ 0.08 min⁻¹ = 37.5 mRNAs per cell, which we report as about 38 transcripts per cell.
- Repressed steady state = 0.5 mRNAs min⁻¹ ÷ 0.08 min⁻¹ = 6.25 mRNAs per cell, about 6 transcripts per cell.
- Fold change = 37.5 ÷ 6.25 = 6.0, so the repressor produces a six-fold drop in steady-state mRNA, which matches the six-fold drop in transcription rate because degradation kinetics did not change.

**Interpretation:** When the mRNA degradation rate constant is unchanged, fold-change in transcription rate is propagated one-to-one into fold-change in steady-state mRNA level. The half-life of the mRNA (ln 2 ÷ 0.08 ≈ 8.7 minutes) sets how quickly the system reaches its new steady state after the perturbation; a longer half-life would slow the response without changing the final ratio.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Gene Expression before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. Card B (missense mutation): the amino acid sequence changed but the protein was still functional. Explain how this is possible using the concept of functionally conservative amino acid substitutions (e.g., Leu → Ile).
2. Card C introduced a premature stop codon. How does the cell detect and degrade mRNAs with premature stop codons? Name this quality-control pathway.
3. If Northern blot shows no change in mRNA level, but Western blot shows dramatically reduced protein, at what level is gene expression being regulated? Name two possible regulatory mechanisms.
4. A gene has 8 ribosomes per mRNA; a second gene's mRNA has 40 ribosomes present. Which gene is being translated more actively? What are two reasons a cell might load one mRNA with more ribosomes than another?
5. The antibiotic streptomycin causes misreading of the A-site codon by destabilising the decoding center of the 30S ribosomal subunit. Predict the effect on translation fidelity and which kingdom of organisms would be most affected (hint: consider that streptomycin targets 30S vs 60S subunits).


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** The *Drosophila* gene *Dscam* encodes a cell-surface receptor required for axon guidance. Its pre-mRNA contains four blocks of mutually exclusive alternative exons (12, 48, 33, and 2 variants for the four exon blocks, respectively), yielding a theoretical upper bound of 12 × 48 × 33 × 2 ≈ 38,000 distinct mRNA isoforms from one locus. Evaluate the regulatory and evolutionary implications of producing this many protein variants from a single gene.
>
> (a) Calculate the theoretical isoform count from the given exon-block sizes, then compare it to the number of distinct proteins you would need to encode this diversity if each isoform required its own gene. Discuss what alternative splicing buys the genome in terms of coding capacity per kilobase.
> (b) Propose a molecular mechanism that could bias which Dscam isoform a given neuron expresses (consider splicing factors, RNA secondary structure, or stochastic exon choice), and outline one experiment that would test whether isoform choice is regulated or random in a defined neuronal population.

## Safety and Ethics Notes {.unnumbered}

No chemical hazards in this simulation/analysis lab. Handle TEM prints with care. If using online databases for real sequence data, comply with institutional access agreements.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group
comparing results and discussing the following prompts. Each member should
contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to
   the textbook's predictions. Where they diverge, suggest at least one
   mechanistic explanation before concluding "experimental error."
2. **What would change the outcome** — propose one modification to the
   procedure that would sharpen the measurement or extend the result to a
   new biological context, and predict what you would observe.
3. **One-sentence headline** — each student composes a single sentence
   summarizing the lab's take-home message, suitable for a tweet. Compare
   sentences across groups; good headlines are short, quantitative, and
   mechanistic.
4. **Connection back to the textbook** — identify one section of
   \cref{sec:unit_IV_gene_expression} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_IV_gene_expression} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_IV_gene_expression}`; all numerical
quantities in this lab use SI units — see \nameref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
