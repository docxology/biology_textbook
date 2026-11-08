# Questions — Active Inference and Free Energy {#sec:q_unit_0_active_inference .unnumbered}


## Questions 1–10 {.unnumbered}

*This activity accompanies \cref{sec:unit_0_active_inference} of the textbook — review that chapter before attempting the exercises below.*

---

## Foundational comparisons {.unnumbered}

## Instructor Use and Coverage Notes {.unnumbered}

- **Coverage target:** Calculate a posterior belief and explain what action would reduce uncertainty or restore a set point.
- **Model/data emphasis:** Bayesian belief updating and expected-free-energy-style policy comparison.
- **Assessment alignment:** Questions and Methods, Representing and Describing Data, Argumentation.
- **Misconception probe:** Active inference is not passive prediction; action changes the sensory data that arrive next.
- **Transfer product:** Map prediction-error reasoning onto chemotaxis, thermoregulation, and attention.
- **Grading focus:** award full credit for mechanism, evidence, boundary conditions, and units when a calculation is required.
- **Suggested use:** draw one recall item, one application item, and one synthesis item when building a short quiz from this bank.

<!-- assess: LO=LO3; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
1. Define 'active inference' in your own words and provide a biological example.

<!-- SOLUTION
**Answer (Q1, Recall).** Active inference is a modeling framework in which actions are selected using a generative model and preferences for outcomes, with expected free energy potentially combining instrumental and information-seeking terms. Perceptual inference instead updates beliefs given observations. Chemotaxis can be modeled this way, but known receptor/motor feedback is not alone evidence that a bacterium literally represents probabilities.
SOLUTION -->
<!-- assess: LO=LO5; bloom=Remember; difficulty=Recall; format=short-answer; minutes=2 -->
2. Name the four state classes in a Markov-blanket partition.

<!-- SOLUTION
**Answer (Q2, Recall).** Internal and external states are separated conditionally by sensory and active blanket states. Sensory states are influenced by external states; active states influence external states. A proposed biological partition must justify these conditional dependencies, not just draw a membrane.
SOLUTION -->
<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
3. State the variational free-energy identity and its scope.

<!-- SOLUTION
**Answer (Q3, Recall).** F[q,o]=KL(q||p(z|o))-ln p(o), hence F is at least -ln p(o). The FEP is a conditional modeling framework, not a demonstrated requirement that every far-from-equilibrium system literally perceives. F is informational, not Gibbs energy.
SOLUTION -->
<!-- assess: LO=LO7; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
4. What do descending predictions and ascending prediction errors represent in predictive-processing models?

<!-- SOLUTION
**Answer (Q4, Recall).** Descending activity represents predictions of lower-level causes or signals; ascending errors represent discrepancies weighted by precision. This is a proposed computational interpretation, not a universal anatomical assignment of every axon.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
5. What is the difference between homeostasis and allostasis?

<!-- SOLUTION
**Answer (Q5, Recall).** Homeostasis holds a regulated variable near a *fixed* set point through reactive negative feedback. Allostasis (Sterling) achieves stability *through change*: the brain predictively adjusts set points and mobilizes resources in anticipation of demand, so the target itself moves. The decisive difference is reactive constancy versus anticipatory, model-based set-point adjustment.
SOLUTION -->

---

## Mechanisms and applications {.unnumbered}

<!-- assess: LO=LO2; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
6. A Gaussian prior has mean 10 m and variance 4 m^2; observation is 16 m with variance 12 m^2. Calculate posterior mean and variance.

<!-- SOLUTION
**Answer (Q6, Application).** Gain=4/(4+12)=0.25; posterior mean=10+0.25(6)=11.5 m; posterior variance=(1-0.25)4=3 m^2. Variances, not standard deviations, enter these formulas.
SOLUTION -->
<!-- assess: LO=LO2; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
7. Repeat Q6 with observation variance 0.5 m^2 and interpret the change.

<!-- SOLUTION
**Answer (Q7, Application).** Gain=4/4.5=8/9; posterior mean=15.333 m and variance=4/9=0.4444 m^2. More precise evidence moves the posterior closer to the observation and reduces uncertainty; it does not prove the observation is unbiased.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
8. Two policies have risk minus information gain G=R-I: A has R=4,I=1; B has R=2.5,I=3. Calculate G and choose the smaller value.

<!-- SOLUTION
**Answer (Q8, Application).** GA=3 and GB=-0.5, so B is preferred under this explicitly defined illustrative objective. The sign convention matters; numbers in an arbitrary utility scale are not measured neural free energy.
SOLUTION -->
<!-- assess: LO=LO4; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
9. Within an active-inference model of fever, distinguish altered preferred temperature from measured temperature.

<!-- SOLUTION
**Answer (Q9, Application).** Inflammatory signaling can raise a regulated target, after which heat-producing actions reduce the difference from that target. This reframes known physiology; it does not establish that fever requires an explicit generative representation or that all fever is beneficial.
SOLUTION -->
<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
10. A mouse turns its head to locate a faint sound, then revises its estimate of source location. Classify the two operations.

