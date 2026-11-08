# Lab B — Complex Adaptive Systems {#sec:lab_unit_0_complex_adaptive_systems .unnumbered}


*This activity accompanies \cref{sec:unit_0_complex_adaptive_systems} of the textbook — review that chapter before attempting the exercises below.*

**\nameref{sec:unit_0_unit_intro} · Lab B**

---

## Learning Objectives {.unnumbered}

- Simulate a simple agent-based system on paper and observe emergent global behavior.
- Compute the period of a logistic map for selected reproductive rates and identify the onset of chaos.
- Sketch a phase diagram for a two-basin attractor landscape and reason about tipping points.
- Distinguish *robustness* from *redundancy* using a worked biological example.

---



<!-- lab-alignment-start -->
### Alignment and Rubric Map {.unnumbered}

- **Outcome 1 (LO7):** Iterate the discrete logistic map and classify bounded long-term behavior.
- **Outcome 2 (LO4):** Use the two sweep directions to identify hysteresis thresholds.
- **Outcome 3 (LO2):** Update a local-rule card model and compare uncoupled controls.
- **Outcome 4 (LO5):** Transfer a robustness mechanism to an immune-system case with a limitation.
- **Chapter LO coverage:** LO2, LO4, LO5, LO7
- **Rubric dimensions:** 12 points: correct iterations/precision (LO7, 3); sweep-history evidence and threshold bracket (LO4, 3); coupled versus uncoupled control and mechanistic explanation (LO2, 3); immune transfer plus uncertainty about biological scale (LO5, 3).
<!-- lab-alignment-end -->
## Pre-Lab Concept Questions {.unnumbered}

*Answer these before starting the investigation — they activate knowledge from the parent chapter.*

1. Distinguish a positive (reinforcing) feedback loop from a negative (balancing) feedback loop, and give one short biological example of each from the parent chapter.
2. A lake receives steady phosphorus runoff for years with little visible change, then shifts abruptly into a turbid eutrophic state. Apply the idea of a tipping point to explain why a small additional input can drive a large outcome here.
3. Compare a random (Erdős–Rényi) network with a scale-free network in terms of how they respond to the targeted removal of a high-degree node. Which topology tends to be more resilient to random failure, and which is more vulnerable to a directed attack on hubs?

## Lab Context: Complex Adaptive Systems {.unnumbered}

A **complex adaptive system (CAS)** is a population of agents whose collective behavior emerges from local rules rather than central control. Examples run from neurons in a cortical circuit to ants in a colony to species in an ecosystem. Two mathematical tools recur across scales:

1. **The logistic map** — a discrete-time model $x_{n+1} = r x_n (1 - x_n)$ that passes from stable fixed point → period-2 → period-4 → chaos as the parameter $r$ increases. It captures the essence of bifurcation theory in a single line of algebra.
2. **Phase-space attractor landscapes** — a potential-well picture that shows how systems can occupy alternative stable states with a "tipping point" between them, and how hysteresis delays recovery.

This lab is paper-based; a calculator and graph paper are the only tools needed.

---

## Pre-Lab (to complete before class) {.unnumbered}

1. Write down the logistic map and draw its form for $0 \le x \le 1$, $r = 2.5$. Mark the intersection with the identity line $x_{n+1} = x_n$ — the fixed point.
2. Briefly define: **attractor**, **bifurcation**, **hysteresis**, **self-organized criticality**.
3. Use the lake sweep cards below as the bistability example; explain what additional history information a single observation would omit.

---

## Paper-Based Materials {.unnumbered}

- Graph paper (2 sheets per student).
- Calculator.
- Colored pens.
- Printed governance card C1, local-rule and sweep cards below; copy the iteration table and draw your landscape on graph paper.

---

## Paper-Based Investigation {.unnumbered}

### Part 0 — Local Rules and Control {.unnumbered}

Apply the printed five-cell ring rule for three synchronous rounds and compare it with the uncoupled control. Record every state vector before reading the instructor key. These deterministic rounds are not independent biological replicates.

### Part 1 — The Logistic Map by Hand {.unnumbered}

1. Starting from $x_0=0.2$, compute 20 iterations for $r=2.5,3.2,3.5,3.8$. Retain at least six decimal places internally and round displayed values to four decimals; extend the worksheet to one row per iteration.
2. Plot each trajectory against iteration number, distinguishing curves by line style as well as color.
3. Compare the finite trajectory with the key's fixed-point, period-2 and period-4 reference values. Describe the irregular $r=3.8$ case without claiming that 20 iterates prove chaos.
4. Optional calculator extension: iterate to $x_{100}$ for $r=3.8$ with $x_0=0.2$ and $0.20001$, retaining full calculator precision. Report precision and the final difference; rounding can strongly change this long-horizon result.

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
- **Diversity** — receptor rearrangement supplies many distinct antigen-recognition possibilities; this packet does not measure repertoire size.

