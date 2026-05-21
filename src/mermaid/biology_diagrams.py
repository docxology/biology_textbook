"""Biology-specific Mermaid diagram factory functions.

Provides one factory per textbook Unit, returning MermaidDiagram objects
that document key biological processes visually. All diagrams are generated
programmatically from the underlying biology src modules where appropriate.
"""

from __future__ import annotations

from .diagrams import flowchart, sequence_diagram, state_diagram
from .renderer import MermaidDiagram
from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)


# ---------------------------------------------------------------------------
# Unit I — Chemistry of Life
# ---------------------------------------------------------------------------


def macromolecule_classification_diagram() -> MermaidDiagram:
    """Classify the four classes of biological macromolecules."""
    return flowchart(
        name="macromolecule_classification",
        title="Biological Macromolecules: Monomers, Polymers, and Functions",
        nodes=[
            ("M", "Biological Macromolecules"),
            ("C", "Carbohydrates"),
            ("L", "Lipids"),
            ("P", "Proteins"),
            ("N", "Nucleic Acids"),
            ("Cm", "Monosaccharides to polysaccharides"),
            ("Lm", "Fatty acids, glycerol, sterols"),
            ("Pm", "Amino acids to polypeptides"),
            ("Nm", "Nucleotides to DNA/RNA"),
            ("Cf", "Energy storage and cell walls"),
            ("Lf", "Membranes, hormones, energy"),
            ("Pf", "Catalysis, structure, transport"),
            ("Nf", "Information storage and expression"),
        ],
        edges=[
            ("M", "C", ""),
            ("M", "L", ""),
            ("M", "P", ""),
            ("M", "N", ""),
            ("C", "Cm", "monomers"),
            ("L", "Lm", "components"),
            ("P", "Pm", "monomers"),
            ("N", "Nm", "monomers"),
            ("Cm", "Cf", "functions"),
            ("Lm", "Lf", "functions"),
            ("Pm", "Pf", "functions"),
            ("Nm", "Nf", "functions"),
        ],
    )


def enzyme_kinetics_diagram() -> MermaidDiagram:
    """Show enzyme-substrate interaction and catalysis cycle."""
    return flowchart(
        name="enzyme_kinetics",
        title="Enzyme Catalysis Cycle and Energy Barrier",
        nodes=[
            ("E", "Enzyme (free)"),
            ("S", "Substrate"),
            ("ES", "Enzyme-substrate complex"),
            ("TS", "Transition state stabilized"),
            ("EP", "Enzyme-product complex"),
            ("P", "Product"),
            ("Ea", "Lower activation energy"),
        ],
        edges=[
            ("E", "ES", "binds substrate"),
            ("S", "ES", ""),
            ("ES", "TS", "induced fit"),
            ("TS", "EP", "chemistry"),
            ("TS", "Ea", "stabilization"),
            ("EP", "P", "releases product"),
            ("EP", "E", "enzyme regenerated"),
        ],
    )


# ---------------------------------------------------------------------------
# Unit II — The Cell
# ---------------------------------------------------------------------------


def organelle_function_diagram() -> MermaidDiagram:
    """Map major organelles to their primary functions."""
    return flowchart(
        name="organelle_functions",
        title="Eukaryotic Organelle Functions",
        nodes=[
            ("Cell", "Eukaryotic Cell"),
            ("Nuc", "Nucleus\n(DNA storage)"),
            ("Mito", "Mitochondria\n(ATP synthesis)"),
            ("Chloro", "Chloroplast\n(Photosynthesis)"),
            ("ER", "Endoplasmic\nReticulum (synthesis)"),
            ("Golgi", "Golgi Apparatus\n(sorting/secretion)"),
            ("Lyso", "Lysosome\n(digestion)"),
            ("Ribo", "Ribosome\n(translation)"),
        ],
        edges=[
            ("Cell", "Nuc", ""),
            ("Cell", "Mito", ""),
            ("Cell", "Chloro", ""),
            ("Cell", "ER", ""),
            ("Cell", "Golgi", ""),
            ("Cell", "Lyso", ""),
            ("Cell", "Ribo", ""),
        ],
        direction="LR",
    )


