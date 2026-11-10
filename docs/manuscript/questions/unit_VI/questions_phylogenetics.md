# Questions — Phylogenetics and the Tree of Life {#sec:q_unit_VI_phylogenetics .unnumbered}


## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Use a tree to infer shared ancestry, character transitions, or divergence time.
- **Model/data emphasis:** Tree-distance, parsimony, and molecular-clock calculations.
- **Assessment alignment:** Visual Representations, Statistical Tests and Data Analysis, Argumentation.
- **Misconception probe:** Living species are cousins, not ancestors of one another.
- **Transfer product:** Transfer tree thinking to pathogens, conservation units, gene families, and development.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.

## Questions 1–10 {.unnumbered}

*This activity accompanies \cref{sec:unit_VI_phylogenetics} of the textbook — review that chapter before attempting the exercises below.*

<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
1. What is a phylogenetic tree? What does each node, branch, and tip represent?

<!-- SOLUTION
**Answer (Q1, Recall).** A phylogenetic tree depicts evolutionary relationships: tips (terminal taxa) are sampled species/sequences, internal nodes are inferred common ancestors (speciation/divergence events), and branches represent lineages through time (length may encode time or amount of change). See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
2. What is a clade (monophyletic group)? Distinguish monophyletic, paraphyletic, and polyphyletic groups.

<!-- SOLUTION
**Answer (Q2, Recall).** A clade (monophyletic group) is an ancestor and all its descendants. Paraphyletic groups include an ancestor and some but not all descendants (e.g., 'reptiles' excluding birds); polyphyletic groups unite taxa without their common ancestor (grouping by convergence). See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
3. Define synapomorphy. How does it differ from a plesiomorphy?

<!-- SOLUTION
**Answer (Q3, Recall).** A synapomorphy is a shared derived character inherited from the most recent common ancestor of a clade and used to diagnose it. A plesiomorphy is an ancestral character shared more broadly; only synapomorphies (not shared ancestral traits) define clades. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
4. What is parsimony in phylogenetics? What does the most parsimonious tree minimize?

<!-- SOLUTION
**Answer (Q4, Recall).** Parsimony selects the tree requiring the fewest evolutionary changes (character-state transitions) to explain the data, invoking the minimum of independent origins/reversals (homoplasy). See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
5. What is a molecular phylogeny? What type of data is used to construct one?

<!-- SOLUTION
**Answer (Q5, Recall).** A molecular phylogeny infers relationships from molecular sequence data — DNA, RNA, or protein sequences (e.g., rRNA genes, mitochondrial genes, or genome-wide markers) — rather than morphology. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
6. What is a bootstrap value? What does a bootstrap of 90% indicate?

<!-- SOLUTION
**Answer (Q6, Recall).** A bootstrap value is the percentage of pseudo-replicate datasets (resampled sites) that recover a given clade. A bootstrap of 90% means the clade is supported in 90% of replicates — strong but not absolute support for that grouping. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
7. What is an outgroup? How is it used to root a phylogenetic tree?

<!-- SOLUTION
**Answer (Q7, Recall).** An outgroup is a taxon known to lie outside the clade of interest. It polarizes characters and roots the tree: the point where the ingroup attaches to the outgroup is the root, defining ancestral vs derived states. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
8. What is horizontal gene transfer (HGT)? In which domains of life is it most common?

<!-- SOLUTION
**Answer (Q8, Recall).** Horizontal (lateral) gene transfer is the transfer of genetic material between organisms other than parent-to-offspring. It is most common among Bacteria and Archaea (and between them), and can make single-gene trees conflict with the organismal tree. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. Define convergent evolution. How can it mislead phylogenetic analysis?

<!-- SOLUTION
**Answer (Q9, Recall).** Convergent evolution produces similar character states independently in unrelated lineages (homoplasy). It misleads phylogenetics by making distantly related taxa appear closely related if those convergent characters are scored as homologous. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
10. What are molecular clocks? How are they calibrated?

<!-- SOLUTION
**Answer (Q10, Recall).** Molecular clocks use the roughly constant accumulation of substitutions over time to date divergences. They are calibrated with independent evidence — dated fossils at nodes or known biogeographic/geological events — to convert genetic distance into absolute time. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->


## Questions 11–20 {.unnumbered}

<!-- assess: LO=LO3; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
11. In the printed three-taxon character matrix (1=present, 0=absent), use lizard as outgroup and parsimony with independent, equally weighted characters to identify support for birds+crocodiles. Distinguish a character unique to one row from proof of an exclusive evolutionary origin.

| Taxon | Archosaur skull | Feathers | 4-chambered heart | Endothermy |
|-------|----------------|----------|-------------------|------------|
| Lizard | 0 | 0 | 0 | 0 |
| Crocodile | 1 | 0 | 1 | 0 |
| Bird | 1 | 1 | 1 | 1 |

