# Questions — Mutations, CRISPR, and Genomics {#sec:q_unit_IV_mutations_and_genomics .unnumbered}


## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Predict the impact of a variant and justify the evidence needed to validate it.
- **Model/data emphasis:** Mutation-rate, edit-efficiency, and sequence-comparison calculations.
- **Assessment alignment:** Concept Explanation, Questions and Methods, Argumentation.
- **Misconception probe:** Not every mutation is harmful, and not every harmful mutation changes a protein sequence.
- **Transfer product:** Transfer variant reasoning to cancer genomics, ancestry, gene therapy, or microbial evolution.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.

## Questions 1–10: Core mechanisms {.unnumbered}

*This activity accompanies \cref{sec:unit_IV_mutations_and_genomics} of the textbook — review that chapter before attempting the exercises below.*

<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define a mutation. Classify mutations by: (a) type of base change; (b) effect on the protein.

<!-- SOLUTION
**Answer (Q1, Recall).** A mutation is a heritable change in the DNA sequence of a cell or organism. **(a) By base change:** *point mutations* are single-base substitutions, subdivided into **transitions** (purine↔purine or pyrimidine↔pyrimidine, e.g. A↔G) and **transversions** (purine↔pyrimidine); larger changes include **insertions** and **deletions** (indels). **(b) By effect on protein:** *silent/synonymous* (codon still specifies the same amino acid), *missense* (different amino acid), *nonsense* (creates a premature stop codon), and *frameshift* (indel not a multiple of three, shifting the reading frame and usually producing a truncated, nonfunctional protein). See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
2. What is a frameshift mutation? How does an insertion vs deletion cause this?

<!-- SOLUTION
**Answer (Q2, Recall).** A frameshift mutation is an insertion or deletion of a number of nucleotides **not a multiple of three**, which shifts the ribosomal reading frame downstream of the change. Because codons are read in non-overlapping triplets from the start codon, an **insertion** pushes all subsequent bases one or two positions to the right and a **deletion** shifts them left; either way every codon after the mutation site is mis-read, almost always generating a string of wrong amino acids and an early premature stop codon, yielding a truncated, nonfunctional protein. An indel that is a multiple of three only adds/removes whole codons and is in-frame, not a frameshift. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
3. What are transposons? Distinguish replicative (copy-and-paste) from non-replicative (cut-and-paste) transposons.

<!-- SOLUTION
**Answer (Q3, Recall).** Transposons ("jumping genes") are mobile DNA elements that can move to new genomic locations, sometimes causing mutations or genome rearrangements. **Replicative (copy-and-paste)** transposons leave the original element in place and insert a new copy elsewhere, so copy number increases — this includes **retrotransposons** (LINEs, SINEs, LTR/HERV elements), which transpose via an RNA intermediate reverse-transcribed into DNA. **Non-replicative (cut-and-paste)** DNA transposons are excised by a transposase from the donor site and reinserted at a target site without net copy gain. The mechanistic distinction is whether an RNA-templated copy is made (replicative) or the element physically relocates (conservative). See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
4. What is the Ames test? What does a positive result indicate?

<!-- SOLUTION
**Answer (Q4, Recall).** The Ames test (Bruce Ames, 1970s) is a bacterial assay for **mutagenicity**. It uses *Salmonella typhimurium* strains carrying a his⁻ mutation (cannot synthesize histidine); the test chemical (often with rat-liver S9 extract to mimic mammalian metabolic activation) is added, and **reversion (back-mutation) to his⁺** is scored as colonies growing on histidine-free medium. A **positive result** (a dose-dependent increase in revertant colonies above background) indicates the chemical is a mutagen; because ~80–90% of known carcinogens are mutagenic, a positive result flags the substance as a probable carcinogen warranting further testing. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
5. Describe the three types of DNA damage repair: (a) nucleotide excision repair (NER); (b) base excision repair (BER); (c) mismatch repair (MMR).

<!-- SOLUTION
**Answer (Q5, Recall).** **(a) Nucleotide excision repair (NER)** removes **bulky, helix-distorting lesions** (e.g., UV-induced pyrimidine dimers, chemical adducts): the damage is recognized, a ~24–32 nt oligonucleotide containing it is excised by endonucleases, and the gap is filled by DNA polymerase and sealed by ligase. **(b) Base excision repair (BER)** corrects **small, non-distorting single-base damage** (oxidation, deamination, alkylation): a DNA glycosylase removes the damaged base, AP endonuclease nicks the abasic site, and a short patch is resynthesized. **(c) Mismatch repair (MMR)** fixes **replication errors** (mispaired bases, small indel loops) that escaped polymerase proofreading; it identifies the newly synthesized (error-containing) strand, excises the stretch, and resynthesizes it, raising replication fidelity ~100–1000-fold. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
6. What is CRISPR-Cas9? Where does CRISPR originate in bacteria?

