# Questions — Epigenetic Inheritance and Disease {.unnumbered}

\label{sec:q_unit_IV_epigenetic_inheritance_and_disease}

<!-- question-coverage-start -->
## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Explain how 3D organisation or inherited marks alter expression and disease risk.
- **Model/data emphasis:** Chromatin-loop, inheritance, and disease-risk reasoning.
- **Assessment alignment:** Concept Explanation, Questions and Methods, Argumentation.
- **Misconception probe:** A chromatin contact map is not proof of function without perturbation.
- **Transfer product:** Apply inheritance logic to cancer, developmental disorders, and environmental exposure.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.
<!-- question-coverage-end -->

## Questions 1–10: Recall and Comprehension {.unnumbered}

*This activity accompanies \cref{sec:unit_IV_epigenetic_inheritance_and_disease} of the textbook — review that chapter before attempting the exercises below.*

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. The X-inactivation centre (Xic) on the inactive X chromosome produces Xist lncRNA, which coats the inactive X in cis. Explain: (a) how Xist RNA spreads along the chromosome; (b) how it recruits PRC2 (H3K27me3) and PRC1 (H2AK119ub1) to compact the Xi; (c) why a small region (pseudo-autosomal region, PAR) escapes X-inactivation.

<!-- SOLUTION
**Answer (Q1, Application).** (a) Xist is transcribed only from the future inactive X and spreads in cis along that chromosome by exploiting its 3D proximity, nucleating from the X-inactivation centre. (b) Xist recruits SPEN/HDAC3 and Polycomb complexes so PRC2 deposits H3K27me3 and PRC1 deposits H2AK119ub1, with later DNA methylation, compacting the Xi into a heterochromatic Barr body. (c) Genes in the pseudoautosomal region escape inactivation because they have homologous active partners on the Y chromosome, so dosage must be maintained from both sex chromosomes. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. A researcher uses Cas9 fused to a DNMT3A (DNA methyltransferase) domain (dCas9-DNMT3A) to specifically methylate a target promoter. Predict: (a) the epigenetic effect at the target gene; (b) whether the silencing will be maintained through DNA replication (yes, DNMT1 maintenance methyltransferase copies the pattern); (c) how you would verify that methylation, not dCas9 binding alone, is responsible for silencing.

<!-- SOLUTION
**Answer (Q2, Application).** (a) dCas9-DNMT3A targeted to the promoter deposits CpG methylation, repressing the gene by blocking activators and recruiting methyl-readers. (b) Yes — once the symmetric CpG pattern is established, DNMT1 (with UHRF1) recognizes hemimethylated CpGs after replication and restores full methylation, so silencing is heritably maintained through cell division. (c) Verify methylation is causal by using a catalytically dead DNMT3A fusion as a control (binding without methylation should not silence) and by treating with a DNMT inhibitor or bisulfite-sequencing the locus to confirm methylation tracks with silencing. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
3. Transgenerational epigenetic inheritance refers to the transmission of epigenetic marks across generations without DNA sequence change. The agouti mouse model showed that maternal methyl-donor diet changes offspring coat colour and obesity risk via CpG methylation of the Avy allele. What does this imply about the erasure of epigenetic marks between generations (which normally occurs in primordial germ cells)?

<!-- SOLUTION
**Answer (Q3, Application).** If diet-induced methylation of the Avy allele in one generation alters offspring coat colour and metabolism, then the genome-wide epigenetic reprogramming that normally erases methylation in primordial germ cells (and again after fertilization) is incomplete at certain loci. Some sequences — including metastable epialleles and certain repeat/transposon-associated regions like Avy — escape full erasure, allowing parental environmental information to be transmitted, although such transgenerational inheritance is locus-specific and the magnitude of true germline transmission requires careful controls. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
4. Long non-coding RNAs (lncRNAs) number >100,000 in the human transcriptome but most have unknown functions. Evaluate the challenges of studying lncRNA function: (a) conservation is low across species (cannot use model organisms easily); (b) knockdown may affect the genomic region itself (enhancer function of the locus); (c) lncRNAs have complex secondary structure but no ORFs. Propose a systematic approach to determine function.

