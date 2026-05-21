# Lab 11 — Metabolic Integration and Regulation {.unnumbered}

\label{sec:lab_unit_III_metabolic_integration}

*This activity accompanies \cref{sec:unit_III_metabolic_integration} of the textbook — review that chapter before attempting the exercises below.*

## Learning Objectives {.unnumbered}

- Design and execute a glucose tolerance test (GTT) simulation to analyze metabolic regulation
- Formulate testable hypotheses about how insulin and glucagon regulate blood glucose
- Identify independent, dependent, and controlled variables in metabolic experiments
- Analyze experimental data using area under the curve (AUC) and statistical methods
- Write a brief scientific report with hypothesis, methods, results, and conclusion



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Metabolic Integration and Regulation.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Describe in one paragraph how insulin promotes glycogen synthesis in the liver, naming at least two enzymes whose activity changes and the direction of each change.
2. Explain what AMPK senses at the molecular level and identify two downstream pathways AMPK activates and one it suppresses when cellular energy charge is low.
3. A healthy person eats a high-carbohydrate meal. Predict the qualitative time course of insulin, glucagon, blood glucose, and hepatic glycogen content over the four hours that follow, and sketch the expected order in which each crosses its peak.

## Pre-Lab Inquiry Questions {.unnumbered}

*Complete these questions before coming to lab. Use your textbook and additional research to inform your hypotheses.*

1. **Hypothesis Formation**: Based on your understanding of insulin and glucagon, predict how a healthy individual's blood glucose would respond to a glucose challenge compared to a type 2 diabetic. Write a clear, testable hypothesis.

2. **Experimental Design**: What is the independent variable in a glucose tolerance test? What is the dependent variable? List at least 5 variables that should be controlled to ensure a fair test.

3. **Scientific Context**: The glucose tolerance test is a clinical diagnostic tool. Why is the area under the curve (AUC) an important metric? What does a larger AUC indicate about metabolic health?

4. **Quantitative Reasoning**: If a normal person's blood glucose peaks at 30 minutes and returns to baseline by 120 minutes, while a diabetic's peaks at 60 minutes and remains elevated at 120 minutes, what does this tell you about insulin secretion and sensitivity?

5. **Real-World Application**: Metformin is a first-line drug for type 2 diabetes. Based on your knowledge of metabolic regulation, how might metformin work? Consider its effects on AMP:ATP ratio and downstream targets.

## Background {.unnumbered}

Metabolic integration means that pathways (glycolysis, gluconeogenesis, β-oxidation, glycogen synthesis) are coordinated by hormonal signals and allosteric regulators, not running independently. Insulin (released postprandially) activates GLUT4 translocation, glycogen synthase, and fatty acid synthesis; it inhibits gluconeogenesis and lipolysis. Glucagon (released during fasting) does the reverse. PFK-1 is the key allosteric valve of glycolysis: activated by AMP, ADP, and fructose-2,6-bisphosphate; inhibited by ATP and citrate.

In this data-analysis lab you will interpret simulated glucose tolerance test data from three subjects (normal, pre-diabetic, type 2 diabetic) and model the allosteric regulation of PFK-1.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| GTT dataset (instructor-provided, printed or digital) | 1 per student |
| Graph paper or laptop with spreadsheet software | 1 |
| Calculator | 1 |
| PFK-1 activity vs [fructose-2,6-BP] graph (provided) | 1 |
| Coloured pencils (3 colours) | 1 set |
| Calculator or optional Python REPL with this project installed | 1 |
| Ruler | 1 |

## Paper-Based Investigation {.unnumbered}

### Part 1: Glucose Tolerance Test Analysis {.unnumbered}

1. **Formulate Your Hypothesis**: Based on your pre-lab research, write a hypothesis about how the GTT curves will differ between normal, pre-diabetic, and diabetic subjects.

2. **Identify Variables**:
   - Independent variable: Subject group (normal, pre-diabetic, type 2 diabetic)
   - Dependent variable: Blood glucose concentration (mM) over time
   - Controlled variables: Glucose dose, timing of measurements, subject age/fasting status, etc.

3. **Set Up Controls**: Why is it important to have a normal control group? What other controls could you include in a clinical GTT study?