<!-- SOLUTION
**Answer (Q10, Application).** Head turning is epistemic action because it changes the evidence sampled; the subsequent belief revision is perceptual inference. Information seeking is not passive perception simply because its goal is knowledge.
SOLUTION -->

---

## Integrated reasoning {.unnumbered}

## Questions 11–20 {.unnumbered}

<!-- assess: LO=LO1; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
11. For a prior N(37,0.25) and likelihood variance 1, observation 34, compute the evidence bound using 0.5 ln(2pi times 1.25)+(34-37)^2/(2 times 1.25). Can posterior updating yield F=2.1 nats?

<!-- SOLUTION
**Answer (Q11, Application).** The bound is 4.631 nats using a 1 degree C reference interval for densities. KL divergence is nonnegative, so F=2.1 is impossible at this fixed observation under this model. Updating q can reach but not cross the bound.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
12. Evaluate a model attributing anxiety solely to highly precise threat priors. State a discriminating experiment and a competing explanation.

<!-- SOLUTION
**Answer (Q12, Synthesis).** Compare responses to systematically manipulated cue reliability while measuring arousal, choices and confidence against a fitted stimulus-response model. A threat-prior account predicts context-dependent weighting beyond cue reliability alone. Sensor bias or learned avoidance can mimic the pattern; require held-out predictive advantage rather than assuming a clinical mechanism from the metaphor.
SOLUTION -->

<!-- assess: LO=LO5; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
13. Propose sensory, active, internal and external states for bacterial chemotaxis and identify a questionable independence assumption.

<!-- SOLUTION
**Answer (Q13, Application).** Receptor signaling can be sensory, motor output active, intracellular signaling internal and attractant field external. Direct diffusion of a signaling molecule across the chosen boundary may violate the proposed conditional independence. A membrane boundary alone does not validate a Markov blanket.
SOLUTION -->

## Data and Model Interpretation Questions (3 marks each) {.unnumbered}

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
14. A prior predicts body temperature should be 37.0 degrees C, but sensory data report 36.2 degrees C with low uncertainty. Predict whether belief updating or action is more likely to reduce prediction error, and justify your answer.

<!-- SOLUTION
**Answer (Q14, Application).** More precise sensory evidence has greater weight relative to a fixed prior in a Bayesian update, but the preferred action cannot be selected from sensory precision alone. Prior variance, action costs, possible future observations and physiological constraints are also needed. Belief updating can recognize a cold state while warming changes future data; these are different operations.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Understand; difficulty=Recall; format=short-answer; minutes=2 -->
15. Explain the difference between prediction error and surprise in an active-inference account.

<!-- SOLUTION
**Answer (Q15, Recall).** Prediction error is the mismatch between predicted and observed sensory data. Surprise is the improbability of the observation under the model. Free-energy-style objectives use tractable bounds on surprise, weighted by precision, to guide belief updating and action.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
16. A patient with panic disorder interprets benign heart-rate increases as evidence of danger. Identify the prior, the sensory evidence, and the prediction-error loop.

<!-- SOLUTION
**Answer (Q16, Application).** The prior is that bodily arousal predicts threat. The sensory evidence is interoceptive input such as increased heart rate. The loop arises when threat interpretation increases sympathetic arousal, which produces more interoceptive evidence that seems to confirm danger.
SOLUTION -->

<!-- assess: LO=LO4; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
17. Compare homeostasis and allostasis from an active-inference perspective.

<!-- SOLUTION
**Answer (Q17, Application).** Homeostasis emphasizes correction around a regulated variable after deviation. Allostasis emphasizes anticipatory regulation: the organism changes physiology in advance of expected demand. Active inference naturally includes both because predictions can drive action before error becomes large.
SOLUTION -->

<!-- assess: LO=LO3; bloom=Apply; difficulty=Application; format=short-answer; minutes=5 -->
18. A chemotactic bacterium tumbles more often when attractant concentration falls. Describe this as action changing future sensory input.

<!-- SOLUTION
**Answer (Q18, Application).** Falling attractant generates prediction error relative to preferred conditions. Tumbling changes direction, sampling a new region of the chemical field. If the new direction increases attractant, future sensory input better matches the organism's preferred state.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
19. What does it mean to assign high precision to a sensory signal? Give one adaptive and one maladaptive example.

<!-- SOLUTION
**Answer (Q19, Application).** High precision means the system treats the signal as reliable and gives it strong influence over belief updating or action. Adaptive examples include attending to pain when tissue damage is likely. Maladaptive examples include over-weighting benign interoceptive sensations during anxiety.
SOLUTION -->

<!-- assess: LO=LO7; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
20. A model predicts that reducing sensory precision should reduce self-generated tickle sensations. Explain why.

<!-- SOLUTION
**Answer (Q20, Application).** Self-generated movement is predicted by motor commands, so the resulting sensory input has lower precision or is attenuated. Reducing precision prevents ordinary self-produced sensations from being treated as surprising external events. If attenuation fails, self-generated sensations can feel unexpectedly salient.
SOLUTION -->