1. For each category, give one concrete example from the immune system.
2. Then list one *fragility* that the same architectural feature introduces. (E.g., immune redundancy also means multiple places autoimmunity can arise.)
3. Discuss in your group: would a maximally robust system also be maximally evolvable?

---

## Data Tables {.unnumbered}

: Logistic-map iteration worksheet for four reproductive parameters. {#tbl:unit_0_complex_adaptive_systems_part_3_robustness_versus_redundancy}
| Iteration $n$ | $x_n$ at $r=2.5$ | $x_n$ at $r=3.2$ | $x_n$ at $r=3.5$ | $x_n$ at $r=3.8$ |
| ------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| 0 | 0.2 | 0.2 | 0.2 | 0.2 |
| 1 | | | | |
| … | | | | |
| 20 | | | | |

Long-term regime at each $r$: $r=2.5$: ___, $r=3.2$: ___, $r=3.5$: ___, $r=3.8$: ___.

: Immune-system robustness mechanisms and associated fragilities. {#tbl:unit_0_complex_adaptive_systems_part_3_robustness_versus_redundancy_2}
| CAS property | Immune-system example | Associated fragility |
| ------------ | --------------------- | -------------------- |
| Redundancy | | |
| Degeneracy | | |
| Modularity | | |
| Negative feedback | | |
| Diversity | | |

---

## Evidence and Reproducibility Checklist {.unnumbered}

- **Primary evidence goal:** Explore how small rule changes alter collective behavior.
- **Data skill to practice:** Distinguish deterministic trends from stochastic variation in repeated simulations.
- **BioSkills emphasis:** Modeling and simulation, Process of science, Quantitative reasoning.
- **Control logic:** identify at least one positive control, one negative control, or one baseline comparison before interpreting results.
- **Measurement discipline:** record units, uncertainty, sample size, and any discarded observation with a reason.
- **Mechanistic link:** connect one result directly to the parent chapter's big idea before writing the conclusion.
- **Reproducibility check:** state one procedural detail that another group would need in order to reproduce the result.

## Paper-Based Evidence Upgrade {.unnumbered}

Before answering the analysis questions, annotate the paper dataset for
**Complex Adaptive Systems** with a reproducibility pass:

: Evidence and reproducibility decisions for local rules and hysteresis. {#tbl:unit_0_complex_adaptive_systems_part_3_robustness_versus_redundancy_3}
| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: Here the reproducibility pass turns on the logistic-map iteration and the hysteresis-loop dataset: record the exact value of $r$ and the seed/initial condition for every trajectory, and for the tipping-point loop note which branch (clear-water versus turbid) you read and the phosphorus level at which the jump occurred, since a different starting point silently changes the conclusion. Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.

### Source-Governance Checkpoint {.unnumbered}

**Printed governance card C1:** All following cards are deterministic synthetic teaching models, not lake measurements or cell experiments; one trajectory per rule/initial condition, no biological replicates. Record r, x0, rounding and sweep history. A short irregular trajectory alone does not establish chaos. Refresh the model if immigration, noise or variable loading is added.

**Local-rule cards (Part 0):** Place five cells in a ring, initial states A–E=(1,1,0,0,0). Synchronously set each next state to 1 if at least one of its two neighbors is 1; otherwise set it to 0. Update three rounds. Negative-coupling control: each cell simply keeps its own state. All states are dimensionless. The coupled first round is (1,1,1,0,1), second (1,1,1,1,1), third all 1; the control remains (1,1,0,0,0). Local propagation, not a global command, explains the difference; this rule is not a measured quorum-sensing mechanism.

**Hysteresis cards for Part 2:** Loading P has arbitrary units and biomass A has arbitrary units. On an increasing sweep, (P,A)=(0,1),(2,1),(4,1),(6,1),(8,9),(10,9). On a decreasing sweep, (10,9),(8,9),(6,9),(4,9),(2,1),(0,1). Each entry is an equilibrated model state, not a replicate. Locate tipping thresholds only within 6<P<=8 and 2<=P<4 from these coarse observations; do not report more precise thresholds. At P=4 or 6 both histories support distinct states.

**Instructor key:** Logistic-map first two iterates at r=2.5 are 0.4,0.6 and the trajectory then stays 0.6. At r=3.2 they are 0.512,0.7995392 and the stable two-cycle is about 0.5130/0.7995; r=3.5 approaches a four-cycle near 0.3828/0.8269/0.5009/0.8750. r=3.8 gives irregular bounded dynamics in this familiar chaotic parameter regime, but neither 20 iterations nor a jagged plot is an independent chaos test. The continuous logistic ODE does not exhibit this period-doubling route. Immune redundancy can buffer loss of one clone but cannot guarantee coverage of an antigen; regulatory feedback limits damage but can also suppress useful responses. Award transfer credit for naming both sides of the same mechanism.

### Worked Example: Local Clustering and Shortest Path {.unnumbered}

**Problem:** A synthetic five-node signaling graph has undirected edges A–B, A–C, B–C, B–D, C–D, D–E. Compute the local clustering coefficient at B and the shortest-path distance from A to E. Use $C_i=2T_i/[k_i(k_i-1)]$, where $T_i$ counts triangles through node $i$.

**Solution:**

- Degree of B = 3 (neighbors A, C, D).
- Pairs of B's neighbors = 3 (A–C, A–D, C–D). Of these, the edges actually present in the graph are A–C and C–D — that is 2 triangles through B.
- Local clustering at B = (2 × 2) / (3 × 2) = 4 / 6 ≈ 0.667.
- Shortest path A → E: A–C–D–E has length 3; A–B–D–E also has length 3. So the path length between A and E is 3 edges.

**Interpretation:** B has a locally cohesive neighborhood and A–E requires three relays in this graph. Topology alone establishes neither stigmergy nor biological response time; those claims require a signal-propagation mechanism and measurements.


## Analysis Questions {.unnumbered}

1. The logistic map transitions from periodic to chaotic behavior as $r$ passes through the Feigenbaum point (~3.57). Why does this transition occur even though the underlying equation is completely deterministic?
2. In Part 2, you drew a hysteresis loop. Why can reducing $P$ to the level *at which* eutrophication occurred fail to restore the clear-water state? What mechanism sustains the turbid attractor?
3. A heavy-tailed event-size pattern can motivate a criticality hypothesis but does not uniquely establish it. Propose a rival mechanism (for example, mixed event populations) and a comparison that could distinguish it. No empirical power-law dataset is supplied here.
4. Cancer has been described as a "failed CAS" where normal tissue homeostasis breaks down. Identify two CAS features that go wrong in malignancy.
5. Propose a paper simulation or card-based experiment using a bacterial-biofilm model to demonstrate one CAS principle (e.g., stigmergic self-organization, threshold transitions, or robustness to perturbation). Describe the set-up, observable, and expected result.

## Post-Lab Synthesis {.unnumbered}

> **Concept Check (Synthesis):** A shallow coastal estuary has shown gradually declining seagrass cover for a decade while nutrient inflow has risen. Recent surveys detect an abrupt loss of the remaining seagrass and a switch to a phytoplankton-dominated turbid state.
>
> (a) Relate the bistability you explored in Part 2's hysteresis loop to this estuary's observed regime shift. What ecological feedback would sustain the phytoplankton-dominated attractor once the system flipped, and how does that connection to bistability change the kind of restoration target a manager should set?
> (b) Predict the qualitative outcome of two interventions: a sharp reduction of nutrient inflow back to historical levels, and the same reduction combined with mechanical removal of phytoplankton biomass to seed seagrass regrowth. Justify the contrast in expected outcomes using the language of attractors, basin depth, and perturbation magnitude.
> (c) Design a short monitoring program (three measurable variables and one statistical early-warning signal, such as rising variance or increased autocorrelation in nutrient or chlorophyll time series) that would detect whether a partly recovered estuary is approaching another tipping point before the visible regime shift occurs.

---

## Discussion Questions {.unnumbered}

1. The SARS-CoV-2 pandemic generated striking geographic and temporal heterogeneity. Which features of a CAS (noise, nonlinearity, network topology) explain the emergence of variants?
2. Is a single cell a CAS? Defend or refute using at least three of the \cref{sec:unit_0_complex_adaptive_systems} criteria.
3. What additional scientific ingredients would be needed to "build life from scratch" in a synthetic CAS? What does the field of synthetic biology currently get right, and what do its failures reveal about the difficulty of engineering life?

---

## Safety and Ethics Notes {.unnumbered}

Paper-based lab — no reagents, no risk. Discussion of SARS-CoV-2 should be current-affairs aware; respect divergent lived experiences of the pandemic. Discussion of cancer as a "failed CAS" should be framed carefully if anyone in the class has personal experience — use the system-level language, not the blame-oriented "cancer cells are selfish" framing.

*Module: `src/biology/ecology/ecology.py` (`logistic_growth`, `lotka_volterra`); `src/biology/evolution/evolution.py` (`simulate_drift`).*
