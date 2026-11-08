# Questions — Gene Expression {#sec:q_unit_IV_gene_expression .unnumbered}


## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Translate or annotate a sequence and explain how a regulatory change alters output.
- **Model/data emphasis:** Reading-frame, codon, and expression-output calculations.
- **Assessment alignment:** Concept Explanation, Questions and Methods, Argumentation.
- **Misconception probe:** A gene is not simply a protein recipe; context controls when, where, and how much product appears.
- **Transfer product:** Apply expression logic to mutations, biotechnology, development, and disease diagnostics.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.

## Questions 1–10: Core mechanisms {.unnumbered}

*This activity accompanies \cref{sec:unit_IV_gene_expression} of the textbook — review that chapter before attempting the exercises below.*

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define gene expression. What are the two major steps?

<!-- SOLUTION
**Answer (Q1, Recall).** Gene expression is the process by which the information in a gene is used to synthesize a functional product, usually a protein. Its two major steps are **transcription** (DNA copied into a complementary mRNA by RNA polymerase in the nucleus) and **translation** (the mRNA decoded by ribosomes into a polypeptide in the cytoplasm). In eukaryotes these are separated in space and time, allowing extensive regulation (RNA processing, transport, stability) between the steps. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. Describe the structure of a eukaryotic mRNA from 5' to 3', including most regulatory elements.

<!-- SOLUTION
**Answer (Q2, Recall).** From 5' → 3': **(1) m⁷G cap** — 7-methylguanosine joined via an unusual 5'→5' triphosphate linkage, added co-transcriptionally by capping enzyme; protects from 5'→3' exonucleases (Xrn1) and is the binding site for **eIF4E**, the rate-limiting step of cap-dependent translation initiation. **(2) 5' UTR** — typically 100–200 nt; contains Kozak context (GCCRCC**AUG**G) and sometimes upstream ORFs (uORFs) or **IRES** elements for regulated translation. **(3) CDS (coding sequence)** — begins at the start codon (AUG), proceeds in triplets to a stop codon (UAA/UAG/UGA); no introns (those were removed by the spliceosome, leaving exon-exon junctions marked by the **EJC**, which triggers NMD if a stop codon appears >50 nt upstream of a junction). **(4) 3' UTR** — typically 500–2000 nt; contains **AU-rich elements (AREs)** for mRNA stability, **miRNA binding sites**, and the polyadenylation signal **AAUAAA**. **(5) Poly-A tail** — 150–250 nt of adenosines, bound by **PABPC1**, which circularises the mRNA via eIF4G–eIF4E to promote re-initiation. Worked example: β-globin mRNA is ~620 nt (5' UTR 50, CDS 441, 3' UTR 131) plus cap and ~150 nt poly-A tail. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
3. Compare bacterial RNA polymerase/σ with eukaryotic Pol II/general TFs in promoter recognition, and distinguish Pol I/III functions.

<!-- SOLUTION
**Answer (Q3, Recall).** Bacterial σ confers promoter recognition on core polymerase; Pol II uses general TFs and Mediator at protein-coding and many noncoding transcription units. Pol I produces large rRNA precursors; Pol III produces tRNA and 5S rRNA. Award recruitment distinction and division of labor; polymerase does not interpret translation codons. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
4. Define a transcription factor. Distinguish general vs specific transcription factors.

<!-- SOLUTION
**Answer (Q4, Recall).** Transcription factors regulate transcription through DNA binding and/or interactions with other components. General factors support assembly and function of canonical Pol II preinitiation machinery; promoter and organism context can alter factor usage, so one fixed TFIIA/B/D/E/F/H inventory is not required identically at every promoter. In tested yeast, classical general factors were required while substantial transcription was TAF-independent \citep{petrenko2019pic}. Specific regulatory factors control particular genes in a cell- or signal-dependent manner, sometimes through partners rather than direct DNA binding. Award basal-machinery versus regulatory roles without an exceptionless definition. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
5. What is RNA splicing? What molecular machinery performs it?

