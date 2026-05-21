#!/usr/bin/env python3
# ruff: noqa: E501
"""Embedded enrichment pass for the biology textbook.

The script is intentionally conservative: it does not add chapters, labs, or
question banks. It embeds reusable frontier/evidence material into existing
chapters, adds paper-based evidence upgrades to labs, upgrades templated answer
keys, and writes an audit matrix for future editorial passes.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import partial
from pathlib import Path
import re
import sys

PROJECT = Path(__file__).resolve().parent.parent
SCRIPT_DIR = PROJECT / "scripts"
MANUSCRIPT = PROJECT / "manuscript"
DOCS = PROJECT / "docs"
SRC = PROJECT / "src"
TEMPLATE_ROOT = PROJECT.parent.parent

for import_path in (SCRIPT_DIR, SRC, TEMPLATE_ROOT, PROJECT):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from scripts.add_mermaid_alt_text import normalize_text  # noqa: E402
from scripts.atomic_io import write_text_atomic  # noqa: E402


@dataclass(frozen=True)
class ChapterRecord:
    unit_id: str
    unit_title: str
    file: str
    title: str

    @property
    def stem(self) -> str:
        return Path(self.file).stem

    @property
    def chapter_path(self) -> Path:
        return MANUSCRIPT / self.unit_id / self.file

    @property
    def lab_path(self) -> Path:
        return MANUSCRIPT / "labs" / self.unit_id / f"lab_{self.stem}.md"

    @property
    def question_path(self) -> Path:
        return MANUSCRIPT / "questions" / self.unit_id / f"questions_{self.stem}.md"

    @property
    def section_ref(self) -> str:
        return f"sec:{self.unit_id}_{self.stem}"


def load_book_toc():
    from biology.toc import load_toc

    return load_toc(PROJECT)


def chapter_records() -> list[ChapterRecord]:
    return [
        ChapterRecord(
            unit_id=chapter.unit_id,
            unit_title=chapter.unit_title,
            file=chapter.file,
            title=chapter.title,
        )
        for chapter in load_book_toc().chapters
    ]


FRONTIER_BY_UNIT: dict[str, tuple[str, str]] = {
    "unit_0": (
        "Systems models are useful when they expose assumptions, uncertainty, and failure modes rather than merely producing elegant diagrams.",
        "Treat every model as a claim about mechanism: define the system boundary, identify the observable that would falsify the model, and report the uncertainty that would change a decision.",
    ),
    "unit_I": (
        "Chemistry-of-life claims now connect classical bonding and thermodynamics with AI-guided structure prediction and experimental validation.",
        "Use AI biomolecular models as hypothesis generators: compare confidence, conservation, solvent exposure, and assay evidence before turning a predicted contact into a biological claim \\citep{abramson2024alphafold3}.",
    ),
    "unit_II": (
        "Cell biology is increasingly measured as live, spatial, single-cell, and perturbational data rather than static diagrams alone.",
        "Ask what measurement scale is being claimed: nanometre structure, single-cell transcript abundance, organelle dynamics, tissue context, or organismal phenotype.",
    ),
    "unit_III": (
        "Metabolism is now studied as a regulated network constrained by energy, redox balance, compartmentation, and environment.",
        "A strong metabolic explanation names the flux, the limiting step, the sensor, and the condition under which the pathway changes direction or priority.",
    ),
    "unit_IV": (
        "Molecular genetics now spans single-reference sequences, telomere-to-telomere assemblies, pangenome graphs, long-read sequencing, CRISPR medicines, and ethical deployment.",
        "When a genomic claim depends on a reference, ask whether short reads, structural variants, ancestry representation, phasing, or clinical validation could change the interpretation \\citep{humanpangenome2023,fda2023casgevy,fda2024casgevythalassemia}.",
    ),
    "unit_V": (
        "Classical genetics remains essential, but modern interpretation adds penetrance, polygenicity, structural variation, ancestry-aware inference, and uncertainty in risk prediction.",
        "A good genetics answer separates the Mendelian transmission model from the evidence needed to use it in a population, family, or clinical setting.",
    ),
    "unit_VI": (
        "Evolutionary claims are strongest when they combine mechanism, comparative evidence, population process, and explicit uncertainty.",
        "Distinguish adaptation from drift, phylogenetic signal from convergence, and historical explanation from a testable prediction about present-day data.",
    ),
    "unit_VII": (
        "Microbiology and infectious disease now require One Health reasoning across people, animals, environments, genomics, and antimicrobial stewardship.",
        "For AMR and pathogen claims, name the organism-resistance pair, the selection pressure, the transmission route, and the surveillance evidence that would change triage \\citep{who2024bppl,cdc2025antibioticuse,murray2022amr}.",
    ),
    "unit_VIII": (
        "Plant biology links molecular regulation to climate stress, water limitation, crop resilience, phenology, and ecosystem feedbacks.",
        "A strong plant explanation names the tissue, signal, environmental driver, measurable trait, and tradeoff between growth, reproduction, defence, and water use.",
    ),
    "unit_IX": (
        "Physiology now blends mechanism with allostasis, immune-endocrine-neural coupling, wearable data, and individualized risk without reducing bodies to simple machines.",
        "Interpret physiological data by separating baseline variation, perturbation response, compensation, and the threshold where compensation becomes pathology.",
    ),
    "unit_X": (
        "Ecology and conservation decisions increasingly combine field data, remote sensing, community knowledge, model uncertainty, and explicit values.",
        "Use biodiversity metrics carefully: population indices, extinction risk categories, ecosystem services, and management targets answer different questions \\citep{ipbes2019global,ipbes2024transformative,wwf2024livingplanet,iucn2025redlist,fao2024sofia}.",
    ),
}


SOURCE_PRACTICE_BY_UNIT: dict[str, str] = {
    "unit_0": "Use model-validation sources when available, and state which observation would falsify the model rather than treating a diagram as proof.",
    "unit_I": "For structure and interaction claims, cite experimental structures when available and treat AlphaFold 3 or AFDB complex predictions as hypotheses to validate with confidence metrics, conservation, mutagenesis, binding, or cryo-EM/X-ray/NMR evidence \\citep{abramson2024alphafold3,velankar2026alphafolddb2025,emblebi2026alphafoldcomplexes}.",
    "unit_II": "For cell-state claims, distinguish microscopy, live-cell perturbation, single-cell sequencing, spatial transcriptomics, and biochemical assay evidence before making a causal statement.",
    "unit_III": "For metabolic claims, keep the organism, compartment, energetic state, and measurement method visible; a pathway map is not enough without flux or concentration evidence.",
    "unit_IV": "For genomics and editing claims, distinguish discovery from clinical actionability, and cite reference resources, regulatory records, or primary editing studies close to the claim \\citep{humanpangenome2023,fda2026casgevy,chalumeau2025primeediting}.",
    "unit_V": "For inheritance and population claims, separate the model assumptions from sampling, ancestry representation, penetrance, linkage, and environment.",
    "unit_VI": "For evolutionary claims, prefer evidence that compares alternatives such as selection, drift, gene flow, constraint, convergence, and shared ancestry.",
    "unit_VII": "For pathogen, AMR, and intervention claims, tie statements to organism-resistance pairs, surveillance evidence, official guidance, and trial/regulatory status \\citep{who2024bppl,who2025tb,who2025malaria,cdc2025lenacapavirprep,cdc2026candidaauris}.",
    "unit_VIII": "For plant-stress and crop claims, name the tissue, environmental driver, field context, and growth-reproduction tradeoff; separate laboratory potential from agronomic adoption.",
    "unit_IX": "For physiology claims, cite the measurement context and distinguish baseline variation, compensation, pathophysiology, and treatment evidence.",
    "unit_X": "For conservation claims, cite assessment sources and state whether the evidence is a population index, extinction-risk assessment, ecosystem-service valuation, satellite product, or policy synthesis \\citep{ipbes2024transformative,noaa2025coralbleaching,fao2025sofi}.",
}


EXTRA_FRONTIER_BY_STEM: dict[str, str] = {
    "cell_theory": "Single-cell atlases are most useful when they clarify the sampled tissue, donor context, assay chemistry, and annotation uncertainty; Human Cell Atlas-style resources turn cell theory into a measurable census, but they do not remove the need for perturbation evidence \\citep{regev2017humancellatlas,pan2024singlecellatlas}.",
    "membrane_transport": "Mechanosensitive channel claims should name the force, lipid environment, oligomeric state, and assay context; TMEM63 channelopathy work links structural rearrangement to disease mutations, so the mechanism should remain tied to the channel family and assay context \\citep{zheng2025tmem63channelopathies}.",
    "photosynthesis": "Carbonyl-sulfide tracer work turns global GPP into an explicitly physiological inference about CO2 diffusion through stomata and mesophyll, so carbon-cycle claims should report the tracer, diffusion assumptions, and biome context rather than treating satellite greenness as a direct proxy for photosynthesis \\citep{lai2024gppcarbonylsulfide}.",
    "plant_structure_and_water": "Hydraulic safety claims should also be benchmarked against comparative vulnerability data: globally, many forest species operate close to xylem failure thresholds, so drought tolerance must be framed as a margin rather than a binary trait \\citep{choat2012hydraulicmargins}.",
    "plant_responses": "Heat-stress responses should be separated by tissue and developmental stage: protecting vegetative leaves is not the same as preserving male reproductive success, where epigenetic regulation and pollen development can be the limiting failure point \\citep{malik2022heatstressmale}. Guard-cell calcium work shows that stomatal dynamics can depend on the count and timing of unitary cytosolic Ca2+ signals, linking ion-channel physiology to whole-plant water tradeoffs without implying plant decision-making is animal-like cognition \\citep{huang2024guardcells}.",
    "ecosystem_ecology": "Vegetation-carbon claims are measurement-sensitive: daily rainfall variability can strongly affect global vegetation activity, so ecosystem productivity arguments should distinguish total precipitation from event timing and intensity \\citep{feldman2024rainfallvariability}.",
}


FOCUS_BY_STEM: dict[str, str] = {
    "systems_science": "system boundary choice, feedback sign, and scale determine whether a model explains or hides the biology.",
    "complex_adaptive_systems": "agent rules, heterogeneity, stochasticity, and path dependence make biological prediction conditional rather than absolute.",
    "active_inference": "active-inference explanations must connect hidden states, sensory evidence, action, and measurable prediction error.",
    "atoms_molecules": "molecular claims need charge, polarity, geometry, concentration, and solvent context.",
    "water_and_life": "water's biological effects depend on hydrogen bonding, colligative context, interfaces, temperature, and solute identity.",
    "macromolecules": "macromolecule explanations should connect sequence, structure, dynamics, modification, interaction, and assay evidence.",
    "enzymes_and_kinetics": "enzyme claims should separate binding, catalysis, regulation, transport limits, and measurement conditions.",
    "cell_theory": "cell-theory evidence now includes microscopy, lineage tracing, omics, and synthetic-cell boundary tests.",
    "cell_structure": "organelle function is dynamic, contact-mediated, and context-dependent rather than a fixed list of compartments.",
    "membrane_transport": "transport claims require gradients, permeability, electrochemical driving force, gating, and energy coupling.",
    "cell_signaling": "signalling explanations should include receptor context, dose, timing, feedback, crosstalk, and cellular state.",
    "bioenergetics_and_respiration": "respiration claims should track electrons, protons, redox poise, ATP yield, and uncoupling.",
    "photosynthesis": "photosynthesis claims should distinguish light capture, carbon fixation, photorespiration, water stress, and canopy context.",
    "metabolic_integration": "metabolic integration depends on compartmentation, hormone state, nutrient availability, and time scale.",
    "dna_replication_and_cell_cycle": "replication claims should connect polymerase accuracy, checkpoint timing, damage response, and cancer relevance.",
    "gene_expression": "expression claims should separate transcription, RNA processing, translation, localization, degradation, and feedback.",
    "mutations_and_genomics": "genomics claims should distinguish variant discovery, pathogenic interpretation, ancestry representation, and clinical actionability.",
    "epigenetics_and_gene_regulation": "epigenetic claims require causal perturbation, cell-type specificity, timing, and inheritance controls.",
    "mendelian_genetics": "Mendelian patterns are starting models that must be qualified by penetrance, linkage, environment, and sampling.",
    "chromosomal_inheritance": "chromosome-scale inheritance depends on recombination, segregation, structural variation, and dosage compensation.",
    "population_genetics": "allele-frequency explanations should name the force, parameter values, assumptions, and data needed to distinguish forces.",
    "evolution_and_selection": "selection claims need fitness components, ecological context, genetic variation, and alternative hypotheses.",
    "genetic_drift_and_speciation": "speciation claims should separate gene flow, reproductive isolation, demographic history, and genomic architecture.",
    "phylogenetics": "phylogenetic confidence depends on sampling, model choice, homology, conflict among loci, and calibration.",
    "bacteria_archaea_viruses": "microbial claims should identify taxonomy, genome architecture, metabolism, resistance mechanism, and environment.",
    "microbial_ecology": "microbiome claims should distinguish correlation, mechanism, host context, perturbation, and causality.",
    "infectious_disease": "infectious-disease reasoning should connect pathogen biology, transmission, immunity, diagnostics, interventions, and equity.",
    "plant_structure_and_water": "plant-water claims require water potential, hydraulic pathway, stomatal control, tissue anatomy, and stress context.",
    "plant_reproduction": "plant reproduction links pollination, development, genetics, phenology, dispersal, and environmental filtering.",
    "plant_responses": "plant response claims should connect signal perception, hormone network, gene expression, phenotype, and tradeoff.",
    "circulation_respiration_homeostasis": "homeostasis claims should connect flow, diffusion, control loops, reserve capacity, and measurement limits.",
    "nervous_system": "neural explanations should separate circuit architecture, glial support, plasticity, behaviour, and evidence scale.",
    "action_potential_synapses": "synaptic claims require ion-channel timing, driving force, transmitter release, receptor dynamics, and plasticity.",
    "endocrine_and_immune": "endocrine-immune claims should include feedback, timing, receptor sensitivity, inflammation, and allostatic load.",
    "population_ecology": "population claims require density dependence, demographic stochasticity, dispersal, age structure, and management objective.",
    "community_ecology": "community claims should identify interaction type, network position, disturbance regime, and observational limits.",
    "ecosystem_ecology": "ecosystem claims should track stocks, fluxes, residence times, boundaries, and coupled cycles.",
    "biomes_and_conservation": "conservation claims must separate ecological evidence, social values, feasibility, and uncertainty in tradeoffs.",
}


FIGURE_BY_STEM: dict[str, tuple[str, str, str, str]] = {
    "macromolecules": (
        "AI Structure Claims Need Validation",
        """flowchart LR
    A["Sequence or complex question"] --> B["AFDB or AlphaFold 3 model"]
    B --> C["Confidence and PAE check"]
    C --> D["Interface or active-site hypothesis"]
    D --> E["Conservation and mutagenesis"]
    E --> F["Binding, kinetics, or structure test"]
    F --> G["Qualified biological claim"]""",
        "Workflow for turning an AI-predicted protein or protein-complex model into a testable, qualified biological claim.",
        "AI structure models are strongest when confidence, interface geometry, conservation, mutagenesis, and experimental assays converge rather than when a model is treated as final evidence \\citep{abramson2024alphafold3,velankar2026alphafolddb2025,emblebi2026alphafoldcomplexes}.",
    ),
    "enzymes_and_kinetics": (
        "Enzyme Engineering Evidence Chain",
        """flowchart LR
    A["Catalytic problem"] --> B["Structure or model"]
    B --> C["Residue hypothesis"]
    C --> D["Variant library"]
    D --> E["Kinetic screen"]
    E --> F["Specificity and stability"]
    F --> G["Application decision"]""",
        "Evidence chain for enzyme engineering from structural hypothesis to kinetic, specificity, and stability evidence.",
        "Enzyme-engineering claims need rate, specificity, stability, and context; a better active-site story is not enough without quantitative kinetics.",
    ),
    "cell_structure": (
        "Membrane-Bound and Condensate Organization",
        """flowchart TD
    A["Cell organization"] --> B["Membrane-bound organelles"]
    A --> C["Biomolecular condensates"]
    B --> D["Lipid barrier and lumen"]
    C --> E["Weak multivalent interactions"]
    E --> F["Concentration threshold"]
    F --> G["Dynamic assembly"]
    G --> H["Function or disease risk"]""",
        "Comparison of classical membrane-bounded compartments with dynamic biomolecular condensates assembled by weak multivalent interactions.",
        "Condensates should be taught as regulatable cellular organization, not as a replacement for membrane-bound organelles or as proof of causality by appearance alone.",
    ),
    "cell_signaling": (
        "Spatial Single-Cell Signalling Evidence",
        """flowchart LR
    A["Tissue sample"] --> B["Spatial transcriptomics"]
    A --> C["Perturbation assay"]
    B --> D["Cell-state map"]
    C --> E["Changed pathway activity"]
    D --> F["Neighbour context"]
    E --> F
    F --> G["Causal signalling model"]""",
        "How spatial transcriptomics and perturbation evidence combine to support a cell-signalling model.",
        "A signalling claim is stronger when receptor state, ligand source, cell neighbourhood, and perturbation response point to the same mechanism.",
    ),
    "membrane_transport": (
        "Transporter Structure to Function",
        """flowchart LR
    A["Predicted transporter fold"] --> B["Cavity and gate residues"]
    B --> C["Substrate or ion hypothesis"]
    C --> D["Mutagenesis panel"]
    D --> E["Transport assay"]
    E --> F["State-cycle model"]""",
        "Workflow linking a predicted membrane-transporter structure to mutagenesis, transport assays, and state-cycle interpretation.",
        "Transporter structure claims need functional assays because transport depends on cycling among states, not a single static conformation \\citep{abramson2024alphafold3,varadi2024alphafolddb}.",
    ),
    "bioenergetics_and_respiration": (
        "Respiration Evidence Accounting",
        """flowchart LR
    A["Carbon substrate"] --> B["Electron carriers"]
    B --> C["Proton gradient"]
    C --> D["ATP synthase"]
    C --> E["Leak or uncoupling"]
    D --> F["ATP yield"]
    E --> G["Heat or lower efficiency"]
    F --> H["Physiological interpretation"]
    G --> H""",
        "Respiration interpretation requires tracking electron carriers, proton motive force, ATP synthesis, and uncoupling.",
        "ATP-yield claims are conditional on shuttle use, proton leak, coupling efficiency, tissue state, and measurement method rather than one fixed number.",
    ),
    "photosynthesis": (
        "Photosynthesis Under Stress",
        """flowchart TD
    A["Light and CO2 supply"] --> B["Electron transport"]
    A --> C["Stomatal conductance"]
    C --> D["Internal CO2"]
    D --> E["Calvin cycle"]
    B --> E
    E --> F["Sugar export"]
    C --> G["Water loss"]
    G --> H["Growth tradeoff"]""",
        "Stress-aware photosynthesis map connecting light capture, stomatal conductance, carbon fixation, sugar export, and water loss.",
        "Photosynthesis in a plant is a coupled carbon-water decision: high light cannot raise growth if CO2 entry, water status, or sink demand becomes limiting.",
    ),
    "mutations_and_genomics": (
        "Genome Editing From Variant to Follow-Up",
        """flowchart LR
    A["Disease mechanism"] --> B["Editing strategy"]
    B --> C["Cell collection or delivery"]
    C --> D["On-target edit assay"]
    D --> E["Off-target and SV checks"]
    E --> F["Clinical endpoint"]
    F --> G["Long-term monitoring"]""",
        "Genome-editing therapy workflow from disease mechanism to editing strategy, safety assays, clinical endpoint, and long-term monitoring.",
        "Casgevy and prime-editing examples show why editing medicines require molecular endpoints, structural-variant surveillance, toxicity monitoring, and long follow-up \\citep{fda2026casgevy,chalumeau2025primeediting}.",
    ),
    "epigenetics_and_gene_regulation": (
        "Epigenetic Causality Ladder",
        """flowchart TD
    A["Chromatin mark observed"] --> B["Cell-type context"]
    B --> C["Perturb writer or eraser"]
    C --> D["Expression change"]
    D --> E["Phenotype or cell state"]
    E --> F["Rescue or orthogonal assay"]
    F --> G["Causal epigenetic claim"]""",
        "Evidence ladder for moving from an observed chromatin mark to a causal epigenetic claim.",
        "An epigenetic mark is not automatically a cause; causal claims need perturbation, timing, cell-type specificity, expression readout, and rescue or orthogonal evidence.",
    ),
    "population_genetics": (
        "Ancestry-Aware Variant Interpretation",
        """flowchart LR
    A["Sampled individuals"] --> B["Reference choice"]
    B --> C["Variant calls"]
    C --> D["Allele frequency"]
    D --> E["Model assumptions"]
    E --> F["Risk or selection claim"]
    B --> G["Pangenome graph"]
    G --> C""",
        "Population-genetic interpretation depends on sampling, reference choice, variant calls, allele frequencies, and model assumptions.",
        "Graph references can reduce reference bias, but population-genetic interpretation still depends on sampling design, assumptions, and validation \\citep{humanpangenome2023}.",
    ),
    "bacteria_archaea_viruses": (
        "AMR Movement Across One Health",
        """flowchart LR
    A["Antibiotic pressure"] --> B["Resistant strain"]
    B --> C["Plasmid or integron"]
    C --> D["Horizontal transfer"]
    D --> E["Clinic"]
    D --> F["Farm"]
    D --> G["Wastewater"]
    E --> H["Surveillance and stewardship"]
    F --> H
    G --> H""",
        "One Health map of antimicrobial-resistance selection, mobile genetic elements, movement across settings, and surveillance.",
        "WHO priority lists are most useful when students connect the organism-resistance pair to selection pressure, transmission route, and stewardship action \\citep{who2024bppl,murray2022amr}.",
    ),
    "microbial_ecology": (
        "Microbiome Causality Ladder",
        """flowchart TD
    A["Association study"] --> B["Longitudinal pattern"]
    B --> C["Mechanistic metabolite"]
    C --> D["Perturbation test"]
    D --> E["Transfer or rescue"]
    E --> F["Host outcome"]
    F --> G["Qualified causality"]""",
        "Microbiome causality ladder from association to longitudinal evidence, mechanism, perturbation, transfer or rescue, and host outcome.",
        "Microbiome claims become stronger as they move from correlation toward perturbation and rescue evidence; many human associations remain context-dependent.",
    ),
    "infectious_disease": (
        "Intervention Choice Across Pathogens",
        """flowchart TD
    A["Pathogen and setting"] --> B["Transmission route"]
    B --> C["Diagnostic evidence"]
    C --> D["Resistance or immune status"]
    D --> E["Drug, vaccine, or vector tool"]
    E --> F["Adherence and equity"]
    F --> G["Surveillance feedback"]""",
        "Decision map for infectious-disease intervention choice across transmission, diagnostics, resistance, adherence, equity, and surveillance feedback.",
        "TB regimens, malaria spatial emanators, lenacapavir PrEP, Candida auris control, and Long COVID mechanisms are cases where intervention choices depend on evidence and setting. \\citep{who2025tb,who2025spatialemanators,cdc2025lenacapavirprep,cdc2026candidaauris,longcovid2026mechanisms}",
    ),
    "plant_structure_and_water": (
        "Hydraulic Safety Tradeoff",
        """flowchart LR
    A["Dry air or soil"] --> B["Lower water potential"]
    B --> C["Stomatal closure"]
    C --> D["Less water loss"]
    C --> E["Less CO2 entry"]
    B --> F["Xylem tension"]
    F --> G["Cavitation risk"]
    D --> H["Survival"]
    E --> I["Lower growth"]""",
        "Plant hydraulic tradeoff connecting water potential, stomatal closure, carbon gain, xylem tension, cavitation risk, survival, and growth.",
        "Drought responses should be read as tradeoffs among carbon gain, water loss, hydraulic safety, and growth rather than as simple stress resistance.",
    ),
    "plant_responses": (
        "Plant Stress Response Decision",
        """flowchart TD
    A["Stress cue"] --> B["Sensor and hormone network"]
    B --> C["ABA or defence signal"]
    C --> D["Gene-expression change"]
    D --> E["Trait response"]
    E --> F["Growth cost"]
    E --> G["Survival benefit"]
    F --> H["Fitness outcome"]
    G --> H""",
        "Plant stress-response map connecting cue perception, hormone signalling, gene expression, trait response, growth cost, and survival benefit.",
        "Stress tolerance is not free: the same response that improves survival can reduce growth or reproduction depending on timing and environment.",
    ),
    "endocrine_and_immune": (
        "Allostasis and Immune-Endocrine Coupling",
        """flowchart LR
    A["Repeated stressor"] --> B["Neural appraisal"]
    B --> C["HPA axis"]
    C --> D["Cortisol rhythm"]
    D --> E["Immune tone"]
    E --> F["Inflammation risk"]
    D --> G["Metabolic allocation"]
    F --> H["Allostatic load"]
    G --> H""",
        "Allostatic-load map linking repeated stressors, HPA-axis dynamics, immune tone, metabolic allocation, and disease risk.",
        "Physiology is often adaptive over short time scales and costly over long time scales, so baseline, perturbation, compensation, and pathology must be distinguished.",
    ),
    "ecosystem_ecology": (
        "Agroecology as Coupled Fluxes",
        """flowchart LR
    A["Soil organic matter"] --> B["Water retention"]
    A --> C["Nutrient cycling"]
    D["Crop diversity"] --> E["Pest regulation"]
    D --> F["Pollinator habitat"]
    B --> G["Yield stability"]
    C --> G
    E --> G
    F --> G
    G --> H["Food security"]""",
        "Agroecology systems map linking soil organic matter, water retention, nutrient cycling, crop diversity, pest regulation, pollinator habitat, yield stability, and food security.",
        "Food-security claims should connect ecological mechanisms to access, resilience, livelihoods, and tradeoffs rather than equating yield alone with nutrition \\citep{fao2025sofi}.",
    ),
    "biomes_and_conservation": (
        "Conservation Decision Evidence Chain",
        """flowchart TD
    A["Biodiversity signal"] --> B["Driver analysis"]
    B --> C["Conservation option"]
    C --> D["Ecological outcome"]
    C --> E["Social feasibility"]
    D --> F["Tradeoff review"]
    E --> F
    F --> G["Adaptive monitoring"]
    H["Coral heat stress"] --> B
    I["Assisted evolution"] --> C""",
        "Conservation evidence chain linking biodiversity signals, driver analysis, intervention options, ecological outcomes, social feasibility, tradeoff review, and adaptive monitoring.",
        "Coral assisted evolution and IPBES transformative-change examples show why conservation decisions need evidence, values, feasibility, and monitoring in the same frame \\citep{ipbes2024transformative,noaa2025coralbleaching,strader2022coralheat}.",
    ),
}


COMPANION_SOURCE_BY_STEM: dict[str, str] = {
    "systems_science": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/cell/cell_biology.py` (`hill_equation`, `receptor_occupancy`, `signal_amplification`) | Turn feedback, thresholds, and signalling gain into inspectable calculations. |\n"
        "| `src/biology/ecology/ecology.py` (`logistic_growth`) | Compare linear intuition with bounded growth and carrying-capacity dynamics. |\n"
        "| `src/biology/biochemistry/biochemistry.py` (`reaction_free_energy`) | Connect system directionality to thermodynamic constraints. |\n"
        "| `src/visualization/plots.py` (`plot_logistic_growth`) and `src/mermaid/biology_diagrams.py` (`population_growth_stages_diagram`) | Check whether graphical summaries preserve the same model assumptions. |\n\n"
        "**Reproducibility check:** change one parameter at a time, record the sign of the response, and explain whether the result reflects feedback, saturation, or an arbitrary boundary choice. "
        "**Cross-reference:** pair this with \\cref{sec:unit_0_complex_adaptive_systems}, \\cref{sec:unit_III_bioenergetics_and_respiration}, and \\cref{sec:unit_X_population_ecology}."
    ),
    "complex_adaptive_systems": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/ecology/ecology.py` (`lotka_volterra`, `biodiversity_indices`, `logistic_growth`) | Explore feedback, interaction strength, and diversity metrics as emergent summaries. |\n"
        "| `src/biology/evolution/evolution.py` (`simulate_selection`, `wright_fisher_drift`, `fitness_landscape_1d`) | Compare selection, drift, and landscape ruggedness as agent-level rules. |\n"
        "| `src/visualization/plots.py` (`plot_lotka_volterra`, `plot_selection_simulation`) | Inspect how oscillations and allele-frequency trajectories depend on starting conditions. |\n"
        "| `src/mermaid/biology_diagrams.py` (`food_web_diagram`, `population_growth_stages_diagram`) | Link network structure to emergent population outcomes. |\n\n"
        "**Reproducibility check:** rerun or recalculate a scenario from two initial states and ask whether convergence, hysteresis, or path dependence is doing the explanatory work. "
        "**Cross-reference:** use \\cref{sec:unit_0_systems_science}, \\cref{sec:unit_V_population_genetics}, and \\cref{sec:unit_X_community_ecology} as comparison cases."
    ),
    "active_inference": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/neuroscience/neuroscience.py` (`action_potential_hh`, `hebbian_weight_update`) | Connect prediction, update, and plasticity to measurable neural variables. |\n"
        "| `src/biology/physiology/physiology.py` (`homeostasis_response`) | Compare allostatic regulation with error-correcting control. |\n"
        "| `src/biology/cell/cell_biology.py` (`receptor_occupancy`, `signal_amplification`) | Make sensing and gain explicit rather than metaphorical. |\n"
        "| `src/mermaid/biology_diagrams.py` (`nervous_system_reflex_diagram`, `hormone_signaling_diagram`) | Contrast reflex arcs, endocrine loops, and inference-style control diagrams. |\n\n"
        "**Reproducibility check:** name the hidden state, observation, action, and error term before treating a biological feedback loop as active inference. "
        "**Cross-reference:** compare with \\cref{sec:unit_IX_nervous_system}, \\cref{sec:unit_IX_circulation_respiration_homeostasis}, and \\cref{sec:unit_II_cell_signaling}."
    ),
    "atoms_molecules": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/biochemistry/biochemistry.py` (`reaction_free_energy`, `atp_free_energy`) | Tie bonding and reaction direction to energy accounting. |\n"
        "| `src/biology/cell/cell_biology.py` (`osmotic_pressure`, `diffusion_flux`) | Connect charge, solubility, and concentration gradients to cell-scale outcomes. |\n"
        "| `src/mermaid/biology_diagrams.py` (`macromolecule_classification_diagram`) | Place atomic and bond-level concepts inside the larger biomolecule map. |\n\n"
        "**Reproducibility check:** for every molecular claim, write the charge/polarity, solvent context, and unit-bearing quantity that would make the claim testable. "
        "**Cross-reference:** extend the same logic in \\cref{sec:unit_I_water_and_life}, \\cref{sec:unit_I_macromolecules}, and \\cref{sec:unit_II_membrane_transport}."
    ),
    "water_and_life": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/cell/cell_biology.py` (`osmotic_pressure`, `diffusion_flux`) | Translate water potential, solute gradients, and diffusion into quantitative predictions. |\n"
        "| `src/biology/botany/botany.py` (`water_potential`, `transpiration_flux`) | Carry water chemistry into plant transport and drought-response scenarios. |\n"
        "| `src/visualization/plots.py` (`plot_light_response_curve`) | Use graph reading practice for environmental-response curves with clear axes and units. |\n\n"
        "**Reproducibility check:** state temperature, solute identity, concentration, and membrane permeability before generalising a water-property claim. "
        "**Cross-reference:** connect molecular water properties to \\cref{sec:unit_VIII_plant_structure_and_water} and \\cref{sec:unit_II_membrane_transport}."
    ),
    "macromolecules": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/biochemistry/biochemistry.py` (`reaction_free_energy`, `glycolysis_summary`) | Relate polymer chemistry and hydrolysis to energy flow. |\n"
        "| `src/biology/genetics/genetics.py` (`dna_complement`, `transcribe_dna_to_mrna`, `translate_mrna`) | Connect nucleic-acid structure to information transfer. |\n"
        "| `src/mermaid/biology_diagrams.py` (`macromolecule_classification_diagram`, `transcription_translation_diagram`) | Compare classification diagrams with sequence-to-function pathways. |\n\n"
        "**Reproducibility check:** separate sequence, three-dimensional structure, modification state, and assay evidence before claiming function. "
        "**Cross-reference:** use this bridge with \\cref{sec:unit_I_enzymes_and_kinetics}, \\cref{sec:unit_IV_gene_expression}, and \\cref{sec:unit_IV_mutations_and_genomics}."
    ),
    "enzymes_and_kinetics": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/biochemistry/biochemistry.py` (`michaelis_menten`, `competitive_inhibition`, `enzyme_rate_curve`) | Reproduce saturation curves, inhibition shifts, and parameter interpretation. |\n"
        "| `src/visualization/plots.py` (`plot_michaelis_menten`) | Check that graph shape, axes, and units match the kinetic equation. |\n"
        "| `src/mermaid/biology_diagrams.py` (`enzyme_kinetics_diagram`) | Keep mechanism, substrate binding, and regulation visually aligned. |\n\n"
        "**Reproducibility check:** report substrate range, enzyme amount, temperature, pH, and rate units before comparing kinetic parameters. "
        "**Cross-reference:** connect kinetics to \\cref{sec:unit_III_metabolic_integration} and \\cref{sec:unit_IV_gene_expression}."
    ),
    "cell_theory": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/cell/cell_biology.py` (`get_organelles_by_cell_type`, `count_membrane_bound_organelles`) | Turn cell-type comparisons into explicit feature lists rather than memorised diagrams. |\n"
        "| `src/mermaid/biology_diagrams.py` (`organelle_function_diagram`) | Connect cell theory to structure-function evidence. |\n\n"
        "**Reproducibility check:** identify the observation scale, specimen state, and imaging limit before deciding what counts as evidence for a cellular claim. "
        "**Cross-reference:** compare with \\cref{sec:unit_II_cell_structure} and \\cref{sec:unit_VII_bacteria_archaea_viruses}."
    ),
    "cell_structure": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/cell/cell_biology.py` (`Organelle`, `get_organelles_by_cell_type`, `count_membrane_bound_organelles`) | Connect organelle inventories to cell type and function. |\n"
        "| `src/mermaid/biology_diagrams.py` (`organelle_function_diagram`, `membrane_transport_diagram`) | Keep compartment diagrams tied to transport and interaction. |\n\n"
        "**Reproducibility check:** treat an organelle claim as conditional on cell type, developmental state, and measurement method. "
        "**Cross-reference:** use \\cref{sec:unit_II_cell_theory}, \\cref{sec:unit_II_membrane_transport}, and \\cref{sec:unit_III_bioenergetics_and_respiration}."
    ),
    "membrane_transport": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/cell/cell_biology.py` (`nernst_potential`, `goldman_equation`, `osmotic_pressure`, `diffusion_flux`) | Reproduce electrochemical, osmotic, and diffusive driving forces. |\n"
        "| `src/visualization/plots.py` (`plot_nernst_potentials`) | Inspect ion-specific gradients and sign conventions. |\n"
        "| `src/mermaid/biology_diagrams.py` (`membrane_transport_diagram`) | Separate channels, carriers, pumps, and coupled transport. |\n\n"
        "**Reproducibility check:** list concentrations, permeability, charge, temperature, and membrane orientation before interpreting transport direction. "
        "**Cross-reference:** connect with \\cref{sec:unit_IX_action_potential_synapses} and \\cref{sec:unit_VIII_plant_structure_and_water}."
    ),
    "cell_signaling": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/cell/cell_biology.py` (`receptor_occupancy`, `hill_equation`, `signal_amplification`) | Quantify ligand binding, cooperativity, and cascade gain. |\n"
        "| `src/mermaid/biology_diagrams.py` (`hormone_signaling_diagram`, `immune_response_diagram`) | Compare receptor logic across endocrine and immune examples. |\n\n"
        "**Reproducibility check:** specify dose, timing, receptor context, feedback, and readout before inferring pathway causality. "
        "**Cross-reference:** extend the same logic in \\cref{sec:unit_IX_endocrine_and_immune} and \\cref{sec:unit_IV_epigenetics_and_gene_regulation}."
    ),
    "bioenergetics_and_respiration": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/biochemistry/biochemistry.py` (`reaction_free_energy`, `atp_free_energy`, `glycolysis_summary`) | Track energy accounting across glycolysis, respiration, and ATP coupling. |\n"
        "| `src/mermaid/biology_diagrams.py` (`glycolysis_pathway_diagram`, `atp_synthesis_diagram`) | Check pathway order and coupling between electron flow and proton motive force. |\n\n"
        "**Reproducibility check:** name the electron donor, acceptor, compartment, proton path, and ATP-yield assumption before comparing respiratory claims. "
        "**Cross-reference:** connect with \\cref{sec:unit_III_photosynthesis}, \\cref{sec:unit_III_metabolic_integration}, and \\cref{sec:unit_I_enzymes_and_kinetics}."
    ),
    "photosynthesis": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/botany/botany.py` (`photosynthesis_rate`, `light_response_curve`) | Reproduce light-response and environmental-limitation scenarios. |\n"
        "| `src/visualization/plots.py` (`plot_light_response_curve`) | Inspect saturation, compensation points, and axis labeling. |\n"
        "| `src/mermaid/biology_diagrams.py` (`photosynthesis_light_dark_diagram`) | Separate light reactions, carbon fixation, and regulation. |\n\n"
        "**Reproducibility check:** report light intensity, CO2, temperature, water status, and plant pathway before comparing photosynthetic rates. "
        "**Cross-reference:** compare with \\cref{sec:unit_VIII_plant_responses} and \\cref{sec:unit_X_ecosystem_ecology}."
    ),
    "metabolic_integration": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/biochemistry/biochemistry.py` (`glycolysis_summary`, `atp_free_energy`, `reaction_free_energy`) | Connect pathway summaries to energy and redox constraints. |\n"
        "| `src/biology/physiology/physiology.py` (`homeostasis_response`) | Compare cellular flux regulation with organism-level homeostasis. |\n"
        "| `src/mermaid/biology_diagrams.py` (`glycolysis_pathway_diagram`, `hormone_signaling_diagram`) | Link metabolic pathways to endocrine control. |\n\n"
        "**Reproducibility check:** state fed/fasted status, tissue, compartment, and time scale before predicting pathway priority. "
        "**Cross-reference:** use \\cref{sec:unit_III_bioenergetics_and_respiration}, \\cref{sec:unit_I_enzymes_and_kinetics}, and \\cref{sec:unit_IX_endocrine_and_immune}."
    ),
    "dna_replication_and_cell_cycle": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/genetics/genetics.py` (`dna_complement`, `hamming_distance`) | Test strand complementarity and sequence-change reasoning. |\n"
        "| `src/mermaid/biology_diagrams.py` (`dna_replication_diagram`, `cell_cycle_diagram`) | Keep replication forks, checkpoints, and cell-cycle stages aligned. |\n\n"
        "**Reproducibility check:** identify strand polarity, origin/fork direction, repair pathway, and checkpoint readout before diagnosing replication errors. "
        "**Cross-reference:** connect with \\cref{sec:unit_IV_mutations_and_genomics} and \\cref{sec:unit_V_chromosomal_inheritance}."
    ),
    "gene_expression": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/genetics/genetics.py` (`transcribe_dna_to_mrna`, `translate_mrna`, `gc_content`) | Reproduce transcription, translation, codon lookup, and sequence-composition checks. |\n"
        "| `src/mermaid/biology_diagrams.py` (`transcription_translation_diagram`, `mirna_biogenesis_diagram`) | Connect coding flow with RNA regulation. |\n\n"
        "**Reproducibility check:** specify template strand, reading frame, RNA-processing assumptions, and regulatory layer before interpreting expression. "
        "**Cross-reference:** use \\cref{sec:unit_IV_epigenetics_and_gene_regulation} and \\cref{sec:unit_I_macromolecules}."
    ),
    "mutations_and_genomics": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/genetics/genetics.py` (`dna_complement`, `translate_mrna`, `hamming_distance`, `jukes_cantor_distance`) | Compare sequence variants, coding effects, and corrected molecular distances. |\n"
        "| `src/mermaid/biology_diagrams.py` (`transcription_translation_diagram`, `dna_replication_diagram`) | Link mutation class to replication and expression context. |\n\n"
        "**Reproducibility check:** distinguish discovery technology, reference representation, variant class, evidence level, and clinical actionability. "
        "**Cross-reference:** connect with \\cref{sec:unit_IV_dna_replication_and_cell_cycle}, \\cref{sec:unit_IV_gene_expression}, and \\cref{sec:unit_VII_bacteria_archaea_viruses}."
    ),
    "epigenetics_and_gene_regulation": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/genetics/genetics.py` (`cpg_methylation_remaining`, `histone_modification_state`) | Convert methylation maintenance and histone-mark claims into explicit state checks. |\n"
        "| `src/visualization/plots.py` (`plot_methylation_heatmap`) | Inspect whether heatmap interpretation depends on color alone or includes labels. |\n"
        "| `src/mermaid/biology_diagrams.py` (`mirna_biogenesis_diagram`, `x_inactivation_diagram`) | Compare RNA-mediated and chromatin-mediated regulation. |\n\n"
        "**Reproducibility check:** require cell type, developmental time, perturbation evidence, and inheritance control before calling a mark causal. "
        "**Cross-reference:** use \\cref{sec:unit_IV_gene_expression}, \\cref{sec:unit_IV_mutations_and_genomics}, and \\cref{sec:unit_V_chromosomal_inheritance}."
    ),
    "mendelian_genetics": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/genetics/genetics.py` (`punnett_square`, `hardy_weinberg`, `chi_squared_test`) | Reproduce inheritance ratios, equilibrium expectations, and goodness-of-fit tests. |\n"
        "| `src/visualization/plots.py` (`plot_punnett_square`) | Check genotype and phenotype tables visually. |\n"
        "| `src/mermaid/biology_diagrams.py` (`mendelian_cross_diagram`) | Link segregation logic to diagrammed crosses. |\n\n"
        "**Reproducibility check:** state genotype notation, dominance model, sample size, and statistical expectation before interpreting a ratio. "
        "**Cross-reference:** compare with \\cref{sec:unit_V_chromosomal_inheritance} and \\cref{sec:unit_V_population_genetics}."
    ),
    "chromosomal_inheritance": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/genetics/genetics.py` (`recombination_frequency`, `genetic_distance`, `infer_three_point_order`) | Convert offspring counts into linkage maps and gene order. |\n"
        "| `src/visualization/plots.py` (`plot_chromosome_structure`) | Connect cytogenetic structure to inheritance patterns. |\n"
        "| `src/mermaid/biology_diagrams.py` (`chromosome_inheritance_diagram`, `x_inactivation_diagram`) | Compare segregation, linkage, and dosage compensation. |\n\n"
        "**Reproducibility check:** specify phase, recombinant classes, crossover assumptions, and mapping limits before inferring chromosome structure. "
        "**Cross-reference:** use \\cref{sec:unit_V_mendelian_genetics}, \\cref{sec:unit_IV_epigenetics_and_gene_regulation}, and \\cref{sec:unit_V_population_genetics}."
    ),
    "population_genetics": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/genetics/genetics.py` (`hardy_weinberg`, `chi_squared_test`, `jukes_cantor_distance`) | Test equilibrium, goodness of fit, and molecular-distance assumptions. |\n"
        "| `src/biology/evolution/evolution.py` (`simulate_selection`, `wright_fisher_drift`, `molecular_clock_divergence_time`) | Compare deterministic and stochastic allele-frequency change. |\n"
        "| `src/visualization/plots.py` (`plot_selection_simulation`) | Inspect trajectories and sampling effects. |\n\n"
        "**Reproducibility check:** state population size, mating model, selection coefficient, migration, mutation, and sampling uncertainty before attributing allele-frequency change. "
        "**Cross-reference:** connect with \\cref{sec:unit_V_mendelian_genetics}, \\cref{sec:unit_VI_evolution_and_selection}, and \\cref{sec:unit_VI_genetic_drift_and_speciation}."
    ),
    "evolution_and_selection": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/evolution/evolution.py` (`selection_one_generation`, `simulate_selection`, `fitness_landscape_1d`) | Reproduce selection trajectories and landscape reasoning. |\n"
        "| `src/visualization/plots.py` (`plot_selection_simulation`) | Compare fitness assumptions with plotted allele-frequency change. |\n"
        "| `src/mermaid/biology_diagrams.py` (`natural_selection_diagram`) | Keep variation, inheritance, differential survival, and adaptation distinct. |\n\n"
        "**Reproducibility check:** define fitness component, environment, heritable variation, and alternative explanation before calling a trait adaptive. "
        "**Cross-reference:** use \\cref{sec:unit_V_population_genetics} and \\cref{sec:unit_VI_genetic_drift_and_speciation}."
    ),
    "genetic_drift_and_speciation": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/evolution/evolution.py` (`wright_fisher_drift`, `simulate_drift`, `isolation_index`) | Compare stochastic drift, bottlenecks, and isolation measures. |\n"
        "| `src/mermaid/biology_diagrams.py` (`speciation_diagram`, `phylogenetic_tree_diagram`) | Connect reproductive isolation to lineage divergence. |\n\n"
        "**Reproducibility check:** report effective population size, migration, selection possibility, and time scale before assigning divergence to drift or speciation. "
        "**Cross-reference:** compare with \\cref{sec:unit_V_population_genetics}, \\cref{sec:unit_VI_evolution_and_selection}, and \\cref{sec:unit_VI_phylogenetics}."
    ),
    "phylogenetics": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/evolution/evolution.py` (`molecular_clock_divergence_time`) | Translate genetic distance and rate assumptions into divergence-time estimates. |\n"
        "| `src/biology/genetics/genetics.py` (`hamming_distance`, `jukes_cantor_distance`) | Compare raw and corrected sequence distances. |\n"
        "| `src/mermaid/biology_diagrams.py` (`phylogenetic_tree_diagram`) | Keep topology, branch length, and interpretation visually distinct. |\n\n"
        "**Reproducibility check:** state alignment quality, homology assumption, substitution model, sampling, and calibration before treating a tree as history. "
        "**Cross-reference:** use \\cref{sec:unit_VI_genetic_drift_and_speciation} and \\cref{sec:unit_VII_bacteria_archaea_viruses}."
    ),
    "bacteria_archaea_viruses": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/microbiology/microbiology.py` (`bacterial_growth_curve`, `doubling_time`, `ViralReplicationResult`) | Check growth, doubling, and viral-replication assumptions. |\n"
        "| `src/visualization/plots.py` (`plot_bacterial_growth`) | Inspect growth phases and axis scaling. |\n"
        "| `src/mermaid/biology_diagrams.py` (`viral_replication_cycle_diagram`) | Link genome strategy to replication cycle. |\n\n"
        "**Reproducibility check:** specify taxon, environment, growth phase, genome type, and measurement method before generalising microbial claims. "
        "**Cross-reference:** connect with \\cref{sec:unit_VII_microbial_ecology} and \\cref{sec:unit_VII_infectious_disease}."
    ),
    "microbial_ecology": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/microbiology/microbiology.py` (`bacterial_growth_curve`, `doubling_time`) | Quantify growth constraints for interacting microbial populations. |\n"
        "| `src/biology/ecology/ecology.py` (`lotka_volterra`, `connectance`, `biodiversity_indices`) | Treat microbiomes as communities with measurable interaction structure. |\n"
        "| `src/mermaid/biology_diagrams.py` (`food_web_diagram`) | Compare cross-feeding and competition with broader food-web logic. |\n\n"
        "**Reproducibility check:** distinguish association, perturbation response, mechanism, and host/environment context before making a microbiome-causality claim. "
        "**Cross-reference:** use \\cref{sec:unit_X_community_ecology} and \\cref{sec:unit_VII_infectious_disease}."
    ),
    "infectious_disease": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/microbiology/microbiology.py` (`basic_reproduction_number`, `sir_model`, `mic_fold_dilution`) | Reproduce transmission and antimicrobial-resistance calculations. |\n"
        "| `src/biology/ecology/ecology.py` (`exponential_growth`) | Compare early outbreak growth with ecological growth models. |\n"
        "| `src/mermaid/biology_diagrams.py` (`immune_response_diagram`, `viral_replication_cycle_diagram`) | Connect pathogen life cycle to host response. |\n\n"
        "**Reproducibility check:** identify pathogen, host population, transmission route, diagnostic window, intervention, and surveillance source before comparing disease claims. "
        "**Cross-reference:** connect with \\cref{sec:unit_VII_bacteria_archaea_viruses}, \\cref{sec:unit_IX_endocrine_and_immune}, and \\cref{sec:unit_X_community_ecology}."
    ),
    "plant_structure_and_water": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/botany/botany.py` (`water_potential`, `transpiration_flux`) | Reproduce plant-water calculations and hydraulic tradeoffs. |\n"
        "| `src/biology/cell/cell_biology.py` (`osmotic_pressure`) | Connect cellular osmotic pressure to tissue-level water movement. |\n"
        "| `src/visualization/plots.py` (`plot_light_response_curve`) | Practice graph interpretation for environmental-response curves. |\n\n"
        "**Reproducibility check:** list solute potential, pressure potential, tissue, humidity, temperature, and stomatal state before predicting water movement. "
        "**Cross-reference:** use \\cref{sec:unit_I_water_and_life} and \\cref{sec:unit_VIII_plant_responses}."
    ),
    "plant_reproduction": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/botany/botany.py` (`plant_biomass_growth`) | Explore growth allocation and reproductive tradeoffs. |\n"
        "| `src/biology/genetics/genetics.py` (`punnett_square`, `chi_squared_test`) | Connect inheritance evidence to breeding and reproductive outcomes. |\n"
        "| `src/mermaid/biology_diagrams.py` (`hormone_signaling_diagram`) | Link developmental timing to hormone signalling. |\n\n"
        "**Reproducibility check:** state pollination mechanism, developmental stage, genetic model, and environmental filter before interpreting reproductive success. "
        "**Cross-reference:** connect with \\cref{sec:unit_V_mendelian_genetics} and \\cref{sec:unit_VIII_plant_responses}."
    ),
    "plant_responses": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/botany/botany.py` (`photosynthesis_rate`, `light_response_curve`, `transpiration_flux`) | Quantify how light, CO2, water, and temperature shape response curves. |\n"
        "| `src/visualization/plots.py` (`plot_light_response_curve`) | Check saturation and stress interpretation visually. |\n"
        "| `src/mermaid/biology_diagrams.py` (`photosynthesis_light_dark_diagram`, `hormone_signaling_diagram`) | Link environmental sensing to pathway response. |\n\n"
        "**Reproducibility check:** name the signal, receptor/tissue, hormone network, phenotype, and tradeoff before claiming adaptive response. "
        "**Cross-reference:** use \\cref{sec:unit_VIII_plant_structure_and_water}, \\cref{sec:unit_VIII_plant_reproduction}, and \\cref{sec:unit_III_photosynthesis}."
    ),
    "circulation_respiration_homeostasis": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/physiology/physiology.py` (`poiseuille_flow`, `oxygen_saturation`, `oxygen_dissociation_curve`, `homeostasis_response`) | Reproduce flow, gas transport, and regulatory response claims. |\n"
        "| `src/visualization/plots.py` (`plot_oxygen_dissociation`) | Inspect shifts in oxygen loading and unloading. |\n\n"
        "**Reproducibility check:** state vessel radius, pressure gradient, haemoglobin state, tissue demand, and feedback variable before interpreting homeostasis. "
        "**Cross-reference:** connect with \\cref{sec:unit_IX_endocrine_and_immune} and \\cref{sec:unit_III_bioenergetics_and_respiration}."
    ),
    "nervous_system": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/neuroscience/neuroscience.py` (`cable_voltage_attenuation`, `hebbian_weight_update`, `action_potential_hh`) | Connect circuit architecture, passive spread, spiking, and plasticity. |\n"
        "| `src/visualization/plots.py` (`plot_action_potential`) | Check timing and amplitude of neural signals. |\n"
        "| `src/mermaid/biology_diagrams.py` (`nervous_system_reflex_diagram`) | Keep stimulus, integration, motor output, and feedback distinct. |\n\n"
        "**Reproducibility check:** specify cell type, circuit level, recording method, and behavioural readout before linking neural mechanism to outcome. "
        "**Cross-reference:** use \\cref{sec:unit_IX_action_potential_synapses} and \\cref{sec:unit_0_active_inference}."
    ),
    "action_potential_synapses": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/neuroscience/neuroscience.py` (`action_potential_hh`, `synaptic_current`, `cable_voltage_attenuation`) | Reproduce spike timing, postsynaptic currents, and passive spread. |\n"
        "| `src/biology/cell/cell_biology.py` (`nernst_potential`, `goldman_equation`) | Check ion gradients and membrane-voltage assumptions. |\n"
        "| `src/visualization/plots.py` (`plot_action_potential`, `plot_nernst_potentials`) | Compare calculated voltages with plotted signals. |\n\n"
        "**Reproducibility check:** list ion concentrations, conductances, reversal potentials, synaptic delay, and receptor type before interpreting excitability. "
        "**Cross-reference:** connect with \\cref{sec:unit_II_membrane_transport} and \\cref{sec:unit_IX_nervous_system}."
    ),
    "endocrine_and_immune": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/physiology/physiology.py` (`homeostasis_response`) | Compare hormone feedback and inflammatory regulation as control problems. |\n"
        "| `src/biology/cell/cell_biology.py` (`receptor_occupancy`, `signal_amplification`) | Quantify receptor sensitivity and cascade gain. |\n"
        "| `src/mermaid/biology_diagrams.py` (`immune_response_diagram`, `hormone_signaling_diagram`) | Connect endocrine and immune sequence logic. |\n\n"
        "**Reproducibility check:** specify ligand/cytokine, receptor, timing, tissue, feedback loop, and readout before calling a response adaptive or pathological. "
        "**Cross-reference:** use \\cref{sec:unit_II_cell_signaling}, \\cref{sec:unit_IX_circulation_respiration_homeostasis}, and \\cref{sec:unit_VII_infectious_disease}."
    ),
    "population_ecology": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/ecology/ecology.py` (`exponential_growth`, `logistic_growth`, `allee_strong_growth`) | Reproduce density-independent, density-dependent, and Allee-effect scenarios. |\n"
        "| `src/visualization/plots.py` (`plot_logistic_growth`) | Inspect carrying capacity and growth-rate assumptions. |\n"
        "| `src/mermaid/biology_diagrams.py` (`population_growth_stages_diagram`) | Link model phases to visual summaries. |\n\n"
        "**Reproducibility check:** state time step, units, density dependence, stochasticity, and management objective before forecasting a population. "
        "**Cross-reference:** compare with \\cref{sec:unit_V_population_genetics} and \\cref{sec:unit_X_community_ecology}."
    ),
    "community_ecology": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/ecology/ecology.py` (`lotka_volterra`, `connectance`, `biodiversity_indices`) | Quantify interactions, network structure, and community diversity. |\n"
        "| `src/visualization/plots.py` (`plot_lotka_volterra`, `plot_species_area_relationship`) | Inspect dynamics and richness-area patterns. |\n"
        "| `src/mermaid/biology_diagrams.py` (`food_web_diagram`) | Keep trophic links and interaction signs explicit. |\n\n"
        "**Reproducibility check:** define interaction sign, spatial scale, sampling effort, disturbance history, and network boundary before interpreting community patterns. "
        "**Cross-reference:** use \\cref{sec:unit_X_population_ecology}, \\cref{sec:unit_X_ecosystem_ecology}, and \\cref{sec:unit_VII_microbial_ecology}."
    ),
    "ecosystem_ecology": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/ecology/ecology.py` (`food_web_trophic_levels`, `connectance`, `biodiversity_indices`) | Translate ecosystem structure into trophic, network, and diversity calculations. |\n"
        "| `src/biology/botany/botany.py` (`photosynthesis_rate`, `water_potential`) | Link primary production and plant-water constraints to ecosystem fluxes. |\n"
        "| `src/mermaid/biology_diagrams.py` (`nutrient_cycle_diagram`, `food_web_diagram`) | Keep stocks, fluxes, and boundaries visually explicit. |\n\n"
        "**Reproducibility check:** state system boundary, stock, flux, residence time, unit, and time window before comparing ecosystem budgets. "
        "**Cross-reference:** connect with \\cref{sec:unit_III_photosynthesis}, \\cref{sec:unit_X_community_ecology}, and \\cref{sec:unit_X_biomes_and_conservation}."
    ),
    "biomes_and_conservation": (
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/ecology/ecology.py` (`species_area_relationship`, `biodiversity_indices`, `connectance`) | Reproduce conservation metrics and tradeoff-sensitive summaries. |\n"
        "| `src/visualization/plots.py` (`plot_species_area_relationship`, `plot_biome_distribution`) | Inspect species-area assumptions and biome comparisons. |\n"
        "| `src/mermaid/biology_diagrams.py` (`food_web_diagram`, `nutrient_cycle_diagram`) | Connect conservation action to ecological pathways. |\n\n"
        "**Reproducibility check:** separate ecological evidence, social objective, feasibility, uncertainty, and monitoring indicator before choosing a conservation action. "
        "**Cross-reference:** use \\cref{sec:unit_X_population_ecology}, \\cref{sec:unit_X_community_ecology}, and \\cref{sec:unit_X_ecosystem_ecology}."
    ),
}


_COMPANION_SECTION_RE = re.compile(
    r"\n*(?:---\s*\n\s*)?#{2,3}\s+Companion Source Module\s*\n.*?"
    r"(?=\n---\s*\n\s*## |\n##\s+|\Z)",
    flags=re.DOTALL,
)
_COMPANION_NOTE_LINE_RE = re.compile(
    r"(?m)^\*(?:Companion source note:|Module:|Figure:|Diagram:|Cross-references:)[^\n]*\n?"
)
_INLINE_COMPANION_NOTE_RE = re.compile(
    r"\*(?:Companion source note:|Module:|Figure:|Diagram:|Cross-references:)[^\n]*\*"
)


def companion_source_section(record: ChapterRecord) -> str:
    body = COMPANION_SOURCE_BY_STEM.get(
        record.stem,
        "| Surface | Use it for |\n"
        "| --- | --- |\n"
        "| `src/biology/` | Connect the chapter concept to a tested model or data structure. |\n\n"
        "**Reproducibility check:** name the input, output, assumption, and evidence limit before using code as support.",
    )
    return f"""