def membrane_transport_diagram() -> MermaidDiagram:
    """Illustrate the types of membrane transport."""
    return flowchart(
        name="membrane_transport",
        title="Membrane Transport by Energy Source and Cargo Size",
        nodes=[
            ("T", "Membrane Transport"),
            ("P", "Passive transport"),
            ("A", "Energy-coupled transport"),
            ("S", "Simple Diffusion"),
            ("F", "Facilitated Diffusion"),
            ("OS", "Osmosis"),
            ("PP", "Primary active pumps"),
            ("SP", "Secondary cotransport"),
            ("Bulk", "Vesicular transport"),
            ("Grad", "Down electrochemical gradient"),
            ("ATP", "ATP or ion-gradient energy"),
        ],
        edges=[
            ("T", "P", ""),
            ("T", "A", ""),
            ("P", "S", ""),
            ("P", "F", ""),
            ("P", "OS", ""),
            ("A", "PP", ""),
            ("A", "SP", ""),
            ("A", "Bulk", ""),
            ("P", "Grad", "driving force"),
            ("A", "ATP", "driving force"),
        ],
    )


# ---------------------------------------------------------------------------
# Unit III — Energy and Metabolism
# ---------------------------------------------------------------------------


def glycolysis_pathway_diagram() -> MermaidDiagram:
    """Show glycolysis steps from glucose to pyruvate."""
    return flowchart(
        name="glycolysis_pathway",
        title="Glycolysis: Investment, Cleavage, and Payoff",
        nodes=[
            ("G", "Glucose (6C)"),
            ("G6P", "Glucose-6-phosphate"),
            ("F6P", "Fructose-6-phosphate"),
            ("F16BP", "Fructose-1,6-bisphosphate"),
            ("Triose", "2x triose phosphate (3C)"),
            ("PG13", "2x 1,3-bisphosphoglycerate"),
            ("PG3", "2x 3-PG to 2-PG"),
            ("PEP", "2× PEP"),
            ("Pyr", "2x pyruvate"),
            ("Net", "Net: +2 ATP, +2 NADH"),
        ],
        edges=[
            ("G", "G6P", "−1 ATP"),
            ("G6P", "F6P", "isomerase"),
            ("F6P", "F16BP", "−1 ATP; PFK-1"),
            ("F16BP", "Triose", "aldolase"),
            ("Triose", "PG13", "GAPDH; +2 NADH"),
            ("PG13", "PG3", "+2 ATP"),
            ("PG3", "PEP", "enolase"),
            ("PEP", "Pyr", "+2 ATP; PK"),
            ("Pyr", "Net", "per glucose"),
        ],
    )


def atp_synthesis_diagram() -> MermaidDiagram:
    """Show electron transport chain and ATP synthesis."""
    return flowchart(
        name="atp_synthesis",
        title="Oxidative Phosphorylation: Electron Flow to ATP",
        nodes=[
            ("NADH", "NADH electrons"),
            ("FADH", "FADH2 electrons"),
            ("CI", "Complex I pumps H+"),
            ("CII", "Complex II feeds Q"),
            ("Q", "Ubiquinone pool"),
            ("CIII", "Complex III pumps H+"),
            ("CIV", "Complex IV pumps H+"),
            ("Pm", "Proton-motive force"),
            ("ATP", "ATP synthase"),
            ("O2", "O2 reduced to water"),
            ("ATPP", "ADP + Pi to ATP"),
        ],
        edges=[
            ("NADH", "CI", "2 e-"),
            ("FADH", "CII", "2 e-"),
            ("CI", "Q", ""),
            ("CII", "Q", ""),
            ("Q", "CIII", ""),
            ("CIII", "CIV", "cytochrome c"),
            ("CIV", "O2", "terminal acceptor"),
            ("CI", "Pm", "4 H+"),
            ("CIII", "Pm", "4 H+"),
            ("CIV", "Pm", "2 H+"),
            ("Pm", "ATP", "H+ flow"),
            ("ATP", "ATPP", "rotary catalysis"),
        ],
        direction="LR",
    )


# ---------------------------------------------------------------------------
# Unit IV — Molecular Genetics
# ---------------------------------------------------------------------------