4. **Data Analysis**: 
   - Plot blood glucose (mM) vs time (min, 0–120 min) for most three subjects on the same graph
   - Annotate key events: glucose ingestion (t = 0), peak blood glucose, return to baseline
   - Calculate AUC for each subject using the trapezoid rule at 30-minute intervals

### Part 2: Computational Biology Exercise - Statistical Analysis with Python {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Use the biochemical models to anchor the class discussion in measured quantities.

```python
from biology.biochemistry import atp_free_energy, glycolysis_summary, michaelis_menten

glycolysis = glycolysis_summary()
rate = michaelis_menten(substrate_conc=2.0, Vmax=10.0, Km=2.0)
atp = atp_free_energy()

print("net ATP:", glycolysis.net_atp)
print("half-saturation rate:", round(rate.reaction_rate, 2))
print("ATP hydrolysis ΔG:", round(atp, 2))
```
### Part 3: Allosteric Regulation Modeling {.unnumbered}

5. **Design an Alternative Data Study**: Instead of just analysing provided data, design a paper experiment to test how different concentrations of fructose-2,6-bisphosphate affect PFK-1 activity. What hypothesis would you test? What concentrations would you request in the dataset?

6. **Hypothesis**: Predict the shape of the dose-response curve. Would it be linear, sigmoidal, or something else? Why?

## Data Recording {.unnumbered}

| Time (min) | Subject A BG (mM) | Subject B BG (mM) | Subject C BG (mM) |
| ---------- | ----------------- | ----------------- | ----------------- |
| 0 | 4.5 | 5.7 | 7.0 |
| 30 | 6.8 | 9.2 | 12.4 |
| 60 | 5.9 | 8.5 | 13.1 |
| 90 | 5.1 | 7.3 | 11.8 |
| 120 | 4.6 | 6.4 | 10.5 |

AUC Subject A: _____ mM·min  
AUC Subject B: _____ mM·min  
AUC Subject C: _____ mM·min  

PFK-1 at 0 µM fructose-2,6-BP: _____; K₀.₅: _____; at 10 µM: _____

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Compare metabolic responses across nutrient and hormone conditions.
- **Data skill to practice:** Use pathway evidence to infer which metabolic state or tissue is active.
- **BioSkills emphasis:** Quantitative reasoning, Modeling and simulation.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Metabolic Integration and Regulation** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in an integrated-metabolism dataset, separate flux from pool size — ask whether isotope-tracer or rate evidence supports each directional claim, and pin every result to a fed/fasted state, tissue, and time window before generalizing. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: How Long Would Liver Glycogen Alone Last in a Fast? {.unnumbered}

**Problem:** Estimate, for a 70 kg adult at rest with a basal metabolic rate (BMR) of 1,500 kcal / day, how long liver glycogen stores alone would meet whole-body energy demand if no other fuel were used. Compare to the energy stored as adipose triglyceride. Use the following typical values: liver glycogen mass ≈ 100 g (energy density ≈ 4 kcal / g); adipose triglyceride mass ≈ 15 kg (energy density ≈ 9 kcal / g).

**Solution:**

Step 1 — Energy in liver glycogen:

- 100 g × 4 kcal / g = 400 kcal

Step 2 — Time supported at rest if glycogen were the sole fuel source:

- 400 kcal ÷ 1,500 kcal / day ≈ 0.27 day ≈ 6.4 hours

Step 3 — Energy in adipose triglyceride:

- 15 kg = 15,000 g; 15,000 g × 9 kcal / g = 135,000 kcal

Step 4 — Time supported at rest by fat stores:

- 135,000 kcal ÷ 1,500 kcal / day ≈ 90 days

Step 5 — Ratio: fat reserves contain roughly 135,000 / 400 ≈ 340 times more energy than liver glycogen.

**Interpretation:** Liver glycogen would support a small fraction of one day at rest. This is why a 24-hour fast forces the liver to switch substantially toward gluconeogenesis (using lactate, glycerol, glucogenic amino acids) and why adipose lipolysis and ketogenesis become quantitatively important within roughly a day of food deprivation. Tissue-specific glucose dependence (notably the brain, which uses about 20% of BMR and prefers glucose) is what compels the body to defend blood glucose by mobilising every substrate that can feed gluconeogenesis or ketogenesis once glycogen is depleted.


## Analysis Questions {.unnumbered}

