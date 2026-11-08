# Lab — Gene Expression {#sec:lab_unit_IV_gene_expression .unnumbered}

*This activity accompanies \cref{sec:unit_IV_gene_expression} of the textbook.*

## Learning Objectives {.unnumbered}

- Identify exon/intron and processing evidence from printed sequence cards.
- Apply the downstream-junction NMD rule with explicit coordinates.
- Translate finite mRNAs and detect a frame shift.
- Discriminate RNA abundance from protein-output mechanisms.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO3):** Identify exon/intron and processing evidence from printed sequence cards.
- **Outcome 2 (LO4):** Apply the downstream-junction NMD rule with explicit coordinates.
- **Outcome 3 (LO5):** Translate finite mRNAs and detect a frame shift.
- **Outcome 4 (LO7):** Discriminate RNA abundance from protein-output mechanisms.
- **Chapter LO coverage:** LO3, LO4, LO5, LO7
- **Rubric (20 points total):**
  - **Evidence — 7 points (LO3, LO4, LO5, LO7):** Award 1 for joining the stated exons into mature WT mRNA, 3 for all four translations with explicit triplet regrouping and termination in the insertion card, 1 for junction distances 100/30 nt and the no-downstream-junction case, and 2 for X/Y mean RNA/protein contrasts against vehicle. A stop codon or trailing incomplete nucleotide is not an amino acid; correct grouping can earn partial credit after a codon error.
  - **Controls — 3 points (LO4, LO7):** Award 1 for vehicle with equal viable-cell/loading and stable RNA/protein references, 1 for comparing transcript A with its same-coordinate translation-inhibited counterpart to isolate translation dependence, and 1 for a matched nascent-RNA, ribosome or half-life comparison whose predicted results discriminate the alternatives for X or Y. A named assay without a comparison/prediction earns at most half of that point.
  - **Uncertainty — 3 points (LO3, LO4, LO7):** Award 1 for recognizing the short minigene as a boundary schematic rather than a validated spliceable construct, 1 for treating the downstream-junction rule as NMD-compatible rather than guaranteed and requiring real isoform coordinates before variant use, and 1 for explaining why an 8 h endpoint in three cultures measures abundance, not transcription or translation rate.
  - **Mechanism — 4 points (LO4, LO7):** Award 1 for translation-dependent surveillance distinguished from nuclear quality control, 1 for why translation inhibition can stabilize A while reducing protein, 1 for distinguishing translation inhibition from faster protein degradation for X, and 1 for distinguishing reduced RNA synthesis from faster RNA decay for Y. Credit mechanistic alternatives only when linked to the printed RNA/protein patterns and a discriminating measurement.
  - **Transfer — 3 points (LO3, LO4):** Using the therapy cards, award 1 for DMD exon skipping versus SMN2 exon inclusion, 1 for explaining why the target exon must exist and why steric splice ASOs are not all RNase-H gapmers, and 1 for a matched splice-product/protein-output check that distinguishes successful RNA processing from restored protein production. Do not infer clinical efficacy from the sequence exercise.
<!-- lab-alignment-end -->

## Lab Context: Gene Expression {.unnumbered}

All numeric observations and sequence/assay cards below are **synthetic teaching evidence**, not patient results or empirical measurements, unless a card explicitly names an official or primary source. No external packet, live lookup, equipment, or software is required.

## Paper-Based Materials {.unnumbered}

Print this complete activity; use pencil, ruler, graph paper, and calculator. Work in pairs but record independent conclusions.

## Printed Evidence Packet {.unnumbered}

### Sequence and codon cards {.unnumbered}

All mRNAs written5′→3′; start at the first AUG; stop codons are not amino acids. A tiny complete codon subset suffices for these tasks.