---

### Companion Source Module

**{record.title}** should leave a reproducible trail from a biological claim to
the code, figure, diagram, or paper-based activity that can test it. Use the
surfaces below to inspect the chapter's assumptions, rerun the relevant model,
or compare the manuscript explanation with companion labs and figures.

{body}
"""


def normalize_companion_source_modules(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        new_text = _COMPANION_SECTION_RE.sub("", text)
        new_text = _COMPANION_NOTE_LINE_RE.sub("", new_text)
        new_text = _INLINE_COMPANION_NOTE_RE.sub("", new_text)
        new_text = re.sub(r"\n---\s*\n\s*\n---\s*\n", "\n---\n", new_text)
        new_text = re.sub(r"\n---\s*\n\s*(?=---\s*\n)", "\n", new_text)
        new_text = re.sub(r"\n{4,}", "\n\n\n", new_text).rstrip()
        new_text = f"{new_text}\n\n{companion_source_section(record).strip()}\n"
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def frontier_section(record: ChapterRecord) -> str:
    unit_claim, unit_move = FRONTIER_BY_UNIT[record.unit_id]
    focus = FOCUS_BY_STEM[record.stem]
    source_practice = SOURCE_PRACTICE_BY_UNIT[record.unit_id]
    extra = EXTRA_FRONTIER_BY_STEM.get(record.stem, "")
    extra_block = f"\n\n{extra}" if extra else ""
    figure = FIGURE_BY_STEM.get(record.stem)
    figure_block = ""
    if figure is not None:
        figure_title, mermaid, alt, caption = figure
        figure_block = f"""