def cell_cycle_diagram() -> MermaidDiagram:
    """Show the eukaryotic cell cycle phases and checkpoints."""
    return state_diagram(
        name="cell_cycle",
        title="Eukaryotic Cell Cycle",
        states=["G1 (growth)", "S phase (DNA synthesis)", "G2 (preparation)", "Mitosis", "Cytokinesis"],
        transitions=[
            ("G1 (growth)", "S phase (DNA synthesis)", "G1 checkpoint"),
            ("S phase (DNA synthesis)", "G2 (preparation)", "DNA replication complete"),
            ("G2 (preparation)", "Mitosis", "G2/M checkpoint"),
            ("Mitosis", "Cytokinesis", "spindle checkpoint"),
            ("Cytokinesis", "G1 (growth)", "division complete"),
        ],
        initial_state="G1 (growth)",
    )


def transcription_translation_diagram() -> MermaidDiagram:
    """Central dogma: DNA → RNA → Protein."""
    return flowchart(
        name="central_dogma",
        title="The Central Dogma of Molecular Biology",
        nodes=[
            ("DNA", "DNA\n(double helix)"),
            ("mRNA", "mRNA\n(single strand)"),
            ("Ribo", "Ribosome\n(translation machinery)"),
            ("Prot", "Polypeptide / Protein"),
            ("Tx", "Transcription\n(nucleus; RNA polymerase)"),
            ("Sp", "RNA processing\n(splicing, capping, poly-A)"),
            ("Tl", "Translation\n(cytoplasm; tRNA, codons)"),
        ],
        edges=[
            ("DNA", "Tx", ""),
            ("Tx", "mRNA", "pre-mRNA"),
            ("mRNA", "Sp", ""),
            ("Sp", "Ribo", "mature mRNA"),
            ("Ribo", "Tl", ""),
            ("Tl", "Prot", ""),
        ],
    )


# ---------------------------------------------------------------------------
# Unit V — Classical Genetics
# ---------------------------------------------------------------------------


def mendelian_cross_diagram() -> MermaidDiagram:
    """Show a monohybrid Punnett square cross (Aa × Aa)."""
    return flowchart(
        name="mendelian_monohybrid",
        title="Monohybrid Cross: Aa × Aa",
        nodes=[
            ("P1", "Parent 1: Aa"),
            ("P2", "Parent 2: Aa"),
            ("G1A", "Gamete A"),
            ("G1a", "Gamete a"),
            ("G2A", "Gamete A"),
            ("G2a", "Gamete a"),
            ("AA", "AA (25%)\nDominant"),
            ("Aa1", "Aa (25%)\nDominant"),
            ("Aa2", "Aa (25%)\nDominant"),
            ("aa", "aa (25%)\nRecessive"),
        ],
        edges=[
            ("P1", "G1A", "meiosis"),
            ("P1", "G1a", "meiosis"),
            ("P2", "G2A", "meiosis"),
            ("P2", "G2a", "meiosis"),
            ("G1A", "AA", "+G2A"),
            ("G1A", "Aa1", "+G2a"),
            ("G1a", "Aa2", "+G2A"),
            ("G1a", "aa", "+G2a"),
        ],
    )


# ---------------------------------------------------------------------------
# Unit VI — Evolution
# ---------------------------------------------------------------------------


def natural_selection_diagram() -> MermaidDiagram:
    """Show the mechanism of natural selection."""
    return flowchart(
        name="natural_selection",
        title="Natural Selection: Heritable Variation to Adaptation",
        nodes=[
            ("Pop", "Population variation"),
            ("Her", "Heritable trait differences"),
            ("Env", "Environmental filter"),
            ("Fit", "Differential fitness"),
            ("Next", "Allele frequencies shift"),
            ("Adap", "Adaptation over generations"),
        ],
        edges=[
            ("Pop", "Her", "genetic basis"),
            ("Her", "Env", "phenotypes exposed"),
            ("Env", "Fit", "selection"),
            ("Fit", "Next", "non-random reproduction"),
            ("Next", "Adap", "repeated cycles"),
            ("Adap", "Pop", "new population"),
        ],
    )


