<!-- render:skip-beamer -->

# Unit 0 — Systems Science and the Biology of Complexity: Introduction {.unnumbered}

**Unit 0 · Introduction**

---

## Why This Unit Matters {.unnumbered}

The modern study of biology began by reducing living phenomena to their smallest parts — cells, molecules, genes. This reductionist strategy yielded extraordinary insight. Yet the more we learned about individual components, the clearer it became that biology cannot be explained by parts alone: a neuron firing is not a thought, a gene is not a behaviour, a metabolic pathway is not a cell. What emerges from the *interaction* of parts — properties no single component possesses in isolation — is the subject of **systems science**.

Unit 0 introduces three interlocking frameworks that recur in every subsequent unit:

1. **Systems science** — the general theory of organised complexity: how hierarchical systems form, how feedback governs their behaviour, how new properties emerge.
2. **Complex adaptive systems** — how populations of agents with local rules give rise to robust, evolvable, collective behaviour.
3. **Active inference and the free energy principle** — a mathematically grounded account of how living agents maintain themselves by predicting and acting on their environments.

Reading Unit 0 is optional but recommended: it supplies the vocabulary of emergence, attractors, bifurcations, allostasis, and precision that makes Units I–X fit together as a single coherent theory of living organisation.

---

## Landmark Discoveries {.unnumbered}

| Year | Contribution | Significance |
| ---- | ------------ | ------------ |
| 1867 | Hermann von Helmholtz — *Handbook of Physiological Optics* | First framing of perception as unconscious inference |
| 1932 | Walter Cannon — *The Wisdom of the Body* | Coined *homeostasis*; proposed regulated internal milieu |
| 1948 | Norbert Wiener — *Cybernetics* | Formalised feedback control; bridged engineering and biology |
| 1968 | Ludwig von Bertalanffy — *General System Theory* | Articulated open systems and hierarchy across disciplines |
| 1977 | Ilya Prigogine — Nobel in Chemistry | Dissipative structures and non-equilibrium self-organisation |
| 1987 | Per Bak, Tang & Wiesenfeld — *Phys. Rev. Lett.* | Self-organised criticality and power-law scaling in CAS |
| 1992 | John Holland — *Adaptation in Natural and Artificial Systems* | Genetic algorithms; formal CAS framework |
| 2010 | Karl Friston — *Nature Rev. Neurosci.* | Free energy principle as a unified theory of brain function |
| 2015 | Peter Sterling — *Allostasis* | Proactive predictive regulation, contrasting homeostasis |

---

## Key Concepts and Connections {.unnumbered}

- **System** — a set of interacting components forming an integrated whole; open systems exchange matter and energy with their environment.
- **Emergence** — properties of a system that cannot be explained solely by properties of its components (e.g., consciousness emerges from neural circuits; life emerges from biochemistry).
- **Feedback** — output fed back as input, shaping future behaviour; negative feedback stabilises, positive feedback amplifies.
- **Attractor** — a region of phase space toward which trajectories converge; phase transitions move a system between attractors.
- **Complex adaptive system (CAS)** — a system of adaptive agents whose collective behaviour self-organises without central control.
- **Free energy** — a variational upper bound on surprise; minimising it unifies perception, action, and learning.
- **Homeostasis vs. allostasis** — passive correction to a fixed set-point vs. predictive adjustment of set-points based on context.

These ideas are deliberately general: every subsequent unit of the textbook re-encounters them. Feedback appears in enzyme regulation (Unit I), in signalling cascades (Unit II), in metabolic flux (Unit III), in population dynamics (Unit X), and in neural control (Unit IX). Attractors describe cell-fate decisions (Unit II), bistable genetic switches (Unit IV), and ecosystem stable states (Unit X). Active inference recurs as the unifying framework for physiology (Unit IX) and behaviour.

---

## Current Evidence Thread {.unnumbered}