### Current Evidence Map: {figure_title}

```mermaid
{mermaid}
```
<!-- alt: {alt} -->
*{caption}*
"""
    title = "## Current Evidence and Frontier Biology"
    return f"""
{title}

For **{record.title}**, frontier biology belongs inside the evidence logic of
the chapter. {unit_claim} The core reading question is this: {focus}

- **What to verify:** identify the observation, model, assay, or dataset that
  would make the claim stronger or weaker.
- **What to qualify:** state the scale, organism, cell type, environmental
  condition, or population where the claim is expected to hold.
- **What to compare:** test at least one alternative explanation, baseline, or
  null model before treating the pattern as causal.
- **What to cite:** distinguish primary evidence, review synthesis, public
  dataset, and institutional guidance; for recent or numeric claims, prefer
  the source closest to the measurement and state what has changed since it was
  published.

{unit_move}

**Source practice:** {source_practice}{extra_block}
{figure_block}
"""


_FRONTIER_SECTION_RE = re.compile(
    r"^## Current Evidence and Frontier Biology\n.*?(?=^## (?:Summary|Key Terms|Further Reading|Companion Source Module)|\Z)",
    flags=re.DOTALL | re.MULTILINE,
)


UNIT_THREAD_BY_UNIT: dict[str, str] = {
    unit: f"""
