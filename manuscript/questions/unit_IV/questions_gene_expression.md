# Questions — Gene Expression — Transcription and Translation {.unnumbered}

\label{sec:q_unit_IV_gene_expression}

<!-- question-coverage-start -->
## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Translate or annotate a sequence and explain how a regulatory change alters output.
- **Model/data emphasis:** Reading-frame, codon, and expression-output calculations.
- **Assessment alignment:** Concept Explanation, Questions and Methods, Argumentation.
- **Misconception probe:** A gene is not simply a protein recipe; context controls when, where, and how much product appears.
- **Transfer product:** Apply expression logic to mutations, biotechnology, development, and disease diagnostics.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.
<!-- question-coverage-end -->

## Questions 1–10: Recall and Comprehension {.unnumbered}

*This activity accompanies \cref{sec:unit_IV_gene_expression} of the textbook — review that chapter before attempting the exercises below.*

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define gene expression. What are the two major steps?

<!-- SOLUTION
**Answer (Q1, Recall).** Gene expression is the process by which the information in a gene is used to synthesize a functional product, usually a protein. Its two major steps are **transcription** (DNA copied into a complementary mRNA by RNA polymerase in the nucleus) and **translation** (the mRNA decoded by ribosomes into a polypeptide in the cytoplasm). In eukaryotes these are separated in space and time, allowing extensive regulation (RNA processing, transport, stability) between the steps. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. Describe the structure of a eukaryotic mRNA from 5' to 3', including most regulatory elements.

<!-- SOLUTION
**Answer (Q2, Recall).** From 5' → 3': **(1) m⁷G cap** — 7-methylguanosine joined via an unusual 5'→5' triphosphate linkage, added co-transcriptionally by capping enzyme; protects from 5'→3' exonucleases (Xrn1) and is the binding site for **eIF4E**, the rate-limiting step of cap-dependent translation initiation. **(2) 5' UTR** — typically 100–200 nt; contains Kozak context (GCCRCC**AUG**G) and sometimes upstream ORFs (uORFs) or **IRES** elements for regulated translation. **(3) CDS (coding sequence)** — begins at the start codon (AUG), proceeds in triplets to a stop codon (UAA/UAG/UGA); no introns (those were removed by the spliceosome, leaving exon-exon junctions marked by the **EJC**, which triggers NMD if a stop codon appears >50 nt upstream of a junction). **(4) 3' UTR** — typically 500–2000 nt; contains **AU-rich elements (AREs)** for mRNA stability, **miRNA binding sites**, and the polyadenylation signal **AAUAAA**. **(5) Poly-A tail** — 150–250 nt of adenosines, bound by **PABPC1**, which circularises the mRNA via eIF4G–eIF4E to promote re-initiation. Worked example: β-globin mRNA is ~620 nt (5' UTR 50, CDS 441, 3' UTR 131) plus cap and ~150 nt poly-A tail. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
3. What is the role of RNA polymerase II in transcription? Where does it bind?

<!-- SOLUTION
**Answer (Q3, Recall).** RNA polymerase II is the enzyme that synthesizes all messenger RNA (and many small RNAs) in eukaryotes, building a complementary RNA copy of the template DNA strand 5'→3'. It does not bind DNA on its own: it is recruited to the **core promoter** (the region around the transcription start site, e.g. the TATA box ~25 bp upstream) as part of the preinitiation complex assembled by general transcription factors (TFIIA–H). Its C-terminal domain (CTD) is phosphorylated to coordinate capping, splicing, and polyadenylation during elongation. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
4. Define a transcription factor. Distinguish general vs specific transcription factors.

<!-- SOLUTION
**Answer (Q4, Recall).** A transcription factor is a protein that binds specific DNA sequences and regulates the rate of transcription. **General (basal) transcription factors** (TFIIA, B, D, E, F, H) are required at every Pol II promoter to position the polymerase and form the preinitiation complex — they set the baseline. **Specific (regulatory) transcription factors** bind enhancers or silencers of particular genes and increase or decrease expression in a gene-, cell-, or signal-dependent way. The mechanistic difference: general factors enable transcription at all; specific factors decide which genes are transcribed and how much. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
5. What is RNA splicing? What molecular machinery performs it?