<!-- SOLUTION
**Answer (Q11, Application).** Within this matrix, skull and heart states are shared by bird and crocodile relative to the lizard outgroup, supporting their grouping with fewer changes under the stipulated coding. Feathers and endothermy distinguish the bird row but do not unite bird+crocodile. This three-row exercise neither supplies snake states nor establishes exclusive evolutionary origins of those traits. Award matrix-based inference and the sampling boundary. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
12. Two competing phylogenies are proposed for the Paleocene mammals: (A) requires 12 evolutionary changes; (B) requires 15 changes. By parsimony, which tree is preferred? Explain what assumption is made when choosing the more parsimonious tree.

<!-- SOLUTION
**Answer (Q12, Application).** Tree A requires 12 changes, tree B requires 15; by parsimony tree A is preferred (fewer steps). The assumption is that evolutionary change is relatively rare, so the hypothesis invoking the fewest independent changes (least homoplasy) is the best estimate — an assumption that weakens when rates are high or branches are long. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
13. Dolphins and ichthyosaurs (extinct reptiles) both have streamlined bodies and fin-like forelimbs. Explain: (a) why a morphological phylogeny based solely on body shape would incorrectly group them; (b) what more reliable character would avoid this error; (c) what type of evolution produced the similarity.

<!-- SOLUTION
**Answer (Q13, Application).** (a) Body shape is convergent for aquatic locomotion, so a shape-based tree wrongly groups dolphins with ichthyosaurs. (b) Reliable characters are independent homologies — DNA sequence and skeletal/developmental synapomorphies (mammalian middle-ear ossicles, mammary structures) place dolphins with mammals. (c) The similarity is convergent (analogous) evolution. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
14. Compare the rooted topologies (Bacteria,(Archaea,Eukarya)), with monophyletic Archaea, and (Bacteria,(Archaea1,(Archaea2,Eukarya))). Which actually nests Eukarya within Archaea?

<!-- SOLUTION
**Answer (Q14, Application).** In the first topology, monophyletic Archaea and Eukarya are sisters, compatible with a three-domain branching hypothesis; sisterhood is not nesting. The second places Eukarya within the archaeal radiation, so named Archaea excluding Eukarya are paraphyletic, as in two-domain hypotheses. Root position and sampling matter. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
15. Two hypothetical taxa differ at 80 of 1000 nucleotide sites. Use JC=−.75ln(1−4p/3) and a lineage-summed rate of .02/site/Myr to estimate divergence. Compare a per-lineage rate of .01 and state uncertainty.

<!-- SOLUTION
**Answer (Q15, Application).** p=.08; JC≈.08459, so t≈4.23 Ma, versus 4 Ma uncorrected. Using per-lineage μ=.01 requires t=JC/(2μ), the same result; do not divide by 2 again when using the lineage-summed rate. Calibration, rate variation, alignment error and ancestral coalescence remain uncertain; no HPD can be computed from these two inputs. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. ABBA-BABA (D-statistics) tests detect gene flow between populations. If D is significantly positive, what does it imply about the relationships between the four taxa (P1, P2, P3, and outgroup)? How did this test reveal Neanderthal–modern human gene flow?

<!-- SOLUTION
**Answer (Q16, Application).** A significantly positive D (ABBA > BABA) indicates gene flow/admixture between P3 and one of P1/P2 beyond that expected from incomplete lineage sorting under the (((P1,P2),P3),O) topology. Excess shared derived alleles between non-African humans (P2) and Neanderthal (P3) versus African humans (P1) revealed Neanderthal–modern-human introgression. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. Biogeographic analysis shows that the freshwater fish genus *Nannoperca* is distributed across southwestern Australia (isolated from other parts by arid zones). How would you distinguish between: (a) vicariance (ancient populations separated by geological changes); (b) long-distance dispersal (a single colonization event across an unsuitable barrier)?

<!-- SOLUTION
**Answer (Q17, Application).** Distinguish by dating divergence relative to barrier age and comparing area cladograms: vicariance predicts divergence times matching the geological/aridification event and concordant patterns across co-distributed taxa; long-distance dispersal predicts divergence younger than the barrier and idiosyncratic, taxon-specific timing inconsistent with a shared vicariant event. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
18. Maximum likelihood (ML) phylogenetics uses an explicit model of sequence evolution (e.g., GTR+Γ) to evaluate the likelihood of observing the data given a tree. Why is ML generally preferred over parsimony for molecular data, especially for distantly related taxa?

