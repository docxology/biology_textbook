# Lab — Mutations, CRISPR, and Genomics {#sec:lab_unit_IV_mutations_and_genomics .unnumbered}

*This activity accompanies \cref{sec:unit_IV_mutations_and_genomics} of the textbook.*

## Learning Objectives {.unnumbered}

- Classify sequence changes with strand and coding-frame context.
- Interpret guide mismatch and heteroduplex cleavage evidence without equating proxies to editing.
- Compare coding, regulatory and prime-editing mechanisms with clinical maturity.
- Evaluate reference/database uncertainty and ethical limits before clinical action.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Classify sequence changes with strand and coding-frame context.
- **Outcome 2 (LO4):** Interpret guide mismatch and heteroduplex cleavage evidence without equating proxies to editing.
- **Outcome 3 (LO5):** Compare coding, regulatory and prime-editing mechanisms with clinical maturity.
- **Outcome 4 (LO9):** Evaluate reference/database uncertainty and ethical limits before clinical action.
- **Chapter LO coverage:** LO1, LO4, LO5, LO9
- **Rubric (20 points total):**
  - **Evidence — 7 points (LO1, LO4, LO5, LO9):** Award 2 for frame/strand-correct WT/S1/S2/insertion translations and variant classes, 1 for PAM and proximal/distal mismatch positions, 2 for mass-based cleaved fraction .32 and both p=.2/.8 roots, 1 for donor HbF changes of 7/12/9 percentage points distinguished from edit percentages, and 1 for describing what the junction-spanning graph/long-read evidence supports without calling the insertion pathogenic. Correct setup can earn partial credit after arithmetic errors.
  - **Controls — 3 points (LO4, LO5):** Award 1 for explaining the WT lane's background-cleavage role, 1 for the no-template lane's contamination check (not a positive cleavage-sensitivity control), and 1 for matched donor baselines/viability when comparing promoter editing with HbF output. The WT and no-template negatives alone cannot validate editing efficiency.
  - **Uncertainty — 4 points (LO4, LO9):** Award 1 for using sequencing to favor the low p branch while retaining finite-read sampling uncertainty, 1 for explaining how nonuniform/multiple alleles or incomplete cleavage invalidate the two-allele mapping and why uniform edited DNA can be T7E1-negative, 1 for distinguishing three cultures from 100 reads per culture as replicates, and 1 for requiring versioned transcript/reference and reviewed classification evidence rather than treating an rs identifier or conflicting synthetic ClinVar card as clinical authorization.
  - **Mechanism — 3 points (LO4, LO5):** Award 1 for why PAM-proximal mismatches often impair recognition more while leaving sequence-context ranking unvalidated, and 2 for distinguishing direct coding correction, BCL11A enhancer disruption and pegRNA-directed promoter rewriting by their target and route to altered protein/HbF output. A shared HbF increase does not make these edits mechanistically identical or equally clinically mature.
  - **Transfer — 3 points (LO9):** In the four ethical scenarios, award 1 for distinguishing a consenting somatic study from unsafe/unvalidated heritable embryo transfer, 1 for consent-governed handling of secondary findings, and 1 for an access/justice decision that does not mistake regulatory validation for equitable availability. Decisions must cite the relevant safety, heritability or consent evidence; an unsupported blanket approval/rejection earns no scenario-specific point.
<!-- lab-alignment-end -->

## Lab Context: Mutations, CRISPR, and Genomics {.unnumbered}

All numeric observations and sequence/assay cards below are **synthetic teaching evidence**, not patient results or empirical measurements, unless a card explicitly names an official or primary source. No external packet, live lookup, equipment, or software is required.

## Paper-Based Materials {.unnumbered}

Print this complete activity; use pencil, ruler, graph paper, and calculator. Work in pairs but record independent conclusions.

## Printed Evidence Packet {.unnumbered}

### Sequence and guide cards {.unnumbered}

All coding DNA cards are 5′→3′; transcribe T→U and start at ATG. Codons needed: ATG=Met; TTT/TTC=Phe; GAA=Glu; GTA=Val; CCT=Pro; ATT=Ile; TGA/TAA=stop.

