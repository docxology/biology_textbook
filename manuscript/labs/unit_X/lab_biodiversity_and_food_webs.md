# Lab — Biodiversity and Food Webs {#sec:lab_unit_X_biodiversity_and_food_webs .unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Biodiversity and Food Webs.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->

*This activity accompanies \cref{sec:unit_X_biodiversity_and_food_webs} of the textbook — review that chapter before attempting the exercises below.*

## Lab Context: Biodiversity and Food Webs {.unnumbered}

This extension lab applies island biogeography, food-web structure, and biodiversity indices to printed ecological datasets and conservation scenarios.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Biodiversity and Food Webs: conservation-assessment source card: index versus census, assessment version, value judgment, and monitoring trigger | 1 |
| Printed datasets, cards, and worksheets referenced below | 1 set per group |
| Graph paper or plain paper for diagrams | 1 |
| Calculator | 1 |

## Paper-Based Investigation {.unnumbered}

4. From the food web diagram: identify most producers, primary consumers, secondary consumers, and apex predators. List most possible food chains containing 4 links.
5. If a producer level has 10,000 kJ available, calculate the energy at each trophic level assuming 10% efficiency. Calculate how many humans (apex predators) can be supported vs if they ate at the primary consumer level.

**Part C — Keystone Predator Analysis**

6. Read the starfish removal experiment data (Paine, 1966, summarized): count species richness before and after sea star (*Pisaster*) removal from an intertidal zone. Explain how removing one species reduced diversity.

**Part D — Succession Mapping**

7. For each chronosequence or remote-sensing card: record dominant vegetation type, estimated time since disturbance, key abiotic factors, and one ecosystem service expected to change during succession.

## Data Recording {.unnumbered}

Species competition (from dataset):

: Alignment and Rubric Map: Day and N₁ (monoculture). {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map_2}
| Day | N₁ (monoculture) | N₁ (mixed) | N₂ (monoculture) | N₂ (mixed) |
| --- | ---------------- | ----------- | ---------------- | ----------- |
| 0 | | | | |
| 4 | | | | |
| 8 | | | | |
| 14 | | | | |

Food web energy pyramid:

: Alignment and Rubric Map: Trophic level and Energy (kJ). {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map_3}
| Trophic level | Energy (kJ) | # Humans supported |
| ------------- | ----------- | ------------------- |
| Producers | 10,000 | — |
| Primary consumers | | |
| Secondary consumers | | |
| Apex predators | | |

Species richness before sea star removal: ___; After: ___

Ecosystem-service tradeoff most improved by succession: ___; tradeoff most reduced by disturbance: ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Compare diversity and network scenarios under area or disturbance change.
- **Data skill to practice:** Interpret food-web, richness, or biogeography datasets.
- **BioSkills emphasis:** Modeling and simulation, Science and society, Communication and collaboration.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Community Ecology and Species Interactions** with a reproducibility pass:

: Alignment and Rubric Map: Evidence check and Student action. {#tbl:unit_X_biodiversity_and_food_webs_alignment_and_rubric_map_4}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: for this community-interaction lab, label every link in the printed network by interaction type (competition, predation, mutualism) and by whether it was observed directly or inferred from co-occurrence, and state how the sampling effort and disturbance history could bias which interactions appear. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Shannon Diversity and Evenness in Two Communities {.unnumbered}

**Problem:** Two communities each contain four species. Community A has 25, 25, 25, 25 individuals across the four species. Community B has 70, 15, 10, 5 individuals. Calculate Shannon diversity H' = −Σ(pᵢ ln pᵢ) for each community, then compute evenness J = H'/H_max with H_max = ln S, where S is the number of species. Which community is more diverse, and which is more even?

**Solution:** For Community A, each proportion pᵢ = 0.25, so −pᵢ ln pᵢ = −0.25 × ln(0.25) = −0.25 × (−1.386) ≈ 0.347. Summing across four species gives H'_A ≈ 4 × 0.347 ≈ 1.386, which equals ln 4 exactly (H_max for S = 4). So J_A = 1.386 / 1.386 = 1.0. For Community B, proportions are 0.70, 0.15, 0.10, 0.05. The corresponding −pᵢ ln pᵢ terms are about 0.250, 0.285, 0.230, 0.150; summing gives H'_B ≈ 0.915. Evenness J_B = 0.915 / 1.386 ≈ 0.66.

**Interpretation:** Community A is at the theoretical maximum diversity for four species (every species equally common), so its evenness is 1.0. Community B has the same richness but is dominated by one species; its diversity drops to about 0.92 and its evenness falls to 0.66. The example shows that Shannon H' combines richness and evenness into a single index — a strongly dominant species can lower H' substantially even when S is held constant.

## Analysis Questions {.unnumbered}

1. In the Lotka-Volterra framework, stable coexistence requires α₁₂ < K₁/K₂ and α₂₁ < K₂/K₁. What do these inequalities mean biologically in terms of intra- vs interspecific competition strength?
2. The pyramid of energy shows that far more humans can be supported by eating at lower trophic levels. Calculate the maximum number of humans at each trophic level from your energy data. What are three reasons why human food systems often involve higher trophic level consumption?
3. When *Pisaster* (sea star) was removed, mussel populations exploded and crowded out other species, reducing diversity. Define keystone species and explain why removing an apex predator can reduce community diversity (trophic cascade).
4. Primary succession begins on bare rock (no soil) while secondary succession follows disturbance on existing soil. Explain how pioneer species (lichens, mosses) facilitate succession on bare rock — which physical and chemical properties of soil do they create? Name Connell and Slatyer's facilitation model.
5. A student claims "climax forests are the most stable and should generally be our conservation goal." Critique this statement using the concept of intermediate disturbance hypothesis (Connell 1978) and give an example of an ecosystem that requires periodic disturbance to maintain high diversity.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** The removal of gray wolves from Yellowstone National Park has been linked to a trophic cascade that reshaped riparian plant communities and stream morphology, and their reintroduction is associated with partial recovery of those systems.
>
> (a) Trace the cascade from predator removal to plant community change: identify the immediate prey-population response, the resulting change in herbivory pressure on willows and aspens, and the downstream consequence for riparian vegetation. Distinguish direct effects (predator on prey) from indirect effects (predator on plants via herbivory).
> (b) Predict at least one effect on soil stability or stream geomorphology that would plausibly follow from the vegetation change in part (a). Identify one observational measurement that ecologists could use to test whether your predicted effect is operating, and one alternative explanation (for example, climate or hydrological change) that the measurement would need to discriminate against.

## Safety and Ethics Notes {.unnumbered}

No live organisms or ecological specimens are required. Optional living-culture demonstrations should be instructor managed, disposed of without release to waterways, and treated as enrichment rather than required evidence.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Biodiversity and Food Webs before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group
comparing results and discussing the following prompts. Each member should
contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to
   the textbook's predictions. Where they diverge, suggest at least one
   mechanistic explanation before concluding "experimental error."
2. **What would change the outcome** — propose one modification to the
   procedure that would sharpen the measurement or extend the result to a
   new biological context, and predict what you would observe.
3. **One-sentence headline** — each student composes a single sentence
   summarizing the lab's take-home message, suitable for a tweet. Compare
   sentences across groups; good headlines are short, quantitative, and
   mechanistic.
4. **Connection back to the textbook** — identify one section of
   \cref{sec:unit_X_biodiversity_and_food_webs} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_X_biodiversity_and_food_webs} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_X_biodiversity_and_food_webs}`; all numerical
quantities in this lab use SI units — see \nameref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