<!-- SOLUTION
**Answer (Q6, Recall).** Engineered SpCas9 is an RNA-guided DNA endonuclease derived from a bacterial Type II CRISPR-Cas system. A guide directs recognition of a complementary duplex target with a compatible PAM; a nuclease-induced break can then undergo end joining or template-dependent repair, with outcomes requiring measurement. CRISPR-Cas adaptive defenses occur in bacteria and archaea: invader-derived spacers in arrays supply sequence information for later recognition. This family-level description does not make each Cas effector or substrate interchangeable \citep{doudna2012,barrangou2007immunity}. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
7. What is gRNA (guide RNA) and what does it do in the Cas9 complex?

<!-- SOLUTION
**Answer (Q7, Recall).** The guide RNA (gRNA), commonly engineered as a **single guide RNA (sgRNA)**, is the targeting component of the CRISPR-Cas9 complex. It combines a crRNA spacer, about 20 nucleotides complementary to the intended DNA target, with a tracrRNA scaffold that binds Cas9. In canonical SpCas9 duplex targeting, protein-PAM recognition licenses local unwinding and guide-target pairing. Changing the spacer can retarget a complementary, PAM-compatible duplex sequence; cleavage and cellular editing outcomes still require validation \citep{doudna2012}. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
8. Define the PAM in canonical SpCas9 double-stranded DNA targeting. Why does it license target recognition, and what substrate boundary limits that statement?

<!-- SOLUTION
**Answer (Q8, Recall).** A **PAM (protospacer adjacent motif)** is a short flanking DNA motif; canonical SpCas9 prefers 5'-NGG-3' on the non-target strand, immediately 3' of the guide-matching protospacer. Protein–PAM recognition licenses local duplex unwinding and guide-target pairing. In canonical Cas9 immunity, recognition of the appropriate protospacer flank helps distinguish an invader's duplex DNA from the repeat-flanked spacer in its CRISPR array. The motif is in the DNA, not part of the guide. This is a duplex-target recognition mechanism, not a substrate-independent rule: the 2012 in-vitro study found that PAM mutations did not prevent target single-stranded DNA cleavage \citep{doudna2012}. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. What is whole-genome sequencing (WGS)? What sequencing technology is most commonly used?

<!-- SOLUTION
**Answer (Q9, Recall).** Whole-genome sequencing (WGS) is the determination of the **complete (or near-complete) nucleotide sequence of an organism's genome** in a single experiment, capturing coding, non-coding, regulatory, and structural variation. The most widely used technology is **Illumina short-read sequencing-by-synthesis** (massively parallel, high accuracy, ~150 bp reads), used for variant calling; **long-read platforms (Oxford Nanopore, PacBio HiFi)** are increasingly used to resolve repeats, structural variants, and produce telomere-to-telomere assemblies. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
10. What is a single nucleotide polymorphism (SNP)? How many SNPs does the average human genome contain?

<!-- SOLUTION
**Answer (Q10, Recall).** A single nucleotide polymorphism (SNP) is a single-base position in the genome at which a **variant allele occurs commonly in the population** (conventionally >1% allele frequency). SNPs are the most abundant form of human genetic variation, used as markers in GWAS, association studies, and ancestry analysis. On average, any two human genomes differ at roughly **4–5 million SNP sites** (about one SNP per ~1000 bp; ~3–4 million when compared to the reference), most of which lie in non-coding regions. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->


## Questions 11–20: Mechanisms and evidence {.unnumbered}

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
11. A chemotherapy drug causes G:C → A:T transitions. What type of DNA damage mechanism does this suggest (alkylation, intercalation, cross-linking, or depurination)? What repair pathway would normally correct this damage?

