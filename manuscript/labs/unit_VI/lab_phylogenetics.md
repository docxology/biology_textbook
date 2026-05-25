# Lab — Phylogenetics and the Tree of Life {.unnumbered}

\label{sec:lab_unit_VI_phylogenetics}

## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_VI_phylogenetics} of the textbook — review that chapter before attempting the exercises below.*

- Construct a cladogram from a morphological character matrix using parsimony
- Interpret a molecular phylogeny to determine divergence times and evolutionary relationships
- Identify synapomorphies and plesiomorphies from a character matrix
- Evaluate conflicting phylogenetic hypotheses using bootstrap support values


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Phylogenetics and the Tree of Life.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define a synapomorphy and explain why shared derived characters, rather than shared ancestral characters (symplesiomorphies), are used to recover phylogenetic relationships. Provide a concrete example, such as the amniotic egg uniting reptiles, birds, and mammals, and describe how the same character can be a synapomorphy at one level of the tree and a symplesiomorphy at a deeper level.
2. Describe what bootstrap support represents in a maximum-likelihood or parsimony phylogeny. Explain how the sites of a sequence alignment are resampled with replacement to build pseudo-replicate trees, and how a bootstrap value (for example, 95) on a branch is interpreted as the fraction of pseudo-replicates that recovered that clade.
3. Distinguish parsimony, maximum likelihood, and Bayesian inference as tree-building criteria. State the optimality criterion or objective function used by each, and identify one strength and one limitation per method (for example, parsimony is conceptually simple but susceptible to long-branch attraction).

## Lab Context: Phylogenetics and the Tree of Life {.unnumbered}

Phylogenetics reconstructs evolutionary history by identifying shared derived characters (**synapomorphies**) that define clades. Maximum parsimony selects the tree requiring the fewest evolutionary changes. Molecular phylogenies use DNA/protein sequence differences, calibrated with fossil dates, to construct ultrametric trees with branch lengths proportional to substitution rate or time. Bootstrap values (percentage of resampled datasets recovering the same clade) indicate support for individual nodes.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Source-governance card for Phylogenetics and the Tree of Life: evolutionary-evidence source card: alternative hypotheses, sampling, calibration, and confidence boundary | 1 |
| Character matrix (12 taxa × 10 morphological characters; 0=absent, 1=present) | 1 printed |
| Molecular phylogeny printout (5 taxa; with branch lengths and bootstrap values) | 1 |
| Cladogram construction guide | 1 |
| Scissors; paste; paper | 1 set |
| Calculator | 1 |

## Paper-Based Investigation {.unnumbered}

**Part A — Manual Cladogram Construction**

1. Using the character matrix, identify which characters are shared among subsets of taxa (synapomorphies) vs ancestral (plesiomorphies shared by outgroup).
2. Use the principle of parsimony to construct the most parsimonious cladogram for 6 selected taxa (the other 6 are "outgroups" — use to root the tree).
3. Count the total number of character-state changes on your tree vs an alternative arrangement. Identify which tree requires fewer changes (most parsimonious).

**Part B — Molecular Phylogeny Interpretation**

4. On the provided molecular phylogeny: identify (a) the most recent common ancestor of taxa A and B; (b) which taxon diverged first from the others; (c) any polytomies (unresolved nodes); (d) the clade with the highest bootstrap support.

## Data Recording {.unnumbered}

Character matrix (excerpt — 5 taxa):

| Taxon | Vertebrae | Four limbs | Feathers | Mammary glands | Placenta |
| ----- | --------- | ---------- | -------- | -------------- | -------- |
| Lamprey | 1 | 0 | 0 | 0 | 0 |
| Salamander | 1 | 1 | 0 | 0 | 0 |
| Crocodile | 1 | 1 | 0 | 0 | 0 |
| Robin | 1 | 1 | 1 | 0 | 0 |
| Human | 1 | 1 | 0 | 1 | 1 |

Your cladogram sketch:

Most parsimonious tree — total changes: ___
Alternative tree — total changes: ___

Molecular phylogeny notes:
- Taxon diverging first: ___
- Highest bootstrap node: ___ (___% support)
- Any polytomies? ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Infer relationships from character or sequence evidence.
- **Data skill to practice:** Read trees correctly and map traits or sequences onto branches.
- **BioSkills emphasis:** Modeling and simulation, Quantitative reasoning, Communication and collaboration.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Phylogenetics and the Tree of Life** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this character-matrix and tree-building lab, justify each clade with a shared derived character (synapomorphy) rather than overall similarity, treat bootstrap percentages as resampling support rather than proof, and flag where horizontal gene transfer or hybridisation would make a strictly bifurcating tree the wrong model. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: UPGMA Tree from a Pairwise Distance Matrix {.unnumbered}

