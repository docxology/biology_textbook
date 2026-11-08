# Lab — Biodiversity and Food Webs {#sec:lab_unit_X_biodiversity_and_food_webs .unnumbered}

*This activity accompanies \cref{sec:unit_X_biodiversity_and_food_webs}.*

## Learning Objectives {.unnumbered}

- Apply richness and species-area reasoning with explicit assumptions.
- Calculate diversity/evenness from complete counts.
- Analyze finite food-web links and removal responses.
- Compare biodiversity-function evidence under controlled sampling.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Apply richness and species-area reasoning with explicit assumptions.
- **Outcome 2 (LO3):** Calculate diversity/evenness from complete counts.
- **Outcome 3 (LO2):** Analyze finite food-web links and removal responses.
- **Outcome 4 (LO7):** Compare biodiversity-function evidence under controlled sampling.



: Alignment and evidence-specific scoring. {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | Diversity/evenness, species–area, web/energy and removal computations |
| Controls | Equal area/effort, identity/fertility and predator-present controls |
| Uncertainty | Finite samples, denominator convention and synthetic-source boundaries |
| Mechanism | Keystone cascade, evenness and diversity-function hypotheses |
| Transfer | Reserve/function decision with overlap and non-energy constraints |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All counts, energy and removal observations are synthetic. They are not Paine’s empirical measurements. This is a standalone biodiversity/food-web lab, not a permuted competition worksheet.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: Diversity and habitat packet. {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map_2}
| Record | Counts or inputs | Boundary |
| --- | --- | --- |
| Even community | species A/B/C/D: 25/25/25/25 | 100 individuals |
| Dominated community | 70/15/10/5 | 100 individuals |
| East reserve | A, B, C, D | four identified species |
| West reserve | C, D, E, F | four identified species |
| Large reserve | A, B, C, D, E | five identified species |
| SAR | $S=10A^{0.25}$; $A$ in hectares; initial area 1,000 ha, new area 100 ha | equilibrium, constant quality |
| Function replicates | richness 1: 8/10/12; richness 4: 16/18/20 g biomass m−2 | randomized plots, common fertility |


: Food web and energy packet. {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map_3}
| Record | Given | Definition |
| --- | --- | --- |
| Nodes | G producer; H herbivore; D detritivore; P predator; A apex consumer | $S=5$ |
| Feeding links | G → H; G → D; H → P; D → P; P → A | resource → consumer; G → D means dead G |
| Connectance | L/[S(S−1)] | directed, no self-links |
| Production | G: 10,000 kJ/day; each transfer efficiency 0.1 | hypothetical constant efficiency |
| Human comparison | one person requires 10,000 kJ/day; all harvestable production assumed edible | person-equivalent days only, not real nutrition |
| Functions | H pollination index 0; D decomposition index 8; P pest-control index 6 | trait cards, not universal roles |


: Synthetic keystone-removal experiment. {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map_4}
| Replicate | Predator-present richness before/after | Predator-removed richness before/after | Dominant mussel cover, present/removed (%) |
| --- | --- | --- | --- |
| 1 | 15/15 | 15/8 | 30/80 |
| 2 | 14/14 | 14/7 | 32/82 |
| 3 | 16/16 | 16/9 | 28/78 |


: Boundary and conservation cards. {#tbl:unit_X_biodiversity_and_food_webs_packet_5}
| Scenario | Evidence supplied | Question |
| --- | --- | --- |
| Paine principle | predator removal can release competitive dominants; see the chapter's primary citation | mechanistic analogy, not these actual counts |
| Two small versus one large | use printed East/West/Large species lists | union versus sum |
| Unequal sampling | site 1: 20 species observed among 100 individuals; site 2: 30 among 1,000 | rarefaction/detection needed |
| Function reliability | richness 1, yearly biomass: 10/4/16; richness 4: 18/16/20 | mean and temporal variability |

## Paper-Based Investigation {.unnumbered}

1. Calculate S,H=−Σpi lnpi and J=H/lnS for both count tables. Show all four contributions and distinguish richness from evenness. Explain the sampling controls needed for the unequal-effort card.
2. Draw the five-node web and compute link count/connectance using the supplied denominator. Define basal, detrital and apex pathways; a real omnivore can span positions.
3. Calculate production at H, P and A for the simple G→H→P→A chain. Convert each to hypothetical person-equivalent days using the supplied energy requirement. Explain why energy alone is not a complete human carrying-capacity calculation.
4. Compute removal-minus-control richness change and mussel-cover contrasts. Explain a predator-mediated diversity mechanism and alternatives, including disturbance/plot effects. Distinguish the synthetic experiment from the cited historical study.
5. Calculate East∪West richness versus Large, then species-area predictions after habitat loss. Compare function means/temporal ranges; propose randomization, species-identity, area and fertility controls before attributing function to diversity.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sample SD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

Competition invasion calculations belong in the community lab. Here all required species identities, links, energy denominators and removal comparisons are printed; no external documentary or unspecified “Paine data” is needed.

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

Even-community H=ln4=1.386294, J=1; dominated-community H≈.914286, J≈.659486. Both have S=4. Five links give connectance 5/20=.25 under the stipulated no-self denominator; 5/25=.20 uses a different convention. Chain production at H, P, A is 1000, 100, 10 kJ/day, equivalent to .1, .01, .001 hypothetical person-days per day. Removal richness changes −7 in every replicate versus 0 in controls; mussel cover means 80 versus 30%, a 50-point difference. East∪West has 6 species, not 8; Large has 5. SAR richness 56.2341→31.6228, a 43.7659% decline. Function means 10 versus 18 g/m²; yearly ranges 12 versus 4 indicate lower variation only in this tiny synthetic series. These are not historical Paine measurements.

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
