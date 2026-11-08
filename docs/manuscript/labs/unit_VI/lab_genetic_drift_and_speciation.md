# Lab — Genetic Drift, Gene Flow, and Speciation {#sec:lab_unit_VI_genetic_drift_and_speciation .unnumbered}

*This activity accompanies \cref{sec:unit_VI_genetic_drift_and_speciation}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Calculate diploid sampling variance and neutral heterozygosity retention.
- **Outcome 2 (LO3):** Compute effective size under sex-ratio skew and compare independent founder samples.
- **Outcome 3 (LO7):** Evaluate reproductive barriers without equating a heuristic ratio or FST with species status.
- **Chapter LO coverage:** LO1, LO3, LO7
- **Rubric (20 points):** Score the following categories separately; keep founder sampling, effective size and reproductive isolation distinct.
  - **Evidence (8 points; LO1, LO3, LO7):** Award 2 for both founder frequency series and theoretical variances (1 each); 1 for the exact Ne36 heterozygosity half-life; 1 for Ne=20 versus 3.8; 2 for island means and the two FST summaries (1 each); 2 for 2/20 versus 9/20 cross-form choices and relative hybrid fertility .8 (1 each).
  - **Controls (3 points; LO1, LO3, LO7):** Award 1 for resetting both founder treatments to p=.5 with with-replacement 2N draws; 1 for comparing sex ratios at the same census size 20; 1 for using within-form fertility 1.0 as the hybrid baseline while recognizing that offered same-form pairings do not themselves test mate preference.
  - **Uncertainty (3 points; LO1, LO7):** Award 1 for distinguishing three realized founder draws from the sampling distribution; 1 for a concrete mating-study limitation (20 choices per condition, unreported apparatus/independent repeat trials, or environmental effects); 1 for explaining why one-locus FST and the unvalidated isolation helper cannot identify migration history or species status.
  - **Mechanism (4 points; LO1, LO3, LO7):** Award 1 for tracing smaller 2N to greater allele-sampling variance; 1 for relating sex-ratio skew to reduced Ne and diversity retention; 1 for interpreting the light-associated choice difference as compatible with a visual prezygotic barrier; 1 for distinguishing partial hybrid-fertility reduction as postzygotic, not complete isolation.
  - **Transfer (2 points; LO7):** In the analysis prompt, award 1 for rejecting a species-status claim based on island morphology/distance or FST alone and 1 for an informative reproductive-barrier comparison with a stated distinguishing prediction. Naming a species threshold earns no transfer credit.
<!-- lab-alignment-end -->

## Lab Context: Genetic Drift, Gene Flow, and Speciation {.unnumbered}