## Current Evidence Thread

Use this unit as an evidence trail rather than a list of topics. {claim} As you
move through the chapters, keep a two-column note: **claim** on the left,
**evidence that would change my confidence** on the right. By the end of the
unit, each major idea should be tied to a measurement, model, citation, or
paper-based lab decision.
"""
    for unit, (claim, _move) in FRONTIER_BY_UNIT.items()
}


def insert_before_anchor(text: str, section: str, anchors: tuple[str, ...]) -> str:
    if section.splitlines()[1].strip() in text:
        return text
    positions = [text.find(anchor) for anchor in anchors if text.find(anchor) != -1]
    if not positions:
        return text.rstrip() + "\n\n" + section.strip() + "\n"
    pos = min(positions)
    return text[:pos].rstrip() + "\n\n" + section.strip() + "\n\n" + text[pos:].lstrip()


def _constant_replacement(_match: re.Match[str], *, replacement: str) -> str:
    return replacement


def enrich_chapters(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        section = frontier_section(record).strip() + "\n\n"
        if _FRONTIER_SECTION_RE.search(text):
            replacer = partial(_constant_replacement, replacement=section)
            new_text = _FRONTIER_SECTION_RE.sub(replacer, text, count=1)
        else:
            new_text = insert_before_anchor(
                text,
                frontier_section(record),
                ("## Summary", "## Key Terms", "## Further Reading and Source Notes"),
            )
        new_text = normalize_text(new_text).text
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def refresh_chapter_scholarship_bullets(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    marker = (
        "- **What to compare:** test at least one alternative explanation, baseline, or\n"
        "  null model before treating the pattern as causal.\n"
    )
    insertion = (
        "- **What to cite:** distinguish primary evidence, review synthesis, public\n"
        "  dataset, and institutional guidance; for recent or numeric claims, prefer\n"
        "  the source closest to the measurement and state what has changed since it was\n"
        "  published.\n"
    )
    for record in records:
        path = record.chapter_path
        text = path.read_text(encoding="utf-8")
        if "- **What to cite:**" in text or marker not in text:
            continue
        new_text = text.replace(marker, marker + insertion, 1)
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def enrich_unit_intros(dry_run: bool) -> int:
    changed = 0
    for unit_id, section in UNIT_THREAD_BY_UNIT.items():
        path = MANUSCRIPT / unit_id / "unit_intro.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = insert_before_anchor(
            text,
            section,
            ("## Computational Toolbox", "## Connections Across the Textbook", "## Chapter Roadmap"),
        )
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


def lab_evidence_section(record: ChapterRecord) -> str:
    focus = FOCUS_BY_STEM[record.stem]
    return f"""