def phylogenetic_tree_diagram() -> MermaidDiagram:
    """Show a simplified phylogenetic tree of life."""
    return flowchart(
        name="phylogenetic_tree",
        title="Tree of Life: Domains and Eukaryogenesis",
        nodes=[
            ("LUCA", "Last Universal Common Ancestor"),
            ("Bac", "Bacteria"),
            ("Arc", "Archaea"),
            ("Host", "Asgard-like archaeal host"),
            ("Endo", "Bacterial endosymbiont"),
            ("Euk", "Eukarya"),
            ("Prot", "Protists"),
            ("Fung", "Fungi"),
            ("Plant", "Plants"),
            ("Anim", "Animals"),
        ],
        edges=[
            ("LUCA", "Bac", "~3.8 Ga"),
            ("LUCA", "Arc", "~3.8 Ga"),
            ("Arc", "Host", "archaeal lineage"),
            ("Bac", "Endo", "alphaproteobacterium"),
            ("Host", "Euk", "host cell"),
            ("Endo", "Euk", "mitochondrion"),
            ("Euk", "Prot", ""),
            ("Euk", "Fung", ""),
            ("Euk", "Plant", ""),
            ("Euk", "Anim", ""),
        ],
    )


# ---------------------------------------------------------------------------
# Unit VII — Microbiology
# ---------------------------------------------------------------------------


def viral_replication_cycle_diagram() -> MermaidDiagram:
    """Show the lytic viral replication cycle."""
    return flowchart(
        name="viral_lytic_cycle",
        title="Lytic Viral Replication Cycle",
        nodes=[
            ("V", "Free virion"),
            ("Att", "Attachment to receptor"),
            ("Entry", "Genome entry"),
            ("Ecl", "Eclipse phase"),
            ("Rep", "Genome replication"),
            ("Prot", "Viral protein synthesis"),
            ("Ass", "Capsid assembly"),
            ("Lys", "Cell lysis"),
            ("Rel", "Virion release"),
        ],
        edges=[
            ("V", "Att", "host range"),
            ("Att", "Entry", "penetration"),
            ("Entry", "Ecl", "no infectious virus"),
            ("Ecl", "Rep", "host machinery"),
            ("Rep", "Prot", "mRNA expression"),
            ("Prot", "Ass", "structural proteins"),
            ("Ass", "Lys", "burst"),
            ("Lys", "Rel", "new virions"),
            ("Rel", "V", "new virions"),
        ],
    )


# ---------------------------------------------------------------------------
# Unit VIII — Botany
# ---------------------------------------------------------------------------


def photosynthesis_light_dark_diagram() -> MermaidDiagram:
    """Show light-dependent and light-independent reactions."""
    return flowchart(
        name="photosynthesis_reactions",
        title="Photosynthesis: Light Reactions and Calvin-Benson Cycle",
        nodes=[
            ("Sun", "Sunlight"),
            ("LR", "Light reactions"),
            ("H2O", "H₂O (oxidised)"),
            ("ATP_N", "ATP + NADPH"),
            ("O2", "O₂ (released)"),
            ("Cal", "Calvin-Benson cycle"),
            ("CO2", "CO₂ (fixed by RuBisCO)"),
            ("G3P", "G3P sugar precursor"),
            ("RuBP", "RuBP regenerated"),
            ("Glu", "Sucrose/starch synthesis"),
        ],
        edges=[
            ("Sun", "LR", "absorbed by chlorophyll"),
            ("H2O", "LR", "electron donor"),
            ("LR", "ATP_N", ""),
            ("LR", "O2", "byproduct"),
            ("ATP_N", "Cal", "powers"),
            ("CO2", "Cal", "reactant"),
            ("Cal", "G3P", "carbon export"),
            ("Cal", "RuBP", "regeneration"),
            ("RuBP", "Cal", "CO2 acceptor"),
            ("G3P", "Glu", "biosynthesis"),
        ],
        direction="LR",
    )


# ---------------------------------------------------------------------------
# Unit IX — Zoology & Systems Physiology
# ---------------------------------------------------------------------------


