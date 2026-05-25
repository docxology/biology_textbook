# Lab — Antimicrobial Resistance and Epidemiology {.unnumbered}

<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Antimicrobial Resistance and Epidemiology.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
\label{sec:lab_unit_VII_antimicrobial_resistance_and_epidemiology}

*This activity accompanies \cref{sec:unit_VII_antimicrobial_resistance_and_epidemiology} of the textbook — review that chapter before attempting the exercises below.*

## Lab Context: Antimicrobial Resistance and Epidemiology {.unnumbered}

This extension lab connects resistance mechanisms, surveillance data, and epidemic modelling using printed case cards and computational templates.

## Paper-Based Materials {.unnumbered}

| Item | Quantity |
| ---- | -------- |
| Source-governance card for Antimicrobial Resistance and Epidemiology: pathogen-surveillance source card: organism-resistance pair, official guidance date, setting, and intervention limit | 1 |
| Printed datasets, cards, and worksheets referenced below | 1 set per group |
| Graph paper or plain paper for diagrams | 1 |
| Calculator | 1 |

## Paper-Based Investigation {.unnumbered}

*Optional computational check: run this self-contained Python snippet from the project root. It uses tested `src/biology` modules and requires no external notebook or CSV file.*

Model outbreak curves with the tested SIR implementation.

```python
from biology.microbiology import sir_model

baseline = sir_model(population=10_000, initial_infected=10, beta_per_day=0.35, gamma_per_day=0.1, days=30)
distancing = sir_model(population=10_000, initial_infected=10, beta_per_day=0.18, gamma_per_day=0.1, days=30)

print("baseline R0:", baseline.r0, "peak infected:", round(max(baseline.infected)))
print("distancing R0:", distancing.r0, "peak infected:", round(max(distancing.infected)))
```
### Part 3: Herd Immunity Calculation {.unnumbered}

5. **Design an Alternative Experiment**: Instead of just calculating herd immunity thresholds, design an experiment to test how different vaccination rates affect disease spread in a simulated population. What hypothesis would you test? How would you model transmission?

6. **Hypothesis**: Predict the relationship between vaccination coverage and peak epidemic size. Would you expect a linear relationship, or something else? Why?

### Part 4: Current Intervention Decision Matrices {.unnumbered}

7. Use the TB decision cards to classify each case as standard drug-susceptible therapy, BPaLM/BPaL eligibility review, or individualized specialist regimen. Record the evidence that makes you confident or uncertain.
8. Use the HIV PrEP comparison card to match patient scenarios to a plausible PrEP option. Separate biological efficacy, adherence feasibility, contraindications, testing needs, and access constraints.
9. Use the malaria vector-control card to design a layered prevention package for a household with night-time exposure, daytime indoor exposure, and insecticide-resistance concerns. Explain why no single tool replaces surveillance.

## Data Recording {.unnumbered}

Epidemic curve: peak at hour ___; attack rate: ___%; estimated incubation: ___ h; R₀ ≈ ___

| Antibiotic | Zone (mm) | Interpretation (S/I/R) |
| ---------- | --------- | ----------------------- |
| Ampicillin | | |
| Kanamycin | | |
| Tetracycline | | |
| Chloramphenicol | | |

Replicate zone agreement within ±2 mm? _______; AMR mechanism card selected: _______
TB regimen path selected: _______; PrEP option justified: _______; malaria control package: _______

| Disease | R₀ | Herd immunity threshold (p_c) |
| ------- | -- | ------------------------------- |
| Measles | 15 | |
| Influenza | 2.5 | |
| COVID-19 | 2.9 | |
| Mumps | 5 | |
| Polio | 6 | |

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Model transmission and compare resistance-control strategies.
- **Data skill to practice:** Interpret resistance assays and outbreak curves.
- **BioSkills emphasis:** Science and society, Process of science, Modeling and simulation.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Infectious Disease and Immunity** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: in this lab, trace every outbreak conclusion back to its evidence chain (case definition, transmission parameter, and the diagnostic or surveillance signal it rests on), and name the alternative epidemic explanation you ruled out before reporting an $R_0$ or attack rate. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example: Herd Immunity Threshold from R-zero {.unnumbered}

**Problem:** A respiratory illness has R₀ = 4 in an unvaccinated population of 80,000. A vaccine with 92% efficacy is available. Calculate (a) the herd immunity threshold H = 1 − 1/R₀, and (b) the minimum vaccination coverage needed to achieve herd immunity given 92% efficacy.

**Solution:** (a) H = 1 − 1/4 = 0.75, so 75% of the population must be immune. (b) Required vaccination coverage = H / vaccine efficacy = 0.75 / 0.92 ≈ 0.815 = 81.5%. At least 81.5% of the population must be vaccinated to reach the herd immunity threshold.

**Interpretation:** Vaccine efficacy below 100% means that a higher fraction of the population must be vaccinated than the herd immunity threshold itself — a key consideration in public health planning.

## Analysis Questions {.unnumbered}

1. If the epidemic curve shows a single sharp peak within a window shorter than the incubation period, what type of source does this suggest? How would a propagated (person-to-person) epidemic curve look different?

2. *E. coli* showed resistance to ampicillin but susceptibility to kanamycin. Explain the likely molecular mechanism of ampicillin resistance (naming the specific enzyme) and why one β-lactamase can create cross-resistance to several related β-lactams while still leaving some β-lactam/β-lactamase-inhibitor combinations, carbapenems, or non-β-lactam drugs active depending on the enzyme and permeability context.

3. Measles has an R₀ of ~15, requiring ~93% vaccination for herd immunity. Your calculation shows that even high measles vaccination coverage is needed. What happens to herd immunity when 5% of a vaccinated population declines vaccination? Relate this to observed measles outbreaks in Europe (2019).

