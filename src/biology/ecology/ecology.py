"""Ecology module.

Covers population growth, Lotka-Volterra predator-prey dynamics,
food web graph analysis, biodiversity indices, and biome characterization.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class Species:
    """A species in an ecological community."""

    name: str
    trophic_level: float  # 1=producer, 2=primary consumer, etc.
    population: float  # current population size
    biomass_kg_per_ind: float = 1.0


@dataclass
class PopulationGrowthResult:
    """Time series from population growth model."""

    times: list[float]
    populations: list[float]
    model: str


@dataclass
class LotkaVolterraResult:
    """Time series from Lotka-Volterra predator-prey model."""

    times: list[float]
    prey: list[float]
    predator: list[float]
    alpha: float  # prey growth rate
    beta: float  # predation rate
    delta: float  # predator growth per prey eaten
    gamma: float  # predator death rate


@dataclass
class BiodiversityResult:
    """Diversity indices for a community."""

    shannon_index: float
    simpson_index: float
    species_richness: int
    evenness: float


# ---------------------------------------------------------------------------
# Population Growth Models
# ---------------------------------------------------------------------------


def exponential_growth(
    N0: float,
    r: float,
    t_end: float,
    steps: int = 100,
) -> PopulationGrowthResult:
    """Simulate exponential population growth: dN/dt = rN.

    Args:
        N0: Initial population size.
        r: Intrinsic rate of increase (per time unit).
        t_end: Total time to simulate.
        steps: Number of time steps.

    Returns:
        PopulationGrowthResult with time series.

    Raises:
        ValueError: If N0 ≤ 0 or steps ≤ 0.
    """
    if N0 <= 0:
        raise ValueError("N0 must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")
    if t_end <= 0:
        raise ValueError("t_end must be positive.")

    dt = t_end / steps
    times = [i * dt for i in range(steps + 1)]
    pops = [N0 * math.exp(r * t) for t in times]
    logger.debug(f"Exponential growth: N0={N0}, r={r}, final N={pops[-1]:.2f}")
    return PopulationGrowthResult(times=times, populations=pops, model="exponential")


def logistic_growth(
    N0: float,
    r: float,
    K: float,
    t_end: float,
    steps: int = 200,
) -> PopulationGrowthResult:
    """Simulate logistic population growth using Euler integration.

    dN/dt = r * N * (1 - N/K)

    Args:
        N0: Initial population.
        r: Intrinsic growth rate.
        K: Carrying capacity.
        t_end: Total simulation time.
        steps: Number of integration steps.

    Returns:
        PopulationGrowthResult with time series.

    Raises:
        ValueError: If any parameter is invalid.
    """
    if N0 <= 0:
        raise ValueError("N0 must be positive.")
    if K <= 0:
        raise ValueError("K (carrying capacity) must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")
    if t_end <= 0:
        raise ValueError("t_end must be positive.")

    dt = t_end / steps
    times = [0.0]
    pops = [N0]
    N = N0

    for _ in range(steps):
        dN = r * N * (1.0 - N / K)
        N = max(0.0, N + dN * dt)
        times.append(times[-1] + dt)
        pops.append(N)

    logger.debug(f"Logistic growth: K={K}, r={r}, final N={pops[-1]:.2f}")
    return PopulationGrowthResult(times=times, populations=pops, model="logistic")


def allee_strong_growth(
    N0: float,
    r: float,
    A: float,
    K: float,
    t_end: float,
    steps: int = 500,
) -> PopulationGrowthResult:
    """Euler integration of the strong Allee + logistic model.

    dN/dt = r * N * (N/A - 1) * (1 - N/K)

    Below the Allee threshold A, per capita growth is negative (strong Allee);
    between A and K the population grows toward K.

    Args:
        N0: Initial population (non-negative).
        r: Intrinsic scale for growth rate (1/time).
        A: Allee threshold (must be positive, typically A < K).
        K: Carrying capacity.
        t_end: Total integration time.
        steps: Euler steps.

    Returns:
        PopulationGrowthResult time series.

    Raises:
        ValueError: If parameters are invalid.
    """
    if N0 < 0:
        raise ValueError("N0 must be non-negative.")
    if r <= 0:
        raise ValueError("r must be positive.")
    if A <= 0 or K <= 0:
        raise ValueError("A and K must be positive.")
    if A >= K:
        raise ValueError("Require A < K for a meaningful strong-Allee window below K.")
    if steps <= 0 or t_end <= 0:
        raise ValueError("steps and t_end must be positive.")

    dt = t_end / steps
    times = [0.0]
    pops = [N0]
    N = N0

    for _ in range(steps):
        dN = r * N * (N / A - 1.0) * (1.0 - N / K) * dt
        N = max(0.0, N + dN)
        times.append(times[-1] + dt)
        pops.append(N)

    logger.debug(
        "Allee strong: A=%s K=%s r=%s final N=%.4f",
        A,
        K,
        r,
        pops[-1],
    )
    return PopulationGrowthResult(times=times, populations=pops, model="allee_strong")


# ---------------------------------------------------------------------------
# Lotka-Volterra Predator-Prey
# ---------------------------------------------------------------------------


def lotka_volterra(
    prey0: float,
    predator0: float,
    alpha: float,
    beta: float,
    delta: float,
    gamma: float,
    t_end: float,
    steps: int = 1000,
) -> LotkaVolterraResult:
    """Simulate Lotka-Volterra predator-prey dynamics.

    dN/dt = α*N  - β*N*P
    dP/dt = δ*N*P - γ*P

    Args:
        prey0: Initial prey population.
        predator0: Initial predator population.
        alpha: Prey birth rate.
        beta: Predation rate.
        delta: Predator growth per prey eaten.
        gamma: Predator death rate.
        t_end: Simulation duration.
        steps: Number of Euler steps.

    Returns:
        LotkaVolterraResult with full time series.

    Raises:
        ValueError: If any parameter is non-positive.
    """
    for name, val in [
        ("prey0", prey0),
        ("predator0", predator0),
        ("alpha", alpha),
        ("beta", beta),
        ("delta", delta),
        ("gamma", gamma),
        ("t_end", t_end),
        ("steps", steps),
    ]:
        if val <= 0:
            raise ValueError(f"{name} must be positive, got {val}")

    dt = t_end / steps
    times = [0.0]
    prey_hist = [prey0]
    pred_hist = [predator0]

    N, P = prey0, predator0
    for _ in range(steps):
        dN = (alpha * N - beta * N * P) * dt
        dP = (delta * N * P - gamma * P) * dt
        N = max(0.0, N + dN)
        P = max(0.0, P + dP)
        times.append(times[-1] + dt)
        prey_hist.append(N)
        pred_hist.append(P)

    logger.info(f"Lotka-Volterra: {steps} steps, final prey={N:.2f}, predator={P:.2f}")
    return LotkaVolterraResult(
        times=times,
        prey=prey_hist,
        predator=pred_hist,
        alpha=alpha,
        beta=beta,
        delta=delta,
        gamma=gamma,
    )


# ---------------------------------------------------------------------------
# Food Web
# ---------------------------------------------------------------------------


def food_web_trophic_levels(
    adjacency: dict[str, list[str]],
) -> dict[str, int]:
    """Estimate trophic levels from a food web adjacency list (BFS from producers).

    Args:
        adjacency: Dict mapping species name → list of species it eats.
                   Producers have an empty list.

    Returns:
        Dict mapping species → trophic level (1-indexed).
    """
    # Producers: nodes that eat nothing
    producers = {sp for sp, prey in adjacency.items() if not prey}
    levels: dict[str, int] = {sp: 1 for sp in producers}

    # BFS upward
    queue: list[str] = list(producers)
    while queue:
        current = queue.pop(0)
        # find who eats current
        for predator, prey_list in adjacency.items():
            if current in prey_list and predator not in levels:
                levels[predator] = levels[current] + 1
                queue.append(predator)

    return levels


def connectance(
    num_species: int,
    num_links: int,
) -> float:
    """Compute food web connectance C = L / S²

    Args:
        num_species: S — number of species.
        num_links: L — number of trophic links.

    Returns:
        Connectance value in [0, 1].

    Raises:
        ValueError: If num_species ≤ 0.
    """
    if num_species <= 0:
        raise ValueError("num_species must be positive.")
    return num_links / (num_species**2)


def species_area_relationship(
    A: float,
    c: float,
    z: float,
) -> float:
    """Compute species richness S = c * A^z.

    Args:
        A: Area.
        c: Species-specific constant (intercept).
        z: Scaling exponent (slope in log-log space).

    Returns:
        Predicted species richness S.
    """
    if A <= 0:
        raise ValueError("Area must be positive.")
    return float(c * (A**z))


# ---------------------------------------------------------------------------
# Biodiversity Indices
# ---------------------------------------------------------------------------


def biodiversity_indices(species_counts: list[int]) -> BiodiversityResult:
    """Compute Shannon, Simpson, and evenness indices.

    Args:
        species_counts: List of individual counts per species.

    Returns:
        BiodiversityResult with all indices.

    Raises:
        ValueError: If all counts are zero or list is empty.
    """
    if not species_counts:
        raise ValueError("species_counts must not be empty.")
    total = sum(species_counts)
    if total == 0:
        raise ValueError("Total count must be positive.")

    proportions = [c / total for c in species_counts if c > 0]
    S = len(proportions)

    # Shannon index H' = -Σ p_i ln(p_i)
    H = -sum(p * math.log(p) for p in proportions)

    # Simpson index D = 1 - Σ p_i²
    D = 1.0 - sum(p**2 for p in proportions)

    # Pielou's evenness J = H / ln(S)
    J = H / math.log(S) if S > 1 else 1.0

    logger.debug(f"Biodiversity: H={H:.4f}, D={D:.4f}, J={J:.4f}, S={S}")
    return BiodiversityResult(shannon_index=H, simpson_index=D, species_richness=S, evenness=J)


# ---------------------------------------------------------------------------
# Biome Data
# ---------------------------------------------------------------------------

BIOMES: dict[str, dict] = {
    "Tropical Rainforest": {
        "mean_annual_temp_C": 25.0,
        "annual_precipitation_mm": 2500,
        "species_richness_rank": 1,
        "NPP_g_m2_yr": 2200,
    },
    "Temperate Deciduous Forest": {
        "mean_annual_temp_C": 10.0,
        "annual_precipitation_mm": 900,
        "species_richness_rank": 4,
        "NPP_g_m2_yr": 1200,
    },
    "Grassland/Savanna": {
        "mean_annual_temp_C": 20.0,
        "annual_precipitation_mm": 500,
        "species_richness_rank": 5,
        "NPP_g_m2_yr": 900,
    },
    "Desert": {
        "mean_annual_temp_C": 30.0,
        "annual_precipitation_mm": 100,
        "species_richness_rank": 7,
        "NPP_g_m2_yr": 100,
    },
    "Tundra": {
        "mean_annual_temp_C": -10.0,
        "annual_precipitation_mm": 250,
        "species_richness_rank": 8,
        "NPP_g_m2_yr": 140,
    },
    "Marine": {
        "mean_annual_temp_C": 15.0,
        "annual_precipitation_mm": 0,
        "species_richness_rank": 2,
        "NPP_g_m2_yr": 500,
    },
}

# Alias for manuscript compatibility
BIOME_DATA = BIOMES

# Alias for manuscript footer compatibility
species_diversity_indices = biodiversity_indices
