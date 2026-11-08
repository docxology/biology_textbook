# Lab — Population Genetics {#sec:lab_unit_V_population_genetics .unnumbered}

*This activity accompanies \cref{sec:unit_V_population_genetics}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO4):** Estimate allele frequencies, expected genotypes and HWE chi-square with estimated-parameter degrees of freedom.
- **Outcome 2 (LO7):** Compare diploid Wright–Fisher replicate outcomes with their conditional variances.
- **Outcome 3 (LO6):** Predict a selection step while distinguishing a missing genotype from an absent allele.
- **Chapter LO coverage:** LO4, LO7, LO6
- **Rubric (20 points):** Score the following categories separately; distinguish allele-copy denominators from diploid-individual counts.
  - **Evidence (8 points; LO4, LO7, LO6):** Award 3 for MN allele frequencies, all expected counts and chi-square/df1 decision (1 each); 2 for both five-run frequency series/means and the two theoretical variances (1 each); 3 for F's q/expected aa, S's survivor q and Ne10 five-generation retention (1 each).
  - **Controls (3 points; LO4, LO7, LO6):** Award 1 for the HWE null conditional on the estimated allele frequency, not a fixed 1:2:1 ratio; 1 for recognizing that both drift treatments start p=.5 and differ in 2N; 1 for comparing S's preselection zygotes with fitness-weighted survivors while holding mutation and migration absent.
  - **Uncertainty (3 points; LO4, LO7):** Award 1 for explaining the estimated-frequency df subtraction; 1 for distinguishing five realized runs from a guaranteed theoretical variance ordering; 1 for stating that HWE agreement or departure alone does not identify selection and naming a plausible confound such as population mixture or genotyping error.
  - **Mechanism (4 points; LO7, LO6):** Award 1 for with-replacement sampling of 2N gene copies; 1 for linking smaller N to greater conditional sampling variance; 1 for showing how F's heterozygotes retain a despite no aa founders; 1 for normalizing S's surviving genotype frequencies before counting a copies.
  - **Transfer (2 points; LO6):** In the analysis prompt, award 1 for rejecting immediate elimination of a after aa lethality and 1 for tracing the surviving allele through Aa into subsequent random-mating zygotes. A missing phenotype is not an absent allele.
<!-- lab-alignment-end -->

## Lab Context: Population Genetics {.unnumbered}

HWE is a genotype-frequency null conditional on allele frequencies. Neither agreement nor departure alone identifies a causal evolutionary force.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: MN counts retained as a synthetic benchmark because the earlier historical-survey attribution was not traceable. {#tbl:unit_V_population_genetics_alignment_and_rubric_map}
| Genotype | MM | MN | NN | Total |
| --- | --- | --- | --- | --- |
| Observed | 298 | 489 | 213 | 1000 diploid individuals |

: Independent one-generation Wright–Fisher teaching replicates, all start p(A)=.5. {#tbl:unit_V_population_genetics_alignment_and_rubric_map_2}
| Replicate | A copies among2N=20 (N10) | A copies among2N=100 (N50) |
| --- | --- | --- |
| 1 | 6 | 48 |
| 2 | 14 | 52 |
| 3 | 10 | 50 |
| 4 | 8 | 46 |
| 5 | 12 | 54 |

: Exact sampling instructions and comparison cards. {#tbl:unit_V_population_genetics_alignment_and_rubric_map_3}
| Card | Rule |
| --- | --- |
| Wright–Fisher | Optional manual extension: label 100 paper slips, 50 A and 50 a. Draw one, record and replace it; repeat 2N times. For later generations use the preceding offspring's 2N labeled gene copies and sample with replacement 2N times. Required calculations use the printed replicate counts and need no bag or physical sampling. |
| F | 20 founder diploids:16AA,4Aa,0aa;random mating, equal survival |
| S | Start p=q=.5;fitnessAA=1,Aa=1,aa=0;compare preselection zygotes with survivors |

: Formulas and explicit HWE decision constants. {#tbl:unit_V_population_genetics_alignment_and_rubric_map_4}
| Quantity | Definition |
| --- | --- |
| Frequencies | p=(2MM+MN)/(2n);q=1−p;E=n(p²,2pq,q²) |
| HWE test | χ²=sum(O−E)^2/E;df=3−1−1=1;critical3.841 atα=.05 |
| Drift | Var(p_next givenp)=p(1−p)/(2N);H_t/H_0=(1−1/(2Ne))^t |
| Selection | After aa lethality, q_next=q/(1+q);no mutation or migration |

## Paper-Based Investigation {.unnumbered}

1. Compute the MN HWE test, showing all expected counts, df and interpretation. Explain how a fixed Mendelian ratio test differs in degrees of freedom.
2. Calculate replicate allele frequencies p(A), not statistical p-values, from the drift counts and find their means. Compare conditional theoretical variances for N10/N50. Explain why five runs do not guarantee the theoretical variance ordering in every realized experiment.
3. Calculate founder q and expected aa zygote fraction in F. Compute the single selection step in S and heterozygosity retained for Ne=10 over 5 generations. Distinguish observed heterozygosity from expected gene diversity.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** Hardy/Weinberg1908 supplies a null model; Wright1931 motivates finite-population sampling. The MN numbers here are an explicitly synthetic benchmark, not a newly verified historical human survey. Historical ancestry labels cannot establish sampling provenance. Revise inference if ascertainment, genotyping error, relatedness or population mixture changes; no inference about a social group is licensed. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Use the equal-p drift treatments to explain which comparison isolates population-size effects and why five runs are limited. Then assess the claim “Because aa survivors in S are zero, the next random-mating generation cannot contain aa.” Use the printed survivor composition and q_next to predict the next zygote aa fraction before another selection step. State the life-cycle stage at which aa would again be absent under the stipulated model.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: p=.5425,q=.4575; E(MM)=294.30625,E(MN)=496.3875,E(NN)=209.30625. χ²≈.2215, df=1, do not reject. One allele-frequency parameter was estimated; a fixed 3:1 test estimates none and has df=1 for 2 classes.
Task 2: N10 p=.3,.7,.5,.4,.6; N50=.48,.52,.50,.46,.54; both means=.5. Theoretical conditional variances=.0125 and .0025. Sampling with replacement implements diploid Wright–Fisher; drawing 10 beads without replacement would instead be a hypergeometric allele sample, not N10 diploids.
Task3:F has4a copies/40=.10,so random union givesaa=.01 even though founders includednoaa. S haspreselection.25AA,.5Aa,.25aa;survivors1/3AA,2/3Aa,q_next=1/3. Retention(.95)^5=.77378094;relative loss=.22621906. Aclass frequencyAa=.42 is not larger thanAA=.49 whenp=.7. Credit denominators andavoid concluding a missing phenotype meansq=0.

Transfer benchmark: S survivors include 2/3 Aa and retain q=1/3. Random union therefore gives aa zygotes q²=1/9 before selection; lethal-aa selection removes them among survivors, not from all subsequent conceptions. This one-generation prediction does not establish an allele-loss time or an equilibrium in a finite population.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
