# Lab — Plant Reproduction and Development {.unnumbered}

\label{sec:lab_unit_VIII_plant_reproduction}

*This activity accompanies \cref{sec:unit_VIII_plant_reproduction} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design a paper-based pollination investigation using anatomical diagrams and pollen-tube datasets
- Formulate testable hypotheses about how environmental factors affect pollen germination data
- Identify independent, dependent, and controlled variables in plant reproduction experiments
- Analyze experimental data using growth rate calculations and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Plant Reproduction and Development.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Describe double fertilization in angiosperms — what are the two fertilization events and what does each produce?
2. Distinguish monocot from dicot seeds based on cotyledon number and seed anatomy.
3. Name three mechanisms of seed dispersal and identify the plant structure or adaptation that facilitates each.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of pollen germination, predict how temperature might affect pollen tube growth rate. Write a clear, testable hypothesis.

2. **Experimental Design**: What is the independent variable in a pollen germination experiment? What is the dependent variable? List at least 5 variables that should be controlled to ensure valid results.

3. **Scientific Context**: Double fertilization is a key innovation in angiosperms. Why is double fertilization advantageous compared to single fertilization in gymnosperms? What evolutionary pressures might have selected for this trait?

4. **Quantitative Reasoning**: If pollen tubes grow at an average rate of 1 mm/hour, how long would it take for a pollen tube to reach an ovule 5 cm away from the stigma? Show your calculation.

5. **Real-World Application**: Climate change is affecting plant reproduction. How might rising temperatures impact pollen viability and fertilization success? What are the implications for crop production?

## Lab Context: Plant Reproduction and Development {.unnumbered}

