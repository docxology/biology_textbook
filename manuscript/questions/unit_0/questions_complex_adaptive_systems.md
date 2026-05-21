# Questions — Ch 0.2: Complex Adaptive Systems {.unnumbered}

\label{sec:q_unit_0_complex_adaptive_systems}

*This activity accompanies \cref{sec:unit_0_complex_adaptive_systems} of the textbook — review that chapter before attempting the exercises below.*

---

## Recall Questions (1 mark each) {.unnumbered}

<!-- question-coverage-start -->
## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Explain an observed population pattern from individual-level rules and identify one falsifiable prediction.
- **Model/data emphasis:** Agent-rule and scaling arguments for emergent biological patterns.
- **Assessment alignment:** Questions and Methods, Representing and Describing Data, Argumentation.
- **Misconception probe:** Emergence is not mysterious; it is a reproducible consequence of interactions plus constraints.
- **Transfer product:** Compare flocking, immune activation, and microbial biofilms as adaptive systems.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.
<!-- question-coverage-end -->

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define 'complex adaptive systems' in your own words and provide a biological example.

<!-- SOLUTION
**Answer (Q1, Recall).** A complex adaptive system is a population of many heterogeneous agents that interact locally, adapt their behaviour from local information, and thereby generate emergent, nonlinear, history-dependent properties that no single agent contains and no central controller imposes. Biological example: an ant colony — individuals follow simple pheromone rules, yet the colony collectively solves foraging, task allocation, and defence (other examples: the immune system, the brain, ecosystems).
SOLUTION -->
<!-- assess: LO=LO2; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. What distinguishes a complex adaptive system from a simple system?

<!-- SOLUTION
**Answer (Q2, Recall).** A simple system has few components and fixed, predictable input–output relations. A complex adaptive system is a network of many heterogeneous agents that act on local information and adapt, producing emergent, nonlinear, history-dependent behaviour that cannot be predicted from any agent alone (e.g., the immune system, an ant colony, an ecosystem). The defining contrast is adaptation and emergence versus fixed, decomposable mechanism.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
3. What is the free energy principle? What does free energy measure?

<!-- SOLUTION
**Answer (Q3, Recall).** The free energy principle (Friston) states that any system that maintains itself far from equilibrium must act and perceive so as to minimise *variational free energy* — an information-theoretic upper bound on sensory surprise. Free energy measures the mismatch between the organism's internal generative model (its predictions) and the sensory data it actually receives; minimising it keeps the organism within its viable physiological states.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
4. Describe one biological example of negative feedback and one of positive feedback.

<!-- SOLUTION
**Answer (Q4, Recall).** Negative feedback: thermoregulation — a rise in core temperature triggers sweating and vasodilation that return temperature toward the set point (stabilising). Positive feedback: the rising phase of the action potential — Na⁺ influx depolarises the membrane, opening more voltage-gated Na⁺ channels and amplifying the depolarisation until channels inactivate (self-reinforcing and self-limiting).
SOLUTION -->
<!-- assess: LO=LO5; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
5. What is the difference between homeostasis and allostasis?

<!-- SOLUTION
**Answer (Q5, Recall).** Homeostasis holds a regulated variable near a *fixed* set point through reactive negative feedback. Allostasis (Sterling) achieves stability *through change*: the brain predictively adjusts set points and mobilises resources in anticipation of demand, so the target itself moves. The decisive difference is reactive constancy versus anticipatory, model-based set-point adjustment.
SOLUTION -->

---

## Application Questions (2 marks each) {.unnumbered}

<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
6. A drug blocks a key kinase in a signalling cascade, but the tumour eventually regrows. Explain this outcome using the concept of feedback compensation.

