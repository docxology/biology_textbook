# Lab — DNA Replication and the Cell Cycle {#sec:lab_unit_IV_dna_replication_and_cell_cycle .unnumbered}

*This activity accompanies \cref{sec:unit_IV_dna_replication_and_cell_cycle} of the textbook.*

## Learning Objectives {.unnumbered}

- Discriminate replication models from density-band evidence.
- Calculate human replication time from ploidy, origins and fork speed.
- Classify checkpoint arrests from finite cell-count evidence.
- Connect damage-response controls with repair interpretation.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO2):** Discriminate replication models from density-band evidence.
- **Outcome 2 (LO3):** Calculate human replication time from ploidy, origins and fork speed.
- **Outcome 3 (LO6):** Classify checkpoint arrests from finite cell-count evidence.
- **Outcome 4 (LO10):** Connect damage-response controls with repair interpretation.
- **Chapter LO coverage:** LO2, LO3, LO6, LO10
- **Rubric (20 points total):**
  - **Evidence — 7 points (LO2, LO3, LO6):** Award 2 for density-band positions/areas at generations 1–3, 2 for mean phase fractions in all five conditions, 2 for the human time using 6.4 Gb and two forks per diploid-genome origin, and 1 for the one-origin bacterial time with Mb→bp conversion. Show denominators and units; retain setup credit after an arithmetic slip.
  - **Controls — 3 points (LO2, LO6, LO10):** Award 1 for generation-0 heavy DNA and the supplied HH/HL/LL density references as band baselines, 1 for vehicle as the phase-distribution baseline, and 1 for proposing uninjured ATM-intact and ATM-loss comparisons under matched culture/assay conditions so genotype effects are not mistaken for a damage-specific repair effect.
  - **Uncertainty — 3 points (LO3, LO6):** Award 1 for treating cultures as independent n rather than individual cells, 1 for explaining why a 4C bin alone cannot resolve G2 from M, and 1 for identifying simultaneous origin firing, equal fork speed and no stalls as ideal-time assumptions rather than observed human S-phase duration. Exact synthetic density areas do not establish real instrument precision.
  - **Mechanism — 4 points (LO2, LO6, LO10):** Award 2 for explaining how generation 1 rejects conservation and two bands at generation 2 reject simple dispersion, 1 for connecting the HU/nocodazole marker clues to stalled synthesis versus mitotic arrest, and 1 for explaining why lack versus availability of a sister template favors end joining in G1 versus permitting HR in S/G2. Do not equate checkpoint arrest with successful DNA repair.
  - **Transfer — 3 points (LO3, LO10):** Award 1 for the halved-human-origin prediction of 2560 s with fork speed/DNA held fixed, 1 for explaining the resulting inverse origin-number dependence without inventing half a bacterial origin or claiming a real interspecies S-phase ranking, and 1 for a repair-specific break/junction assay with predicted results that distinguish repaired DNA from merely reduced ATM-dependent arrest.
<!-- lab-alignment-end -->

## Lab Context: DNA Replication and the Cell Cycle {.unnumbered}

All numeric observations and sequence/assay cards below are **synthetic teaching evidence**, not patient results or empirical measurements, unless a card explicitly names an official or primary source. No external packet, live lookup, equipment, or software is required.

## Paper-Based Materials {.unnumbered}

Print this complete activity; use pencil, ruler, graph paper, and calculator. Work in pairs but record independent conclusions.

## Printed Evidence Packet {.unnumbered}

### Density-band cards {.unnumbered}

Synthetic normalized band areas from three independent culture preparations after transfer from heavy15N to light14N medium. Density positions g/mL: HH1.724,HL1.717,LL1.710. Each triple gives percent area, totaling100 per preparation.

