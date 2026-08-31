# Lab — Plant Structure and Water Relations {#sec:lab_unit_VIII_plant_structure_and_water .unnumbered}


*This activity accompanies \cref{sec:unit_VIII_plant_structure_and_water} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design a paper-based transpiration investigation using printed plant-water datasets
- Formulate testable hypotheses about how environmental factors affect transpiration rate
- Identify independent, dependent, and controlled variables in plant physiology experiments
- Analyze experimental data using water potential calculations and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Plant Structure and Water Relations.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Define water potential Ψ and explain why water moves spontaneously from high to low Ψ — give one example of each water potential component (solute, pressure, matric).
2. Describe the role of the Casparian strip in the endodermis — why must water enter the symplast at this point?
3. Distinguish xylem from phloem: which conducts water and which conducts photosynthate, and what structural features reflect their different functions?

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of transpiration, predict which environmental condition (bright light, wind, high humidity, dim light) will result in the highest transpiration rate. Write a clear, testable hypothesis.

2. **Experimental Design**: What is the independent variable in a transpiration experiment? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: The cohesion-tension theory explains how water moves upward in plants against gravity. Why is this mechanism dependent on transpiration? What would happen to water transport if transpiration were completely stopped?

4. **Quantitative Reasoning**: If a plant loses 5 grams of water in 30 minutes, what is its transpiration rate in g/hr? If the leaf surface area is 100 cm², what is the transpiration rate per unit area (g/m²/hr)?

5. **Real-World Application**: Drought stress affects crop yields. How does understanding transpiration help in developing drought-resistant crops? What traits would you select for?

## Lab Context: Plant Structure and Water Relations {.unnumbered}

