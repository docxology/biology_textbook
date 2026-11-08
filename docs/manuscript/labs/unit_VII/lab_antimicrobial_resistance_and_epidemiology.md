# Lab — Antimicrobial Resistance and Epidemiology {#sec:lab_unit_VII_antimicrobial_resistance_and_epidemiology .unnumbered}

*This activity accompanies \cref{sec:unit_VII_antimicrobial_resistance_and_epidemiology}.*

## Learning Objectives {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO6):** Calculate resistance selection and recipient transfer in a specified order with conserved frequency bookkeeping.
- **Outcome 2 (LO2):** Reconstruct conservative Euler SIR transfers and compare a finite-horizon intervention scenario.
- **Outcome 3 (LO7):** Interpret organism–drug surveillance denominators and distinguish official adjusted estimates from synthetic raw counts.
- **Chapter LO coverage:** LO6, LO2, LO7
- **Rubric (20 points):** Score the following categories separately; keep resistance frequencies, concurrently infected counts and surveillance proportions distinct.
  - **Evidence (8 points; LO6, LO2, LO7):** Award 2 for selection→transfer and reversed-order frequencies (1 each); 3 for the N1000 first two updates/day4 comparison, the N10000 first quarter-day update and its day30/printed-maximum comparison (1 per group); 2 for both sites' blood/urine rates and pooled rates (1 each); 1 for distinguishing the official reported estimates from the synthetic raw table without inventing organism-specific denominators.
  - **Controls (3 points; LO6, LO2, LO7):** Award 1 for using growing no-drug and clear sterile controls to support MIC 4 µg/mL; 1 for the matched initial states/gamma/dt in each baseline-versus-contact-reduction comparison; 1 for matching organism–drug, specimen, time period and AST definition before comparing surveillance rates.
  - **Uncertainty (3 points; LO2, LO7):** Award 1 for distinguishing a largest printed 30-day I from the eventual epidemic peak; 1 for recognizing Euler-step/printing limitations rather than treating trajectories as calibrated forecasts; 1 for identifying referral/specimen selection and the absence of organism-specific raw denominators in the WHO summary.
  - **Mechanism (4 points; LO6, LO2):** Award 1 for applying transfer only to the susceptible recipients remaining at that stage; 1 for explaining clone versus cross-lineage plasmid sharing without a proven transfer direction; 1 for showing algebraically that the same F/G transfers conserve S+I+R; 1 for explaining why disease-only efficacy with ET=0 leaves Re unchanged.
  - **Transfer (2 points; LO7):** In the analysis prompt, award 1 for rejecting a site-level population-burden ranking from pooled cultured-isolate rates and 1 for identifying specimen standardization plus community/ascertainment information needed for that broader inference. Repeating pooled percentages without this boundary earns no transfer credit.
<!-- lab-alignment-end -->

## Lab Context: Antimicrobial Resistance and Epidemiology {.unnumbered}

Frequency change, infection burden and surveillance percentages are not interchangeable. This packet supplies complete recurrence inputs and a finite printed trajectory, not a promise to obtain missing data by running code.

## Paper-Based Materials {.unnumbered}

This printed packet, paper, pencil and a calculator are sufficient. No culture, image download, volunteer family survey, database access or Python execution is required. All newly stipulated observations below are **synthetic teaching data**, not empirical measurements or clinical decision rules. Replicates and denominators are given explicitly; do not treat technical repeats as independent biological samples.

## Printed Evidence Packet {.unnumbered}

