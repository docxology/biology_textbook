# Questions — Active Inference and the Free Energy Principle {#sec:q_unit_0_active_inference .unnumbered}


*This activity accompanies \cref{sec:unit_0_active_inference} of the textbook — review that chapter before attempting the exercises below.*

---

## Recall Questions (1 mark each) {.unnumbered}

<!-- question-coverage-start -->
## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Calculate a posterior belief and explain what action would reduce uncertainty or restore a set point.
- **Model/data emphasis:** Bayesian belief updating and expected-free-energy-style policy comparison.
- **Assessment alignment:** Questions and Methods, Representing and Describing Data, Argumentation.
- **Misconception probe:** Active inference is not passive prediction; action changes the sensory data that arrive next.
- **Transfer product:** Map prediction-error reasoning onto chemotaxis, thermoregulation, and attention.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.
<!-- question-coverage-end -->

<!-- assess: LO=LO1; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define 'active inference' in your own words and provide a biological example.

<!-- SOLUTION
**Answer (Q1, Recall).** Active inference is the behavioral corollary of the free energy principle: an agent minimizes expected free energy (sensory surprise) not only by updating its internal generative model to fit data (perception) but by *acting* to make sensory data match its predictions about preferred states. Biological example: a chemotactic bacterium whose model 'expects' high nutrient acts by modulating tumble frequency so that sensed nutrient rises toward the expected value — fulfilling its predictions rather than merely recording them.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. What distinguishes a complex adaptive system from a simple system?

<!-- SOLUTION
**Answer (Q2, Recall).** A simple system has few components and fixed, predictable input–output relations. A complex adaptive system is a network of many heterogeneous agents that act on local information and adapt, producing emergent, nonlinear, history-dependent behavior that cannot be predicted from any agent alone (e.g., the immune system, an ant colony, an ecosystem). The defining contrast is adaptation and emergence versus fixed, decomposable mechanism.
SOLUTION -->
<!-- assess: LO=LO3; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
3. What is the free energy principle? What does free energy measure?

<!-- SOLUTION
**Answer (Q3, Recall).** The free energy principle (Friston) states that any system that maintains itself far from equilibrium must act and perceive so as to minimize *variational free energy* — an information-theoretic upper bound on sensory surprise. Free energy measures the mismatch between the organism's internal generative model (its predictions) and the sensory data it actually receives; minimizing it keeps the organism within its viable physiological states.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
4. Describe one biological example of negative feedback and one of positive feedback.

<!-- SOLUTION
**Answer (Q4, Recall).** Negative feedback: thermoregulation — a rise in core temperature triggers sweating and vasodilation that return temperature toward the set point (stabilizing). Positive feedback: the rising phase of the action potential — Na⁺ influx depolarizes the membrane, opening more voltage-gated Na⁺ channels and amplifying the depolarization until channels inactivate (self-reinforcing and self-limiting).
SOLUTION -->
<!-- assess: LO=LO5; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
5. What is the difference between homeostasis and allostasis?

<!-- SOLUTION
**Answer (Q5, Recall).** Homeostasis holds a regulated variable near a *fixed* set point through reactive negative feedback. Allostasis (Sterling) achieves stability *through change*: the brain predictively adjusts set points and mobilizes resources in anticipation of demand, so the target itself moves. The decisive difference is reactive constancy versus anticipatory, model-based set-point adjustment.
SOLUTION -->

---

## Application Questions (2 marks each) {.unnumbered}

<!-- assess: LO=LO6; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
6. A drug blocks a key kinase in a signaling cascade, but the tumor eventually regrows. Explain this outcome using the concept of feedback compensation.

<!-- SOLUTION
**Answer (Q6, Application).** Blocking one kinase removes a single edge of a signaling network, but negative-feedback nodes the pathway normally suppresses are de-repressed and parallel routes reroute flux to restore downstream signaling (e.g., loss of ERK-mediated feedback reactivates upstream receptor/PI3K input). The network's redundancy and compensatory feedback restore proliferative output, so single-target inhibition is evaded — which is why combination therapy is often required.
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
**Answer (Q9, Application).** Under active inference an organism acts to fulfil its predictions about preferred, viable states. Infection raises the *expected* (set-point) temperature encoded by the hypothalamic generative model; the body then acts — shivering, vasoconstriction — to realize that prediction because elevated temperature accelerates immune kinetics and impairs pathogen replication. Fever is thus a controlled, model-driven allostatic shift rather than a regulatory failure, adaptive up to its metabolic and tissue-stress costs.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
10. In evolutionary terms, what is niche construction, and how does it relate to the free energy principle?

<!-- SOLUTION
**Answer (Q10, Application).** Niche construction is the organism's modification of its own environment (beaver dams, earthworm-altered soil), changing the selection pressures it and its descendants experience. Under the free energy principle, agents minimize surprise not only by updating internal models (perception) but by acting on the world so it matches their expected states — niche construction is free-energy minimization externalised and inherited across generations, stabilizing the organism–environment fit.
SOLUTION -->