<!-- SOLUTION
**Answer (Q11, Application).** G:C→A:T is compatible with O6-alkylguanine mispairing with thymine;MGMT directly reverses O6-alkylguanine. It is not a unique diagnostic signature. In contrast,8-oxoG is an oxidation product that can pair with adenine and generate G:C→T:A transversions;OGG1-initiated BER addresses it. Award lesion chemistry,pairing,mutationclass andrepair distinction. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
12. Xeroderma pigmentosum (XP) patients have mutations in NER pathway genes (XPA-XPG). Explain: (a) what lesion NER repairs (CPDs from UV-B); (b) why XP patients have dramatically increased skin cancer risk; (c) why the nervous system is also affected in some XP subtypes.

<!-- SOLUTION
**Answer (Q12, Application).** **(a)** NER repairs **bulky helix-distorting lesions**, especially UV-B–induced **cyclobutane pyrimidine dimers (CPDs)** and 6-4 photoproducts. **(b)** XP patients carry loss-of-function mutations in NER genes (XPA–XPG), so sunlight-induced dimers persist; unrepaired lesions are bypassed by error-prone translesion polymerases, producing **C→T mutations** at dipyrimidine sites that accumulate in skin-cell oncogenes/tumor suppressors — giving a dramatically increased (often >1000-fold) **skin cancer** risk at an early age. **(c)** Some XP complementation groups (and the related trichothiodystrophy/Cockayne overlap) also impair **transcription-coupled repair** and TFIIH function; neurons cannot replace themselves and are highly sensitive to accumulated transcription-blocking endogenous DNA damage, producing **progressive neurodegeneration**. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
13. On the HBB coding strand, wild-type GAG→GTG (A→T) causes sickle hemoglobin. Design ex vivo Cas9-plus-donor correction to GAG, including guide/PAM placement, repair controls and stem-cell-function validation.

<!-- SOLUTION
**Answer (Q13, Synthesis).** Choose a matching spacer near the codon and an appropriate PAM, checking patient-specific sequence and off-target sites. Transient RNP plus donor can support HDR; NHEJ alone does not specify GTG→GAG. Quantify intended alleles, indels, structural outcomes and retained stem-cell function with unedited and donor-only controls. Award strand-correct chemistry, design, repair specificity and functional safety; HDR is not the only possible editing technology. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
14. A hypothetical patient's tumor is MSI-high because of mismatch-repair deficiency. Explain how replication errors can create candidate neoantigens and why PD-1 blockade can produce responses across different tissues. Why does a tissue-agnostic rationale or eligibility category not guarantee an individual response?

<!-- SOLUTION
**Answer (Q14, Application).** MMR deficiency permits replication errors, including indels at short repeats, to persist; coding frameshifts can create novel peptides. Presentation, T-cell recognition and the tumor environment determine whether candidate neoantigens elicit an effective response. Pembrolizumab blocks PD-1 signaling and can release an inhibitory constraint on T cells; it does not make every mutation immunogenic or remove every resistance mechanism. Le and colleagues' historical advanced-MMR-deficient cohort across twelve tumor types observed objective responses in 46/86 patients (about 53%), not all patients, and reported primary and acquired resistance \citep{le2017mismatch}. This supports a cross-tissue biomarker rationale, not universal efficacy or a claim about every current regulatory indication. Credit replication-error mechanism, conditional immune recognition and the population-to-patient boundary. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
15. Alu elements are non-autonomous SINE retrotransposons. Explain how an RNA intermediate can use L1-encoded machinery, distinguishing ORF2p's enzymatic roles from ORF1p. For a hypothetical insertion into a BRCA2 coding exon, explain possible effects and the evidence needed before inferring loss of function. Name germline mechanisms that can repress transposable elements.

<!-- SOLUTION
**Answer (Q15, Application).** Alu RNA is transcribed by RNA polymerase III and can recruit L1 ORF2p, which supplies endonuclease and reverse-transcriptase activities. ORF1p is an RNA-binding/chaperone protein, not those two enzymes; marked-Alu HeLa assays retained mobilization with an ORF1-defective construct but not comparable activity with an ORF2-defective construct \citep{dewannieux2003alu}. This is a specified experimental preparation, not a universal endogenous insertion rate. A coding-exon insertion could alter reading frame, splice processing or protein sequence; test the actual allele, transcripts, protein and homologous-recombination function rather than assume complete BRCA2 loss or inevitable cancer. A pathogenic germline allele can confer predisposition without every carrier developing disease. Germline repression can involve DNA methylation and PIWI--piRNA pathways, with mechanisms depending on organism, cell state and element. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. GWAS identify disease-associated variants, many in noncoding regions. Explain regulatory hypotheses and eQTL analysis, distinguish association from causal identification, and state what is missing before an odds ratio of 1.2 can be interpreted as absolute risk or clinical utility for type 2 diabetes.

