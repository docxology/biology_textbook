# Mutations, CRISPR, and Genomics

\label{sec:unit_IV_mutations_and_genomics}

\begin{figure}[htbp]
\centering
\includegraphics[width=0.9\textwidth]{../figures/mutation_rate_spectrum.png}
\caption{Source-scoped mutation-rate evidence with separate target and time bases. Numeric panels describe single-nucleotide substitutions per position, selected dinucleotide microsatellites per locus, CNVs per haploid genome, and gene duplication per million years across eukaryotes. These estimates cannot be ranked as genomic burden. Two additional classes have no verified numeric value supplied.}
\label{fig:unit_IV_mutation_rate_spectrum}
\end{figure}

<!-- alt: Separate mutation evidence panels retain row-specific denominators, organisms, time bases and ascertainment; per-position, per-locus, per-genome and evolutionary-time estimates do not share a comparable burden axis. -->


<!-- chapter-metadata-badge -->
> Level 2/3 · 55 min read · 75 min lecture · Prerequisites: \cref{sec:unit_IV_gene_expression}

## Learning Objectives

1. Classify [**mutation**](#gl:mutation)s by type (point, frameshift, chromosomal), molecular change, and functional consequence.
2. Describe mutagenic agents and assays for mutagenicity (Ames test).
3. Explain DNA repair mechanisms and their relationship to human disease.
4. Describe the CRISPR-Cas9 mechanism in detail, including PAM recognition, DSB creation, and repair outcomes.
5. Compare CRISPR-Cas9, base editing, and prime editing technologies.
6. Define the [**genome**](#gl:genome) and describe key genomic features revealed by sequencing.
7. Explain next-generation sequencing technologies and their applications.
8. Describe GWAS methodology and its contributions to understanding complex disease.
9. Evaluate ethical issues in personal genomics and genetic testing.

<!-- curriculum-scaffold-start -->
### Study Blueprint

- **Big idea:** Genomic variation becomes biological consequence through sequence context, repair, and selection.
- **Core concepts:** mutation classes, DNA repair, CRISPR, genome analysis.
- **Framework alignment:** Vision & Change: Information flow, exchange, and storage, Structure and function; AP Biology: Information Storage and Transmission, Systems Interactions; NGSS-style topics: Inheritance and Variation of Traits, Structure and Function.
- **Model or quantitative lens:** Mutation-rate, edit-efficiency, and sequence-comparison calculations.
- **Data skill:** Classify variants and predict likely molecular effect from sequence evidence.
- **Practice cadence:** Concept Explanation, Questions and Methods, Argumentation.
- **Common misconception to repair:** Not every mutation is harmful, and not every harmful mutation changes a protein sequence.
- **Primary lab:** \nameref{sec:lab_unit_IV_mutations_and_genomics}.
- **Question bank:** \nameref{sec:q_unit_IV_mutations_and_genomics}.
- **Transfer task:** Transfer variant reasoning to cancer genomics, ancestry, gene therapy, or microbial evolution.
- **Bridge to computation:** `biology.genetics.genetics.hamming_distance`.
<!-- curriculum-scaffold-end -->

---

> **Opening Vignette — One Letter Changes Everything**
> 
> In 1949, Linus Pauling published a paper in *Science* titled "Sickle Cell Anemia, a Molecular Disease" — the first time a human illness was attributed to a chemical change in a specific [**protein**](#gl:protein). Eight years later, Vernon Ingram used the newly developed technique of protein fingerprinting to identify the precise mutation: a single amino acid substitution, glutamic acid to valine, at position 6 of the β-globin chain. Just one [**nucleotide**](#gl:nucleotide) change — GAG to GTG — makes hemoglobin polymerize under low-oxygen conditions, distorting red blood cells into rigid sickle shapes that clog capillaries. That one point mutation causes pain crises, organ damage, and shortened lifespan for millions worldwide. The sickle-cell story remains the most compelling illustration of how a single mutational event can cascade through molecular structure, protein function, cell physiology, and whole-organism health.

## Types of Mutations

A **mutation** is any heritable change in DNA sequence. Mutations are the ultimate source of most genetic variation and therefore the raw material for evolution.

### Mutation Rates: A Quantitative Framework

> **Mathematical Background:** A Poisson model can approximate rare, independent mutation events with a specified expected count. For a review of probability distributions relevant to genetics, see \nameref{sec:appendix_math_review}.

The approximate human germline single-base-substitution rate $1.2\times10^{-8}$ per base per generation is a useful order-of-magnitude teaching value, not a universal constant. \cref{fig:unit_IV_mutation_rate_spectrum} retains each source-specific denominator and time basis: per-locus microsatellite estimates and per-genome CNV estimates are not per-base rates. The unsorted `MutationRateEvidence` catalog carries provenance and ascertainment; it does not rank burden or population variance. Expected burden additionally requires eligible target size and non-overlapping classes.

The figure's numeric panels use a direct family-quartet substitution estimate, selected-microsatellite measurements, a population-inferred CNV estimate and an evolutionary-time gene-duplication estimate \citep{roach2010inheritance,sun2012microsatellites,conrad2010cnv,lynch2000duplication}. Their targets, ascertainment and time bases differ; they do not form a commensurate burden ranking.

\begin{equation}M_{\mathrm{SNV}} = 2N \times \mu \approx 6.4 \times 10^9 \times 1.2 \times 10^{-8} \approx 70\text{--}80 \text{ new substitutions/offspring}\label{eq:mutations_per_gen}\end{equation}

This is an illustrative expected substitution count, not a measured count for every child or an upper bound. For a target containing $L$ eligible base copies, assume independent events and a uniform per-base, per-generation rate $\mu$; the resulting **Poisson model** gives:

\begin{equation}P(k) = \frac{(\mu L)^k \, e^{-\mu L}}{k!}\label{eq:poisson_mut}\end{equation}

This is used to assess whether a [**gene**](#gl:gene) or genomic region has an excess of mutations relative to the background rate — a signature of positive selection or a mutational hotspot.

For genome-wide studies, the **Bonferroni-corrected significance threshold** for $m$ independent tests is:

\begin{equation}\alpha_{\text{corrected}} = \frac{\alpha}{m} = \frac{0.05}{10^6} = 5 \times 10^{-8}\label{eq:bonferroni_correction}\end{equation}

This is the standard genome-wide significance threshold for GWAS: primarily associations with $p < 5 \times 10^{-8}$ are considered robust.

The **Ka/Ks ratio** (also called dN/dS or ω) measures the ratio of nonsynonymous to synonymous substitution rates, revealing the mode of [**natural selection**](#gl:natural-selection):

\begin{equation}\omega = \frac{K_a}{K_s} = \frac{d_N}{d_S}\label{eq:omega_ratio}\end{equation}

where $\omega < 1$ indicates purifying selection, $\omega = 1$ neutral evolution, and $\omega > 1$ positive selection.

### Nucleotide-Level (Point) Mutations

: Nucleotide-Level (Point) Mutations: Type and Description. {#tbl:unit_IV_mutations_and_genomics_nucleotide_level_point_mutations}
| Type | Description | Example Consequence |
|------|-------------|---------------------|
| **Transition** | Purine to purine (A to G) or pyrimidine to pyrimidine (C to T) | Most common; often neutral or conservative amino acid change |
| **Transversion** | Purine to pyrimidine or vice versa (A to C, A to T, G to C, G to T) | Rarer (~2:1 transition:transversion ratio); more often disruptive |
| **Silent (synonymous)** | [**Codon**](#gl:codon) change producing the same amino acid (degeneracy) | Usually no phenotypic effect; may affect splicing or mRNA stability |
| **Missense** | Codon change producing a different amino acid | Conservative (e.g., Leu to Ile) or non-conservative (e.g., Glu to Val in sickle cell) |
| **Nonsense** | Point mutation creating a premature stop codon | Truncated protein; usually non-functional; often triggers NMD |
| **Splice site** | Mutation at [**intron**](#gl:intron)-[**exon**](#gl:exon) boundary (GT/AG dinucleotides) | Exon skipping, intron retention, or cryptic splice site activation |

### Insertions, Deletions, and Frameshifts

- **Insertion**: One or more nucleotides added to the sequence
- **Deletion**: One or more nucleotides removed from the sequence
- **Frameshift**: An insertion or deletion that is NOT a multiple of 3 bp -- shifts the entire downstream reading frame, producing a completely altered amino acid sequence and usually encountering a premature stop codon
- **In-frame insertion/deletion**: A multiple of 3 bp -- adds or removes amino acids without disrupting the reading frame (e.g., the deltaF508 mutation in CFTR is a 3-bp deletion removing Phe508, causing cystic fibrosis)

### Copy Number Variants and Structural Mutations

- **Copy number variants (CNVs)**: Duplications or deletions of segments from 1 kb to several Mb. The average human genome contains ~1,000 CNVs relative to the reference. CNVs contribute more base pairs of variation between individuals than SNPs.
- **Inversions**: A chromosomal segment is reversed end-to-end. Pericentric inversions include the [**centromere**](#gl:centromere); paracentric do not. Inversions can disrupt genes at breakpoints or alter regulatory landscapes.
- **Translocations**: A segment moves to a different [**chromosome**](#gl:chromosome). **Reciprocal translocations** exchange segments between two chromosomes. **Robertsonian translocations** fuse the long arms of two acrocentric chromosomes (13, 14, 15, 21, 22).

> **Clinical Connection: The Philadelphia Chromosome**
> The t(9;22) reciprocal translocation creates the **Philadelphia chromosome** -- a derivative chromosome 22 carrying the **BCR-ABL1** fusion gene. This fusion produces a constitutively active tyrosine kinase that drives chronic myelogenous leukemia (CML). The targeted tyrosine kinase inhibitor **imatinib (Gleevec)** revolutionized CML therapy, converting a fatal disease into a manageable chronic condition (5-year survival increased from ~30% to >90%). This is a paradigm for targeted cancer therapy.

### Trinucleotide Repeat Expansion Disorders

A special class of mutations involving expansion of short tandem repeats:

: Trinucleotide Repeat Expansion Disorders: Disease and Repeat. {#tbl:unit_IV_mutations_and_genomics_trinucleotide_repeat_expansion_disorders}
| Disease | Repeat | Normal Range | Pathogenic Range | Location | Mechanism |
|---------|--------|-------------|-----------------|----------|-----------|
| Huntington disease | CAG (Gln) | 6-35 | >36 (full penetrance >40) | HTT exon 1 | Toxic polyglutamine aggregation |
| Fragile X syndrome | CGG | 5-44 | >200 (full-mutation range) | FMR1 5' UTR | Typically promoter hypermethylation and reduced FMR1 expression; exceptions require direct assays |
| Myotonic dystrophy type 1 | CTG | 5-34 | >50 | DMPK 3' UTR | Toxic RNA foci sequester MBNL1 |
| Friedreich ataxia | GAA | 5-33 | >66 | FXN intron 1 | [**Heterochromatin**](#gl:heterochromatin) formation silences FXN |

For FMR1, repeat size does not by itself establish methylation, RNA abundance or FMRP abundance. Unmethylated full mutations can retain elevated RNA \citep{tassone2000unmethylated}, and size/methylation mosaicism can produce mixed states; measure each molecular endpoint rather than infer obligatory silencing from the repeat threshold. Premutation alleles are typically active, but RNA abundance alone does not establish normal protein production or a single mechanism for every premutation-associated phenotype.

**Anticipation**: These diseases show **genetic anticipation** -- earlier onset and increased severity in successive generations -- because the unstable repeats tend to expand further during DNA replication (particularly during germ cell divisions).

**Concept Check 13.1**

> 1. Classify the sickle cell mutation (GAG to GUG in beta-globin codon 6) by type.
> 2. Why are frameshift mutations generally more deleterious than missense mutations?
> 3. Explain why trinucleotide repeat diseases show anticipation.
> 4. The deltaF508 CFTR mutation is a 3-bp deletion. Why is this NOT a frameshift?

> **Worked Example — Poisson Distribution of De Novo Substitutions:** Assume an illustrative germline substitution rate of 1.2 × 10⁻⁸ per base per generation and a diploid target of 6.4 × 10⁹ base copies. The expected count is λ = 1.2 × 10⁻⁸ × 6.4 × 10⁹ = 76.8, rounded to 77 for this model. With independent events at a uniform rate, P(k) = e^(-λ)λ^k/k! and P(0) = e^(-77) ≈ 3.6 × 10⁻³⁴. A rough normal approximation without continuity correction gives P(>100) ≈ 1 - Φ((100 - 77)/√77) ≈ 0.0044. These probabilities are conditional on the illustrative model, not population-wide empirical frequencies. Kong et al.'s cohort, described below, estimated about two additional substitutions per year of paternal age; applying that linear effect over 20 years gives about 40 additional substitutions on average, not a prediction for an individual family.

> **Concept Check (Evaluate):** Mutational signatures catalogued in the COSMIC database reveal that each major DNA-damaging agent leaves a characteristic pattern. UV radiation induces C→T transitions at dipyrimidine sites (especially CC→TT). Tobacco smoking causes C→A transversions (SBS4). Alkylating agents tend to produce G→A transitions at CpG dinucleotides. (a) A patient's tumor shows predominantly C→T transitions at TpCpN trinucleotides (signatures SBS2 and SBS13, characteristic of APOBEC deaminase activity). Propose a molecular mechanism explaining why APOBEC enzymes — which normally edit RNA and act on retroviral DNA intermediates — generate this signature in tumor cells, and identify which step in the cell cycle exposes single-stranded DNA to APOBEC. (b) The same patient's tumor is then exposed to a novel chemotherapy. Design a pre-clinical sequencing strategy (number of biopsies, sequencing depth, signature-decomposition approach) that would let you decide whether the therapy adds a new mutational signature or enriches the pre-existing APOBEC signature.

> **Concept Check (Synthesis):** COSMIC mutational signatures are derived by NMF decomposition of cancer mutation catalogs. Signature SBS3 (homologous recombination deficiency, HR-deficient) is characterized by: (a) What trinucleotide context patterns define SBS3 and explain the molecular mechanism producing them — why does HR deficiency produce these specific patterns rather than, say, APOBEC-driven C→T mutations at TCA/TCT contexts? (b) PARP inhibitors (olaparib) are FDA-approved for HR-deficient (BRCA1/2-mutated) cancers. Explain the concept of synthetic lethality: why does BRCA1/2 mutation sensitize cells to PARP inhibition, while PARP inhibition alone is not lethal to HR-proficient cells? (c) Cancer cells treated with platinum compounds (cisplatin, carboplatin) acquire resistance through multiple mechanisms: HR restoration (BRCA2 reversion mutations), PARP1 loss, 53BP1 loss, and REV1/pol ζ upregulation. For each mechanism, predict the mutational signature change you would observe in a post-treatment biopsy.

---

## Mutagenic Agents and DNA-Damage Mechanisms

### Physical Mutagens: Radiation and Replication Stress

**UV radiation (UVB, 280-320 nm)**:
- Creates **cyclobutane pyrimidine dimers (CPDs)**: covalent bonds form between adjacent pyrimidines (T-T most common)
- Creates **6-4 photoproducts (6-4 PPs)**: covalent bond between positions 6 and 4 of adjacent pyrimidines
- Both distort the helix and block replication/[**transcription**](#gl:transcription)
- Repaired by nucleotide excision repair (NER); failure causes xeroderma pigmentosum

**Ionizing radiation (X-rays, gamma rays)**:
- Creates reactive oxygen species (ROS) that attack bases and the sugar-phosphate backbone
- Causes single-strand breaks (SSBs) and double-strand breaks (DSBs)
- DSBs are the most dangerous lesion -- if unrepaired, lead to chromosomal translocations, deletions, or cell death
- Repaired by NHEJ and HR

### Chemical Mutagens and Base-Altering Reactions

: Chemical Mutagens and Base-Altering Reactions: Agent and Type. {#tbl:unit_IV_mutations_and_genomics_chemical_mutagens_and_base_altering_reactions}
| Agent | Type | Mechanism | Mutation Caused |
|-------|------|-----------|----------------|
| **EMS** (ethyl methanesulfonate) | Alkylating agent | Adds ethyl group to O$^6$ of guanine | G:C to A:T transitions |
| **Nitrogen mustard** | Bifunctional alkylating agent | Cross-links DNA strands | Blocks replication; DSBs |
| **Nitrous acid (HNO$_2$)** | Deaminating agent | Deaminates C to U, A to hypoxanthine | C:G to T:A and A:T to G:C transitions |
| **Ethidium bromide** | Intercalating agent | Inserts between base pairs, stretching the helix | Frameshift mutations (insertions/deletions) |
| **5-Bromouracil (5-BU)** | Base analog | Incorporated in place of T; tautomerizes to pair with G | A:T to G:C transitions |
| **Acridine orange** | Intercalating agent | Inserts between bases | Frameshift mutations |
| **Benzo&#91;a&#93;pyrene** (cigarette smoke) | Polycyclic aromatic hydrocarbon | Forms bulky adducts on guanine (after CYP1A1 activation) | G:C to T:A transversions; NER substrate |

**Reactive oxygen species (ROS)**: Endogenous byproducts of [**aerobic**](#gl:aerobic) metabolism (superoxide O$_2^{-}$, hydroxyl radical OH$\cdot$, hydrogen peroxide H$_2$O$_2$). ROS oxidize guanine to **8-oxoguanine (8-oxoG)**, which mispairs with adenine, causing G:C to T:A transversions. Repaired by BER (OGG1 glycosylase).

### The Ames Test

The **Ames test** (Bruce Ames, 1973) is a bacterial mutagenicity assay that uses *Salmonella typhimurium* strains carrying various **his$^-$** (histidine-requiring) mutations:

**Procedure**:
1. His$^-$ bacteria are plated on minimal medium (no histidine)
2. Test chemical applied (with and without liver microsomal extract S9 to simulate mammalian metabolic activation)
3. Count revertant colonies (his$^+$) that can grow without histidine
4. Compare to spontaneous reversion rate (negative control) and known mutagen (positive control)

**Interpretation**: A significant increase in revertant colonies indicates the chemical is mutagenic. Different tester strains detect different mutation types (e.g., TA98 detects frameshifts; TA100 detects base substitutions).

**Correlation**: ~80-90% of known carcinogens are mutagenic in the Ames test. The Ames test is a standard regulatory tool for chemical safety screening.

---

## DNA Damage and Repair

DNA damage includes chemically distinct lesions from endogenous chemistry and environmental exposure. Ward's review concerns ionizing-radiation damage in mammalian cells \citep{ward1988}; it does not establish a universal endogenous daily lesion count for every human cell.

### DNA Damage — Mechanisms and Quantification

Lesion formation rate, unrepaired burden and fixed mutation frequency are different quantities. A per-cell-per-day estimate requires cell type, genome amount, exposure, interval, assay and repair conditions; the following table deliberately does not assign universal frequencies.

: DNA Damage: Lesion Mechanisms and Measurement Requirements. {#tbl:unit_IV_mutations_and_genomics_dna_damage_quantitative_background}
| Lesion type | Mechanism or source | Quantification boundary |
| ----------- | ------------------- | ----------------------- |
| Depurination / abasic sites | Hydrolysis of base–sugar bonds; abasic sites can also be repair intermediates | Separate formation from remaining abasic-site burden |
| Depyrimidination | Hydrolysis | Specify base identity, temperature and assay |
| Cytosine deamination (C → U) | Hydrolytic base conversion | Uracil detection is not automatically a fixed mutation count |
| 5-methylcytosine deamination (5mC → T) | Deamination of methylated cytosine | State methylation context and repair opportunity |
| Oxidized guanine (8-oxoG) | Oxidation involving guanine C8 | Control oxidation introduced during sample processing |
| Other oxidized bases | Chemically distinct oxidation products | Identify the measured products rather than summing incompatible assays |
| Single-strand breaks | Backbone damage or repair intermediates | Distinguish breaks from alkali-labile sites under the chosen assay |
| Interstrand crosslinks | Covalent links between opposite strands, including aldehyde-derived lesions | Specify crosslink chemistry and exposure |
| Replication-associated DSBs | Some damaged or collapsed forks produce one-ended breaks | Fork arrest is not automatically a DSB; state the cell-cycle and detection method |
| Other DSBs | Radiation, enzymatic cleavage or sufficiently close opposing-strand lesions | A damage-focus count is not necessarily a one-to-one break count |
| UV-induced CPDs | Photochemical pyrimidine dimers | Report wavelength, fluence, tissue depth and repair interval |
| Alkylated bases | Endogenous or exogenous alkyl donors | Identify the adduct and distinguish exposure from residual burden |
| Topoisomerase-linked lesions | Trapped covalent enzyme–DNA intermediates | Camptothecin targets topoisomerase I; etoposide targets topoisomerase II |

**Replication-associated DSBs** can be one-ended lesions requiring coordinated repair and restart. A nearby sister chromatid supports homologous-recombination pathways in S/G2; this does not establish that every stalled fork becomes a break or that one universal daily number accounts for most physiological DSBs.

Polymerase selectivity, proofreading and mismatch repair reduce errors during genome copying. A final per-base replication-error estimate requires an organism, division interval and assay; it is not the same quantity as a daily count of chemically damaged bases.

```mermaid
flowchart TD
    A[DNA Damage] --> B{Type of Damage?}
    B -->|"Alkylated base (O6-meG)"| C["Direct Reversal: MGMT transfers methyl group (suicide enzyme)"]
    B -->|"Oxidized base (8-oxoG), deaminated base (U), AP site"| D["Base Excision Repair (BER)"]
    B -->|"Bulky adduct (CPD, 6-4PP, benzo[a]pyrene)"| E["Nucleotide Excision Repair (NER)"]
    B -->|"Replication mismatch, small indel loop"| F["Mismatch Repair (MMR)"]
    B -->|"Double-strand break"| G{End and template context?}
    G -->|"End joining feasible across the cycle"| H["NHEJ: Ku70/80 + DNA-PKcs + Ligase IV"]
    G -->|"Homologous template available; common sister-based routes in S/G2"| I["Homologous Recombination: MRN + BRCA1/2 + RAD51"]
    B -->|"Interstrand crosslink (ICL)"| J["Fanconi Anemia Pathway: FA proteins + NER + HR"]

    D --> K["Glycosylase removes base --> APE1 cuts --> Pol beta fills --> Ligase III seals"]
    E --> L["XPC detects distortion --> TFIIH unwinds --> XPF/XPG cut --> 24-32 nt removed --> Pol delta fills"]
    F --> M["MSH2/6 detects mismatch --> MLH1/PMS2 nicks new strand --> EXO1 degrades --> Pol delta fills"]
    H --> N["Compatible ends can be joined accurately;<br/>processing or misjoining may change sequence"]
    I --> O["Homologous-template-guided repair;<br/>not an error-free guarantee"]

    style A fill:#d9534f,color:#fff
    style N fill:#f0ad4e,color:#000
    style O fill:#5cb85c,color:#fff
```
<!-- alt: Flowchart showing selected DNA damage repair pathways: end structure, cell-cycle state and homologous-template availability influence outcomes; no pathway name guarantees accuracy or a fixed duration. -->

*Selected DNA damage repair pathways: end structure, cell-cycle state and homologous-template availability influence outcomes; no pathway name guarantees accuracy or a fixed duration.*

### DNA Repair Pathway Specificity and Disease Consequences

: DNA Repair Pathway Specificity and Disease Consequences: Damage Type and Repair Pathway. {#tbl:unit_IV_mutations_and_genomics_dna_repair_pathway_specificity_and_disease_consequences}
| Damage Type | Repair Pathway | Key Proteins | Disease if Defective |
|-------------|---------------|-------------|---------------------|
| UV dimers (CPD, 6-4PP) | Nucleotide excision repair (NER) | XPA, RPA, XPD, XPB, XPF-ERCC1, XPG, PCNA, Pol delta | Xeroderma pigmentosum (1,000x skin cancer risk) |
| Oxidized bases (8-oxoG) | Base excision repair (BER) | OGG1 glycosylase, APE1, Pol beta, XRCC1, Ligase III | MUTYH-associated polyposis |
| Alkylated bases (O$^6$-meG) | Direct reversal | MGMT (methyltransferase) | Glioblastoma (MGMT [**promoter**](#gl:promoter) methylation predicts temozolomide response) |
| Replication mismatch | Mismatch repair (MMR) | MLH1, MSH2, MSH6, PMS2 | Lynch syndrome (colorectal, endometrial cancer) |
| Double-strand break | NHEJ | Ku70/80, DNA-PKcs, Artemis, Ligase IV | SCID (severe combined immunodeficiency) |
| Double-strand break | Homologous [**recombination**](#gl:recombination) (HR) | ATM, MRN, BRCA1, BRCA2, RAD51, RPA | Hereditary breast/ovarian cancer |
| Interstrand crosslinks | Fanconi anemia pathway | FANC proteins (A-W), then NER + HR | Fanconi anemia (bone marrow failure, cancer) |

> **Clinical Connection: MGMT Methylation and Glioblastoma**
> Glioblastoma is the most aggressive brain tumor (median survival ~15 months). The alkylating agent **temozolomide** is a standard chemotherapy. Tumors with **MGMT promoter methylation** (silencing MGMT expression) cannot repair temozolomide-induced O$^6$-methylguanine lesions, making them more sensitive to the drug. MGMT promoter methylation status is therefore a critical predictive biomarker: methylated tumors have ~21-month median survival vs ~12 months for unmethylated tumors when treated with temozolomide (Hegi et al., 2005, *NEJM*).

### Base Excision Repair (BER) — Mechanism in Detail

BER handles oxidised, deaminated, and alkylated single-base lesions. The pathway has two main subdivisions:

**Short-patch BER (single-nucleotide replacement, ~80 % of events):**
1. **DNA glycosylase** recognizes the lesion and cleaves the N-glycosidic bond, producing an abasic (AP) site. There are 11 DNA glycosylases in humans, each with substrate specificity:

: Base Excision Repair (BER) — Mechanism in Detail: Glycosylase and Lesion recognized. {#tbl:unit_IV_mutations_and_genomics_base_excision_repair_ber_mechanism_in_detail}
| Glycosylase | Lesion recognized | Notes |
| ----------- | ----------------- | ----- |
| **OGG1** | 8-oxoguanine paired with C | Most clinically important; oxidative damage; bifunctional (lyase activity creates SSB) |
| **MUTYH** | Adenine misincorporated opposite 8-oxoG (post-replication mismatch) | Loss-of-function → MUTYH-associated polyposis (MAP) |
| **NTH1** | Oxidised pyrimidines (thymine glycol, dihydrouracil) | Bifunctional |
| **NEIL1, NEIL2, NEIL3** | Ring-fragmented purines (FapyG, FapyA), oxidised pyrimidines | Bifunctional; β,δ-elimination produces 3′-phosphate end |
| **MPG (AAG)** | 3-methyladenine, 7-methylguanine, ethenoadenine | Monofunctional (no lyase) |
| **UNG (uracil DNA glycosylase)** | Uracil (deamination product or U mis-incorporation) | Most active; nuclear and mitochondrial isoforms |
| **TDG** | Thymine in T:G mismatch (5mC deamination); 5fC/5caC (TET pathway) | Active in DNA demethylation |
| **SMUG1** | Uracil; backup to UNG | Monofunctional |
| **MBD4** | Thymine in T:G mismatch at CpG sites | Methylation-CpG specific |
| **MYH (MUTYH)** | A from A:8-oxoG mispair | See above |

2. **AP endonuclease (APE1, also called APE)** cuts the DNA backbone 5′ to the AP site, leaving a 3′-OH and a 5′-deoxyribose phosphate (dRP) terminus.
3. **DNA polymerase β (pol β)** has both DNA polymerase activity (fills the 1-nt gap with the correct nucleotide) and **dRP lyase activity** (removes the 5′-dRP).
4. **DNA ligase III + XRCC1** seals the resulting nick (ATP-dependent).

**Long-patch BER (2–10 nucleotide replacement, ~20 % of events):**
- Used when the dRP cannot be removed (e.g., oxidised dRP) or when the lesion creates a strand-displacement intermediate.
- DNA pol δ/ε extends, displacing the 5′ flap; **FEN1** cleaves the flap; **DNA ligase I** seals.

**OGG1 mechanism specifically** (the most studied glycosylase):
- OGG1 scans DNA for 8-oxoguanine. The 8-oxoG flips out of the helix into OGG1's catalytic pocket.
- Active-site lysine (K249) acts as nucleophile, attacking the C1′ of the deoxyribose; the N-glycosidic bond breaks via a Schiff-base intermediate.
- A second active-site residue (D268) hydrolyses the intermediate, releasing the 8-oxoG base and leaving an AP site.
- OGG1 is bifunctional: a β-elimination at the 3′ phosphate produces a 3′-α,β-unsaturated aldehyde, which APE1 must process before pol β can extend.
- 8-oxoG is mutagenic because it pairs with adenine (Hoogsteen face) instead of cytosine — leading to G:C → T:A transversions if not repaired.

**Clinical link — MUTYH-associated polyposis (MAP):** Biallelic loss-of-function mutations in MUTYH cause autosomal recessive colorectal polyposis. The mechanism: OGG1 normally removes 8-oxoG, but if 8-oxoG escapes repair and is replicated, it pairs with A. MUTYH normally removes that A; without MUTYH, the A becomes fixed as a G:C → T:A transversion. MAP tumors have a characteristic mutational signature (transversions at GAA contexts).

### Comparing NER and MMR — A Side-by-Side Table

The pathways have distinct substrates and proteins, often confused. Here is a direct comparison:

: Comparing NER and MMR — A Side-by-Side Table: Feature and Nucleotide Excision Repair (NER). {#tbl:unit_IV_mutations_and_genomics_comparing_ner_and_mmr_a_side_by_side_table}
| Feature | Nucleotide Excision Repair (NER) | Mismatch Repair (MMR) |
| ------- | --------------------------------- | --------------------- |
| **Substrate** | Bulky helix-distorting lesions: CPDs, 6-4 photoproducts, cisplatin adducts, polycyclic aromatic hydrocarbons | Mismatched bases (G-T, A-C); small (1–13 nt) insertion/deletion loops |
| **Recognition** | Helix distortion or transcription stalling | Mismatch geometry directly bound by MutSα/β |
| **Initiation timing** | Any cell-cycle phase | Post-replicative (S/G2) |
| **Strand discrimination** | Both strands repaired | New strand identified by transient nicks (5′ direction in eukaryotes; HMGB1) |
| **Primary recognition factor** | XPC-RAD23B (GG-NER); CSA-CSB (TC-NER, transcription-coupled) | MSH2-MSH6 (MutSα; mismatches and 1-nt loops); MSH2-MSH3 (MutSβ; 2–13-nt loops) |
| **Verification factor** | TFIIH (XPB-helicase 3′→5′; XPD-helicase 5′→3′) — unwinds ~25 bp | MLH1-PMS2 (MutLα; endonuclease) makes incision |
| **Excision** | XPF-ERCC1 (5′ cut), XPG (3′ cut); 24–32 nt fragment removed | Exonuclease 1 (Exo1) degrades from MutLα cut to past mismatch; ~150 nt fragment removed |
| **Synthesis** | Pol δ/ε with PCNA, RFC | Pol δ |
| **Ligation** | DNA ligase I | DNA ligase I |
| **Disease (loss-of-function)** | Xeroderma pigmentosum (XPA–XPG, ~1,000× skin cancer); Cockayne syndrome (CSA, CSB; premature aging) | Lynch syndrome / HNPCC (MLH1, MSH2, MSH6, PMS2; 50–80% lifetime CRC risk; MSI-high tumors) |
| **Therapeutic relevance** | Cisplatin sensitivity correlates with NER capacity | MSI-high tumors respond to anti-PD-1 (pembrolizumab) due to high neoantigen load |

### HR vs NHEJ — Pathway Choice Mechanism

The choice between homologous recombination (HR) and non-homologous end joining (NHEJ) is regulated by cell-cycle phase and a competition at the broken DNA ends.

**Pathway-determining factors:**

: HR vs NHEJ — Pathway Choice Mechanism: Step and NHEJ-favoring. {#tbl:unit_IV_mutations_and_genomics_hr_vs_nhej_pathway_choice_mechanism}
| Step | NHEJ-favoring | HR-favoring |
| ---- | -------------- | ------------ |
| Cell-cycle context | Can operate across the cycle; often important in G1/G0 | Sister-based routes favored when a sister is available in S/G2; homologous templates are not definitionally limited to sisters |
| End recognition | **Ku70/Ku80** binds ends | Resection competence and end-associated factors influence pathway engagement |
| End processing | **DNA-PKcs** and end-processing/ligation factors; processing depends on substrate | **MRN complex** (MRE11–RAD50–NBN) participates in resection initiation |
| End-resection regulator | **53BP1** + **RIF1** + **PTIP** + **shieldin** complex (REV7-MAD2L2-SHLD1/2/3) — protects ends from resection | **CtIP** (CDK-phosphorylated in S/G2) + **MRN** initiates resection; **EXO1** + **DNA2** + **BLM** extend resection |
| Fidelity | Compatible-end joining can preserve sequence; processing or wrong-end joining can alter it | Template choice, synthesis and resolution affect outcome; no error-free guarantee |
| Kinetics | End compatibility, processing and preparation affect measured rate | Resection, template search, synthesis and preparation affect measured rate |
| Key proteins (after end-recognition) | DNA-PKcs, Artemis (nuclease), XRCC4, Ligase IV, XLF/Cernunnos, PAXX | RPA → BRCA2 → RAD51 (filament) → strand invasion → D-loop → resolution |
| Outcome | Direct joining with or without a changed junction | Template-guided synthesis can restore sequence or yield conversion/rearrangement outcomes |

**Cell-cycle-dependent regulation is not an exclusive switch.** CDK/CtIP-linked resection regulation and end protection influence pathway use, but cycle phase alone does not specify substrate, template or final sequence. In the cited complementary-end experiments, canonical end joining preserved some junctions accurately \citep{guirouilhbarbat2007nhej}; this refutes an intrinsically error-prone classification without making every NHEJ event accurate.

**BRCA1/53BP1 balance is context dependent.** End protection and resection influence repair-pathway engagement; they are not a single competition for one histone mark or a direct BRCT–MDC1 recognition rule. In the studied Brca1-mutant cell models, loss of 53BP1 promoted end processing, restored the measured HR response and reduced PARP-inhibitor hypersensitivity, whereas Lig4 loss did not rescue the HR defect \citep{bunting2010resection}. That experimental distinction does not guarantee HR restoration or drug resistance for every BRCA1 variant or tumor.

**BRCA2 and RAD51 loading.** After resection, RPA coats exposed ssDNA; BRCA2 supports RAD51 filament formation on that substrate. Defective BRCA2 can impair homologous repair, but this is not a universal rate-limiting-step assignment. PARP-inhibitor response requires variant-, cell- and treatment-specific evidence rather than an automatic sensitivity prediction from a pathway name (see \cref{sec:unit_IV_dna_replication_and_cell_cycle}).

**Ku70/80 and end access.** Ku binds DNA ends and can restrain resection. End-bound complexes, substrate processing and the relevant removal pathways influence access by other repair machinery; neither a single binding constant nor one mandatory proteasomal route establishes a universal NHEJ-versus-HR kinetic ranking.

> **Concept Check (Analysis):** MMR strand discrimination is system-specific: the methylation/MutH model applies to organisms such as E. coli, not all bacteria, while nick-directed mechanisms operate in other systems. (a) In a stipulated error-correction calculation, take an incoming mismatch rate of $10^{-7}$ per copied base and removal of 99.9% by MMR. Calculate the residual rate and fold difference if this removal is absent; these assumptions do not measure a universal polymerase or clinical mutation rate. (b) Explain how inherited heterozygosity and a somatic second hit can raise Lynch-syndrome cancer risk without implying that every carrier develops an adult tumor. Compare expected MSI/IHC patterns with an MMR-proficient control, and explain why germline and appropriate tumor testing are needed rather than diagnosing inherited disease from MSI alone.

**Concept Check 13.2**

> 1. Why is the Ames test performed with and without liver microsomal extract (S9)?
> 2. Explain why MGMT is called a "suicide [**enzyme**](#gl:enzyme)."
> 3. A patient has mutations in both BRCA1 [**allele**](#gl:allele)s. Which repair pathway is defective? Why does this predispose to breast/ovarian cancer rather than most cancer types?
> 4. Compare the fidelity of NHEJ and HR. When would each be preferred?

---

## CRISPR-Cas9: Mechanism and Applications

**Background**: CRISPR (Clustered Regularly Interspaced Short Palindromic Repeats) is the adaptive immune system of bacteria and [**archaea**](#gl:archaea). Jennifer Doudna and Emmanuelle Charpentier received the 2020 Nobel Prize in Chemistry for demonstrating that CRISPR-Cas9 could be programmed with a synthetic guide RNA for precise genome editing (Jinek et al., 2012, *Science*).

### Natural CRISPR Immunity

In bacteria, CRISPR functions as immunological memory:

1. **Adaptation**: When a bacterium survives phage infection, a short sequence from the phage genome (the **protospacer**) is integrated into the CRISPR array as a new **spacer** between repeat sequences
2. **Expression**: The CRISPR array is transcribed into pre-crRNA, which is processed (with tracrRNA in Type II systems) into mature crRNA
3. **Interference**: The crRNA guides Cas9 to complementary foreign DNA; Cas9 cleaves it, preventing subsequent infection

### Engineered CRISPR-Cas9

```mermaid
flowchart TD
    A["Select target and strategy<br/>design complementary guide"] --> B["Prepare guide and editor<br/>sgRNA or prime-editing pegRNA"]
    B --> C["Deliver selected Cas9-derived editor<br/>and guide components to cells"]
    C --> D["Guide-bound editor recognizes<br/>a compatible PAM"]
    D --> E["Local DNA unwinding<br/>guide-target pairing"]
    E --> F{Guide-Target Complementarity?}
    F -->|"No Match"| D
    F -->|"Target recognized"| Strategy{"Editing strategy?"}
    Strategy -->|"Nuclease Cas9"| G["RuvC cleaves non-target strand<br/>HNH cleaves target strand"]
    G --> H["Double-Strand Break 3 bp Upstream of PAM"]
    H --> I{Repair Pathway?}
    I -->|"No Donor Template"| J["NHEJ: Error-Prone Repair"]
    J --> K["Indels at cut site<br/>possible gene disruption"]
    I -->|"Donor Template Provided (ssODN or Plasmid)"| L["HDR: Homology-Directed Repair"]
    L --> M["Precise Gene Correction or Insertion"]
    Strategy -->|"Base editor"| N["Cas9 nickase or dCas9<br/>+ deaminase"]
    N --> O["C-to-T or A-to-G conversion<br/>without a programmed DSB"]
    Strategy -->|"Prime editor"| P["Cas9 nickase + reverse transcriptase<br/>+ pegRNA"]
    P --> Q["Targeted substitutions or small indels<br/>without a programmed DSB"]

    style A fill:#4a90d9,color:#fff
    style K fill:#f0ad4e,color:#000
    style M fill:#5cb85c,color:#fff
    style O fill:#5cb85c,color:#fff
    style Q fill:#5cb85c,color:#fff
```
<!-- alt: Flowchart showing genome-editing strategies branch before cleavage: nuclease Cas9 uses double-strand-break repair, whereas base and prime editors use deamination or nickase–reverse-transcriptase chemistry without a programmed DSB. -->

*Genome-editing strategies branch before cleavage: nuclease Cas9 uses double-strand-break repair, whereas base and prime editors use deamination or nickase–reverse-transcriptase chemistry without a programmed DSB \citep{komor2016,anzalone2019}.*

**Key molecular details**:
- **sgRNA (single guide RNA)**: A conventional SpCas9 guide fuses the crRNA spacer (about 20 nt complementary to the target) with the tracrRNA scaffold that binds Cas9. The roughly 100-nt sgRNA supplies the RNA targeting component; enzyme, compatible target and cellular repair conditions remain separate requirements.
- **PAM (protospacer adjacent motif)**: For canonical *S. pyogenes* Cas9 (SpCas9) duplex targeting, the preferred PAM is **5'-NGG-3'** on the non-target strand, immediately 3' of the target sequence. PAM recognition licenses local duplex unwinding and guide-target testing. This requirement is scoped to double-stranded DNA: in the 2012 in-vitro assays, target single-stranded DNA cleavage was unaffected by PAM mutations \citep{doudna2012}.
- **Cleavage**: The **HNH domain** cleaves the guide-complementary target strand; the **RuvC domain** cleaves the non-target strand. The canonical duplex-target schematic places the break about 3 bp upstream of the PAM; substrate-dependent non-target-strand processing in the original assays cautions against treating every product as an identical blunt end \citep{doudna2012}.

### Beyond Cas9: Expanded Toolkit

: Beyond Cas9: Expanded Toolkit: Tool and Mechanism. {#tbl:unit_IV_mutations_and_genomics_beyond_cas9_expanded_toolkit}
| Tool | Mechanism | Application |
|------|-----------|-------------|
| **Cas12a (Cpf1)** | Creates staggered DSB; T-rich PAM (TTTN); self-processes crRNA array | Multiplexed editing; organisms with AT-rich genomes |
| **Cas13 (RNA-targeting)** | Cleaves RNA (not DNA); collateral RNA cleavage in bacteria | RNA knockdown; viral RNA detection (SHERLOCK diagnostic) |
| **dCas9 (dead Cas9)** | Catalytically inactive (D10A + H840A mutations); binds but does not cut | CRISPRi (transcriptional repression with KRAB domain); CRISPRa (activation with VP64/p65/Rta) |
| **Base editors** | dCas9 or Cas9-nickase fused to deaminase | CBE (cytidine base editor): C-to-T conversion; ABE (adenine base editor): A-to-G conversion; no DSB needed |
| **Prime editors** | Cas9-H840A nickase fused to M-MLV reverse transcriptase + pegRNA | "Search-and-replace": any point mutation, small insertion, or small deletion; no DSB, no donor template needed |

**CRISPR diagnostics:** SHERLOCK and DETECTR exploit collateral nuclease activity after target recognition: Cas13 collateral RNA cleavage and Cas12a collateral ssDNA cleavage convert a sequence match into a fluorescent or lateral-flow signal \citep{gootenberg2017sherlock,chen2018detectr}. That makes CRISPR a diagnostic logic as well as an editing logic, but it does not remove the usual validation burdens: sample preparation, contamination control, limit of detection, clinical sensitivity/specificity, and variant coverage still determine whether an assay is deployable.

**Current evidence: prime editing as promoter rewriting.** Prime editing is especially useful when the desired change is not simply "cut here" but "install a small regulatory pattern." A 2025 *Blood* study used prime-editing guide RNAs to introduce multiple hereditary-persistence-of-fetal-hemoglobin-like edits into the *HBG1/HBG2* gamma-globin promoters, aiming to reactivate fetal hemoglobin without making a double-strand break \citep{chalumeau2025primeediting}. Editing efficiency varied among donor hematopoietic stem/progenitor cells, so this should be treated as early translational evidence rather than an approved therapy. The concept is powerful: regulatory DNA can be edited to change *when and where* a gene is expressed, not only whether its protein-coding sequence is intact.

### Therapeutic Applications (2024-2025)

**Casgevy (exagamglogene autotemcel)**: First CRISPR-based therapy approved by FDA for sickle cell disease (December 2023) and later for transfusion-dependent beta-thalassaemia (January 2024), with EMA authorization following in 2024. A July 2026 supplemental approval expanded the eligible population from 12 years and older to **2 years and older**, the first gene therapy cleared for sickle cell disease patients this young \citep{fda2023casgevy,fda2024casgevythalassemia,fda2026casgevy}.

- **Indication**: Sickle cell disease (SCD) and transfusion-dependent beta-thalassemia
- **Mechanism**: Ex vivo CRISPR editing of patient hematopoietic stem cells (HSCs) to disrupt the *BCL11A* erythroid enhancer. BCL11A is a repressor of fetal hemoglobin (HbF, alpha2-gamma2). Disrupting its erythroid enhancer reactivates HbF production, which does not sickle and compensates for defective HbS.
- **Results**: In SCD, the regulatory endpoint is freedom from severe vaso-occlusive crises after treatment; transfusion independence is the endpoint used for transfusion-dependent beta-thalassaemia. Early exa-cel studies also reported sustained fetal-hemoglobin induction, so the durable teaching point is endpoint specificity: the same edited cell product is judged against different disease-specific clinical outcomes \citep{fda2023casgevy,fda2024casgevythalassemia,fda2026casgevylabel}.

**NTLA-2001 (in vivo CRISPR)**:
- **Indication**: Transthyretin (ATTR) amyloidosis
- **Mechanism**: Lipid nanoparticle (LNP)-delivered Cas9 mRNA + sgRNA targeting the *TTR* gene in hepatocytes -- direct in vivo editing (no cell harvest needed)
- **Results**: Single infusion achieved 80-95% serum TTR reduction (Gillmore et al., 2021, *NEJM*)

**Safety considerations**:
- **Off-target editing**: sgRNA may bind sites with 1-3 mismatches. Mitigated by high-fidelity Cas9 variants (SpCas9-HF1, eSpCas9, HiFi Cas9) and careful guide RNA design (off-target prediction algorithms: Cas-OFFinder, CRISPOR)
- **Immunogenicity**: ~79% of humans have pre-existing antibodies to SpCas9; strategies include using Cas9 from other species or transient delivery (mRNA/RNP vs. viral vectors)
- **NHEJ:HDR ratio**: ~1000:1 in non-dividing cells (most therapeutically relevant cells); S/G2 phase favors HDR; base editors and prime editors circumvent this limitation

> **Clinical Connection: Base Editing for Sickle Cell Disease**
> On the HBB coding DNA strand, wild type is GAG (Glu), sickle is GTG (Val), and Makassar is GCG (Ala). A complementary-strand A-to-G edit can produce coding T-to-C, converting GTG to GCG; it does not revert GTG to GAG. Regulatory editing that raises γ-globin is distinct from direct HBB coding conversion. Avoiding programmed double-strand breaks does not remove bystander, off-target, or delivery risks; maturity must be documented for the actual program, not inferred from editor class.

**Mitochondrial DNA editing boundary:** Standard CRISPR-Cas systems work poorly for mtDNA because guide RNAs are difficult to import into mitochondria. DddA-derived cytosine base editors (DdCBEs) solve part of the problem by using TALE-DddA protein fusions to install targeted C$\cdot$G-to-T$\cdot$A edits in mtDNA without guide RNA \citep{mok2020mitochondrialbaseediting}. This is a major tool advance, not a general approved therapy: heteroplasmy, off-target editing, delivery, selectable mutation classes, and tissue specificity remain the current translational constraints \citep{barrerapaez2023mitochondrialediting}.

**Concept Check 13.3**

> 1. Why does canonical SpCas9 recognition of a double-stranded DNA target require a compatible PAM? Relate this to self/nonself discrimination, and distinguish the primary paper's single-stranded-DNA assay result.
> 2. Compare NHEJ and HDR outcomes after Cas9-mediated DSB. Why is HDR difficult to achieve in post-mitotic cells?
> 3. What advantage does base editing offer over standard Cas9 editing for correcting point mutations?
> 4. Explain the mechanism of Casgevy: why does disrupting BCL11A treat sickle cell disease?

---

## Genomics: The Human Genome

The **Human Genome Project** (1990-2003; Venter et al., 2001 and International Human Genome Sequencing Consortium, 2001) produced the first draft reference. The **T2T Consortium** (Nurk et al., 2022) completed the first truly gapless reference genome (CHM13), filling ~8% of previously unresolvable sequence (centromeres, [**telomere**](#gl:telomere)s, segmental duplications, rDNA arrays).

### Human Genome Composition

: Human Genome Composition: Component and Fraction. {#tbl:unit_IV_mutations_and_genomics_human_genome_composition}
| Component | Fraction | Details |
|-----------|----------|---------|
| Protein-coding exons | ~1.5% | ~19,000-20,000 genes; average gene ~27 kb; average of 8.8 exons |
| Introns | ~26% | Average intron ~3.4 kb; some >100 kb |
| Transposable elements | ~46% | LINEs (21%, especially L1), SINEs (13%, especially Alu), DNA transposons (3%), LTR retrotransposons (9%) |
| Intergenic sequence | ~15% | Includes regulatory elements, structural sequences |
| Non-coding RNA genes | ~5,000+ loci | lncRNAs, miRNAs, snRNAs, snoRNAs, rRNAs, tRNAs |
| Simple sequence repeats | ~3% | Microsatellites (1-6 bp repeat units) and minisatellites (7-100 bp) |
| Segmental duplications | ~5% | Blocks >1 kb with >90% sequence identity; hotspots for chromosomal rearrangement |

### Transposable Elements — Mechanism and Genomic Impact

Transposable elements (TEs) make up ~46 % of the human genome — far more than the ~1.5 % occupied by protein-coding exons. They are ancient mobile DNA elements that have shaped genome architecture over evolutionary time. They fall into three major classes:

**Class I — RNA-mediated retrotransposons (copy-and-paste; majority of human TEs):**

1. **LINE-1 (Long Interspersed Nuclear Element 1)** — a human retrotransposon family with full-length elements of roughly 6 kb and many fragmented or inactive copies. Assembly-specific copy counts and a defined activity assay are needed before estimating the retrotransposition-competent subset.
   - Encodes ORF1 (RNA-binding chaperone) and ORF2 (with reverse-transcriptase + endonuclease activities)
   - **Retrotransposition mechanism (Target-Primed Reverse Transcription, TPRT):**
     1. L1 transcribed by Pol II → L1 mRNA (~6 kb, capped, polyadenylated)
     2. L1 mRNA exported to cytoplasm, translated to ORF1p and ORF2p
     3. Cis-binding of ORF1p/ORF2p to their own mRNA forms a ribonucleoprotein (RNP)
     4. RNP enters nucleus
     5. ORF2p endonuclease nicks genomic DNA at TTAAAA-like sites, exposing 3′-OH
     6. The 3′-OH primes reverse transcription using L1 mRNA as template
     7. Second-strand DNA synthesis completes integration
     8. Target site duplication (TSD; 7–20 bp) flanks the new insertion, plus a poly-A tail at the 3′ end
   - Most insertions are 5′-truncated due to incomplete RT
   - In the studied L1.3-transfected HeLa preparations, L1 expression produced endonuclease-dependent damage signals and COMET evidence of fragmentation \citep{gasior2006l1damage}. Detected damage events were not equivalent to successful insertions. This does not establish an endogenous 100-nicks-per-cell-per-day rate; transcriptional repression and failure to complete an already initiated TPRT event are distinct mechanisms.

2. **Alu elements (Short Interspersed Nuclear Element 1, SINE)** — ~13 % of human genome; ~1.1 million copies; ~300 bp.
   - Derived from 7SL RNA (signal recognition particle component); contain RNA Pol III internal promoter
   - **Mobilization requires L1 machinery** (parasitic on LINE-1's ORF2p RT/endonuclease)
   - Transcription by Pol III; the Alu RNA recruits L1 ORF2p in *trans* and inserts via the same TPRT mechanism
   - Alu elements are densest in gene-rich regions; insertions in introns can disrupt splicing or create new alternative exons

3. **SVA elements (SINE-VNTR-Alu)** — ~3,000 copies; ~2 kb; younger than Alu (~25 Mya). Hybrid composite.

4. **LTR retrotransposons (HERV — human endogenous retroviruses)** — ~9 % of genome; relics of ancient retroviral insertions. Most are inactivated; some HERV-K elements remain intact and may be re-activated in cancer.

**Class II — DNA transposons (cut-and-paste; ~3 % of human genome):**
- Most inactivated in modern human genome (no active class II TE in humans)
- Mechanism: a transposase enzyme (encoded by the TE) recognizes terminal inverted repeats (TIRs) flanking the element, excises the element, and re-integrates it elsewhere
- Mariner / Tc1, hAT, P-element families most derive from class II
- Hyperactive synthetic DNA transposons (e.g., **Sleeping Beauty**, **PiggyBac**) are now used as gene-delivery tools in research and CAR-T therapy

**Genomic and clinical impact of TE insertions:**
- Ewing and Kazazian's 2010 population-model estimate was one L1 retrotransposition per 95–270 live births, under demographic assumptions; this is not 100 new L1/Alu insertions per child \citep{ewing2010l1}.
- TE insertions can disrupt coding or regulatory sequence. Disease fractions and somatic insertion counts depend on tissue, detection method, and denominator; no universal neuron or disease-mutation percentage is supplied here.
- Cancer cells often re-activate TE expression (LINE-1 demethylation is a hallmark of global cancer hypomethylation), contributing to chromosomal instability and inflammation

**Defense mechanisms against TE activity:**
- **DNA methylation** of TE promoters (DNMT3A/B targets active TE families during germline development)
- **KRAB-ZFP transcriptional repression**: > 350 KRAB-zinc finger proteins recognize specific TE families and recruit KAP1/TRIM28 → SETDB1 → H3K9me3 silencing
- **piRNA pathway** in germline: piRNAs (26–32 nt) bind PIWI clade Argonautes (PIWIL1/MILI, PIWIL4/MIWI2) and silence TEs via the "ping-pong amplification" cycle
- **APOBEC3 deaminases**: cytidine deaminases that mutate TE-derived ssDNA, restricting retrotransposition and HIV integration

### Structural Variants — Inversions, CNVs, and Disease

**Inversions** are large segments of DNA flipped end-to-end. Unlike SNPs, they are difficult to detect by short-read sequencing (the inversion preserves sequence content, primarily orientation changes). Long-read sequencing (PacBio HiFi, Oxford Nanopore) and optical mapping (Bionano Saphyr) have revealed:
- Population inversion catalogs pooled across people are not counts per individual. Inversions can disrupt genes or change regulatory topology; breakpoint-spanning evidence and phasing test their effects. Casgevy deliberately disrupts an erythroid BCL11A enhancer; its rationale does not require an asserted universal inversion mechanism.

**Copy Number Variants (CNVs)** are duplications or deletions of segments > 1 kb. Two major mechanisms:
- **Non-allelic homologous recombination (NAHR)** between segmental duplications (low-copy repeats, LCRs) — produces recurrent CNVs at predictable breakpoints (e.g., 22q11.2 microdeletion, 16p11.2 micro-CNV)
- **Replication-based mechanisms (FoSTeS, MMBIR)** — produce non-recurrent CNVs at variable breakpoints

**CNVs in autism and schizophrenia:**

: Structural Variants — Inversions, CNVs, and Disease: Locus and Size. {#tbl:unit_IV_mutations_and_genomics_structural_variants_inversions_cnvs_and_disease}
| Locus | Size | Phenotype | Frequency in cases vs controls |
| ----- | ---- | --------- | ----------------------------- |
| **16p11.2** (deletion or duplication) | ~600 kb | Autism, intellectual disability, obesity (deletion) | ~1 % of autism cases vs 0.04 % controls |
| **22q11.2** (deletion = DiGeorge syndrome / 22q11DS) | ~3 Mb | Schizophrenia (~25 % of carriers), congenital heart disease, palatal defects | ~25 % schizophrenia risk |
| **15q11–13** (duplication of maternal allele) | ~4 Mb | Autism, epilepsy | ~1 % of autism |
| **NRXN1** (Neurexin-1) (heterozygous deletion) | Variable, exonic | Autism, schizophrenia, intellectual disability | 5–10× enrichment |
| **CNTNAP2** (heterozygous loss) | Variable, exonic | Autism, language delay, epilepsy | Modest enrichment |
| **3q29** (microdeletion) | ~1.6 Mb | Schizophrenia (~40× risk increase) | Rare but high penetrance |
| **22q11.2** (microduplication) | 1.5–3 Mb in the cited study | Lower schizophrenia association in the combined study; ASD/developmental outcomes are distinct, not excluded | Rees et al.: 3/21,138 schizophrenia cases vs 22/25,867 controls; OR 0.17 (95% CI 0.050–0.56). Incomplete protection, not a deterministic carrier prognosis \citep{Rees2014Duplication} |
| **1q21.1** (deletion or duplication) | ~1.4 Mb | Schizophrenia, autism, microcephaly (deletion) | ~10× risk |
| **15q13.3** (deletion) | ~1.5 Mb | Schizophrenia, epilepsy (deletion) | ~10× risk |

**Why CNVs are so impactful:** Each CNV affects 1–5 dosage-sensitive genes simultaneously. The cumulative effect on neural development is large because brain development depends on stoichiometric protein interactions. Rare CNVs (occurring in < 1 % of population) collectively explain ~5 % of schizophrenia cases and ~10 % of autism cases — a substantial fraction of risk despite each individual CNV being rare.

> **Concept Check (Synthesis):** Copy number variation (CNV) is a class of structural genetic variation in which segments of $\geq 1$ kb are duplicated or deleted. A major mechanism is non-allelic homologous recombination (NAHR) between flanking segmental duplications. (a) Chromosome 15q11–q13 carries large segmental duplications that flank the Prader–Willi / Angelman syndrome region. Explain why this architecture predisposes the region to recurrent microdeletions and microduplications, and predict the phenotypic consequence of a paternally vs. maternally inherited deletion — the answer should invoke genomic imprinting at SNRPN and UBE3A. (b) The 22q11.2 deletion syndrome (the molecular basis of DiGeorge / velocardiofacial syndrome) occurs in roughly 1 in 4,000 live births, making it one of the most common recurrent microdeletion syndromes in humans. Given that NAHR drives most recurrence, sketch how the expected deletion frequency should scale with (i) the length of the flanking segmental duplications, (ii) the percent sequence identity between them, and (iii) the genomic distance separating them. Use this to argue why 22q11.2 is so structurally unstable relative to a hypothetical CNV interval flanked by 5 kb duplications at 90% identity.

### Genomic Variation Across SNVs, Structural Variants, and Haplotypes

- **Single nucleotide polymorphisms (SNPs)**: ~1 per 300 bp on average; the human genome contains ~4-5 million SNPs per individual relative to the reference. Most are neutral; ~2% in coding regions; ~0.5% are missense.
- **Indels**: ~500,000 per genome; usually 1-50 bp
- **Copy number variants (CNVs)**: ~1,000 per genome; collectively encompass ~4 Mb
- **Structural variants (SVs)**: inversions, translocations, large insertions; ~2,500 per genome
- **Two individuals differ by ~0.1% of their genomes (~3 million SNPs)**, but most variation is within populations rather than between populations (Lewontin, 1972; Fst ~0.12).

### The ENCODE Project

The **ENCODE** (Encyclopedia of DNA Elements) Project (2003-present) systematically mapped functional elements in the human genome:

- **Key finding**: >80% of the genome has at least one biochemical function ([**chromatin**](#gl:chromatin) accessibility, transcription factor binding, [**histone**](#gl:histone) modification, RNA transcription)
- **Revised "junk DNA" narrative**: Much non-coding DNA has regulatory function (enhancers, insulators, lncRNAs); however, "biochemical activity" does not necessarily mean "biologically important" (ongoing debate)
- **~400,000 enhancers** identified; most disease-associated SNPs (from GWAS) fall in non-coding regulatory regions, not protein-coding genes

---

## Next-Generation Sequencing Technologies

```mermaid
flowchart LR
    A[Genomic DNA Extracted] --> B{Sequencing Platform?}
    B -->|Short-Read| C["Illumina Sequencing-by-Synthesis"]
    B -->|Long-Read| D["Oxford Nanopore / PacBio"]

    C --> E["Fragment DNA (300-500 bp)"]
    E --> F["Ligate Adapters; Bridge Amplification on Flow Cell"]
    F --> G["Sequencing-by-Synthesis: Fluorescent Reversible Terminators"]
    G --> H["Read Length: 150-300 bp Paired-End"]
    H --> I["Output: ~600 Gb per Run (NovaSeq)"]

    D --> J["Nanopore: DNA Passes Through Protein Pore"]
    J --> K["Current Changes Identify Each Base in Real Time"]
    K --> L["Read Length: >100 kb (Record: >4 Mb)"]

    D --> M["PacBio HiFi: Circular Consensus Sequencing"]
    M --> N["Polymerase Reads Circular Template Multiple Times"]
    N --> O["Read Length: 10-25 kb; Accuracy: >99.9%"]

    I --> P{Assembly Strategy?}
    L --> P
    O --> P
    P -->|"Known Species"| Q["Reference-Guided Mapping (BWA, Minimap2)"]
    P -->|"New Species"| R["De Novo Assembly (hifiasm, Shasta)"]
    Q --> S["Variant Calling (GATK, DeepVariant)"]
    R --> T["Contig Assembly --> Scaffolding --> Gap Filling"]

    style A fill:#4a90d9,color:#fff
    style I fill:#5cb85c,color:#fff
    style L fill:#5cb85c,color:#fff
    style O fill:#5cb85c,color:#fff
```
<!-- alt: Flowchart showing genomic sequencing approaches. Short-read (Illumina) provides high throughput and accuracy for variant calling; long-read (Nanopore, PacBio HiFi) resolves structural variants, repeats, and enables de novo assembly. -->

*Genomic sequencing approaches. Short-read (Illumina) provides high throughput and accuracy for variant calling; long-read (Nanopore, PacBio HiFi) resolves structural variants, repeats, and enables de novo assembly.*

### Pangenome Graph Reasoning

The old mental model of a genome reference was a single linear string. That is still useful, but it hides ancestry-specific haplotypes, structural variants, alternate gene copies, and repeat-resolved sequence that do not align cleanly to one coordinate path. The Human Pangenome Reference Consortium's 2023 draft reference introduced a graph built from 47 diverse individuals and 94 phased haplotypes; its 2025 Release II expanded the resource to assemblies from 232 individuals with high-quality phased assemblies; the May 12, 2025 announcement described comprehensive annotations and graph alignments as forthcoming, so later availability requires release-specific artifacts \citep{humanpangenome2023,hprc2025release2}. In a graph, a variant is not merely "different from the reference"; it is a path through an explicitly represented set of alternatives. This improves reasoning about structural variation and representation, while adding new validation obligations: graph alignment, annotation transfer, clinical reporting, and population sampling must become part of the claim.

```mermaid
flowchart LR
    L["Single linear reference"] --> M["Reads forced onto one path"]
    M --> N["Small variants called well"]
    M --> O["Structural variants and ancestry-specific alleles can be missed"]

    P["Pangenome graph"] --> Q["Shared backbone plus alternate paths"]
    Q --> R["SNPs, indels, inversions, insertions, and haplotypes represented"]
    R --> S["Variant interpretation with path evidence"]
    S --> T["Clinical claim requires graph-aware validation"]
```
<!-- alt: Flowchart showing pangenome graph reasoning. A graph reference turns population variation into explicit alternate paths, improving structural-variant interpretation while making validation and reporting more complex. -->

*Pangenome graph reasoning. A graph reference turns population variation into explicit alternate paths, improving structural-variant interpretation while making validation and reporting more complex.*

: Pangenome Graph Reasoning: Technology and Read Length. {#tbl:unit_IV_mutations_and_genomics_pangenome_graph_reasoning}
| Technology | Read Length | Accuracy | Throughput | Cost (30x Human Genome) | Key Application |
|-----------|-----------|----------|-----------|------------------------|-----------------|
| Illumina NovaSeq X | 150-300 bp | >99.9% (Q30+) | ~600 Gb/run | ~$200 | Variant calling, RNA-seq, exome |
| PacBio Revio (HiFi) | 10-25 kb | >99.9% (consensus) | ~90 Gb/run | ~$1,000 | Structural variants, de novo assembly, [**epigenetics**](#gl:epigenetics) |
| Oxford Nanopore PromethION | >100 kb possible | ~99% (Q20+) | ~100 Gb/run | ~$500 | Real-time sequencing, field deployment, direct RNA sequencing |

---

## Genome-Wide Association Studies (GWAS)

GWAS identify genetic variants (typically SNPs) associated with complex traits or diseases by comparing allele frequencies between cases and controls.

**Methodology**:
1. Genotype hundreds of thousands to millions of SNPs across the genome in large cohorts (typically >10,000 individuals)
2. Test each SNP for association with the [**phenotype**](#gl:phenotype) using logistic regression (binary traits) or linear regression (quantitative traits)
3. Apply a stringent significance threshold ($p < 5 \times 10^{-8}$) to account for ~1 million independent tests (Bonferroni-like correction)
4. Display results on a **Manhattan plot**: genomic position (x-axis) vs. $-\log_{10}(p)$ (y-axis); significant associations appear as peaks above the genome-wide significance line

**Key concepts**:
- **[Linkage](#gl:linkage) disequilibrium (LD)**: Non-random association of alleles at nearby loci. A significant SNP may not be the causal variant but rather in LD with it (a "tag SNP").
- **Effect sizes**: Most GWAS-identified variants have small effect sizes (odds ratio 1.1-1.3); complex traits are highly polygenic
- **Missing heritability**: GWAS variants collectively explain primarily a fraction of heritability for most traits (e.g., ~25% of height heritability, despite identifying >700 loci)

**Examples of GWAS discoveries**:
- Type 2 diabetes: >400 loci, including TCF7L2 (strongest effect), PPARG, KCNJ11
- Age-related macular degeneration: CFH (complement factor H) -- led to complement-targeted therapies
- Autoimmune diseases: HLA region as the strongest risk factor for type 1 diabetes, celiac disease, rheumatoid arthritis

---

## Comparative Genomics and Molecular Evolution

**Synteny**: Conservation of gene order between species. Humans and mice share ~90% of genes in syntenic blocks, despite 75-80 million years of divergence.

**Conserved non-coding elements (CNEs)**: ~5% of the human genome is under purifying selection (much more than the ~1.5% that encodes protein). These conserved regions likely include enhancers, silencers, and structural elements essential for gene regulation.

**Ultraconserved elements (UCEs)**: A particularly remarkable subset — ~481 segments of ≥ 200 bp that are perfectly identical (100 % sequence identity) across human, mouse, and rat genomes (Bejerano et al., 2004 *Science*). These elements have remained unchanged for ~80 million years, implying extreme purifying selection. UCEs cluster near developmental transcription factors (e.g., *DACH1*, *POU3F2*) and are enriched in enhancers controlling early embryonic patterning. Their function remains incompletely understood — paradoxically, knocking out individual UCEs in mice produces primarily subtle phenotypes, raising questions about why selection is so strong if redundancy is high.

**Comparative-genomics signals used to investigate selection:** These are model-dependent observations, not a lookup table proving adaptation. Neutral demographic, recombination, mutation-rate and ascertainment models must be considered; concordant statistics can share the same confounder. A functional assay establishes a specified phenotype, not by itself the historical fitness advantage \citep{tajima1989neutrality,nielsen2005selection,sabeti2007selection}.

: Selection-related sequence signals and their inferential limits. {#tbl:unit_IV_mutations_and_genomics_pangenome_graph_reasoning_2}
| Signature | Detection method | Interpretation |
| --------- | ----------------- | -------------- |
| Conserved across species | phastCons, phyloP and phylogenetic rate comparisons | Consistent with constraint relative to an appropriate neutral background; does not identify a specific biological function by itself |
| Conserved background with lineage-specific acceleration | Lineage-specific substitution-rate tests | May reflect adaptive change, relaxed constraint or another rate/bias process; acceleration alone does not establish a disease mechanism |
| Population differentiation or asymmetric haplotype extent | Fst outlier comparisons, XP-EHH | Candidate population-specific selection after calibration; Fst is not a fixation count, and population structure can create outliers |
| $d_N/d_S>1$ under a tested codon model | PAML/codeml model comparisons | Can support positive protein-level selection with alignment/model checks; a gene name alone is not evidence of a sweep |
| Negative Tajima's D | Standardized difference between pairwise and segregating-site diversity estimates | Excess low-frequency variation relative to the specified null; growth, selection and other departures can produce it |
| Extended haplotype homozygosity or long-range LD | iHS, EHH and related haplotype comparisons | Candidate sweep signal conditional on allele frequency, recombination, demography and ascertainment; not standalone proof of adaptation |

### Mutation Rates — Spontaneous vs Induced

Mutation evidence depends on cellular context, exposure, repair and ascertainment. As in the unsorted `MutationRateEvidence` catalog, each quantitative estimate needs its own target and time basis. This table separates inherited substitution rates, DNA damage and accumulated somatic burden; its rows are not a common rate scale.

: Mutation evidence: rates, damage and somatic burden with distinct measurement bases. {#tbl:unit_IV_mutations_and_genomics_mutation_rates_spontaneous_vs_induced}
| Context | Metric or process | Evidence boundary |
| ------- | ----------------- | ----------------- |
| Human germline, family quartet | ≈1.1 × 10⁻⁸ substitutions per position per haploid genome per generation | Direct family estimate \citep{roach2010inheritance}; not a universal constant |
| Human germline, Icelandic trios | 1.20 × 10⁻⁸ substitutions per nucleotide per generation | 78 trios; mean paternal age 29.7 years; source-specific estimate \citep{kong2012germline} |
| Human somatic tissues | Accumulation in a sampled cell lineage | Per-year burden is not per-division rate without a division history |
| Wild-type *E. coli* and yeast | Replication fidelity and repair limit mutation | Rates require strain, growth conditions, target and assay |
| MMR-deficient *E. coli* | Loss of mismatch correction can elevate mutation | A fold change requires a matched strain and the same mutation target |
| UV exposure | CPDs and 6-4 photoproducts are DNA lesions | Wavelength, fluence and repair interval matter; lesions are not fixed substitutions |
| Ionizing radiation | Strand breaks and other DNA lesions | DSBs per cell per dose are damage yield, not mutations per base |
| Tobacco exposure | ≈150 substitutions per cell per pack-year, inferred for lung | Cancer-sequence regression; inferred normal-cell accumulation, not missense count |
| EMS exposure | Alkylation can produce G:C → A:T transitions | Mutation yield depends on organism, dose, exposure time and target |
| 5-FU treatment | Thymidylate synthase inhibition and nucleotide mis-incorporation | Treatment response and mutation accumulation are distinct outcomes |
| MMR-deficient tumors | Microsatellite instability and altered mutation burden | Tumor burden is not a germline or per-division rate; Lynch syndrome is inherited predisposition |
| MUTYH-associated polyposis | Defective repair of adenine opposite 8-oxoG | Does not imply simultaneous OGG1 deficiency or one universal fold increase |
| BRCA1/2-deficient tumors | Defective homologous recombination can alter structural-variant patterns | Neither a unique rearrangement pattern nor a common per-base rate follows |
| POLE proofreading-deficient tumors | High accumulated substitution burden and characteristic signatures | Specific pathogenic variants matter; tumor burden is not per-generation rate |

The tobacco estimate comes from Alexandrov et al. (2016), who related cancer mutation catalogs to cumulative smoking exposure \citep{alexandrov2016smoking}. One pack-year means one pack per day for one year. Their estimate is not a direct longitudinal measurement of normal lung epithelium. Signature 4 is dominated by C→A substitutions and resembles the experimental benzo&#91;a&#93;pyrene signature; substitutions are not necessarily coding or missense.
In a prospective trial of nivolumab in advanced MMR-proficient, POLE-mutated solid tumors, Rousseau et al. (2022) found that selected pathogenic proofreading-domain variants were associated with high burden and response, whereas variants not affecting proofreading derived no benefit \citep{rousseau2022pole}. A POLE variant alone does not establish proofreading deficiency, and even that deficiency is not a guarantee of response for every patient.

**Mutation counts are not evolutionary limits.** The teaching calculation in \cref{eq:mutations_per_gen} estimates new single-base substitutions under stated assumptions, not a universal maximum per child, a count of deleterious alleles or proof of an adaptation optimum. Mutation supplies variation, while selection and drift affect its persistence; observed rates also reflect molecular mechanisms and measurement choices. Muller's ratchet concerns stochastic loss of the least mutation-loaded class in finite, non-recombining populations, not a universal ceiling on human germline mutation. Comparisons among microbes, mammals and viruses require matched mutation classes, targets and generation definitions rather than an organism ranking from heterogeneous estimates.

**Gene duplication and divergence** \citep{ohno1970}: Whole-genome duplications (WGD) and segmental duplications create paralogous genes. After duplication:
- **Neofunctionalization**: One copy acquires a new function
- **Subfunctionalization**: Each copy retains a subset of the original function
- **Pseudogenization**: One copy accumulates mutations and becomes a pseudogene

**Ka/Ks ratio** (dN/dS): The ratio of nonsynonymous (amino acid-changing) to synonymous (silent) substitution rates:
- Ka/Ks < 1: purifying (negative) selection (most genes)
- Ka/Ks = 1: neutral evolution
- Ka/Ks > 1: positive (adaptive) selection (rare; examples: immune genes, reproductive proteins)

---

## Personal Genomics and Ethical Issues

### Pharmacogenomics and Evidence-Governed Prescribing

Genetic variation affects drug response:

Pharmacogenomics is strongest when it is treated as one evidence layer in prescribing rather than a deterministic label. A genotype can alter enzyme activity, transporter expression, immune recognition, or drug target sensitivity, but clinical interpretation also depends on ancestry representation in the evidence base, co-medications, age, liver and kidney function, indication, and whether the variant is actually phased or captured by the assay. Pangenome and long-read resources improve the chance of detecting structural or ancestry-associated variants missed by a single linear reference, but clinical use still requires validated phenotype links and reporting standards \citep{humanpangenome2023}.

: Pharmacogenomics and Evidence-Governed Prescribing: Gene and Drug. {#tbl:unit_IV_mutations_and_genomics_pharmacogenomics_and_evidence_governed_prescribing}
| Gene | Drug | Effect of Variant |
|------|------|-------------------|
| **CYP2D6** | Codeine, tamoxifen | Poor metabolizers: codeine ineffective (cannot convert to morphine); ultra-rapid metabolizers: toxicity risk |
| **CYP2C19** | Clopidogrel (Plavix) | Poor metabolizers: reduced anti-platelet effect; increased cardiovascular risk |
| **VKORC1 + CYP2C9** | Warfarin | Variants explain ~40% of dosing variation; FDA-approved pharmacogenomic labeling |
| **HLA-B*5701** | Abacavir (HIV) | Pre-treatment testing mandatory; positive patients have ~50% risk of hypersensitivity reaction |
| **DPYD** | 5-fluorouracil | DPD deficiency: potentially fatal toxicity; pre-treatment testing recommended in EU |

### Ethical Considerations in Personal and Clinical Genomics

- **Genetic privacy**: Genetic information reveals predisposition, not certainty. The **GINA Act** (Genetic Information Nondiscrimination Act, 2008, USA) prohibits genetic discrimination in employment and health insurance but does NOT cover life insurance, disability insurance, or long-term care insurance.
- **Direct-to-consumer (DTC) testing**: Companies like 23andMe provide ancestry and health risk information. Concerns include: limited clinical validity for most variants, potential for anxiety, and data privacy (law enforcement access to databases).
- **BRCA1/2 testing decisions**: Positive results require careful genetic counseling. Prophylactic mastectomy reduces breast cancer risk by >90% but is psychologically significant. The 2013 *Myriad Genetics* Supreme Court decision (Association for Molecular Pathology v. Myriad Genetics) ruled that naturally occurring genes cannot be patented but [**cDNA**](#gl:cdna) can be.
- **Germline editing**: Editing human embryos raises profound ethical questions. The 2018 He Jiankui case (CCR5-edited babies in China) was widely condemned as premature, reckless, and ethically unacceptable. International consensus: germline editing for reproduction should not proceed until safety and efficacy are established and broad societal consensus is reached.

> **Clinical Connection: Pharmacogenomic Testing in Practice**
> The Clinical Pharmacogenetics Implementation Consortium (CPIC) publishes evidence-based guidelines for 23+ gene-drug pairs. Pre-emptive pharmacogenomic testing (genotyping a panel of pharmacogenes before any drug is prescribed) is increasingly implemented in health systems. The PREDICT study (Vanderbilt) and RIGHT study (Mayo Clinic) demonstrated that pre-emptive testing is feasible and can prevent adverse drug reactions.

---

## Worked Example: Per-Gene De Novo Mutation Probability

**Problem:** Use an illustrative $\mu=1.2\times10^{-8}$ per coding base per generation and DMD coding target 11,058 bp per X chromosome. DMD spans a large genomic interval but is not the largest human coding sequence. Assume one X copy for an XY offspring and two for an XX offspring; disregard parental-age and site heterogeneity.

\begin{equation}\lambda_{XY}=\mu(11{,}058)=1.32696\times10^{-4},\quad\lambda_{XX}=2.65392\times10^{-4}\label{eq:dmd_cds_lambda}\end{equation}

\begin{equation}P(0)=e^{-\lambda};\quad P_{XY}(0)\approx0.9998673,\quad P_{XX}(0)\approx0.9997346\label{eq:dmd_cds_p0}\end{equation}

\begin{equation}P(\ge1)=1-e^{-\lambda}\approx\lambda\label{eq:dmd_cds_pge1}\end{equation}

These are probabilities of any new coding substitution, not Duchenne incidence. Synonymous, tolerated missense, and pathogenic changes differ; sex, XCI, variant class, transcript, and functional evidence matter. Large deletions/duplications are outside this calculation.


## Worked Example: Mutation Analysis

**Problem**: A wild-type mRNA sequence reads:

5'-AUG-UUU-GGA-GAA-CUU-UAG-3'

(a) Translate the wild-type sequence.

: Ethical Considerations in Personal and Clinical Genomics: Codon and Amino Acid. {#tbl:unit_IV_mutations_and_genomics_ethical_considerations_in_personal_and_clinical_genomics}
| Codon | Amino Acid |
|-------|-----------|
| AUG | Met |
| UUU | Phe |
| GGA | Gly |
| GAA | Glu |
| CUU | Leu |
| UAG | Stop |

**Protein**: Met-Phe-Gly-Glu-Leu (5 amino acids)

(b) A transition mutation changes the 10th nucleotide (first position of codon 4) from G to A: GAA to AAA.

: Ethical Considerations in Personal and Clinical Genomics. {#tbl:unit_IV_mutations_and_genomics_ethical_considerations_in_personal_and_clinical_genomics_2}
| Codon | Wild-type AA | Mutant AA |
|-------|-------------|-----------|
| GAA | Glu | AAA = Lys |

This is a **missense mutation** (Glu to Lys: non-conservative, charge reversal).

(c) A transition changes the 7th nucleotide (first position of codon 3) from G to A: GGA to AGA.

GGA (Gly) to AGA (Arg): **missense** (non-conservative; small nonpolar to large positive).

(d) A deletion removes the 4th nucleotide (U): sequence becomes AUG-UUG-GAG-AAC-UUU-AG...

This is a **frameshift mutation**. New reading frame: Met-Leu-Glu-Asn-Phe... (completely different protein, no stop codon in remaining sequence -- read-through into 3' UTR).

---

## Computational Bridge

In silico [**translation**](#gl:translation) checks mutation consequences quickly:

```python
from biology.genetics import translate_mrna

wt = translate_mrna("AUGGAAUAA")
print(wt)
```

> **Clinical / systems note:** Pharmacogenomic dosing (warfarin, thiopurines, clopidogrel) is implemented as clinical algorithms over the same variant catalog GWAS discovers --- bridging population statistics to individual prescriptions.

---

### Post-Approval CRISPR Therapeutics: Casgevy and the Safety Frontier

Casgevy edits autologous CD34+ cells ex vivo at the erythroid BCL11A enhancer to increase HbF, followed by myeloablative conditioning. The July 2026 FDA label covers SCD with recurrent VOCs and TDT at age 2+. Adult/adolescent evaluable cohorts: 29/31 met VF12 (no protocol-defined severe VOCs for at least 12 consecutive months within the first 24 months); 32/35 met TI12 (transfusion independence for at least 12 consecutive months within the first 24 months, weighted average Hb at least 9 g/dL). Evaluation starts 60 days after the last transfusion for post-transplant support (or TDT management). Separate cohorts aged 5 to less than 12 reported 8/8 VF12 and 8/9 TI12. The label states that use at ages 2 to less than 5 is supported by extrapolation; these children were not studied in the cited trials. Do not pool different cohorts or endpoints \citep{fda2026casgevylabel}.

The label warns that variant-dependent off-target editing cannot be excluded. Assay coverage and detection limits must be stated rather than asserting a universal 100-site/0.1% guarantee. Trial participants were eligible to enroll in continuing follow-up totaling 15 years post-infusion; this is not evidence that every recipient completed that observation period \citep{fda2026casgevylabel}.

### The Telomere-to-Telomere (T2T) Consortium: A Truly Complete Human Genome

The human reference genome, from the Human Genome Project's 2003 draft through GRCh38 (2013), contained **> 200 Mb of unresolved gaps** — chiefly heterochromatic satellite arrays at centromeres, the short arms of acrocentric chromosomes (13, 14, 15, 21, 22), and segmental duplications. The **T2T-CHM13 assembly** (Nurk et al., *Science* 2022) closed these gaps using long-read sequencing (PacBio HiFi, Oxford Nanopore Ultra-long) on a hydatidiform mole (uniform haplotype, no [**heterozygous**](#gl:heterozygous) complications), yielding the first **gapless 3.055 Gb human genome**.

T2T resolved previously inaccessible repetitive regions, improving annotation and structural-variation analysis. Added models must be distinguished as protein-coding genes, paralogs, or pseudogenes, not treated as 2,000 new protein-coding genes. CHM13 is one near-haploid assembly, not every human haplotype; release-specific pangenome comparisons test generality.

---

## Current Evidence and Frontier Biology: Mutations, CRISPR, and Genomics

For **Mutations, CRISPR, and Genomics**, frontier biology belongs inside the evidence logic of
the chapter. Molecular genetics now spans single-reference sequences, telomere-to-telomere assemblies, pangenome graphs, long-read sequencing, CRISPR medicines, and ethical deployment. The core reading question is this: genomics claims should distinguish variant discovery, pathogenic interpretation, ancestry representation, and clinical actionability.

- **What to verify:** identify the observation, model, assay, or dataset that
  would make the claim stronger or weaker.
- **What to qualify:** state the scale, organism, cell type, environmental
  condition, or population where the claim is expected to hold.
- **What to compare:** test at least one alternative explanation, baseline, or
  null model before treating the pattern as causal.
- **What to cite:** distinguish primary evidence, review synthesis, public
  dataset, and institutional guidance; for recent or numeric claims, prefer
  the source closest to the measurement and state what has changed since it was
  published.

When a genomics claim depends on a reference, ask whether reads, structural variants, ancestry representation, phasing, or clinical validation changes the interpretation \citep{humanpangenome2023,fda2023casgevy,fda2024casgevythalassemia}.

Clinical variant interpretation must separate variant existence from medical meaning. dbSNP supplies submitted sequence-variation identifiers; the original ClinVar publication describes an archive of submitted variant–phenotype assertions, including conflicting interpretations \citep{landrum2014clinvar}. RefSeq and MANE help specify reference sequences and transcripts. For an educational variant record, identify the reference assembly/transcript, available identifiers, assertion source and evidence rather than equating "listed" with "pathogenic" \citep{dbsnp2026,clinvar2026,refseq2026,mane2026}. Current review-status and identifier policies require current documentation; this textbook does not certify 2026 database policy or provide clinical variant classification.

Translation evidence has separate ledgers as well. ClinicalTrials.gov records protocol, recruitment, and submitted-results status, while FDA product pages and approval materials determine approved indications. Casgevy and Lyfgenia are therefore best compared as distinct approved sickle-cell therapies with different molecular strategies: CRISPR-Cas9 enhancer editing for Casgevy and lentiviral gene addition for Lyfgenia \citep{clinicaltrials2026,fda2026casgevy,fda2026lyfgenia}.

**Source practice:** For mutation, genomics, and editing claims, distinguish discovery from clinical actionability, and cite reference resources, regulatory records, or primary editing studies close to the claim \citep{humanpangenome2023,fda2026casgevy,chalumeau2025primeediting}.

### Current Evidence Map: Genome Editing From Variant to Follow-Up

```mermaid
flowchart LR
    A["Disease mechanism"] --> B["Editing strategy"]
    B --> C["Cell collection or delivery"]
    C --> D["On-target edit assay"]
    D --> E["Off-target and SV checks"]
    E --> F["Clinical endpoint"]
    F --> G["Long-term monitoring"]
```
<!-- alt: Flowchart showing casgevy and prime-editing examples show why editing medicines require molecular endpoints, structural-variant surveillance, toxicity monitoring, and long follow-up. -->

*Casgevy and prime-editing examples show why editing medicines require molecular endpoints, structural-variant surveillance, toxicity monitoring, and long follow-up \citep{fda2026casgevy,chalumeau2025primeediting}.*

## Summary

- **Mutations** range from single nucleotide changes (transitions, transversions, silent, missense, nonsense) to large chromosomal rearrangements (deletions, duplications, inversions, translocations). Frameshifts and nonsense mutations are typically most disruptive.
- **Mutagenic agents** include UV radiation (CPDs), alkylating agents (EMS), intercalators (ethidium bromide), and ROS (8-oxoG). The Ames test screens chemicals for mutagenicity.
- **DNA repair**: BER (damaged bases), NER (bulky adducts), MMR (mismatches), NHEJ/HR (DSBs), Fanconi pathway (interstrand crosslinks). Defects cause cancer predisposition (XP, Lynch syndrome, BRCA-associated cancers, Fanconi anemia).
- **CRISPR-Cas9**: sgRNA + Cas9 creates DSB at PAM-adjacent site; NHEJ for knockouts, HDR for precise edits. Base editors (C-to-T, A-to-G) and prime editors avoid DSBs. First approved therapy: Casgevy (sickle cell disease via BCL11A disruption).
- **Human genome**: ~3.2 Gb; ~20,000 protein-coding genes (1.5%); 46% transposable elements; ENCODE shows >80% has biochemical activity. T2T consortium completed gapless reference (2022).
- **NGS technologies**: Illumina (short-read, high throughput), PacBio HiFi and Nanopore (long-read, structural variant resolution).
- **GWAS**: Identify SNP-trait associations at genome-wide significance ($p < 5 \times 10^{-8}$); most complex trait variants have small effect sizes; results displayed on Manhattan plots.
- **Ethics**: GINA Act protections, pharmacogenomic testing (CYP2D6, warfarin dosing), BRCA testing decisions, germline editing moratorium.
- **Connections:** See \cref{sec:unit_IV_dna_replication_and_cell_cycle} for repair pathways, \nameref{sec:unit_V_unit_intro} for inheritance of variants, and \nameref{sec:unit_VII_unit_intro} for CRISPR origins in bacterial immunity.

---

## Review Questions

1. Distinguish between transitions and transversions. Which is more common and why?
2. Explain why frameshift mutations are generally more deleterious than missense mutations. Give an exception where a missense mutation is highly pathogenic.
3. A patient has microsatellite instability in their colorectal tumor. What DNA repair pathway is likely defective? Name the genes involved.
4. Describe the CRISPR-Cas9 mechanism step by step, from guide design to DSB repair.
5. Compare base editing and prime editing. When would you choose each technology?
6. What is the "end-replication problem" of the Human Genome Project, and how did the T2T consortium solve it?
7. Explain GWAS methodology. Why does a Manhattan plot show peaks, and what does a significant peak mean?
8. What is linkage disequilibrium, and why is it important for interpreting GWAS results?
9. Describe the pharmacogenomic basis for warfarin dose variation. Which genes are involved?
10. Discuss the ethical issues raised by the He Jiankui CRISPR babies case. What international guidelines exist for germline editing?
11. Explain why a SNP in a **splice donor** can have larger effect sizes than a missense change in the same exon, using NMD concepts.
12. A GWAS hit lies in intronic sequence with no coding change. Propose two mechanistic classes of causal variants compatible with that pattern.

---


## Further Reading and Source Notes: Mutations, CRISPR, and Genomics

- Ohno (1970). *Evolution by Gene Duplication*. Springer-Verlag.
- Doudna & Charpentier (2014). The new frontier of genome engineering with {CRISPR-Cas9}. *Science*, 346.
- Lander et al. (2001). Initial sequencing and analysis of the human genome. *Nature*, 409.
- Richards et al. (2015). Standards and guidelines for the interpretation of sequence variants: ACMG/AMP consensus recommendation. *Genetics in Medicine*, 17.
- Alexandrov et al. (2013). Signatures of mutational processes in human cancer. *Nature*, 500.

---

## Key Terms

1. **Transition** -- purine-to-purine or pyrimidine-to-pyrimidine point mutation
2. **Transversion** -- purine-to-pyrimidine (or reverse) point mutation
3. **Frameshift mutation** -- insertion/deletion not a multiple of 3 bp, altering reading frame
4. **Nonsense-mediated decay (NMD)** -- mRNA surveillance pathway eliminating transcripts with premature stop codons
5. **Trinucleotide repeat expansion** -- unstable repeat growth causing anticipation in diseases like Huntington
6. **Ames test** -- bacterial mutagenicity assay using histidine-requiring Salmonella revertants
7. **CRISPR-Cas9** -- RNA-guided endonuclease for programmable genome editing
8. **PAM (protospacer adjacent motif)** -- short flanking motif (canonical NGG for SpCas9) licensing recognition/unwinding of a double-stranded DNA target, not a universal requirement for binding or cleavage of every substrate
9. **Base editor** -- dCas9/nickase fused to deaminase for C-to-T or A-to-G conversion without DSB
10. **Prime editor** -- Cas9-nickase + reverse transcriptase + pegRNA for search-and-replace editing
11. **GWAS (genome-wide association study)** -- unbiased scan for SNP-trait associations across the genome
12. **Linkage disequilibrium** -- non-random association of alleles at nearby loci
13. **Manhattan plot** -- genome-wide visualization of association p-values
14. **Pharmacogenomics** -- study of genetic variation affecting drug response
15. **ENCODE** -- Encyclopedia of DNA Elements; mapped functional elements across the human genome
16. **Copy number variant (CNV)** -- duplication or deletion of a genomic segment >1 kb
17. **Synthetic lethality** -- cell death from simultaneous loss of two compensatory pathways

---

## Companion Source Module: Mutations, CRISPR, and Genomics

**Mutations, CRISPR, and Genomics** should leave a reproducible trail from a biological claim to
the code, figure, diagram, or paper-based activity that can test it. Use the
surfaces below to inspect the chapter's assumptions, rerun the relevant model,
or compare the manuscript explanation with companion labs and figures.

: Companion source surfaces for Mutations, CRISPR, and Genomics. {#tbl:unit_IV_mutations_and_genomics_companion_source_surfaces}
| Surface | Use it for |
| --- | --- |
| `src/biology/genetics/genetics.py` (`dna_complement`, `translate_mrna`, `hamming_distance`, `jukes_cantor_distance`) | Compare sequence variants, coding effects, and corrected molecular distances. |
| `src/mermaid/biology_diagrams.py` (`transcription_translation_diagram`, `dna_replication_diagram`) | Link mutation class to replication and expression context. |

**Reproducibility check:** distinguish discovery technology, reference representation, variant class, evidence level, and clinical actionability. **Cross-reference:** connect with \cref{sec:unit_IV_dna_replication_and_cell_cycle}, \cref{sec:unit_IV_gene_expression}, and \cref{sec:unit_VII_bacteria_archaea_viruses}.