def nervous_system_reflex_diagram() -> MermaidDiagram:
    """Show a spinal reflex arc."""
    return sequence_diagram(
        name="reflex_arc",
        title="Spinal Reflex Arc",
        participants=[
            "Stimulus",
            "Sensory Receptor",
            "Sensory Neuron",
            "Spinal Cord",
            "Motor Neuron",
            "Effector Muscle",
        ],
        messages=[
            ("Stimulus", "Sensory Receptor", "noxious stimulus"),
            ("Sensory Receptor", "Sensory Neuron", "action potential"),
            ("Sensory Neuron", "Spinal Cord", "afferent signal"),
            ("Spinal Cord", "Motor Neuron", "efferent signal"),
            ("Motor Neuron", "Effector Muscle", "contraction (withdrawal)"),
        ],
    )


def immune_response_diagram() -> MermaidDiagram:
    """Show innate and adaptive immune responses."""
    return flowchart(
        name="immune_response",
        title="Immune Response Overview",
        nodes=[
            ("Path", "Pathogen\n(antigen)"),
            ("Innate", "Innate Immunity\n(immediate)"),
            ("Phag", "Phagocytes\n(neutrophils, macrophages)"),
            ("Inflam", "Inflammation\n(cytokines)"),
            ("APC", "Antigen-Presenting\nCell (dendritic)"),
            ("Adapt", "Adaptive Immunity\n(delayed, specific)"),
            ("TH", "Helper T cell\n(CD4+)"),
            ("TC", "Cytotoxic T cell\n(CD8+)"),
            ("B", "B cell → Plasma cell"),
            ("Ab", "Antibodies\n(humoral immunity)"),
            ("Mem", "Memory cells\n(long-lived)"),
        ],
        edges=[
            ("Path", "Innate", "triggers"),
            ("Innate", "Phag", ""),
            ("Innate", "Inflam", ""),
            ("Phag", "APC", "presents antigen"),
            ("APC", "Adapt", "activates"),
            ("Adapt", "TH", ""),
            ("Adapt", "TC", ""),
            ("Adapt", "B", ""),
            ("TH", "B", "activates"),
            ("B", "Ab", "secretes"),
            ("TH", "Mem", ""),
            ("TC", "Mem", ""),
            ("B", "Mem", ""),
        ],
    )


# ---------------------------------------------------------------------------
# Unit X — Ecology
# ---------------------------------------------------------------------------


def food_web_diagram() -> MermaidDiagram:
    """Show a simplified terrestrial food web."""
    return flowchart(
        name="terrestrial_food_web",
        title="Terrestrial Food Web and Nutrient Recycling",
        nodes=[
            ("Sun", "Solar Energy"),
            ("Pl", "Plants (producers)"),
            ("Ins", "Insects (herbivores)"),
            ("Sm", "Small mammals"),
            ("Bird", "Insectivorous birds"),
            ("Fox", "Fox"),
            ("Hk", "Hawk"),
            ("Det", "Detritus"),
            ("Dec", "Decomposers"),
            ("Nutr", "Mineral nutrients"),
        ],
        edges=[
            ("Sun", "Pl", "photosynthesis"),
            ("Pl", "Ins", "herbivory"),
            ("Pl", "Sm", "herbivory"),
            ("Ins", "Bird", "predation"),
            ("Sm", "Fox", "predation"),
            ("Bird", "Hk", "predation"),
            ("Fox", "Hk", "predation"),
            ("Pl", "Det", "litter"),
            ("Ins", "Det", "death"),
            ("Sm", "Det", "death"),
            ("Bird", "Det", "death"),
            ("Fox", "Det", "death"),
            ("Hk", "Det", "death"),
            ("Det", "Dec", "decomposition"),
            ("Dec", "Nutr", "mineralization"),
            ("Nutr", "Pl", "uptake"),
        ],
        direction="LR",
    )


def population_growth_stages_diagram() -> MermaidDiagram:
    """Show phases of logistic population growth.

    Short state tokens avoid mmdc stateDiagram-v2 reserved-word / parsing edge cases.
    """
    return state_diagram(
        name="population_growth_phases",
        title="Logistic Population Growth Phases",
        states=["Lag", "Exponential", "Decelerating", "Stationary"],
        transitions=[
            ("Lag", "Exponential", "population establishes"),
            ("Exponential", "Decelerating", "N approaches K/2"),
            ("Decelerating", "Stationary", "N near K"),
            ("Stationary", "Decelerating", "resource pulse"),
        ],
        initial_state="Lag",
        final_states=[],
    )