**Problem:** Three species A, B, and C share a common ancestor. The pairwise distances are d(A, B) = 0.05, d(A, C) = 0.12, and d(B, C) = 0.10. Using the UPGMA algorithm, infer the tree topology, calculate node depths, draw the tree with branch lengths, and convert the depths to divergence times assuming a molecular clock of 2 percent per million years.

**Solution:** UPGMA joins the two closest lineages first. The smallest distance is d(A, B) = 0.05, so A and B cluster first. The node AB lies at depth d(A, B) / 2 = 0.025 (each tip is 0.025 from the node). The new distance from the AB cluster to C is the average of the original distances from C to each member: d(AB, C) = (d(A, C) + d(B, C)) / 2 = (0.12 + 0.10) / 2 = 0.11. The node ABC then lies at depth d(AB, C) / 2 = 0.055. The branch length from the AB node up to the ABC node is 0.055 − 0.025 = 0.030, and the branch from C up to the ABC node is 0.055. Converting depths to divergence times with a clock of 2 percent per million years (i.e., 0.02 substitutions per site per million years), the A–B split occurred at 0.025 / 0.02 = 1.25 million years ago, and the AB–C split occurred at 0.055 / 0.02 = 2.75 million years ago.

**Interpretation:** UPGMA produces an ultrametric tree, in which every tip is equidistant from the root — an assumption equivalent to a strict molecular clock across lineages. The estimated split times here depend on that assumption; if the clock varies among lineages, neighbor-joining or a relaxed-clock model in a Bayesian framework would be more appropriate. The distances in this example are also small enough that no multiple-hit correction is applied; for larger distances, a Jukes-Cantor or more parameter-rich substitution model is typically used before tree construction.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Phylogenetics and the Tree of Life before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. In your character matrix, which character (vertebrae, four limbs, feathers, etc.) defines the broadest clade (most inclusive group)? Which is the most restricted synapomorphy (smallest clade)? Explain the concept of nested hierarchy.
2. Crocodiles share a more recent common ancestor with birds than with lizards, despite looking more like lizards. What does this illustrate about the limits of morphological similarity as an indicator of evolutionary relationship?
3. A bootstrap value of 95% means that 95% of resampled datasets recover that node. How would you interpret a node with 42% bootstrap support? Should it be included in the published tree?
4. Horizontal gene transfer (HGT) in bacteria allows genes to jump between unrelated lineages — violating the vertical (parent-to-offspring) assumption of phylogenetics. Explain how HGT would appear as a misleading signal in a molecular phylogeny, and describe one method used to detect it.
5. The "Tree of Life" analogy implies a bifurcating, hierarchical structure. However, hybridisation (interspecies mating, e.g., in plants) produces reticulate evolution — a network rather than a tree. Name two plant genera where reticulate evolution occurs and describe how allopolyploidy contributes to speciation.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A clade of recently diverged species presents a phylogenetic pattern that could either reflect a true adaptive radiation or be an artefact of incomplete lineage sorting (ILS). Evaluate the additional data — morphological, behavioural, and geographic — that would help discriminate between the two scenarios, and explain why ILS is especially problematic in rapidly diversifying groups.
>
> (a) Identify the genomic signature of incomplete lineage sorting: discordance among gene trees across loci, with each gene tree retaining a different sampling of ancestral polymorphism. Describe how a coalescent-based species-tree method (such as ASTRAL) or a tool detecting introgression (such as the D-statistic) can summarize this discordance, and note why ILS is more frequent in clades with short internal branches and large effective population sizes — precisely the regime expected during rapid radiation.
> (b) Describe the morphological, behavioural, and geographic data that would help resolve the ambiguity. Morphological synapomorphies (such as shared adaptive structures) and behavioural traits (such as courtship displays or feeding modes) that consistently track the molecular species tree support a true radiation; mosaic patterns that conflict with the gene-tree majority hint at ILS or introgression. Geographic data — current ranges, fossil localities, paleo-environmental reconstructions — can corroborate plausible isolation events that would have driven divergence.
> (c) Outline a verification plan. Sequence many independent loci from across the genome, build per-locus gene trees, summarize their concordance with a species-tree method, and overlay morphological and biogeographic evidence. Predict that a true radiation will show coherent signal across these data types, while a pattern dominated by ILS will show discordant gene trees with little morphological or geographic alignment. Identify at least one remaining ambiguity — such as ancient introgression between sister lineages — that this plan would not fully resolve and that would require additional approaches (for example, ancestral-state reconstruction or ancient-DNA sampling) to address.

## Safety and Ethics Notes {.unnumbered}

No chemical hazards. When discussing evolutionary relationships involving humans and other primates, maintain scientific respect for most organisms and evolutionary histories.

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
   summarising the lab's take-home message, suitable for a tweet. Compare
   sentences across groups; good headlines are short, quantitative, and
   mechanistic.
4. **Connection back to the textbook** — identify one section of
   \cref{sec:unit_VI_phylogenetics} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VI_phylogenetics} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_VI_phylogenetics}`; all numerical
quantities in this lab use SI units — see \cref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
