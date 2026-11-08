# Lab — Immune System Architecture {#sec:lab_unit_IX_immune_system_defense .unnumbered}

*This activity accompanies \cref{sec:unit_IX_immune_system_defense}.*

## Learning Objectives {.unnumbered}

- Separate innate recognition/complement from adaptive specificity.
- Analyze controlled ligand-receptor and serum-survival evidence.
- Distinguish primary/booster memory and tolerance.
- Evaluate biomarkers and immune-therapy claims without overdiagnosis.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Separate innate recognition/complement from adaptive specificity.
- **Outcome 2 (LO2):** Analyze controlled ligand-receptor and serum-survival evidence.
- **Outcome 3 (LO3):** Distinguish primary/booster memory and tolerance.
- **Outcome 4 (LO7):** Evaluate biomarkers and immune-therapy claims without overdiagnosis.



: Alignment and evidence-specific scoring. {#tbl:unit_IX_immune_system_defense_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | ligand/serum contrasts,folds andclone arithmetic |
| Controls | vehicle/ligand/genotype rescue,viability andheatedserum controls |
| Uncertainty | n3syntheticreplicates,heatconfounding andnondiagnostic biomarker limits |
| Mechanism | TLR/complement/factorH andadaptive memory/tolerance mechanisms |
| Transfer | dated product/indication-specific therapy argument |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All numerical observations and patients are synthetic, not extracted trial results. This immune-only lab has no thyroid or reproductive-hormone exercise. Literature cards support mechanisms and dated indication boundaries, not invented response percentages.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: Receptor-ligand factorial. {#tbl:unit_IX_immune_system_defense_alignment_and_rubric_map_2}
| Cells | LPS IL6(pg/mL),rep1/2/3 | Pam3CSK4 IL6 | VehicleIL6 | Viability(%) |
| --- | --- | --- | --- | --- |
| WT | 95/100/105 | 75/80/85 | 4/5/6 | 96/97/98 |
| TLR4KO | 5/6/4 | 76/81/86 | 4/5/6 | 95/96/97 |
| TLR4rescue | 90/95/100 | 74/79/84 | 4/5/6 | 96/97/98 |


: Complement survival. {#tbl:unit_IX_immune_system_defense_alignment_and_rubric_map_3}
| Meningococcalstrain | Activeserum survival(%),rep1/2/3 | Heatedserum(%) |
| --- | --- | --- |
| WTfHbp | 78/80/82 | 97/98/99 |
| fHbpdeletion | 18/20/22 | 96/98/100 |
| Rescue | 74/76/78 | 97/98/99 |


: Adaptive and biomarker inputs. {#tbl:unit_IX_immune_system_defense_alignment_and_rubric_map_4}
| Record | Values | Boundary |
| --- | --- | --- |
| Primaryantibody | day0/7/14/28:0/20/60/30arbitraryunits | same assay |
| Boosterantibody | day0/3/7/14:30/100/240/180 | different baseline |
| AntigenCD8 | primaryday7=10;boosterday7=40 cells/µL | not total lymphocytes |
| Healthy/illcytokines | IL6:5/1200;TNF:10/380;IL10:2/720pg/mL | one person, not a threshold |
| Bclone | 100 cells,12exactdoublings | no death/selection |


: Therapy source cards. {#tbl:unit_IX_immune_system_defense_packet_5}
| Claim | Sourceidentity | Boundary |
| --- | --- | --- |
| fHbp-factorH | Madico2006 doi10.4049/jimmunol.177.1.501 | not source of synthetic numbers |
| AtezolizumabTNBC | FDAwithdrawnapprovals;withdrawn2021 | historical, not current indication |
| IL17vsIL23 | risankizumablabel:adultCrohndisease | different pathway/disease effects |
| CD19/BCMACAR-T | product,indication,lineanddaterequired | no aggregate efficacy percentage |
| MHC-Iloss | lessCD8recognition/lessNKinhibition | activating input still needed |

Mechanism reference: innate receptors recognize shared molecular patterns; TLR4 supports the stipulated LPS response, while the retained Pam3CSK4 response tests another receptor pathway. Complement damages susceptible bacteria; bacterial fHbp can recruit host factor H to reduce complement attack. Adaptive B/T clones have antigen specificity and memory; antibody titre is an assay endpoint, not a supplied protective threshold. Naive T cells receive IL7 and self-peptide–MHC survival signals, while productive effector activation normally requires antigen recognition, costimulation and context; recognition without those signals can promote tolerance. Therapy-card scope: atezolizumab targets PD-L1, and its TNBC indication here is explicitly withdrawn in 2021. Risankizumab targets IL23p19 and the printed label card names adult Crohn disease. Neither card supplies a trial endpoint, effect size or complete safety profile; mark those fields “not supplied” and identify the label/trial evidence needed rather than fabricate them or require a lookup.

## Paper-Based Investigation {.unnumbered}

1. Compute mean IL6 and ligand-minus-vehicle responses. Use genotype×ligand specificity, rescue and viability to distinguish signaling from death/assay failure.
2. Compare active/heated serum survival by strain. Explain complement/factorH recruitment and why deletion/rescue is informative. Propose complement-component-specific confirmation because heating changes more than one serum property.
3. Compare response timing/peaks and baseline antibody. Relate memoryB/T specificity to booster response without equating titre with protection, duration or herd immunity.
4. Compute cytokine folds and clone size. Explain why elevations alone cannot distinguish infection, autoimmunity, assay error and other causes; propose additional evidence, not treatment thresholds.
5. Write an evidence-bounded therapy card using one printed product: distinguish target, indication and available date, then mark missing endpoint/safety evidence explicitly. Do not invent an efficacy percentage or treatment recommendation. Explain naiveT maintenance byIL7/selfpMHC versus effector activation/tolerance requirements using the reference card.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sampleSD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

An efficacy rate needs a named product, eligible population, endpoint and timepoint;none of these synthetic assays estimates CAR-T, checkpoint or sepsis treatment efficacy.

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

LPS-minus-vehicle means 95, 0, 90 pg/mL for WT/KO/rescue; Pam3 responses 75, 76, 74. Active-serum survival means 80/20/76 versus heated 98/98/98, differences −18/−78/−22 points; deletion reduces active survival 60 points versus WT. Cytokine folds 240/38/360 are not diagnoses. 100×2^12=409600 cells. Booster peak 240 versus 60 is 4 fold but has a different baseline and timing; matched endpoints are needed. fHbp recruits factor H and reduces complement attack, not host-factor-H deletion. IL23 blockade can treat Crohn disease whereas IL17 blockade has different risks. Withdrawn indications cannot be listed as current. \cite{madico2006factorh,fda2026withdrawncancer,fda2026risankizumab}

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
