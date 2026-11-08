# Lab — Community Interactions and Succession {#sec:lab_unit_X_community_interactions .unnumbered}

*This activity accompanies \cref{sec:unit_X_community_interactions}.*

## Learning Objectives {.unnumbered}

- Classify competition regimes using invasion margins.
- Evaluate direct/indirect effects in a supplied community network.
- Compare succession with soil and disturbance legacies.
- Assess biocontrol benefits, non-target effects and evidence quality.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO2):** Classify competition regimes using invasion margins.
- **Outcome 2 (LO8):** Evaluate direct/indirect effects in a supplied community network.
- **Outcome 3 (LO7):** Compare succession with soil and disturbance legacies.
- **Outcome 4 (LO11):** Assess biocontrol benefits, non-target effects and evidence quality.



: Alignment and evidence-specific scoring. {#tbl:unit_X_community_interactions_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | invasion/equilibrium,plotcontrasts andtrait calculations |
| Controls | monocultures,matchedbiocontrolarms andsitehistory controls |
| Uncertainty | n3plots,nonequilibrium andchronosequence confounding |
| Mechanism | competition/nullcline anddirect/indirect interaction mechanisms |
| Transfer | biocontrol decision balancing yield,nontarget andrights evidence |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All abundance, network and succession cards are synthetic. This is a standalone competition/community laboratory, not a food-energy or Shannon worksheet renamed from biodiversity.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: Replicated competition observations. {#tbl:unit_X_community_interactions_source_governance_checkpoint}
| Day | Aalone(rep1/2/3) | Balone | Ainmixture | Binmixture |
| --- | --- | --- | --- | --- |
| 0 | 10/10/10 | 10/10/10 | 10/10/10 | 10/10/10 |
| 4 | 35/37/39 | 34/36/38 | 30/32/34 | 29/31/33 |
| 8 | 75/77/79 | 74/76/78 | 53/55/57 | 52/54/56 |
| 14 | 98/100/102 | 97/99/101 | 65/67/69 | 64/66/68 |


: Parameter and legacy cases. {#tbl:unit_X_community_interactions_packet_3}
| Card | Inputs | Boundary |
| --- | --- | --- |
| Coexistence | K1=K2=100,a12=a21=.5,r1=r2=.2/day | positive growth rates |
| Species1wins | K1=1000,K2=500,a12=.8,a21=.9 | u600,v−400 |
| Species2wins | K1=500,K2=1000,a12=.9,a21=.8 | u−400,v600 |
| Priority | K1=K2=100,a12=a21=1.5 | interior saddle |
| Barelavayear1 | no organic soil;lichen/mosscover20%,vascular5% | primarysuccession |
| Abandonedfieldyear1 | topsoil/root bank;grass60%,shrub5% | secondarysuccession |
| Fieldyear10 | grass30%,shrub40%,tree10% | different cohort, not repeat observation |
| Fieldyear40 | grass10%,shrub20%,tree60% | land use/climate unmeasured |


: Forest network and service packet. {#tbl:unit_X_community_interactions_packet_4}
| Component | Printed interactions or measurements | Task |
| --- | --- | --- |
| 15 nodes | oak, maple, pine, grass, fern, fungus, bacteria, deer, hare, caterpillar, aphid, beetle, spider, bird, fox | count distinct nodes |
| Directed feeding links (resource → consumer) | oak → deer; maple → deer; grass → hare; oak → caterpillar; maple → aphid; caterpillar → bird; aphid → beetle; beetle → spider; spider → bird; hare → fox; bird → fox | direct versus indirect |
| Nonfeeding links | fungus ↔ oak nutrient/carbon exchange; dead pine → fungus; detritus → bacteria | separate interaction types |
| Traits | oak leaf N 1, grass 3; weights .6/.4 versus .2/.8 | community-weighted leaf N |
| Biocontrol plots | pest before 100/100/100; after enemy release 20/25/30; matched control 80/85/90 | three plots per arm |
| Nontarget counts | release 5/6/4; control 20/19/21 | possible cost |
| Service outcomes | yield release 8/9/10, control 6/7/8 kg/plot; infiltration both 10/11/12 mm/h | no universal service gain |

Network/trait reference: the 15 named living nodes define the counted community; detritus is an external nonliving pool, and “dead pine” is material from the named pine node, not another species. A feeding arrow runs resource→consumer: consumers depress their resources, so greater fox predation on hare can indirectly release grass. The mutualism card stipulates reciprocal resource benefit, not a measured interaction coefficient. Leaf-N values 1 and 3 use the same arbitrary trait units; community-weighted mean=Σ(relative abundance×trait value). Treat each independent plot, not repeated organisms within it, as the biocontrol replicate.

## Paper-Based Investigation {.unnumbered}

1. Plot monoculture/mixed means and ranges. Estimate K from monocultures. Solve N1+a12N2=K1 and a21N1+N2=K2 for the coexistence case. Compare with day14 without assuming equilibrium.
2. Compute u=K1−a12K2 and v=K2−a21K1 for all four cases. Classify coexistence, exclusion or priority effects. Explain why zero margins and a12a21=1 need separate boundary analysis. Do not substitute a predator-prey API.
3. Draw the forest links with separate feeding, mutualism and decomposition legends. Give a fox→hare→grass indirect pathway. Signs alone do not estimate interaction strength or stability.
4. Compare primary/secondary succession cards and the chronosequence. Identify soil/root legacy, site history and longitudinal controls before inferring facilitation or inevitable climax. Calculate both weighted leaf-N values.
5. Quantify pest, yield and non-target contrasts. Design randomized matched plots, dispersal tracking and release-free controls. Balance benefits against persistence, non-target harm and local consent.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sampleSD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

Analytical invasion and equilibrium calculations suffice; no nonexistent competition API is required. Distinguish a topological network from a parameterized dynamical model.

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

Coexistence equilibrium is 66.6667 per species; day 14 means 67 and 66 are compatible with approach, not proof. Margins u,v are 50,50 (coexistence); 600,−400 (species 1); −400,600 (species 2); −50,−50 (priority). The priority case has an interior saddle, not stable coexistence. The forest has 15 named nodes and 11 listed feeding links; the other interaction types require separate definitions. Weighted leaf N=1.8 versus 2.6. Pest means 25 versus 85: a 60-count difference; declines from baseline are 75 versus 15. Yield means 9 versus 7 kg; non-target means 5 versus 20, a 15-count reduction. Equal infiltration does not demonstrate a soil-service gain. Successional cohorts are not necessarily one causal time trajectory.

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