# ---------------------------------------------------------------------------
# New diagrams (batch 2)
# ---------------------------------------------------------------------------


def speciation_diagram() -> MermaidDiagram:
    """Speciation mechanisms: allopatric, sympatric, and polyploidy."""
    return flowchart(
        name="speciation_diagram",
        title="Speciation Mechanisms",
        nodes=[
            ("A", "Ancestral Population"),
            ("B", "Allopatric Speciation"),
            ("C", "Sympatric Speciation"),
            ("D", "Polyploidy Speciation"),
            ("B1", "Independent genetic drift"),
            ("B2", "Dobzhansky-Muller incompatibilities"),
            ("B3", "Reproductive isolation complete"),
            ("C1", "Disruptive natural selection"),
            ("C2", "Assortative mating"),
            ("C3", "Host-race divergence"),
            ("D1", "Autopolyploidy 4n"),
            ("D2", "Allopolyploid hybridization"),
            ("D3", "Instant reproductive isolation"),
        ],
        edges=[
            ("A", "B", "geographic barrier"),
            ("A", "C", "ecological divergence"),
            ("A", "D", "genome duplication"),
            ("B", "B1", ""),
            ("B1", "B2", ""),
            ("B2", "B3", ""),
            ("C", "C1", ""),
            ("C1", "C2", ""),
            ("C2", "C3", "sympatric outcome"),
            ("D", "D1", ""),
            ("D", "D2", ""),
            ("D2", "D3", "chromosome doubling"),
        ],
        direction="TD",
    )


def hormone_signaling_diagram() -> MermaidDiagram:
    """GPCR cAMP/IP3 and RTK PI3K/Akt/mTOR signalling pathways."""
    return flowchart(
        name="hormone_signaling_diagram",
        title="Hormone Signalling Pathways",
        nodes=[
            ("H1", "Peptide hormone"),
            ("H2", "Steroid hormone"),
            ("H3", "Insulin RTK"),
            ("R1", "GPCR surface receptor"),
            ("R2", "Nuclear Receptor NR"),
            ("AC", "Adenylyl Cyclase"),
            ("PLC", "Phospholipase C"),
            ("cAMP", "cAMP second messenger"),
            ("PKA", "PKA kinase"),
            ("CREB", "CREB gene expression"),
            ("IP3", "IP3 ER Ca2+ release"),
            ("DAG", "DAG PKC activation"),
            ("IRS", "IRS1/2 adaptor"),
            ("PI3K", "PI3K PIP3"),
            ("Akt", "Akt PKB"),
            ("GLUT4", "GLUT4 glucose uptake"),
            ("mTOR", "mTORC1 protein synthesis"),
            ("HRE", "Hormone Response Element"),
            ("Tx", "Transcriptional activation"),
        ],
        edges=[
            ("H1", "R1", "cannot cross membrane"),
            ("H2", "R2", "diffuses in"),
            ("H3", "IRS", "RTK autophosphorylation"),
            ("R1", "AC", "Gs coupling"),
            ("R1", "PLC", "Gq coupling"),
            ("AC", "cAMP", ""),
            ("cAMP", "PKA", ""),
            ("PKA", "CREB", ""),
            ("PLC", "IP3", ""),
            ("PLC", "DAG", ""),
            ("IRS", "PI3K", ""),
            ("PI3K", "Akt", "PIP3"),
            ("Akt", "GLUT4", ""),
            ("Akt", "mTOR", ""),
            ("R2", "HRE", "LBD plus DBD"),
            ("HRE", "Tx", ""),
        ],
        direction="TD",
    )