<!-- SOLUTION
**Answer (Q4, Application).** (a) Because lncRNA sequences evolve rapidly, simple cross-species conservation cannot identify functional ones and model organisms may lack orthologues. (b) Knockdown or deletion can perturb the act of transcription or an underlying enhancer/DNA element rather than the RNA product itself, confounding interpretation. (c) Lacking ORFs and conserved domains, function must be inferred from structure and interactions. A systematic approach: combine RNA-targeting knockdown (ASOs/CRISPRi versus locus deletion controls), rescue with exogenous transcript, map RNA–chromatin/protein interactions (CHART/ChIRP, RAP), and test specific structural motifs by targeted mutation. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
5. Chromatin accessibility (measured by ATAC-seq) is strongly correlated with gene expression. Explain: (a) how nucleosome positioning regulates transcription factor accessibility; (b) the role of pioneer transcription factors (e.g., FOXA1) in opening closed chromatin; (c) how ATAC-seq works mechanistically (Tn5 transposase cuts accessible DNA and adds sequencing adapters).

<!-- SOLUTION
**Answer (Q5, Application).** (a) Nucleosomes occlude DNA, so where they are positioned determines whether transcription-factor binding sites and promoters are accessible; nucleosome-depleted regions correlate with active regulatory elements. (b) Pioneer factors such as FOXA1 can engage their motifs within closed, nucleosomal chromatin and recruit remodellers to open it, licensing other factors to bind. (c) ATAC-seq uses hyperactive Tn5 transposase that preferentially inserts into open chromatin, simultaneously cutting accessible DNA and adding sequencing adapters, so read density reports genome-wide accessibility. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

## Questions 21–30: Synthesis and Evaluation {.unnumbered}

<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
6. Evaluate the claim that cancer is largely an epigenetic disease. Cite evidence from: (a) global hypomethylation and CpG island hypermethylation in cancer; (b) frequent mutations in chromatin remodelling enzymes (ARID1A, SMARCA4, KMT2D) in cancer; (c) the success of HDAC inhibitors and DNMT inhibitors clinically. Under what conditions are purely epigenetic therapies (without targeted mutation correction) appropriate?

<!-- SOLUTION
**Answer (Q6, Synthesis).** (a) Cancers show genome-wide hypomethylation (activating oncogenes/transposons) alongside focal CpG-island hypermethylation that silences tumour suppressors, an epigenetic phenotype. (b) Frequent loss-of-function mutations in chromatin regulators (ARID1A, SMARCA4, KMT2D) show the chromatin machinery is itself a driver. (c) Clinical efficacy of DNMT inhibitors (azacitidine) and HDAC inhibitors supports reversible epigenetic causation. The claim holds where epigenetic silencing is the dominant lesion (e.g., MDS, IDH-mutant gliomas) and a reactivatable gene exists; purely epigenetic therapy is inappropriate when fixed driver mutations or deletions, not silencing, sustain the tumour. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
7. Design a pharmaceutical strategy to reactivate a silenced tumour suppressor gene in a cancer with promoter hypermethylation. Compare DNMT inhibitors (5-azacitidine, broad demethylation), targeted dCas9-TET1 (site-specific demethylation), and HDAC inhibitors. What are the risks of broad epigenome reprogramming vs targeted approaches?

<!-- SOLUTION
**Answer (Q7, Synthesis).** Hypothesis: re-expressing the silenced tumour suppressor restores growth control. Compare arms: a DNMT inhibitor (5-azacitidine) causes broad passive demethylation and reactivates many genes but risks global genome instability and off-target reactivation; dCas9-TET1 demethylates only the targeted promoter, giving specificity but limited efficiency and delivery challenges; HDAC inhibitors broadly reopen chromatin but are nonspecific and transient. Measure target re-expression, methylation, growth arrest, with vehicle and catalytically dead controls; the decision rule is restored expression and arrest specifically when the targeted mark is removed. Broad reprogramming risks awakening oncogenes and toxicity; targeted approaches trade efficiency for safety. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
8. Super-enhancers are clusters of enhancers (~25–50 kb) bound by an unusually high density of transcription factors (BRD4, Mediator), associated with strong transcription of oncogenes (MYC, BCL2) in cancer. Evaluate the evidence for super-enhancer addiction in cancer cells, and explain why BET bromodomain inhibitors (JQ1) preferentially disengage from super-enhancers over typical enhancers.