<!-- SOLUTION
**Answer (Q18, Synthesis).** ML evaluates trees under an explicit substitution model, allowing multiple substitutions and rate heterogeneity that simple parsimony does not represent. It can reduce long-branch artifacts when the model and sampling are adequate, but it does not know the true process and can be biased by misspecification. Consistency is a conditional model property, not a guarantee for every empirical alignment. Compare model fit, taxon sampling and alternative histories. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. Gene trees vs species trees: individual gene trees can differ from the species tree due to incomplete lineage sorting (ILS) or horizontal gene transfer. What is ILS, and why is it more likely for genes with short internodal branches (rapid speciation)?

<!-- SOLUTION
**Answer (Q19, Application).** Incomplete lineage sorting is the persistence of ancestral polymorphism through successive speciation events, so a gene's coalescence predates speciation and its tree differs from the species tree. It is likelier with short internodal branches (rapid successive speciation) because there is little time for lineages to coalesce/sort between divergence events. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. The "long branch attraction" (LBA) artifact occurs when rapidly evolving lineages with many changes falsely cluster together in parsimony or distance analysis. Explain the mechanism of LBA and propose two strategies to avoid it (taxon sampling, model-based methods).

<!-- SOLUTION
**Answer (Q20, Application).** Long-branch attraction: rapidly evolving (long) branches accumulate many independent changes, some matching by chance (homoplasy), which parsimony/distance methods misread as shared ancestry, clustering the long branches together regardless of true relationships. Mitigate by adding taxa to break long branches and by using model-based (ML/Bayesian) methods that correct for multiple substitutions. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->


## Questions 21–30 {.unnumbered}

<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
21. Evaluate Asgard-related archaeal ancestry of the eukaryotic host using three distinct evidence types: genomic protein-family assignments, phylogenomic topology and experiments on selected proteins or cultured cells. Which conclusions do they support, and which claims about endomembranes, ancestral timing or engulfment require additional evidence? Explain how sampling, markers and models affect fine placement.

<!-- SOLUTION
**Answer (Q21, Synthesis).** Genomic actin/actin-regulator, ubiquitin/ESCRT and other homologs support related cellular components, not the presence of eukaryotic organelles in every Asgard cell. Phylogenomic studies strongly support Asgard-related archaeal host ancestry; corrected 2023 and 2025 analyses differ in the closest sampled branch, so marker/paralogy controls, taxon sampling and evolutionary models remain relevant. Experiments add different evidence: selected purified proteins have tested activities, and an actin-associated cytoskeleton and defined protrusion/motility behaviors have been observed in particular Asgard cultures. Those results do not directly observe a pre-mitochondrial ancestor, establish an identical complete endomembrane system or demonstrate historical engulfment. Mitochondrial bacterial ancestry is a separate contribution. Credit an answer that distinguishes these evidence types and proposes tests of alternatives such as horizontal transfer, gene loss or incomplete assemblies; do not require the student to assert that all eukaryotic cellular machinery was already present. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
22. Design a phylogenomic study (using hundreds of genes rather than one marker) to resolve a "soft polytomy" (unresolved node) in the avian tree of life. Describe: coalescent methods (ASTRAL) vs concatenation (ML on combined alignment), what sources of conflict between gene trees need to be accounted for, and how you would determine whether the polytomy reflects rapid radiation rather than incomplete data.

<!-- SOLUTION
**Answer (Q22, Synthesis).** Sample many independent loci and taxa; compare concatenation with multispecies-coalescent inference, quantify gene-tree estimation error, ILS and introgression, and test short but nonzero internodes against a hard polytomy. Rapid radiation can produce ILS, so these are not exclusive explanations. Roughly balanced alternative gene trees and unresolved support are not proof of simultaneous divergence. Credit explicit models, uncertainty and a comparison using increased data or sampling. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
23. Explain why homologous small-subunit rRNA was useful for comparing cellular lineages: conserved and variable regions, broad distribution and functional constraints. Why is it not a universal marker for viruses, and what limits its interpretation as a species tree?

<!-- SOLUTION
**Answer (Q23, Synthesis).** Homologous small-subunit rRNAs occur across cellular lineages and combine conserved regions with variable regions useful at different phylogenetic depths. Viruses do not share one universal rRNA marker. Transfer, divergent/paralogous copies, primer coverage, compositional biases, rate variation and saturation can mislead inference, so neither broad conservation nor a single rRNA tree guarantees a true species tree. Award cellular scope, marker utility and limitations. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
24. Bayesian phylogenetics (MrBayes, BEAST) uses prior probabilities and MCMC sampling to estimate the posterior distribution of trees. Compare Bayesian vs maximum likelihood approaches: (a) what is the difference in interpretation of the "support" values (posterior probabilities vs bootstrap); (b) when does Bayesian inference provide overconfident node support; (c) how is divergence time estimation performed in BEAST?