<!-- SOLUTION
**Answer (Q5, Recall).** RNA splicing is the removal of non-coding **introns** from pre-mRNA and the joining of the flanking **exons** to produce a mature, translatable mRNA. It is carried out by the **spliceosome**, a large ribonucleoprotein complex of five small nuclear RNPs (U1, U2, U4, U5, U6 snRNPs) plus associated proteins. The snRNAs recognize the 5' splice site (GU), branch-point adenosine, and 3' splice site (AG) and catalyze two transesterification reactions that excise the intron as a lariat. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
6. Define the genetic code. What is a codon? How many codons encode amino acids?

<!-- SOLUTION
**Answer (Q6, Recall).** The genetic code is the set of rules by which nucleotide triplets in mRNA specify amino acids during translation. A **codon** is a sequence of three consecutive nucleotides read by the ribosome. There are $4^3 = 64$ codons total: **61 encode the 20 amino acids** (the code is therefore degenerate/redundant) and **3 are stop codons** (UAA, UAG, UGA). AUG is the start codon and also encodes methionine. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
7. What is the ribosome composed of? Name the three ribosomal sites (A, P, E sites).

<!-- SOLUTION
**Answer (Q7, Recall).** The ribosome is a ribonucleoprotein machine made of **ribosomal RNA (rRNA) and ribosomal proteins**, organized into a small subunit (40S in eukaryotes; reads the mRNA) and a large subunit (60S; catalyzes peptide-bond formation via the rRNA peptidyl transferase center). It has three tRNA-binding sites: the **A site** (Aminoacyl — accepts the incoming aminoacyl-tRNA), the **P site** (Peptidyl — holds the tRNA bearing the growing chain), and the **E site** (Exit — holds the deacylated tRNA before it leaves). See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
8. Describe initiation, elongation, and termination of translation in eukaryotes.

<!-- SOLUTION
**Answer (Q8, Recall).** **Initiation:** the 40S subunit, with initiator Met-tRNAi and initiation factors (eIF4E binds the m⁷G cap), scans the mRNA 5'→3' to the first AUG in good Kozak context; the 60S subunit then joins to form the 80S ribosome. **Elongation:** aminoacyl-tRNAs are delivered to the A site by eEF1A; the peptidyl transferase center forms the peptide bond; eEF2 drives translocation, shifting tRNAs A→P→E one codon at a time. **Termination:** a stop codon enters the A site, recognized by release factor eRF1, which triggers hydrolysis and release of the completed polypeptide, then ribosome recycling. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. What is tRNA? What is the anticodon, and what is aminoacyl-tRNA synthetase?

<!-- SOLUTION
**Answer (Q9, Recall).** tRNA (transfer RNA) is a small (~76 nt) cloverleaf-folded RNA that physically links a codon to its amino acid during translation. The **anticodon** is a three-nucleotide loop that base-pairs antiparallel with the complementary mRNA codon in the ribosomal A site. **Aminoacyl-tRNA synthetases** are enzymes (one per amino acid) that covalently attach the correct amino acid to the 3' CCA end of its cognate tRNA, using ATP; their proofreading establishes the accuracy of the genetic code ("the second genetic code"). See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
10. Translate 5′-AUGUUUGAAUAA-3′ and 5′-AUGUUCGAAUAA-3′. Relate the products to genetic-code degeneracy and wobble.

<!-- SOLUTION
**Answer (Q10, Application).** Both encode Met–Phe–Glu then terminate at UAA. UUU/UUC differ at codon position3 but both specify Phe; wobble contributes to recognition of synonymous codons. Award reading frame, stop and third-position distinction; not all third-base changes are synonymous. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->


## Questions 11–20: Mechanisms and evidence {.unnumbered}

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
11. Pre-mRNA splicing must be precise to within one nucleotide. Explain the two-step transesterification mechanism of splicing and the role of branch point A, 5' splice site, and 3' splice site in spliceosome assembly.