<!-- SOLUTION
**Answer (Q6, Application).** Blocking one kinase removes a single edge of a signalling network, but negative-feedback nodes the pathway normally suppresses are de-repressed and parallel routes reroute flux to restore downstream signalling (e.g., loss of ERK-mediated feedback reactivates upstream receptor/PI3K input). The network's redundancy and compensatory feedback restore proliferative output, so single-target inhibition is evaded — which is why combination therapy is often required.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
7. Explain why the lac operon switch is described as bistable. What advantage does bistability provide over a graded (linear) response?

<!-- SOLUTION
**Answer (Q7, Application).** Positive feedback (the LacY permease imports inducer, which further activates the operon) combined with cooperative repressor binding gives the system two stable states — fully ON or fully OFF — separated by an unstable threshold. Bistability produces a sharp, hysteretic, all-or-none commitment that filters molecular noise and avoids wasteful partial expression, whereas a graded linear response would track every fluctuation in inducer concentration.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
8. How does the concept of attractors in phase space relate to cell fate? Give an example.

<!-- SOLUTION
**Answer (Q8, Application).** In the dynamical-systems view of gene-regulatory networks, each stable attractor in expression state space corresponds to a cell type; a cell's state flows to the nearest attractor and resists small perturbations within its basin. Example: a hematopoietic progenitor sits near an unstable point and commits to an erythroid or myeloid attractor once a regulatory switch (e.g., the GATA1–PU.1 toggle) pushes it across the separatrix.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
9. Apply the active inference framework to explain how a fever might be adaptive rather than merely a pathological response.

<!-- SOLUTION
**Answer (Q9, Application).** Under active inference an organism acts to fulfil its predictions about preferred, viable states. Infection raises the *expected* (set-point) temperature encoded by the hypothalamic generative model; the body then acts — shivering, vasoconstriction — to realise that prediction because elevated temperature accelerates immune kinetics and impairs pathogen replication. Fever is thus a controlled, model-driven allostatic shift rather than a regulatory failure, adaptive up to its metabolic and tissue-stress costs.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
10. In evolutionary terms, what is niche construction, and how does it relate to the free energy principle?

<!-- SOLUTION
**Answer (Q10, Application).** Niche construction is the organism's modification of its own environment (beaver dams, earthworm-altered soil), changing the selection pressures it and its descendants experience. Under the free energy principle, agents minimise surprise not only by updating internal models (perception) but by acting on the world so it matches their expected states — niche construction is free-energy minimisation externalised and inherited across generations, stabilising the organism–environment fit.
SOLUTION -->

---

## Synthesis Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO3; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
11. Compare and contrast the immune system and an evolving tumour as complex adaptive systems. In each case, identify (a) the agents, (b) the selection pressures, (c) an emergent property, and (d) a critical vulnerability.

<!-- SOLUTION
**Answer (Q11, Synthesis).** Both are populations of heritable, variable, selected agents whose adaptive behaviour is emergent. (a) Agents: lymphocyte clones vs tumour subclones. (b) Selection pressures: antigen affinity and self-tolerance vs immune attack, therapy, hypoxia. (c) Emergent property: immunological memory vs collective drug resistance. (d) Critical vulnerability: tolerance breakdown or T-cell exhaustion vs dependence on a driver mutation or shared resource. The decisive contrast: the immune system is selected for host benefit, whereas tumour evolution is selected purely for local proliferative fitness against the host.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
12. A patient with chronic anxiety has persistent overactivation of the sympathetic nervous system even in the absence of objective threat. Using predictive coding and active inference, construct a mechanistic account of how prior beliefs about threat might drive this pattern. How might therapeutic interventions (CBT, interoceptive exposure) alter the generative model?

<!-- SOLUTION
**Answer (Q12, Synthesis).** A precise prior predicting threat makes the generative model expect high interoceptive arousal; because that prior is weighted as highly precise, it dominates weaker sensory evidence, and prediction errors are resolved by *active* inference — driving sympathetic output to make the body match the 'danger' prediction, sustaining arousal with no external threat. CBT and interoceptive exposure reduce the precision of the threat prior and increase the weighting of disconfirming interoceptive evidence, reshaping the generative model so predictions no longer demand sympathetic activation.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
13. Describe how ecosystem collapse (e.g., coral bleaching, fishery collapse) can be framed as a phase transition in a complex adaptive system. What warning signals might precede the transition? Why is recovery often much harder than the original decline?