1. Based on the GTT data, which AUC threshold might a clinician use to diagnose type 2 diabetes? How does the shape of Subject C's curve differ from Subject A's, and what does this indicate about β-cell insulin secretion capacity?

2. Subject B is pre-diabetic. Suggest two lifestyle interventions that would shift Subject B's GTT curve toward Subject A's profile. For each, identify the specific metabolic pathway or hormone axis restored.

3. In the post-meal state (high insulin), what happens to hepatic fructose-2,6-bisphosphate levels? Trace: insulin → PFK-2 phosphorylation state → [fructose-2,6-BP] → PFK-1 activity → glycolysis rate.

4. During intense exercise, AMP levels spike. Using the allosteric model, predict and explain the combined effect of elevated AMP and elevated fructose-2,6-BP on glycolytic flux in exercising muscle.

5. Metformin, the first-line drug for type 2 diabetes, inhibits Complex I of the mitochondrial electron transport chain, increasing the AMP:ATP ratio. Using your metabolic knowledge, predict at least three downstream effects of elevated AMP: (a) on PFK-1; (b) on glycogen synthase; (c) on gluconeogenesis. Does this make metabolic sense as a diabetes treatment?


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** Compare metabolic responses to a 24-hour fast in two individuals: (i) a metabolically healthy adult and (ii) a patient with untreated type 1 diabetes (effectively zero circulating insulin). Use the GTT/AUC data and the chapter:
>
> (a) For the healthy adult, describe the predicted time course of blood glucose, insulin, glucagon, free fatty acids, and ketone bodies over the 24 hours. Identify the key hormonal switch that initiates lipolysis and ketogenesis.
> (b) For the type 1 diabetic, predict how each of the same variables would differ — and explain why, in molecular terms, the absence of insulin removes a brake on lipolysis and ketogenesis even when blood glucose is elevated.
> (c) Use your prediction in (b) to explain why diabetic ketoacidosis is a medical emergency in this scenario. Distinguish it carefully from physiological ketosis seen during normal prolonged fasting in a healthy individual, identifying the variable that crosses a pathological threshold and the mechanism that drives the crossing.

## Extension Analysis Questions {.unnumbered}

6. **Statistical Analysis**: Calculate the standard error of the mean (SEM) for each subject group. Construct 95% confidence intervals. Are the differences between groups statistically significant based on your ANOVA?

7. **Experimental Error Analysis**: What are three potential sources of error in this data analysis? How could you modify the procedure to reduce each source of error?

8. **Experimental Design**: If you were to design a follow-up experiment to distinguish between insulin resistance and β-cell dysfunction in the pre-diabetic subject, what would you measure? How would you interpret the results?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design a Metabolic Syndrome Risk Assessment Tool**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- What factors contribute to metabolic syndrome (obesity, hypertension, high blood glucose, dyslipidemia)?
- How can we use simple measurements to assess risk?
- Write a detailed protocol for assessing metabolic health in a human population

**Session 2**: Data Collection and Analysis
- Use de-identified public datasets or fully simulated classroom data
- Calculate risk scores based on waist circumference, blood pressure, fasting glucose, triglycerides, HDL
- Analyze correlations between different risk factors

**Session 3**: Tool Development and Presentation
- Develop a simple risk assessment tool (questionnaire or calculator)
- Validate it against known metabolic syndrome criteria
- Create a scientific poster or presentation

## Real-World Problem Solving: Metabolic Diseases {.unnumbered}

**Case Study: Type 2 Diabetes Prevention**

Type 2 diabetes is largely preventable through lifestyle modifications, yet incidence continues to rise globally. 

1. **Research Task**: Investigate the effectiveness of different interventions (diet, exercise, medication) in preventing or delaying type 2 diabetes in high-risk individuals.

2. **Ethical Consideration**: Should employers or insurance companies offer incentives for healthy behaviors? What are the potential benefits and risks of such programs?

3. **Policy Proposal**: Design a community-based program to reduce the incidence of type 2 diabetes. Consider factors like access to healthy food, safe spaces for exercise, and education.

## Safety and Ethics Notes {.unnumbered}

Paper-based data-analysis lab — no chemical hazards, biological samples, or volunteer data collection are required. If using real public patient data, most data must be de-identified and handled with privacy-preserving practices.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_III_metabolic_integration} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_III_metabolic_integration} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/biochemistry/biochemistry.py` for metabolic calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