def dna_replication_diagram() -> MermaidDiagram:
    """DNA replication fork machinery: origin firing through Okazaki maturation."""
    return flowchart(
        name="dna_replication_diagram",
        title="DNA Replication Fork Machinery",
        nodes=[
            ("ORC", "ORC marks origin"),
            ("MCM", "Mcm2-7 loaded in G1"),
            ("CMG", "CMG helicase fires"),
            ("Fork", "Replication fork"),
            ("Lead", "Leading strand Pol epsilon"),
            ("Lag", "Lagging strand"),
            ("Ldone", "Leading strand product"),
            ("PrimA", "Pol alpha-primase RNA primer"),
            ("OkA", "Pol delta extends Okazaki fragment"),
            ("Nick", "Nick in lagging strand"),
            ("Gap", "Gap filled"),
            ("LigDone", "Okazaki fragment matured"),
            ("PCNA", "PCNA sliding clamp"),
        ],
        edges=[
            ("ORC", "MCM", ""),
            ("MCM", "CMG", "S-CDK plus DDK"),
            ("CMG", "Fork", "unwinds dsDNA"),
            ("Fork", "Lead", ""),
            ("Fork", "Lag", ""),
            ("Lead", "Ldone", "continuous 5to3"),
            ("Lag", "PrimA", ""),
            ("PrimA", "OkA", ""),
            ("OkA", "Nick", "FEN1 flap removal"),
            ("Nick", "Gap", "DNA Pol delta fill"),
            ("Gap", "LigDone", "LIG1 plus ATP"),
            ("PCNA", "Lead", "PIP box"),
            ("PCNA", "OkA", "PIP box"),
            ("PCNA", "Nick", "PIP box"),
        ],
        direction="LR",
    )


def nutrient_cycle_diagram() -> MermaidDiagram:
    """Nitrogen biogeochemical cycle: fixation, nitrification, denitrification."""
    return flowchart(
        name="nutrient_cycle_diagram",
        title="Nitrogen Biogeochemical Cycle",
        nodes=[
            ("Atm", "Atmospheric N2"),
            ("NH3", "Ammonium NH4+"),
            ("NO2", "Nitrite NO2-"),
            ("NO3", "Nitrate NO3-"),
            ("Plant", "Plant protein"),
            ("Animal", "Animal protein"),
            ("OM", "Organic detritus"),
            ("N2O", "N2O greenhouse gas"),
            ("N2", "N2 returned to atmosphere"),
            ("Aquatic", "Aquatic eutrophication"),
        ],
        edges=[
            ("Atm", "NH3", "fixation by diazotrophs"),
            ("NH3", "NO2", "Nitrosomonas nitrification"),
            ("NO2", "NO3", "Nitrobacter nitrification"),
            ("NO3", "Plant", "plant uptake"),
            ("Plant", "Animal", "herbivory"),
            ("Animal", "OM", "death and excretion"),
            ("OM", "NH3", "decomposers ammonification"),
            ("NO3", "N2O", "partial denitrification"),
            ("N2O", "N2", "complete denitrification"),
            ("N2", "Atm", ""),
            ("NO3", "Aquatic", "leaching and runoff"),
        ],
        direction="TD",
    )


def chromosome_inheritance_diagram() -> MermaidDiagram:
    """X-inactivation, dosage compensation, and sex-linked inheritance."""
    return flowchart(
        name="chromosome_inheritance_diagram",
        title="Sex-Linked Inheritance and X-Inactivation",
        nodes=[
            ("Dev", "Female embryo XX cell"),
            ("Xi", "X-inactivation begins blastocyst"),
            ("Barr", "Barr body inactive X"),
            ("Mosaic", "Somatic mosaicism"),
            ("App", "Calico cat orange black patches"),
            ("AD", "Ectodermal dysplasia mosaic females"),
            ("SL", "X-linked recessive trait"),
            ("Off", "Offspring"),
            ("Carr", "Carrier daughters XAXa"),
            ("Aff", "Affected sons XaY"),
            ("Norm", "Normal sons XAY"),
        ],
        edges=[
            ("Dev", "Xi", "Day 5-7 XIST RNA"),
            ("Xi", "Barr", "random per cell"),
            ("Barr", "Mosaic", "clonal propagation"),
            ("Mosaic", "App", ""),
            ("Mosaic", "AD", ""),
            ("SL", "Off", "carrier mother XAXa"),
            ("Off", "Carr", ""),
            ("Off", "Aff", ""),
            ("Off", "Norm", ""),
        ],
        direction="TD",
    )