<!-- SOLUTION
**Answer (Q8, Synthesis).** Super-enhancers are dense clusters of enhancers occupied by high levels of BRD4, Mediator, and master transcription factors that drive very high expression of identity and oncogene loci (MYC, BCL2). Evidence for addiction: cancer cells are disproportionately dependent on these few super-enhancer-driven genes, so disrupting them collapses the oncogenic program. Because super-enhancers depend on cooperative, high-density BRD4/Mediator occupancy and phase-separated condensates, BET inhibitors such as JQ1 disengage BRD4 more steeply from super-enhancers than from typical enhancers — a small drop in occupancy disproportionately collapses the cooperative assembly, preferentially shutting off MYC. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. Evaluate the concept of "epigenetic clock" (Horvath clock): methylation of specific CpG sites in blood DNA correlates with biological age more accurately than chronological age. What do deviations from the epigenetic clock predict? Can lifestyle interventions (caloric restriction, exercise) reduce epigenetic age, and what experimental evidence supports this?

<!-- SOLUTION
**Answer (Q9, Synthesis).** The Horvath epigenetic clock estimates biological age from methylation at a defined set of CpG sites (~353), often more accurately tracking physiological aging than chronological age. Positive deviations (epigenetic age acceleration) predict elevated all-cause mortality and risk of age-related disease, while negative deviations associate with longevity. Some interventions (caloric restriction in animal models, exercise, and small human trials) modestly slow or reverse epigenetic age, but evidence is correlational and confounded by cell-type composition, so randomized longitudinal data with matched cell populations are needed before causal claims. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
10. 3D chromatin organisation (TADs — topologically associating domains) is largely maintained by CTCF and cohesin. Evaluate what would happen to gene regulation if cohesin loading were abolished globally: (a) which enhancer-promoter pairs would become aberrantly activated; (b) what new gene expression states would emerge; (c) is this consistent with the observation that cohesin mutations cause Cornelia de Lange syndrome?

<!-- SOLUTION
**Answer (Q10, Synthesis).** TAD boundaries are built by CTCF and cohesin through loop extrusion. (a) Abolishing cohesin loading would eliminate most loops/TADs, so enhancers could aberrantly contact promoters outside their normal domains, switching on genes that are normally insulated. (b) New, dysregulated expression states would emerge, generally with modest, widespread changes rather than wholesale reprogramming, since promoter-proximal control persists. (c) This is consistent with cohesin/NIPBL mutations causing Cornelia de Lange syndrome, a multisystem developmental disorder, because partial loss of cohesin function subtly mis-wires enhancer–promoter contacts genome-wide during development. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

## Questions 11–20: Application and Analysis {.unnumbered}

<!-- assess: LO=LO4; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
11. CRISPR interference (CRISPRi) uses dCas9-KRAB (a transcriptional repressor) to silences target genes without cutting DNA. Compare CRISPRi with ASO (antisense oligonucleotide) knockdown at the mRNA level and classical promoter deletion by CRISPR. What are the therapeutic advantages of CRISPRi (temporal control, reversibility, no off-target DSBs)?

<!-- SOLUTION
**Answer (Q11, Synthesis).** CRISPRi (dCas9-KRAB) recruits repressive chromatin machinery to a promoter to silence transcription without cutting DNA, acting at the chromatin/transcription level. ASO knockdown acts post-transcriptionally by triggering RNase H degradation of the mRNA, leaving the gene intact and requiring continuous dosing. Classical CRISPR promoter deletion permanently removes DNA via double-strand breaks. CRISPRi's advantages are reversibility and tunable, inducible temporal control, multiplexing, and avoidance of off-target double-strand breaks and permanent genomic scars, making it safer and more flexible for functional and therapeutic silencing. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
12. Maternal nutrition during peri-conception affects offspring health across the life course (Barker/DOHaD hypothesis). Using three specific nutrients (folate, methionine, choline) and their roles in one-carbon metabolism → SAM production → methyltransferase substrate supply, evaluate the molecular mechanism by which poor maternal nutrition could cause persistent epigenetic changes in offspring that increase adult diabetes or cardiovascular disease risk.

