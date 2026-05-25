"""Visualization registry and backward-compatible re-exports."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from visualization.plots_botany import (
    plot_light_response_curve,
    plot_photosynthesis_rate,
    plot_water_potential_transpiration,
)
from visualization.plots_cell import (
    plot_chromosome_structure,
    plot_ghk_permeability,
    plot_hill_equation,
    plot_nernst_potentials,
    plot_osmotic_pressure,
)
from visualization.plots_ecology import (
    plot_allee_threshold_dynamics,
    plot_biome_distribution,
    plot_biodiversity_indices,
    plot_food_web_trophic_levels,
    plot_logistic_growth,
    plot_lotka_volterra,
    plot_species_area_relationship,
)
from visualization.plots_evolution import plot_fitness_landscape, plot_molecular_clock
from visualization.plots_genetics import (
    plot_genetic_drift_trajectories,
    plot_hardy_weinberg,
    plot_methylation_heatmap,
    plot_punnett_square,
    plot_selection_simulation,
    plot_translation_codons,
)
from visualization.plots_microbiology import (
    plot_bacterial_growth,
    plot_mic_dilution_series,
    plot_sir_model,
)
from visualization.plots_physiology import (
    plot_action_potential,
    plot_glycolysis_summary,
    plot_homeostasis_feedback,
    plot_michaelis_menten,
    plot_oxygen_dissociation,
    plot_poiseuille_flow,
)

FigureGenerator = Callable[[Path], Path]

FIGURE_ASPECT: dict[str, str] = {
    "lotka_volterra": "landscape",
    "hardy_weinberg": "landscape",
    "logistic_growth": "landscape",
    "species_area_relationship": "landscape",
    "genetic_drift_trajectories": "landscape",
    "selection_simulation": "landscape",
    "food_web_trophic_levels": "landscape",
}


ALL_FIGURE_GENERATORS: list[tuple[str, FigureGenerator]] = [
    ("nernst_potentials", plot_nernst_potentials),
    ("ghk_permeability", plot_ghk_permeability),
    ("hill_equation", plot_hill_equation),
    ("osmotic_pressure", plot_osmotic_pressure),
    ("punnett_square", lambda output_dir: plot_punnett_square("Aa", "Aa", output_dir)),
    ("chromosome_structure", plot_chromosome_structure),
    ("hardy_weinberg", plot_hardy_weinberg),
    ("translation_codons", plot_translation_codons),
    ("oxygen_dissociation", plot_oxygen_dissociation),
    ("poiseuille_flow", plot_poiseuille_flow),
    ("michaelis_menten", plot_michaelis_menten),
    ("glycolysis_summary", plot_glycolysis_summary),
    ("homeostasis_feedback", plot_homeostasis_feedback),
    ("lotka_volterra", plot_lotka_volterra),
    ("selection_simulation", plot_selection_simulation),
    ("fitness_landscape", plot_fitness_landscape),
    ("molecular_clock", plot_molecular_clock),
    ("action_potential", plot_action_potential),
    ("light_response_curves", plot_light_response_curve),
    ("photosynthesis_rate", plot_photosynthesis_rate),
    ("water_potential_transpiration", plot_water_potential_transpiration),
    ("bacterial_growth", plot_bacterial_growth),
    ("sir_model", plot_sir_model),
    ("mic_dilution_series", plot_mic_dilution_series),
    ("methylation_heatmap", plot_methylation_heatmap),
    ("logistic_growth", plot_logistic_growth),
    ("allee_threshold_dynamics", plot_allee_threshold_dynamics),
    ("biodiversity_indices", plot_biodiversity_indices),
    ("food_web_trophic_levels", plot_food_web_trophic_levels),
    ("species_area_relationship", plot_species_area_relationship),
    ("biome_distribution", plot_biome_distribution),
    ("genetic_drift_trajectories", plot_genetic_drift_trajectories),
]
