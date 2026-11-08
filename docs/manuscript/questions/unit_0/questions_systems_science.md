# Questions — Systems Science and Emergence {#sec:q_unit_0_systems_science .unnumbered}


## Questions 1–10 {.unnumbered}

*This activity accompanies \cref{sec:unit_0_systems_science} of the textbook — review that chapter before attempting the exercises below.*

---

## Foundational comparisons {.unnumbered}

## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Given a biological scenario, identify the system boundary, feedback loop, and missing measurement.
- **Model/data emphasis:** Box-and-arrow causal models with explicit inputs, outputs, and feedback signs.
- **Assessment alignment:** Questions and Methods, Representing and Describing Data, Argumentation.
- **Misconception probe:** A system is not just a list of parts; the interactions are part of the explanation.
- **Transfer product:** Apply the same feedback map to a cell, organism, and ecosystem, then name what changes at each scale.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.

<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define 'systems science' in your own words and provide a biological example.

<!-- SOLUTION
**Answer (Q1, Recall).** Systems science studies how the *organization of and interactions among* components — not the components in isolation — generate the behavior of a whole; it makes the boundary, components, environment, flows, and feedback signs explicit. Biological example: blood-glucose regulation, where pancreas, insulin, glucagon, liver, and muscle form a feedback network whose stable set-point behavior cannot be read off any single hormone.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
2. Distinguish a component, an interaction and a boundary using a mitochondrion.

<!-- SOLUTION
**Answer (Q2, Recall).** An ATP synthase is a component; proton flow coupled to its rotation is an interaction; the outer membrane can define an organelle boundary, with metabolites crossing it. A boundary must match the question, not imply isolation.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
3. Why is a Hill response with coefficient n=4 nonlinear but not by itself bistable?

<!-- SOLUTION
**Answer (Q3, Recall).** Occupancy is a nonlinear rational function of ligand and is single-valued at every concentration. Bistability requires two stable states under identical inputs and a feedback/dynamical mechanism; steepness alone is insufficient.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
4. Describe one biological example of negative feedback and one of positive feedback.

<!-- SOLUTION
**Answer (Q4, Recall).** Negative feedback: thermoregulation — a rise in core temperature triggers sweating and vasodilation that return temperature toward the set point (stabilizing). Positive feedback: the rising phase of the action potential — Na⁺ influx depolarizes the membrane, opening more voltage-gated Na⁺ channels and amplifying the depolarization until channels inactivate (self-reinforcing and self-limiting).
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
5. Distinguish feedback from feed-forward using insulin regulation.

<!-- SOLUTION
**Answer (Q5, Recall).** Glucose-triggered insulin is feedback because the regulated variable initiates correction; meal-cue-triggered secretion is feed-forward because it anticipates the rise. Both can coexist; feed-forward is not evidence that feedback is absent.
SOLUTION -->

---

## Mechanisms and applications {.unnumbered}

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
6. A drug blocks a key kinase in a signaling cascade, but the tumor eventually regrows. Explain this outcome using the concept of feedback compensation.

<!-- SOLUTION
**Answer (Q6, Application).** Blocking one kinase removes a single edge of a signaling network, but negative-feedback nodes the pathway normally suppresses are de-repressed and parallel routes reroute flux to restore downstream signaling (e.g., loss of ERK-mediated feedback reactivates upstream receptor/PI3K input). The network's redundancy and compensatory feedback restore proliferative output, so single-target inhibition is evaded — which is why combination therapy is often required.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
7. Under what conditions can the lac regulatory network be bistable? Compare a possible benefit of history-dependent memory with a cost of delayed switching, and explain why a graded response need not be linear.

<!-- SOLUTION
**Answer (Q7, Application).** LacY-mediated inducer uptake can reinforce operon expression, but bistability depends on inducer, growth conditions, feedback strength and regulatory parameters. Evidence is two stable expression states at the same input and history-dependent switching, not a Hill sigmoid alone. Such memory can buffer fluctuations; it can also delay adaptation when conditions change. A graded response need not be linear. Fitness benefits require a defined environmental comparison and measurements, not memory alone \citep{zander2017lac,julou2020lacfitness}.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
8. A developmental module has three cell types that exchange growth signals. Explain one emergent behavior and a measurement that distinguishes it from isolated-cell growth.

<!-- SOLUTION
**Answer (Q8, Application).** A spatial growth boundary can arise from reciprocal inhibition among types. Compare mixed culture with equal-density isolated cultures and measure proliferation versus position. Matching bulk growth alone cannot establish the proposed interaction mechanism.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
9. For theta=L^n/(K^n+L^n), calculate occupancy at L=K and L=2K for n=1 and n=4.

<!-- SOLUTION
**Answer (Q9, Application).** At K both give 0.5. At 2K, n=1 gives 2/3 and n=4 gives 16/17=0.9412. The steeper response changes sensitivity, not the number of equilibria. Award one calculation component per ligand condition.
SOLUTION -->
<!-- assess: LO=LO8; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
10. A chemostat has dilution D=0.20 h^-1 and microbial growth mu(S)=0.6S/(2+S) h^-1, with S in mM. Find the nonwashout steady substrate level.