<!-- SOLUTION
**Answer (Q5, Recall).** RNA splicing is the removal of non-coding **introns** from pre-mRNA and the joining of the flanking **exons** to produce a mature, translatable mRNA. It is carried out by the **spliceosome**, a large ribonucleoprotein complex of five small nuclear RNPs (U1, U2, U4, U5, U6 snRNPs) plus associated proteins. The snRNAs recognize the 5' splice site (GU), branch-point adenosine, and 3' splice site (AG) and catalyze two transesterification reactions that excise the intron as a lariat. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
6. Define the genetic code. What is a codon? How many codons encode amino acids?

<!-- SOLUTION
**Answer (Q6, Recall).** The genetic code is the set of rules by which nucleotide triplets in mRNA specify amino acids during translation. A **codon** is a sequence of three consecutive nucleotides read by the ribosome. There are $4^3 = 64$ codons total: **61 encode the 20 amino acids** (the code is therefore degenerate/redundant) and **3 are stop codons** (UAA, UAG, UGA). AUG is the start codon and also encodes methionine. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
7. What is the ribosome composed of? Name the three ribosomal sites (A, P, E sites).

<!-- SOLUTION
**Answer (Q7, Recall).** The ribosome is a ribonucleoprotein machine made of **ribosomal RNA (rRNA) and ribosomal proteins**, organized into a small subunit (40S in eukaryotes; reads the mRNA) and a large subunit (60S; catalyzes peptide-bond formation via the rRNA peptidyl transferase center). It has three tRNA-binding sites: the **A site** (Aminoacyl — accepts the incoming aminoacyl-tRNA), the **P site** (Peptidyl — holds the tRNA bearing the growing chain), and the **E site** (Exit — holds the deacylated tRNA before it leaves). See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
8. Describe initiation, elongation, and termination of translation in eukaryotes.

<!-- SOLUTION
**Answer (Q8, Recall).** **Initiation:** the 40S subunit, with initiator Met-tRNAi and initiation factors (eIF4E binds the m⁷G cap), scans the mRNA 5'→3' to the first AUG in good Kozak context; the 60S subunit then joins to form the 80S ribosome. **Elongation:** aminoacyl-tRNAs are delivered to the A site by eEF1A; the peptidyl transferase center forms the peptide bond; eEF2 drives translocation, shifting tRNAs A→P→E one codon at a time. **Termination:** a stop codon enters the A site, recognized by release factor eRF1, which triggers hydrolysis and release of the completed polypeptide, then ribosome recycling. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. What is tRNA? What is the anticodon, and what is aminoacyl-tRNA synthetase?

<!-- SOLUTION
**Answer (Q9, Recall).** tRNA (transfer RNA) is a small (~76 nt) cloverleaf-folded RNA that physically links a codon to its amino acid during translation. The **anticodon** is a three-nucleotide loop that base-pairs antiparallel with the complementary mRNA codon in the ribosomal A site. **Aminoacyl-tRNA synthetases** are enzymes (one per amino acid) that covalently attach the correct amino acid to the 3' CCA end of its cognate tRNA, using ATP; their proofreading establishes the accuracy of the genetic code ("the second genetic code"). See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO10; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
10. What is the wobble hypothesis? Which position of the codon allows degeneracy?

