# Unit I — Chemistry of Life: Introduction {#sec:unit_I_unit_intro .unnumbered}


## Why This Unit Matters {.unnumbered}

Every organism on Earth — a bacterium dividing in a hydrothermal vent, a redwood drawing water through
100 meters of trunk, a neuron firing in your brain right now — is made of the same ~25 elements obeying
the same quantum-mechanical rules identified over the last two centuries. Chemistry is not merely a
prerequisite for biology; it provides a molecular account of biological mechanisms. Bonding,
electrostatics, solvent interactions, and thermodynamics together help explain protein folding and DNA
structure. Buffers help constrain pH changes during metabolism.

This unit begins with atoms and ends with molecular machines. We trace how the CHNOPS elements (carbon,
hydrogen, nitrogen, oxygen, phosphorus, sulfur) occur in functional groups, how these chemical features
relate to the major biomolecule classes, and how enzymes — including protein catalysts — accelerate
reactions. Along the way you will
encounter the Pauling electronegativity scale, the Henderson-Hasselbalch equation, the Michaelis-Menten
model, and the principle of chirality: the mirror-image selectivity that means L-amino acids build your
proteins while D-sugars fuel your cells.

A thread connecting every chapter: **water**. The anomalous properties of water — its high boiling
point, the cohesion-tension mechanism in plants, its role as both solvent and reactant — make Earth
habitable and make most aqueous biochemistry possible. As the physical chemist Lawrence Henderson (1913)
argued in *The Fitness of the Environment*, water is not an incidental solvent but the molecule around
which life has been shaped by evolution.

---

## Landmark Discoveries {.unnumbered}

| Discoverer(s) | Year | Journal / Source | Discovery | Significance |
| ------------- | ---- | ---------------- | --------- | ------------ |
| Friedrich Wöhler | 1828 | \citep{wohler1828} | Synthesis of urea from inorganic ammonium cyanate | Challenged a strict separation between organic and inorganic chemistry |
| Linus Pauling & Robert Corey | 1951 | \citep{pauling1951helix} | α-helix and β-sheet structures of proteins | Connected protein secondary structure with hydrogen-bonding models |
| James Watson & Francis Crick | 1953 | \citep{watson1953} | Double-helix structure of DNA | Anti-parallel, complementary base-pairing via H-bonds; immediately suggested replication mechanism |
| Frederick Sanger and collaborators | 1955 | \citep{sanger1955insulin} | Complete covalent structure of bovine insulin | Defined amino-acid chains and disulfide connectivity; sequence constrains folding in its physical context |
| Leonor Michaelis & Maud Menten | 1913 | \citep{michaelis1913} | Enzyme-substrate saturation kinetics | Derived $v = V_{max}[S]/(K_m + [S])$; quantitative foundation of enzymology |
| Daniel Koshland | 1958 | \citep{koshland1958} | Induced-fit model of enzyme catalysis | Replaced lock-and-key; explained conformational changes in enzyme-substrate interaction |
| Jacques Monod, Jeffries Wyman & Jean-Pierre Changeux | 1965 | \citep{monod1965} | MWC model of allosteric regulation | Showed enzymes have distinct regulatory and catalytic sites; explains cooperative binding |

---

## Chemical interactions, biomolecules, and catalysis {.unnumbered}

```mermaid
---
config:
  layout: dagre
---
graph TD
    subgraph C["Chemical context"]
        A["Atoms and bonds"]
        W["Water and buffers"]
        F["Functional groups"]
    end
    subgraph B["Biomolecule classes"]
        CH["Carbohydrates"]
        L["Lipids"]
        P["Proteins"]
        N["Nucleic acids"]
    end
    subgraph K["Catalysis"]
        E["Enzyme catalysis"]
        R["Kinetics and regulation"]
    end
    A ---|"polarity and pH"| W
    A ---|"chemical structure"| F
    F ---|"chemical features"| CH
    F ---|"chemical features"| L
    F ---|"chemical features"| P
    F ---|"chemical features"| N
    P ---|"protein catalyst examples"| K
    E ---|"models and control"| R
    classDef default fill:#f4f5f6,stroke:#59636e,color:#17212b
    style C fill:#fafafa,stroke:#526777,color:#17212b
    style B fill:#fafafa,stroke:#526777,color:#17212b
    style K fill:#fafafa,stroke:#526777,color:#17212b
```
<!-- alt: Graph showing chemical context connects biomolecule classes with catalyst models and regulation. Connectors name selected relationships, not reaction steps or prerequisites; kinetic models require their stated assumptions. Protein catalysts are examples, not an exhaustive definition of enzymes. -->

*Chemical context connects biomolecule classes with catalyst models and regulation. Connectors name selected relationships, not reaction steps or prerequisites; kinetic models require their stated assumptions. Protein catalysts are examples, not an exhaustive definition of enzymes.*

---

## Current Evidence Thread {.unnumbered}

Read \nameref{sec:unit_I_unit_intro} as the point where the chemistry of life becomes measurable. Structural methods, spectroscopy, kinetic assays, and perturbations provide different kinds of evidence; a structural map alone does not directly determine all thermodynamic or kinetic quantities. Evaluate macromolecular predictions against the evidence relevant to the claim. As you
move through the chapters, keep a two-column note: **claim** on the left,
**evidence that would change my confidence** on the right. By the end of the
unit, each major idea should be tied to a measurement, model, citation, or
paper-based lab decision.