Vascular plants have three tissue systems: dermal (epidermis, cuticle, guard cells), ground (parenchyma, collenchyma, sclerenchyma), and vascular (xylem for water/mineral transport upward; phloem for sugar/assimilate transport, bidirectional). Transpiration — evaporation of water from stomata — drives the cohesion-tension mechanism that pulls water from root to leaf. Environmental factors (light, humidity, temperature, wind) modulate transpiration rate by affecting stomatal aperture.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_VIII_plant_structure_and_water_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Plant Structure and Water Relations: plant evidence source card: tissue, driver, field context, breeding/adoption boundary, and refresh trigger | 1 |
| Printed dicot stem and root cross-section diagrams with scale bars | 1 packet |
| Transpiration dataset for four environmental treatments, with three replicates each | 1 |
| Leaf-area and stomatal-density data cards for broadleaf, needleleaf, and succulent plants | 1 set |
| Water-potential reference sheet and worked example | 1 |
| Crop water-use case packet with drought, yield, and irrigation data | 1 |
| Graph paper or spreadsheet template | 1 |
| Calculator or optional Python REPL with this project installed | 1 |
| Optional extension card describing a potometer or celery-dye demonstration | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Anatomical Diagram and Tissue Identification {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how stem and root anatomy differ in their vascular tissue arrangement.

2. **Identify Variables**:
   - Independent variable: Plant organ (stem vs root)
   - Dependent variable: Tissue arrangement and identification
   - Controlled variables: image source, scale-bar calibration, diagram resolution, tissue orientation, scoring key, and blind-card order.

3. **Set Up Controls**: Why is it important for the diagram packet to include a labeled reference image and an unlabelled image from the same species? What other controls could you include to ensure accurate tissue identification?

4. **Data Collection**:
   - Use the printed stem cross-section diagram to identify and label: epidermis, cortex (parenchyma), vascular bundles (xylem = larger, thick-walled; phloem = smaller, thin-walled), pith.
   - Use the printed root cross-section diagram to identify: epidermis (root hairs), cortex, endodermis (Casparian strip), pericycle, vascular cylinder (xylem star pattern; phloem between xylem arms).
   - Record at least three independent tissue-identification decisions per organ, citing the visual feature used for each decision.

### Part 2: Computational Biology Exercise — Transpiration Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Check water-potential and transpiration calculations from your data table.

```python
from biology.botany import transpiration_flux, water_potential

leaf = water_potential(solute_concentration_M=0.3, turgor_pressure_MPa=0.4)
flux = transpiration_flux(
    stomatal_conductance_mol_m2_s=0.2,
    internal_vapor_conc_mol_m3=0.5,
    external_vapor_conc_mol_m3=0.3,
)

print("water potential:", round(leaf.water_potential_MPa, 3), "MPa")
print("transpiration flux:", round(flux.flux_mmol_m2_s, 2), "mmol m^-2 s^-1")
```
### Part 3: Transpiration Dataset and Model Check {.unnumbered}

5. **Design an Alternative Dataset**: Instead of just comparing environmental treatments, design a dataset to test how plant species with different leaf types (e.g., broadleaf vs needleleaf) differ in their transpiration rates. What hypothesis would you test? Which variables would you hold constant?

6. **Hypothesis**: Predict the relationship between leaf surface area and transpiration rate. Would you expect a linear relationship, or would stomatal density also play a role? Why?

7. **Reproducibility Check**: For each treatment, calculate the mean, range, and coefficient of variation across the three printed replicates. Flag any replicate that would change the treatment ranking if removed, and decide whether it should be retained.

## Data Recording {.unnumbered}

: Part 3: Transpiration Dataset and Model Check: Structure and Observed in stem?. {#tbl:unit_VIII_plant_structure_and_water_part_3_transpiration_dataset_and_model_check}
| Structure | Observed in stem? | Observed in root? | Function |
| --------- | ----------------- | ----------------- | -------- |
| Epidermis | | | |
| Xylem | | | |
| Phloem | | | |
| Endodermis | | | |
| Pith | | | |

: Part 3: Transpiration Dataset and Model Check: Condition and Mean water loss (g). {#tbl:unit_VIII_plant_structure_and_water_part_3_transpiration_dataset_and_model_check_2}
| Condition | Mean water loss (g) | Time (min) | Transpiration rate (g/min) | Transpiration (g/m²/min) |
| --------- | -------------- | ---------- | ------------------------- | ------------------------ |
| Dim light, still | | | | |
| Bright light, still | | | | |
| Dim light, fan | | | | |
| Bag (humid, still) | | | | |

Diagram evidence for xylem pathway: feature 1: ___; feature 2: ___; feature 3: ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Measure or model water movement through plant tissues.
- **Data skill to practice:** Interpret plant-water data from pressure, solute, and humidity measurements.
- **BioSkills emphasis:** Interdisciplinary nature of science, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Plant Structure and Water Relations** with a reproducibility pass:

: Part 3: Transpiration Dataset and Model Check: Evidence check and Student action. {#tbl:unit_VIII_plant_structure_and_water_part_3_transpiration_dataset_and_model_check_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this water-relations lab, anchor every claim to a water-potential value or gradient and the hydraulic pathway it acts on (soil-root-xylem-leaf-air), and distinguish stomatal regulation, tissue anatomy, and stress context as separate, testable controls on transport. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Water Potential and Osmotic Equilibrium {.unnumbered}

**Problem:** A mesophyll cell has solute potential Ψs = −0.9 MPa and pressure potential Ψp = 0.4 MPa, giving Ψcell = −0.5 MPa. After 2 hours of transpiration, Ψp drops to 0.15 MPa (Ψs unchanged). (a) Calculate the new Ψcell. (b) If xylem water potential is −0.35 MPa, predict direction of water movement between cell and xylem. (c) If the cell is placed in a sucrose solution with Ψsolution = −0.7 MPa, predict osmotic direction.

**Solution:** (a) New Ψcell = −0.9 + 0.15 = −0.75 MPa. (b) Ψcell (−0.75) < Ψxylem (−0.35), so water moves from xylem into the cell. (c) Ψcell (−0.75) < Ψsolution (−0.7) numerically (more negative), so water moves from solution into cell — wait, water moves toward lower (more negative) Ψ: Ψcell = −0.75 is more negative than Ψsolution = −0.7, so water moves from solution into cell.

**Interpretation:** Both solute concentration (Ψs) and turgor pressure (Ψp) determine the direction of water movement. Transpiration lowers Ψp, creating the driving force for water uptake from xylem — the basis of the cohesion-tension mechanism.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Plant Structure and Water Relations before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. The diagram packet traces water movement through xylem rather than phloem. Why does bulk water transport follow xylem pathways, and what would you predict for sugar movement in phloem under the pressure-flow hypothesis?

2. Which condition produced the highest transpiration rate — bright light or fan? Explain why wind increases transpiration using the concept of the diffusion boundary layer.

3. Stomata open when guard cells swell (K⁺ influx followed by water via osmosis). Explain how light triggers stomatal opening via the proton pump (H⁺-ATPase) and K⁺ channels, and why abscisic acid (ABA) causes stomatal closure during drought.

4. The Casparian strip forces water from the cortex to enter the endodermis symplastically (through cells), not apoplastically (through cell walls). Why is this selectivity important for plant mineral uptake?

5. A plant biologist clips the tip of a phloem sieve tube using a laser scalpel. Predict what happens to sugar transport above and below the cut within 30 seconds, using your knowledge of the pressure-flow hypothesis for phloem loading and unloading.

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: Using the three printed replicates per treatment, how would you analyze variation in transpiration rates? What statistical test would you use to determine if differences between conditions are significant?

7. **Experimental Error Analysis**: What are three potential sources of error in transpiration measurements? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you wanted to test the effect of a specific hormone (e.g., ABA) on stomatal closure using a paper dataset, what concentrations would you include, what response variable would you measure, and what baseline comparison would make the result interpretable?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Study of Plant Water Use Efficiency**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How does water use efficiency (WUE) vary among plant species from different environments?
- Formulate a hypothesis about the relationship between WUE and drought tolerance
- Design an experiment measuring transpiration and photosynthesis rates

**Session 2**: Data Extraction and Analysis
- Extract transpiration rates from printed potometer or gravimetric datasets
- Compare photosynthesis rates from CO₂ exchange or O₂ evolution data tables
- Calculate intrinsic water use efficiency (photosynthesis/transpiration)

**Session 3**: Data Interpretation and Presentation
- Compare WUE across species
- Correlate WUE with environmental adaptations (e.g., leaf thickness, stomatal density)
- Create a scientific poster or presentation

## Real-World Problem Solving: Plant Water Relations and Agriculture {.unnumbered}

**Case Study: Irrigation Management**

1. **Research Task**: Investigate the concept of crop water use efficiency (WUE). What is the typical range for major crops like wheat, rice, and corn? How does WUE vary with environmental conditions?

2. **Ethical Consideration**: Should farmers be encouraged or required to use water-saving irrigation techniques (e.g., drip irrigation) in water-scarce regions? What are the economic and social implications of such policies?

3. **Policy Proposal**: Design a policy to promote water-efficient agriculture in drought-prone areas. Consider: incentives for adopting efficient irrigation, water pricing, and monitoring systems.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A plant growing in moderately saline soil (Ψsoil = −0.6 MPa) must maintain sufficient turgor for cell expansion.
>
> (a) Using water potential arithmetic, explain what adjustments the plant must make to Ψs and/or Ψp to maintain a favorable Ψcell for water uptake from the soil.
> (b) Evaluate the metabolic cost of osmotic adjustment (accumulating compatible solutes such as proline or glycine betaine) compared to the alternative of reducing cell expansion and growth.
> (c) Predict how a plant adapted to saline conditions (halophyte) would differ from a glycophyte in terms of root cell Ψs values at equivalent soil salinity.

## Optional Wet-Lab Demonstration {.unnumbered}

An instructor may demonstrate celery dye movement or potometer data collection if local safety rules and materials allow. This is not required for the lab; the default investigation uses printed diagrams and datasets.

## Safety and Ethics Notes {.unnumbered}

No wet materials are required. If an optional demonstration is used, handle blades, glassware, and food dye primarily under instructor supervision. When discussing agricultural water use, consider the needs of different stakeholders.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarizing the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_VIII_plant_structure_and_water} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VIII_plant_structure_and_water} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `docs/manuscript/glossary.md`.
- Explore the Python code in `src/biology/botany/botany.py` for plant water relations calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
