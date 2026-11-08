# Questions — Complex Adaptive Systems {#sec:q_unit_0_complex_adaptive_systems .unnumbered}


## Questions 1–10 {.unnumbered}

*This activity accompanies \cref{sec:unit_0_complex_adaptive_systems} of the textbook — review that chapter before attempting the exercises below.*

---

## Foundational comparisons {.unnumbered}

## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Explain an observed population pattern from individual-level rules and identify one falsifiable prediction.
- **Model/data emphasis:** Agent-rule and scaling arguments for emergent biological patterns.
- **Assessment alignment:** Questions and Methods, Representing and Describing Data, Argumentation.
- **Misconception probe:** Emergence is not mysterious; it is a reproducible consequence of interactions plus constraints.
- **Transfer product:** Compare flocking, immune activation, and microbial biofilms as adaptive systems.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.

<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define 'complex adaptive systems' in your own words and provide a biological example.

<!-- SOLUTION
**Answer (Q1, Recall).** A complex adaptive system is a population of many heterogeneous agents that interact locally, adapt their behavior from local information, and thereby generate emergent, nonlinear, history-dependent properties that no single agent contains and no central controller imposes. Biological example: an ant colony — individuals follow simple pheromone rules, yet the colony collectively solves foraging, task allocation, and defense (other examples: the immune system, the brain, ecosystems).
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
2. What is stigmergy in an ant colony?

<!-- SOLUTION
**Answer (Q2, Recall).** Agents modify a shared environment, such as a pheromone trail, which influences later agents. No ant needs a map of the colony-wide route.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
3. Distinguish variation from selection in an adapting population.

<!-- SOLUTION
**Answer (Q3, Recall).** Variation creates phenotypic or genetic alternatives; differential reproductive success changes their frequencies. Selection does not generate a needed mutation on demand.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
4. Define hysteresis and name the comparison that demonstrates it.

<!-- SOLUTION
**Answer (Q4, Recall).** At the same external parameter, the stable state depends on whether the parameter was approached from above or below. Measure both increasing and decreasing sweeps after equilibration; a single steep curve is insufficient.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
5. In the NK landscape, what do N and K represent?

<!-- SOLUTION
**Answer (Q5, Recall).** N counts loci or components; K counts the other components influencing each component contribution. Increased epistasis can make the landscape more rugged; K is not population size.
SOLUTION -->

---

## Mechanisms and applications {.unnumbered}

<!-- assess: LO=LO7; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
6. Compute two iterations of x_next=3.2x(1-x) from x0=0.2.

<!-- SOLUTION
**Answer (Q6, Application).** x1=0.512 and x2=3.2(0.512)(0.488)=0.7995392. Preserve adequate precision because rounding differences propagate.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
7. For the logistic map, derive the nonzero fixed point and test its stability at r=2.5 and r=3.2.

<!-- SOLUTION
**Answer (Q7, Application).** xstar=1-1/r. The derivative there is 2-r, so it is stable when abs(2-r)<1. At 2.5 the derivative is -0.5 (stable); at 3.2 it is -1.2 (unstable). This is a discrete map, not the continuous logistic ODE.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
8. A synthetic lake switches to turbid at P=8 loading units when P rises, but returns to clear at P=3 when P falls. Predict its state at P=5 for both histories.

<!-- SOLUTION
**Answer (Q8, Application).** Starting clear and increasing to 5 leaves it clear; starting turbid and decreasing to 5 leaves it turbid. The interval 3<P<8 supports history-dependent alternatives under this illustrative rule.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
9. Compare genetic algorithms with biological selection, naming one shared operation and one limitation.

<!-- SOLUTION
**Answer (Q9, Application).** Both can combine heritable variation with differential replication or retention. A genetic algorithm usually has a designer-defined objective and representation; biological fitness is contextual and does not require a designer or a fixed global goal.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
10. A resistant variant starts at frequency 0.01 and has survival 1; sensitive cells have survival 0.1. Find the resistant fraction among survivors.

<!-- SOLUTION
**Answer (Q10, Application).** Resistant survivor mass=0.01; sensitive=0.99 times 0.1=0.099. Fraction=0.01/0.109=0.09174. Frequency rises without requiring treatment-induced mutation; survival is not subsequent reproductive fitness.
SOLUTION -->

---

## Integrated reasoning {.unnumbered}

## Questions 11–20 {.unnumbered}