All founder treatments must start from the same baseline. Differentiation, morphological divergence and reproductive isolation are related but distinct measurements.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Independent founder draws from pA=.5; each draw samples withreplacement andfounder number is diploid. {#tbl:unit_VI_genetic_drift_and_speciation_alignment_and_rubric_map}
| Replicate | A copies/12 (6founders) | A copies/40 (20founders) |
| --- | --- | --- |
| 1 | 3 | 18 |
| 2 | 9 | 22 |
| 3 | 6 | 20 |
| Control | Each synthetic treatment resets to the same50A/50a source | Counts above represent2N independent with-replacement draws; analyze the printed draws, not a new physical sampling activity |

: Synthetic island-bird observations; three independent birds perisland. {#tbl:unit_VI_genetic_drift_and_speciation_part_3_morphological_divergence_analysis}
| Island ID | Beak lengths mm | Masses g | Distance from source km |
| --- | --- | --- | --- |
| Santa Cruz | 10,11,12 | 20,21,22 | 0 |
| Genovesa | 12,13,14 | 22,23,24 | 100 |
| Española | 14,15,16 | 24,25,26 | 200 |
| Fernandina | 10,11,12 | 20,21,22 | 250 |

: Synthetic cichlid barrier observations under two light conditions; each row20independent mating choices. {#tbl:unit_VI_genetic_drift_and_speciation_part_3_morphological_divergence_analysis_2}
| Case | Same-form choices | Cross-form choices | Hybrid fertility relative to within-form |
| --- | --- | --- | --- |
| Clear water A/B | 18 | 2 | .8 |
| Turbid water A/B | 11 | 9 | .8 |
| Within-form control | 20 offered same-form pairings | Not applicable | 1.0 |
| Allele sample | A:p=.8;B:p=.2;C:p=.5 | Equal populations at one neutral locus | No migration timeseries supplied |

: Model constants and provenance boundaries. {#tbl:unit_VI_genetic_drift_and_speciation_part_3_morphological_divergence_analysis_3}
| Quantity | Rule |
| --- | --- |
| Ne sex ratio | 4NmNf/(Nm+Nf); compare 10 males/10 females with 1 male/19 females |
| Drift | Var(p_next)=pq/(2N);Ht/H0=(1−1/(2Ne))^t |
| FST teachingdefinition | (HT−HS)/HT;H=2p(1−p);equal demeweight |
| Isolation helper | mu/(mu+m) is an unvalidated heuristic, not FST or observed reproductive isolation; mu=m gives .5 independent of N; both zero is undefined |

## Paper-Based Investigation {.unnumbered}

1. Compute founder allele frequencies and theoretical variances, keeping treatments independent. Use the heterozygosity-retention rule to compute the exact half-life for Ne36.
2. Compute Ne for both sex ratios and explain why skew increases drift. Relate the independent founder-sample spreads in Task1 to the sampling variances. Calculate island means and assess whether distance establishes speciation. Calculate FST forA/B, thenA/B/C with equal weights; state what these values do not identify.
3. Compare cichlid choice proportions and hybrid fertility with controls. Decide which prezygotic/postzygotic barriers the cards support, what remains uncertain and why the isolation helper cannot establish species status.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Wright1931 provides a finite-population framework. Haba etal2025 (Science,DOI10.1126/science.ady4515 \citep{haba2025mosquito}) revises the recent London-origin story for undergroundmosquitoes using historical/modern genomes; anecological contrast isnot enough to date or locate speciation. These island/cichlid observations are synthetic,not fielddata from those taxa. Refresh an origin/barrier claim withdemographic/genomic history orreplicated reciprocalmating evidence. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain why the common founder source and fixed census-size sex-ratio contrast matter. Then assess the proposed transfer “The most different island birds must be separate species because distance and FST diagnose isolation.” Use the Fernandina counterexample and the cichlid cards to identify what is and is not measured. Propose, on paper, a reciprocal within-form versus cross-form mating/fertility comparison for the island populations and state how a reproductive-barrier prediction differs from a morphology-only explanation. Do not invent its results.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: Six-founder frequencies are 0.25,0.75,0.5; twenty-founder frequencies are 0.45,0.55,0.5. Conditional variances are 0.25/12=0.0208333 and 0.25/40=0.00625. The exact half-life ln(0.5)/ln(71/72) is about 49.56 generations.
Task 2: Effective sizes are 20 versus 3.8; skew lowers Ne and increases drift. Mean beak lengths are 11,13,15,11 mm; mean masses 21,23,25,21 g. The most distant island matches the source, so these synthetic data do not show a monotonic distance rule. For A/B, HT=0.5,HS=0.32,FST=0.36. For A/B/C, pooled p=0.5,HS=0.38,FST=0.24. These one-locus summaries are not migration estimates, species thresholds or causal tests.
Task 3: Cross-form choices rise from 2/20=0.10 to 9/20=0.45 in turbid water, consistent with weaker visual assortative mating; hybrid fertility 0.8 indicates a partial postzygotic cost. Sample size, apparatus, replication and environmental effects limit inference. Complete isolation and historical sympatric origin do not follow. The mu/(mu+m) heuristic contains no mating data or population size and is not FST.

Transfer benchmark: Fernandina is most distant yet matches source trait means; FST measures the printed neutral-locus differentiation, not reproductive compatibility. A reciprocal cross comparison under matched conditions, with within-population controls, could test reduced cross-pairing, hybrid viability or fertility. Morphological difference alone does not predict such a deficit, and no island crossing outcomes are supplied. The cichlid observations illustrate partial barriers, not an island species verdict.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