<!-- SOLUTION
**Answer (Q16, Application).** A noncoding association may tag a regulatory or splice-altering causal variant through linkage disequilibrium; the associated SNP need not itself alter function. An eQTL associates genotype with expression and nominates genes/mechanisms but does not alone establish mediation or causal colocalization. An odds ratio of 1.2 does not specify absolute risk: baseline risk, population, time horizon and other predictors are required. Utility additionally depends on calibration, discrimination and a decision endpoint; modest association is neither proof of individual usefulness nor universal uselessness. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. The P53 gene is mutated in >50% of all human cancers. Explain: (a) the "gain-of-function" mutations in TP53 (R248W, R175H) that not only eliminate tumor suppression but actively promote invasion; (b) how wild-type p53 regulates CDK inhibitor p21 and pro-apoptotic PUMA; (c) what therapeutic strategy (restoring wild-type TP53 conformation using small molecules — APR-246) is being tested.

<!-- SOLUTION
**Answer (Q17, Application).** **(a)** Certain *TP53* missense alleles (e.g., **R248W, R175H**) are **gain-of-function**: beyond losing wild-type tumor-suppressor activity, the mutant p53 acquires new oncogenic properties — binding other transcription factors and remodeling gene expression to promote invasion, metastasis, and chemoresistance (often also dominant-negative over any remaining wild-type p53). **(b)** Wild-type p53 is a transcription factor that, on DNA damage, induces the **CDK inhibitor p21** (CDKN1A) to enforce G1/S arrest for repair, and pro-apoptotic targets such as **PUMA** (and BAX) to trigger apoptosis if damage is severe. **(c)** A tested strategy is **APR-246/eprenetapopt**, a small molecule that covalently modifies mutant p53 to **restore a wild-type-like conformation** and transcriptional activity, reactivating p21/PUMA-driven arrest and apoptosis in p53-mutant tumors. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. Why do out-of-frame DMD deletions often cause severe Duchenne while some in-frame deletions permit milder Becker disease? Explain mutation-amenable skipping of an existing exon 51 and its limits.

<!-- SOLUTION
**Answer (Q18, Application).** Frame-disrupting deletions often create premature stops and severe dystrophin deficiency; some in-frame deletions preserve a shorter, partly functional protein. The reading-frame rule has exceptions and deletion size alone does not determine severity. An exon-51-targeting ASO can restore frame only for an amenable deletion whose transcript still contains exon 51 and whose new junction is in frame; an already deleted exon cannot itself be skipped. The product remains internally shortened. Restored frame or detectable dystrophin does not by itself prove functional rescue, clinical benefit or conversion to a Becker course; measure the relevant protein and clinical endpoints. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
19. Epigenome-wide association studies (EWAS) examine DNA methylation differences between cases and controls. Explain: (a) why methylation differences (epimutations) are harder to interpret than genetic mutations; (b) why cell-type composition confounds EWAS analysis; (c) how MR (Mendelian randomisation) can be used to determine whether methylation changes are causal or merely correlative with disease.

<!-- SOLUTION
**Answer (Q19, Synthesis).** **(a)** Epimutations (DNA-methylation differences) are harder to interpret than genetic mutations because methylation is **dynamic, tissue- and cell-type-specific, age-dependent, and often a consequence rather than a cause** of disease — so an association does not establish direction or mechanism. **(b)** Bulk tissue is a mixture of cell types with very different methylomes; if cases and controls differ in **cell-type composition** (e.g., more immune cells), apparent methylation differences may merely reflect that composition shift, a major confounder requiring deconvolution or cell-sorted data. **(c)** **Mendelian randomization** uses germline SNPs that influence methylation (mQTLs) as instrumental variables: because alleles are randomized at conception and fixed before disease, an association between the genetically predicted methylation level and disease supports a **causal** (not merely correlative) role, provided the instrument is valid and not pleiotropic. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. Oxford Nanopore sequencing reads individual DNA/RNA molecules by measuring ionic current changes as they pass through a protein pore. Compare this technology to Illumina short-read sequencing: advantages (read length, direct RNA, base modifications, real-time), disadvantages (raw error rate ~5% vs <0.1%), and the application where each is most suitable.

