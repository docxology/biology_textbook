# Lab — Natural Selection and Adaptation {#sec:lab_unit_VI_evolution_and_selection .unnumbered}

*This activity accompanies \cref{sec:unit_VI_evolution_and_selection}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO3):** Compare genotype-specific survival in two habitats without confusing spatial selection with heterozygote disadvantage.
- **Outcome 2 (LO7):** Project offspring allele frequencies and breeder-equation responses under explicit inheritance assumptions.
- **Outcome 3 (LO8):** Distinguish comparative trait association from inherited change using the supplied finch and resistance cards.
- **Chapter LO coverage:** LO3, LO7, LO8
- **Rubric (20 points):** Score the five categories independently; label model predictions separately from printed observations.
  - **Evidence (8 points; LO3, LO7, LO8):** Award 2 for replicate survival/relative-viability comparisons and habitat-specific survivor p (1 each); 1 for random-union offspring genotype frequencies; 2 for the two three-generation breeder-equation trajectories (1 each); 1 for plotting all 14 finch means; 2 for pR_next with and without drug (1 each). Use starting genotype numbers and frequency-normalizing denominators explicitly.
  - **Controls (3 points; LO3, LO7):** Award 1 for comparing the same genotype's per-100 survival across habitats; 1 for holding the specified 100:200:100 starting cohort constant when projecting survivor p; 1 for identifying what is held fixed in each breeder-equation model (parent mean versus selection differential). Do not compare raw survivor totals from different starting genotype counts as survival rates.
  - **Uncertainty (3 points; LO7, LO8):** Award 1 for explaining that survival does not measure fecundity; 1 for treating equal gamete contribution/random union as assumptions, not observed descendants; 1 for naming plasticity or shared ancestry as an alternative to inherited response in the species-mean association and identifying relevant missing common-garden or parent–offspring evidence.
  - **Mechanism (4 points; LO3, LO7, LO8):** Award 1 for explaining why habitat-specific homozygote survival is not heterozygote disadvantage; 1 for tracing differential survival into gamete frequency; 1 for explaining the shrinking differential with fixed parents versus its renewal in the alternative projection; 1 for linking the sign of resistance change to the stipulated environment-specific relative fitness, not directed mutation.
  - **Transfer (2 points; LO8):** In the analysis prompt, award 1 for rejecting a treatment-withdrawal prescription from the no-drug fitness card and 1 for a comparison that preserves necessary effective care while monitoring resistance and patient outcomes. A fitness calculation alone earns no transfer points.
<!-- lab-alignment-end -->

## Lab Context: Natural Selection and Adaptation {.unnumbered}