<!-- SOLUTION
**Answer (Q10, Application).** At nonzero steady biomass mu=D. Thus 0.20(2+S)=0.6S, giving S=1 mM. This requires feed substrate above 1 mM and positive biomass; it does not prove the equilibrium is attainable for every feed.
SOLUTION -->

---

## Integrated reasoning {.unnumbered}

## Questions 11–20 {.unnumbered}

<!-- assess: LO=LO8; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
11. For x prime=-0.5x with x(0)=8 mM above a zero reference, calculate x(2 min) and the half-time.

<!-- SOLUTION
**Answer (Q11, Application).** x(2)=8 exp(-1)=2.943 mM and half-time=ln2/0.5=1.386 min. This is a continuous linear relaxation with no delay, not a delayed oscillator.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
12. For x prime=-kx(t-tau), tau=10 s, find the first instability threshold and onset period. What is not established above threshold?

<!-- SOLUTION
**Answer (Q12, Application).** kcrit=pi/(2tau)=0.1571 s^-1; period=4tau=40 s. Linear instability yields growing deviations, not a bounded stable cycle. Nonlinear dynamics and a physiological fit are needed to establish the latter.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
13. A network has many low-degree nodes and three hubs. Design evidence needed before calling it scale-free.

<!-- SOLUTION
**Answer (Q13, Synthesis).** Record the full degree distribution and sampling procedure; fit a power-law tail with a stated cutoff and compare alternatives such as lognormal tails using held-out or goodness-of-fit checks. Hubs alone establish heterogeneity, not a unique power law. Credit data, competing model, fit criterion and limitation separately.
SOLUTION -->

## Data and Model Interpretation Questions (3 marks each) {.unnumbered}

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
14. A homeostatic variable is measured at 98, 101, 105, 112, and 130 units after a perturbation. Identify whether the response appears damped, amplified, or unstable, and name one missing measurement needed before drawing a systems-level conclusion.

<!-- SOLUTION
**Answer (Q14, Application).** The sequence is moving away from the original range rather than returning toward it, so the first interpretation is an amplified or unstable response. A full answer should ask for at least one missing measurement such as the set point, sampling interval, perturbation size, feedback gain, or whether the response later plateaus. Without the time scale and set point, the same numbers could represent transient compensation, runaway positive feedback, or a new stable state.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
15. Draw a signed feedback diagram for blood glucose regulation that includes glucose, insulin, glucagon, liver glycogen breakdown, and muscle glucose uptake. Which links are negative feedback links?

<!-- SOLUTION
**Answer (Q15, Application).** Blood glucose increases insulin secretion; insulin increases muscle glucose uptake and liver glycogen synthesis, both of which lower blood glucose. Blood glucose falling increases glucagon secretion; glucagon increases liver glycogen breakdown and gluconeogenesis, which raises blood glucose. The negative feedback links are the pathways by which high glucose triggers insulin-mediated glucose lowering and low glucose triggers glucagon-mediated glucose raising.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. In a predator-prey system, prey abundance rises first, predator abundance rises after a delay, and prey then falls. Explain why the delay matters for oscillation rather than immediate stabilization.

<!-- SOLUTION
**Answer (Q16, Application).** A delayed predator response can peak after prey have begun declining, allowing overshoot. Whether oscillations decay, grow or form a bounded cycle depends on the specified growth, predation, delay and limiting terms. A sufficiently large gain-delay product can destabilize an explicit delayed negative-feedback model, but does not by itself prove a stable predator-prey cycle.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. A pathway has two parallel routes from receptor activation to transcription. Blocking one route reduces output by 20%. What systems property explains this robustness, and what experiment would test it?

<!-- SOLUTION
**Answer (Q17, Application).** Parallel routes create redundancy and distributed control, so flux or signal output does not depend on one route alone. Test this by inhibiting each route separately and together, then measuring the transcriptional output. A synergistic drop under dual inhibition would support pathway compensation.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. A network diagram has many nodes with two links and three nodes with hundreds of links. What kind of network does this suggest, and why is it robust to random node loss but vulnerable to targeted hub loss?

<!-- SOLUTION
**Answer (Q18, Application).** This suggests a scale-free or heavy-tailed network. Random removal usually hits low-degree nodes, so global connectivity is preserved. Targeting hubs removes many paths at once, fragmenting the network and causing disproportionate functional loss.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. A cell-fate model has two stable attractors, A and B. A weak transient signal moves the cell partway toward B, but it returns to A; a stronger signal switches it to B permanently. Explain this in terms of basins of attraction.

<!-- SOLUTION
**Answer (Q19, Application).** Each attractor has a basin: states inside that basin flow back to the attractor after small perturbations. The weak signal stays inside A's basin, so the cell returns to A. The stronger signal crosses the separatrix into B's basin, so the dynamics carry the cell toward B even after the signal ends.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
20. A researcher reports that deleting one enzyme in a pathway has no phenotype, so the enzyme is unimportant. Critique this conclusion using compensation and context dependence.