: Synthetic closed-population SIR teaching trajectories, N1000,I0=10,S0=990,R0count=0; gamma=.1/day, dt1day. Values rounded only for printing. {#tbl:unit_VII_antimicrobial_resistance_and_epidemiology_alignment_and_rubric_map}
| Day | BaselineS,I,R (beta=.30/day) | Reduced-contactS,I,R (beta=.15/day) |
| --- | --- | --- |
| 0 | 990,10,0 | 990,10,0 |
| 1 | 987.03,11.97,1 | 988.515,10.485,1 |
| 2 | 983.485575,14.317425,2.197 | 986.960313,10.991187,2.0485 |
| 3 | 979.261281,17.109976,3.628742 | 985.333133,11.519248,3.147619 |
| 4 | 974.234740,20.425520,5.339740 | 983.630589,12.069868,4.299544 |
| Euler transfers | F=dt×betaSI/N;G=dt×gammaI;Snext=S−F | Inext=I+F−G;Rnext=R+G;use all three old-state values in each simultaneous update |

: Synthetic resistance and transmission mechanism cards. {#tbl:unit_VII_antimicrobial_resistance_and_epidemiology_part_4_current_intervention_decision_matrices}
| Card | Inputs and boundary |
| --- | --- |
| Selection/HGT | pR=.10,wR=1,wS=.5; first selection, thenh=.10 of remaining susceptible recipients converts; no reverse transfer. |
| Drug assay | Broth concentrations32,16,8,4,2,1µg/mL:clear,clear,clear,clear,growth,growth;no-drug control grows,sterile control stays clear. |
| Genomic context | Two ward isolates share a core lineage and plasmidP; unrelated wastewater lineage also carriesP. No complete transmission chronology. |
| Vaccine counterexample | $R_0=4$,95% disease efficacy but $E_T=0$; coverage100%. In the homogeneous durable transmission model, $p_c=.75$ is the $R_e=1$ boundary, not coverage or guaranteed elimination. Do not substitute endpoints. |

: Synthetic organism–drug raw surveillance table; first isolate per patient, same one-year period and testing rule; counts are resistant/tested. {#tbl:unit_VII_antimicrobial_resistance_and_epidemiology_part_4_current_intervention_decision_matrices_2}
| Site | E.coli–third-generation-cephalosporin blood | Samepair urine | Tested at clinic |
| --- | --- | --- | --- |
| A | 30/100 | 40/400 | Hospital referrals selected; no community sampling |
| B | 6/20 | 80/800 | Mostly outpatient urine sampling |
| Controls/limits | Same defined AST criterion within this teaching table | No missing AST results among included rows | No inference of population incidence from cultures alone |

: Real official-source snapshot and finite intervention decision cards; these are paraphrases, not invented raw GLASS counts. {#tbl:unit_VII_antimicrobial_resistance_and_epidemiology_part_4_current_intervention_decision_matrices_3}
| Source/case | Printed evidence |
| --- | --- |
| WHO GLASS report 2025 | Published October 13, 2025; over 23 million bacteriologically confirmed cases in report scope; 104 countries report 2023 data; 93 infection–pathogen–drug combinations; 16 combinations tracked 2018–2023. |
| WHO result summary 2025 | Bloodstream third-generation-cephalosporin resistance exceeds 40% for E.coli and 55% for K.pneumoniae globally. Organism-specific raw denominators and uncertainty are not supplied by this news summary; do not assign 23 million to either row. |
| T1 | Adult drug-susceptible pulmonaryTB, no stated shorter-regimen selection: distinguish classical2HRZE/4HR phases. |
| T2 | RR-TB, eligible BPaLM/BPaL pathway after review, fluoroquinolone resistant. |
| T3 | RR-TB, significant toxicity/eligibility uncertainty: specialist individualized/alternative-regimen review needed. |
| P | HIV-negative prevention candidate cannot sustain daily pills but can attend scheduled injections; suspected acute infection must first be excluded; access and product-specific eligibility remain. |
| M | Household has bed nets and indoor pre-bedtime exposure; local vector resistance is uncertain. |


### Complete30-Day Baseline/Distancing Comparison {.unnumbered}

This second synthetic scenario preserves the original 30-day comparison: population 10,000, initial infected 10, initial susceptible 9,990, no initially recovered, gamma 0.1/day, beta 0.35/day versus 0.18/day. Apply the coupled Euler recurrence above at dt 0.25 day (four substeps per day), not a one-day update. Daily rows are sampled from those substeps; entries are printed to three decimals, so displayed totals can differ slightly from 10,000 by rounding.

: Thirty-day coupled-Euler teaching trajectories. {#tbl:unit_VII_antimicrobial_resistance_and_epidemiology_thirty_day_euler}
| Day | Baseline S,I,R | Distancing S,I,R |
| --- | --- | --- |
| 0 | 9990.000,10.000,0.000 | 9990.000,10.000,0.000 |
| 1 | 9986.163,12.740,1.098 | 9988.147,10.822,1.030 |
| 2 | 9981.277,16.227,2.496 | 9986.143,11.712,2.145 |
| 3 | 9975.057,20.666,4.277 | 9983.974,12.674,3.352 |
| 4 | 9967.142,26.314,6.544 | 9981.628,13.715,4.658 |
| 5 | 9957.074,33.495,9.432 | 9979.089,14.840,6.071 |
| 6 | 9944.274,42.620,13.106 | 9976.343,16.057,7.600 |
| 7 | 9928.013,54.206,17.781 | 9973.373,17.373,9.254 |
| 8 | 9907.373,68.901,23.726 | 9970.160,18.796,11.044 |
| 9 | 9881.205,87.515,31.279 | 9966.686,20.334,12.980 |
| 10 | 9848.076,111.053,40.871 | 9962.928,21.997,15.075 |
| 11 | 9806.211,140.753,53.036 | 9958.865,23.794,17.341 |
| 12 | 9753.427,178.126,68.446 | 9954.472,25.736,19.792 |
| 13 | 9687.071,224.995,87.934 | 9949.723,27.834,22.443 |
| 14 | 9603.955,283.517,112.528 | 9944.589,30.101,25.310 |
| 15 | 9500.321,356.195,143.484 | 9939.040,32.549,28.410 |
| 16 | 9371.840,445.839,182.321 | 9933.044,35.193,31.763 |
| 17 | 9213.674,555.478,230.848 | 9926.565,38.048,35.388 |
| 18 | 9020.649,688.171,291.180 | 9919.565,41.129,39.306 |
| 19 | 8787.566,846.703,365.731 | 9912.005,44.454,43.542 |
| 20 | 8509.688,1033.143,457.169 | 9903.840,48.041,48.119 |
| 21 | 8183.408,1248.264,568.328 | 9895.024,51.910,53.066 |
| 22 | 7807.072,1490.880,702.048 | 9885.508,56.081,58.411 |
| 23 | 7381.814,1757.225,860.961 | 9875.237,60.578,64.185 |
| 24 | 6912.245,2040.546,1047.209 | 9864.156,65.422,70.422 |
| 25 | 6406.726,2331.126,1262.148 | 9852.203,70.640,77.157 |
| 26 | 5877.032,2616.902,1506.066 | 9839.315,76.257,84.428 |
| 27 | 5337.339,2884.672,1777.990 | 9825.421,82.302,92.277 |
| 28 | 4802.666,3121.702,2075.631 | 9810.449,88.804,100.747 |
| 29 | 4287.148,3317.356,2395.496 | 9794.321,95.793,109.886 |
| 30 | 3802.521,3464.337,2733.142 | 9776.956,103.301,119.743 |

Compare day30 and the largest printed infected count within this30-day horizon; do not call that the eventual epidemic peak. Reconstruct the first0.25day update independently to see why the daily rows cannot be reproduced by one-day Euler steps.

## Paper-Based Investigation {.unnumbered}

1. Calculate selection then transfer and reverse the order as a distinct model. Infer MIC from the assay; classify what the genomic cards support without assigning transfer direction.
2. For the two N1000 scenarios reconstruct the first two one-day SIR updates, check total-population bookkeeping by algebra and compare day4 infections. For the N10000 comparison reconstruct the first quarter-day update and compare day30 and the largest printed daily I. State why a finite-horizon maximum is not necessarily the full epidemic peak. Evaluate the disease-only vaccine counterexample and explain why the ideal immune-fraction boundary supplies no vaccination coverage without a transmission effect.
3. Calculate blood, urine and pooled resistance proportions at each site and explain the sampling-composition effect. Compare the official snapshot without fabricating raw counts. Route T1–T3 uniquely using the stated susceptibility/eligibility sequence; propose a feasible prevention discussion for P/M with surveillance and access limits.

## Data Recording {.unnumbered}

For each task record the case/replicate identifier, supplied inputs with units, equation or classification rule, intermediate calculation, result and one alternative explanation. Keep the printed evidence unchanged and mark any proposed exclusion with a reason.

## Paper-Based Evidence Upgrade {.unnumbered}

**Printed source card:** WHO's Global antibiotic resistance surveillance report 2025 (ISBN 9789240116337) and October 13, 2025 official news release provide the empirical snapshot above. The greater-than percentages are reported estimates, not raw numerator/denominator pairs. O’Neill 2016 is a historical conditional 2050 scenario, not current measured burden. WHO 2025 TB guidance and malaria indoor-emanator recommendations are conditional; clinical choices require full current eligibility and susceptibility review. All raw teaching tables and SIR trajectories are synthetic, not new empirical data or clinical forecasts. Source-card tasks: identify which observations are synthetic and which statements summarize published evidence; record the publication date and endpoint/model; name a refresh trigger. A live source lookup is not required to answer this packet.

## Analysis Questions {.unnumbered}

Explain what each assay and SIR control holds constant and why the 30-day maximum is horizon-limited. Then assess the proposed transfer “Site A has a larger population resistance burden because 14% exceeds Site B's pooled 10.4878%.” Use the within-specimen rates and specimen weights to diagnose the difference. State what a common specimen weighting could resolve and what population-sampling or incidence information would still be missing. Do not manufacture raw denominators from the WHO summary.

<!-- SOLUTION
## Instructor Worked Results and Scoring Expectations {.unnumbered}

Task 1: selection p=.10/(.10+.90×.5)=.181818; transfer then gives .181818+.1(.818182)=.263636. Reverse order gives p=.19 before selection and .19/(.19+.81×.5)=.319328 afterward. MIC 4 µg/mL. Core similarity supports a spreading clone hypothesis; plasmid sharing across lineages supports mobile-element sharing but not direction or the exact event history.
Task 2: baseline day 0→1 infection F 2.97, recovery G 1; day 1→2 F 3.544425, G 1.197. Reduced-contact F 1.485, G 1 initially; next F 1.55468696625, G 1.0485. The same F/G leave one compartment and enter another, so S+I+R stays 1000 before printing-roundoff. Day 4 I 20.425520 versus 12.069868, about 8.355652 fewer concurrently infected, not a demonstrated reduction in the eventual peak or final size. Disease-only vaccination leaves Re 4. The real API rejects beta×dt>1 or gamma×dt>1; grid safety does not ensure numerical accuracy, and output times honor the requested horizon.
Task 3: A blood 30%, urine 10%, pooled 70/500=14%; B blood 30%, urine 10%, pooled 86/820≈10.4878%. Different specimen weights explain the pooled difference despite identical within-specimen rates. Official adjusted estimates cannot be reconstructed by pooling these synthetic counts or multiplying their percentages by 23 million. T1: classical two-month HRZE then four-month HR; T2 excludes moxifloxacin-containing BPaLM and requires otherwise-eligible BPaL/alternative review; T3: specialist pathway, not an automatic short regimen. P supports discussion of suitable long-acting PrEP only after required testing/eligibility; M supports evaluating indoor emanators as an adjunct to nets with local surveillance, not replacing them.



**Thirty-day comparison:** Initial quarter-day baseline transfers are infection 0.874125 and recovery 0.25, giving S 9989.125875, I 10.624125, R 0.25. With distancing, infection 0.44955 gives S 9989.55045, I 10.19955, R 0.25. At the printed precision, baseline day 30 is S 3802.521, I 3464.337, R 2733.142 and distancing is S 9776.956, I 103.301, R 119.743. Each largest printed daily I occurs at day 30; their difference is 3361.036 concurrently infected. These are synthetic forward-Euler predictions, not empirical outbreak observations or a calibrated clinical forecast. Neither maximum establishes the eventual outbreak peak beyond the requested horizon.

Transfer benchmark: Both sites have 30% blood and 10% urine resistance; common specimen weights therefore produce the same standardized teaching proportion. The pooled difference reflects specimen composition. Standardization does not repair referral selection, establish community incidence or supply population denominators. The official global estimates cannot be reconstructed from these synthetic rows or by using the report-wide 23 million as an organism-specific denominator.
SOLUTION -->

## Safety and Ethics {.unnumbered}

Paper only: no hazardous materials or human-subject recruitment. Synthetic pedigrees and clinical cases are not diagnoses. Use person-first language, do not infer identity, parentage or ancestry from the examples, and distinguish equitable access and informed consent from the biological calculation.

## Optional Extension {.unnumbered}

Design, on paper, one additional controlled comparison and predict its result under each competing explanation. Actual wet or clinical work requires appropriate supervision and approval and is not part of this activity.