<!-- SOLUTION
**Answer (Q12, Synthesis).** Folate, methionine, and choline feed one-carbon metabolism to regenerate S-adenosylmethionine (SAM), the universal methyl donor for DNMTs and histone methyltransferases. Poor maternal supply of these nutrients lowers SAM (and shifts the SAM:SAH ratio), reducing methyltransferase activity during the sensitive peri-conceptional window. This produces altered, persistent DNA-methylation patterns at metabolic gene promoters and imprinted loci in the offspring, which are maintained through development and program tissues toward impaired glucose handling and vascular dysfunction, raising adult diabetes and cardiovascular disease risk (the DOHaD/Barker mechanism). See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
13. Evaluate the concept of "bivalent chromatin domains" in embryonic stem cells: developmental gene promoters carry both active (H3K4me3) and repressive (H3K27me3) marks simultaneously, maintaining them in a "poised" state. How does this enable rapid differentiation in either direction, and what happens to bivalent domains as cells commit to a specific lineage?

<!-- SOLUTION
**Answer (Q13, Synthesis).** Bivalent domains carry the activating H3K4me3 and repressive H3K27me3 marks together at developmental gene promoters in embryonic stem cells, holding genes transcriptionally poised — repressed but primed for rapid activation. On differentiation cues the domain resolves in a lineage-specific way: genes needed in that lineage lose H3K27me3 and become fully active (monovalent H3K4me3), while genes for alternative fates lose H3K4me3 and become stably repressed (monovalent H3K27me3). This allows fast, bidirectional commitment, and once a cell adopts a lineage the bivalent state is resolved into a single stable mark. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
14. Fragile X syndrome is caused by CGG repeat expansion (>200 repeats) in the *FMR1* gene's 5' UTR, leading to hypermethylation and gene silencing. Evaluate the molecular relationship between repeat expansion and hypermethylation: which comes first, what protein (MBNL1/DNMT3A) reads the repeat expansion, and why does the "premutation" (55–200 repeats) have a partially different phenotype (FXTAS) compared to full mutation?

<!-- SOLUTION
**Answer (Q14, Synthesis).** In Fragile X, the CGG repeat expansion comes first: when the FMR1 5' UTR repeat exceeds ~200 (full mutation), the expanded CGG tract is recognized and triggers de novo DNA methylation (via DNMT3A and silencing RNA/heterochromatin pathways) of the FMR1 promoter CpG island, shutting off FMRP. The premutation (55–200 repeats) is not methylated and FMR1 is still transcribed — even overexpressed — so the toxic phenotype (FXTAS, premature ovarian insufficiency) is an RNA gain-of-function from excess CGG-containing mRNA, distinct from the loss-of-function silencing in the full mutation. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
15. Critically evaluate the potential of epigenetic editing as a permanent therapeutic intervention. Specifically: if dCas9-DNMT3A is used to methylate and silence an oncogene, will the silencing persist through cell division (via DNMT1 maintenance methylation), and what are the risks of epigenetic drift or passenger methylation at off-target sites? Propose experimental criteria to determine whether a therapeutic epigenetic edit is "safe and durable."

<!-- SOLUTION
**Answer (Q15, Synthesis).** dCas9-DNMT3A-induced promoter methylation can persist through division because the symmetric CpG mark is copied each S phase by DNMT1/UHRF1 maintenance methylation, so silencing is heritable even after the editor is removed. Risks include epigenetic drift (gradual loss or spreading of methylation), reactivation, and passenger/off-target methylation at unintended loci with their own phenotypic consequences. Criteria for a safe, durable edit: stable target silencing and methylation over many passages and in vivo, genome-wide methylation profiling showing minimal off-target marks, no oncogene reactivation or growth advantage, and reversibility/controllability if adverse effects appear. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. Define epigenetics. Give two examples of epigenetic modifications.

<!-- SOLUTION
**Answer (Q16, Recall).** Epigenetics is the study of heritable changes in gene expression that do not alter the underlying DNA sequence but instead change chromatin state and accessibility. Two examples are DNA methylation of cytosine at CpG dinucleotides (generally repressive at promoters) and covalent histone tail modifications such as acetylation (H3K27ac, activating) or methylation (H3K27me3, repressive). See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. What is DNA methylation? Which nucleotide is typically methylated in mammals, and what effect does methylation at gene promoters generally have on transcription?