<!-- assess: LO=LO6; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
11. A two-locus synthetic fitness table is 00:1, 10:2, 01:2, 11:0.5. Identify peaks under single-bit changes and explain path dependence.

<!-- SOLUTION
**Answer (Q11, Application).** 10 and 01 are local peaks: each neighbor has lower fitness. Starting at 00, either first beneficial substitution can trap an uphill-only walk at a different peak. The double mutant is not additively beneficial; the table has sign epistasis.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
12. A perturbation of amplitude 2 cannot cross a basin barrier of 3 in an illustrative threshold model. Predict recovery after the pulse and identify a limitation of the analogy.

<!-- SOLUTION
**Answer (Q12, Application).** The state remains in its original basin and relaxes toward its original attractor. A larger perturbation might cross the boundary, but amplitude and barrier must be expressed in comparable model coordinates. A potential landscape is not automatically a measured therapy-response law.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
13. Describe how ecosystem collapse (e.g., coral bleaching, fishery collapse) can be framed as a phase transition in a complex adaptive system. What warning signals might precede the transition? Why is recovery often much harder than the original decline?

<!-- SOLUTION
**Answer (Q13, Application).** A reef or fishery near a bifurcation has a shallow basin of attraction; a small additional forcing (warming, harvest pressure) pushes it across a tipping point into an alternative stable state (algal-dominated reef, collapsed stock). Early-warning signals are signatures of *critical slowing down* — rising variance, increased autocorrelation, and slower recovery from small disturbances. Recovery is hard because of hysteresis: feedbacks that stabilize the new state (macroalgal dominance, recruitment failure) mean the driver must fall far below the original threshold before the system flips back.
SOLUTION -->

## Data and Model Interpretation Questions (3 marks each) {.unnumbered}

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
14. In an agent-based simulation, changing one local rule from "align with three neighbors" to "align with six neighbors" causes global order to appear faster. Explain why this is an emergent result rather than a command from a central controller.

<!-- SOLUTION
**Answer (Q14, Application).** The global pattern changes because each agent samples more neighbors, increasing local coupling. No agent stores the global pattern or directs the group. The ordered state emerges from repeated local interactions plus boundary conditions.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
15. A microbial biofilm becomes resistant to an antibiotic even though many isolated cells from the same biofilm remain sensitive. Give two complex-adaptive explanations.

<!-- SOLUTION
**Answer (Q15, Application).** Biofilm structure can limit diffusion, create slow-growing or dormant cells, and generate chemical microenvironments that reduce drug efficacy. Interactions among cells, matrix, nutrients, and gradients create a collective phenotype that isolated cells do not show.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. A fitness landscape has one tall narrow peak and one lower broad peak. Which peak is easier for a population to maintain under mutation and environmental noise, and why?

<!-- SOLUTION
**Answer (Q16, Application).** The broad peak is usually more robust because nearby genotypes still have relatively high fitness. A tall narrow peak may have high maximum fitness but is fragile: small mutational or environmental shifts can move the population into low-fitness territory.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
17. Explain how a phase transition differs from a gradual linear change. Use one biological example.

<!-- SOLUTION
**Answer (Q17, Recall).** A phase transition occurs when a small parameter change near a threshold produces a qualitative state change. Examples include quorum sensing activation, membrane depolarization threshold, ecosystem eutrophication, or protein folding. Linear change lacks that abrupt threshold behavior.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
18. A population repeatedly evolves the same resistance mutation in separate cultures. Does this prove evolution is deterministic? Give a careful answer.

<!-- SOLUTION
**Answer (Q18, Synthesis).** It shows strong constraint or a high-probability adaptive route, not full determinism. Selection, mutation supply, population size, and available genetic paths can make outcomes repeatable, while drift and rare mutations still create contingency.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. Compare self-organization in embryonic patterning and in ant foraging. What is shared, and what differs?

<!-- SOLUTION
**Answer (Q19, Application).** Both involve local interactions that produce organized global patterns. Embryonic patterning often uses molecular gradients, gene regulatory networks, and mechanical constraints; ant foraging uses mobile agents, pheromone trails, and reinforcement. The shared logic is local rule plus feedback; the substrates and time scales differ.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
20. A complex system model reproduces one observed pattern but fails under a new perturbation. What does this tell you about model validation?

<!-- SOLUTION
**Answer (Q20, Synthesis).** Matching one pattern is not enough. A useful model should also predict responses to perturbation, reproduce independent data, and fail in interpretable ways. The failure may reveal missing agents, hidden variables, wrong interaction rules, or parameter overfitting.
SOLUTION -->