<!-- SOLUTION
**Answer (Q11, Application).** Splicing proceeds by **two sequential transesterification reactions**. First, the 2'-OH of the **branch-point adenosine** attacks the phosphate at the **5' splice site (GU)**, cleaving exon 1 and forming a lariat intermediate. Second, the freed 3'-OH of exon 1 attacks the **3' splice site (AG)**, joining the two exons and releasing the intron as a lariat. Spliceosome assembly recognizes these elements stepwise: U1 snRNP base-pairs the 5' splice site, U2 snRNP binds the branch point (bulging the branch A), and the U4/U6·U5 tri-snRNP completes the catalytic core — the one-nucleotide precision comes from this combinatorial recognition of all three signals. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
12. Alternative splicing generates multiple protein isoforms from one gene. *Drosophila Dscam* gene can produce >38,000 isoforms through mutually exclusive exon splicing. Explain: (a) the general mechanism of alternative splicing; (b) why *Dscam* diversity is important for axon guidance in neural wiring; (c) one human disease caused by aberrant alternative splicing.

<!-- SOLUTION
**Answer (Q12, Application).** **(a)** Alternative splicing includes or excludes particular exons (or uses alternative 5'/3' splice sites) in a regulated way, so one gene yields multiple mRNAs and protein isoforms; in *Dscam*, mutually exclusive selection among large clusters of variant exons combinatorially generates >38,000 isoforms. **(b)** This diversity gives each neuron a near-unique Dscam "identity tag"; isoform-specific homophilic binding mediates **self-avoidance**, so a neuron's own branches repel each other while still tiling among other neurons — essential for correct axon/dendrite wiring. **(c)** Spinal muscular atrophy is caused by aberrant *SMN2* exon 7 splicing (the therapy nusinersen corrects it); other examples include myotonic dystrophy and many cancers. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
13. The 5' cap (m⁷G) and poly-A tail of eukaryotic mRNA serve similar functions — protecting mRNA from exonuclease attack and promoting translation initiation. Explain: (a) how the 5' cap is added; (b) how eIF4E binding to the cap recruits the 43S pre-initiation complex; (c) why some viruses (e.g., poliovirus) cleave eIF4G to direct ribosomes to IRES sequences instead.

<!-- SOLUTION
**Answer (Q13, Application).** **(a) 5' cap addition** occurs co-transcriptionally when nascent pre-mRNA is ~25 nt long: (i) RNA 5'-triphosphatase removes the γ-phosphate; (ii) guanylyltransferase adds GMP via a unique **5'–5' triphosphate bridge**; (iii) guanine-N7-methyltransferase methylates N7 of the guanine, yielding **m⁷GpppN**. The capping enzyme is recruited via the phosphorylated CTD (Ser5-P) of RNA pol II — physically linking transcription to capping. **(b) eIF4E binding**: cytosolic **eIF4E** recognizes m⁷G via stacking with two conserved tryptophans (W56, W102), with K_d ≈ 100 nM. eIF4E forms eIF4F with **eIF4G (scaffold) and eIF4A (DEAD-box helicase)**; eIF4G simultaneously binds **PABPC1 on the poly-A tail** (circularising the mRNA) and recruits the **43S PIC** (40S + eIF1, eIF1A, eIF3, eIF2-GTP-Met-tRNAi) via eIF3. The 43S then scans 5' → 3' using eIF4A's ATP-dependent helicase activity until it finds the Kozak AUG. **(c) Poliovirus hijack**: poliovirus 2A protease **cleaves eIF4G** between the eIF4E-binding domain and the eIF3/eIF4A-binding domain. This shuts down **cap-dependent translation** of host mRNA but leaves intact the C-terminal half of eIF4G that binds viral **IRES** (internal ribosome entry site) in the 5' UTR of poliovirus RNA — so viral translation continues while host translation collapses. This is why the cell "looks infected" within hours: host protein synthesis drops > 90 %. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
14. The ribosome proof-reads aminoacyl-tRNA selection at the A site. Explain: (a) initial selection based on codon-anticodon base pairing (induced fit); (b) proofreading step (kinetokinetics — GTPase activation primarily if correct aa-tRNA is bound); (c) why errors occur at ~1 in 10,000 vs DNA polymerase errors of 1 in 10⁹ (why is translation less accurate?).