<!-- SOLUTION
**Answer (Q20, Application).** **Oxford Nanopore** threads a single DNA/RNA strand through a protein nanopore and infers bases from characteristic ionic-current shifts. **Advantages over Illumina:** very long reads (kb–Mb, resolving repeats, structural variants, and enabling de novo/telomere-to-telomere assembly), **direct RNA sequencing**, detection of **base modifications** (e.g., methylation) without bisulfite, real-time/portable output. **Disadvantages:** higher raw per-base error (~5% vs <0.1% for Illumina) and lower throughput per dollar for SNV calling. **Best use:** Illumina for high-accuracy SNV/small-variant detection and large cohort genotyping; Nanopore (or PacBio HiFi) for structural-variant discovery, repeat regions, full-length isoforms, epigenetic marks, and rapid field/clinical sequencing. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->


## Questions 21–30: Transfer and evaluation {.unnumbered}

<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
21. Evaluate the safety of germline CRISPR editing (modifying embryo DNA, producing heritable changes) as attempted by He Jiankui in 2018. Identify three specific scientific risks (off-target edits, mosaicism, unintended immune consequences) and three ethical concerns (informed consent, enhancement vs therapy, equity of access). What international governance frameworks should govern germline editing?

<!-- SOLUTION
**Answer (Q21, Synthesis).** Empirically, He Jiankui edited *CCR5* in human embryos (2018) producing live births; documented and predicted problems include **off-target double-strand breaks**, **mosaicism** (not all cells edited), large deletions, and an **uncertain benefit** (the targeted *CCR5* change did not even reproduce the protective allele). The judgment that germline editing was unsafe and unethical follows because heritable, irreversible changes were introduced into healthy embryos without medical necessity, adequate preclinical safety, or genuine informed consent. Ethical concerns: **defective consent**, blurring **therapy vs enhancement**, and **equity of access**. Governance should require an enforceable international moratorium on clinical germline editing, oversight bodies (WHO registry, national regulators), and a transparent, criteria-based pathway. What would change the conclusion: demonstrated elimination of off-target/mosaicism risk plus a clear, otherwise-unavailable medical benefit and robust consent. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
22. A patient carries a disease-associated haplotype in which short reads map poorly because a 3-kb insertion and nearby promoter variant are absent from the linear reference. Design a graph-aware interpretation workflow: compare a single-reference call, a pangenome graph path, ClinVar/dbSNP/RefSeq/MANE status checks, and long-read validation; then explain when base editing, prime editing, Casgevy-style enhancer disruption, or Lyfgenia-style lentiviral gene addition would be the most defensible therapeutic logic.

<!-- SOLUTION
**Answer (Q22, Synthesis).** A strong workflow first asks whether the apparent variant is a mapping artifact: remap reads against a pangenome graph that contains the insertion path, inspect read support across both breakpoints, check dbSNP for the submitted variant identifier, ClinVar for assertion/review status, and RefSeq/MANE for the transcript used to name the change, then confirm phase with long reads or linked reads before reporting a clinical haplotype \citep{dbsnp2026,clinvar2026,refseq2026,mane2026}. Base editing is best for a single transition within an editor's activity window when bystander edits are acceptable or avoidable. Prime editing is better for installing or correcting a short promoter motif, such as fetal-globin promoter rewrites, because the edit is templated without a double-strand break. Casgevy-style enhancer disruption is a different logic: it does not repair *HBB* but changes erythroid regulation by reducing BCL11A enhancer activity to raise fetal hemoglobin. Lyfgenia-style lentiviral gene addition is another regulatory path: it adds a functional hemoglobin transgene rather than editing the native locus, so ClinicalTrials.gov trial status and FDA approved indications must be checked separately \citep{clinicaltrials2026,fda2026lyfgenia}. Keep sequence evidence, database currency, expression evidence, editing feasibility, off-target assessment, and clinical maturity separate. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
23. Evaluate the "cancer genome atlas" concept: sequencing thousands of tumor genomes has generated a mutation landscape for most cancer types, identifying "drivers" vs "passengers." What statistical criteria distinguish drivers from passengers, and why have most cancer driver mutations proven difficult to target therapeutically?

