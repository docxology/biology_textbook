# Questions — Ch 0.1: Systems Science and the Logic of Emergence {.unnumbered}

\label{sec:q_unit_0_systems_science}

*This activity accompanies \cref{sec:unit_0_systems_science} of the textbook — review that chapter before attempting the exercises below.*

---

## Recall Questions (1 mark each) {.unnumbered}

<!-- question-coverage-start -->
## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Given a biological scenario, identify the system boundary, feedback loop, and missing measurement.
- **Model/data emphasis:** Box-and-arrow causal models with explicit inputs, outputs, and feedback signs.
- **Assessment alignment:** Questions and Methods, Representing and Describing Data, Argumentation.
- **Misconception probe:** A system is not just a list of parts; the interactions are part of the explanation.
- **Transfer product:** Apply the same feedback map to a cell, organism, and ecosystem, then name what changes at each scale.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.
<!-- question-coverage-end -->

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define 'systems science' in your own words and provide a biological example.

<!-- SOLUTION
**Answer (Q1, Recall).** Systems science studies how the *organisation of and interactions among* components — not the components in isolation — generate the behaviour of a whole; it makes the boundary, components, environment, flows, and feedback signs explicit. Biological example: blood-glucose regulation, where pancreas, insulin, glucagon, liver, and muscle form a feedback network whose stable set-point behaviour cannot be read off any single hormone.
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
14. A homeostatic variable is measured at 98, 101, 105, 112, and 130 units after a perturbation. Identify whether the response appears damped, amplified, or unstable, and name one missing measurement needed before drawing a systems-level conclusion.

<!-- SOLUTION
**Answer (Q14, Analysis).** The sequence is moving away from the original range rather than returning toward it, so the first interpretation is an amplified or unstable response. A full answer should ask for at least one missing measurement such as the set point, sampling interval, perturbation size, feedback gain, or whether the response later plateaus. Without the time scale and set point, the same numbers could represent transient compensation, runaway positive feedback, or a new stable state.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
15. Draw a signed feedback diagram for blood glucose regulation that includes glucose, insulin, glucagon, liver glycogen breakdown, and muscle glucose uptake. Which links are negative feedback links?

<!-- SOLUTION
**Answer (Q15, Application).** Blood glucose increases insulin secretion; insulin increases muscle glucose uptake and liver glycogen synthesis, both of which lower blood glucose. Blood glucose falling increases glucagon secretion; glucagon increases liver glycogen breakdown and gluconeogenesis, which raises blood glucose. The negative feedback links are the pathways by which high glucose triggers insulin-mediated glucose lowering and low glucose triggers glucagon-mediated glucose raising.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. In a predator-prey system, prey abundance rises first, predator abundance rises after a delay, and prey then falls. Explain why the delay matters for oscillation rather than immediate stabilization.

<!-- SOLUTION
**Answer (Q16, Analysis).** Delayed negative feedback can overshoot. Predator numbers respond to earlier prey abundance, not the current state, so predation pressure can peak after prey have already begun declining. If the product of feedback gain and delay is large enough, the system cycles instead of returning smoothly to equilibrium.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. A pathway has two parallel routes from receptor activation to transcription. Blocking one route reduces output by 20%. What systems property explains this robustness, and what experiment would test it?

<!-- SOLUTION
**Answer (Q17, Application).** Parallel routes create redundancy and distributed control, so flux or signal output does not depend on one route alone. Test this by inhibiting each route separately and together, then measuring the transcriptional output. A synergistic drop under dual inhibition would support pathway compensation.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. A network diagram has many nodes with two links and three nodes with hundreds of links. What kind of network does this suggest, and why is it robust to random node loss but vulnerable to targeted hub loss?

<!-- SOLUTION
**Answer (Q18, Analysis).** This suggests a scale-free or heavy-tailed network. Random removal usually hits low-degree nodes, so global connectivity is preserved. Targeting hubs removes many paths at once, fragmenting the network and causing disproportionate functional loss.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. A cell-fate model has two stable attractors, A and B. A weak transient signal moves the cell partway toward B, but it returns to A; a stronger signal switches it to B permanently. Explain this in terms of basins of attraction.

<!-- SOLUTION
**Answer (Q19, Analysis).** Each attractor has a basin: states inside that basin flow back to the attractor after small perturbations. The weak signal stays inside A's basin, so the cell returns to A. The stronger signal crosses the separatrix into B's basin, so the dynamics carry the cell toward B even after the signal ends.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. A researcher reports that deleting one enzyme in a pathway has no phenotype, so the enzyme is unimportant. Critique this conclusion using compensation and context dependence.