---

## Synthesis Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO3; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
11. Compare and contrast the immune system and an evolving tumor as complex adaptive systems. In each case, identify (a) the agents, (b) the selection pressures, (c) an emergent property, and (d) a critical vulnerability.

<!-- SOLUTION
**Answer (Q11, Synthesis).** Both are populations of heritable, variable, selected agents whose adaptive behavior is emergent. (a) Agents: lymphocyte clones vs tumor subclones. (b) Selection pressures: antigen affinity and self-tolerance vs immune attack, therapy, hypoxia. (c) Emergent property: immunological memory vs collective drug resistance. (d) Critical vulnerability: tolerance breakdown or T-cell exhaustion vs dependence on a driver mutation or shared resource. The decisive contrast: the immune system is selected for host benefit, whereas tumor evolution is selected purely for local proliferative fitness against the host.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
12. A patient with chronic anxiety has persistent overactivation of the sympathetic nervous system even in the absence of objective threat. Using predictive coding and active inference, construct a mechanistic account of how prior beliefs about threat might drive this pattern. How might therapeutic interventions (CBT, interoceptive exposure) alter the generative model?

<!-- SOLUTION
**Answer (Q12, Synthesis).** A precise prior predicting threat makes the generative model expect high interoceptive arousal; because that prior is weighted as highly precise, it dominates weaker sensory evidence, and prediction errors are resolved by *active* inference — driving sympathetic output to make the body match the 'danger' prediction, sustaining arousal with no external threat. CBT and interoceptive exposure reduce the precision of the threat prior and increase the weighting of disconfirming interoceptive evidence, reshaping the generative model so predictions no longer demand sympathetic activation.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
13. Describe how ecosystem collapse (e.g., coral bleaching, fishery collapse) can be framed as a phase transition in a complex adaptive system. What warning signals might precede the transition? Why is recovery often much harder than the original decline?

<!-- SOLUTION
**Answer (Q13, Synthesis).** A reef or fishery near a bifurcation has a shallow basin of attraction; a small additional forcing (warming, harvest pressure) pushes it across a tipping point into an alternative stable state (algal-dominated reef, collapsed stock). Early-warning signals are signatures of *critical slowing down* — rising variance, increased autocorrelation, and slower recovery from small disturbances. Recovery is hard because of hysteresis: feedbacks that stabilize the new state (macroalgal dominance, recruitment failure) mean the driver must fall far below the original threshold before the system flips back.
SOLUTION -->

## Data and Model Interpretation Questions (3 marks each) {.unnumbered}

<!-- assess: LO=LO6; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
14. A prior predicts body temperature should be 37.0 degrees C, but sensory data report 36.2 degrees C with low uncertainty. Predict whether belief updating or action is more likely to reduce prediction error, and justify your answer.

<!-- SOLUTION
**Answer (Q14, Analysis).** Low sensory uncertainty gives the observation high precision, so the organism should update its belief that it is cold and act to restore temperature. Actions might include shivering, vasoconstriction, or seeking warmth. If the sensory data were low precision, belief updating would be weaker and the prior would dominate.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Apply; difficulty=Application; format=short-answer; minutes=4 -->
15. Explain the difference between prediction error and surprise in an active-inference account.

<!-- SOLUTION
**Answer (Q15, Analysis).** Prediction error is the mismatch between predicted and observed sensory data. Surprise is the improbability of the observation under the model. Free-energy-style objectives use tractable bounds on surprise, weighted by precision, to guide belief updating and action.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. A patient with panic disorder interprets benign heart-rate increases as evidence of danger. Identify the prior, the sensory evidence, and the prediction-error loop.

<!-- SOLUTION
**Answer (Q16, Application).** The prior is that bodily arousal predicts threat. The sensory evidence is interoceptive input such as increased heart rate. The loop arises when threat interpretation increases sympathetic arousal, which produces more interoceptive evidence that seems to confirm danger.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. Compare homeostasis and allostasis from an active-inference perspective.

<!-- SOLUTION
**Answer (Q17, Analysis).** Homeostasis emphasizes correction around a regulated variable after deviation. Allostasis emphasizes anticipatory regulation: the organism changes physiology in advance of expected demand. Active inference naturally includes both because predictions can drive action before error becomes large.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
18. A chemotactic bacterium tumbles more often when attractant concentration falls. Describe this as action changing future sensory input.

<!-- SOLUTION
**Answer (Q18, Application).** Falling attractant generates prediction error relative to preferred conditions. Tumbling changes direction, sampling a new region of the chemical field. If the new direction increases attractant, future sensory input better matches the organism's preferred state.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. What does it mean to assign high precision to a sensory signal? Give one adaptive and one maladaptive example.