: Density-band cards {#tbl:unit_IV_dna_replication_and_cell_cycle_alignment_and_rubric_map}
| Generation | HH% | HL% | LL% |
| --- | --- | --- | --- |
| 0 | 100,100,100 | 0,0,0 | 0,0,0 |
| 1 | 0,0,0 | 100,100,100 | 0,0,0 |
| 2 | 0,0,0 | 48,50,52 | 52,50,48 |
| 3 | 0,0,0 | 24,25,26 | 76,75,74 |

Reference card: a conservative model predicts HH plusLL after generation1; a dispersive model predicts one shifting intermediate band after generation2. The synthetic areas illustrate the logic of Meselson–Stahl, not recovered1958 measurements \citep{meselson1958}.

### Cell-cycle evidence cards {.unnumbered}

DNA-content cytometry simplified to G1/S/G2-M bins (2C/intermediate/4C); 100 cells scored per independently prepared culture, three cultures per condition. No micrograph lookup is needed. Marker cards: EdU+ indicates DNA synthesis; phospho-H3+ indicates mitosis, not all4C cells.

: Cell-cycle evidence cards {#tbl:unit_IV_dna_replication_and_cell_cycle_part_3_semiconservative_replication_analysis}
| Condition | G1 counts | S counts | G2/M counts | Marker clue |
| --- | --- | --- | --- | --- |
| Vehicle | 50,52,48 | 30,28,32 | 20,20,20 | EdU+ in S |
| Hydroxyurea | 20,22,18 | 70,68,72 | 10,10,10 | RPA-ssDNA,phospho-CHK1 high |
| Nocodazole | 10,12,8 | 10,8,12 | 80,80,80 | Unattached kinetochores,phospho-H3 high |
| DSB,ATM intact | 70,72,68 | 10,8,12 | 20,20,20 | p53/p21 high |
| DSB,ATM loss | 45,47,43 | 35,33,37 | 20,20,20 | Reduced p53/p21 response |

### Fork geometry and repair {.unnumbered}

: Fork geometry and repair {#tbl:unit_IV_dna_replication_and_cell_cycle_part_3_semiconservative_replication_analysis_2}
| Card | Supplied input |
| --- | --- |
| Human target | 3.2Gb haploid;6.4Gb diploid DNA to copy in S phase |
| Origins | 50,000 simultaneously active across diploid genome |
| Fork velocity | 50bp/s per fork;two opposite forks/origin |
| Bacterial comparator | 4.6Mb circular chromosome;one bidirectional origin;1000bp/s/fork |
| Repair comparison | DSB in G1:no sister chromatid;DSB in S/G2:sister available |
| Molecular direction | New DNA5′→3′;primase makes RNA primer;RNaseH/FEN1 process eukaryotic primers/flaps;ligase seals nicks |

Assume evenly spaced origins, simultaneous firing and no stalls solely for the time calculation.

## Paper-Based Investigation {.unnumbered}

1. Sketch bands at generations1–3 and explain which two timepoints exclude conservative and dispersive alternatives.

2. Calculate mean phase fractions by condition. Use marker evidence to distinguish stalled S from mitotic arrest and identify a limit of DNA-content bins.

3. Calculate ideal human and bacterial completion times, then halve only the human active-origin number and recalculate. Use total DNA/(origins×2 forks/origin×speed), converting Gb to 10⁹ bp and Mb to 10⁶ bp. Do not interpret half a bacterial origin as a physical comparator.

4. Choose a plausible repair route in G1 versus S/G2, explain ATM-loss checkpoint evidence, and propose a repair-specific assay rather than treating arrest as repair success.

## Data Recording {.unnumbered}

Record each calculation with units, the comparison/control, and one alternative explanation. Show intermediate steps; use a separate column for observed card evidence versus inferred mechanism.

## Paper-Based Evidence Upgrade {.unnumbered}

Origin firing is asynchronous in real S phase, forks vary/stall, and transcription/replication conflicts matter; ideal times are lower-bound teaching calculations, not predicted human S-phase duration. Cells within a culture are subsamples; cultures are independent n=3. Density resolution and marker specificity constrain conclusions.

## Analysis Questions {.unnumbered}

Explain which result supports the proposed mechanism, which result would falsify it, and what additional measurement would discriminate the strongest alternative. Apply the mechanism to a new tissue, genotype, or condition without treating synthetic observations as clinical evidence.

> **Concept Check:** Why does a4C DNA-content peak not distinguish G2 arrest from mitosis, and which printed marker resolves the nocodazole case?

## Instructor Key and Scoring Expectations {.unnumbered}

### Worked Results and Interpretation {.unnumbered}

<!-- SOLUTION
Semiconservative replication gives all HL at generation 1, half HL/half LL at 2, quarter HL/three-quarter LL at 3. Generation 1 excludes conservation; two bands at 2 exclude simple dispersion. Mean vehicle G1/S/G2M=50/30/20%; HU 20/70/10; nocodazole 10/10/80; DSB ATM-intact 70/10/20; ATM-loss 45/35/20. Cytometry alone cannot distinguish G2 from M; phospho-H3 and attachment evidence support mitotic arrest for nocodazole. Ideal human time=6.4e9/(50000×2×50)=1280 s=21.33 min; each fork travels 64000 bp. Halving origins doubles time to 2560 s. Using 3.2 Gb with 50000 origins defined *per haploid set* would give 640 s; never call 3.2 Gb diploid. Bacterial time 4.6e6/(2×1000)=2300 s=38.33 min. G1 favors end joining; S/G2 permits sister-template HR. ATM loss reduces DSB-induced arrest but neither checkpoint activation nor survival proves repaired DNA; use break/junction sequencing and matched uninjured ATM controls. See \cref{sec:unit_IV_dna_replication_and_cell_cycle}.
SOLUTION -->

## Safety and Ethics Notes {.unnumbered}

Required work is paper-only: no cultures, reagents, biological samples, medical decisions, or participant data collection. Optional wet/equipment extensions require institutional protocols and separate approval; they are not needed to complete or score this activity.