<!-- SOLUTION
**Answer (Q13, Synthesis).** A reef or fishery near a bifurcation has a shallow basin of attraction; a small additional forcing (warming, harvest pressure) pushes it across a tipping point into an alternative stable state (algal-dominated reef, collapsed stock). Early-warning signals are signatures of *critical slowing down* — rising variance, increased autocorrelation, and slower recovery from small disturbances. Recovery is hard because of hysteresis: feedbacks that stabilise the new state (macroalgal dominance, recruitment failure) mean the driver must fall far below the original threshold before the system flips back.
SOLUTION -->

## Data and Model Interpretation Questions (3 marks each) {.unnumbered}

<!-- assess: LO=LO6; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
14. In an agent-based simulation, changing one local rule from "align with three neighbours" to "align with six neighbours" causes global order to appear faster. Explain why this is an emergent result rather than a command from a central controller.

<!-- SOLUTION
**Answer (Q14, Analysis).** The global pattern changes because each agent samples more neighbours, increasing local coupling. No agent stores the global pattern or directs the group. The ordered state emerges from repeated local interactions plus boundary conditions.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
15. A microbial biofilm becomes resistant to an antibiotic even though many isolated cells from the same biofilm remain sensitive. Give two complex-adaptive explanations.

<!-- SOLUTION
**Answer (Q15, Application).** Biofilm structure can limit diffusion, create slow-growing or dormant cells, and generate chemical microenvironments that reduce drug efficacy. Interactions among cells, matrix, nutrients, and gradients create a collective phenotype that isolated cells do not show.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. A fitness landscape has one tall narrow peak and one lower broad peak. Which peak is easier for a population to maintain under mutation and environmental noise, and why?

<!-- SOLUTION
**Answer (Q16, Analysis).** The broad peak is usually more robust because nearby genotypes still have relatively high fitness. A tall narrow peak may have high maximum fitness but is fragile: small mutational or environmental shifts can move the population into low-fitness territory.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. Explain how a phase transition differs from a gradual linear change. Use one biological example.

<!-- SOLUTION
**Answer (Q17, Analysis).** A phase transition occurs when a small parameter change near a threshold produces a qualitative state change. Examples include quorum sensing activation, membrane depolarization threshold, ecosystem eutrophication, or protein folding. Linear change lacks that abrupt threshold behaviour.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. A population repeatedly evolves the same resistance mutation in separate cultures. Does this prove evolution is deterministic? Give a careful answer.

<!-- SOLUTION
**Answer (Q18, Evaluation).** It shows strong constraint or a high-probability adaptive route, not full determinism. Selection, mutation supply, population size, and available genetic paths can make outcomes repeatable, while drift and rare mutations still create contingency.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. Compare self-organization in embryonic patterning and in ant foraging. What is shared, and what differs?

<!-- SOLUTION
**Answer (Q19, Analysis).** Both involve local interactions that produce organized global patterns. Embryonic patterning often uses molecular gradients, gene regulatory networks, and mechanical constraints; ant foraging uses mobile agents, pheromone trails, and reinforcement. The shared logic is local rule plus feedback; the substrates and time scales differ.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. A complex system model reproduces one observed pattern but fails under a new perturbation. What does this tell you about model validation?

<!-- SOLUTION
**Answer (Q20, Evaluation).** Matching one pattern is not enough. A useful model should also predict responses to perturbation, reproduce independent data, and fail in interpretable ways. The failure may reveal missing agents, hidden variables, wrong interaction rules, or parameter overfitting.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
21. Explain why heterogeneity among agents can make a population more resilient.