def mirna_biogenesis_diagram() -> MermaidDiagram:
    """miRNA biogenesis: pri-miRNA processing through RISC loading."""
    return flowchart(
        name="mirna_biogenesis_diagram",
        title="miRNA Biogenesis and RISC Loading",
        nodes=[
            ("Pol2", "RNA Pol II\ntranscription"),
            ("Pri", "pri-miRNA\nstem-loop"),
            ("Drosha", "Microprocessor\nDrosha DGCR8"),
            ("Pre", "pre-miRNA\n70 nt"),
            ("Export", "Exportin-5\nRanGTP"),
            ("Cyto", "Cytoplasm"),
            ("Dicer", "Dicer TRBP"),
            ("Duplex", "miRNA miRNA*\nduplex"),
            ("RISC", "AGO2 RISC\nmature strand"),
            ("Target", "mRNA silencing\ntranslational block"),
        ],
        edges=[
            ("Pol2", "Pri", ""),
            ("Pri", "Drosha", "nucleus"),
            ("Drosha", "Pre", ""),
            ("Pre", "Export", ""),
            ("Export", "Cyto", ""),
            ("Cyto", "Dicer", ""),
            ("Dicer", "Duplex", ""),
            ("Duplex", "RISC", "strand selection"),
            ("RISC", "Target", ""),
        ],
        direction="TD",
    )


def x_inactivation_diagram() -> MermaidDiagram:
    """X-chromosome inactivation: XIST coating and heterochromatin assembly."""
    return flowchart(
        name="x_inactivation_diagram",
        title="X-Inactivation — XIST RNA and Heterochromatin",
        nodes=[
            ("XX", "Early XX somatic cell"),
            ("Count", "Count X chromosomes"),
            ("Choice", "Choose future inactive X"),
            ("Xa", "Xa remains transcriptionally active"),
            ("Xi", "Xi initiates silencing"),
            ("XIST", "XIST RNA coats Xi in cis"),
            ("Polycomb", "Polycomb marks H3K27me3 and H2AK119ub"),
            ("DNAme", "DNA methylation and late replication stabilize silence"),
            ("Escape", "Escape genes remain partially active"),
            ("Barr", "Condensed Barr body"),
            ("Mosaic", "Mitotic inheritance creates tissue mosaicism"),
        ],
        edges=[
            ("XX", "Count", "early embryo"),
            ("Count", "Choice", ""),
            ("Choice", "Xa", ""),
            ("Choice", "Xi", ""),
            ("Xi", "XIST", "cis spreading"),
            ("XIST", "Polycomb", "recruitment"),
            ("Polycomb", "DNAme", "maintenance"),
            ("DNAme", "Barr", "compaction"),
            ("Barr", "Mosaic", "cell divisions"),
            ("Xi", "Escape", "incomplete silencing"),
        ],
        direction="TD",
    )


# ---------------------------------------------------------------------------
# All Diagrams Registry
# ---------------------------------------------------------------------------

ALL_BIOLOGY_DIAGRAMS: list[MermaidDiagram] = [
    macromolecule_classification_diagram(),
    enzyme_kinetics_diagram(),
    organelle_function_diagram(),
    membrane_transport_diagram(),
    glycolysis_pathway_diagram(),
    atp_synthesis_diagram(),
    cell_cycle_diagram(),
    transcription_translation_diagram(),
    mendelian_cross_diagram(),
    natural_selection_diagram(),
    phylogenetic_tree_diagram(),
    viral_replication_cycle_diagram(),
    photosynthesis_light_dark_diagram(),
    nervous_system_reflex_diagram(),
    immune_response_diagram(),
    food_web_diagram(),
    population_growth_stages_diagram(),
    # Batch 2 (added for comprehensive coverage)
    speciation_diagram(),
    hormone_signaling_diagram(),
    dna_replication_diagram(),
    nutrient_cycle_diagram(),
    chromosome_inheritance_diagram(),
    mirna_biogenesis_diagram(),
    x_inactivation_diagram(),
]