## Paper-Based Evidence Upgrade

Before answering the analysis questions, annotate the paper dataset for
**{record.title}** with a reproducibility pass:

| Evidence check | Student action |
| --- | --- |
| Control logic | Mark the comparison that functions as the baseline, negative control, or reference case. |
| Uncertainty | Circle the row, card, diagram feature, or model assumption most likely to change the conclusion. |
| Model comparison | State whether a simpler rule, null model, or alternative mechanism could explain the same pattern. |
| Decision threshold | Write the minimum evidence that would make you revise the interpretation. |
| Reproducibility | Record the exact scoring rule another group would need to reproduce your classification. |

Focus note: {focus} Keep required work paper-based; any material-handling or
equipment version belongs only in an optional extension.
"""


def enrich_labs(records: list[ChapterRecord], dry_run: bool) -> int:
    changed = 0
    for record in records:
        path = record.lab_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = insert_before_anchor(
            text,
            lab_evidence_section(record),
            ("## Analysis Questions", "## Additional Analysis Questions", "## Debrief and Reflection"),
        )
        if new_text != text:
            changed += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed


_QUESTION_LINE = re.compile(r"^(\d{1,2})\.\s+(.+?)\s*$", re.MULTILINE)
_SOLUTION_BLOCK = re.compile(
    r"(<!-- SOLUTION\s*\n)(.*?)(\n\s*SOLUTION -->)",
    flags=re.DOTALL,
)


ANSWER_SIGNATURES = (
    "Rubric for *",
    "name the relevant players",
    "scale-setting detail",
    "state the judgment, cite two lines of evidence",
    "identify the governing equation or ratio",
    "specify the manipulated variable",
    "a complete response should",
    "Chapter-specific anchor:",
    "Common pitfall:",
    "Answer key for *",
    "define the concept precisely",
    "place it at the correct biological scale",
    "trace the causal sequence",
    "choose the relevant equation, ratio, or probability model",
    "state the hypothesis, variable being changed",
    "make a justified judgment",
    "Name the term in ",
    "Evidence anchor:",
    "Tie the reasoning to \\cref{",
    "Credit requires an explicit mechanism",
    "prompt-linked evidence",
    "Core response for *",
    "Expected answer for *",
)


def question_kind(question: str) -> str:
    q = question.lower()
    starts_quant = q.startswith(("calculate ", "compute ", "estimate ", "determine the value", "find the value"))
    if starts_quant or re.search(r"\b(χ²|chi[- ]square)\b", q):
        return "quantitative"
    if re.search(r"\b(calculate|compute|estimate|set up|solve|expected)\b", q) and (
        re.search(r"\d|%|χ²", q)
        or re.search(
            r"\b(ratio|ratios|probability|frequency|frequencies|value|km|mm|mol|percent|chi[- ]square)\b",
            q,
        )
    ):
        return "quantitative"
    if re.search(r"\b(evaluate|critique|argue|assess|weigh|defend or refute)\b", q[:80]):
        return "evaluation"
    if re.search(r"\b(design|designs|experiment|test whether|propose|devise|what experiment)\b", q):
        return "experimental"
    if re.search(r"\b(compare|contrast|distinguish|differentiate|difference between)\b", q[:120]):
        return "comparison"
    if re.search(
        r"\b(probability|expected ratios?|phenotype ratios?|genotype ratios?|allele frequenc(?:y|ies)|genotype frequenc(?:y|ies)|recombination frequenc(?:y|ies)|frequency|frequencies)\b",
        q,
    ):
        return "quantitative"
    if q.startswith(("a patient ", "a researcher ", "a student ", "given ", "consider ", "suppose ")):
        return "application"
    if re.search(r"\b(why|how|explain|mechanism|cause|causes|predict)\b", q[:140]):
        return "mechanism"
    return "definition"


_QUESTION_PREAMBLE_RE = re.compile(
    r"^(?:a\s+(?:student|patient|researcher|scientist|clinician|farmer|breeder|conservationist)\s+[^.]*\.\s*"
    r"|consider(?:\s+a|\s+the)?\s+[^.]*\.\s*"
    r"|given\s+[^.]*\.\s*"
    r"|suppose\s+[^.]*\.\s*"
    r"|imagine\s+[^.]*\.\s*)",
    flags=re.IGNORECASE,
)

_QUESTION_VERB_PREFIXES = (
    "state ",
    "define ",
    "list ",
    "identify ",
    "name ",
    "rank ",
    "describe ",
    "describe the ",
    "outline ",
    "outline the ",
    "sketch ",
    "draw ",
    "write ",
    "write the ",
    "give ",
    "what is ",
    "what are ",
    "compare ",
    "contrast ",
    "distinguish ",
    "differentiate ",
    "explain ",
    "evaluate ",
    "assess ",
    "critique ",
    "calculate ",
    "compute ",
    "estimate ",
    "determine ",
    "find ",
    "design ",
    "propose ",
    "devise ",
    "suggest ",
)


def subject_phrase(question: str) -> str:
    """Return a concise, prompt-specific subject for an answer key."""

    subject = question.strip().rstrip(". ")
    subject = _QUESTION_PREAMBLE_RE.sub("", subject).strip()
    lowered = subject.lower()
    for prefix in sorted(_QUESTION_VERB_PREFIXES, key=len, reverse=True):
        if lowered.startswith(prefix):
            subject = subject[len(prefix) :].lstrip()
            break
    if "?" in subject:
        subject = subject.split("?", 1)[0]
    if ". " in subject:
        subject = subject.split(". ", 1)[0]
    if len(subject) > 150:
        boundary = max(subject.rfind(", ", 0, 145), subject.rfind("; ", 0, 145))
        if boundary < 70:
            boundary = 147
        subject = subject[:boundary].rstrip(",; ") + "..."
    return subject or "the prompt"


def evidence_target(kind: str, record: ChapterRecord) -> str:
    targets = {
        "definition": "definition, boundary condition, and one concrete example",
        "mechanism": "causal sequence, named components, and a measurable intermediate",
        "comparison": "two comparison axes, shared feature, difference, and consequence",
        "quantitative": "equation or ratio, substitutions with units, range check, and interpretation",
        "experimental": "hypothesis, control, measured response, predicted pattern, and falsifier",
        "evaluation": "judgment, two evidence lines, limitation, and condition that would change the conclusion",
        "application": "chapter principle, decisive evidence in the scenario, and observable prediction",
    }
    return targets[kind] + f" from \\cref{{{record.section_ref}}}"


def scholarship_check(kind: str) -> str:
    checks = {
        "definition": "give the scale or context where the definition changes interpretation",
        "mechanism": "separate mechanism from correlation and name the weakest inferential step",
        "comparison": "explain why the contrast changes prediction or interpretation",
        "quantitative": "report assumptions, units, and whether model choice could change the conclusion",
        "experimental": "make the control strong enough that a negative result would be informative",
        "evaluation": "separate empirical evidence from value judgments and state a counterexample",
        "application": "state which observation would decide between the chapter model and an alternative",
    }
    return checks[kind]


def prompt_cues(question: str) -> str:
    """Extract a compact list of requirements already present in the prompt."""

    cues: list[str] = []
    for marker, body in re.findall(r"\(([a-e])\)\s*([^;(]+(?:\([^)]*\))?)", question):
        cue = " ".join(body.split()).strip(" .")
        if cue:
            cues.append(f"{marker}) {cue}")
    if cues:
        return "; ".join(cues[:5])

    quantities: list[str] = []
    quantity_pattern = re.compile(
        r"(?<![-A-Za-z])(?P<op>[~≈<>])?\s*(?P<num>\d+(?:\.\d+)?)\s*"
        r"(?P<unit>%|km²|ha|mm|°C|yr|years?|days?|individuals?|species|M|s⁻¹)?"
        r"(?:\s*(?P<scale>million|billion|trillion))?",
        flags=re.IGNORECASE,
    )
    for match in quantity_pattern.finditer(question):
        op = match.group("op") or ""
        num = match.group("num")
        unit = match.group("unit") or ""
        scale = match.group("scale") or ""
        if not (op or unit or scale or "." in num or float(num) > 10):
            continue
        quantities.append(" ".join(part for part in (op + num, unit, scale) if part).strip())
    if quantities:
        return "carry through the provided values " + ", ".join(list(dict.fromkeys(quantities))[:5])

    stop_words = {
        "Apply",
        "Assess",
        "Calculate",
        "Compare",
        "Construct",
        "Critically",
        "Define",
        "Describe",
        "Design",
        "Determine",
        "Distinguish",
        "During",
        "Evaluate",
        "Explain",
        "For",
        "Give",
        "How",
        "Identify",
        "In",
        "List",
        "Name",
        "Predict",
        "Propose",
        "Rank",
        "State",
        "The",
        "Using",
        "What",
        "Why",
    }
    named_items = re.findall(r"\b[A-Z][A-Za-z0-9+/βαγδκλ-]{2,}\b", question)
    named_items = [item for item in named_items if item not in stop_words]
    if named_items:
        unique = list(dict.fromkeys(named_items))[:6]
        return "explicitly use " + ", ".join(unique)

    return "answer every requested clause, not just the opening phrase"


def common_pitfall(kind: str, question: str) -> str:
    q = question.lower()
    if kind == "quantitative":
        return "writing a formula without checking units, assumptions, or biological meaning"
    if "correlation" in q or "evidence" in q or kind == "evaluation":
        return "treating evidence strength and personal judgment as the same thing"
    if kind == "comparison":
        return "listing two facts without naming the decision that the contrast changes"
    if kind == "experimental":
        return "proposing a measurement without a baseline, control, or falsifying result"
    if kind == "mechanism":
        return "jumping from input to outcome without the intermediate biological step"
    return "giving a vocabulary label without an example, boundary condition, or consequence"


def answer_key(q_num: int, question: str, record: ChapterRecord) -> str:
    kind = question_kind(question)
    tier = "Recall" if q_num <= 10 else "Application" if q_num <= 20 else "Synthesis"
    focus = FOCUS_BY_STEM[record.stem]
    subject = subject_phrase(question)
    return (
        f"**Answer (Q{q_num}, {tier}).** The response on *{subject}* should use "
        f"the {evidence_target(kind, record)}. Prompt-specific details to include: "
        f"{prompt_cues(question)}. Evidence standard: {scholarship_check(kind)}. "
        f"Avoid {common_pitfall(kind, question)}. Chapter context: {focus}"
    )


def refine_question_banks(records: list[ChapterRecord], dry_run: bool) -> tuple[int, int]:
    changed_files = 0
    changed_blocks = 0
    by_question_path = {record.question_path: record for record in records}
    for path, record in sorted(by_question_path.items()):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        questions = {int(m.group(1)): m.group(2) for m in _QUESTION_LINE.finditer(text)}
        counter = 0

        def repl(
            match: re.Match[str],
            *,
            chapter_record: ChapterRecord = record,
            chapter_questions: dict[int, str] = questions,
        ) -> str:
            nonlocal counter, changed_blocks
            counter += 1
            body = match.group(2).strip()
            q_num = counter
            if not any(sig in body for sig in ANSWER_SIGNATURES):
                return match.group(0)
            new_body = answer_key(q_num, chapter_questions.get(q_num, ""), chapter_record)
            if new_body == body:
                return match.group(0)
            changed_blocks += 1
            return f"{match.group(1)}{new_body}{match.group(3)}"

        new_text = _SOLUTION_BLOCK.sub(repl, text)
        if new_text != text:
            changed_files += 1
            if not dry_run:
                write_text_atomic(path, new_text)
    return changed_files, changed_blocks


def count_pattern(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, flags=re.MULTILINE))


def write_audit_matrix(records: list[ChapterRecord], dry_run: bool) -> int:
    lines = [
        "# Embedded Enrichment Audit Matrix",
        "",
        "Generated by `scripts/enrich_embedded_textbook.py`. This matrix is a planning and review surface; canonical ordering remains `manuscript/config.yaml`.",
        "",
        "| Unit | Surface | Path | Current evidence | Embedded pass target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        chapter_text = record.chapter_path.read_text(encoding="utf-8")
        h2_count = count_pattern(chapter_text, r"^##\s+")
        citation_count = count_pattern(chapter_text, r"\\cite[tp]?\{")
        mermaid_count = count_pattern(chapter_text, r"^```mermaid")
        chapter_evidence = (
            f"{len(chapter_text):,} chars; "
            f"{h2_count} H2; "
            f"{citation_count} citations; "
            f"{mermaid_count} Mermaid"
        )
        lines.append(
            f"| {record.unit_id} | Chapter | `{record.chapter_path.relative_to(PROJECT)}` | {chapter_evidence} | Current evidence/frontier box; accessibility and citation review |"
        )
        if record.lab_path.exists():
            lab_text = record.lab_path.read_text(encoding="utf-8")
            lines.append(
                f"| {record.unit_id} | Lab | `{record.lab_path.relative_to(PROJECT)}` | {len(lab_text):,} chars | Paper-based evidence upgrade, controls, uncertainty, reproducibility |"
            )
        if record.question_path.exists():
            question_text = record.question_path.read_text(encoding="utf-8")
            solution_count = count_pattern(question_text, r"<!-- SOLUTION")
            lines.append(
                f"| {record.unit_id} | Questions | `{record.question_path.relative_to(PROJECT)}` | {solution_count} solution blocks | Prompt-specific answer keys, evidence use, scholarship checks |"
            )
    glossary_text = (MANUSCRIPT / "glossary.md").read_text(encoding="utf-8")
    glossary_anchor_count = count_pattern(glossary_text, r"\{#gl:")
    lines.extend(
        [
            f"| all | Glossary | `manuscript/glossary.md` | {glossary_anchor_count} anchors | Semantic references, qualified definitions, first-use closure |",
            "| all | Appendices | `manuscript/appendices/*.md` | reference appendices | Accessibility, semantic references, no hard-coded rendered numbers |",
            "",
            "## Review Defaults",
            "",
            "- Preserve 38 chapters, 38 labs, and 38 question banks.",
            "- Add embedded improvements only; do not add new renderable chapter surfaces.",
            "- Cite or qualify recent and numeric claims.",
            "- Keep required labs paper-based; optional material extensions stay clearly optional.",
            "- Use `\\cref{...}` and generated figure/equation labels instead of hard-coded rendered numbers.",
        ]
    )
    out = DOCS / "embedded_enrichment_audit_matrix.md"
    text = "\n".join(lines) + "\n"
    old = out.read_text(encoding="utf-8") if out.exists() else ""
    if text == old:
        return 0
    if not dry_run:
        write_text_atomic(out, text)
    return 1


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    records = chapter_records()
    matrix = write_audit_matrix(records, args.dry_run)
    unit_intros = enrich_unit_intros(args.dry_run)
    chapters = enrich_chapters(records, args.dry_run)
    scholarship_bullets = refresh_chapter_scholarship_bullets(records, args.dry_run)
    companion_modules = normalize_companion_source_modules(records, args.dry_run)
    labs = enrich_labs(records, args.dry_run)
    question_files, question_blocks = refine_question_banks(records, args.dry_run)
    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(
        f"[{mode}] matrix={matrix} unit_intros={unit_intros} chapters={chapters} "
        f"scholarship_bullets={scholarship_bullets} companion_modules={companion_modules} labs={labs} "
        f"question_files={question_files} question_blocks={question_blocks}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
