# Lab — Population Ecology and Growth Models {#sec:lab_unit_X_population_ecology .unnumbered}

*This activity accompanies \cref{sec:unit_X_population_ecology}.*

## Learning Objectives {.unnumbered}

- Compare exponential/logistic fits and finite-step error.
- Test a strong-Allee threshold with supplied colony records.
- Estimate abundance from complete capture histories.
- Separate harvest and viability decisions from fixed-model predictions.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO2):** Compare exponential/logistic fits and finite-step error.
- **Outcome 2 (LO4):** Test a strong-Allee threshold with supplied colony records.
- **Outcome 3 (LO8):** Estimate abundance from complete capture histories.
- **Outcome 4 (LO10):** Separate harvest and viability decisions from fixed-model predictions.



: Alignment and evidence-specific scoring. {#tbl:unit_X_population_ecology_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | growth/capture/matrix/harvest computations with time units |
| Controls | closedmarkedpond and controlledcolonycomparison |
| Uncertainty | rounding,timestep,capturebias andPVA scenario uncertainty |
| Mechanism | densitydependence,Allee mechanism andstageversusage distinction |
| Transfer | harvest/viability recommendation with explicit endpoint |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All series and capture histories are synthetic. Parameters illustrate mechanisms, not forecasts for yeast, deer, moths or social-insect species.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: Population time series. {#tbl:unit_X_population_ecology_alignment_and_rubric_map_2}
| Time | Yeast(cells/mL) | Introducedmoth(count) | Hareindex |
| --- | --- | --- | --- |
| 0 | 10 | 10 | 50 |
| 1 | 18 | 20 | 70 |
| 2 | 31 | 40 | 100 |
| 3 | 50 | 80 | 140 |
| 4 | 69 | 160 | 160 |
| 5 | 83 | 320 | 140 |
| 6 | 92 | 640 | 100 |
| 7 | 96 | 1280 | 70 |
| 8 | 98 | 2560 | 50 |
| 9 | 99 | 5120 | 40 |
| 10 | 100 | 10240 | 50 |


: Capture histories and density experiment. {#tbl:unit_X_population_ecology_alignment_and_rubric_map_3}
| Record | Supplied data | Assumptions |
| --- | --- | --- |
| Firstcapture | IDs1–50marked,released | marks retained, no harm |
| SecondcaptureA | 30 fish;markedIDs1–5;25unmarked | MC/R; independent mixing |
| SecondcaptureB | 30 fish;markedIDs6–11;24unmarked | alternative independent sample, not merged |
| Knownpondcensus | 300 fish | for relative-error comparison only |
| Deer | N100/300/500,K500,r.2yr−1 | fixed logistic |
| Modelcheck | N0=50,K500,r.3,t=10yr | analytic versus Euler; not observed series |


: Colony Allee, harvest and viability cards. {#tbl:unit_X_population_ecology_packet_4}
| Case | Given | Task |
| --- | --- | --- |
| Colony founding | A20, K200, r.4 yr−1; N10/30/100; dN/dt=rN(1−N/K)(N/A−1) | sign and per-capita rates |
| Replicate founding outcomes | N10:0/10 survive; N30:6/10; N100:9/10 at1 yr | synthetic associations, not proof alone |
| Fish harvest | r.2 yr−1, K500000 fish; N100000 | growth and MSY |
| Stochastic PVA | N50:200/1000 extinctions by100 yr; N200:40/1000 | specified scenario only |
| Stage matrix | rows [0,0,2], [.4,0,0], [0,.5,.5]; initial [50,20,10] | stages, not strict ages |

Calculation reference: the three printed time series use arbitrary shared time units, not asserted species-specific years. For fixed-r,K logistic growth use N(t)=K/[1+(K/N0−1)exp(−rt)], dN/dt=rN(1−N/K), and per-capita growth r(1−N/K). For the yeast increment comparison estimate r from the first interval as (N1−N0)/[N0(1−N0/K)], with K estimated from its plateau; do not borrow r from the separate deer/model-check cards. In the stage model, multiply the printed matrix by the column vector of stage counts; columns identify source stages and rows destination stages. PVA persistence=1−extinctions/runs for the printed100-year horizon.

## Paper-Based Investigation {.unnumbered}

1. Plot all series on linear and log axes. Estimate moth r=ln(Nt/N0)/t and yeast K. Estimate yeast r from its first increment using the printed rule, then compare later increments with rN(1−N/K). Rounded observations do not establish an exact law, and a monotone curve cannot explain the hare cycle.
2. Use N=MC/R for each capture. Report absolute and relative error versus 300. Explain mark loss, unequal catchability and migration biases; the printed sample contains an integer number of marked fish.
3. Compute deer per-capita and total growth. For N0=50, K=500, r=.3, compare exact logistic N10 with one forward-Euler step of 10 years: N10≈N0+10rN0(1−N0/K). Explain why such a coarse step is not a credible trajectory; propose smaller-step convergence comparison.
4. Compute colony growth signs and per-capita rates. Design a worker-number experiment controlling queen condition, food and disease. Project the stage matrix once and twice.
5. Compare fish growth at N100000 with rK/4 and identify the abundance maximizing growth. Interpret the PVA scenario; genetic Ne guidelines are not census-MVP predictions.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sampleSD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

An optional canonical logistic_growth(N0,r,K,t_end,steps) returns a result with populations. It is a numerical model; compare convergence against the supplied analytic formula. The continuous fixed-r,K logistic equation does not generate chaos.

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

Moth r=ln2=.693147 per time unit; yeast plateau≈100. Hare values cycle over 10 time units. Capture estimates 300 and 250 have relative errors 0 and 16.667%. Deer per-capita growth=.16, .08, 0 yr−1; totals 16, 24, 0. Analytic model N10≈345.284; the single-step Euler estimate 185 underestimates by 160.284. Coarse-step error is not biological evidence of oscillation. Colony per-capita rates −.19, .17, .8 yr−1 give total growth −1.9, 5.1, 80. A fixed threshold A defines strong Allee dynamics; survival associations alone have alternatives. Stage projections are [20,20,15], then [30,8,17.5]. Fish growth 16000 fish/yr versus MSY 25000 at N=250000. PVA persistence 80% and 96% is conditional on the specified model.

With yeast K≈100, the first-interval increment 8 gives illustrative r≈8/[10×.9]=.888889 per time unit. For the next interval this predicts 13.12 cells/mL versus the printed increment 13; at N=31 it predicts 19.0133 versus 19. Such comparisons assess a rough finite-step model, not proof of an exact differential equation. Capture absolute errors are 0 and 50 fish; the second estimate undercounts. The Allee r is .4 yr−1 for the founding model, so its per-capita rates and the one-year outcome comparison share that time unit.

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
