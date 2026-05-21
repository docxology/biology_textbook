<!-- render:skip-beamer -->

# Lab 10 — Photosynthesis {.unnumbered}

\label{sec:lab_unit_III_photosynthesis}

*This activity accompanies \cref{sec:unit_III_photosynthesis} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and analyse an experiment to quantify photosynthesis rates using a simulated leaf-disc dataset
- Formulate testable hypotheses about how light wavelength and intensity affect photosynthesis
- Identify independent, dependent, and controlled variables in experimental designs
- Analyze experimental data using basic statistical methods and data visualization
- Write a brief scientific report with hypothesis, methods, results, and conclusion


<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Photosynthesis.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on the absorption spectra of chlorophyll a and b, predict which color of light (red, blue, green, or clear) will result in the fastest photosynthesis rate. Write a clear, testable hypothesis statement.

2. **Experimental Design**: What is the independent variable in this experiment? What is the dependent variable? List at least 5 variables that should be controlled to ensure a fair test.

3. **Scientific Context**: The Ruben & Kamen (1941) experiment used $^{18}$O-labeled water to prove that oxygen released during photosynthesis comes from water, not carbon dioxide. Why was this experiment groundbreaking? How did it change our understanding of photosynthesis?

4. **Quantitative Reasoning**: Calculate the energy per photon for red light ($\lambda = 700$ nm) and blue light ($\lambda = 450$ nm). Which has more energy? How might this affect photosynthesis efficiency?

5. **Real-World Application**: Commercial greenhouses often use LED grow lights. Based on your knowledge of photosynthesis, what light spectrum would you recommend for maximizing plant growth? Consider both energy efficiency and photosynthetic efficiency.

## Background {.unnumbered}