<!-- SOLUTION
**Answer (Q14, Application).** Correct codon–anticodon pairing strongly accelerates elongation-factor GTPase activation during initial selection. Near-cognate substrates can still hydrolyze GTP and then be preferentially rejected during accommodation/proofreading; hydrolysis is not conditional on perfect pairing with absolute certainty. \citet{gromadski2004fidelity} measured this kinetic discrimination in a bacterial system. Translation errors generally do not alter inherited DNA sequence, but their effects can include harmful misfolding or altered cellular functions, not just one harmless short-lived protein. Error rates depend on substrate and assay; the quoted values are approximate comparisons, not universal constants. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
15. Cycloheximide blocks the elongation step of eukaryotic translation (not prokaryotic), because it specifically inhibits the 60S subunit translocation step. Explain: (a) what translocation means mechanistically; (b) why prokaryotic ribosomes (70S) are not blocked; (c) how this selectivity is exploited in laboratory cell biology experiments.

<!-- SOLUTION
**Answer (Q15, Application).** **(a) Translocation** is the eEF2-driven, GTP-dependent movement of the ribosome by exactly one codon along the mRNA after peptide-bond formation, shifting the tRNAs from A→P and P→E sites and opening the A site for the next aminoacyl-tRNA. **(b)** Cycloheximide binds the **E site of the 60S subunit**, blocking eEF2-mediated translocation; prokaryotic 70S ribosomes have structurally distinct large-subunit rRNA/proteins that cycloheximide does not recognize, so bacterial translation is unaffected. **(c)** This eukaryote-specific, rapid, reversible arrest is exploited to **freeze ribosomes on mRNA** — e.g., to stabilize polysomes for polysome profiling and ribosome profiling (Ribo-seq), and to halt protein synthesis in pulse-chase and cytotoxicity experiments. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. Nonsense-mediated mRNA decay (NMD) degrades mRNAs with premature stop codons. Explain: (a) how the cell recognizes a premature vs normal stop codon (role of exon-junction complexes); (b) the UPF1/SMG cascade; (c) why NMD is a quality control mechanism that also regulates normal gene expression for ~10% of genes.

<!-- SOLUTION
**Answer (Q16, Application).** **(a)** During the pioneer round of translation the ribosome displaces exon-junction complexes (EJCs). A stop codon is judged **premature if an EJC remains >50–55 nt downstream of it** (a normal stop is the last codon, with no downstream EJC). **(b)** The retained EJC recruits **UPF1**, which is phosphorylated by SMG1; phospho-UPF1 then recruits SMG5/6/7, triggering endonucleolytic cleavage (SMG6) and exonucleolytic decay of the transcript. **(c)** NMD is both quality control — destroying truncating-mutation and error-prone transcripts to prevent dominant-negative truncated proteins — and a normal regulatory mechanism: ~10% of transcripts (including alternatively spliced isoforms with PTC-containing exons and autoregulated splicing-factor mRNAs) are physiologically tuned by NMD. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
17. Polyribosomes (polysomes) consist of multiple ribosomes simultaneously translating the same mRNA. If a 1,500-nt coding sequence is occupied by ribosomes spaced on average every 80 nt, how many ribosomes are simultaneously translating this mRNA? Calculate the rate of protein synthesis per mRNA if each ribosome adds 2 amino acids/sec.

<!-- SOLUTION
**Answer (Q17, Application).** Ribosome count: $N = \dfrac{1500\ \mathrm{nt}}{80\ \mathrm{nt/ribosome}} = \mathbf{18.75 \approx 19\ \mathrm{ribosomes}}$ simultaneously engaged. Protein output: each ribosome adds 2 aa/s → 19 × 2 = **38 amino acids per second** across the polysome. Time to complete one protein per ribosome: 1500 nt ÷ 3 = 500 codons ÷ 2 codons/s = **250 s ≈ 4 min**. Steady-state output per mRNA = 1 finished protein every (80 nt / 2 codons·s × 3 nt/codon) ≈ **13 s per completed chain**, i.e. ~280 proteins/h/mRNA. Biological sanity check: this matches measured translation rates in mammalian cells (median ~5 proteins/mRNA/min for short transcripts). Sucrose-gradient polysome profiles show β-actin mRNA (~1800 nt) in fractions containing 8–12 ribosomes — consistent with our estimate once you account for scanning delays and the fact that the first ~40 nt after the cap are typically bare (eIF4E/PABPC1 footprint). **Biological significance**: polysome occupancy (footprint density from ribosome profiling / Ribo-seq) is the gold-standard readout of translation efficiency; a 19-ribosome polysome represents high expression, while a monosome-enriched mRNA is either stalled or repressed. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO9; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. Predict lac output for lactose absent/glucose absent, lactose present/glucose absent, and lactose present/glucose present. Why does CAP activation not override bound LacI?