<!-- SOLUTION
**Answer (Q23, Synthesis).** Empirically, sequencing thousands of tumors (e.g., TCGA) maps recurrent mutations across cancer types. **Drivers vs passengers** are distinguished statistically: drivers show **mutation recurrence above the background mutation rate** (MutSigCV-type models correcting for gene length, replication timing, and context), **selection signatures** (elevated nonsynonymous/synonymous or clustering at hotspots), and functional/pathway enrichment; passengers are random by-product mutations consistent with background. The judgment that driver discovery has not translated easily into therapy follows because many drivers are **tumor-suppressor losses or "undruggable" proteins** (e.g., TP53, RAS until recently, transcription factors) lacking enzymatic pockets, and tumor heterogeneity/resistance limits single-target success. What would change the conclusion: new modalities (degraders, covalent KRAS inhibitors, synthetic lethality) making previously undruggable drivers tractable. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
24. Synthetic chromosomes have been designed and built in yeast (Sc2.0, synthetic chromosome project). Evaluate the design principles (removal of transposons, recombination tags added, inducible evolution mode via SCRaMbLE), and discuss whether a fully synthetic human chromosome could be built and what it would require.

<!-- SOLUTION
**Answer (Q24, Synthesis).** Sc2.0 redesigns yeast chromosomes with defined principles: **removal of destabilizing/repetitive elements** (transposons, introns, redundant tRNA genes relocated), **synonymous recoding** (e.g., recoding stop codons to free a codon), insertion of **loxPsym recombination tags** at non-essential 3' ends to enable **SCRaMbLE** (Cre-induced inducible genome rearrangement for accelerated, controllable evolution), and watermarks/PCRTags for tracking — yielding a streamlined, programmable genome. The causal logic: design choices → reduced genome instability and a built-in diversification tool → a viable, evolvable synthetic eukaryotic chromosome. A fully synthetic **human** chromosome is far harder: it would require accurate megabase synthesis and assembly, functional **centromeres, telomeres, and origins**, correct large-scale 3D chromatin/epigenetic regulation, and stable mitotic segregation — currently beyond reach and raising serious safety/ethical constraints. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Explain how PIWI-bound piRNAs recognize transposon transcripts by sequence complementarity, how amplification reinforces silencing, and why imperfect matches do not mean Watson–Crick pairing is absent.

<!-- SOLUTION
**Answer (Q25, Synthesis).** **(a)** piRNAs (~24–31 nt, PIWI-bound, Dicer-independent) recognize transposons by **sequence complementarity to transposon transcripts**, but tolerance for mismatches plus an amplifying "**ping-pong**" cycle (sense and antisense piRNAs reciprocally guiding cleavage) lets the system target diverse, mutating transposons rather than requiring exact Watson–Crick matching of a fixed siRNA. **(b)** Loss of PIWI proteins (e.g., MILI/MIWI/MIWI2 knockouts) **derepresses transposons in the germline**, causing insertional mutagenesis, DNA damage, meiotic arrest, and **infertility/sterility** — showing piRNA silencing is essential for genome integrity in germ cells. **(c)** Beyond transposons, piRNAs can also target some **non-transposon mRNAs** (regulating their stability/translation, e.g., during spermiogenesis), indicating a broader post-transcriptional regulatory role. What would change this view: evidence that observed mRNA effects are indirect consequences of transposon derepression rather than direct piRNA targeting. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Precision oncology based on tumor sequencing identifies actionable mutations. However, intratumoral heterogeneity (ITH) means that some cells within the tumor may lack the targeted mutation. Evaluate: (a) how clonal vs subclonal mutations are distinguished by variant allele frequency; (b) why targeting a clonal mutation (present in most cells) is more likely to be effective; (c) how liquid biopsy (circulating tumor DNA, ctDNA) can detect resistance mechanisms before clinical progression.

<!-- SOLUTION
**Answer (Q26, Synthesis).** Purity- and copy-number-adjusted VAF, with sampling uncertainty and spatial coverage, can help estimate cancer-cell fractions; low VAF alone does not establish subclonality. A clonal target offers broader coverage than a subclonal target, but its presence does not exclude pre-existing bypass resistance or variable drug response. ctDNA may reveal resistance-associated molecular changes before imaging, subject to shedding and assay sensitivity. Earlier detection alone does not show that switching treatment earlier improves outcomes; that requires a prospective strategy comparison with clinical endpoints. Award clonality assumptions, resistance limits and detection-versus-benefit distinction. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. Evaluate whether "de-extinction" (reviving extinct species via CRISPR genome editing of a close relative) is scientifically feasible for: (a) the woolly mammoth (editing *Loxodonta africana* genome ~50 key cold-adaptation genes); (b) the passenger pigeon (*Ectopistes migratorius*, using band-tailed pigeon as template). What are the ecological risks of reintroducing de-extinct animals?

