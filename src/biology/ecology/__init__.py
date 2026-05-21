"""Ecology subpackage."""

from .ecology import (
    Species,
    PopulationGrowthResult,
    LotkaVolterraResult,
    BiodiversityResult,
    exponential_growth,
    logistic_growth,
    allee_strong_growth,
    lotka_volterra,
    food_web_trophic_levels,
    connectance,
    biodiversity_indices,
    species_area_relationship,
    BIOMES,
    BIOME_DATA,
)

__all__ = [
    "Species",
    "PopulationGrowthResult",
    "LotkaVolterraResult",
    "BiodiversityResult",
    "exponential_growth",
    "logistic_growth",
    "allee_strong_growth",
    "lotka_volterra",
    "food_web_trophic_levels",
    "connectance",
    "biodiversity_indices",
    "species_area_relationship",
    "BIOMES",
    "BIOME_DATA",
]