<!-- SOLUTION
**Answer (Q24, Synthesis).** (a) Bayesian support is a posterior probability (probability the clade is true given data and priors); bootstrap is a frequentist resampling proportion. (b) Bayesian PP can be overconfident under model misspecification or with very short internal branches. (c) BEAST estimates divergence times by combining a clock model, tree prior, and fossil/biogeographic calibration priors via MCMC to sample dated trees. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Compare long-read sequencing of intact polyploid genomes with ancient DNA made of short damaged fragments. What problems can improved read length solve, and which require separate evidence controls?

<!-- SOLUTION
**Answer (Q25, Synthesis).** Long molecules can bridge repeats, phase haplotypes and help distinguish subgenomes or paralogs, improving orthology inference. A sequencing platform cannot restore ancient molecules fragmented before extraction; damage, contamination and reference bias need blanks, independent libraries, molecular-damage analysis and appropriate treatment/validation. Better assembly also does not remove substitution-model or taxon-sampling uncertainty at deep nodes. Credit the distinction between molecule availability, assembly and phylogenetic inference. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Why can microbial gene trees form a network even when many core genes retain a vertical backbone? Can one fraction of HGT be assigned to every genome?

<!-- SOLUTION
**Answer (Q26, Synthesis).** Genes differ in transfer opportunity, selection and detectability; different markers can have different histories. Infer a vertical backbone using multiple conserved loci and compare gene content, synteny and gene-tree conflict for evidence of HGT. A universal transferred fraction or level where all vertical history fails is not supported; the dataset, method and timescale must be specified. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. Transposable elements have been used as phylogenetic markers (SINEs/LINEs as candidate synapomorphies). Evaluate the inference that a shared insertion originated in a common ancestor, considering: (a) persistence of insertions; (b) independence from nucleotide-substitution models; (c) limitations such as element excision, parallel insertions at hotspots and incomplete lineage sorting.

<!-- SOLUTION
**Answer (Q27, Synthesis).** (a) Transposon (SINE/LINE) insertions are effectively irreversible, so a shared insertion is a near-unambiguous synapomorphy. (b) Presence/absence does not depend on substitution-model assumptions. (c) Limitations: rare precise excision and parallel insertions into hotspots, and incomplete lineage sorting of polymorphic insertions, can still create homoplasy, so multiple independent insertions are used. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
28. The "total evidence dating" approach (tip calibration) uses morphological characters from fossils as direct terminal taxa (not just calibration points) in Bayesian time-tree analysis. Evaluate the advantages of total evidence dating over node calibration, and describe what happens to morphological branch length estimates when the model of trait evolution (e.g., Mk model) is misspecified.

<!-- SOLUTION
**Answer (Q28, Synthesis).** Total-evidence (tip) dating places fossils as dated terminal taxa with morphological characters, jointly estimating topology and timescale and using the fossilised-birth–death process, which propagates uncertainty better than fixing node ages. If the morphological model (e.g., Mk) is misspecified, morphological branch lengths and hence inferred rates and divergence times are biased, distorting the time tree. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
29. Horizontal gene transfer in cancer (somatic HGT from tumor microenvironment bacteria into human cells) has been reported but remains controversial. Evaluate the evidence: (a) what sequencing artifacts can mimic bacterial HGT; (b) what controls are needed to rule out contamination; (c) if real, what functional consequences might cancer-incorporated bacterial genes have?

<!-- SOLUTION
**Answer (Q29, Synthesis).** (a) Bacterial reads can arise from index-hopping, reference contamination, or chimeric assembly mimicking HGT. (b) Needed controls: matched blanks, multiple independent libraries, paired-end reads spanning human–bacterial junctions, and orthogonal validation (PCR/FISH). (c) If real, integrated bacterial genes could alter host gene expression or metabolism in tumor cells, but the bar for evidence is high given pervasive artifact risk. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
30. Critically assess whether a "tree of life" can be reconstructed from extant biodiversity alone, without fossil calibration. What information is intrinsically lost when primarily the tips (extant species) and not the internal nodes (extinct ancestors) are known? Use the concept of incomplete ancestry and the "big-bang" topology problem of rapid early diversification as a specific example.

<!-- SOLUTION
**Answer (Q30, Synthesis).** From extant tips alone, extinct lineages and ancestral states are unobserved, so deep relationships, ancestral character reconstruction, and absolute timing are weakly identified. Rapid early diversification gives near-simultaneous splits ('big-bang' topology) with little informative signal on short internal branches, so without fossil calibration both branching order and timescale of the deep tree remain poorly resolved. See \cref{sec:unit_VI_phylogenetics}.
SOLUTION -->
