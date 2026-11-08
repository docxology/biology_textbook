# Preface {.unnumbered}

## A Textbook Built With Code {.unnumbered}

Welcome to *Introduction to Biology: A Generative Approach* — **Instructor Edition** with visible model answers in the question-bank appendices — an open-source textbook covering introductory biology across **Unit 0 — Systems Science for Biology: Introduction**, the thematic sequence from **Unit I — Chemistry of Life: Introduction** through **Unit X — Ecology: Introduction**, and **44 core chapters**, plus optional **laboratories** and **question banks** in the appendices. Selected quantitative models have corresponding tested Python implementations; not every calculation, biological mechanism or empirical claim is implemented by the package.

The accompanying package implements selected models, including Michaelis–Menten kinetics, Lotka–Volterra predator–prey dynamics, and Hodgkin–Huxley action potentials. Their assumptions, units, and numerical schemes matter as much as the formulas. Many figures are generated from these models; illustrative simulations are not empirical measurements or validated clinical predictors. Paper laboratories remain usable without running Python.

The philosophy is: **understand biology by computing biology**.

**How to read this book digitally:** The reference build is a **PDF** with LaTeX typesetting. Screen-reader handling of PDF mathematics varies; alt text and captions do not by themselves establish PDF/UA conformance. The [biology textbook source repository](https://github.com/docxology/biology_textbook) contains the manuscript, figures, tests, and code. The [Zenodo record](https://doi.org/10.5281/zenodo.20286478) archives the earlier manuscript edition 1.0/software 1.0.0; it is not a deposition of edition 1.1/software 2.0.0. Larger-type settings require paired edits to `docs/manuscript/config.yaml` and `docs/manuscript/preamble.md`, as described in `docs/accessibility.md`.

**Accessible formats:** The compact PDF is optimized for print density, not for every reader. For screen-reader review, HTML/MathJax workflows usually preserve reading order and mathematical navigation better than a dense PDF. Figures and Mermaid diagrams include alt text plus captions, and the large-type reader profile increases margins, font size, and line spacing without changing chapter order or cross-reference IDs.

---

## Five Big Ideas in Biology {.unnumbered}

Biology is a vast and diverse science, but a small set of orienting themes recurs across its subdisciplines.
This book groups them as **Five Big Ideas** (Evolution; Information; Structure and function; Systems and emergence; Cells).
They map pedagogically to the five **core concepts** in AAAS *Vision and Change in Undergraduate Biology Education* \citep{visionandchange2011};
that report also defines six **core competencies** (quantitative reasoning, modeling, data interpretation, and related practice skills),
which this text addresses through labs, models, and inquiry—not as a sixth numbered “big idea” heading.
Unit 0 — Systems Science for Biology: Introduction adds an optional systems orientation: active inference and the free energy principle are graduate-depth lenses for connecting feedback, prediction, and behavior \citep{friston2017,parr2022activeinference}, not part of the introductory-biology canon that Vision & Change defines for the core undergraduate sequence.
The themes below recur across the units that follow.

### Evolution: the unifying theory of life {.unnumbered}

*\"Nothing in biology makes sense except in the light of evolution.\"* — Theodosius \citet{dobzhansky1973}

Evolution by natural selection explains the origin of species, the genetic code being nearly universal,
the homology between a human arm and a bat wing, and why influenza vaccines must be redesigned every
year. Unit VI — Evolution: Introduction, Unit V — Classical Genetics and Heredity: Introduction, and Unit IV — Molecular Genetics: Introduction develop this idea from population
genetics algorithms to phylogenetic tree reconstruction.

### Structure and function are inseparable {.unnumbered}

A phospholipid bilayer's amphipathy helps explain compartment formation, but membrane proteins, lipid composition, and electrochemical gradients also determine membrane behavior (\cref{sec:unit_II_membrane_transport}). Hemoglobin cooperativity depends on quaternary conformational changes, while protonation and other ligands contribute to the Bohr effect (\cref{sec:unit_IX_circulation_respiration_homeostasis}). ATP synthase couples a rotor and stator to cyclic catalytic-site changes; its outline alone does not explain the mechanism (\cref{sec:unit_III_bioenergetics_and_respiration}). Structure constrains function, but a mechanistic account also needs interactions, energetics, and context.

### Information — storage, transfer, expression {.unnumbered}

DNA is not merely a chemical; it is a **code**. An alphabet of four nucleotides encodes a program
of 20 amino acids, creating an effectively unlimited diversity of proteins. Unit IV — Molecular Genetics: Introduction (Molecular Genetics)
examines the molecular machinery that reads this code — from DNA helicases to ribosomes — and how
errors in the code drive disease and evolution. Unit V — Classical Genetics and Heredity: Introduction (Classical Genetics) examines how the code is
transmitted between generations. Unit VII — Microbiology: Introduction (Microbiology) shows how viruses inject their own code into
host cells.

### Emergent properties: the whole exceeds the parts {.unnumbered}

A single neuron can fire or remain silent, while interacting neural circuits support behavior. Predator effects can propagate through food webs without determining every community outcome (\cref{sec:unit_X_community_interactions}). Metabolism likewise couples pathways: lactate formation regenerates NAD⁺ to sustain glycolysis when respiratory NADH oxidation is limited (\cref{sec:unit_III_bioenergetics_and_respiration}), rather than a slight redox-ratio change universally switching all metabolism between two modes. Systems thinking follows these interactions, feedback loops, and constraints across scales.

### Cells: the universal unit of life {.unnumbered}

Every living organism is composed of one or more cells, sharing a common molecular toolkit:
phospholipid membranes, DNA, ribosomes, ATP. Unit II — The Cell: Introduction examines the cell as a physical and computational
system. Unit VII — Microbiology: Introduction through Unit IX — Zoology and Systems Physiology: Introduction extend this to specialized cells: bacteria, plant cells, neurons, immune cells.
Understanding the cell is not a module to be completed — it is a perspective to carry through every
subsequent chapter.

---

## How Science Actually Works {.unnumbered}

This textbook presents science not as a collection of established facts but as a dynamic, self-correcting
process of inquiry. Understanding how scientific knowledge is generated, tested, and revised is as
important as knowing what is currently accepted.

**The hypothetico-deductive method.** A hypothesis proposes a testable explanation from which predictions can be derived. In Marshall's self-infection experiment, ingestion of a bacterial culture was followed by histologically documented acute gastritis, not demonstrated peptic ulceration \citep{marshall1985koch}. The experiment supported a causal role in acute gastritis; it did not by itself establish the causes of peptic ulcers. The lesson is to distinguish the endpoint actually observed from a broader hypothesis that requires further evidence.

**Models and computation as scientific tools.** Modern biology is inseparable from mathematical
modeling. The Michaelis-Menten equation (1913) is a model. The Hardy-Weinberg principle is a model.
The Hodgkin-Huxley equations (1952) were Nobel Prize-winning models. A model is not a simplification
that sacrifices truth; it is a commitment to precision — stating *exactly* what you are and are not
claiming. The Python modules in this textbook implement these models so that you can inspect their
assumptions, vary their parameters, and see where they break.

**Primary literature and synthesis.** Citations identify the evidence or synthesis used for a claim. Primary papers bring readers closer to methods and observations, but they remain open to error, reanalysis, and failed replication. Reviews and institutional guidance serve different purposes. Evidence strength depends on design, measurement, scope, and corroboration—not on a source label alone.

**Revision is not failure.** Replication, new measurements, and better models can revise explanations. Evidence that DNA carries hereditary information and evidence for its double-helical structure answer different questions; one did not simply replace a “protein helix” model. Enzyme binding likewise includes both conformational selection and induced-fit mechanisms rather than one universal replacement story. Scientific revision should identify which claim changed, which evidence changed it, and which conclusions remain supported.

---

## How to Use the Unit Introductions {.unnumbered}

Each unit begins with a `unit_intro.md` page containing:

- **A narrative hook** explaining why this area of biology matters and what surprises it holds
- **A landmark discoveries table** citing the experiments that established the field
- **A concept map** (Mermaid diagram) showing how the chapters connect to each other and to other units
- **A chapter roadmap** mapping each chapter to its core question and key equation

Use these pages as **advance organisers** — read them before starting the unit and return to them
when you feel you have lost the conceptual thread. The best moment to understand how a jigsaw piece
fits is before you lose sight of the box.

---

## Scope and Organization {.unnumbered}

The textbook proceeds from atoms to ecosystems, following the standard introductory course arc.
The table below is generated from `docs/manuscript/config.yaml`; unit and chapter titles are
plain TOC titles from the canonical manifest.

<!-- preface-scope-start -->
| Instructional block | Core chapters |
| ---- | ------------- |
| **\hyperref[sec:unit_0_unit_intro]{Unit 0 — Systems Science for Biology: Introduction}** | \hyperref[sec:unit_0_systems_science]{Systems Science and Emergence}; \hyperref[sec:unit_0_complex_adaptive_systems]{Complex Adaptive Systems}; \hyperref[sec:unit_0_active_inference]{Active Inference and Free Energy}; \hyperref[sec:unit_0_history_philosophy_biology]{History and Philosophy of Biology} |
| **\hyperref[sec:unit_I_unit_intro]{Unit I — Chemistry of Life: Introduction}** | \hyperref[sec:unit_I_atoms_molecules]{Atoms, Molecules, and Chemical Bonds}; \hyperref[sec:unit_I_water_and_life]{Water — The Molecule of Life}; \hyperref[sec:unit_I_macromolecules]{Biological Macromolecules}; \hyperref[sec:unit_I_enzymes_and_kinetics]{Enzymes and the Kinetics of Catalysis} |
| **\hyperref[sec:unit_II_unit_intro]{Unit II — The Cell: Introduction}** | \hyperref[sec:unit_II_cell_theory]{Cell Theory and Cell Types}; \hyperref[sec:unit_II_cell_structure]{Cell Structure and Organelles}; \hyperref[sec:unit_II_membrane_transport]{Membrane Structure and Transport}; \hyperref[sec:unit_II_cell_signaling]{Cell Signaling and Communication} |
| **\hyperref[sec:unit_III_unit_intro]{Unit III — Energy and Metabolism: Introduction}** | \hyperref[sec:unit_III_bioenergetics_and_respiration]{Bioenergetics and Cellular Respiration}; \hyperref[sec:unit_III_photosynthesis]{Photosynthesis}; \hyperref[sec:unit_III_metabolic_integration]{Metabolic Integration and Regulation} |
| **\hyperref[sec:unit_IV_unit_intro]{Unit IV — Molecular Genetics: Introduction}** | \hyperref[sec:unit_IV_dna_replication_and_cell_cycle]{DNA Replication and the Cell Cycle}; \hyperref[sec:unit_IV_gene_expression]{Gene Expression}; \hyperref[sec:unit_IV_mutations_and_genomics]{Mutations, CRISPR, and Genomics}; \hyperref[sec:unit_IV_chromatin_and_epigenetic_mechanisms]{Chromatin and Epigenetic Mechanisms}; \hyperref[sec:unit_IV_epigenetic_inheritance_and_disease]{Epigenetic Inheritance and Disease} |
| **\hyperref[sec:unit_V_unit_intro]{Unit V — Classical Genetics and Heredity: Introduction}** | \hyperref[sec:unit_V_mendelian_principles]{Mendelian Principles and Probability}; \hyperref[sec:unit_V_mendelian_extensions_and_human_genetics]{Mendelian Extensions and Human Genetics}; \hyperref[sec:unit_V_chromosomal_inheritance]{Chromosomal Inheritance and Linkage}; \hyperref[sec:unit_V_population_genetics]{Population Genetics} |
| **\hyperref[sec:unit_VI_unit_intro]{Unit VI — Evolution: Introduction}** | \hyperref[sec:unit_VI_evolution_and_selection]{Natural Selection and Adaptation}; \hyperref[sec:unit_VI_genetic_drift_and_speciation]{Genetic Drift, Gene Flow, and Speciation}; \hyperref[sec:unit_VI_phylogenetics]{Phylogenetics and the Tree of Life} |
| **\hyperref[sec:unit_VII_unit_intro]{Unit VII — Microbiology: Introduction}** | \hyperref[sec:unit_VII_bacteria_archaea_viruses]{Bacteria, Archaea, and Viruses}; \hyperref[sec:unit_VII_microbial_ecology]{Microbial Ecology and the Microbiome}; \hyperref[sec:unit_VII_host_immunity_and_vaccines]{Host Immunity and Vaccines}; \hyperref[sec:unit_VII_antimicrobial_resistance_and_epidemiology]{Antimicrobial Resistance and Epidemiology} |
| **\hyperref[sec:unit_VIII_unit_intro]{Unit VIII — Botany — Plant Biology: Introduction}** | \hyperref[sec:unit_VIII_plant_structure_and_water]{Plant Structure and Water Relations}; \hyperref[sec:unit_VIII_plant_reproduction]{Plant Reproduction and Development}; \hyperref[sec:unit_VIII_plant_responses]{Plant Responses to the Environment} |
| **\hyperref[sec:unit_IX_unit_intro]{Unit IX — Zoology and Systems Physiology: Introduction}** | \hyperref[sec:unit_IX_circulation_respiration_homeostasis]{Circulation and Respiration}; \hyperref[sec:unit_IX_nervous_system]{Nervous System and Neural Signaling}; \hyperref[sec:unit_IX_action_potential_synapses]{Action Potentials and Synaptic Transmission}; \hyperref[sec:unit_IX_endocrine_signaling]{Endocrine Signaling and Homeostasis}; \hyperref[sec:unit_IX_immune_system_defense]{Immune System Architecture} |
| **\hyperref[sec:unit_X_unit_intro]{Unit X — Ecology: Introduction}** | \hyperref[sec:unit_X_population_ecology]{Population Ecology and Growth Models}; \hyperref[sec:unit_X_community_interactions]{Community Interactions and Succession}; \hyperref[sec:unit_X_biodiversity_and_food_webs]{Biodiversity and Food Webs}; \hyperref[sec:unit_X_ecosystem_ecology]{Ecosystem Ecology}; \hyperref[sec:unit_X_biomes_and_conservation]{Biomes and Conservation Biology} |
<!-- preface-scope-end -->

---

## Reading paths by goal {.unnumbered}

| Goal | Where to start | How to use the code |
| ---- | -------------- | ------------------- |
| **Exam / course survey** | Unit intros + chapter summaries + the companion question banks in their separate appendix sequence | Answer odd-numbered questions first; check module footers for `biology.*` imports. |
| **Wet-lab or clinical bridge** | Unit II — The Cell: Introduction, Unit IV — Molecular Genetics: Introduction, Unit VII — Microbiology: Introduction, and Unit IX — Zoology and Systems Physiology: Introduction | Read boxed clinical / systems notes; pair with labs in the same unit. |
| **Modeling / CS** | Unit 0 — Systems Science for Biology: Introduction, then any unit’s “Bridge to computation” | Run examples with `uv run python` from the project root; regenerate figures with `scripts/generate_figures.py`. |
| **Ecology / field biology** | Unit VI — Evolution: Introduction and Unit X — Ecology: Introduction, plus Photosynthesis | Focus on `biology.ecology.ecology` functions cited in chapter footers; work Lotka–Volterra and logistic examples by hand then in Python. |

---

## How to Use This Book {.unnumbered}

Each chapter is designed for introductory biology learners and can be read in two modes:

1. **Concept-first**: Read the narrative, work the examples, and do the questions.
2. **Model-first**: Run the companion modules and treat the text as interpretation of model behavior.

**Across the book, the integrated approach combines:**

1. **Conceptual narrative** — the biological story and mechanism in plain language with precise vocabulary.
2. **Quantitative framework** — equations, derivations, and worked numerical examples.
3. **Primary citations** — key papers (author, year, journal) supporting mechanisms; citations are included where used.
4. **Python source** — executable implementations of selected models, with explicit assumptions and units; not every biological concept has a computational implementation.
5. **Figures** — generated by `src/visualization/plots.py` (`ALL_FIGURE_GENERATORS`) and `src/mermaid/biology_diagrams.py`.
6. **Clinical connections** — boxed examples connecting molecular mechanisms to human disease, therapy, and public health.
7. **Review and discussion questions** — a 30-item companion question bank per chapter, plus end-of-chapter review questions, from calculation to synthesis (Unit 0 — Systems Science for Biology: Introduction uses discussion prompts; other units mix numeric and conceptual items).

---

## Computational Infrastructure {.unnumbered}

The project’s biology code is organized by domain:

```text
src/biology/
├── biochemistry/    — Enzyme kinetics, macromolecule analysis
├── cell/            — Membrane biophysics, signaling, organelles
├── genetics/        — Mendelian ratios, Hardy-Weinberg, linkage mapping
├── physiology/      — Homeostasis, hemoglobin, cardiac models
├── ecology/         — Population dynamics, community models
├── evolution/       — Drift simulation, fitness landscapes
├── microbiology/    — Growth curves, MIC, viral cycles
├── botany/          — Water potential, transpiration, photosynthesis pathways
└── neuroscience/    — Action potentials, synapse models
```

**Diagram generation:**

```text
src/mermaid/biology_diagrams.py  — diagram factories registered in ALL_BIOLOGY_DIAGRAMS
src/visualization/plots.py    — matplotlib figure generators (ALL_FIGURE_GENERATORS)
```

Most code conforms to the project’s **no-mocks policy**: tests use real computations.

---

## Pedagogical Standards {.unnumbered}

**What this book assumes:** basic chemistry (atomic structure, covalent bonds, pH), basic algebra, and optional access to Python. No prior biology is required.

**Mathematical notation** is standard across most chapters:

- Concentrations in mol/L (M) or mmol/L (mM) as context requires
- Reaction rates in M·s⁻¹ or μmol·min⁻¹·mg protein⁻¹
- Genetic distances in centimorgans (cM)
- Physiological parameters accompanied by their organism, preparation, and physical conditions; human body-temperature examples do not define universal physiological standards

**Primary citations** follow the format Author (year), *Journal*, and are embedded inline. They are selective: landmark results and a small number of current references where they materially clarify the consensus.

---

## Open Science Commitment {.unnumbered}

This book is released under the Creative Commons Attribution 4.0 International Licence (CC BY 4.0): you may freely use, adapt, and redistribute it with attribution. Most accompanying source code is released under the Apache-2.0 Licence.

The entire textbook — source markdown files, Python modules, figure scripts, and the build pipeline — is publicly available. The intent is for this resource to be a living, improvable document rather than a static product. Pull requests are welcome.

---

## Acknowledgements {.unnumbered}

This textbook was developed as part of the Research Project Template infrastructure for open, reproducible science education. Gratitude to the open-source communities behind [Pandoc](https://pandoc.org/), [LaTeX](https://www.latex-project.org/), [Mermaid](https://mermaid.js.org/), and [matplotlib](https://matplotlib.org/).