: Sequence and guide cards {#tbl:unit_IV_mutations_and_genomics_alignment_and_rubric_map}
| Card | Coding DNA |
| --- | --- |
| WT | ATG TTT GAA CCT TAA |
| S1 | ATG TTC GAA CCT TAA |
| S2 | ATG TTT GTA CCT TAA |
| Insertion | ATG A TTT GAA CCT TAA |
| SpCas9 target top strand | 5′-GACCTGATCGTACGATTCGA-TGG-3′ |
| Perfect protospacer | GACCTGATCGTACGATTCGA |
| Distal mismatch | AACCTGATCGTACGATTCGA |
| Proximal mismatch | GACCTGATCGTACGATTCGG |

TGG is the PAM on this written strand, not part of the 20 nt guide-target match. Last protospacer bases are PAM-proximal. These are paper recognition cards, not validated clinical guides.

### Gel and sequence-validation cards {.unnumbered}

Synthetic background-corrected DNA mass units after denaturation/random reannealing and T7E1. Uncut amplicon500bp; mismatched duplex cleavage products300+200bp. Assume complete equal-sensitivity cleavage of all heteroduplexes and only WT plus one edited allele; under this restrictive model fcleaved=2p(1-p). Bands are given as intensities, so no external gel image is required.

: Gel and sequence-validation cards {#tbl:unit_IV_mutations_and_genomics_part_4_pangenome_database_and_prime_editing_decision_cards}
| Lane/culture | 500bp mass | 300bp mass | 200bp mass |
| --- | --- | --- | --- |
| WT control | 100 | 0 | 0 |
| Edited culture1 | 68 | 19.2 | 12.8 |
| Edited culture2 | 68 | 19.2 | 12.8 |
| Edited culture3 | 68 | 19.2 | 12.8 |
| No-template control | 0 | 0 | 0 |

Independent amplicon-sequencing validation:20/100,22/100,18/100 reads edited in the same three cultures. Reads are sampling units within cultures; culture is the biological replicate. An exact HDR allele can form a mismatch against WT; a uniform edited population can be T7E1-negative.

### Reference, maturity and decision cards {.unnumbered}

: Reference, maturity and decision cards {#tbl:unit_IV_mutations_and_genomics_part_4_pangenome_database_and_prime_editing_decision_cards_2}
| Card | Evidence |
| --- | --- |
| Linear reference | L–R;sample short reads at junction show20% unmapped |
| Alternate graph path | L–[3000bp insertion]–R;two independent long reads span each junction on one phased haplotype |
| Synthetic dbSNP card | rsExample;existence identifier only;no pathogenicity assertion |
| Synthetic ClinVar card | VariationExample;conflicting classifications;review date2026-01-01;not an actual record |
| Synthetic transcript card | RefSeq accession NM_example.1;matched Ensembl transcript;MANE flag must be verified before real use |
| Casgevy | BCL11A erythroid enhancer disruption; FDA July 2026 SCD with recurrent VOCs/TDT age 2+; not direct HBB correction \citep{fda2026casgevylabel} |
| Prime-editing teaching data | DonorsA/B/C:target promoter motif edited40/60/50%;HbF10/16/12%versus matchedbaseline3/4/3%;synthetic,not clinical response |
| Ethical scenarios | Adult consenting somatic study;embryo transfer after unvalidated edit;secondary finding without consent;unequal access to validated treatment |

The prime-editing mechanism uses pegRNA-directed sequence rewriting; its synthetic donor readouts do not reproduce Chalumeau2025, which provides the real early-translational study context \citep{chalumeau2025primeediting}.

## Paper-Based Investigation {.unnumbered}

1. Translate and classify each coding card; distinguish predicted protein effect from demonstrated pathogenicity.

2. Mark the PAM and proximal/distal mismatch positions. Predict why proximal mismatches often disrupt SpCas9 more strongly but cannot guarantee an ordering without measurement.

3. Calculate cleaved fraction as summed cleaved-band mass divided by total lane mass, solve the two-allele equation for both possible p values, and compare each with the sequencing read counts. Explain two ways T7E1 can underestimate or misidentify editing. The 100 sequencing reads per culture are finite samples, not exact allele fractions required to reproduce every gel intensity.

4. Interpret the graph evidence and unresolved database claim. Compare direct coding correction, enhancer disruption and promoter prime editing; calculate each donor's HbF percentage-point change, distinguishing it from target-edit percentage. Analyze each ethical scenario using consent, safety, justice and heritability.

## Data Recording {.unnumbered}

Record each calculation with units, the comparison/control, and one alternative explanation. Show intermediate steps; use a separate column for observed card evidence versus inferred mechanism.

## Paper-Based Evidence Upgrade {.unnumbered}

T7E1 is a mismatch proxy,not a complete off-target or HDR assay. DNA target tests for RNA viruses require a reverse-transcription step;SARS-CoV-2 is not a DNA virus. Mutation-rate records with per-base/per-locus/per-genome/evolutionary-time denominators cannot be ranked as one burden. Synthetic database identifiers are expressly not lookup targets or patient results;real clinical work requires versioned accessions,review status and independent validation.

## Analysis Questions {.unnumbered}

Explain which result supports the proposed mechanism, which result would falsify it, and what additional measurement would discriminate the strongest alternative. Apply the mechanism to a new tissue, genotype, or condition without treating synthetic observations as clinical evidence.

> **Concept Check:** Why could a uniformly edited sample show no T7E1 cleavage, while a precisely HDR-edited/WT mixture does show cleavage?

## Instructor Key and Scoring Expectations {.unnumbered}

### Worked Results and Interpretation {.unnumbered}

<!-- SOLUTION
S1 is synonymous Phe; S2 is missense Glu→Val. The insertion groups ATG-ATT-TGA-ACC-TTA-A, giving Met–Ile then stop; WT is Met–Phe–Glu–Pro. Cleaved fraction=(19.2+12.8)/100=.32. Solving 2p(1-p)=.32 gives p=.2 or .8: allele information is required to choose a branch. Sequencing 20/22/18% supports the low branch, mean20%, range18–22%; cleavage32% is not editing20%. Multiple edited alleles, sequence bias and incomplete cleavage invalidate the simple mapping. PAM-proximal mismatch is at the last protospacer base; distal mismatch is at the first. Proximal seed mismatches are often less tolerated, but context must be measured. Graph and junction-spanning long reads support an insertion on one haplotype, not pathogenicity. Conflicting classifications and synthetic accessions cannot authorize care. Prime-editing donors show HbF increases7/12/9 percentage points; these synthetic changes are not clinical benefit. Compare matched controls and viability. Somatic consent does not legitimize unvalidated embryo transfer; secondary findings require consent governance and access inequity may persist after validation. See \cref{sec:unit_IV_mutations_and_genomics}.
SOLUTION -->

## Safety and Ethics Notes {.unnumbered}

Required work is paper-only: no cultures, reagents, biological samples, medical decisions, or participant data collection. Optional wet/equipment extensions require institutional protocols and separate approval; they are not needed to complete or score this activity.
