# Lab — Epigenetic Inheritance and Disease {#sec:lab_unit_IV_epigenetic_inheritance_and_disease .unnumbered}

*This activity accompanies \cref{sec:unit_IV_epigenetic_inheritance_and_disease} of the textbook.*

## Learning Objectives {.unnumbered}

- Interpret matched-normalization contact maps and perturbation evidence.
- Identify the first unexposed generation in imprinting/exposure designs.
- Select controls that separate inherited marks from DNA/cultural confounding.
- Interpret trial design,cohort,endpoint and regulatory status separately.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret matched-normalization contact maps and perturbation evidence.
- **Outcome 2 (LO2):** Identify the first unexposed generation in imprinting/exposure designs.
- **Outcome 3 (LO6):** Select controls that separate inherited marks from DNA/cultural confounding.
- **Outcome 4 (LO7):** Interpret trial design,cohort,endpoint and regulatory status separately.
- **Chapter LO coverage:** LO1, LO2, LO6, LO7
- **Rubric (20 points total):**
  - **Evidence — 6 points (LO1, LO2, LO6, LO7):** Award 1 for contact/RNA means and fourfold deletion changes with repair return, 1 for F3 methylation/phenotype means with pedigree denominators, 1 for both exposure maps, 1 for the maternal/paternal ICR state comparison, and 2 for 9/62 and 22/104 responses plus endpoint-specific 61%/74% hazard reductions. Arithmetic credit requires the correct cohort and endpoint, not interchangeable percentages.
  - **Controls — 4 points (LO1, LO6):** Award 1 for matched contact normalization/window size and isogenic boundary repair, 1 for viable-cell normalization and an orthogonal perturbation in the puncta case, 1 for sequence/genotype and cross-fostering/standard-diet comparisons in the inheritance case, and 1 for mark-specific removal/reinstatement with matched manipulation controls. Explain which causal alternative each control tests.
  - **Uncertainty — 4 points (LO1, LO6, LO7):** Award 1 for identifying viability loss as a puncta/RNA confound and withholding an LLPS claim from FRAP/drug sensitivity alone, 1 for explaining that three F3 pedigrees with matched assayed-locus genotype do not exclude genome-wide genetic or maternal-care alternatives, 1 for the single-arm sarcoma cohort's lack of placebo comparison, and 1 for distinguishing a hazard ratio from absolute response probability or a proportional change in waiting time.
  - **Mechanism — 3 points (LO1, LO2):** Award 1 for a boundary-insulation explanation consistent with deletion and repair without assuming every contact is productive, 1 for the methylation→reduced CTCF→increased maternal IGF2 link, and 1 for distinguishing protection after fertilization from imprint erasure and sex-specific re-establishment in germ cells.
  - **Transfer — 3 points (LO2, LO6, LO7):** Award 1 for applying exposure logic to obtain F3 for gestational and F2 for paternal-preconception designs, 1 for naming evidence that would distinguish persistent association from mark-mediated inheritance, and 1 for interpreting the dated clinical cards by product/indication, cohort and endpoint without converting historical response data into present approval or a treatment recommendation. Withdrawal of romidepsin PTCL must not be generalized to CTCL.
<!-- lab-alignment-end -->

## Lab Context: Epigenetic Inheritance and Disease {.unnumbered}

All numeric observations and sequence/assay cards below are **synthetic teaching evidence**, not patient results or empirical measurements, unless a card explicitly names an official or primary source. No external packet, live lookup, equipment, or software is required.

## Paper-Based Materials {.unnumbered}

Print this complete activity; use pencil, ruler, graph paper, and calculator. Work in pairs but record independent conclusions.

## Printed Evidence Packet {.unnumbered}

### Contact and condensate evidence {.unnumbered}

Synthetic capture-contact counts per 10,000 valid pairs; matched 500 kb windows; three independent cultures per arm. Target RNA is normalized to reference RNA. Boundary repair reverses the defined deletion in isogenic cells.