Angiosperms (flowering plants) undergo **double fertilisation**: one sperm nucleus (n) fuses with the egg (n) to form the zygote (2n); a second sperm fuses with the two polar nuclei (2×n = 2n) to form the primary endosperm nucleus (3n), which nourishes the developing embryo. Pollen grains (male gametophytes, n) germinate on the stigma and grow a pollen tube through the style to deliver sperm to the embryo sac (female gametophyte) in the ovule.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Source-governance card for Plant Reproduction and Development: plant evidence source card: tissue, driver, field context, breeding/adoption boundary, and refresh trigger | 1 |
| Flower anatomy diagram packet with labelled and unlabelled angiosperm structures | 1 |
| Pollination and dispersal syndrome card set (wind, managed honeybee, bumblebee, solitary bee, moth, bird, generalized flowers, and elaiosome-bearing seeds for myrmecochory) | 1 set |
| Pollen-tube growth dataset across temperature and sucrose treatments | 1 |
| Printed micrograph panels or schematic pollen-tube images with scale bars | 1 set |
| Double-fertilisation ploidy worksheet | 1 |
| Climate-risk case packet for crop flowering, heat stress, and pollinator service data | 1 |
| Graph paper or spreadsheet template | 1 |
| Calculator or optional Python REPL with this project installed | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Flower Anatomy and Pollination Strategy Cards {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how flower morphology relates to pollination strategy.

2. **Identify Variables**:
   - Independent variable: Pollination syndrome (wind vs insect)
   - Dependent variable: Flower morphological traits (petal colour, fragrance, pollen size, stigma surface)
   - Controlled variables: Plant species, growing conditions, measurement methods, etc.

3. **Set Up Controls**: Why is it important for each pollination-syndrome card to include both a labelled reference image and a blinded comparison image? What other controls could you include to ensure accurate comparisons?

4. **Data Collection**:
   - Identify external parts on the printed diagram: sepals, petals, stamens (anther + filament), pistil (stigma + style + ovary).
   - Use the ovary cross-section diagram to locate ovules and trace the path a pollen tube would follow.
   - Use micrograph panels or schematic cards to record pollen characteristics such as size, surface texture, and tube length.
   - Compare wind-pollinated, bee-pollinated, and ant-dispersed cards. Fill in the comparison table and cite the trait evidence behind each classification.

### Part 2: Computational Biology Exercise — Pollen Tube Growth Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Use a growth curve as a quantitative analogue for pollen-tube extension.

```python
from biology.botany import plant_biomass_growth

growth = plant_biomass_growth(
    initial_biomass_g=0.2,
    relative_growth_rate=0.35,
    carrying_capacity_g=10.0,
    duration_days=10,
)
print("initial biomass:", growth.biomass_g[0])
print("final biomass:", round(growth.biomass_g[-1], 2))
print("days recorded:", len(growth.times_days))
```
### Part 3: Pollen Germination Dataset {.unnumbered}

5. **Design an Alternative Dataset**: Instead of just measuring pollen tube growth at different temperatures, design a dataset to test how sugar concentration affects pollen tube growth. What hypothesis would you test? What sugar concentrations would you include, and what treatment would serve as the baseline?

6. **Hypothesis**: Predict the relationship between sucrose concentration and pollen tube growth rate. Would you expect a linear increase, a saturating curve, or something else? Why?

7. **Reproducibility Check**: For the printed pollen-tube dataset, calculate mean growth rate and standard deviation for each treatment. Decide whether the temperature effect is larger than within-treatment variation.

## Data Recording {.unnumbered}

Flower anatomy diagram (label most structures):

`[Annotate the printed flower diagram here]`

| Structure | Present? | Description (colour, size, texture) |
| --------- | -------- | ------------------------------------- |
| Sepals | | |
| Petals | | |
| Anthers | | |
| Stigma | | |
| Style | | |
| Ovary | | |
| Ovules | | |

| Time (min) | Pollen tube length (µm) | Pollen tube growth rate (µm/min) |
| ---------- | ----------------------- | --------------------------------- |
| 0 | 0 | — |
| 30 | | |
| 60 | | |
| 90 | | |
| 120 | | |

| Character | Wind-pollinated (grass) | Bee-pollinated (lily or orchard flower) | Ant-dispersed seed |
| --------- | ----------------------- | ------------------------- | ------------------ |
| Petal colour | | |
| Fragrance | | |
| Pollen size | | |
| Pollen surface | | |
| Stigma surface | | |
| Dispersal reward or cue | | | |

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Compare reproductive structures and developmental outcomes.
- **Data skill to practice:** Track ploidy, tissue origin, and reproductive stage from diagrams or observations.
- **BioSkills emphasis:** Interdisciplinary nature of science, Process of science.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Plant Reproduction and Development** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Field translation | Note whether the evidence comes from a diagram, growth chamber, greenhouse, field plot, or long-term observation, and state what changes when the scale changes. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this reproduction lab, tie every classification to the reproductive structure or stage it depends on (sporophyte versus gametophyte, pollen versus ovule, self- versus cross-pollination) and state the pollination, development, or dispersal mechanism that links genotype to the observed trait. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Reproductive Success and Seed Survival {.unnumbered}

**Problem:** A flowering plant produces 500 seeds per reproductive season. Germination rate is 6%. Of germinated seeds, 20% survive to reproductive age. The plant lives for 15 reproductive seasons. (a) Calculate seeds germinating per season, (b) seedlings surviving to reproduction per season, and (c) total reproductive offspring produced over the plant's lifetime.

**Solution:** (a) 500 × 0.06 = 30 germinating seeds/season. (b) 30 × 0.20 = 6 surviving to reproduction per season. (c) 6 × 15 = 90 reproductive offspring over the plant's lifetime.

**Interpretation:** For a stable population (neither growing nor declining), each individual must on average produce exactly one surviving replacement over its lifetime. With 90 potential offspring over 15 seasons, this plant has high fecundity — but most offspring are lost at the germination and early establishment stages, consistent with a Type III survivorship curve.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Plant Reproduction and Development before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. Pollen tube growth is driven by cytoplasmic streaming and tip-directed vesicle fusion. What is the role of Ca²⁺ ions (specifically the tip-focused Ca²⁺ gradient) in regulating pollen tube polarity and growth direction?

2. Describe double fertilisation: where does each sperm go, what does each produce, and what are the ploidy levels of the zygote and endosperm?

3. A honeybee, a bumblebee, and a solitary bee visit different fragrant, brightly coloured flowers with sticky pollen. A grass flower has no petals, no fragrance, and produces vast quantities of dry pollen. A woodland herb produces an elaiosome-bearing seed that ants carry to the nest. Explain the evolutionary logic behind each strategy using cost-benefit trade-offs, and state why "bee pollination" is still too broad unless the visitor actually transfers pollen.

4. Self-incompatibility (SI) systems prevent self-fertilisation in many plant species. The S-RNase system in *Petunia* involves the pistil secreting an RNase that degrades pollen tube RNA if the pollen S-allele matches the pistil S-allele. How does this mechanism selectively destroy "self" pollen without harming "foreign" pollen?

5. Seedless watermelons are triploid (3n). Explain the steps used to produce them (starting from a colchicine treatment of diploid cells), and why triploid plants are sterile — using the concept of homologous chromosome pairing during meiosis.

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: If the pollen germination dataset includes three replicates per treatment, how would you analyze variation in growth rates? What statistical test would you use to determine if differences between temperatures are significant?

7. **Experimental Error Analysis**: What are three potential sources of error in pollen tube growth measurements? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you wanted to test the effect of a specific hormone (e.g., auxin) on pollen tube growth using archived image measurements, what concentrations would you test, how would the images be blinded, and how would you measure the effect?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Study of Plant Reproductive Strategies**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How do flower traits correlate with pollination syndrome, and how do seed rewards correlate with ant-mediated dispersal?
- Formulate a hypothesis about the relationship between specific traits (e.g., petal colour, nectar production, floral tube depth, elaiosome presence) and pollinator or disperser type
- Design a study comparing multiple plant species

**Session 2**: Data Extraction and Analysis
- Extract flower morphology data from species cards, image databases, or published datasets
- Score pollinator visits from provided video stills or summarized observation tables, separating managed honeybees from wild bees when the evidence allows it
- Analyze correlations between traits and pollinator type; add a myrmecochory extension that compares seed-removal rates for elaiosome-present vs elaiosome-removed cards

**Session 3**: Data Interpretation and Presentation
- Perform statistical analysis (e.g., principal component analysis)
- Discuss the evolutionary implications of your findings
- Create a scientific poster or presentation

## Real-World Problem Solving: Plant Reproduction and Agriculture {.unnumbered}

**Case Study: Pollinator Decline**

1. **Research Task**: Investigate the causes and consequences of pollinator decline (bees, butterflies, etc.). What crop groups depend on animal pollination, and how do dependence estimates differ between staple calories, fruits, nuts, and specialty crops? Separate managed honeybee service from wild-bee service when evidence permits that distinction.

2. **Field-Translation Consideration**: A warming treatment advances flowering in a chamber experiment, but a field dataset shows variable pollinator emergence. What evidence would let you decide whether the crop faces pollen heat failure, pollinator mismatch, or both?

3. **Policy Proposal**: Design a policy to protect pollinator populations while supporting agricultural productivity. Consider: incentives for habitat restoration, pesticide timing, heat-wave monitoring during flowering, seed-set surveillance, nesting substrate for wild bees, and edge-habitat management that does not increase invasive-ant disruption of native seed dispersal.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Two related plant species occupy the same environment. Species A produces 2,000 small seeds (0.1 mg each), while Species B produces 50 large seeds (40 mg each). Germination rate for A is 3%; for B is 65%.
>
> (a) Calculate the number of germinating seeds per season for each species and compare their reproductive strategies.
> (b) In a nutrient-poor environment with sparse canopy, predict which species would have higher seedling survival rates and explain using seed reserve reasoning.
> (c) Evaluate the evolutionary trade-off between seed number and seed size in terms of r-selected versus K-selected life history strategies.

## Optional Wet-Lab Demonstration {.unnumbered}

An instructor may demonstrate flower dissection or pollen germination with appropriate allergy precautions and approved materials. This is not required; the default lab uses diagrams, cards, and archived pollen-tube measurements.

## Safety and Ethics Notes {.unnumbered}

No wet materials are required. Pollen can be an allergen in optional demonstrations, and colchicine is discussed conceptually primarily. When discussing pollinator decline, consider the impacts on both ecosystems and human food security.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_VIII_plant_reproduction} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VIII_plant_reproduction} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/botany/botany.py` for plant reproduction calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
