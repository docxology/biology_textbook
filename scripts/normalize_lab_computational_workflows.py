#!/usr/bin/env python3
"""Replace stale notebook-based lab sections with tested, self-contained snippets.

The textbook labs are paper-first activities. Optional computation should run
against this project's ``src/biology`` modules without requiring hidden
notebooks, CSV files, or dependencies outside ``pyproject.toml``.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from _bootstrap import PROJECT, ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = PROJECT / "manuscript"


@dataclass(frozen=True)
class LabWorkflow:
    """A replacement workflow for one lab's Part 2 computational exercise."""

    relative_path: str
    source_module: str
    body: str

    @property
    def path(self) -> Path:
        return MANUSCRIPT / self.relative_path


def _body(intro: str, code: str) -> str:
    return (
        "*Optional computational check: run this self-contained Python snippet from the project root. "
        "It uses tested `src/biology` modules and requires no external notebook or CSV file.*\n\n"
        f"{intro}\n\n"
        "```python\n"
        f"{code.strip()}\n"
        "```\n\n"
    )


WORKFLOWS: tuple[LabWorkflow, ...] = (
    LabWorkflow(
        "labs/unit_III/lab_photosynthesis.md",
        "src/biology/botany/botany.py",
        _body(
            "Compare your light-response table with the project photosynthesis model.",
            """
from biology.botany import photosynthesis_rate, light_response_curve

for light in (0, 100, 500, 1000):
    rate = photosynthesis_rate(light, max_rate_µmol_CO2_m2_s=22.0)
    print(light, round(rate, 2))

curve = light_response_curve(n_points=5)
print("first/last model points:", curve[0], curve[-1])
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_III/lab_metabolic_integration.md",
        "src/biology/biochemistry/biochemistry.py",
        _body(
            "Use the biochemical models to anchor the class discussion in measured quantities.",
            """
from biology.biochemistry import atp_free_energy, glycolysis_summary, michaelis_menten

glycolysis = glycolysis_summary()
rate = michaelis_menten(substrate_conc=2.0, Vmax=10.0, Km=2.0)
atp = atp_free_energy()

print("net ATP:", glycolysis.net_atp)
print("half-saturation rate:", round(rate.reaction_rate, 2))
print("ATP hydrolysis ΔG:", round(atp, 2))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_IV/lab_dna_replication_and_cell_cycle.md",
        "src/biology/genetics/genetics.py",
        _body(
            "Check template-strand logic before interpreting replication and cell-cycle data.",
            """
from biology.genetics import cpg_methylation_remaining, dna_complement, transcribe_dna_to_mrna

template = "TACGGA"
print("complement:", dna_complement(template))
print("mRNA:", transcribe_dna_to_mrna(template))
print("methylation after 3 divisions:", round(cpg_methylation_remaining(0.9, 3, 0.85), 3))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_IV/lab_epigenetics_and_gene_regulation.md",
        "src/biology/genetics/genetics.py",
        _body(
            "Model maintenance methylation and classify histone marks without external files.",
            """
from biology.genetics import cpg_methylation_remaining, histone_modification_state

for efficiency in (0.95, 0.85, 0.60):
    remaining = cpg_methylation_remaining(0.8, divisions=4, maintenance_efficiency=efficiency)
    print(efficiency, round(remaining, 3))

for mark in ("H3K27me3", "H3K27ac", "H3K4me2"):
    print(mark, histone_modification_state(mark))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_IV/lab_mutations_and_genomics.md",
        "src/biology/genetics/genetics.py",
        _body(
            "Quantify sequence change with the same distance functions used in the chapter.",
            """
from biology.genetics import gc_content, hamming_distance, jukes_cantor_distance

reference = "ATGCGTAC"
variant = "ATGAGTTC"
p_distance = hamming_distance(reference, variant) / len(reference)

print("GC reference:", round(gc_content(reference), 2))
print("Hamming distance:", hamming_distance(reference, variant))
print("Jukes-Cantor distance:", round(jukes_cantor_distance(p_distance), 3))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_V/lab_chromosomal_inheritance.md",
        "src/biology/genetics/genetics.py",
        _body(
            "Infer a simple three-point map from pairwise recombination distances.",
            """
from biology.genetics import genetic_distance, infer_three_point_order

distances = {("A", "B"): 12.0, ("B", "C"): 8.0, ("A", "C"): 20.0}
order = infer_three_point_order(distances)

print("gene order:", " - ".join(order.order))
print("adjacent distances:", order.adjacent_distances_cM)
print("24 recombinants among 200 progeny:", genetic_distance(24, 200), "cM")
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_V/lab_mendelian_genetics.md",
        "src/biology/genetics/genetics.py",
        _body(
            "Validate the paper Punnett-square and chi-square calculations.",
            """
from biology.genetics import chi_squared_test, punnett_square

cross = punnett_square("Aa", "Aa")
observed = [450.0, 130.0]
expected = [0.75 * sum(observed), 0.25 * sum(observed)]
chi = chi_squared_test(observed, expected)

print("genotype ratios:", cross.genotype_ratios)
print("phenotype ratios:", cross.phenotype_ratios)
print("χ²:", round(chi.chi_squared, 2), "reject?", chi.reject_null)
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_VI/lab_evolution_and_selection.md",
        "src/biology/evolution/evolution.py",
        _body(
            "Compare a hand-calculated allele-frequency change with the selection simulator.",
            """
from biology.evolution import Population, simulate_selection

start = Population(name="demo", p=0.3, q=0.7, fitness_AA=1.0, fitness_Aa=0.9, fitness_aa=0.6)
history = simulate_selection(start, generations=10)

print("starting p:", start.p)
print("final p:", round(history[-1].p, 3))
print("generations recorded:", len(history))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_VI/lab_genetic_drift_and_speciation.md",
        "src/biology/evolution/evolution.py",
        _body(
            "Run deterministic drift simulations by fixing the random seed.",
            """
from biology.evolution import isolation_index, simulate_drift

small = simulate_drift(p=0.5, N=20, generations=10, rng_seed=7)
large = simulate_drift(p=0.5, N=500, generations=10, rng_seed=7)

print("small-population final p:", round(small[-1], 3))
print("large-population final p:", round(large[-1], 3))
print("isolation example:", round(isolation_index(gene_flow_rate=0.01, mutation_rate=0.001), 3))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_VII/lab_bacteria_archaea_viruses.md",
        "src/biology/microbiology/microbiology.py",
        _body(
            "Use the microbiology module to check growth and MIC calculations.",
            """
from biology.microbiology import bacterial_growth_curve, doubling_time, mic_fold_dilution

growth = bacterial_growth_curve(N0=1_000, doubling_time_hr=0.5, t_end_hr=4.0)
print("final population:", int(growth.populations[-1]))
print("doubling time from counts:", round(doubling_time(1_000, 16_000, 2.0), 2))
print("MIC dilution series:", mic_fold_dilution(128.0, dilution_factor=2, n_tubes=5))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_VII/lab_infectious_disease.md",
        "src/biology/microbiology/microbiology.py",
        _body(
            "Model outbreak curves with the tested SIR implementation.",
            """
from biology.microbiology import sir_model

baseline = sir_model(population=10_000, initial_infected=10, beta_per_day=0.35, gamma_per_day=0.1, days=30)
distancing = sir_model(population=10_000, initial_infected=10, beta_per_day=0.18, gamma_per_day=0.1, days=30)

print("baseline R0:", baseline.r0, "peak infected:", round(max(baseline.infected)))
print("distancing R0:", distancing.r0, "peak infected:", round(max(distancing.infected)))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_VII/lab_microbial_ecology.md",
        "src/biology/ecology/ecology.py",
        _body(
            "Calculate diversity from table counts and compare named reference organisms.",
            """
from biology.ecology import biodiversity_indices
from biology.microbiology import REFERENCE_ORGANISMS

counts = [42, 18, 15, 9, 6]
diversity = biodiversity_indices(counts)
print("Shannon:", round(diversity.shannon_index, 3))
print("evenness:", round(diversity.evenness, 3))
print("reference domains:", sorted({organism.domain for organism in REFERENCE_ORGANISMS}))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_VIII/lab_plant_reproduction.md",
        "src/biology/botany/botany.py",
        _body(
            "Use a growth curve as a quantitative analogue for pollen-tube extension.",
            """
from biology.botany import plant_biomass_growth

growth = plant_biomass_growth(
    initial_biomass_g=0.2,
    relative_growth_rate=0.35,
    carrying_capacity_g=10.0,
    duration_days=10,
)
print("initial biomass:", growth.biomass_g[0])
print("final biomass:", round(growth.biomass_g[-1], 2))
print("days recorded:", len(growth.times_days))
""",
        ),
    ),
    LabWorkflow(
        "labs/unit_VIII/lab_plant_structure_and_water.md",
        "src/biology/botany/botany.py",
        _body(
            "Check water-potential and transpiration calculations from your data table.",
            """
from biology.botany import transpiration_flux, water_potential

leaf = water_potential(solute_concentration_M=0.3, turgor_pressure_MPa=0.4)
flux = transpiration_flux(
    stomatal_conductance_mol_m2_s=0.2,
    internal_vapor_conc_mol_m3=0.5,
    external_vapor_conc_mol_m3=0.3,
)

print("water potential:", round(leaf.water_potential_MPa, 3), "MPa")
print("transpiration flux:", round(flux.flux_mmol_m2_s, 2), "mmol m^-2 s^-1")
""",
        ),
    ),
)


PART2_RE = re.compile(
    r"\*Complete this section using the provided Jupyter Notebook:[^\n]+\*\n\n.*?(?=\n### Part 3:)",
    re.DOTALL,
)
NOTEBOOK_LINE_RE = re.compile(r"- Investigate the Jupyter notebook `[^`]+` [^\n]+\n?")
MODULE_REPLACEMENTS = {
    "src/biology/genetics.py": "src/biology/genetics/genetics.py",
    "src/biology/evolution.py": "src/biology/evolution/evolution.py",
    "src/biology/microbiology.py": "src/biology/microbiology/microbiology.py",
    "src/biology/botany.py": "src/biology/botany/botany.py",
    "src/biology/biochemistry.py": "src/biology/biochemistry/biochemistry.py",
}


def normalise_lab(workflow: LabWorkflow, *, dry_run: bool = False) -> bool:
    """Normalise one lab file. Return True when content would change."""
    text = workflow.path.read_text(encoding="utf-8")
    new = text.replace(
        "| Computer with Python/Jupyter Notebook | 1 |",
        "| Calculator or optional Python REPL with this project installed | 1 |",
    )
    new = PART2_RE.sub(workflow.body.rstrip(), new)
    new = NOTEBOOK_LINE_RE.sub(
        "- Use the self-contained Part 2 snippet as the computational template; "
        "it runs against tested project modules without external notebooks or CSV files.\n",
        new,
    )
    for stale, current in MODULE_REPLACEMENTS.items():
        new = new.replace(stale, current)
    if new != text and not dry_run:
        write_text_atomic(workflow.path, new)
    return new != text


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    changed = 0
    for workflow in WORKFLOWS:
        if normalise_lab(workflow, dry_run=dry_run):
            changed += 1
            marker = "D" if dry_run else "+"
            print(f"  [{marker}] {workflow.relative_path} -> {workflow.source_module}")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] labs_normalised={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