<!-- SOLUTION
**Answer (Q27, Synthesis).** Empirically, **de-extinction by CRISPR** does not literally resurrect an extinct species; it edits a close living relative toward the extinct phenotype. **(a)** For the woolly mammoth, ~50 cold-adaptation genes (hemoglobin, hair, fat, *TRPV3*) can be edited into the **Asian elephant (*Elephas maximus*, not *Loxodonta*)** genome, but a viable animal requires solving elephant cloning/artificial-womb gestation and integrating many edits — partial feasibility at best, yielding a cold-tolerant elephant hybrid, not a true mammoth. **(b)** The passenger pigeon (*Ectopistes migratorius*) using band-tailed pigeon as template faces the same limits plus avian cloning being unsolved. The judgment of limited feasibility rests on incomplete ancient genomes, polygenic phenotypes, and reproductive-technology gaps. **Ecological risks:** disrupted modern ecosystems, disease introduction, no surviving social/migratory learning, and diversion of conservation resources. What would change it: solved reproductive cloning and complete, high-quality ancient genomes. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
28. Compare HIV/lentiviral integration preferences with therapeutic recombinant AAV persistence. Distinguish wild-type Rep-dependent AAVS1 targeting from recombinant-vector behavior, and identify vector-design, tissue and dose information needed to assess genotoxicity rather than infer a safe harbor guarantee.

<!-- SOLUTION
**Answer (Q28, Synthesis).** HIV/lentiviral integration favors active transcription units and can disrupt or dysregulate host loci. Therapeutic recombinant AAV generally persists predominantly episomally, but integration can occur; it should not be assigned routine Rep-dependent AAVS1 targeting or zero genotoxic risk. Early SCID-X1 gamma-retroviral insertional leukemias are a design-specific warning, not an interchangeable risk estimate for every lentiviral vector. Compare actual vector regulatory elements, integration profiles, dose, tissue, clonal expansion and long-term outcomes. Award wild-type/recombinant and gamma-retroviral/lentiviral distinctions rather than a universal safety ranking. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
29. tRNA suppressors can read through stop codons, restoring protein production from genes with premature stop mutations. Evaluate the therapeutic use of aminoglycoside antibiotics (gentamicin) as readthrough agents for nonsense mutations (e.g., in *Dystrophin*) — what are the molecular mechanisms, the challenges of specificity (also read through normal stop codons), and the clinical results to date?

<!-- SOLUTION
**Answer (Q29, Synthesis).** Gentamicin is an aminoglycoside that perturbs decoding and can promote near-cognate tRNA insertion at a premature stop. Ataluren is not an aminoglycoside and should not be assigned that class mechanism. Stop context, concentration, NMD and inserted residue determine rescue; normal-stop readthrough and oto/nephrotoxicity are risks. Award class distinction, mechanism, context and functional/safety endpoints; full-length protein alone is not clinical benefit. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
30. Critically evaluate the technical and ethical implications of building a "minimal synthetic cell" with a fully defined genome (as in the Venter Institute's JCVI-syn3.0, ~473 genes). What does the set of essential genes reveal about the minimal requirements for cellular life? If this minimal genome could be commercially manufactured and sold, what biosafety and biosecurity regulations should apply?

<!-- SOLUTION
**Answer (Q30, Synthesis).** Empirically, JCVI-syn3.0 (Venter Institute) is a chemically synthesized, transplanted minimal *Mycoplasma* genome of **~473 genes** that supports self-replication. The set of essential genes shows that minimal cellular life still requires the core processes — **genome replication, transcription, translation, membrane/lipid biogenesis, and basic metabolism** — yet ~**149 essential genes still have unknown function**, revealing that we do not fully understand even a minimal cell. The judgment that this is profound but bounded follows: it defines a lower bound on life's genetic complexity without claiming we can yet design genomes from first principles. **Biosafety/biosecurity:** commercial minimal cells would need DNA-synthesis screening, containment and engineered biocontainment (kill switches, auxotrophy), licensing/traceability, dual-use review, and international oversight. What would change the assessment: a minimal genome whose every gene's function is known and that is provably non-viable outside controlled conditions. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