: Sequence and codon cards {#tbl:unit_IV_gene_expression_alignment_and_rubric_map}
| Card | Sequence or mapping |
| --- | --- |
| WT mature mRNA | AUG UUU GAA CCU UAA |
| Synonymous | AUG UUC GAA CCU UAA |
| Missense | AUG UUU GUA CCU UAA |
| One-base insertion after AUG | AUG A UUU GAA CCU UAA |
| Codons | AUG = Met; UUU/UUC = Phe; GAA = Glu; CCU = Pro; GUA = Val; AUU = Ile; UGA/UAA = stop |
| Minigene exons | Exon1=AUGUUU;intron=GUACACAG;exon2=GAACCUUAA |

The short intron is a schematic boundary card, not a functional spliceable construct: donorGU and acceptorAG are shown, but real branch-point/length requirements are omitted.

### Junction and translation-surveillance cards {.unnumbered}

Positions are on mature mRNA in nucleotides; distance is junction coordinate minus last nucleotide of stop codon. Apply a teaching rule: >55nt upstream of a downstream junction is NMD-compatible, not guaranteed; ≤50nt is less compatible. EJCs sit roughly20–24nt upstream of junctions.

: Junction and translation-surveillance cards {#tbl:unit_IV_gene_expression_alignment_and_rubric_map_2}
| Transcript | Stop ends at nt | Downstream junction nt | Condition |
| --- | --- | --- | --- |
| A | 100 | 200 | Translation active |
| B | 170 | 200 | Translation active |
| C | 100 | None | Last exon |
| A + translation inhibitor | 100 | 200 | Translation blocked |

### Northern/Western evidence {.unnumbered}

Three independent cell cultures per condition; equal viable cell number and loading. Signals normalized to unchanged referenceRNA/protein=1; measure after8h. Assays do not themselves report transcription rate.

: Northern/Western evidence {#tbl:unit_IV_gene_expression_alignment_and_rubric_map_3}
| Condition | Target mRNA | Target protein |
| --- | --- | --- |
| Vehicle | 1.0,1.1,0.9 | 1.0,1.1,0.9 |
| Treatment X | 1.0,1.1,0.9 | 0.2,0.3,0.4 |
| Treatment Y | 0.2,0.3,0.4 | 0.3,0.4,0.5 |

X/Y are blinded mechanisms; reduced protein can arise from translation inhibition or accelerated degradation. RNA loss can reflect transcription reduction or RNA decay.

### Regulatory and therapy cards {.unnumbered}

: Regulatory and therapy cards {#tbl:unit_IV_gene_expression_alignment_and_rubric_map_4}
| Condition | Lactose | Glucose | LacI operator binding | CAP–cAMP |
| --- | --- | --- | --- | --- |
| L1 | Absent | Absent | Bound | Active |
| L2 | Present | Absent | Released | Active |
| L3 | Present | Present | Released | Low |
| L4 | Absent | Present | Bound | Low |

Lac decision rule: bound LacI strongly represses output even when CAP–cAMP is active. When LacI is released, active CAP–cAMP supports high output and low CAP–cAMP supports basal output. These are qualitative categories, not zero-versus-fixed transcript counts.

Therapy cards: eteplirsen binds an existing exon 51 in amenable DMD genotypes and promotes skipping; casimersen targets exon 45; nusinersen promotes SMN2 exon 7 inclusion. RNase-H-gapmer ASOs recruit enzymatic RNA cleavage; steric splice ASOs do not all share that mechanism.

## Paper-Based Investigation {.unnumbered}

1. Splice the schematic minigene and translate WT/synonymous/missense/insertion cards, showing codon grouping and where translation stops.

2. Calculate junction distances and classify NMD compatibility; explain why nuclear RNA quality control is not synonymous with translation-dependent NMD.

3. Compare meanRNA/protein changes and propose one discriminating nascent-RNA, ribosome, or protein-half-life measurement for each treatment.

4. Complete lac outputs and compare the three therapy cards without proposing skipping an exon already deleted.
For one printed splice-therapy card, specify an untreated-versus-treated paper comparison of exon-junction products and protein output. What result would show altered processing without demonstrating restored protein production? Do not invent a measured response or target an exon already absent.

## Data Recording {.unnumbered}

Record each calculation with units, the comparison/control, and one alternative explanation. Show intermediate steps; use a separate column for observed card evidence versus inferred mechanism.

## Paper-Based Evidence Upgrade {.unnumbered}

Cultures supply n=3; densitometry ratios depend on loading and reference stability. EndpointRNA abundance is not transcription rate, and endpointprotein is not translation rate. NMD rules have exceptions and require transcript accession/isoform coordinates for real variants. Required tasks involve no live RNA, cells, or software.

## Analysis Questions {.unnumbered}

Explain which result supports the proposed mechanism, which result would falsify it, and what additional measurement would discriminate the strongest alternative. Apply the mechanism to a new tissue, genotype, or condition without treating synthetic observations as clinical evidence.

> **Concept Check:** Why can translation inhibition stabilize a premature-stop transcript while simultaneously reducing its protein output?

## Instructor Key and Scoring Expectations {.unnumbered}

### Worked Results and Interpretation {.unnumbered}

<!-- SOLUTION
Splicing yieldsAUGUUUGAACCUUAA. WT and synonymous:Met–Phe–Glu–Pro;missense:Met–Phe–Val–Pro. Insertion groupsAUG-AUU-UGA-ACC-UUA-A:Met–Ile then stop;the trailing incomplete nucleotide is not translated. A distance100nt is NMD-compatible;B30nt less compatible;C lacks a downstream-junction trigger but otherNMD routes are possible. Blocking translation suppresses canonical NMD while also reducing protein production: mRNA stabilization is not translation rescue. X meanRNA1/protein0.3 supports a post-transcriptional effect, not a unique mechanism. Y meanRNA0.3/protein0.4 could reflect reduced synthesis or faster decay;nascentRNA or RNA-half-life distinguishes. LacL2 highest,L3 basal,L1/L4 strongly repressed (not literal zero transcription);CAP is active inL1 despite LacI repression. Nusinersen inclusion differs fromDMD skipping;only an existing exon can be targeted. Full credit requires class-specificASO logic rather than saying allASOs act stoichiometrically. See \cref{sec:unit_IV_gene_expression}.
SOLUTION -->

**Splice-transfer benchmark:** Compare the same transcript/genotype and loading conditions with and without the proposed splice ASO. Eteplirsen/casimersen promote skipping of an existing amenable exon; nusinersen promotes SMN2 exon 7 inclusion. Changed junction products with unchanged/low protein show altered processing without demonstrated protein rescue; a protein assay is needed in addition to a splice assay. These predictions do not establish treatment efficacy.

## Safety and Ethics Notes {.unnumbered}

Required work is paper-only: no cultures, reagents, biological samples, medical decisions, or participant data collection. Optional wet/equipment extensions require institutional protocols and separate approval; they are not needed to complete or score this activity.