<!-- SOLUTION
**Answer (Q20, Evaluation).** No phenotype under one condition does not prove no function. Parallel pathways, stored metabolites, regulatory compensation, or a benign test environment can mask the enzyme's role. A stronger design would test multiple stresses, time points, genetic backgrounds, and combined perturbations.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
21. A negative feedback loop has a sensor that saturates at high input values. Predict what happens when the input exceeds the sensor's dynamic range.

<!-- SOLUTION
**Answer (Q21, Analysis).** Once the sensor saturates, increases in input no longer produce proportionally larger corrective signals. The system may appear stable over moderate inputs but fail abruptly outside its measurable range. This is why receptor saturation, assay saturation, and physiological reserve must be distinguished.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
22. Explain how modularity can make a system both more evolvable and more fragile.

<!-- SOLUTION
**Answer (Q22, Analysis).** Modularity localizes change: one module can vary without destroying every other function, which supports evolvability. The same architecture can be fragile at module interfaces or shared hubs, because disrupting a connector can isolate otherwise functional modules.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
23. Compare a thermostat, blood calcium regulation, and quorum sensing. Which parts of the analogy are useful, and where does the analogy break down?

<!-- SOLUTION
**Answer (Q23, Analysis).** The thermostat analogy is useful for set point, sensor, comparator, and effector logic. Blood calcium adds multiple organs, hormones, and time scales. Quorum sensing adds population-level communication and threshold-like collective behaviour. The analogy breaks down when biological systems change their own sensors, set points, and effectors through development, learning, or evolution.
SOLUTION -->

## Evaluation and Design Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
24. Design a minimal experiment to distinguish direct causation from correlation in a proposed feedback loop between a hormone and a behaviour.

<!-- SOLUTION
**Answer (Q24, Create).** A strong design manipulates the hormone while measuring behaviour, includes vehicle and sham controls, and ideally blocks the receptor to test specificity. Time-resolved measurements should show that hormone change precedes behavioural change. A rescue condition, such as restoring receptor signaling, would strengthen causal inference.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. A model of fever treats body temperature as a fixed set point. Evaluate why this model fails during infection and propose a better systems description.

<!-- SOLUTION
**Answer (Q25, Evaluation).** During infection, cytokines and prostaglandins alter the regulated target temperature, so fever is not simply failure to maintain 37 degrees C. A better model includes a context-sensitive set point, immune signals, heat-production effectors, heat-loss effectors, and costs such as metabolic demand or tissue damage.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Propose two early-warning indicators that a lake ecosystem is approaching a tipping point. Explain why each indicator is mechanistically plausible.

<!-- SOLUTION
**Answer (Q26, Create).** Plausible indicators include critical slowing down after small disturbances, rising variance in algal biomass, increasing autocorrelation, declining water clarity, or rapid nutrient pulses. They are plausible because systems near a tipping point recover more slowly and fluctuate more strongly before switching states.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. A clinician wants a single biomarker for sepsis severity. Use systems thinking to argue for or against relying on one marker.

<!-- SOLUTION
**Answer (Q27, Evaluation).** A single marker is easy to measure but risky because sepsis is a multi-organ, multi-feedback syndrome. Lactate, cytokines, blood pressure, renal function, and mental status capture different parts of the system. A panel plus trajectory over time is more reliable than one static value.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
28. Build a modular explanation of wound healing with at least three modules and one feedback link between modules.

<!-- SOLUTION
**Answer (Q28, Create).** One modular explanation includes hemostasis, inflammation, tissue proliferation, and remodeling. Inflammation recruits immune cells and growth factors that stimulate proliferation; excessive inflammation feeds back negatively by delaying remodeling and can create chronic wounds. The answer should identify modules, links, and at least one measurable output such as collagen deposition or wound area.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
29. A student says, "If we know every molecule in a cell, we know the cell." Respond using emergence, scale, and model choice.

<!-- SOLUTION
**Answer (Q29, Evaluation).** Knowing every molecule is not enough unless interactions, spatial organization, time scales, and boundary conditions are also known. Emergent properties such as oscillation, polarity, and fate commitment arise from relations among parts. The appropriate model depends on the question: molecular detail for catalysis, network detail for signaling, and coarse-grained variables for tissue behaviour.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
30. Choose one biological system from another unit of the textbook and outline how you would model it as a system with state variables, inputs, outputs, and feedback.

<!-- SOLUTION
**Answer (Q30, Create).** Examples include membrane potential, glucose regulation, photosynthesis, infection spread, or population growth. A complete answer names state variables, external inputs, measurable outputs, feedback links, and one model limitation. The best answers also identify a parameter that could be estimated from data.
SOLUTION -->

---

*Module: `src/biology/` (general).*