## Questions 21–30 {.unnumbered}

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
21. Explain why active inference is not the same as reinforcement learning, even though both can describe adaptive behavior.

<!-- SOLUTION
**Answer (Q21, Application).** Reinforcement learning often frames behavior as maximizing expected reward through value learning. Active inference frames behavior as minimizing expected uncertainty and prediction error under preferred states. Both can select adaptive actions, but active inference emphasizes generative models, precision, and epistemic information seeking.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
22. Use active inference to explain why inflammation can be both protective and harmful.

<!-- SOLUTION
**Answer (Q22, Application).** A candidate active-inference account treats inflammation as action toward preferred viable tissue states; persistent danger predictions could be modeled as sustaining action after a threat has resolved. Independently established immune feedback and tissue injury can also explain persistence. Compare explicit quantitative predictions with a simpler cytokine-feedback model; the framework alone proves neither the mechanism nor a treatment.
SOLUTION -->

<!-- assess: LO=LO2; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
23. A generative model predicts predator risk from smell and sound. If smell is blocked, what should happen to reliance on sound, and what experiment would test this?

<!-- SOLUTION
**Answer (Q23, Synthesis).** If smell becomes unavailable or low precision, the organism should rely more heavily on sound if sound remains informative. Test this by manipulating olfactory access and measuring orienting, freezing, or avoidance responses to controlled sound cues while holding predator risk constant.
SOLUTION -->

## Evaluation and Design Questions (4 marks each) {.unnumbered}

<!-- assess: LO=LO8; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
24. Design a behavioral experiment to test whether interoceptive precision differs between anxious and non-anxious participants.

<!-- SOLUTION
**Answer (Q24, Synthesis).** A strong design measures heartbeat detection, breathing-load detection, or confidence-calibrated interoceptive tasks in both groups. It should include objective performance, confidence, symptom measures, and a control sensory task. A prediction is that anxious participants overweight or miscalibrate interoceptive signals, especially under uncertainty.
SOLUTION -->

<!-- assess: LO=LO1; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
25. Evaluate the claim: "Active inference explains everything, so it explains nothing."

<!-- SOLUTION
**Answer (Q25, Synthesis).** The concern is valid if the framework is used only metaphorically. It becomes scientifically useful when it produces falsifiable generative models, explicit priors, precision assumptions, and predictions that differ from alternative models. The answer should separate broad framework from testable implementation.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
26. Propose an active-inference account of placebo analgesia.

<!-- SOLUTION
**Answer (Q26, Synthesis).** Placebo cues can change priors about expected pain relief and alter the precision assigned to nociceptive signals. Descending control may reduce the impact of pain prediction errors. A test would compare pain ratings and physiological markers under deceptive, open-label, and no-treatment conditions.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Evaluate; difficulty=Synthesis; format=short-answer; minutes=8 -->
27. A clinician wants to reduce chronic dyspnea by changing primarily lung mechanics. Use active inference to explain why cognitive or interoceptive therapy might also help.

<!-- SOLUTION
**Answer (Q27, Synthesis).** Dyspnea is not only airflow; it is inferred from sensory signals, priors, attention, and precision. Therapy that recalibrates threat priors or interoceptive precision may reduce perceived breathlessness even when lung mechanics change little. This does not deny physiology; it adds model-based interpretation.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
28. Build an active-inference explanation of immune tolerance.

<!-- SOLUTION
**Answer (Q28, Synthesis).** Immune tolerance can be framed as a learned model that treats self-antigens and harmless contexts as expected, low-threat states. Regulatory cells, deletion, anergy, and checkpoint signaling reduce precision or action toward those cues. Autoimmunity can result when the system assigns threat to self-associated evidence.
SOLUTION -->

<!-- assess: LO=LO6; bloom=Analyze; difficulty=Application; format=short-answer; minutes=5 -->
29. Compare an organism seeking food and a scientist designing an experiment as epistemic agents.

<!-- SOLUTION
**Answer (Q29, Application).** Both act to sample informative states. The organism moves to reduce uncertainty about food location while satisfying metabolic preferences. The scientist manipulates conditions to reduce uncertainty among hypotheses. The goals, representations, and ethics differ, but both use action to gather better evidence.
SOLUTION -->

<!-- assess: LO=LO8; bloom=Create; difficulty=Synthesis; format=short-answer; minutes=8 -->
30. Choose one later textbook topic and formulate an active-inference version of its central mechanism.

<!-- SOLUTION
**Answer (Q30, Synthesis).** One candidate model is glucose regulation: a preferred glucose range supplies a prior preference, interoceptive glucose signals are observations, and feeding or endocrine output are actions (1). Hidden food availability can be represented by a belief distribution with explicit sensory precision (1). An information-seeking variant predicts choosing an informative food cue even before glucose falls, unlike a specified purely reactive controller (1). Compare cue-information conditions at matched energy cost and require improved held-out predictions; the known endocrine mechanism alone does not demonstrate literal inference (1). See \cref{sec:unit_0_active_inference}.
SOLUTION -->

---

*Module: `src/biology/` (general).*
