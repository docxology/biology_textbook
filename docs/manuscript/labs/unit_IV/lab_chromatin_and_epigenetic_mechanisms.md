# Lab — Chromatin and Epigenetic Mechanisms {#sec:lab_unit_IV_chromatin_and_epigenetic_mechanisms .unnumbered}

*This activity accompanies \cref{sec:unit_IV_chromatin_and_epigenetic_mechanisms} of the textbook.*

## Learning Objectives {.unnumbered}

- Interpret histone enrichment relative to input and IgG controls.
- Distinguish bisulfite sequence and methylation-specific primer readouts.
- Calculate maintenance dilution with the defined cytosine observable.
- Separate direct maternal exposure from germline-inheritance evidence.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO3):** Interpret histone enrichment relative to input and IgG controls.
- **Outcome 2 (LO4):** Distinguish bisulfite sequence and methylation-specific primer readouts.
- **Outcome 3 (LO11):** Calculate maintenance dilution with the defined cytosine observable.
- **Outcome 4 (LO12):** Separate direct maternal exposure from germline-inheritance evidence.
- **Chapter LO coverage:** LO3, LO4, LO11, LO12
- **Rubric (20 points total):**
  - **Evidence — 6 points (LO3, LO4, LO11, LO12):** Award 2 for the state-specific ChIP means in percent input with the RNA contrast kept separate, 1 for A/B primer-state interpretations, 2 for both maintenance trajectories with the defined cytosine fraction, and 1 for the six litter proportions and .75 versus .25 group means. Correct recurrence setup can earn partial credit after an arithmetic error; presence/absence PCR is not a percent-methylation estimate.
  - **Controls — 4 points (LO3, LO4):** Award 1 for explaining input normalization and IgG background, 1 for the methylated/unmethylated primer references, 1 for the non-CpG conversion and no-template checks, and 1 for a writer-perturbation design with catalytic-dead/rescue and viability comparisons linked to mark/RNA readouts. State what each comparison excludes, not merely its name.
  - **Uncertainty — 3 points (LO3, LO4, LO12):** Award 1 for explaining why mixed M/U PCR signal or standard bisulfite cannot uniquely quantify 5mC, 1 for why bulk histone enrichments do not prove both marks occupy one allele/nucleosome, and 1 for treating litters rather than sixty offspring as exposure replicates and limiting the synthetic association accordingly.
  - **Mechanism — 4 points (LO3, LO4, LO11):** Award 1 for C→U→T conversion versus retained methylated C with unchanged nominal amplicon length, 2 for explaining old-strand retention plus maintenance in fnext=f(1+p)/2 and its p=0/p=1/n=0 limits, and 1 for distinguishing a mark–RNA correlation from writer-dependent causal regulation tested by the proposed perturbation.
  - **Transfer — 3 points (LO12):** Award 1 for mapping gestational exposure to F1 and future F2 germ cells, 1 for selecting unexposed F3 descendants rather than calling F1/F2 transgenerational proof, and 1 for explaining how cross-fostering/standardized diet/genotype comparisons address particular alternatives while leaving gestational exposure or genetic confounding unresolved. Persistence alone is not proof of germline mark-mediated causation.
<!-- lab-alignment-end -->

## Lab Context: Chromatin and Epigenetic Mechanisms {.unnumbered}

All numeric observations and sequence/assay cards below are **synthetic teaching evidence**, not patient results or empirical measurements, unless a card explicitly names an official or primary source. No external packet, live lookup, equipment, or software is required.

## Paper-Based Materials {.unnumbered}

Print this complete activity; use pencil, ruler, graph paper, and calculator. Work in pairs but record independent conclusions.

## Printed Evidence Packet {.unnumbered}

### Bisulfite and ChIP cards {.unnumbered}

Synthetic same-locus assays: cytosine in an unmethylated CpG converts to U, then PCR reads T; 5mC remains C. Original top-strand segment 5′-ACGCGT-3′; unmethylated product ATGTGT; fully methylated product ACGCGT. Identical flanking primers retain the same nominal 200 bp amplicon length; methylation-specific primer sets M/U distinguish converted sequence, not 200-versus-400 bp size. Non-CpG conversion-control C must convert.