## Questions 21–30 {.unnumbered}

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
21. Explain why heterogeneity among agents can make a population more resilient.

<!-- SOLUTION
**Answer (Q21, Application).** Heterogeneity spreads risk. If agents differ in behavior, physiology, genotype, or location, one stress rarely harms all agents equally. Diversity can preserve function during perturbation, though it can also slow coordinated responses.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
22. A cancer therapy kills 99% of tumor cells but leaves a small resistant subpopulation. Explain why this can select for relapse.

<!-- SOLUTION
**Answer (Q22, Application).** Therapy changes the selection environment. Sensitive cells are removed, reducing competition for resistant cells. If resistant cells survive and replicate, the post-treatment tumor can be enriched for the resistant phenotype even if it was initially rare.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
23. Distinguish adaptation by natural selection from adaptation by learning within an organism. Why can both be described as adaptive processes?

<!-- SOLUTION
**Answer (Q23, Recall).** Natural selection changes population allele or trait frequencies across generations; learning changes behavior or internal models within a lifetime. Both are adaptive because feedback from the environment alters future performance, but the substrate, inheritance, and time scale differ.
SOLUTION -->

## Evaluation and Design Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO2; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
24. Design a simple agent-based model for immune-cell recruitment to an infection site. Specify agents, local rules, and one emergent output.

<!-- SOLUTION
**Answer (Q24, Synthesis).** Agents might include immune cells, pathogens, and damaged tissue cells. Local rules could include chemotaxis up a cytokine gradient, pathogen killing on contact, cytokine release after recognition, and cell death after a lifespan. Emergent outputs include inflammatory focus size, pathogen clearance time, or overshooting tissue damage.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Evaluate the claim: "Because complex systems are unpredictable, modeling them is useless."

<!-- SOLUTION
**Answer (Q25, Synthesis).** The claim is too strong. Complex systems may be hard to predict exactly, but models can identify thresholds, sensitivities, robust qualitative behaviors, and useful intervention points. The goal is often constrained prediction and mechanistic insight, not perfect point forecasting.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Propose a way to detect whether a community pattern is produced by local interactions or by a shared external gradient.

<!-- SOLUTION
**Answer (Q26, Synthesis).** Measure or manipulate the external gradient while also mapping local neighbor effects. If the pattern persists after controlling for the gradient, local interactions are implicated. Transplant, removal, or randomized-neighbor experiments can separate neighbor causation from shared environmental forcing.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. A student says emergence means "anything can happen." Correct this using constraints and repeated patterns.

<!-- SOLUTION
**Answer (Q27, Synthesis).** Emergence does not mean arbitrary outcomes. It means global properties arise from interactions among parts. The outcomes are constrained by rules, geometry, resources, feedback, and history, which is why similar patterns can recur across biofilms, tissues, flocks, and ecosystems.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
28. Build a complex-adaptive explanation of antibiotic resistance that includes mutation, selection, horizontal gene transfer, and clinical practice.

<!-- SOLUTION
**Answer (Q28, Synthesis).** Mutation and horizontal gene transfer generate variation; antibiotic exposure selects resistant variants; hospitals and farms can amplify transmission; incomplete treatment or misuse changes the selection regime. The emergent population-level result is increased resistance prevalence.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
29. Choose one chapter later in the textbook and explain how its topic could be reframed as a complex adaptive system.

<!-- SOLUTION
**Answer (Q29, Synthesis).** A biofilm example has heterogeneous microbial cells as agents (1), local nutrient uptake, matrix secretion and neighbor signaling as interactions (1), and differential growth or survival under nutrient/drug gradients as adaptation (1). A collective tolerant phenotype that weakens when cells are dispersed is a testable emergent output; compare intact/dispersed samples at matched drug exposure and control growth state, because dispersal itself changes physiology (1). This is a concrete CAS hypothesis, not proof that all resistance is emergent; see \cref{sec:unit_0_complex_adaptive_systems}.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
30. Design a falsifiable prediction that would distinguish two competing rule sets in an agent-based model of cell migration.

<!-- SOLUTION
**Answer (Q30, Synthesis).** A good prediction identifies a perturbation that makes the rule sets diverge. For example, if one model depends on chemotaxis and another on contact inhibition, flattening the chemical gradient should disrupt directed migration only in the chemotaxis model, whereas changing cell density should mainly affect the contact-inhibition model.
SOLUTION -->

---

*Module: `src/biology/` (general).*