## Chapter Roadmap {.unnumbered}

| Chapter | Title | Core Question | Key Equation / Model |
| ------- | ----- | ------------- | -------------------- |
| \cref{sec:unit_I_atoms_molecules} | Atoms, Molecules, and Chemical Bonds | Why do atoms bond, and how does bond type determine biological function? | $\Delta G^{\circ\prime} = -nF\Delta E^{\circ\prime}$ |
| \cref{sec:unit_I_water_and_life} | Water — The Molecule of Life | What makes water anomalous, and why is that anomaly essential for life? | $\pi = iCRT$ (osmotic pressure) |
| \cref{sec:unit_I_macromolecules} | Biological Macromolecules | How do major biomolecule classes build structures and carry out life's functions? | Molecular size, polymerization where applicable, and lipid assembly |
| \cref{sec:unit_I_enzymes_and_kinetics} | Enzymes and the Kinetics of Catalysis | How do enzymes lower activation energy, and how is their activity regulated? | $v = V_{max}[S]/(K_m + [S])$ |

---

## Connections Across the Textbook {.unnumbered}

\nameref{sec:unit_I_unit_intro} establishes the chemical vocabulary for the entire textbook:

- The **bond energies and functional groups** introduced here reappear in \nameref{sec:unit_III_unit_intro} (energy released by glucose oxidation), \nameref{sec:unit_IV_unit_intro} (phosphodiester bonds of DNA), and \nameref{sec:unit_V_unit_intro} (crossing-over in chromatin).
- **Enzyme kinetics and allostery** (\cref{sec:unit_I_enzymes_and_kinetics}) reappear in \nameref{sec:unit_III_unit_intro} (PFK-1 regulation) and \nameref{sec:unit_VII_unit_intro} (antibiotic enzyme targets). Hemoglobin cooperativity in \nameref{sec:unit_IX_unit_intro} is a related binding-model comparison, not enzyme catalysis.
- **pH and buffers** link directly to \nameref{sec:unit_II_unit_intro} (lysosomal pH 4.5 vs. cytoplasmic pH 7.2), \nameref{sec:unit_III_unit_intro} (mitochondrial proton gradient), and \nameref{sec:unit_IX_unit_intro} (blood acid-base balance in clinical contexts).
- **Chirality** of L-amino acids and D-sugars reappears in \nameref{sec:unit_VII_unit_intro} (D-amino acids in bacterial cell walls) and \nameref{sec:unit_V_unit_intro} (enzyme specificity in DNA repair).

> **Before you begin:** You should be comfortable with scientific notation, logarithms, and basic algebra. No prior chemistry or biology is assumed.


## Computational Toolbox — Unit I {.unnumbered}

The following demonstrates the real `src/biology/biochemistry` functions used to
generate figures and worked examples throughout \nameref{sec:unit_I_unit_intro}.

```python
from biology.biochemistry import michaelis_menten, glycolysis_summary

# Stipulated Michaelis-Menten teaching parameters, not an enzyme assay fit:
# Vmax = 12.0 µmol/min, Km = 0.8 µM, substrate = 2.0 µM.
result = michaelis_menten(substrate_conc=2.0, Vmax=12.0, Km=0.8)
print(f"Reaction rate at [S]=2 µM: {result.reaction_rate:.2f} µmol/min")
# Expected: Reaction rate at [S]=2 µM: 8.57 µmol/min
# (= 12.0 × 2.0 / (0.8 + 2.0); Vmax/2 occurs at [S]=Km=0.8 µM)

# Glycolysis summary: net products per glucose
summary = glycolysis_summary()
print(f"Net ATP yield: {summary.net_atp} ATP per glucose")
print(f"NADH produced: {summary.net_nadh} NADH per glucose")
print(f"Steps represented: {len(summary.steps)}")
# Expected:
# Net ATP yield: 2 ATP per glucose
# NADH produced: 2 NADH per glucose
# Steps represented: 10
```

> **Try it yourself:** Install the project environment (`uv sync`) and run
> `python3 -c "from biology.biochemistry import michaelis_menten; print(michaelis_menten(5, 10, 2))"`.
> Modify substrate concentration to trace the full saturation curve.

---

*Source modules: `src/biology/biochemistry/biochemistry.py` — enzyme kinetics models, macromolecule analysis.*
*Figures generated by `src/visualization/plots.py` (Michaelis-Menten plots) and `src/mermaid/biology_diagrams.py`.*

## Cross-Unit Integration {.unnumbered}

The chemistry of \nameref{sec:unit_I_unit_intro} is the necessary prelude to the cell. Every concept introduced here — covalent and non-covalent bonds, hydrophobicity, weak interactions, protein folding driven by entropy and enthalpy — becomes operational in \nameref{sec:unit_II_unit_intro}'s account of the cell membrane and the cytoskeleton. The phospholipid bilayer is a direct expression of the hydrophobic effect; membrane proteins fold so that hydrophobic side chains face the lipid interior and polar residues face the aqueous environment; ion channels exploit the same electrostatic and hydrogen-bonding logic you saw in protein structure. As you read \nameref{sec:unit_II_unit_intro}, return to the bonding diagrams of \nameref{sec:unit_I_unit_intro} whenever a transport mechanism or membrane property feels arbitrary — it is almost always a chemistry consequence.
