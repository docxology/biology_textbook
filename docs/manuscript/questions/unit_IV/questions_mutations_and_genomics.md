# Questions — Mutations, CRISPR, and Genomics {#sec:q_unit_IV_mutations_and_genomics .unnumbered}


<!-- question-coverage-start -->
## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Predict the impact of a variant and justify the evidence needed to validate it.
- **Model/data emphasis:** Mutation-rate, edit-efficiency, and sequence-comparison calculations.
- **Assessment alignment:** Concept Explanation, Questions and Methods, Argumentation.
- **Misconception probe:** Not every mutation is harmful, and not every harmful mutation changes a protein sequence.
- **Transfer product:** Transfer variant reasoning to cancer genomics, ancestry, gene therapy, or microbial evolution.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.
<!-- question-coverage-end -->

## Questions 1–10: Recall and Comprehension {.unnumbered}

*This activity accompanies \cref{sec:unit_IV_mutations_and_genomics} of the textbook — review that chapter before attempting the exercises below.*

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define a mutation. Classify mutations by: (a) type of base change; (b) effect on the protein.

<!-- SOLUTION
**Answer (Q1, Recall).** A mutation is a heritable change in the DNA sequence of a cell or organism. **(a) By base change:** *point mutations* are single-base substitutions, subdivided into **transitions** (purine↔purine or pyrimidine↔pyrimidine, e.g. A↔G) and **transversions** (purine↔pyrimidine); larger changes include **insertions** and **deletions** (indels). **(b) By effect on protein:** *silent/synonymous* (codon still specifies the same amino acid), *missense* (different amino acid), *nonsense* (creates a premature stop codon), and *frameshift* (indel not a multiple of three, shifting the reading frame and usually producing a truncated, nonfunctional protein). See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. What is a frameshift mutation? How does an insertion vs deletion cause this?

<!-- SOLUTION
**Answer (Q2, Recall).** A frameshift mutation is an insertion or deletion of a number of nucleotides **not a multiple of three**, which shifts the ribosomal reading frame downstream of the change. Because codons are read in non-overlapping triplets from the start codon, an **insertion** pushes all subsequent bases one or two positions to the right and a **deletion** shifts them left; either way every codon after the mutation site is mis-read, almost always generating a string of wrong amino acids and an early premature stop codon, yielding a truncated, nonfunctional protein. An indel that is a multiple of three only adds/removes whole codons and is in-frame, not a frameshift. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
3. What are transposons? Distinguish replicative (copy-and-paste) from non-replicative (cut-and-paste) transposons.

<!-- SOLUTION
**Answer (Q3, Recall).** Transposons ("jumping genes") are mobile DNA elements that can move to new genomic locations, sometimes causing mutations or genome rearrangements. **Replicative (copy-and-paste)** transposons leave the original element in place and insert a new copy elsewhere, so copy number increases — this includes **retrotransposons** (LINEs, SINEs, LTR/HERV elements), which transpose via an RNA intermediate reverse-transcribed into DNA. **Non-replicative (cut-and-paste)** DNA transposons are excised by a transposase from the donor site and reinserted at a target site without net copy gain. The mechanistic distinction is whether an RNA-templated copy is made (replicative) or the element physically relocates (conservative). See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
4. What is the Ames test? What does a positive result indicate?

<!-- SOLUTION
**Answer (Q4, Recall).** The Ames test (Bruce Ames, 1970s) is a bacterial assay for **mutagenicity**. It uses *Salmonella typhimurium* strains carrying a his⁻ mutation (cannot synthesize histidine); the test chemical (often with rat-liver S9 extract to mimic mammalian metabolic activation) is added, and **reversion (back-mutation) to his⁺** is scored as colonies growing on histidine-free medium. A **positive result** (a dose-dependent increase in revertant colonies above background) indicates the chemical is a mutagen; because ~80–90% of known carcinogens are mutagenic, a positive result flags the substance as a probable carcinogen warranting further testing. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
5. Describe the three types of DNA damage repair: (a) nucleotide excision repair (NER); (b) base excision repair (BER); (c) mismatch repair (MMR).

