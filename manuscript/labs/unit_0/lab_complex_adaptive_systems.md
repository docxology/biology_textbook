# Lab B — Complex Adaptive Systems {.unnumbered}

\label{sec:lab_unit_0_complex_adaptive_systems}

*This activity accompanies \cref{sec:unit_0_complex_adaptive_systems} of the textbook — review that chapter before attempting the exercises below.*

**\nameref{sec:unit_0_unit_intro} · Lab B**

---

## Learning Objectives {.unnumbered}

- Simulate a simple agent-based system on paper and observe emergent global behaviour.
- Compute the period of a logistic map for selected reproductive rates and identify the onset of chaos.
- Sketch a phase diagram for a two-basin attractor landscape and reason about tipping points.
- Distinguish *robustness* from *redundancy* using a worked biological example.

---



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO1):** Interpret the supplied evidence or model output for Complex Adaptive Systems.
- **Outcome 2 (LO2):** Identify controls and comparison groups that make the claim testable.
- **Outcome 3 (LO3):** Quantify uncertainty, boundary conditions, or alternative explanations before concluding.
- **Outcome 4 (LO4):** Transfer the mechanism to a new biological case or public-facing decision.
- **Chapter LO coverage:** LO1, LO2, LO3, LO4
- **Rubric dimensions:** evidence; controls; uncertainty; mechanism; transfer.
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Distinguish a positive (reinforcing) feedback loop from a negative (balancing) feedback loop, and give one short biological example of each from the parent chapter.
2. A lake receives steady phosphorus runoff for years with little visible change, then shifts abruptly into a turbid eutrophic state. Apply the idea of a tipping point to explain why a small additional input can drive a large outcome here.
3. Compare a random (Erdős–Rényi) network with a scale-free network in terms of how they respond to the targeted removal of a high-degree node. Which topology tends to be more resilient to random failure, and which is more vulnerable to a directed attack on hubs?

## Background {.unnumbered}

A **complex adaptive system (CAS)** is a population of agents whose collective behaviour emerges from local rules rather than central control. Examples run from neurons in a cortical circuit to ants in a colony to species in an ecosystem. Two mathematical tools recur across scales:

1. **The logistic map** — a discrete-time model $x_{n+1} = r x_n (1 - x_n)$ that passes from stable fixed point → period-2 → period-4 → chaos as the parameter $r$ increases. It captures the essence of bifurcation theory in a single line of algebra.
2. **Phase-space attractor landscapes** — a potential-well picture that shows how systems can occupy alternative stable states with a "tipping point" between them, and how hysteresis delays recovery.

This lab is paper-based; a calculator and graph paper are the only tools needed.

---

## Pre-Lab (to complete before class) {.unnumbered}

1. Write down the logistic map and draw its form for $0 \le x \le 1$, $r = 2.5$. Mark the intersection with the identity line $x_{n+1} = x_n$ — the fixed point.
2. Briefly define: **attractor**, **bifurcation**, **hysteresis**, **self-organised criticality**.
3. Bring three examples of bistable biological systems to class (for Part 3 discussion).

---

## Paper-Based Materials {.unnumbered}

- Graph paper (2 sheets per student).
- Calculator.
- Coloured pens.
- Worksheet with a blank logistic-map table and a blank phase landscape.

---

## Paper-Based Investigation {.unnumbered}

### Part 1 — The Logistic Map by Hand {.unnumbered}

1. Starting from $x_0 = 0.2$, compute 20 iterations of the logistic map for each of these $r$ values: $r = 2.5,\; 3.2,\; 3.5,\; 3.8$.
2. For each $r$, plot $x_n$ against iteration number $n$ on the same axes (use a different colour for each $r$).
3. Identify the long-term behaviour: fixed point, period-2, period-4, or chaotic.
4. Bonus: compute $x_{100}$ for $r = 3.8$ with $x_0 = 0.2$ and $x_0 = 0.20001$. How different are they? Relate to "sensitive dependence on initial conditions."

### Part 2 — Attractor Landscape and Tipping Points {.unnumbered}

A shallow lake has two alternative stable states: **clear** (low algae, clear water) and **turbid** (high algae, murky). Phosphorus loading $P$ shifts which state is stable.

1. Sketch the potential landscape $U(A)$ (where $A$ = algal biomass) for three values of $P$: low (primarily clear is stable), intermediate (both states stable), and high (primarily turbid is stable).
2. Mark the **tipping point** ($P_1$) where the clear state loses stability as $P$ increases.
3. Mark the **restoration point** ($P_2$) where the turbid state loses stability as $P$ decreases.
4. Compare $P_1$ and $P_2$ — which is smaller? This gap is the hysteresis loop and explains why eutrophication is hard to reverse.

### Part 3 — Robustness Versus Redundancy {.unnumbered}

Consider the mammalian immune system as a CAS. It has five categories of robustness:

- **Redundancy** — multiple B-cell clones specific to the same antigen.
- **Degeneracy** — T- and B-cells with overlapping but distinct function.
- **Modularity** — innate vs. adaptive compartments.
- **Negative feedback** — regulatory T cells suppress overactive responders.
- **Diversity** — V(D)J recombination generates ~$10^{11}$ receptor sequences.

1. For each category, give one concrete example from the immune system.
2. Then list one *fragility* that the same architectural feature introduces. (E.g., immune redundancy also means multiple places autoimmunity can arise.)
3. Discuss in your group: would a maximally robust system also be maximally evolvable?

---

## Data Tables {.unnumbered}