<!-- SOLUTION
**Answer (Q18, Application).** Outputs are strongly repressed, high and basal/lower, respectively. Allolactose relieves LacI; low glucose favors CAP–cAMP activation. CAP may be active without lactose while LacI still represses. Award three states and dual-control mechanism; do not claim literal zero transcription. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. For a conventional secretory cargo with a cleavable N-terminal signal peptide, explain SRP-dependent cotranslational ER targeting, signal-peptide cleavage and quality control. Compare disposal of misfolded ER and cytosolic proteins. Why does this model not describe every ER-entry or secretion route?

<!-- SOLUTION
**Answer (Q19, Application).** SRP recognizes the emerging hydrophobic signal peptide and can pause elongation while targeting the ribosome to the SRP receptor and Sec61; translation then continues with translocation. Signal peptidase removes the specified cleavable signal peptide. Appropriate misfolded ER substrates undergo ERAD, including retrotranslocation and cytosolic proteasomal degradation; cytosolic substrates use chaperones, proteasomes or autophagy. Sec62-dependent posttranslational ER entry is an experimentally demonstrated alternative for some cargos \citep{lakkaraju2012sec62}. Absence of a conventional signal peptide does not alone exclude unconventional secretion. Award the named route and its limits. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. Transcription factors bind specific DNA sequences (motifs). A transcriptional activator contains a DNA-binding domain (DBD) and an activation domain (AD). Explain: (a) what structural motifs are common in DBDs (zinc finger, helix-turn-helix, leucine zipper); (b) how the activation domain recruits the Mediator complex; (c) how enhancers (located kb away from promoters) loop to contact the preinitiation complex through cohesin-mediated chromosome looping.

<!-- SOLUTION
**Answer (Q20, Application).** **(a)** Common DNA-binding domains include the **zinc finger** (Cys₂His₂ fingers inserting an α-helix into the major groove), the **helix-turn-helix / homeodomain**, and the **basic leucine zipper (bZIP)** and basic helix-loop-helix, which dimerize and grip DNA with basic regions. **(b)** The separate **activation domain** does not bind DNA; it recruits coactivators and the **Mediator complex**, which bridges the enhancer-bound activator to RNA Pol II and the general transcription factors, stimulating preinitiation-complex assembly and CTD phosphorylation. **(c)** Distal enhancers contact promoters through **chromatin looping**: cohesin and CTCF organize loop domains (TADs), bringing the enhancer-bound activator/Mediator into physical proximity with the promoter even when they are tens of kb apart in linear sequence. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->


## Questions 21–30: Transfer and evaluation {.unnumbered}

<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
21. Evaluate the dual role of SR proteins (serine-arginine-rich splicing factors) in both constitutive and alternative splicing and mRNA export. What does the dual role of SR proteins reveal about the evolutionary coupling between nuclear RNA processing and cytoplasmic translation?

<!-- SOLUTION
**Answer (Q21, Synthesis).** Empirically, SR proteins bind exonic splicing enhancers to promote spliceosome assembly and regulate alternative splice-site choice, *and* they remain bound to the spliced mRNP where they help recruit the TREX export machinery (e.g., via NXF1/TAP) and influence cytoplasmic translation efficiency. The judgment — that nuclear processing and cytoplasmic fate are evolutionarily coupled — follows because the same factor physically links splicing, export, and translation, making them a coordinated pipeline rather than independent steps; this "mRNP marking" also explains why spliced mRNAs are translated more efficiently than intronless ones. What would change the conclusion: showing SR-protein splicing and export functions are genetically separable (separation-of-function mutants), or that export/translation enhancement occurs equally without SR deposition. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
22. Design a comprehensive experiment to map most enhancers controlling a specific gene in a given cell type using: (a) H3K27ac ChIP-seq (active enhancer mark); (b) ATAC-seq (open chromatin); (c) HiC chromatin conformation capture; (d) CRISPR deletion of candidate enhancers and transcriptional output measurement. How would you prioritize which enhancers are most important?