<!-- SOLUTION
**Answer (Q10, Recall).** The **wobble hypothesis** (Crick, 1966) states that base pairing between the third base of the codon and the first base of the anticodon is less stringent than standard Watson–Crick pairing, so a single tRNA can read several synonymous codons. The **third (3') codon position** allows this degeneracy: non-standard pairings (e.g., G–U, or inosine in the anticodon pairing with U, C, or A) let ~45 tRNAs decode all 61 sense codons, explaining the code's redundancy. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->

## Questions 11–20: Application and Analysis {.unnumbered}

<!-- assess: LO=LO1; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
11. Pre-mRNA splicing must be precise to within one nucleotide. Explain the two-step transesterification mechanism of splicing and the role of branch point A, 5' splice site, and 3' splice site in spliceosome assembly.

<!-- SOLUTION
**Answer (Q11, Application).** Splicing proceeds by **two sequential transesterification reactions**. First, the 2'-OH of the **branch-point adenosine** attacks the phosphate at the **5' splice site (GU)**, cleaving exon 1 and forming a lariat intermediate. Second, the freed 3'-OH of exon 1 attacks the **3' splice site (AG)**, joining the two exons and releasing the intron as a lariat. Spliceosome assembly recognizes these elements stepwise: U1 snRNP base-pairs the 5' splice site, U2 snRNP binds the branch point (bulging the branch A), and the U4/U6·U5 tri-snRNP completes the catalytic core — the one-nucleotide precision comes from this combinatorial recognition of all three signals. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
12. Alternative splicing generates multiple protein isoforms from one gene. *Drosophila Dscam* gene can produce >38,000 isoforms through mutually exclusive exon splicing. Explain: (a) the general mechanism of alternative splicing; (b) why *Dscam* diversity is important for axon guidance in neural wiring; (c) one human disease caused by aberrant alternative splicing.

<!-- SOLUTION
**Answer (Q12, Application).** **(a)** Alternative splicing includes or excludes particular exons (or uses alternative 5'/3' splice sites) in a regulated way, so one gene yields multiple mRNAs and protein isoforms; in *Dscam*, mutually exclusive selection among large clusters of variant exons combinatorially generates >38,000 isoforms. **(b)** This diversity gives each neuron a near-unique Dscam "identity tag"; isoform-specific homophilic binding mediates **self-avoidance**, so a neuron's own branches repel each other while still tiling among other neurons — essential for correct axon/dendrite wiring. **(c)** Spinal muscular atrophy is caused by aberrant *SMN2* exon 7 splicing (the therapy nusinersen corrects it); other examples include myotonic dystrophy and many cancers. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
13. The 5' cap (m⁷G) and poly-A tail of eukaryotic mRNA serve similar functions — protecting mRNA from exonuclease attack and promoting translation initiation. Explain: (a) how the 5' cap is added; (b) how eIF4E binding to the cap recruits the 43S pre-initiation complex; (c) why some viruses (e.g., poliovirus) cleave eIF4G to direct ribosomes to IRES sequences instead.

<!-- SOLUTION
**Answer (Q13, Application).** **(a) 5' cap addition** occurs co-transcriptionally when nascent pre-mRNA is ~25 nt long: (i) RNA 5'-triphosphatase removes the γ-phosphate; (ii) guanylyltransferase adds GMP via a unique **5'–5' triphosphate bridge**; (iii) guanine-N7-methyltransferase methylates N7 of the guanine, yielding **m⁷GpppN**. The capping enzyme is recruited via the phosphorylated CTD (Ser5-P) of RNA pol II — physically linking transcription to capping. **(b) eIF4E binding**: cytosolic **eIF4E** recognises m⁷G via stacking with two conserved tryptophans (W56, W102), with K_d ≈ 100 nM. eIF4E forms eIF4F with **eIF4G (scaffold) and eIF4A (DEAD-box helicase)**; eIF4G simultaneously binds **PABPC1 on the poly-A tail** (circularising the mRNA) and recruits the **43S PIC** (40S + eIF1, eIF1A, eIF3, eIF2-GTP-Met-tRNAi) via eIF3. The 43S then scans 5' → 3' using eIF4A's ATP-dependent helicase activity until it finds the Kozak AUG. **(c) Poliovirus hijack**: poliovirus 2A protease **cleaves eIF4G** between the eIF4E-binding domain and the eIF3/eIF4A-binding domain. This shuts down **cap-dependent translation** of host mRNA but leaves intact the C-terminal half of eIF4G that binds viral **IRES** (internal ribosome entry site) in the 5' UTR of poliovirus RNA — so viral translation continues while host translation collapses. This is why the cell "looks infected" within hours: host protein synthesis drops > 90 %. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
14. The ribosome proof-reads aminoacyl-tRNA selection at the A site. Explain: (a) initial selection based on codon-anticodon base pairing (induced fit); (b) proofreading step (kinetokinetics — GTPase activation primarily if correct aa-tRNA is bound); (c) why errors occur at ~1 in 10,000 vs DNA polymerase errors of 1 in 10⁹ (why is translation less accurate?).

<!-- SOLUTION
**Answer (Q14, Application).** **(a) Initial selection:** the ternary complex (eEF1A·GTP·aa-tRNA) samples the A-site codon; correct Watson–Crick codon–anticodon pairing induces a conformational closure of the 30S/40S decoding center (induced fit) that accelerates GTPase activation. **(b) Proofreading:** GTP is hydrolyzed only when pairing is correct; after hydrolysis the tRNA must be "accommodated" into the peptidyl transferase center — a second checkpoint where near-cognate tRNAs preferentially dissociate before peptide-bond formation. **(c)** Translation tolerates a higher error rate (~10⁻⁴) than DNA replication (~10⁻⁹) because protein errors affect only one short-lived molecule and are not heritable, whereas DNA errors are passed to all descendants; selection therefore optimized replication fidelity far more strongly than translation, and a faster, less accurate ribosome favors growth. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
15. Cycloheximide blocks the elongation step of eukaryotic translation (not prokaryotic), because it specifically inhibits the 60S subunit translocation step. Explain: (a) what translocation means mechanistically; (b) why prokaryotic ribosomes (70S) are not blocked; (c) how this selectivity is exploited in laboratory cell biology experiments.

<!-- SOLUTION
**Answer (Q15, Application).** **(a) Translocation** is the eEF2-driven, GTP-dependent movement of the ribosome by exactly one codon along the mRNA after peptide-bond formation, shifting the tRNAs from A→P and P→E sites and opening the A site for the next aminoacyl-tRNA. **(b)** Cycloheximide binds the **E site of the 60S subunit**, blocking eEF2-mediated translocation; prokaryotic 70S ribosomes have structurally distinct large-subunit rRNA/proteins that cycloheximide does not recognize, so bacterial translation is unaffected. **(c)** This eukaryote-specific, rapid, reversible arrest is exploited to **freeze ribosomes on mRNA** — e.g., to stabilize polysomes for polysome profiling and ribosome profiling (Ribo-seq), and to halt protein synthesis in pulse-chase and cytotoxicity experiments. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. Nonsense-mediated mRNA decay (NMD) degrades mRNAs with premature stop codons. Explain: (a) how the cell recognises a premature vs normal stop codon (role of exon-junction complexes); (b) the UPF1/SMG cascade; (c) why NMD is a quality control mechanism that also regulates normal gene expression for ~10% of genes.

<!-- SOLUTION
**Answer (Q16, Application).** **(a)** During the pioneer round of translation the ribosome displaces exon-junction complexes (EJCs). A stop codon is judged **premature if an EJC remains >50–55 nt downstream of it** (a normal stop is the last codon, with no downstream EJC). **(b)** The retained EJC recruits **UPF1**, which is phosphorylated by SMG1; phospho-UPF1 then recruits SMG5/6/7, triggering endonucleolytic cleavage (SMG6) and exonucleolytic decay of the transcript. **(c)** NMD is both quality control — destroying truncating-mutation and error-prone transcripts to prevent dominant-negative truncated proteins — and a normal regulatory mechanism: ~10% of transcripts (including alternatively spliced isoforms with PTC-containing exons and autoregulated splicing-factor mRNAs) are physiologically tuned by NMD. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. Polyribosomes (polysomes) consist of multiple ribosomes simultaneously translating the same mRNA. If a 1,500-nt coding sequence is occupied by ribosomes spaced on average every 80 nt, how many ribosomes are simultaneously translating this mRNA? Calculate the rate of protein synthesis per mRNA if each ribosome adds 2 amino acids/sec.

<!-- SOLUTION
**Answer (Q17, Application).** Ribosome count: $N = \dfrac{1500\ \mathrm{nt}}{80\ \mathrm{nt/ribosome}} = \mathbf{18.75 \approx 19\ \mathrm{ribosomes}}$ simultaneously engaged. Protein output: each ribosome adds 2 aa/s → 19 × 2 = **38 amino acids per second** across the polysome. Time to complete one protein per ribosome: 1500 nt ÷ 3 = 500 codons ÷ 2 codons/s = **250 s ≈ 4 min**. Steady-state output per mRNA = 1 finished protein every (80 nt / 2 codons·s × 3 nt/codon) ≈ **13 s per completed chain**, i.e. ~280 proteins/h/mRNA. Biological sanity check: this matches measured translation rates in mammalian cells (median ~5 proteins/mRNA/min for short transcripts). Sucrose-gradient polysome profiles show β-actin mRNA (~1800 nt) in fractions containing 8–12 ribosomes — consistent with our estimate once you account for scanning delays and the fact that the first ~40 nt after the cap are typically bare (eIF4E/PABPC1 footprint). **Biological significance**: polysome occupancy (footprint density from ribosome profiling / Ribo-seq) is the gold-standard readout of translation efficiency; a 19-ribosome polysome represents high expression, while a monosome-enriched mRNA is either stalled or repressed. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. Internal ribosome entry sites (IRES) allow cap-independent translation initiation, used by viruses (Hepatitis C, poliovirus) and in cellular stress responses, when eIF4E activity is reduced. Compare IRES-mediated vs cap-dependent initiation: which cellular proteins are replaced by viral ITAF proteins, and under what stress conditions does cellular IRES-mediated translation occur?

<!-- SOLUTION
**Answer (Q18, Application).** **Cap-dependent** initiation requires eIF4E to bind the m⁷G cap, eIF4G as scaffold, eIF4A helicase, and 5' scanning to the AUG. **IRES-mediated** initiation uses a structured RNA element in the 5' UTR that recruits the 40S subunit directly, bypassing the cap. Viral IRESs replace cap-recognition factors with **IRES trans-acting factors (ITAFs)**: depending on IRES class, they need little or no eIF4E/eIF4G (e.g., the CrPV IRES needs no initiation factors; HCV recruits eIF3 and 40S directly; poliovirus uses a cleaved eIF4G fragment plus ITAFs such as PCBP2/PTB). Cellular IRESs are used when **cap-dependent translation is suppressed** — mitosis, hypoxia, ER/nutrient stress, apoptosis, and viral infection — to keep translating survival, stress, and pro-apoptotic mRNAs. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. The signal recognition particle (SRP) recognises hydrophobic signal peptides emerging from ribosomes translating secretory proteins. Explain: (a) how SRP stalls translation while targeting the ribosome to the rough ER; (b) how signal peptidase cleaves the signal peptide in the ER lumen; (c) what happens to cytosolic misfolded proteins lacking a signal peptide vs ER-targeted ones.

<!-- SOLUTION
**Answer (Q19, Application).** **(a)** As a hydrophobic signal peptide emerges from the ribosome, the **signal recognition particle (SRP)** binds it and contacts the ribosome, **pausing elongation**; SRP then docks the ribosome onto the SRP receptor at the rough ER, transferring it to the Sec61 translocon, after which translation resumes and the chain is threaded into the ER. **(b)** Inside the ER lumen, **signal peptidase** cleaves the signal sequence from the nascent chain, releasing the mature protein into the lumen for folding and modification. **(c)** ER-targeted proteins that misfold are detected by ER quality control and retro-translocated for **ERAD** (ER-associated degradation by the cytosolic proteasome); cytosolic proteins lacking a signal peptide that misfold are handled by cytosolic chaperones and the **ubiquitin–proteasome system** (or autophagy), never entering the secretory pathway. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO10; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. Transcription factors bind specific DNA sequences (motifs). A transcriptional activator contains a DNA-binding domain (DBD) and an activation domain (AD). Explain: (a) what structural motifs are common in DBDs (zinc finger, helix-turn-helix, leucine zipper); (b) how the activation domain recruits the Mediator complex; (c) how enhancers (located kb away from promoters) loop to contact the preinitiation complex through cohesin-mediated chromosome looping.

<!-- SOLUTION
**Answer (Q20, Application).** **(a)** Common DNA-binding domains include the **zinc finger** (Cys₂His₂ fingers inserting an α-helix into the major groove), the **helix-turn-helix / homeodomain**, and the **basic leucine zipper (bZIP)** and basic helix-loop-helix, which dimerize and grip DNA with basic regions. **(b)** The separate **activation domain** does not bind DNA; it recruits coactivators and the **Mediator complex**, which bridges the enhancer-bound activator to RNA Pol II and the general transcription factors, stimulating preinitiation-complex assembly and CTD phosphorylation. **(c)** Distal enhancers contact promoters through **chromatin looping**: cohesin and CTCF organize loop domains (TADs), bringing the enhancer-bound activator/Mediator into physical proximity with the promoter even when they are tens of kb apart in linear sequence. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->

## Questions 21–30: Synthesis and Evaluation {.unnumbered}

<!-- assess: LO=LO1; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
21. Evaluate the dual role of SR proteins (serine-arginine-rich splicing factors) in both constitutive and alternative splicing and mRNA export. What does the dual role of SR proteins reveal about the evolutionary coupling between nuclear RNA processing and cytoplasmic translation?

<!-- SOLUTION
**Answer (Q21, Synthesis).** Empirically, SR proteins bind exonic splicing enhancers to promote spliceosome assembly and regulate alternative splice-site choice, *and* they remain bound to the spliced mRNP where they help recruit the TREX export machinery (e.g., via NXF1/TAP) and influence cytoplasmic translation efficiency. The judgment — that nuclear processing and cytoplasmic fate are evolutionarily coupled — follows because the same factor physically links splicing, export, and translation, making them a coordinated pipeline rather than independent steps; this "mRNP marking" also explains why spliced mRNAs are translated more efficiently than intronless ones. What would change the conclusion: showing SR-protein splicing and export functions are genetically separable (separation-of-function mutants), or that export/translation enhancement occurs equally without SR deposition. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
22. Design a comprehensive experiment to map most enhancers controlling a specific gene in a given cell type using: (a) H3K27ac ChIP-seq (active enhancer mark); (b) ATAC-seq (open chromatin); (c) HiC chromatin conformation capture; (d) CRISPR deletion of candidate enhancers and transcriptional output measurement. How would you prioritise which enhancers are most important?

<!-- SOLUTION
**Answer (Q22, Synthesis).** **Hypothesis:** a defined set of distal enhancers drives the gene's expression in this cell type. **Design:** map candidates with H3K27ac ChIP-seq (active enhancers) and ATAC-seq (open chromatin), then use Hi-C/capture Hi-C to identify which open, acetylated regions physically loop to the promoter; the **control/comparison** is an unedited population and CRISPRi/CRISPR deletion of each candidate vs a scrambled-gRNA control. **Measured outcome:** target-gene mRNA (RT-qPCR/RNA-seq) after each perturbation, with biological replicates. **Prioritization:** rank enhancers by (i) magnitude of expression loss on deletion, (ii) strength of the Hi-C contact with the promoter, (iii) H3K27ac/ATAC signal and conservation, and (iv) presence of relevant TF motifs/footprints. A **falsifying result**: deleting the top-ranked enhancer leaves expression unchanged, indicating redundancy or that the causal element was missed. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
23. The "RNA world" hypothesis proposes that early life was based on RNA molecules that could both carry genetic information and catalyse reactions. Evaluate: (a) the evidence supporting RNA world (ribozymes, ribosome as a ribozyme, universality of the genetic code); (b) the transition from RNA world to the DNA-protein world; (c) what modern ribozymes tell us about the chemistry of early catalysis.

<!-- SOLUTION
**Answer (Q23, Synthesis).** Empirical support for an RNA world: **ribozymes** (self-splicing introns, RNase P) prove RNA can catalyze chemistry; the **ribosome's peptidyl transferase center is all rRNA** (a ribozyme), implying protein synthesis predates protein enzymes; and the near-**universal genetic code** plus RNA cofactors (ATP, NAD, coenzyme A) look like molecular fossils. The judgment that an RNA world existed rests on these as evidence that RNA once carried both information and catalysis. The transition to DNA/protein: DNA (more chemically stable, proofreadable) took over information storage and proteins (20 side chains) took over catalysis, with RNA retained as the intermediary. What would weaken it: failure to demonstrate an RNA replicase ribozyme, or evidence that early metabolism was peptide- or metabolism-first rather than RNA-based. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
24. Transcription and translation are physically coupled in prokaryotes (translation begins before transcription is complete). Evaluate the consequences of this coupling: how does it allow attenuation (regulation of transcription termination by ribosome speed), and why would coupling like this have evolved in prokaryotes but not eukaryotes (where transcription and translation are spatially separated)?

<!-- SOLUTION
**Answer (Q24, Synthesis).** In prokaryotes there is no nuclear envelope, so ribosomes load onto an mRNA's 5' end while RNA polymerase is still transcribing it (coupling). This enables **attenuation**, e.g. the *trp* operon: a ribosome translating a leader peptide rich in Trp codons stalls or proceeds depending on tryptophan availability; its position determines which alternative RNA hairpin forms, either a terminator (transcription stops) or an antiterminator (transcription continues) — ribosome speed directly controls transcription termination. This could not evolve in eukaryotes because transcription (nucleus) and translation (cytoplasm) are **spatially and temporally separated** by the nuclear envelope and by pre-mRNA processing, so a translating ribosome can never contact an actively transcribing polymerase; eukaryotes instead regulate via distinct mechanisms (chromatin, splicing, export, miRNAs). See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Ribosome biogenesis occurs in the nucleolus and is rate-limiting for cell growth. Evaluate the regulatory relationship between mTORC1, Pol I transcription of rDNA, and ribosome biogenesis. Why does mTOR inhibition suppress cell growth even in cells with unlimited amino acid supply?

<!-- SOLUTION
**Answer (Q25, Synthesis).** Ribosome biogenesis (rDNA transcription by Pol I, rRNA processing, assembly in the nucleolus) consumes most of a growing cell's transcriptional output and is rate-limiting for proliferation. **mTORC1** integrates growth-factor and nutrient signals and directly stimulates ribosome production: it activates Pol I (via TIF-IA/UBF), Pol III (5S rRNA, tRNA, via Maf1 repression), and translation of ribosomal-protein mRNAs (via S6K1 and 4E-BP1). Therefore mTOR inhibition (rapamycin) suppresses growth **even with abundant amino acids** because it shuts down the biosynthetic capacity needed to make new ribosomes — without enough ribosomes the cell cannot increase mass or divide, regardless of substrate supply. The evidence: rapamycin rapidly reduces nucleolar size, 45S pre-rRNA, and polysome levels. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Evaluate the molecular mechanism of translation by the ribosome in the context of the "peptidyl transferase" ribosome activity: specifically, is the catalysis chemical (RNA catalysis) or entropic (positioning effect)? Cite the key experiment (Nobel Prize 2009) that settled this debate.

<!-- SOLUTION
**Answer (Q26, Synthesis).** The empirical question is whether peptide-bond catalysis is chemical (rRNA acting as a true catalyst) or mainly **entropic** (the ribosome positioning/orienting substrates and excluding water, with little chemical transition-state stabilization). The decisive evidence is the **atomic-resolution crystal structures of the 50S subunit (Steitz, Moore; Nobel Prize in Chemistry 2009, shared with Ramakrishnan and Yonath)**: the peptidyl transferase center is composed entirely of 23S rRNA with no protein side chains near the active site, and subsequent biochemistry showed catalysis works largely by **substrate positioning and proton shuttling/entropic effects** rather than classical acid–base chemistry. So the ribosome is a ribozyme, and its catalysis is predominantly proximity/orientation-based. What would overturn this: finding a protein side chain essential for the chemical step, or a single-atom rRNA substitution that abolishes chemistry without affecting positioning. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. Single-molecule translation experiments using fluorescently labelled ribosomes and mRNAs have revealed "pausing" during elongation opposite rare codons, and "synchronised" waves of ribosome density on mRNA. Evaluate what these observations reveal about codon usage optimisation and how synonymous mutations (same amino acid, different codon) can dramatically affect protein folding by altering translation speed.

<!-- SOLUTION
**Answer (Q27, Synthesis).** Single-molecule and ribosome-profiling data show that elongation is non-uniform: ribosomes **pause at rare codons** (those read by low-abundance tRNAs) and move in correlated waves. The causal chain: a synonymous ("silent") mutation changes codon usage → alters local tRNA-decoding speed → changes the elongation rate at that position → shifts the timing of **co-translational folding**, so domains may misfold or be processed differently even though the amino-acid sequence is unchanged. This reveals that codon choice is itself an optimized layer of information (translational kinetics), not redundant: examples include the *MDR1* C3435T synonymous variant altering substrate specificity and synonymous changes affecting protein stability and aggregation. The interpretation: codon usage co-evolves with folding pathways; "silent" mutations can be functionally consequential. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
28. Design a gene therapy strategy for a patient with haemophilia A (lacking factor VIII). Compare: mRNA therapy (synthetic mRNA with pseudo-uridine modification for stability); AAV vector gene therapy (liver-tropism, long-term expression); and base editing (correct the point mutation in situ). Evaluate the trade-offs in immunogenicity, duration of effect, and delivery efficiency.

<!-- SOLUTION
**Answer (Q28, Synthesis).** **Hypothesis/options compared:** (1) **mRNA therapy** — pseudouridine-modified synthetic factor VIII mRNA in lipid nanoparticles: easy to redose, low genotoxicity, but **transient** expression and innate-immune/LNP delivery limits. (2) **AAV gene therapy** — liver-tropic AAV carrying B-domain-deleted F8: **long-lived** expression from a single dose, but pre-existing/induced anti-AAV immunity, payload-size limits, and episomal loss in dividing hepatocytes; one-time only. (3) **Base editing** — in-situ correction of the causal point mutation: potentially **permanent and physiologic** (native locus regulation), but constrained by editable mutation type, delivery to hepatocytes, and off-target/bystander risk. **Measured outcomes:** circulating FVIII activity, bleeding rate, anti-FVIII/anti-vector antibodies, durability. **Controls/falsification:** untreated and vehicle arms; the approach fails if FVIII activity does not rise above the ~5% therapeutic threshold or if immunogenicity neutralizes the product. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
29. RNA interference (RNAi) was discovered when dsRNA triggered gene silencing in *C. elegans* (Fire and Mello, 1998). Evaluate the mechanism (Dicer, RISC, Ago2-mediated cleavage), the evolutionary origin of RNAi (antiviral defence), and the clinical development of siRNA therapeutics (inclisiran for PCSK9 silencing). What advantages does siRNA have over antisense oligonucleotides (ASOs) for gene silencing?

<!-- SOLUTION
**Answer (Q29, Synthesis).** **Mechanism:** long dsRNA is cleaved by **Dicer** into ~21–23 nt siRNAs; one strand is loaded into **RISC** with **Ago2**, which uses perfect complementarity to **endonucleolytically cleave** the target mRNA. **Evolutionary origin:** RNAi arose as an **antiviral and anti-transposon defense** (recognizing dsRNA replication intermediates), conserved from plants and invertebrates to mammals. **Clinical:** chemically stabilized, GalNAc-conjugated siRNAs such as **inclisiran** silence hepatic *PCSK9*, durably lowering LDL cholesterol with twice-yearly dosing. **siRNA vs ASO advantages:** siRNA acts catalytically (one RISC degrades many mRNAs) giving high potency and long duration, exploits an endogenous enzymatic pathway, and (with GalNAc) achieves efficient liver delivery — whereas ASOs act stoichiometrically and generally need more frequent dosing for comparable knockdown. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO10; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
30. Critically evaluate the concept of the "central dogma" (DNA → RNA → protein). Identify three biological exceptions that violate a strict reading of the central dogma (reverse transcription, RNA editing, prion replication), explain their mechanisms, assess whether these exceptions require a fundamental revision of the central dogma, and state what RNAcentral-style database checks are needed before claiming that a non-coding RNA has a defined gene model and function.

<!-- SOLUTION
**Answer (Q30, Synthesis).** The central dogma states information flows DNA→RNA→protein and not back out of protein. Three classic challenges: **(1) Reverse transcription** — retroviruses/telomerase make DNA from RNA (RNA→DNA), expanding allowed information flow but not violating the core prohibition (no protein→nucleic-acid). **(2) RNA editing** — e.g., A-to-I (ADAR) or C-to-U (APOBEC) editing changes mRNA sequence after transcription, so the protein differs from the genomic template; this elaborates the RNA step rather than reversing flow. **(3) Prions** — a misfolded protein (PrP^Sc) templates conformational conversion of normal protein, transmitting *conformational*, not sequence, information protein→protein. **Assessment:** Crick's strict statement (no information from protein back to nucleic acid) survives — none of these transfers sequence from protein to DNA/RNA; they are **elaborations within the framework**, not a fundamental revision, though prions show heritable information can be protein-borne. Source-governed RNA interpretation then asks whether the RNAcentral entry is sequence-level or gene-level, which release and identifiers are being used, whether isoforms/splice variants are merged correctly, and whether literature links support function rather than only mention the RNA \citep{rnacentral2026}. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