<!-- SOLUTION
**Answer (Q17, Recall).** DNA methylation is the covalent addition of a methyl group, catalyzed by DNA methyltransferases (DNMT1 maintenance; DNMT3A/3B de novo). In mammals it occurs almost exclusively on cytosine within 5'-CpG-3' dinucleotides. Methylation of a CpG island in a gene promoter generally represses transcription by blocking activator binding and recruiting methyl-binding repressors and HDACs, producing stable gene silencing. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. What is a histone? Name four types of histone modification and one enzyme family for each.

<!-- SOLUTION
**Answer (Q18, Recall).** A histone is a small basic protein (H2A, H2B, H3, H4) that packages DNA into nucleosomes. Four modification types and an enzyme family for each: acetylation (HATs/KATs add, HDACs remove), methylation (KMTs such as PRC2/EZH2 add, KDMs/demethylases remove), phosphorylation (kinases such as Aurora B), and ubiquitination (E3 ligases such as RING1B on H2AK119). See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. What does H3K4me3 mark indicate? What about H3K27me3?

<!-- SOLUTION
**Answer (Q19, Recall).** H3K4me3 is an activating mark enriched at the promoters of actively transcribed genes, written by MLL/COMPASS and read by basal transcription machinery. H3K27me3 is a repressive mark deposited by Polycomb repressive complex 2 (EZH2) that silences developmental genes and is read by PRC1. Both are lysine methylation on H3, but their distinct positions and reader complexes give opposite functional outcomes. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. What is chromatin remodelling? Name one chromatin remodelling complex.

<!-- SOLUTION
**Answer (Q20, Recall).** Chromatin remodelling is the ATP-dependent repositioning, ejection, or restructuring of nucleosomes to change DNA accessibility for transcription factors and the replication/repair machinery. One example is the SWI/SNF (BAF) complex, which uses ATP hydrolysis to slide or evict nucleosomes; other families include ISWI, CHD/NuRD, and INO80. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

## Questions 21–30: Synthesis and Evaluation {.unnumbered}

<!-- assess: LO=LO7; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
21. What is the lac operon? Which molecules control it?

<!-- SOLUTION
**Answer (Q21, Recall).** The lac operon is a cluster of E. coli genes (lacZ, lacY, lacA) encoding enzymes for lactose uptake and metabolism, transcribed from a single promoter. It is controlled by negative regulation via the LacI repressor (released when allolactose, the inducer, binds it) and positive regulation via CAP–cAMP, which activates transcription when glucose is low. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
22. What is a repressor protein? What is an activator protein?

<!-- SOLUTION
**Answer (Q22, Recall).** A repressor is a regulatory protein that binds DNA (typically an operator or silencer) and decreases transcription, for example by blocking RNA polymerase or recruiting repressive chromatin machinery. An activator binds DNA (an enhancer or CAP site) and increases transcription by recruiting or stabilizing RNA polymerase and coactivators, as CAP–cAMP does at the lac promoter. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
23. Define allosteric regulation in the context of transcription. Give an example.

<!-- SOLUTION
**Answer (Q23, Recall).** Allosteric regulation is the modulation of a regulatory protein's DNA-binding activity by a small effector molecule binding at a separate site, changing the protein's conformation. In the lac operon, allolactose binds the LacI repressor and allosterically reduces its affinity for the operator, releasing it from DNA and allowing transcription; conversely, tryptophan acts as a corepressor that activates the trp repressor. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
24. What are non-coding RNAs? Name three biologically important types.

<!-- SOLUTION
**Answer (Q24, Recall).** Non-coding RNAs are functional RNA transcripts that are not translated into protein but instead regulate gene expression and genome organization. Three important types are microRNAs (~22 nt, guide RISC to repress target mRNAs), small interfering RNAs (siRNAs, drive sequence-specific mRNA cleavage in RNAi), and long non-coding RNAs (lncRNAs such as Xist, which scaffold chromatin-modifying complexes). See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. What is genomic imprinting? Give one example of an imprinted gene.

<!-- SOLUTION
**Answer (Q25, Recall).** Genomic imprinting is parent-of-origin–specific monoallelic expression, in which a gene is expressed only from the maternally or only from the paternally inherited allele, set by differential DNA methylation at imprinting control regions in the germline. An example is IGF2, expressed only from the paternal allele (the maternal allele is silenced via the CTCF-controlled IGF2/H19 ICR). See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

## Questions 11–20: Application and Analysis {.unnumbered}