<!-- SOLUTION
**Answer (Q19, Analysis).** High precision means the system treats the signal as reliable and gives it strong influence over belief updating or action. Adaptive examples include attending to pain when tissue damage is likely. Maladaptive examples include over-weighting benign interoceptive sensations during anxiety.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. A model predicts that reducing sensory precision should reduce self-generated tickle sensations. Explain why.

<!-- SOLUTION
**Answer (Q20, Analysis).** Self-generated movement is predicted by motor commands, so the resulting sensory input has lower precision or is attenuated. Reducing precision prevents ordinary self-produced sensations from being treated as surprising external events. If attenuation fails, self-generated sensations can feel unexpectedly salient.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
21. Explain why active inference is not the same as reinforcement learning, even though both can describe adaptive behavior.

<!-- SOLUTION
**Answer (Q21, Analysis).** Reinforcement learning often frames behavior as maximizing expected reward through value learning. Active inference frames behavior as minimizing expected uncertainty and prediction error under preferred states. Both can select adaptive actions, but active inference emphasizes generative models, precision, and epistemic information seeking.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
22. Use active inference to explain why inflammation can be both protective and harmful.

<!-- SOLUTION
**Answer (Q22, Application).** Inflammation can be protective because it changes tissue conditions to control infection and repair damage. It becomes harmful when the model or feedback loop keeps inflammatory action active after the threat is gone, or when the response creates tissue damage that generates further danger signals.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
23. A generative model predicts predator risk from smell and sound. If smell is blocked, what should happen to reliance on sound, and what experiment would test this?

<!-- SOLUTION
**Answer (Q23, Application).** If smell becomes unavailable or low precision, the organism should rely more heavily on sound if sound remains informative. Test this by manipulating olfactory access and measuring orienting, freezing, or avoidance responses to controlled sound cues while holding predator risk constant.
SOLUTION -->

## Evaluation and Design Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Synthesis; format=short-answer; minutes=7 -->
24. Design a behavioral experiment to test whether interoceptive precision differs between anxious and non-anxious participants.

<!-- SOLUTION
**Answer (Q24, Create).** A strong design measures heartbeat detection, breathing-load detection, or confidence-calibrated interoceptive tasks in both groups. It should include objective performance, confidence, symptom measures, and a control sensory task. A prediction is that anxious participants overweight or miscalibrate interoceptive signals, especially under uncertainty.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Evaluate the claim: "Active inference explains everything, so it explains nothing."

<!-- SOLUTION
**Answer (Q25, Evaluation).** The concern is valid if the framework is used only metaphorically. It becomes scientifically useful when it produces falsifiable generative models, explicit priors, precision assumptions, and predictions that differ from alternative models. The answer should separate broad framework from testable implementation.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Propose an active-inference account of placebo analgesia.

<!-- SOLUTION
**Answer (Q26, Create).** Placebo cues can change priors about expected pain relief and alter the precision assigned to nociceptive signals. Descending control may reduce the impact of pain prediction errors. A test would compare pain ratings and physiological markers under deceptive, open-label, and no-treatment conditions.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. A clinician wants to reduce chronic dyspnea by changing primarily lung mechanics. Use active inference to explain why cognitive or interoceptive therapy might also help.

<!-- SOLUTION
**Answer (Q27, Evaluation).** Dyspnea is not only airflow; it is inferred from sensory signals, priors, attention, and precision. Therapy that recalibrates threat priors or interoceptive precision may reduce perceived breathlessness even when lung mechanics change little. This does not deny physiology; it adds model-based interpretation.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
28. Build an active-inference explanation of immune tolerance.

<!-- SOLUTION
**Answer (Q28, Create).** Immune tolerance can be framed as a learned model that treats self-antigens and harmless contexts as expected, low-threat states. Regulatory cells, deletion, anergy, and checkpoint signaling reduce precision or action toward those cues. Autoimmunity can result when the system assigns threat to self-associated evidence.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
29. Compare an organism seeking food and a scientist designing an experiment as epistemic agents.

<!-- SOLUTION
**Answer (Q29, Analysis).** Both act to sample informative states. The organism moves to reduce uncertainty about food location while satisfying metabolic preferences. The scientist manipulates conditions to reduce uncertainty among hypotheses. The goals, representations, and ethics differ, but both use action to gather better evidence.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=9 -->
30. Choose one later textbook topic and formulate an active-inference version of its central mechanism.

<!-- SOLUTION
**Answer (Q30, Create).** Good choices include glucose regulation, plant tropisms, infection response, synaptic plasticity, or conservation decision-making. A complete answer names preferred states, sensory evidence, priors, actions, precision assumptions, and one prediction that would distinguish the active-inference framing from a simpler feedback model.
SOLUTION -->

---

*Module: `src/biology/` (general).*