<!-- SOLUTION
**Answer (Q21, Analysis).** Heterogeneity spreads risk. If agents differ in behaviour, physiology, genotype, or location, one stress rarely harms all agents equally. Diversity can preserve function during perturbation, though it can also slow coordinated responses.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
22. A cancer therapy kills 99% of tumour cells but leaves a small resistant subpopulation. Explain why this can select for relapse.

<!-- SOLUTION
**Answer (Q22, Application).** Therapy changes the selection environment. Sensitive cells are removed, reducing competition for resistant cells. If resistant cells survive and replicate, the post-treatment tumour can be enriched for the resistant phenotype even if it was initially rare.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
23. Distinguish adaptation by natural selection from adaptation by learning within an organism. Why can both be described as adaptive processes?

<!-- SOLUTION
**Answer (Q23, Analysis).** Natural selection changes population allele or trait frequencies across generations; learning changes behaviour or internal models within a lifetime. Both are adaptive because feedback from the environment alters future performance, but the substrate, inheritance, and time scale differ.
SOLUTION -->

## Evaluation and Design Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
24. Design a simple agent-based model for immune-cell recruitment to an infection site. Specify agents, local rules, and one emergent output.

<!-- SOLUTION
**Answer (Q24, Create).** Agents might include immune cells, pathogens, and damaged tissue cells. Local rules could include chemotaxis up a cytokine gradient, pathogen killing on contact, cytokine release after recognition, and cell death after a lifespan. Emergent outputs include inflammatory focus size, pathogen clearance time, or overshooting tissue damage.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Evaluate the claim: "Because complex systems are unpredictable, modeling them is useless."

<!-- SOLUTION
**Answer (Q25, Evaluation).** The claim is too strong. Complex systems may be hard to predict exactly, but models can identify thresholds, sensitivities, robust qualitative behaviours, and useful intervention points. The goal is often constrained prediction and mechanistic insight, not perfect point forecasting.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Propose a way to detect whether a community pattern is produced by local interactions or by a shared external gradient.

<!-- SOLUTION
**Answer (Q26, Create).** Measure or manipulate the external gradient while also mapping local neighbour effects. If the pattern persists after controlling for the gradient, local interactions are implicated. Transplant, removal, or randomized-neighbour experiments can separate neighbour causation from shared environmental forcing.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. A student says emergence means "anything can happen." Correct this using constraints and repeated patterns.

<!-- SOLUTION
**Answer (Q27, Evaluation).** Emergence does not mean arbitrary outcomes. It means global properties arise from interactions among parts. The outcomes are constrained by rules, geometry, resources, feedback, and history, which is why similar patterns can recur across biofilms, tissues, flocks, and ecosystems.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
28. Build a complex-adaptive explanation of antibiotic resistance that includes mutation, selection, horizontal gene transfer, and clinical practice.

<!-- SOLUTION
**Answer (Q28, Create).** Mutation and horizontal gene transfer generate variation; antibiotic exposure selects resistant variants; hospitals and farms can amplify transmission; incomplete treatment or misuse changes the selection regime. The emergent population-level result is increased resistance prevalence.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
29. Choose one chapter later in the textbook and explain how its topic could be reframed as a complex adaptive system.

<!-- SOLUTION
**Answer (Q29, Create).** Strong examples include immune activation, cancer evolution, microbial ecology, neural circuits, plant hormone networks, or conservation landscapes. A full answer names the agents, interactions, feedback loops, variation, and emergent property.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
30. Design a falsifiable prediction that would distinguish two competing rule sets in an agent-based model of cell migration.

<!-- SOLUTION
**Answer (Q30, Create).** A good prediction identifies a perturbation that makes the rule sets diverge. For example, if one model depends on chemotaxis and another on contact inhibition, flattening the chemical gradient should disrupt directed migration only in the chemotaxis model, whereas changing cell density should mainly affect the contact-inhibition model.
SOLUTION -->

---

*Module: `src/biology/` (general).*