<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. A CpG island in the CDKN2A (p16) promoter is hypermethylated in a lung cancer cell. Trace the molecular consequences: (a) which protein is silenced; (b) what happens to CDK4/6 activity; (c) what happens to cell cycle progression; (d) why this is an alternative mechanism to p16 deletion for bypassing the G₁ checkpoint.

<!-- SOLUTION
**Answer (Q26, Application).** (a) Hypermethylation of the CDKN2A CpG island silences the p16^INK4a protein. (b) Without p16 to inhibit CDK4/6, Cyclin D–CDK4/6 remains active. (c) Active CDK4/6 hyperphosphorylates Rb, releasing E2F so the cell passes the G1 restriction point and proliferates. (d) This epigenetic silencing is functionally equivalent to deleting or mutating p16 — it inactivates the gene without changing the DNA sequence, an alternative route to bypassing the G1 checkpoint, and it is potentially reversible with demethylating agents. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. Polycomb repressive complex 2 (PRC2) trimethylates H3K27 and is overexpressed in many cancers. Explain: (a) the molecular mechanism of H3K27me3-mediated gene silencing; (b) how PRC2 spreads repression across large chromosomal domains; (c) why EZH2 (the catalytic subunit of PRC2) is a therapeutic target (tazemetostat).

<!-- SOLUTION
**Answer (Q27, Application).** (a) PRC2 trimethylates H3K27 (H3K27me3), which recruits PRC1 to ubiquitinate H2AK119 and compact chromatin, blocking transcription. (b) H3K27me3 is itself read by the PRC2 EED subunit, creating positive feedback that spreads the mark in cis across broad domains. (c) Overactive or mutant EZH2 hyper-represses tumour-suppressor and differentiation genes, so the catalytic EZH2 subunit is druggable; tazemetostat is an FDA-approved EZH2 inhibitor that reactivates these genes. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
28. In the lac operon, explain the logic of dual control by the lac repressor AND catabolite activator protein (CAP). Under which combination of conditions is the operon most highly transcribed? Under which is it completely silent?

<!-- SOLUTION
**Answer (Q28, Application).** The lac repressor provides negative control (bound to the operator unless allolactose is present) and CAP–cAMP provides positive control (active only when glucose is low, raising cAMP). The operon is maximally transcribed when lactose is present AND glucose is absent: the repressor is released and CAP–cAMP activates the promoter. It is completely silent when lactose is absent, because the repressor stays bound regardless of glucose status. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
29. RNA interference (RNAi) via siRNA silences gene expression post-transcriptionally. Compare siRNA (perfectly complementary → mRNA cleavage by Ago2) vs miRNA (partially complementary → translational repression and mRNA destabilisation). How does each affect the steady-state abundance of target mRNA?

<!-- SOLUTION
**Answer (Q29, Application).** siRNAs are perfectly complementary to their targets and direct Ago2 to endonucleolytically cleave (slice) the mRNA, sharply lowering its steady-state abundance. miRNAs are only partially complementary (matching mainly through the seed region) and act mostly by repressing translation and promoting deadenylation/decay, causing a more modest reduction in mRNA levels and a larger drop in protein output. Both reduce target expression, but siRNA produces stronger, cleavage-based mRNA loss. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
30. Enhancers can activate promoters over distances of >1 Mb in the genome by chromatin looping mediated by cohesin and CTCF. Explain: (a) the role of CTCF as a chromatin barrier/insulator; (b) how loss of a CTCF binding site at the IGF2/H19 imprinting control region (ICR) causes Beckwith-Wiedemann syndrome; (c) how 4C and HiC experiments confirm enhancer-promoter looping.

<!-- SOLUTION
**Answer (Q30, Application).** (a) CTCF binds insulator sequences and, with cohesin, organizes chromatin loops/TAD boundaries that block enhancers from acting across them. (b) At the IGF2/H19 ICR the maternal allele is unmethylated, so CTCF binds and insulates IGF2 from the downstream enhancers; loss of that CTCF site (or its methylation) lets the enhancer loop to IGF2, causing biallelic IGF2 expression and overgrowth (Beckwith-Wiedemann syndrome). (c) Chromosome-conformation methods such as 4C and Hi-C detect ligated DNA contacts, directly demonstrating physical enhancer–promoter looping. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