4. An immunocompromised patient (CD4 T cell count < 200/µL, HIV+ AIDS) contracts measles despite prior vaccination. Explain: (a) why the vaccine may be insufficient; (b) which branch of adaptive immunity (humoral or cellular) is most deficient; (c) what specific viral clearance mechanism is impaired.

5. The O'Neill Review's 10-million-deaths-per-year by 2050 AMR estimate is a historical warning scenario, not a current burden count \citep{oneill2016amr}. Describe three specific mechanisms by which bacteria acquire resistance genes, and evaluate two distinct policy interventions that would slow the spread of AMR at a population level.
6. A malaria programme already distributes insecticide-treated nets, but household surveys show substantial indoor activity before bedtime. Use the vector-control matrix to decide whether spatial emanators could be an added tool, and state two evidence gaps that would still require local monitoring.

## Extension Analysis Questions {.unnumbered}

7. **Statistical Analysis**: If the printed dataset includes three replicate disc-diffusion images, how would you analyze the variation in zone diameters? What statistical test would you use to determine if differences between antibiotics are significant?

8. **Experimental Error Analysis**: What are three potential sources of error in epidemic curve analysis? How could you modify the procedure to reduce each source of error?

9. **Experimental Design**: If you wanted to test the effectiveness of different public health interventions (e.g., vaccination, social distancing) in controlling an outbreak, how would you design the experiment? What data would you collect? How would you analyze it?

## Group Project Extension (Multi-Session) {.unnumbered}

**Design an Epidemiological Study of Vaccine Hesitancy**

This project will span 2-3 lab sessions:

**Session 1**: Research Question and Hypothesis
- How does vaccine hesitancy affect disease outbreak size?
- Formulate a hypothesis about the relationship between vaccine coverage and outbreak probability
- Design a study using simulation or real outbreak data

**Session 2**: Data Collection and Analysis
- Collect data on vaccine coverage and outbreak sizes from public health records
- Analyze the correlation between coverage and outbreak size
- Model the impact of increasing vaccine hesitancy on outbreak risk

**Session 3**: Data Interpretation and Presentation
- Calculate the critical vaccination threshold for different diseases
- Discuss the public health implications of declining vaccine coverage
- Create a scientific poster or presentation

## Real-World Problem Solving: Epidemic Ethics {.unnumbered}

**Case Study: Quarantine and Civil Liberties**

1. **Research Task**: Investigate the legal and ethical basis for quarantine during infectious disease outbreaks. What are the key principles that balance public health needs with individual rights?

2. **Ethical Consideration**: Should governments have the power to enforce quarantine on individuals who refuse vaccination? What are the potential benefits and risks of such policies?

3. **Policy Proposal**: Design a policy for implementing quarantine measures during an outbreak that respects civil liberties while protecting public health. Consider: due process, compensation for lost income, and transparent decision-making.


## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A pathogen evolves increased transmissibility (higher R₀) while simultaneously causing milder symptoms.
>
> (a) Using fitness trade-off reasoning, explain why reduced virulence might accompany increased transmissibility from an evolutionary perspective.
> (b) How would an increase in R₀ from 2 to 5 change the herd immunity threshold, and what does this imply for the fraction of the population that must be immune?
> (c) Evaluate whether increased transmissibility alone (without changes in virulence) would change the total number of individuals affected during an epidemic — use the final size equation concept to guide your reasoning.

## Safety and Ethics Notes {.unnumbered}

Default lab work uses printed outbreak datasets, susceptibility images, and AMR mechanism cards primarily. No bacterial cultures, agar plates, or antibiotic discs are required. Optional wet susceptibility demonstrations must use approved BSL-1 organisms under instructor supervision and local disposal rules. Discuss epidemic data without stigmatising affected groups. When discussing antibiotics, emphasize following current prescriber instructions, avoiding unnecessary antibiotic starts, using diagnostics when available, and protecting access to effective treatment.

### Source-Governance Checkpoint {.unnumbered}

Complete the source-governance card for Antimicrobial Resistance and Epidemiology before writing the conclusion. Name the source type or model snapshot, record the evidence date or version, decide whether the claim is stable or fast-moving, and write one refresh trigger that would force the interpretation to change. Treat the card as a printed evidence object, not as a live web lookup.

## Debrief and Reflection {.unnumbered}

After you finish the practical work, spend 5–10 minutes in your small group comparing results and discussing the following prompts. Each member should contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to the textbook's predictions. Where they diverge, suggest at least one mechanistic explanation before concluding "experimental error."

2. **What would change the outcome** — propose one modification to the procedure that would sharpen the measurement or extend the result to a new biological context, and predict what you would observe.

3. **One-sentence headline** — each student composes a single sentence summarising the lab's take-home message, suitable for a tweet. Compare sentences across groups; good headlines are short, quantitative, and mechanistic.

4. **Connection back to the textbook** — identify one section of \cref{sec:unit_VII_antimicrobial_resistance_and_epidemiology} that your data either confirmed or complicated. Cite the specific passage.

5. **Experimental Design Reflection**: What was the strongest aspect of your experimental design? What would you change if you could repeat the experiment?

## Further Reading (Lab) {.unnumbered}

- Revisit the parent chapter \cref{sec:unit_VII_antimicrobial_resistance_and_epidemiology} for the theoretical foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter (each has a `#gl:term-slug` link in the text) — its master definition is in `manuscript/glossary.md`.
- Explore the Python code in `src/biology/microbiology/microbiology.py` for epidemiological calculations.
- Use the self-contained Part 2 snippet as the computational template; it runs against tested project modules without external notebooks or CSV files.