<!-- SOLUTION
**Answer (Q22, Synthesis).** **Hypothesis:** a defined set of distal enhancers drives the gene's expression in this cell type. **Design:** map candidates with H3K27ac ChIP-seq (active enhancers) and ATAC-seq (open chromatin), then use Hi-C/capture Hi-C to identify which open, acetylated regions physically loop to the promoter; the **control/comparison** is an unedited population and CRISPRi/CRISPR deletion of each candidate vs a scrambled-gRNA control. **Measured outcome:** target-gene mRNA (RT-qPCR/RNA-seq) after each perturbation, with biological replicates. **Prioritization:** rank enhancers by (i) magnitude of expression loss on deletion, (ii) strength of the Hi-C contact with the promoter, (iii) H3K27ac/ATAC signal and conservation, and (iv) presence of relevant TF motifs/footprints. A **falsifying result**: deleting the top-ranked enhancer leaves expression unchanged, indicating redundancy or that the causal element was missed. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO10; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
23. Design a Hox-protein experiment distinguishing DNA-binding specificity, cofactor interactions and expression domain as causes of different developmental programs.

<!-- SOLUTION
**Answer (Q23, Synthesis).** Compare matched Hox expression, motif-mutant reporters, DNA-binding/cofactor-domain swaps and cofactor loss/rescue. Measure occupancy, lineage-specific RNA and phenotype. Award three competing mechanisms, controlled perturbations and functional readouts; binding alone does not prove cell fate. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
24. Many bacteria couple transcription and translation. Explain how this enables the illustrated trp leader-peptide attenuation mechanism, and why ordinary nuclear transcription and cytosolic translation cannot couple in that same direct way. What limits prevent generalizing to every prokaryotic transcript or every eukaryotic compartment?

<!-- SOLUTION
**Answer (Q24, Synthesis).** In the bacterial trp example, a ribosome translates the nascent leader RNA while polymerase is still transcribing. Trp-tRNA availability influences ribosome stalling at Trp codons, determining terminator versus antiterminator hairpin formation and hence downstream transcription. Ordinary nuclear transcription and cytosolic translation are spatially separated, preventing this same direct coupling. Neither the absence of a nucleus nor this example proves that every prokaryotic transcript couples, and the argument is not an evolutionary prohibition on attenuation-like regulation in every eukaryotic compartment. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Ribosome biogenesis occurs in the nucleolus and is rate-limiting for cell growth. Evaluate the regulatory relationship between mTORC1, Pol I transcription of rDNA, and ribosome biogenesis. Why does mTOR inhibition suppress cell growth even in cells with unlimited amino acid supply?

<!-- SOLUTION
**Answer (Q25, Synthesis).** Ribosome biogenesis (rDNA transcription by Pol I, rRNA processing, assembly in the nucleolus) consumes most of a growing cell's transcriptional output and is rate-limiting for proliferation. **mTORC1** integrates growth-factor and nutrient signals and directly stimulates ribosome production: it activates Pol I (via TIF-IA/UBF), Pol III (5S rRNA, tRNA, via Maf1 repression), and translation of ribosomal-protein mRNAs (via S6K1 and 4E-BP1). Therefore mTOR inhibition (rapamycin) suppresses growth **even with abundant amino acids** because it shuts down the biosynthetic capacity needed to make new ribosomes — without enough ribosomes the cell cannot increase mass or divide, regardless of substrate supply. The evidence: rapamycin rapidly reduces nucleolar size, 45S pre-rRNA, and polysome levels. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Evaluate evidence that the peptidyl-transferase center is RNA-based. Why are substrate positioning and proton-transfer chemistry not mutually exclusive explanations?

<!-- SOLUTION
**Answer (Q26, Synthesis).** Structures show an RNA-dominated catalytic center; biochemical perturbations test individual contributions. Substrate positioning, water exclusion and proton-transfer networks can all lower the activation barrier. Award structural evidence, kinetic evidence and their nonexclusive interpretation; Nobel recognition is not itself an experiment settling every chemical step. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. Matched cultures show RNA1→1 but protein1→0.3 after treatment; another treatment gives RNA1→0.3 and protein1→0.4. Design measurements distinguishing transcription, RNA decay, translation and protein degradation.