Photosynthesis converts light energy to chemical energy: **6 CO₂ + 6 H₂O + light → C₆H₁₂O₆ + 6 O₂**. The light-dependent reactions in the thylakoid membrane split water (photolysis) and generate NADPH and ATP; the Calvin cycle in the stroma uses NADPH and ATP to fix CO₂ into G3P and ultimately glucose. A floating leaf-disc assay can estimate photosynthesis because O₂ accumulation increases buoyancy; here, an image-and-data packet provides the same ET₅₀ evidence without requiring plant material, bicarbonate solution, lamps, or cutting tools.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Simulated leaf-disc time-course dataset by light colour | 1 |
| Light-intensity and inverse-square worksheet | 1 |
| Chlorophyll absorption spectrum packet | 1 |
| Experimental-design card set: controls, variables, confounds | 1 |
| Calculator or optional Python REPL with this project installed | 1 |
| Spreadsheet software (Excel/Google Sheets) | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Experimental Design and Hypothesis Testing {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a clear hypothesis about how light color will affect photosynthesis rate. Example: "If photosynthesis is driven by chlorophyll absorption, then red light will result in a faster photosynthesis rate (lower ET₅₀) than green light because chlorophyll absorbs red wavelengths more efficiently."

2. **Identify Variables**:
   - Independent variable: Light color (red, blue, green, clear)
   - Dependent variable: ET₅₀ (time for 50% of discs to float)
   - Controlled variables: Temperature, CO₂ proxy concentration, disc size in the model, initial disc status, light-source distance, etc.

3. **Set Up Controls**: Why is it important to have a clear filter (white light) control? What other controls could you include?

4. **Audit the Simulated Assay**: Use the method card to check whether disc size, starting status, CO₂ availability, temperature, and light distance are controlled across most conditions.

5. **Data Collection**: 
   - Read the number of floating discs at 1-minute intervals for 20 minutes from the dataset
   - Use the three provided replicate runs for each condition
   - Calculate ET₅₀ for each replicate using linear interpolation or the formula: ET₅₀ = (t₂ - t₁) × (5 - n₁) / (n₂ - n₁) + t₁

### Part 2: Computational Biology Exercise - Data Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Compare your light-response table with the project photosynthesis model.

```python
from biology.botany import photosynthesis_rate, light_response_curve

for light in (0, 100, 500, 1000):
    rate = photosynthesis_rate(light, max_rate_µmol_CO2_m2_s=22.0)
    print(light, round(rate, 2))

curve = light_response_curve(n_points=5)
print("first/last model points:", curve[0], curve[-1])
```
### Part 3: Light Intensity and Inverse-Square Law {.unnumbered}

6. **Intensity Experiment**: Use the provided white-light dataset at three distances: 10 cm, 20 cm, and 40 cm. Record ET₅₀ at each distance.

7. **Data Analysis**: Plot ET₅₀ against 1/d² (relative intensity). Is the relationship linear? The linearity should hold primarily up to light saturation; beyond that, rate is limited by Calvin-cycle throughput, not light.

8. **Calculate Photon Flux**: If a point light source emits 1500 μmol photons/m²/s at 20 cm, what is the photon flux at 10 cm and 40 cm? (Assume inverse-square law applies to point sources.)

### Part 4: CAM vs C3 Comparison (Extended Investigation) {.unnumbered}

8. **Design an Alternative Experiment**: Design a paper protocol to compare photosynthesis rates between a C3 plant model and a CAM plant model. Consider how CAM plants fix CO₂ at night and release it during the day. What simulated measurements would you request? How would you control variables?

9. **Hypothesis**: Predict what you would observe if you measured O₂ production or CO₂ uptake in light vs dark for both plant types.

## Data Recording {.unnumbered}

| Time (min) | Clear (white) | Red filter | Blue filter | Green filter |
| ---------- | ------------- | ---------- | ----------- | ------------ |
| 0 | 0/10 | 0/10 | 0/10 | 0/10 |
| 2 | | | | |
| 4 | | | | |
| 6 | | | | |
| 8 | | | | |
| 10 | | | | |
| 15 | | | | |
| 20 | | | | |

ET₅₀ (time for 5 discs to float): Clear __ Red __ Blue __ Green __

Light intensity experiment:
| Distance (cm) | Relative Intensity (1/d²) | ET₅₀ |
| ------------- | ------------------------- | ---- |
| 10 | 1.00 | |
| 20 | 0.25 | |
| 40 | 0.0625 | |

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Measure or model photosynthetic rate under changing light or carbon conditions.
- **Data skill to practice:** Interpret light-response and carbon-fixation data.
- **BioSkills emphasis:** Quantitative reasoning, Modeling and simulation.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Photosynthesis** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in a photosynthesis dataset, name the limiting factor — ask whether a rate change reflects light, CO₂ supply/stomata, or RuBisCO/photorespiration, and test whether a leaf- or chloroplast-scale gain would survive whole-plant water and sink limits. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

## Analysis Questions {.unnumbered}

1. Which wavelength produced the fastest disc floating (lowest ET₅₀)? Which produced the slowest? How does this correlate with the absorption spectrum of chlorophyll a and b? Was your hypothesis supported?

2. Why were discs first made to sink? What gas was removed during vacuum infiltration, and why does replacing it with CO₂-solution cause sinking?

3. As light intensity increases, photosynthesis rate increases to a plateau (light saturation point). Identify the limiting factor at each side of this curve and explain at the biochemical level.

4. The Calvin cycle does not directly require light. Why would removing light quickly halt the Calvin cycle reactions? (Hint: consider the fate of NADPH and ATP between the two stages.)

5. A crop scientist wants to maximise yield using artificial grow lights. Using your results, recommend the optimal light wavelength(s) and explain. What other environmental factors (CO₂, temperature, water) should she simultaneously optimise, and what law of limiting factors applies?

## Extension Analysis Questions {.unnumbered}

6. Rising atmospheric CO₂ (from ~280 ppm pre-industrial to >420 ppm today) is predicted to increase C3 photosynthesis more than C4. Explain why, using your understanding of RuBisCO's oxygenation reaction (photorespiration) and the CO₂-concentrating mechanism in C4 plants.

7. Plants grown under monochromatic green light develop abnormally (etiolated). Given that green light is weakly absorbed by chlorophyll, explain why green leaves appear green and why gardeners with LED grow lights generally select red + blue mixtures rather than "full-spectrum" (which wastes energy in the green).

8. The **Hill reaction** (Robin Hill, 1939) demonstrated that isolated chloroplasts can reduce artificial electron acceptors (e.g., DCPIP) in light, without CO₂ fixation. Describe what this result proved about the separability of the light and dark reactions — and why it was historically transformative for photosynthesis research.

9. **Statistical Analysis**: Calculate the standard error of the mean (SEM) for each light condition. Construct 95% confidence intervals. Are the differences between light conditions statistically significant based on your ANOVA?

10. **Experimental Error Analysis**: What are three potential sources of error in this experiment? How could you modify the procedure to reduce each source of error?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Data Study to Test the Effect of Temperature on Photosynthesis**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How does temperature affect the rate of photosynthesis?
- What enzymes are involved? What is the optimal temperature range for these enzymes?
- Write a detailed paper protocol to test temperature effects using provided ET₅₀ datasets or simulation cards

**Session 2**: Data Collection
- Analyse the provided ET₅₀ data at different temperatures
- Include proper controls and replicates

**Session 3**: Data Analysis and Presentation
- Analyze your data using statistical methods
- Create a scientific poster or presentation
- Compare your results to the Q₁₀ rule for temperature effects on biochemical reactions

## Real-World Problem Solving: Climate Change and Photosynthesis {.unnumbered}

**Case Study: Rising CO₂ and Plant Productivity**

Very high-emissions scenarios can push atmospheric CO₂ toward roughly 800-1000 ppm by 2100, while lower-emissions pathways remain far below that range \citep{ipcc2021ar6wg1}. While C3 plants may benefit from CO₂ fertilization under controlled conditions, temperature, water availability, nutrient limitation, ozone exposure, pests, and sink demand often constrain the effect in real ecosystems and farms.

1. **Research Task**: Investigate the concept of CO₂ fertilization. Which plant types (C3 vs C4) benefit more? What are the limitations of this effect in natural ecosystems?

2. **Ethical Consideration**: Should we rely on enhanced plant growth to offset carbon emissions? What are the potential ecological consequences of artificially increasing CO₂ levels in forests or agricultural systems?

3. **Policy Proposal**: Design a policy that balances the need for carbon sequestration through plant growth with the preservation of biodiversity and ecosystem function.

## Optional Wet-Lab Extension {.unnumbered}

An instructor may run a floating leaf-disc demonstration with approved materials, but the required lab uses the simulated dataset and design audit. Optional work should be framed as validating the paper model.

## Safety and Ethics Notes {.unnumbered}

Paper-based lab — no plant material, cutting tools, bicarbonate solution, cups, hot lamps, or wet materials are required. Optional demonstrations require instructor supervision, eye-comfort precautions around bright lights, and ordinary tool safety.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_III_photosynthesis} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_III_photosynthesis} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/biochemistry/biochemistry.py` for photosynthesis-related calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