: Contact perturbation and rescue {#tbl:unit_IV_epigenetic_inheritance_and_disease_alignment_and_rubric_map}
| Condition | Contact counts | Target RNA |
| --- | --- | --- |
| Intact boundary | 10,12,8 | 1.0,1.1,0.9 |
| Boundary deletion | 40,44,36 | 4.0,4.2,3.8 |
| Boundary repair | 12,10,8 | 1.1,1.0,0.9 |

Condensate cards: vehicle puncta in 100/100 cells; drug puncta in 20/100; RNA falls from 1 to 0.4; viability falls from 100% to 60%. A separate IDR mutant reduces puncta but preserves measured DNA binding. FRAP recovery or hexanediol sensitivity alone does not prove liquid–liquid phase separation.

### Generational and imprinting evidence {.unnumbered}

: Exposure and allele cards {#tbl:unit_IV_epigenetic_inheritance_and_disease_alignment_and_rubric_map_2}
| Card | Supplied evidence |
| --- | --- |
| Gestational F0 exposure | Direct exposure reaches F1 fetus and its future F2 germ cells; F3 reared unexposed |
| Paternal F0 preconception exposure | Sperm exposed; F1 conceived afterward; F2 unexposed |
| Maternal IGF2/H19 ICR | Unmethylated, CTCF bound, IGF2 low, H19 high |
| Paternal IGF2/H19 ICR | Methylated, CTCF low, IGF2 high, H19 low |
| Maternal ICR hypermethylation | CTCF binding falls; maternal IGF2 increases |
| PGC reset | Parental imprints erased, then sex-specific marks re-established during gametogenesis |

Synthetic F3 data from three independent pedigrees per arm: methylated-cytosine fractions 0.20,0.22,0.18 versus controls 0.10,0.11,0.09; phenotype units 12,13,11 versus controls 10,11,9. Standard diet and assayed-locus genotype are matched; no genome-wide variant exclusion or mark-specific rescue is provided.

### Dated clinical cards {.unnumbered}

Paraphrases of retrieved primary/official sources, not fabricated measurements or source quotations; reviewed 2026-11-07.

: Cohort, endpoint and regulatory evidence {#tbl:unit_IV_epigenetic_inheritance_and_disease_alignment_and_rubric_map_3}
| Source | Printed evidence |
| --- | --- |
| Gounder 2020, NCT02601950 | Open-label single-arm 62-patient INI1/SMARCB1-loss epithelioid sarcoma cohort: 9 responses, median PFS 5.5 months, median response time 3.9 months, no placebo \citep{gounder2020tazemetostat} |
| FDA withdrawal table | Tazemetostat both indications: 2026-06-22; panobinostat MM: 2022-03-24; romidepsin PTCL: 2021-07-30, not a statement that CTCL was withdrawn \citep{fda2026withdrawncancer} |
| FDA INDIGO 2024 | 331 randomized post-surgery IDH1/2-mutant grade-2 glioma patients; PFS HR 0.39, next-intervention HR 0.26 \citep{fda2024vorasidenib} |
| FDA AUGMENT-101 2024 | 104 R/R acute leukemia patients with KMT2A translocation; CR+CRh 22/104 (21.2%); median duration of CR+CRh 6.4 months; age 1+ approval \citep{fda2024revumenib} |

## Paper-Based Investigation {.unnumbered}

1. Compute mean contact and RNA fold changes; explain how boundary repair strengthens causal inference and why mismatched normalization prevents absolute probability comparisons.
For the condensate cards, compare drug-induced puncta/RNA loss with the viability change. Propose a viable-cell-normalized comparison and an orthogonal IDR-mutant test; explain what could remain unresolved about phase separation even if puncta and RNA change together.
2. Map the first unexposed generation in both exposure designs. Interpret parent-of-origin ICR states and distinguish PGC reset from post-fertilization protection.
3. Compare F3 means and design sequence, cross-fostering, and mark-editing rescue controls to discriminate alternatives.
4. Reconstruct the two response fractions and both INDIGO relative hazard reductions using $100(1-HR)$%. Separate PFS from time to next intervention, hazard from absolute probability or waiting time, and historical trial results from the dated U.S. regulatory card; name each cohort and endpoint.

## Data Recording {.unnumbered}

Record each calculation with units, the comparison/control, and one alternative explanation. Show intermediate steps; use a separate column for observed card evidence versus inferred mechanism.

## Paper-Based Evidence Upgrade {.unnumbered}

Bulk contact maps do not prove LLPS or function. Persistence into an unexposed generation is necessary but insufficient for a causal inheritance claim. Refresh product/indication status against official records; historical trial data remain historical. No clinical recommendation follows from these cards.

## Analysis Questions {.unnumbered}

Explain which result supports the proposed mechanism, which result would falsify it, and what additional measurement would discriminate the strongest alternative. Apply the mechanism to a new tissue, genotype, or condition without treating synthetic observations as clinical evidence.

> **Concept Check:** Why does persistence into F3 strengthen a gestational-exposure claim without proving that a methylation change, rather than DNA variation, caused the phenotype?

## Instructor Key and Scoring Expectations {.unnumbered}

### Worked Results and Interpretation {.unnumbered}

<!-- SOLUTION
Contact means 10→40→10 per 10,000 pairs, RNA 1→4→1: deletion increases both fourfold and repair rescues them, supporting boundary function without proving every contact is productive. Drug puncta loss is confounded by 40% viability loss; normalize viable cells and use orthogonal perturbations. Gestational F0: first unexposed F3; paternal preconception F0: first unexposed F2. Maternal ICR methylation can reduce CTCF insulation and increase IGF2. Imprints may be protected after fertilization but normally reset in PGCs. F3 means 0.20 versus 0.10 and phenotype 12 versus 10 support association, not mark-mediated causation; sequence, maternal-care and selection confounding remain. Mark-specific removal and reinstatement strengthen causality. Sarcoma 9/62=14.5% (rounded15%), no placebo comparison. INDIGO PFS 1−0.39=61% lower hazard; next intervention 1−0.26=74% lower hazard, not 74% shorter waiting time. Revumenib 22/104=21.15%, specifically CR+CRh; 6.4 months describes that response duration. Tazemetostat is no longer FDA-approved for the two listed indications. See \cref{sec:unit_IV_epigenetic_inheritance_and_disease}.
SOLUTION -->

## Safety and Ethics Notes {.unnumbered}

Required work is paper-only: no cultures, reagents, biological samples, medical decisions, or participant data collection. Optional wet/equipment extensions require institutional protocols and separate approval; they are not needed to complete or score this activity.
