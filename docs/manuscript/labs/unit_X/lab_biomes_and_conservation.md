# Lab — Biomes and Conservation Biology {#sec:lab_unit_X_biomes_and_conservation .unnumbered}


## Learning Objectives {.unnumbered}

*This activity accompanies \cref{sec:unit_X_biomes_and_conservation} of the textbook — review that chapter before attempting the exercises below.*

- Classify biomes from climate data (mean annual temperature, precipitation, Whittaker diagram)
- Calculate species-area relationship parameters and predict extinction risk from habitat loss
- Evaluate minimum viable population (MVP) and reserve design principles for a case species
- Apply IUCN Red List criteria to classify conservation status of a provided species profile


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Biomes and Conservation Biology.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. List two abiotic and two biotic factors that shape the geographic distribution of terrestrial biomes. For each factor, describe in one sentence how a change in that factor could shift a biome boundary on a continental map.
2. State the IUCN Red List criterion most commonly cited for the "Critically Endangered" category — for example, an observed or projected population reduction over the past or next three generations, or a very small or restricted population. Cite at least one quantitative threshold that the IUCN typically uses.
3. Define effective population size (Ne) in your own words, and explain in two sentences why Ne is often substantially smaller than the census population size N in wild populations.

## Lab Context: Biomes and Conservation Biology {.unnumbered}

Biomes are large-scale communities determined primarily by climate (temperature and precipitation). The species-area relationship **$S = cA^z$** (log-linear: log S = log c + z·log A) predicts that decreasing habitat area reduces species richness; the exponent z (typically 0.2–0.35 for oceanic islands) can be used to predict extinction rates from deforestation. Minimum viable population (MVP) analyses determine the population size needed for a defined probability of persistence over a defined time frame. IUCN Red List criteria assign species to categories (LC, NT, VU, EN, CR, EW, EX) based on population decline rates, geographic range, and quantitative extinction risk.

## Paper-Based Materials {.unnumbered}

