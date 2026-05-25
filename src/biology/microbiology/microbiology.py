"""Microbiology module.

Covers bacterial growth curves, doubling time, viral replication cycles,
antibiotic resistance (MIC), and microbial classification.
All computations are real microbiological models — no mock methods.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class GrowthCurveResult:
    """Bacterial population growth over time."""

    times_hr: list[float]
    populations: list[float]  # number of cells
    log_populations: list[float]
    doubling_time_hr: float
    growth_rate_per_hr: float


@dataclass
class ViralReplicationResult:
    """Simplified one-step viral replication cycle data."""

    eclipse_period_hr: float  # time before first phage released
    burst_size: int  # virions released per host cell
    latent_period_hr: float  # eclipse + maturation
    replication_type: str  # "lytic" or "lysogenic"


@dataclass
class SIRResult:
    """Susceptible-infected-recovered epidemic trajectory."""

    times_days: list[float]
    susceptible: list[float]
    infected: list[float]
    recovered: list[float]
    r0: float


@dataclass
class MicrobialOrganism:
    """A reference microbial species."""

    name: str
    domain: str  # Bacteria, Archaea, Eukarya, Virus
    kingdom: str
    cell_wall: str  # composition
    example_habitat: str
    gram_stain: str = "N/A"  # "positive", "negative", or "N/A"
    oxygen_requirement: str = "aerobic"


# ---------------------------------------------------------------------------
# Bacterial Growth
# ---------------------------------------------------------------------------


def bacterial_growth_curve(
    N0: float,
    doubling_time_hr: float,
    t_end_hr: float,
    steps: int = 200,
    lag_phase_hr: float = 1.0,
    stationary_phase_start_hr: float | None = None,
    carrying_capacity: float | None = None,
) -> GrowthCurveResult:
    """Simulate a full bacterial growth curve with lag and stationary phases.

    During exponential phase: N(t) = N0 * 2^((t - lag) / t_d)
    Stationary phase: N = carrying_capacity (constant).

    Args:
        N0: Initial cell count.
        doubling_time_hr: Time for population to double (hours).
        t_end_hr: Total simulation time (hours).
        steps: Number of time steps.
        lag_phase_hr: Duration of lag phase (hours).
        stationary_phase_start_hr: Time at which stationary phase begins.
        carrying_capacity: Max population in stationary phase.

    Returns:
        GrowthCurveResult with full time series.

    Raises:
        ValueError: If parameters are invalid.
    """
    if N0 <= 0:
        raise ValueError("N0 must be positive.")
    if doubling_time_hr <= 0:
        raise ValueError("doubling_time_hr must be positive.")
    if t_end_hr <= 0:
        raise ValueError("t_end_hr must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")

    mu = math.log(2) / doubling_time_hr  # specific growth rate hr⁻¹
    dt = t_end_hr / steps
    times = [i * dt for i in range(steps + 1)]
    pops = []

    for t in times:
        if t < lag_phase_hr:
            N = N0
        else:
            N = N0 * (2 ** ((t - lag_phase_hr) / doubling_time_hr))
            if stationary_phase_start_hr is not None and t >= stationary_phase_start_hr:
                N = carrying_capacity or N
        pops.append(N)

    log_pops = [math.log10(max(p, 1.0)) for p in pops]
    logger.debug(f"Growth curve: t_d={doubling_time_hr}h, final N={pops[-1]:.2e}")
    return GrowthCurveResult(
        times_hr=times,
        populations=pops,
        log_populations=log_pops,
        doubling_time_hr=doubling_time_hr,
        growth_rate_per_hr=mu,
    )


def doubling_time(
    N0: float,
    Nt: float,
    elapsed_time_hr: float,
) -> float:
    """Calculate doubling time from population measurements.

    t_d = elapsed_time * ln(2) / ln(Nt / N0)

    Args:
        N0: Initial population.
        Nt: Final population.
        elapsed_time_hr: Elapsed time (hours).

    Returns:
        Doubling time in hours.

    Raises:
        ValueError: If populations are invalid or time ≤ 0.
    """
    if N0 <= 0 or Nt <= 0:
        raise ValueError("Populations must be positive.")
    if Nt <= N0:
        raise ValueError("Nt must be greater than N0 for growth calculation.")
    if elapsed_time_hr <= 0:
        raise ValueError("elapsed_time_hr must be positive.")
    return elapsed_time_hr * math.log(2) / math.log(Nt / N0)


# ---------------------------------------------------------------------------
# Minimum Inhibitory Concentration
# ---------------------------------------------------------------------------


def mic_fold_dilution(
    starting_concentration_ug_mL: float,
    dilution_factor: int,
    n_tubes: int,
) -> list[float]:
    """Compute antibiotic concentrations across a broth dilution MIC series.

    Args:
        starting_concentration_ug_mL: Highest concentration (µg/mL).
        dilution_factor: Serial dilution factor (typically 2).
        n_tubes: Number of dilution tubes.

    Returns:
        List of antibiotic concentrations in descending order.

    Raises:
        ValueError: If parameters are invalid.
    """
    if starting_concentration_ug_mL <= 0:
        raise ValueError("starting_concentration_ug_mL must be positive.")
    if dilution_factor < 2:
        raise ValueError("dilution_factor must be ≥ 2.")
    if n_tubes < 1:
        raise ValueError("n_tubes must be ≥ 1.")
    return [starting_concentration_ug_mL / (dilution_factor**i) for i in range(n_tubes)]


# ---------------------------------------------------------------------------
# Epidemic Dynamics
# ---------------------------------------------------------------------------


def basic_reproduction_number(beta_per_day: float, gamma_per_day: float) -> float:
    """Compute the SIR basic reproduction number R0 = beta / gamma."""
    if beta_per_day < 0:
        raise ValueError("beta_per_day must be non-negative.")
    if gamma_per_day <= 0:
        raise ValueError("gamma_per_day must be positive.")
    return beta_per_day / gamma_per_day


def sir_model(
    population: int,
    initial_infected: int,
    beta_per_day: float,
    gamma_per_day: float,
    days: float,
    steps_per_day: int = 4,
) -> SIRResult:
    """Simulate a closed-population SIR outbreak with Euler integration.

    Args:
        population: Total population size.
        initial_infected: Initial infected individuals.
        beta_per_day: Transmission coefficient per day.
        gamma_per_day: Recovery coefficient per day.
        days: Simulated duration in days.
        steps_per_day: Euler substeps per day.

    Returns:
        SIRResult containing time series and R0.

    Raises:
        ValueError: If any parameter is outside the model domain.
    """
    if population <= 0:
        raise ValueError("population must be positive.")
    if not (0 < initial_infected <= population):
        raise ValueError("initial_infected must be in [1, population].")
    if beta_per_day < 0:
        raise ValueError("beta_per_day must be non-negative.")
    if gamma_per_day <= 0:
        raise ValueError("gamma_per_day must be positive.")
    if days <= 0:
        raise ValueError("days must be positive.")
    if steps_per_day <= 0:
        raise ValueError("steps_per_day must be positive.")

    steps = int(days * steps_per_day)
    dt = 1.0 / steps_per_day
    susceptible_now = float(population - initial_infected)
    infected_now = float(initial_infected)
    recovered_now = 0.0
    times = [0.0]
    susceptible = [susceptible_now]
    infected = [infected_now]
    recovered = [recovered_now]

    for step in range(1, steps + 1):
        new_infections = beta_per_day * susceptible_now * infected_now / population
        new_recoveries = gamma_per_day * infected_now
        susceptible_now = max(0.0, susceptible_now - new_infections * dt)
        infected_now = max(0.0, infected_now + (new_infections - new_recoveries) * dt)
        recovered_now = min(float(population), recovered_now + new_recoveries * dt)
        times.append(step * dt)
        susceptible.append(susceptible_now)
        infected.append(infected_now)
        recovered.append(recovered_now)

    return SIRResult(
        times_days=times,
        susceptible=susceptible,
        infected=infected,
        recovered=recovered,
        r0=basic_reproduction_number(beta_per_day, gamma_per_day),
    )


# ---------------------------------------------------------------------------
# Viral Replication Reference Data
# ---------------------------------------------------------------------------

VIRAL_REPLICATION_CYCLES: dict[str, ViralReplicationResult] = {
    "T4 bacteriophage (lytic)": ViralReplicationResult(
        eclipse_period_hr=0.33,
        burst_size=200,
        latent_period_hr=0.5,
        replication_type="lytic",
    ),
    "Lambda phage (lysogenic)": ViralReplicationResult(
        eclipse_period_hr=0.5,
        burst_size=100,
        latent_period_hr=1.0,
        replication_type="lysogenic",
    ),
    "Influenza A (animal virus)": ViralReplicationResult(
        eclipse_period_hr=4.0,
        burst_size=500,
        latent_period_hr=8.0,
        replication_type="lytic",
    ),
}


# ---------------------------------------------------------------------------
# Reference Organisms
# ---------------------------------------------------------------------------

REFERENCE_ORGANISMS: list[MicrobialOrganism] = [
    MicrobialOrganism(
        "Escherichia coli",
        "Bacteria",
        "Proteobacteria",
        "Peptidoglycan (thin)",
        "Intestinal flora",
        gram_stain="negative",
        oxygen_requirement="facultative anaerobe",
    ),
    MicrobialOrganism(
        "Staphylococcus aureus",
        "Bacteria",
        "Firmicutes",
        "Peptidoglycan (thick)",
        "Skin microbiome",
        gram_stain="positive",
        oxygen_requirement="facultative anaerobe",
    ),
    MicrobialOrganism(
        "Mycobacterium tuberculosis",
        "Bacteria",
        "Actinobacteria",
        "Mycolic acids",
        "Lung tissue",
        gram_stain="acid-fast",
        oxygen_requirement="aerobic",
    ),
    MicrobialOrganism(
        "Saccharomyces cerevisiae",
        "Eukarya",
        "Fungi",
        "Chitin + β-glucan",
        "Soil / fermentation",
        oxygen_requirement="facultative anaerobe",
    ),
    MicrobialOrganism(
        "SARS-CoV-2",
        "Virus",
        "Coronaviridae",
        "Protein capsid + lipid envelope",
        "Respiratory tract",
        oxygen_requirement="N/A",
    ),
    MicrobialOrganism(
        "Methanobacterium thermoautotrophicum",
        "Archaea",
        "Methanobacteria",
        "Pseudopeptidoglycan",
        "Hydrothermal vents",
        oxygen_requirement="strict anaerobe",
    ),
]