Survival differences demonstrate one component of selection. Inherited change additionally requires reproduction and a specified link between phenotype and transmitted alleles.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Independent replicate genotype survival counts; each entry is survivors of 100 starting individuals per genotype. {#tbl:unit_VI_evolution_and_selection_alignment_and_rubric_map}
| Replicate | Lava AA,Aa,aa | Sand AA,Aa,aa |
| --- | --- | --- |
| 1 | 90,90,50 | 50,90,90 |
| 2 | 88,92,52 | 52,88,92 |
| 3 | 92,88,48 | 48,92,88 |

: Synthetic finch comparison (species labels F01–F14; each mean from 10 birds; depths mm, seed force N). {#tbl:unit_VI_evolution_and_selection_part_3_finch_beak_analysis}
| Species IDs | Beak-depth means in ID order | Seed-force means in ID order |
| --- | --- | --- |
| F01–F07 | 6,7,8,9,10,11,12 | 1,2,3,4,5,6,7 |
| F08–F14 | 13,14,15,16,17,18,19 | 8,9,10,11,12,13,14 |
| Within-population baseline | Mean10.0mm; selected parents11.0mm;h²=.45 | No reciprocal-rearing or pedigree measurements supplied for species comparison |

: Resistance/stewardship cases, all start pR=.10; haploid fitnesses and MICs are stipulated. {#tbl:unit_VI_evolution_and_selection_part_3_finch_beak_analysis_2}
| Environment | wR,wS | R MIC,S MIC (µg/mL) | Evidence boundary |
| --- | --- | --- | --- |
| No drug | .9,1 | 16,1 | Cost in this medium only |
| Drug | 1,.2 | 16,1 | No mutation/HGT in this calculation |
| Stewardship | Use a clinically effective susceptible drug when indicated | No dose/duration given | Do not invent a treatment protocol from fitness alone |

: Reproduction rules and controls. {#tbl:unit_VI_evolution_and_selection_part_3_finch_beak_analysis_3}
| Calculation | Rule |
| --- | --- |
| Diploid survival | Start100AA,200Aa,100aa in each habitat;p_next=(2AA_surv+Aa_surv)/(2total_surv);each survivor contributes equal gametes |
| Offspring | Random union of survivor gametes gives p_next²,2p_nextq_next,q_next²;no migration |
| Haploid | pR_next=pR wR/[pR wR+(1−pR)wS] |
| Quantitative trait | R=h²(parentmean−currentmean);hold selected-parent mean11.0mm fixed |

## Paper-Based Investigation {.unnumbered}

1. Convert each genotype survival replicate to relative viability and compare habitats. Use replicate1 rates with the specified100:200:100 starting cohort to compute survivor p and offspring genotype expectations. Distinguish genotype from color assumptions.
2. Project three offspring mean beak depths with fixed parents 11.0 mm; compare with parents selected 1.0 mm above each generation's current mean.
3. Plot all14 synthetic species means; assess whether correlation proves evolutionary response. Calculate pR_next with and without drug, and propose an evidence-based stewardship comparison preserving necessary treatment.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Darwin/Wallace1858 links heritable variation to differential reproductive success. Nachman etal2003 (DOI10.1073/pnas.0431157100 \citep{nachman2003melanism}) found MC1R-associated dark coats at one lava population but not another, supporting different-gene convergence,not universal MC1R changes. All counts here are new synthetic teaching observations. Revise a local-adaptation inference when migration,genotype-specific fecundity or common-garden evidence changes. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain what the matched starting cohorts isolate and why finch species means cannot establish inherited change. Then assess the proposed transfer “Withhold necessary treatment because the no-drug model lowers resistance.” Use the no-drug/drug fitness cards to separate an evolutionary prediction from a care recommendation. Propose a stewardship comparison that reduces avoidable exposure without denying indicated treatment, and name both the resistance endpoint and the patient-outcome safeguard it would require. No dose or treatment duration is supplied.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: Lava replicate 1 survival rates are 0.9,0.9,0.5. Applied to the 100:200:100 starting cohort, survivors are 90,180,50; pA=360/640=0.5625. Sand gives 50,180,90 survivors and pA=280/640=0.4375. Random-union offspring on lava have AA 0.31640625,Aa 0.4921875,aa 0.19140625; sand swaps the homozygote frequencies. These data show habitat-specific selection, not a globally unfit heterozygote. Offspring expectations are model predictions, not measured descendants.
Task 2: Fixed-parent means are 10.45,10.6975,10.833625 mm. Keeping the selection differential constant instead gives 10.45,10.90,11.35 mm. Credit the changed selected-parent mean in the second model rather than reuse of the initial differential in both models.
Task3: The fourteen stipulated species means have a perfect positive association, not an empirical estimate or proof of inherited change. Common-garden and parent–offspring evidence distinguish plasticity, shared ancestry and inheritance. No-drug resistance p_next=0.09/0.99=0.090909; drug p_next=0.10/0.28=0.357143. Compare susceptibility-guided necessary therapy with avoidable exposure and monitor both clinical outcomes and resistance; no dose or cycling prescription follows from these fitness values.

Transfer benchmark: The decline .10→.090909 without drug is conditional on the medium's fitnesses and does not measure patient benefit or safety of withholding care. An acceptable paper comparison is susceptibility-guided, clinically necessary therapy with reduced avoidable exposure versus usual practice, tracking resistance alongside clinical outcomes and access. No regimen, dose or duration follows from the packet.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
