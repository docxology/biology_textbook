# Preface {.unnumbered}

## A Textbook Built With Code {.unnumbered}

Welcome to *Introduction to Biology: A Generative Approach* — **Instructor Edition** with visible model answers in the question-bank appendices — an open-source textbook covering introductory biology across **Unit 0 — Systems Science for Biology: Introduction**, the thematic sequence from **Unit I — Chemistry of Life: Introduction** through **Unit X — Ecology: Introduction**, and **44 core chapters**, plus optional **laboratories** and **question banks** in the appendices. Where this text uses quantitative models, the corresponding computations are implemented as tested Python modules.

Whether we examine Michaelis–Menten enzyme kinetics, Lotka–Volterra predator–prey dynamics, or Hodgkin–Huxley action potentials, the underlying mathematical model exists as a working module in the accompanying codebase. Many figures are generated programmatically. Process diagrams are expressed using Mermaid where it improves clarity. For instructors and independent learners, this supports inspection, extension, and reproducible re-generation of results.

The philosophy is: **understand biology by computing biology**.

**How to read this book digitally:** The reference build is a compact **PDF** with LaTeX typesetting. Not all screen readers handle mathematical notation the same way in PDF; the same sources also produce **HTML** for some workflows. The [biology textbook source repository](https://github.com/docxology/biology_textbook) contains the manuscript, figures, tests, and code; the [Zenodo archival DOI record](https://doi.org/10.5281/zenodo.20286478) identifies a fixed edition snapshot. If you need larger type or margins, a **reader** typography profile is documented (paired edits to `manuscript/config.yaml` and `manuscript/preamble.md` — see `docs/accessibility.md` in the project tree). The book does not re-express every formula in natural language; where precision matters, work through the worked examples and the linked `src/biology` modules.

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

A phospholipid bilayer is 7 nm thick and amphipathic — and those two structural facts explain every
property of biological membranes (Unit I — Chemistry of Life: Introduction and Unit II — The Cell: Introduction). The α-helix of hemoglobin's subunits explains its
cooperativity and the Bohr effect (Unit I — Chemistry of Life: Introduction and Unit IX — Zoology and Systems Physiology: Introduction). The T-shaped architecture of the mitochondrial
ATP synthase explains rotary catalysis (Unit III — Energy and Metabolism: Introduction). In biology, whenever you ask *how*, the answer is
typically embedded in *shape*.

### Information — storage, transfer, expression {.unnumbered}

DNA is not merely a chemical; it is a **code**. An alphabet of four nucleotides encodes a program
of 20 amino acids, creating an effectively unlimited diversity of proteins. Unit IV — Molecular Genetics: Introduction (Molecular Genetics)
examines the molecular machinery that reads this code — from DNA helicases to ribosomes — and how
errors in the code drive disease and evolution. Unit V — Classical Genetics and Heredity: Introduction (Classical Genetics) examines how the code is
transmitted between generations. Unit VII — Microbiology: Introduction (Microbiology) shows how viruses inject their own code into
host cells.

### Emergent properties: the whole exceeds the parts {.unnumbered}

A single neuron can fire or remain silent. A brain can think. A single predator can collapse an entire
intertidal community (Unit X — Ecology: Introduction). A slight imbalance in NAD⁺/NADH ratio shunts metabolism from aerobic
to anaerobic (Unit III — Energy and Metabolism: Introduction). Emergence — complex behavior arising from simple rules — is everywhere in
biology, and understanding it requires systems thinking: tracking flows, feedback loops, and
nonlinear dynamics, not just cataloguing parts.

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

**The hypothetico-deductive method.** A hypothesis is a testable, falsifiable prediction. Barry
Marshall and Robin Warren's hypothesis that bacteria cause peptic ulcers (not stress) was so contrary
to medical consensus that Marshall famously drank a *Helicobacter pylori* culture to demonstrate the
relationship \citep{marshall1985koch}. Their Nobel Prize-winning work illustrates how a single decisive
experiment can overturn decades of received wisdom.

**Models and computation as scientific tools.** Modern biology is inseparable from mathematical
modeling. The Michaelis-Menten equation (1913) is a model. The Hardy-Weinberg principle is a model.
The Hodgkin-Huxley equations (1952) were Nobel Prize-winning models. A model is not a simplification
that sacrifices truth; it is a commitment to precision — stating *exactly* what you are and are not
claiming. The Python modules in this textbook implement these models so that you can inspect their
assumptions, vary their parameters, and see where they break.

**Primary literature vs. textbook synthesis.** This textbook cites primary papers at point of use.
When you see \"(Author et al., Year, *Journal*)\" inline, that citation points to the experiment or
calculation that established the claim. Science journalism, textbooks, and Wikipedia involve more
layers of interpretation. Primary papers are the ultimate authority — and learning to read them is a
core competency this textbook aims to develop.

**Revision is not failure.** Every chapter in this book contains examples of ideas revised or
overturned: the flat earth was replaced by a spherical one; Lamarckian inheritance was replaced by
Darwinian selection; the DNA double helix replaced protein as the genetic material; the \"lock-and-key\"
enzyme model was replaced by \"induced fit\". A willingness to revise beliefs on evidence is not
weakness — it is the engine of scientific progress.

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
The table below is generated from `manuscript/config.yaml`; unit and chapter titles are
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
| **Exam / course survey** | Unit intros + chapter summaries + the companion question bank that follows each chapter | Answer odd-numbered questions first; check module footers for `biology.*` imports. |
| **Wet-lab or clinical bridge** | Unit II — The Cell: Introduction, Unit IV — Molecular Genetics: Introduction, Unit VII — Microbiology: Introduction, and Unit IX — Zoology and Systems Physiology: Introduction | Read boxed clinical / systems notes; pair with labs in the same unit. |
| **Modeling / CS** | Unit 0 — Systems Science for Biology: Introduction, then any unit’s “Bridge to computation” | Run examples with `uv run python` from the project root; regenerate figures with `scripts/generate_figures.py`. |
| **Ecology / field biology** | Unit VI — Evolution: Introduction and Unit X — Ecology: Introduction, plus Photosynthesis | Focus on `ecology.py` functions cited in chapter footers; work Lotka–Volterra and logistic examples by hand then in Python. |

---

## How to Use This Book {.unnumbered}

Each chapter is designed for introductory biology learners and can be read in two modes:

1. **Concept-first**: Read the narrative, work the examples, and do the questions.
2. **Model-first**: Run the companion modules and treat the text as interpretation of model behavior.

**For each concept, the integrated approach is:**

1. **Conceptual narrative** — the biological story and mechanism in plain language with precise vocabulary.
2. **Quantitative framework** — equations, derivations, and worked numerical examples.
3. **Primary citations** — key papers (author, year, journal) supporting mechanisms; citations are included where used.
4. **Python source** — model code in the project’s biology modules (importable and runnable).
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
- Most physiological parameters indexed to standard conditions (37 °C, pH 7.4, sea level) unless stated

**Primary citations** follow the format Author (year), *Journal*, and are embedded inline. They are selective: landmark results and a small number of current references where they materially clarify the consensus.

---

## Open Science Commitment {.unnumbered}

This book is released under the Creative Commons Attribution 4.0 International Licence (CC BY 4.0): you may freely use, adapt, and redistribute it with attribution. Most accompanying source code is released under the Apache-2.0 Licence.

The entire textbook — source markdown files, Python modules, figure scripts, and the build pipeline — is publicly available. The intent is for this resource to be a living, improvable document rather than a static product. Pull requests are welcome.

---

## Acknowledgements {.unnumbered}

This textbook was developed as part of the Research Project Template infrastructure for open, reproducible science education. Gratitude to the open-source communities behind [Pandoc](https://pandoc.org/), [LaTeX](https://www.latex-project.org/), [Mermaid](https://mermaid.js.org/), and [matplotlib](https://matplotlib.org/).

---

*Author:* **Daniel Ari Friedman**, Active Inference Institute
*ORCID:* [0000-0001-6232-9096](https://orcid.org/0000-0001-6232-9096)
*Edition 1.0, 2026*
*Licence: CC BY 4.0 (content) · Apache-2.0 (code)*