<!-- SOLUTION
**Answer (Q5, Recall).** **(a) Nucleotide excision repair (NER)** removes **bulky, helix-distorting lesions** (e.g., UV-induced pyrimidine dimers, chemical adducts): the damage is recognized, a ~24–32 nt oligonucleotide containing it is excised by endonucleases, and the gap is filled by DNA polymerase and sealed by ligase. **(b) Base excision repair (BER)** corrects **small, non-distorting single-base damage** (oxidation, deamination, alkylation): a DNA glycosylase removes the damaged base, AP endonuclease nicks the abasic site, and a short patch is resynthesized. **(c) Mismatch repair (MMR)** fixes **replication errors** (mispaired bases, small indel loops) that escaped polymerase proofreading; it identifies the newly synthesized (error-containing) strand, excises the stretch, and resynthesizes it, raising replication fidelity ~100–1000-fold. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
6. What is CRISPR-Cas9? Where does CRISPR originate in bacteria?

<!-- SOLUTION
**Answer (Q6, Recall).** CRISPR-Cas9 is a programmable, RNA-guided DNA endonuclease used for genome editing: a **guide RNA** directs the **Cas9** protein to a complementary DNA sequence adjacent to a PAM, where Cas9 creates a double-strand break that the cell repairs by NHEJ (disruptive indels) or HDR (precise edits with a donor template). It originates as a **bacterial and archaeal adaptive immune system**: short fragments of invading phage/plasmid DNA are stored as spacers in **CRISPR arrays**, transcribed into crRNAs, and used by Cas nucleases to recognize and cleave matching nucleic acid on re-infection. (Doudna & Charpentier, 2020 Nobel Prize in Chemistry.) See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
7. What is gRNA (guide RNA) and what does it do in the Cas9 complex?