Systems-science and complexity claims are not evidenced the way a single-gene knockout is; the evidence is whether a model's assumptions survive contact with data. A claim earns confidence when its generative model exposes the parameters and boundary that matter, when a perturbation or time-series test could have falsified it but did not, and when an explicit null or alternative model fails where it succeeds. Across this unit — emergence, adaptive agents, and active inference — read each idea as such a model and ask what observation would move you. As you
move through the chapters, keep a two-column note: **claim** on the left,
**evidence that would change my confidence** on the right. By the end of the
unit, each major idea should be tied to a measurement, model, citation, or
paper-based lab decision.

## Chapter Roadmap {.unnumbered}

```mermaid
graph LR
    C1["Systems Science<br/>and the Logic<br/>of Emergence"] --> C2["Complex Adaptive<br/>Systems"]
    C2 --> C3["Active Inference<br/>and the Free<br/>Energy Principle"]
    C1 -.->|"feedback, emergence"| UI["Units I–X"]
    C2 -.->|"attractors, evolution"| UI
    C3 -.->|"prediction, allostasis"| UI

    style C1 fill:#34495e,color:#fff
    style C2 fill:#2c3e50,color:#fff
    style C3 fill:#1a252f,color:#fff
```
<!-- alt: Graph showing unit 0 roadmap: systems science introduces feedback and emergence, complex adaptive systems adds attractors and evolution, and active inference connects prediction and allostasis to later units. -->

*Unit 0 roadmap: systems science introduces feedback and emergence, complex adaptive systems adds attractors and evolution, and active inference connects prediction and allostasis to later units.*

| Chapter | Core question | Key tools |
| ------- | ------------- | --------- |
| 0.1 Systems Science | *How does organisation arise from interaction?* | Feedback, hierarchy, Hill equation, delay oscillation |
| 0.2 Complex Adaptive Systems | *How do simple local rules produce robust global behaviour?* | Phase space, bifurcation, fitness landscape, power laws |
| 0.3 Active Inference | *How do living agents maintain themselves against disorder?* | Bayesian inference, free energy, precision, allostasis |

---

## Connections Across the Textbook {.unnumbered}

- **Unit I — Chemistry of Life**: thermodynamic gradients (Unit 0.1) explain why proteins fold spontaneously; catalysis is a feedback-regulated modular system.
- **Unit II — The Cell**: organelles are modules; the fluid-mosaic membrane is a self-organised phase; signalling cascades are hierarchical feedback loops.
- **Unit III — Energy and Metabolism**: glycolysis and the TCA cycle are classic examples of allosteric feedback and feed-forward control.
- **Unit IV–V — Genetics**: regulatory networks, bistable switches, and epigenetic memory are CAS par excellence.
- **Unit VI — Evolution**: fitness landscapes from \cref{sec:unit_0_complex_adaptive_systems} are the formal substrate of selection.
- **Unit IX — Physiology and Neuroscience**: allostasis from \cref{sec:unit_0_active_inference} and predictive coding replace simple fixed-set-point homeostasis as the model of central control.
- **Unit X — Ecology**: phase transitions, alternative stable states, and tipping points apply the mathematics of \cref{sec:unit_0_complex_adaptive_systems} directly.

---

## Computational Toolbox — Unit 0 {.unnumbered}

The three Unit 0 chapters are conceptual rather than algorithmic, but they motivate every piece of code used later:

- **Hill cooperative binding:** cell-biology helpers, especially `hill_equation()`.
- **Receptor occupancy:** cell-signalling helpers for ligand binding and response.
- **Logistic dynamics:** ecology helpers for growth under carrying capacity.
- **Lotka–Volterra oscillation:** ecology helpers for predator–prey cycles.
- **Bayesian update:** neuroscience-style posterior inference, illustrated in \cref{sec:unit_0_active_inference}.

Each concrete chapter later in the textbook either uses one of these helpers or gives the reader a chance to write the next one.

---

*Source modules: `src/biology/` (general framework across most domains).*
*Figures: `src/mermaid/biology_diagrams.py` — systems-level diagrams reused throughout the book.*