<!-- SOLUTION
**Answer (Q20, Synthesis).** No phenotype under one condition does not prove no function. Parallel pathways, stored metabolites, regulatory compensation, or a benign test environment can mask the enzyme's role. A stronger design would test multiple stresses, time points, genetic backgrounds, and combined perturbations.
SOLUTION -->

## Questions 21–30 {.unnumbered}

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
21. A negative feedback loop has a sensor that saturates at high input values. Predict what happens when the input exceeds the sensor's dynamic range.

<!-- SOLUTION
**Answer (Q21, Application).** Once the sensor saturates, increases in input no longer produce proportionally larger corrective signals. The system may appear stable over moderate inputs but fail abruptly outside its measurable range. This is why receptor saturation, assay saturation, and physiological reserve must be distinguished.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
22. Explain how modularity can make a system both more evolvable and more fragile.

<!-- SOLUTION
**Answer (Q22, Application).** Modularity localizes change: one module can vary without destroying every other function, which supports evolvability. The same architecture can be fragile at module interfaces or shared hubs, because disrupting a connector can isolate otherwise functional modules.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
23. Compare a thermostat, blood calcium regulation, and quorum sensing. Which parts of the analogy are useful, and where does the analogy break down?

<!-- SOLUTION
**Answer (Q23, Application).** The thermostat analogy is useful for set point, sensor, comparator, and effector logic. Blood calcium adds multiple organs, hormones, and time scales. Quorum sensing adds population-level communication and threshold-like collective behavior. The analogy breaks down when biological systems change their own sensors, set points, and effectors through development, learning, or evolution.
SOLUTION -->

## Evaluation and Design Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO2; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
24. Design a minimal experiment to distinguish direct causation from correlation in a proposed feedback loop between a hormone and a behavior.

<!-- SOLUTION
**Answer (Q24, Synthesis).** A strong design manipulates the hormone while measuring behavior, includes vehicle and sham controls, and ideally blocks the receptor to test specificity. Time-resolved measurements should show that hormone change precedes behavioral change. A rescue condition, such as restoring receptor signaling, would strengthen causal inference.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. A model of fever treats body temperature as a fixed set point. Evaluate why this model fails during infection and propose a better systems description.

<!-- SOLUTION
**Answer (Q25, Synthesis).** During infection, cytokines and prostaglandins alter the regulated target temperature, so fever is not simply failure to maintain 37 degrees C. A better model includes a context-sensitive set point, immune signals, heat-production effectors, heat-loss effectors, and costs such as metabolic demand or tissue damage.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Propose two early-warning indicators that a lake ecosystem is approaching a tipping point. Explain why each indicator is mechanistically plausible.

<!-- SOLUTION
**Answer (Q26, Synthesis).** Plausible indicators include critical slowing down after small disturbances, rising variance in algal biomass, increasing autocorrelation, declining water clarity, or rapid nutrient pulses. They are plausible because systems near a tipping point recover more slowly and fluctuate more strongly before switching states.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. A clinician wants a single biomarker for sepsis severity. Use systems thinking to argue for or against relying on one marker.

<!-- SOLUTION
**Answer (Q27, Synthesis).** A single marker is easy to measure but risky because sepsis is a multi-organ, multi-feedback syndrome. Lactate, cytokines, blood pressure, renal function, and mental status capture different parts of the system. A panel plus trajectory over time is more reliable than one static value.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
28. Build a modular explanation of wound healing with at least three modules and one feedback link between modules.

<!-- SOLUTION
**Answer (Q28, Synthesis).** One modular explanation includes hemostasis, inflammation, tissue proliferation, and remodeling. Inflammation recruits immune cells and growth factors that stimulate proliferation; excessive inflammation feeds back negatively by delaying remodeling and can create chronic wounds. The answer should identify modules, links, and at least one measurable output such as collagen deposition or wound area.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
29. A student says, "If we know every molecule in a cell, we know the cell." Respond using emergence, scale, and model choice.

<!-- SOLUTION
**Answer (Q29, Synthesis).** Knowing every molecule is not enough unless interactions, spatial organization, time scales, and boundary conditions are also known. Emergent properties such as oscillation, polarity, and fate commitment arise from relations among parts. The appropriate model depends on the question: molecular detail for catalysis, network detail for signaling, and coarse-grained variables for tissue behavior.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
30. Choose one biological system from another unit of the textbook and outline how you would model it as a system with state variables, inputs, outputs, and feedback.

<!-- SOLUTION
**Answer (Q30, Synthesis).** One keyed example is glucose regulation: states are plasma glucose and circulating insulin; a meal is an input and measured glucose/insulin trajectories are outputs (1). Glucose stimulates insulin, which increases uptake and suppresses hepatic output, closing a negative loop (1). Compare a matched meal with and without an uptake perturbation and fit a clearance/response-time parameter from serial measurements (1). Tissue heterogeneity and secretion delay limit a one-compartment model (1). Alternative systems earn credit for equally concrete variables, signed links, evidence and limitations; see \cref{sec:unit_0_systems_science}.
SOLUTION -->

---

*Module: `src/biology/` (general).*