<!-- SOLUTION
**Answer (Q27, Synthesis).** The first pattern supports translation/degradation changes; the second may reflect transcription or RNA decay. Measure nascent RNA and RNA half-life, ribosome occupancy and protein turnover with matched loading/viability controls. Award pattern interpretation and discriminating measurements; endpoint abundance alone is not a synthesis rate. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
28. Design a hemophilia A therapy comparison: investigational FVIII mRNA delivery, a named liver-directed AAV product, and editing only if a supplied F8 variant is amenable to the chosen editor. Evaluate product-specific eligibility, redosing, duration, immunogenicity and delivery; specify clinical and laboratory outcomes rather than a single success threshold.

<!-- SOLUTION
**Answer (Q28, Synthesis).** Modified FVIII mRNA offers transient expression, with redosing dependent on formulation, delivery and immune responses. AAV F8 gene addition can provide prolonged expression but has payload, immunity, liver-safety and durability constraints. The June 2023 ROCTAVIAN label specifies one-time administration and adult severe hemophilia A eligibility with AAV5-antibody and other screening \citep{fda2023roctavianlabel}; that is product-specific, not an eternal rule for all vectors. Editing requires the actual variant, editable chemistry/window and relevant-cell delivery, with off-target/bystander assessment. Compare FVIII activity using specified assays, bleeding rates, factor use, inhibitors, liver effects and durability against appropriate controls. No single 5% FVIII threshold alone defines clinical success or failure. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
29. RNA interference (RNAi) was discovered when dsRNA triggered gene silencing in *C. elegans* (Fire and Mello, 1998). Evaluate the mechanism (Dicer, RISC, Ago2-mediated cleavage), the evolutionary origin of RNAi (antiviral defense), and the clinical development of siRNA therapeutics (inclisiran for PCSK9 silencing). What advantages does siRNA have over antisense oligonucleotides (ASOs) for gene silencing?

<!-- SOLUTION
**Answer (Q29, Synthesis).** Guide-loaded Ago2 can cleave complementary target RNA with turnover; chemically designed siRNAs can enter downstream of Dicer processing. RNase-H-recruiting gapmer ASOs also support enzymatic target turnover, unlike steric splice-modifying ASOs. Potency, duration, tissue delivery and toxicity depend on chemistry and target. Award RISC mechanism, ASO class distinction and delivery limits; do not infer universal siRNA superiority. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
30. Critically evaluate the concept of the "central dogma" (DNA → RNA → protein). Identify three biological exceptions that violate a strict reading of the central dogma (reverse transcription, RNA editing, prion replication), explain their mechanisms, assess whether these exceptions require a fundamental revision of the central dogma, and state what RNAcentral-style database checks are needed before claiming that a non-coding RNA has a defined gene model and function.

<!-- SOLUTION
**Answer (Q30, Synthesis).** The central dogma states information flows DNA→RNA→protein and not back out of protein. Three classic challenges: **(1) Reverse transcription** — retroviruses/telomerase make DNA from RNA (RNA→DNA), expanding allowed information flow but not violating the core prohibition (no protein→nucleic-acid). **(2) RNA editing** — e.g., A-to-I (ADAR) or C-to-U (APOBEC) editing changes mRNA sequence after transcription, so the protein differs from the genomic template; this elaborates the RNA step rather than reversing flow. **(3) Prions** — a misfolded protein (PrP^Sc) templates conformational conversion of normal protein, transmitting *conformational*, not sequence, information protein→protein. **Assessment:** Crick's strict statement (no information from protein back to nucleic acid) survives — none of these transfers sequence from protein to DNA/RNA; they are **elaborations within the framework**, not a fundamental revision, though prions show heritable information can be protein-borne. Source-governed RNA interpretation then asks whether the RNAcentral entry is sequence-level or gene-level, which release and identifiers are being used, whether isoforms/splice variants are merged correctly, and whether literature links support function rather than only mention the RNA \citep{rnacentral2026}. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->