<!-- SOLUTION
**Answer (Q7, Recall).** The guide RNA (gRNA), commonly engineered as a **single guide RNA (sgRNA)**, is the targeting component of the CRISPR-Cas9 complex. It is a fusion of a **crRNA** — whose ~20-nucleotide spacer is complementary to the intended DNA target — and a **tracrRNA** scaffold that binds and activates Cas9. The gRNA loads into Cas9 and, by Watson–Crick base-pairing of its spacer with the target DNA (immediately 5' of a PAM), positions the Cas9 nuclease domains to introduce a site-specific double-strand break. Changing the 20-nt spacer reprograms Cas9 to any new genomic site. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
8. Define the PAM sequence. Why is it required for CRISPR cutting?

<!-- SOLUTION
**Answer (Q8, Recall).** The **PAM (protospacer adjacent motif)** is a short DNA sequence (5'-NGG-3' for *Streptococcus pyogenes* Cas9) located immediately 3' of the 20-nt target (protospacer) in the genomic DNA. It is **required because Cas9 first recognizes the PAM** through protein–DNA contacts; PAM binding licenses local DNA unwinding and lets the guide RNA test for complementarity, after which the nuclease domains cut. The PAM is **not part of the guide RNA**, so the bacterium's own CRISPR array (which lacks an adjacent PAM at the spacer) is not cleaved — this is how Cas9 distinguishes invader DNA from self and avoids autoimmunity. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. What is whole-genome sequencing (WGS)? What sequencing technology is most commonly used?

<!-- SOLUTION
**Answer (Q9, Recall).** Whole-genome sequencing (WGS) is the determination of the **complete (or near-complete) nucleotide sequence of an organism's genome** in a single experiment, capturing coding, non-coding, regulatory, and structural variation. The most widely used technology is **Illumina short-read sequencing-by-synthesis** (massively parallel, high accuracy, ~150 bp reads), used for variant calling; **long-read platforms (Oxford Nanopore, PacBio HiFi)** are increasingly used to resolve repeats, structural variants, and produce telomere-to-telomere assemblies. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
10. What is a single nucleotide polymorphism (SNP)? How many SNPs does the average human genome contain?

<!-- SOLUTION
**Answer (Q10, Recall).** A single nucleotide polymorphism (SNP) is a single-base position in the genome at which a **variant allele occurs commonly in the population** (conventionally >1% allele frequency). SNPs are the most abundant form of human genetic variation, used as markers in GWAS, association studies, and ancestry analysis. On average, any two human genomes differ at roughly **4–5 million SNP sites** (about one SNP per ~1000 bp; ~3–4 million when compared to the reference), most of which lie in non-coding regions. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->


## Questions 11–20: Application and Analysis {.unnumbered}

<!-- assess: LO=LO2; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
11. A chemotherapy drug causes G:C → A:T transitions. What type of DNA damage mechanism does this suggest (alkylation, intercalation, cross-linking, or depurination)? What repair pathway would normally correct this damage?

<!-- SOLUTION
**Answer (Q11, Application).** A G:C → A:T transition is the signature of **alkylation** (or oxidative deamination), not intercalation, cross-linking, or simple depurination. **Mechanism:** an alkylating agent adds an alkyl group to guanine forming **O⁶-methylguanine (or 8-oxoG)**, which mispairs with thymine during replication; the next round fixes the change as G:C → A:T. **Repair pathway:** O⁶-alkylguanine is reversed directly by **MGMT (O⁶-methylguanine-DNA methyltransferase)**, while oxidized/alkylated bases are normally removed by **base excision repair (BER)** (e.g., OGG1 glycosylase for 8-oxoG); mismatch repair can also act on the resulting mispair. Failure of these explains the mutator phenotype of alkylating chemotherapeutics. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
12. Xeroderma pigmentosum (XP) patients have mutations in NER pathway genes (XPA-XPG). Explain: (a) what lesion NER repairs (CPDs from UV-B); (b) why XP patients have dramatically increased skin cancer risk; (c) why the nervous system is also affected in some XP subtypes.

<!-- SOLUTION
**Answer (Q12, Application).** **(a)** NER repairs **bulky helix-distorting lesions**, especially UV-B–induced **cyclobutane pyrimidine dimers (CPDs)** and 6-4 photoproducts. **(b)** XP patients carry loss-of-function mutations in NER genes (XPA–XPG), so sunlight-induced dimers persist; unrepaired lesions are bypassed by error-prone translesion polymerases, producing **C→T mutations** at dipyrimidine sites that accumulate in skin-cell oncogenes/tumor suppressors — giving a dramatically increased (often >1000-fold) **skin cancer** risk at an early age. **(c)** Some XP complementation groups (and the related trichothiodystrophy/Cockayne overlap) also impair **transcription-coupled repair** and TFIIH function; neurons cannot replace themselves and are highly sensitive to accumulated transcription-blocking endogenous DNA damage, producing **progressive neurodegeneration**. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
13. A researcher designs a CRISPR experiment to correct a point mutation (G→A) in the *HBB* gene causing sickle-cell disease. List: (a) the guide RNA design rules; (b) the delivery method for cells (RNP electroporation vs viral vector); (c) why homology-directed repair (HDR, requiring a donor template) is needed rather than NHEJ; (d) how to increase HDR efficiency.

<!-- SOLUTION
**Answer (Q13, Application).** **(a) Guide RNA design:** choose a 20-nt spacer matching *HBB* near the codon-6 mutation, immediately 5' of an NGG PAM, with high on-target and minimal off-target/self-similarity scores; place the cut close to the edit site. **(b) Delivery:** for *ex vivo* editing of patient hematopoietic stem cells, **ribonucleoprotein (Cas9 protein + sgRNA) electroporation** is preferred over viral vectors — it is transient (lower off-target and immunogenicity, no insertional mutagenesis). **(c)** Correcting G→A back to wild type requires **HDR** because only HDR copies a supplied **donor template** to install the exact sequence; **NHEJ** merely religates the break and introduces random indels (a knockout, not a correction). **(d) Increasing HDR:** use a single-stranded oligo donor, deliver in S/G2 phase, inhibit NHEJ (e.g., DNA-PK/Ligase IV inhibitors or NHEJ-pathway suppression), and use chemically protected donors at optimized stoichiometry. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
14. A patient's tumor has microsatellite instability (MSI-high) due to MMR deficiency. Explain: (a) what kinds of mutations accumulate in MSI-high tumors; (b) why MSI tumors produce many neoantigens; (c) why pembrolizumab (anti-PD-1) is effective in MSI-high tumors regardless of cancer type (tissue-agnostic treatment).

<!-- SOLUTION
**Answer (Q14, Application).** **(a)** MMR deficiency means replication-slippage errors at short tandem repeats go uncorrected, so MSI-high tumors accumulate huge numbers of **indels in microsatellites** and a very high overall **mutation burden**, especially frameshifts in coding repeats. **(b)** Frameshifted coding sequences generate novel out-of-frame peptides — **neoantigens** — that are highly immunogenic because they are not present in normal tissue and are seen as foreign by T cells. **(c)** This high neoantigen load makes the tumor strongly immune-recognized but held in check by the PD-1/PD-L1 checkpoint; **pembrolizumab (anti-PD-1)** releases that brake, restoring T-cell killing. Because the mechanism depends on neoantigen load rather than tissue of origin, anti-PD-1 is approved **tissue-agnostically** for MSI-high/dMMR tumors. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
15. Transposaon Alu (SINE family) comprise ~11% of the human genome. Explain: (a) how Alu elements replicate via RNA intermediates (SINE retrotransposition); (b) how an Alu insertion in exon 16 of BRCA2 could cause breast cancer; (c) how the host genome suppresses transposon activity in the germline (piRNA pathway).

<!-- SOLUTION
**Answer (Q15, Application).** **(a)** Alu elements are **non-autonomous SINE retrotransposons**: they are transcribed by RNA Pol III, and the resulting RNA is reverse-transcribed and integrated by the **LINE-1 (L1) machinery** (ORF1/ORF2 proteins providing reverse transcriptase and endonuclease) — a copy-and-paste, RNA-intermediate mechanism that has expanded Alu to ~11% of the genome. **(b)** A new Alu insertion into **exon 16 of BRCA2** disrupts the coding sequence (introducing extra sequence, splicing changes, or a frameshift/premature stop), abolishing functional BRCA2 and its homologous-recombination DNA-repair role, predisposing to breast/ovarian cancer. **(c)** In the germline, transposons are silenced by the **piRNA pathway**: PIWI proteins loaded with piRNAs recognize transposon transcripts, cleaving them and directing DNA methylation/heterochromatin at their loci to prevent mobilization. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. GWAS (genome-wide association studies) have identified thousands of SNPs associated with disease risk, but most are in non-coding regions. Explain: (a) why non-coding SNPs are biologically meaningful (enhancer activity, splicing regulation); (b) how eQTL analysis links SNPs to gene expression levels; (c) why a SNP with odds ratio 1.2 for Type 2 Diabetes is clinically uninformative for individual risk prediction.

<!-- SOLUTION
**Answer (Q16, Application).** **(a)** Most trait-associated SNPs are non-coding because they lie in **regulatory DNA** — enhancers, promoters, or splicing elements — where they alter transcription-factor binding, chromatin state, or splice-site usage and thus change gene *dosage* rather than protein sequence. **(b)** **eQTL analysis** correlates a SNP's genotype with mRNA expression levels across many individuals; a SNP that statistically predicts expression of a nearby (cis) or distant (trans) gene is an expression QTL, providing the mechanistic link from a non-coding GWAS hit to a target gene. **(c)** A SNP with **odds ratio ~1.2** shifts an individual's absolute Type 2 Diabetes risk only marginally and is swamped by environmental and polygenic background; such small effect sizes are useful for understanding biology and population-level architecture but are **not clinically informative for predicting an individual's risk**. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. The P53 gene is mutated in >50% of all human cancers. Explain: (a) the "gain-of-function" mutations in TP53 (R248W, R175H) that not only eliminate tumor suppression but actively promote invasion; (b) how wild-type p53 regulates CDK inhibitor p21 and pro-apoptotic PUMA; (c) what therapeutic strategy (restoring wild-type TP53 conformation using small molecules — APR-246) is being tested.

<!-- SOLUTION
**Answer (Q17, Application).** **(a)** Certain *TP53* missense alleles (e.g., **R248W, R175H**) are **gain-of-function**: beyond losing wild-type tumor-suppressor activity, the mutant p53 acquires new oncogenic properties — binding other transcription factors and remodeling gene expression to promote invasion, metastasis, and chemoresistance (often also dominant-negative over any remaining wild-type p53). **(b)** Wild-type p53 is a transcription factor that, on DNA damage, induces the **CDK inhibitor p21** (CDKN1A) to enforce G1/S arrest for repair, and pro-apoptotic targets such as **PUMA** (and BAX) to trigger apoptosis if damage is severe. **(c)** A tested strategy is **APR-246/eprenetapopt**, a small molecule that covalently modifies mutant p53 to **restore a wild-type-like conformation** and transcriptional activity, reactivating p21/PUMA-driven arrest and apoptosis in p53-mutant tumors. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. Gene therapy for Duchenne muscular dystrophy (DMD, caused by large deletions in *Dystrophin*) uses exon skipping with antisense oligonucleotides (AONs). Explain: (a) why some deletions cause severe DMD while frameshifted deletions are less severe (in-frame vs out-of-frame); (b) how AON targeting exon 51 restores the reading frame; (c) why this produces "Becker-like" dystrophin rather than fully corrected dystrophin.

<!-- SOLUTION
**Answer (Q18, Application).** **(a)** Dystrophin tolerates internal in-frame deletions (producing shortened but partly functional protein → milder **Becker** muscular dystrophy), whereas **out-of-frame** deletions shift the reading frame, create a premature stop, and abolish dystrophin → severe **Duchenne**. So a large deletion's severity depends on whether it disrupts the reading frame, not its size. **(b)** An antisense oligonucleotide complementary to **exon 51** masks its splice signals, causing the spliceosome to **skip exon 51**; this removes additional sequence so that the exon junctions flanking the original deletion are realigned **back into frame**, allowing translation of an internally truncated protein. **(c)** The restored protein lacks the skipped exon(s), so it is an internally shortened, **Becker-like dystrophin** with partial function — converting a severe DMD phenotype toward a milder one rather than fully curing it. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. Epigenome-wide association studies (EWAS) examine DNA methylation differences between cases and controls. Explain: (a) why methylation differences (epimutations) are harder to interpret than genetic mutations; (b) why cell-type composition confounds EWAS analysis; (c) how MR (Mendelian randomisation) can be used to determine whether methylation changes are causal or merely correlative with disease.

<!-- SOLUTION
**Answer (Q19, Application).** **(a)** Epimutations (DNA-methylation differences) are harder to interpret than genetic mutations because methylation is **dynamic, tissue- and cell-type-specific, age-dependent, and often a consequence rather than a cause** of disease — so an association does not establish direction or mechanism. **(b)** Bulk tissue is a mixture of cell types with very different methylomes; if cases and controls differ in **cell-type composition** (e.g., more immune cells), apparent methylation differences may merely reflect that composition shift, a major confounder requiring deconvolution or cell-sorted data. **(c)** **Mendelian randomization** uses germline SNPs that influence methylation (mQTLs) as instrumental variables: because alleles are randomized at conception and fixed before disease, an association between the genetically predicted methylation level and disease supports a **causal** (not merely correlative) role, provided the instrument is valid and not pleiotropic. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. Oxford Nanopore sequencing reads individual DNA/RNA molecules by measuring ionic current changes as they pass through a protein pore. Compare this technology to Illumina short-read sequencing: advantages (read length, direct RNA, base modifications, real-time), disadvantages (raw error rate ~5% vs <0.1%), and the application where each is most suitable.

<!-- SOLUTION
**Answer (Q20, Application).** **Oxford Nanopore** threads a single DNA/RNA strand through a protein nanopore and infers bases from characteristic ionic-current shifts. **Advantages over Illumina:** very long reads (kb–Mb, resolving repeats, structural variants, and enabling de novo/telomere-to-telomere assembly), **direct RNA sequencing**, detection of **base modifications** (e.g., methylation) without bisulfite, real-time/portable output. **Disadvantages:** higher raw per-base error (~5% vs <0.1% for Illumina) and lower throughput per dollar for SNV calling. **Best use:** Illumina for high-accuracy SNV/small-variant detection and large cohort genotyping; Nanopore (or PacBio HiFi) for structural-variant discovery, repeat regions, full-length isoforms, epigenetic marks, and rapid field/clinical sequencing. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->


## Questions 21–30: Synthesis and Evaluation {.unnumbered}

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
21. Evaluate the safety of germline CRISPR editing (modifying embryo DNA, producing heritable changes) as attempted by He Jiankui in 2018. Identify three specific scientific risks (off-target edits, mosaicism, unintended immune consequences) and three ethical concerns (informed consent, enhancement vs therapy, equity of access). What international governance frameworks should govern germline editing?

<!-- SOLUTION
**Answer (Q21, Synthesis).** Empirically, He Jiankui edited *CCR5* in human embryos (2018) producing live births; documented and predicted problems include **off-target double-strand breaks**, **mosaicism** (not all cells edited), large deletions, and an **uncertain benefit** (the targeted *CCR5* change did not even reproduce the protective allele). The judgment that germline editing was unsafe and unethical follows because heritable, irreversible changes were introduced into healthy embryos without medical necessity, adequate preclinical safety, or genuine informed consent. Ethical concerns: **defective consent**, blurring **therapy vs enhancement**, and **equity of access**. Governance should require an enforceable international moratorium on clinical germline editing, oversight bodies (WHO registry, national regulators), and a transparent, criteria-based pathway. What would change the conclusion: demonstrated elimination of off-target/mosaicism risk plus a clear, otherwise-unavailable medical benefit and robust consent. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
22. A patient carries a disease-associated haplotype in which short reads map poorly because a 3-kb insertion and nearby promoter variant are absent from the linear reference. Design a graph-aware interpretation workflow: compare a single-reference call, a pangenome graph path, ClinVar/dbSNP/RefSeq/MANE status checks, and long-read validation; then explain when base editing, prime editing, Casgevy-style enhancer disruption, or Lyfgenia-style lentiviral gene addition would be the most defensible therapeutic logic.

<!-- SOLUTION
**Answer (Q22, Synthesis).** A strong workflow first asks whether the apparent variant is a mapping artifact: remap reads against a pangenome graph that contains the insertion path, inspect read support across both breakpoints, check dbSNP for the submitted variant identifier, ClinVar for assertion/review status, and RefSeq/MANE for the transcript used to name the change, then confirm phase with long reads or linked reads before reporting a clinical haplotype \citep{dbsnp2026,clinvar2026,refseq2026,mane2026}. Base editing is best for a single transition within an editor's activity window when bystander edits are acceptable or avoidable. Prime editing is better for installing or correcting a short promoter motif, such as fetal-globin promoter rewrites, because the edit is templated without a double-strand break. Casgevy-style enhancer disruption is a different logic: it does not repair *HBB* but changes erythroid regulation by reducing BCL11A enhancer activity to raise fetal hemoglobin. Lyfgenia-style lentiviral gene addition is another regulatory path: it adds a functional hemoglobin transgene rather than editing the native locus, so ClinicalTrials.gov trial status and FDA approved indications must be checked separately \citep{clinicaltrials2026,fda2026lyfgenia}. Keep sequence evidence, database currency, expression evidence, editing feasibility, off-target assessment, and clinical maturity separate. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
23. Evaluate the "cancer genome atlas" concept: sequencing thousands of tumor genomes has generated a mutation landscape for most cancer types, identifying "drivers" vs "passengers." What statistical criteria distinguish drivers from passengers, and why have most cancer driver mutations proven difficult to target therapeutically?

<!-- SOLUTION
**Answer (Q23, Synthesis).** Empirically, sequencing thousands of tumors (e.g., TCGA) maps recurrent mutations across cancer types. **Drivers vs passengers** are distinguished statistically: drivers show **mutation recurrence above the background mutation rate** (MutSigCV-type models correcting for gene length, replication timing, and context), **selection signatures** (elevated nonsynonymous/synonymous or clustering at hotspots), and functional/pathway enrichment; passengers are random by-product mutations consistent with background. The judgment that driver discovery has not translated easily into therapy follows because many drivers are **tumor-suppressor losses or "undruggable" proteins** (e.g., TP53, RAS until recently, transcription factors) lacking enzymatic pockets, and tumor heterogeneity/resistance limits single-target success. What would change the conclusion: new modalities (degraders, covalent KRAS inhibitors, synthetic lethality) making previously undruggable drivers tractable. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
24. Synthetic chromosomes have been designed and built in yeast (Sc2.0, synthetic chromosome project). Evaluate the design principles (removal of transposons, recombination tags added, inducible evolution mode via SCRaMbLE), and discuss whether a fully synthetic human chromosome could be built and what it would require.

<!-- SOLUTION
**Answer (Q24, Synthesis).** Sc2.0 redesigns yeast chromosomes with defined principles: **removal of destabilizing/repetitive elements** (transposons, introns, redundant tRNA genes relocated), **synonymous recoding** (e.g., recoding stop codons to free a codon), insertion of **loxPsym recombination tags** at non-essential 3' ends to enable **SCRaMbLE** (Cre-induced inducible genome rearrangement for accelerated, controllable evolution), and watermarks/PCRTags for tracking — yielding a streamlined, programmable genome. The causal logic: design choices → reduced genome instability and a built-in diversification tool → a viable, evolvable synthetic eukaryotic chromosome. A fully synthetic **human** chromosome is far harder: it would require accurate megabase synthesis and assembly, functional **centromeres, telomeres, and origins**, correct large-scale 3D chromatin/epigenetic regulation, and stable mitotic segregation — currently beyond reach and raising serious safety/ethical constraints. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Transposons in the germline are silenced by piRNAs (PIWI-interacting RNAs). The piRNA pathway (PIWI proteins, ping-pong amplification) produces a feed-forward silencing loop. Evaluate: (a) how piRNAs recognize transposons without classical Watson-Crick base pairing; (b) why depletion of PIWI proteins causes germline transposon mobilization and infertility in mice; (c) whether piRNAs can also target non-transposon mRNAs.

<!-- SOLUTION
**Answer (Q25, Synthesis).** **(a)** piRNAs (~24–31 nt, PIWI-bound, Dicer-independent) recognize transposons by **sequence complementarity to transposon transcripts**, but tolerance for mismatches plus an amplifying "**ping-pong**" cycle (sense and antisense piRNAs reciprocally guiding cleavage) lets the system target diverse, mutating transposons rather than requiring exact Watson–Crick matching of a fixed siRNA. **(b)** Loss of PIWI proteins (e.g., MILI/MIWI/MIWI2 knockouts) **derepresses transposons in the germline**, causing insertional mutagenesis, DNA damage, meiotic arrest, and **infertility/sterility** — showing piRNA silencing is essential for genome integrity in germ cells. **(c)** Beyond transposons, piRNAs can also target some **non-transposon mRNAs** (regulating their stability/translation, e.g., during spermiogenesis), indicating a broader post-transcriptional regulatory role. What would change this view: evidence that observed mRNA effects are indirect consequences of transposon derepression rather than direct piRNA targeting. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Precision oncology based on tumor sequencing identifies actionable mutations. However, intratumoral heterogeneity (ITH) means that some cells within the tumor may lack the targeted mutation. Evaluate: (a) how clonal vs subclonal mutations are distinguished by variant allele frequency; (b) why targeting a clonal mutation (present in most cells) is more likely to be effective; (c) how liquid biopsy (circulating tumor DNA, ctDNA) can detect resistance mechanisms before clinical progression.

<!-- SOLUTION
**Answer (Q26, Synthesis).** The causal chain: tumor sequencing finds actionable mutations, but **intratumoral heterogeneity** means a targeted mutation may be present in only a subset of cells, so therapy spares non-carrying clones and resistance emerges. **(a)** Clonal vs subclonal mutations are distinguished by **variant allele frequency (VAF)** adjusted for tumor purity and copy number: **clonal** mutations (in all cancer cells) cluster near the expected fully-penetrant VAF, whereas **subclonal** mutations show lower VAF (present in a fraction of cells). **(b)** Targeting a **clonal** mutation is more likely effective because every tumor cell carries it, so no pre-existing escape population is spared; targeting a subclonal driver leaves resistant clones to expand. **(c)** **Liquid biopsy (ctDNA)** non-invasively samples tumor-derived DNA from blood, so emerging **resistance mutations** (e.g., EGFR T790M) can be detected as rising ctDNA fractions **before radiographic/clinical progression**, enabling earlier therapy switching. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. Evaluate whether "de-extinction" (reviving extinct species via CRISPR genome editing of a close relative) is scientifically feasible for: (a) the woolly mammoth (editing *Loxodonta africana* genome ~50 key cold-adaptation genes); (b) the passenger pigeon (*Ectopistes migratorius*, using band-tailed pigeon as template). What are the ecological risks of reintroducing de-extinct animals?

<!-- SOLUTION
**Answer (Q27, Synthesis).** Empirically, **de-extinction by CRISPR** does not literally resurrect an extinct species; it edits a close living relative toward the extinct phenotype. **(a)** For the woolly mammoth, ~50 cold-adaptation genes (hemoglobin, hair, fat, *TRPV3*) can be edited into the **Asian elephant (*Elephas maximus*, not *Loxodonta*)** genome, but a viable animal requires solving elephant cloning/artificial-womb gestation and integrating many edits — partial feasibility at best, yielding a cold-tolerant elephant hybrid, not a true mammoth. **(b)** The passenger pigeon (*Ectopistes migratorius*) using band-tailed pigeon as template faces the same limits plus avian cloning being unsolved. The judgment of limited feasibility rests on incomplete ancient genomes, polygenic phenotypes, and reproductive-technology gaps. **Ecological risks:** disrupted modern ecosystems, disease introduction, no surviving social/migratory learning, and diversion of conservation resources. What would change it: solved reproductive cloning and complete, high-quality ancient genomes. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
28. Retroviral integration (HIV integrates into host genome) is both a challenge for cure research and a tool for gene therapy vectors. Evaluate the "semi-random" integration pattern of HIV (preference for active transcription units) and how this differs from AAV (predominantly episomal in non-dividing cells, rare integration at AAVS1 safe harbor). Why does insertional mutagenesis risk differ between retroviral and AAV gene therapies?

<!-- SOLUTION
**Answer (Q28, Synthesis).** The causal logic links integration site to genotoxic risk. **HIV (lentivirus)** integrates **semi-randomly but preferentially into actively transcribed gene bodies** (LEDGF/p75-tethered), so a therapeutic lentiviral vector can insert within or near active genes, with some risk of dysregulating them. **AAV** is predominantly **episomal in non-dividing cells**, with only rare integration (occasionally at the **AAVS1** "safe harbor"), so it persists largely without altering host loci. Therefore **insertional-mutagenesis risk is higher for integrating retro/lentiviral vectors** (historically causing leukemia in early SCID-X1 gamma-retroviral trials due to enhancer activation of *LMO2*) than for AAV, whose mainly non-integrating biology limits oncogene activation but trades off durability (episome loss in dividing cells). What would change this: modified vectors (SIN-LTR, insulators, targeted integration) substantially lowering retroviral genotoxicity. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
29. tRNA suppressors can read through stop codons, restoring protein production from genes with premature stop mutations. Evaluate the therapeutic use of aminoglycoside antibiotics (gentamicin) as readthrough agents for nonsense mutations (e.g., in *Dystrophin*) — what are the molecular mechanisms, the challenges of specificity (also read through normal stop codons), and the clinical results to date?

<!-- SOLUTION
**Answer (Q29, Synthesis).** The mechanism: **suppressor/readthrough** allows a near-cognate aminoacyl-tRNA to be inserted at a **premature stop codon**, restoring full-length protein. **Aminoglycosides (gentamicin, and the designed agent ataluren/PTC124)** bind the ribosomal decoding (A) site, reducing fidelity so a sense amino acid is incorporated at a PTC, producing some functional **dystrophin** in nonsense-mutation Duchenne. **Specificity challenge:** the ribosome cannot distinguish a premature from a normal stop codon, so readthrough of **legitimate stop codons** risks C-terminally extended aberrant proteins and toxicity; efficiency is also low and context-dependent (PTC identity and surrounding sequence). **Clinical results to date:** effects have been **modest and inconsistent** — ataluren showed marginal/equivocal benefit (conditional EU approval, not FDA-approved), and aminoglycoside toxicity (oto-/nephrotoxicity) limits chronic use. Outcome would change with non-toxic, PTC-selective readthrough drugs. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
30. Critically evaluate the technical and ethical implications of building a "minimal synthetic cell" with a fully defined genome (as in the Venter Institute's JCVI-syn3.0, ~473 genes). What does the set of essential genes reveal about the minimal requirements for cellular life? If this minimal genome could be commercially manufactured and sold, what biosafety and biosecurity regulations should apply?

<!-- SOLUTION
**Answer (Q30, Synthesis).** Empirically, JCVI-syn3.0 (Venter Institute) is a chemically synthesized, transplanted minimal *Mycoplasma* genome of **~473 genes** that supports self-replication. The set of essential genes shows that minimal cellular life still requires the core processes — **genome replication, transcription, translation, membrane/lipid biogenesis, and basic metabolism** — yet ~**149 essential genes still have unknown function**, revealing that we do not fully understand even a minimal cell. The judgment that this is profound but bounded follows: it defines a lower bound on life's genetic complexity without claiming we can yet design genomes from first principles. **Biosafety/biosecurity:** commercial minimal cells would need DNA-synthesis screening, containment and engineered biocontainment (kill switches, auxotrophy), licensing/traceability, dual-use review, and international oversight. What would change the assessment: a minimal genome whose every gene's function is known and that is provably non-viable outside controlled conditions. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->