: Bisulfite and ChIP cards {#tbl:unit_IV_chromatin_and_epigenetic_mechanisms_alignment_and_rubric_map}
| Sample/control | M-specific 200 bp | U-specific 200 bp | Non-CpG conversion |
| --- | --- | --- | --- |
| Fully methylated reference | Present | Absent | Pass |
| Unmethylated reference | Absent | Present | Pass |
| Sample A, 3 independent cultures | Present in 3/3 | Absent in 3/3 | Pass |
| Sample B, 3 independent cultures | Present in 3/3 | Present in 3/3 | Pass |
| No-template controls | Absent | Absent | Not applicable |

ChIP qPCR at one developmental promoter: three independent cultures per state, percent input H3K4me3/H3K27me3/IgG. State 1: 8,9,10 / 1,1,1 / 0.2,0.2,0.2; state 2: 1,1,1 / 7,8,9 / 0.2,0.2,0.2. Matched RNA means 20 and 2 arbitrary units. Presence/absence MS-PCR is qualitative, not a reliable percent-methylation measurement.

### Maintenance and exposure cards {.unnumbered}

: Cytosine dilution and exposure design {#tbl:unit_IV_chromatin_and_epigenetic_mechanisms_source_governance_checkpoint}
| Card | Supplied evidence |
| --- | --- |
| Dilution model | fnext=f(1+p)/2; f=methylated eligible cytosine fraction; p=maintenance efficiency; no de novo methylation or active removal |
| Initial condition | f0=0.8,p=0.9; calculate generations0–2 |
| Complete block | f0=0.9,p=0; calculate generations0–3 |
| Maternal diet model | F0 pregnant dam receives diet+ or matched control; F1 Avy genotype held fixed |
| Diet+ litters | Brown-coat offspring16/20,14/20,15/20 in three independent litters |
| Control litters | Brown-coat offspring5/20,6/20,4/20 in three independent litters |
| Exposure map | Gestational F0 exposure directly reaches F1 fetus and F1 germ cells (future F2) |
| Proposed follow-up | Cross-foster, standardize postnatal diet, genotype and measure unexposed F3 descendants across pedigrees |

Each count represents one independent litter of 20 synthetic offspring; offspring share maternal conditions. This illustrates association and is not a recovered published dataset.

## Paper-Based Investigation {.unnumbered}

1. Infer methylation states from primer controls and explain why bisulfite conversion does not double same-primer product length.
2. Compare ChIP means with IgG, associate marks with RNA, and propose a causal perturbation with matched controls.
3. Calculate both maintenance trajectories; explain p=0,p=1,n=0 limits and specify the observable.
4. Calculate litter proportions and group means, map direct exposure and identify the first unexposed generation.

## Data Recording {.unnumbered}

Record each calculation with units, the comparison/control, and one alternative explanation. Show intermediate steps; use a separate column for observed card evidence versus inferred mechanism.

## Paper-Based Evidence Upgrade {.unnumbered}

ChIP enrichment is population-average occupancy; two marks in bulk need not coexist on the same allele/nucleosome. Standard bisulfite cannot distinguish 5mC from 5hmC. A short synthetic model trajectory is not an epigenetic clock or clinical-response predictor. Source card: synthetic cultures/litters; exposure timing, cell composition and conversion efficiency are potential conclusion-changing confounders.

## Analysis Questions {.unnumbered}

Explain which result supports the proposed mechanism, which result would falsify it, and what additional measurement would discriminate the strongest alternative. Apply the mechanism to a new tissue, genotype, or condition without treating synthetic observations as clinical evidence.

> **Concept Check:** Why can simultaneous H3K4me3 and H3K27me3 enrichment in a mixed-cell sample fail to prove bivalency on one allele?

## Instructor Key and Scoring Expectations {.unnumbered}

### Worked Results and Interpretation {.unnumbered}

<!-- SOLUTION
A is compatible with predominantly methylated templates; B contains both primer-detectable states, but PCR bias prevents exact quantification. Both nominal products are 200 bp: conversion does not double length. ChIP means for state1: H3K4me3=9%, H3K27me3=1%, IgG=0.2%; state2: 1%,8%,0.2%. RNA20→2 correlates with repression but cannot establish causation. Writer depletion with catalytic-dead, rescue and viability controls followed by mark/accessibility/RNA assays tests causality. With f0=.8,p=.9: .8,.76,.722; with f0=.9,p=0: .9,.45,.225,.1125; p=1 preserves f0. Maternal-diet litter proportions .80,.70,.75 versus .25,.30,.20 have group means .75 versus .25. Litters, not the 60 individual offspring, are exposure replicates. F1 and future F2 germ cells are directly exposed during gestation; F3 is first unexposed. Cross-fostering addresses postnatal care, not gestational exposure or genetic confounding. See \cref{sec:unit_IV_chromatin_and_epigenetic_mechanisms}.
SOLUTION -->

## Safety and Ethics Notes {.unnumbered}

Required work is paper-only: no cultures, reagents, biological samples, medical decisions, or participant data collection. Optional wet/equipment extensions require institutional protocols and separate approval; they are not needed to complete or score this activity.