| Iteration $n$ | $x_n$ at $r=2.5$ | $x_n$ at $r=3.2$ | $x_n$ at $r=3.5$ | $x_n$ at $r=3.8$ |
| ------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| 0 | 0.2 | 0.2 | 0.2 | 0.2 |
| 1 | | | | |
| … | | | | |
| 20 | | | | |

Long-term regime at each $r$: $r=2.5$: ___, $r=3.2$: ___, $r=3.5$: ___, $r=3.8$: ___.

| CAS property | Immune-system example | Associated fragility |
| ------------ | --------------------- | -------------------- |
| Redundancy | | |
| Degeneracy | | |
| Modularity | | |
| Negative feedback | | |
| Diversity | | |

---

<!-- lab-evidence-checklist-start -->
## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Explore how small rule changes alter collective behaviour.
- **Data skill to practice:** Distinguish deterministic trends from stochastic variation in repeated simulations.
- **BioSkills emphasis:** Modeling and simulation, Process of science, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.
<!-- lab-evidence-checklist-end -->

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Complex Adaptive Systems** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: Here the reproducibility pass turns on the logistic-map iteration and the hysteresis-loop dataset: record the exact value of $r$ and the seed/initial condition for every trajectory, and for the tipping-point loop note which branch (clear-water versus turbid) you read and the phosphorus level at which the jump occurred, since a different starting point silently changes the conclusion. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Worked Example {.unnumbered}

**Problem:** A small quorum-sensing study models 5 bacterial cells as nodes in a graph. The undirected edges (signalling pairs) are: A–B, A–C, B–C, B–D, C–D, D–E. Compute the local clustering coefficient at node B and the average path length between A and E. Local clustering coefficient at a node is C_i = 2·(triangles through i) / (k_i · (k_i − 1)), where k_i is that node's degree.

**Solution:**

- Degree of B = 3 (neighbours A, C, D).
- Pairs of B's neighbours = 3 (A–C, A–D, C–D). Of these, the edges actually present in the graph are A–C and C–D — that is 2 triangles through B.
- Local clustering at B = (2 × 2) / (3 × 2) = 4 / 6 ≈ 0.667.
- Shortest path A → E: A–C–D–E has length 3; A–B–D–E also has length 3. So the path length between A and E is 3 edges.

**Interpretation:** A clustering coefficient near 0.67 at node B indicates that most of B's signalling partners also signal with each other — a hallmark of locally cohesive community structure that supports stigmergic coordination (cells can corroborate signals through redundant local links). The path length of 3 between the most-distant pair shows that even in this tiny graph, signal propagation requires intermediate relays; longer paths in a real biofilm slow the global response and contribute to threshold-like collective behaviour.


## Analysis Questions {.unnumbered}

1. The logistic map transitions from periodic to chaotic behaviour as $r$ passes through the Feigenbaum point (~3.57). Why does this transition occur even though the underlying equation is completely deterministic?
2. In Part 2, you drew a hysteresis loop. Why can reducing $P$ to the level *at which* eutrophication occurred fail to restore the clear-water state? What mechanism sustains the turbid attractor?
3. Power-law distributions appear in earthquake magnitudes, neural avalanches, and extinction events. What common CAS mechanism could explain this shared pattern?
4. Cancer has been described as a "failed CAS" where normal tissue homeostasis breaks down. Identify two CAS features that go wrong in malignancy.
5. Propose a paper simulation or card-based experiment using a bacterial-biofilm model to demonstrate one CAS principle (e.g., stigmergic self-organisation, threshold transitions, or robustness to perturbation). Describe the set-up, observable, and expected result.

## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A shallow coastal estuary has shown gradually declining seagrass cover for a decade while nutrient inflow has risen. Recent surveys detect an abrupt loss of the remaining seagrass and a switch to a phytoplankton-dominated turbid state.
>
> (a) Relate the bistability you explored in Part 2's hysteresis loop to this estuary's observed regime shift. What ecological feedback would sustain the phytoplankton-dominated attractor once the system flipped, and how does that connection to bistability change the kind of restoration target a manager should set?
> (b) Predict the qualitative outcome of two interventions: a sharp reduction of nutrient inflow back to historical levels, and the same reduction combined with mechanical removal of phytoplankton biomass to seed seagrass regrowth. Justify the contrast in expected outcomes using the language of attractors, basin depth, and perturbation magnitude.
> (c) Design a short monitoring programme (three measurable variables and one statistical early-warning signal, such as rising variance or increased autocorrelation in nutrient or chlorophyll time series) that would detect whether a partly recovered estuary is approaching another tipping point before the visible regime shift occurs.

---

## Discussion Questions {.unnumbered}

1. The SARS-CoV-2 pandemic generated striking geographic and temporal heterogeneity. Which features of a CAS (noise, nonlinearity, network topology) explain the emergence of variants?
2. Is a single cell a CAS? Defend or refute using at least three of the \cref{sec:unit_0_complex_adaptive_systems} criteria.
3. What additional scientific ingredients would be needed to "build life from scratch" in a synthetic CAS? What does the field of synthetic biology currently get right, and what do its failures reveal about the difficulty of engineering life?

---

## Safety and Ethics Notes {.unnumbered}

Paper-based lab — no reagents, no risk. Discussion of SARS-CoV-2 should be current-affairs aware; respect divergent lived experiences of the pandemic. Discussion of cancer as a "failed CAS" should be framed carefully if anyone in the class has personal experience — use the system-level language, not the blame-oriented "cancer cells are selfish" framing.

*Module: `src/biology/ecology/ecology.py` (`logistic_growth`, `lotka_volterra`); `src/biology/evolution/evolution.py` (`simulate_drift`).*
