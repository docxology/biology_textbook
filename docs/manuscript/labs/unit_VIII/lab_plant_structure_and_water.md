# Lab — Plant Structure and Water Relations {#sec:lab_unit_VIII_plant_structure_and_water .unnumbered}

*This activity accompanies \cref{sec:unit_VIII_plant_structure_and_water}.*

## Learning Objectives {.unnumbered}

- Calculate water potential and predict root-to-leaf water movement.
- Normalize replicated water-loss measurements and test environmental predictions.
- Trace the selective root pathway using the supplied anatomical schematic.
- Compare carbon-water tradeoffs using explicitly defined efficiencies.

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO3):** Calculate water potential and predict root-to-leaf water movement.
- **Outcome 2 (LO4):** Normalize replicated water-loss measurements and test environmental predictions.
- **Outcome 3 (LO5):** Trace the selective root pathway using the supplied anatomical schematic.
- **Outcome 4 (LO9):** Compare carbon-water tradeoffs using explicitly defined efficiencies.



: Alignment and evidence-specific scoring. {#tbl:unit_VIII_plant_structure_and_water_alignment_and_rubric_map}
| Dimension | 4-point evidence requirement |
| --- | --- |
| Evidence | correct blank/area/time/molar normalization with replicates |
| Controls | matched environment, blank, soil seal, and independent pots |
| Uncertainty | range/SD plus limitations of three pots and unmatched model parameters |
| Mechanism | potential direction and endodermal selectivity; distinguish A/gs from A/E |
| Transfer | quantified irrigation-yield recommendation with a testable follow-up |

Each dimension is worth 4 points (total 20): award 4 for a correct supported response, 2 for a partially correct response with an important omission, 1 for a relevant but unsupported assertion, and 0 for absent/incorrect work. The evidence column states the actual product required, not a generic participation criterion.
<!-- lab-alignment-end -->

## Lab Context {.unnumbered}

All measurements below are synthetic teaching observations, not measurements from a cited experiment. They form a complete paper packet: no plant, microscope, internet connection, or Python installation is required.

## Paper-Based Materials {.unnumbered}

Print this entire packet including its supplied tables; use paper, pencil and a calculator. Graph paper is optional. Everything needed for the core investigation is printed below. Optional code or literature links are not required observations.

## Supplied Evidence Packet {.unnumbered}


: Root and stem schematic cards. {#tbl:unit_VIII_plant_structure_and_water_part_3_transpiration_dataset_and_model_check}
| Card | Printed description | Feature to label |
| --- | --- | --- |
| Root radial section | Outside→root hair/epidermis→cortex→suberized endodermis→pericycle→central vascular cylinder | apoplast, symplast, Casparian strip |
| Young eudicot stem | Epidermis encloses cortex; ring of bundles has external phloem, cambium, internal xylem | tissue systems and transport direction |
| Young monocot stem | Vascular bundles scattered in ground tissue; each has xylem and phloem | contrast with eudicot; do not infer all monocots lack secondary thickening |


: Replicated transpiration inputs. {#tbl:unit_VIII_plant_structure_and_water_part_3_transpiration_dataset_and_model_check_2}
| Treatment | Loss in 30 min, pots 1/2/3 (g) | Leaf area per pot (m²) | A (µmol CO2 m−2 s−1) | gs (mol H2O m−2 s−1) |
| --- | --- | --- | --- | --- |
| Still air,22°C,50%RH | 1.0/1.1/.9 | .010 | 10 | .20 |
| Wind,22°C,50%RH | 1.5/1.6/1.4 | .010 | 11 | .22 |
| Still,32°C,50%RH | 1.8/1.9/1.7 | .010 | 9 | .18 |
| Still,22°C,80%RH | .4/.5/.3 | .010 | 10 | .20 |


: Leaf and irrigation comparison cards. {#tbl:unit_VIII_plant_structure_and_water_part_3_transpiration_dataset_and_model_check_3}
| Case | Stomata(mm−2) | Thickness(mm) | Irrigation(Lm−2season−1) | Yield(kgm−2season−1) |
| --- | --- | --- | --- | --- |
| Mesic crop | 180 | .20 | 300 | 1.5 |
| Thick xeromorphic crop | 80 | .60 | 200 | 1.2 |
| Thin aquatic emergent | 250 | .12 | 400 | 1.6 |


: Water potential and flux inputs. {#tbl:unit_VIII_plant_structure_and_water_packet_5}
| Compartment | Ψs(MPa) | Ψp(MPa) | height(m) |
| --- | --- | --- | --- |
| Soil | −.20 | 0 | 0 |
| Root cell | −.60 | .20 | 0 |
| Xylem at leaf | −.10 | −1.60 | 10 |
| Mesophyll | −1.90 | 0 | 10 |

Assume the matric term is negligible in these aqueous compartments. Use Ψ=Ψs+Ψp+ρgh with ρ=1000 kg m−3, g=9.81 m s−2, and 1 MPa=10^6 Pa. Flux comparison uses conductance .20 mol m−2 s−1 and dimensionless internal/external water-vapor mole fractions .0125/.0075. Pots are sealed over soil; matched unplanted blanks each lose .05 g in 30 min. Subtract blank loss before normalization. Molar mass water=18 g mol−1.

Anatomy reference for the drawing: roots anchor the plant and acquire water/ions; shoots comprise stems, leaves and reproductive organs. Dermal tissue covers organs, ground tissue supports storage/photosynthesis, and vascular tissue contains xylem and phloem. The apoplast follows cell walls; the symplast follows connected cytoplasm. In this simplified young-root model stipulate an intact endodermal Casparian strip with no developmental bypass: radial apoplastic entry is blocked, so an ion must cross a selective membrane before vascular access. This is a model boundary, not perfect exclusion in every real root.

## Paper-Based Investigation {.unnumbered}

1. Draw and label the two organ systems and three tissue systems. Under the stipulated intact-barrier/no-bypass model, trace one ion from soil to xylem and mark its membrane-selective entry. Explain why real developmental discontinuities limit generalization.
2. For each environment subtract the blank, divide by .010 m² and 1800 s, and convert grams to mmol water. Report mean, range, sample SD (n−1 denominator), and individual values. Compare each change with still-air reference; identify treatment, response, controls, and pot rather than leaf subsample as the experimental unit.
3. Calculate each Ψ and water-flow direction. Reconcile gravitational head with the supplied negative pressures; do not change gravitational sign to force an answer.
4. Calculate conductance×mole-fraction difference; compare that illustrative model flux with measured flux without assuming that its parameters describe every treatment. Calculate A/gs (intrinsic WUE) and A/E (instantaneous WUE, using measured molarE). Distinguish these from seasonal yield/irrigation.
5. Recommend a crop under limited irrigation, stating the yield sacrificed, uncertainty, and a field control needed before attributing differences to stomatal density.

## Data Recording {.unnumbered}

For each task record: given inputs with units; equation/assumption; intermediate arithmetic; result with units; replicate identifier; comparison/control; and one limitation. Draw graphs with labeled axes and retain individual observations rather than only a fitted line. Report range or sampleSD where replicates are supplied; do not invent confidence intervals from absent data.

## Paper-Based Evidence Upgrade {.unnumbered}

Use the chapter transpiration model only as an optional calculation cross-check; supply dimensionless mole fractions, not kPa vapor pressures. A new crop with equal gs but twice A doubles intrinsicWUE without proving seasonal yield doubles.

## Analysis and Submission {.unnumbered}

Submit labeled diagrams and calculations for every numbered investigation task, a concise results table or graph, and a claim–evidence–mechanism paragraph. Close with the strongest alternative explanation, a discriminating control, and a transfer decision whose assumptions are explicit. Clearly distinguish synthetic observations from cited biological mechanisms.

## Safety and Ethics {.unnumbered}

This is a paper-only exercise. Do not collect human/animal specimens, administer drugs, conduct stimulation or release organisms. Synthetic clinical-style patterns are not diagnoses or treatment advice. Respect source attribution, participant privacy, local rights and ecological uncertainty.

<!-- SOLUTION
### Instructor Worked Key {.unnumbered}

Reference corrected losses=.95, 1.05, .85 g, mean .95 g; mean E=.95/18×1000/(.01×1800)=2.9321 mmol m−2 s−1 and sample SD=.30864. Wind/heat/humid means are 4.4753/5.4012/1.08025 mmol m−2 s−1. Root Ψ=−.40 versus soil −.20, favoring entry. Leaf xylem Ψ=−1.6019 and mesophyll −1.8019 MPa, favoring xylem→mesophyll; gravity contributes +.0981 MPa. Model E=.001 mol=1 mmol m−2 s−1. Reference intrinsic WUE=50 µmol CO2/mol H2O; instantaneous WUE=10/.0029321≈3410.5 µmol/mol (3.4105 mmol/mol). Seasonal efficiencies are .005, .006, .004 kg/L; the xeromorphic card has highest irrigation efficiency, not highest absolute yield. Anatomy alone cannot establish a treatment effect.

In treatment order, mean corrected E values above each have sample SD .30864 mmol m−2 s−1 and replicate range width .61728; wind, heat and humid means differ from reference by +52.63%, +84.21% and −63.16%. Intrinsic A/gs is 50 µmol/mol for all four cards, whereas A/E is approximately 3410.5, 2458.6, 1666.3, 9257.1 µmol/mol. The xeromorphic crop saves 100 L/m² versus mesic but sacrifices .3 kg/m² yield (20%); compare these stipulated seasonal outcomes, not an inferred causal effect of stomatal density.

Accept equivalent correctly bounded reasoning. Check the complete working, units, control logic and uncertainty—not agreement with a preferred narrative.
-->