: Alignment and Rubric Map: Item and Quantity. {#tbl:unit_X_biomes_and_conservation_alignment_and_rubric_map}
| Item | Quantity |
| ---- | -------- |
| Source-governance card for Biomes and Conservation Biology: conservation-assessment source card comparing GBIF occurrence records, IUCN category evidence, IPBES policy synthesis, assessment version, and monitoring trigger | 1 |
| GBIF occurrence-filter worksheet with coordinate uncertainty, date, basis of record, taxonomic backbone match, duplicate flag, and sampling-bias notes | 1 |
| Whittaker biome diagram (printed with temperature and precipitation axes) | 1 |
| Climate data cards (10 locations: MAT and MAP values) | 1 set |
| Species-area relationship dataset (6 habitat fragments: area and species count) | 1 |
| Log-log graph paper | 1 |
| IUCN criteria worksheet (table of criteria A–E) | 1 |
| Species profile card: fictional vaquita-like cetacean (population data, trend, range) | 1 |
| Reserve-design decision matrix with habitat area, corridor cost, carbon storage, and community co-benefits | 1 |
| Climate-shift scenario cards for biome boundaries and conservation priorities | 1 set |
| Coral bleaching degree-heating-week cards with recovery, mortality, and symbiont-shuffling scenarios | 1 set |
| IPBES/food-security tradeoff card: agroecology, yield, pollinator habitat, waste reduction, and equity indicators | 1 |
| Calculator | 1 |

## Paper-Based Investigation {.unnumbered}

**Part A — Biome Classification**

1. For each of 10 climate data cards (MAT in °C, MAP in mm), plot the location on the Whittaker diagram. Identify the biome for each location.

**Part B — Species-Area Relationship**

2. Plot log(S) vs log(A) for the 6 habitat fragments on log-log paper. Fit a line; calculate the slope (z exponent) and the y-intercept (log c).
3. Using $S = cA^z$, predict species richness in a fragment one-tenth the area of the largest.
4. If a deforestation event reduces a forest from 10,000 ha to 100 ha, predict the percentage of species lost using the same equation.

**Part C — MVP Analysis**

5. Given MVP data for the provided species: 50/500 rule (N_e > 50 for short-term genetic viability; N_e > 500 for long-term). Current population: 35 individuals. Is the population below the short-term MVP? Design a 10-year recovery plan with specific targets.

**Part D — IUCN Classification**

6. Apply IUCN criteria to the species profile (population decline 80% in 10 years; < 250 mature individuals; geographic range < 100 km²). Determine IUCN status.
7. Use the reserve-design matrix to compare a single large reserve, several small reserves, and a connected-corridor plan. Score each option for extinction risk, climate refugia, ecosystem services, and governance tradeoffs.

**Part E — Coral and Food-System Decision Cards**

8. Classify coral scenarios by degree-heating-week exposure, recovery interval, and local stressors. Decide whether the evidence supports likely recovery, repeated bleaching risk, or high mortality risk.
9. Use the symbiont-response cards to distinguish symbiont shuffling, assisted gene flow, selective breeding, and microbiome conditioning. State one benefit, one tradeoff, and one missing validation step for each.
10. Use the IPBES/food-security card to compare two conservation plans: one maximizing protected area alone and one combining habitat protection with agroecological transition, pollinator corridors, and food-waste reduction. Score biodiversity, nutrition, equity, and feasibility separately.

## Data Recording {.unnumbered}

Biome classifications:

: Alignment and Rubric Map: Location and MAT (°C). {#tbl:unit_X_biomes_and_conservation_alignment_and_rubric_map_2}
| Location | MAT (°C) | MAP (mm) | Biome |
| -------- | --------- | --------- | ----- |
| 1 | 28 | 2,400 | |
| 2 | −5 | 300 | |
| 3 | 15 | 600 | |
| 4 | 22 | 100 | |
| 5 | 0 | 50 | |

(continue for 10 locations)

Species-area relationship:
z = ___; c = ___; predicted S at 1/10 area = ___; % species lost = ___%

MVP assessment: current N = 35; MVP_short = 50; MVP_long = 500
Status: BELOW/ABOVE short-term MVP; IUCN status: ___

Reserve-design score: extinction risk = ___; climate refugia = ___; ecosystem services = ___; governance risk = ___
Coral risk class: _______; assisted-evolution option: _______; food-system tradeoff score: biodiversity ___ / nutrition ___ / equity ___ / feasibility ___

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Compare biome patterns and conservation tradeoffs.
- **Data skill to practice:** Use maps, trend data, and threat categories to justify conservation priorities.
- **BioSkills emphasis:** Modeling and simulation, Science and society, Communication and collaboration.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Biomes and Conservation Biology** with a reproducibility pass:

: Alignment and Rubric Map: Evidence check and Student action. {#tbl:unit_X_biomes_and_conservation_alignment_and_rubric_map_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: for this conservation lab, separate the ecological signal in the printed dataset (a biodiversity index, range map, or protected-area comparison) from the value judgement and the feasibility constraint, and name explicitly which counterfactual or unprotected reference the decision is being measured against. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Heterozygosity Loss in a Small Tiger Population {.unnumbered}

**Problem:** A population viability analysis (PVA) for a wild population of 85 tigers projects a 15% extinction risk over the next 100 years under a slow decline (r ≈ −0.01/yr). Using the rule of thumb Ne ≈ N/3 for a structured wild population, calculate the effective population size. Then estimate the expected heterozygosity retained after 10 generations using H_t = H_0 × (1 − 1/(2Ne))^t, with H_0 = 0.45.

**Solution:** Effective population size: Ne ≈ 85 / 3 ≈ 28. Per-generation retention factor: (1 − 1/(2 × 28)) = (1 − 1/56) ≈ 0.9821. After 10 generations: H_10 = 0.45 × (0.9821)^10 ≈ 0.45 × 0.836 ≈ 0.376. So expected heterozygosity drops from 0.45 to roughly 0.38 — about a 16% relative loss in 10 generations under drift alone.

**Interpretation:** Genetic drift erodes heterozygosity faster in small populations because each generation loses a fraction 1/(2Ne) of the variation in expectation. With Ne ≈ 28, even a decade of generations is enough to make inbreeding depression and reduced adaptive capacity plausible concerns. Conservation actions that raise effective size — corridors, translocations, genetic rescue — can slow this loss substantially.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Biomes and Conservation Biology before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Analysis Questions {.unnumbered}

1. Two locations had the same MAT but very different biomes because of different MAP values. What does this demonstrate about the relative importance of temperature vs precipitation in biome determination? Name an example pair from the Whittaker diagram where this contrast is striking.
2. Your log-log plot of the species-area relationship should be linear. What does the slope (z) represent ecologically? Why do oceanic islands have higher z values (~0.35) than mainland habitat patches (~0.12)?
3. Predicted species loss from deforestation assumes equilibrium. Explain the concept of "extinction debt" — why the full extinction toll of habitat reduction is primarily realized decades after the habitat loss, and what this implies for urgency in conservation action.
4. The 50/500 rule gives threshold population sizes for genetic viability. Explain: (a) why populations below N_e = 50 suffer inbreeding depression; (b) why populations below N_e = 500 lose the variation needed to adapt to future environmental change. What is the difference between census population size (N_c) and effective population size (N_e)?
5. Design a conservation reserve for a large mammal (e.g., tiger, Amur leopard) with a home range of 200 km² that requires a minimum viable population of 100 individuals. Calculate the minimum reserve area, explain whether a single large reserve (SLOSS debate: Single Large or Several Small) is preferable in this case, and identify two human activities outside the reserve boundary that would most threaten population persistence.
6. A reef has high DHW exposure but a recovery window long enough for partial symbiont reshuffling, while a nearby watershed continues to deliver nutrient pollution. Which intervention should be treated as climate adaptation, which as local-stressor reduction, and why would assisted evolution alone be insufficient?
7. A food-security policy increases short-term yield by removing hedgerows and reducing crop diversity. Use the IPBES/food-system tradeoff card to evaluate why yield, pollination, soil stability, nutrition, and equity must be scored separately rather than collapsed into one "more food" metric.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A regional conservation board can fund one of two options for a fragmented forest landscape: (i) a wildlife corridor connecting two isolated forest fragments of about 200 individuals each, or (ii) a captive-breeding program drawing from one of the fragments.
>
> (a) Using minimum viable population theory and what you know about effective population size, evaluate how each option would influence Ne, gene flow, and the rate of heterozygosity loss across the next several generations. Identify which option is more likely to produce a measurable change in genetic diversity within ten years.
> (b) Identify one specific risk associated with each option — for example, disease transmission through the corridor or behavioral deficits in captive-bred releases — and propose one monitoring metric that would let the team detect that risk early enough to adjust the strategy.

## Safety and Ethics Notes {.unnumbered}

No hazardous materials. Conservation discussions involving indigenous land rights and protected area design should be approached with cultural sensitivity and recognition of land sovereignty principles. IUCN assessments require reliable species data — discuss uncertainty and the precautionary principle.

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
   \cref{sec:unit_X_biomes_and_conservation} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_X_biomes_and_conservation} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `#gl:term-slug` link in the text) — its master
  definition is in `docs/manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\cref{sec:unit_X_biomes_and_conservation}`; all numerical
quantities in this lab use SI units — see \nameref{sec:appendix_units_and_constants} for
unit conversions and biological-scale reference values.*
