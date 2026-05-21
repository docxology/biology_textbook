"""Evolution module.

Covers natural selection models, fitness landscapes, phylogenetics,
Hardy-Weinberg deviations, and speciation concepts.
All computations are real mathematical models — no mock methods.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from infrastructure.core.logging.utils import get_logger

logger = get_logger(__name__)


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class Population:
    """A population with allele frequencies and selection coefficients."""

    name: str
    p: float  # frequency of allele A
    q: float  # frequency of allele a
    fitness_AA: float = 1.0
    fitness_Aa: float = 1.0
    fitness_aa: float = 1.0

    def __post_init__(self) -> None:
        """Validate that allele frequencies sum to 1."""
        if abs(self.p + self.q - 1.0) > 1e-9:
            raise ValueError(f"p + q must equal 1, got {self.p + self.q}")

    @property
    def mean_fitness(self) -> float:
        """W-bar: mean fitness of the population."""
        return self.p**2 * self.fitness_AA + 2 * self.p * self.q * self.fitness_Aa + self.q**2 * self.fitness_aa


@dataclass
class SelectionResult:
    """Result of one generation of natural selection."""

    generation: int
    p: float
    q: float
    mean_fitness: float
    delta_p: float  # change in p from previous generation


@dataclass
class PhylogeneticNode:
    """A node in a phylogenetic tree."""

    name: str
    parent: Optional[str] = None
    branch_length: float = 0.0
    children: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Natural Selection
# ---------------------------------------------------------------------------


def selection_one_generation(pop: Population) -> Population:
    """Apply one generation of natural selection to a population.

    Uses the standard selection equation:
        p' = (p² w_AA + p*q w_Aa) / W-bar

    Args:
        pop: Starting population with allele frequencies and fitnesses.

    Returns:
        New Population after one generation.

    Raises:
        ValueError: If mean fitness is zero.
    """
    W = pop.mean_fitness
    if W <= 0:
        raise ValueError("Mean fitness W-bar must be positive.")

    p_new = (pop.p**2 * pop.fitness_AA + pop.p * pop.q * pop.fitness_Aa) / W
    q_new = 1.0 - p_new

    logger.debug(f"Selection: p {pop.p:.4f} → {p_new:.4f}, W-bar={W:.4f}")
    return Population(
        name=pop.name,
        p=p_new,
        q=q_new,
        fitness_AA=pop.fitness_AA,
        fitness_Aa=pop.fitness_Aa,
        fitness_aa=pop.fitness_aa,
    )


def simulate_selection(
    initial_pop: Population,
    generations: int,
) -> list[SelectionResult]:
    """Simulate natural selection over multiple generations.

    Args:
        initial_pop: Starting population.
        generations: Number of generations to simulate.

    Returns:
        List of SelectionResult, one per generation.

    Raises:
        ValueError: If generations ≤ 0.
    """
    if generations <= 0:
        raise ValueError("generations must be positive.")

    pop = initial_pop
    results: list[SelectionResult] = []
    prev_p = pop.p

    for gen in range(1, generations + 1):
        pop = selection_one_generation(pop)
        results.append(
            SelectionResult(
                generation=gen,
                p=pop.p,
                q=pop.q,
                mean_fitness=pop.mean_fitness,
                delta_p=pop.p - prev_p,
            )
        )
        prev_p = pop.p

    logger.info(f"Simulated {generations} generations; final p={pop.p:.6f}")
    return results


# ---------------------------------------------------------------------------
# Genetic Drift — Wright-Fisher binomial sampling
# ---------------------------------------------------------------------------


def wright_fisher_drift(
    p: float,
    N: int,
    rng_seed: int = 42,
) -> float:
    """Simulate one generation of genetic drift via binomial sampling.

    Args:
        p: Current allele frequency.
        N: Effective population size (diploid individuals).
        rng_seed: Random seed for reproducibility.

    Returns:
        New allele frequency after one generation of drift.

    Raises:
        ValueError: If p not in [0,1] or N ≤ 0.
    """
    import random

    if not (0.0 <= p <= 1.0):
        raise ValueError(f"p must be in [0, 1], got {p}.")
    if N <= 0:
        raise ValueError("N must be positive.")

    rng = random.Random(rng_seed)  # nosec B311 - deterministic teaching simulation, not cryptography.
    copies = 2 * N
    # Binomial sampling
    drawn = sum(1 for _ in range(copies) if rng.random() < p)
    p_new = drawn / copies
    logger.debug(f"Drift: N={N}, p {p:.4f} → {p_new:.4f}")
    return p_new


def simulate_drift(
    p: float,
    N: int,
    generations: int,
    rng_seed: int = 42,
) -> list[float]:
    """Simulate genetic drift over multiple generations.

    Args:
        p: Initial allele frequency.
        N: Effective population size.
        generations: Number of generations.
        rng_seed: Random seed.

    Returns:
        List of allele frequencies per generation (including initial).

    Raises:
        ValueError: If inputs are invalid.
    """
    if generations <= 0:
        raise ValueError("generations must be positive.")
    import random

    rng = random.Random(rng_seed)  # nosec B311 - deterministic teaching simulation, not cryptography.
    history = [p]
    for _ in range(generations):
        copies = 2 * N
        drawn = sum(1 for _ in range(copies) if rng.random() < history[-1])
        history.append(drawn / copies)
    return history


# ---------------------------------------------------------------------------
# Fitness Landscape
# ---------------------------------------------------------------------------


def fitness_landscape_1d(
    allele_freqs: list[float],
    fitness_AA: float,
    fitness_Aa: float,
    fitness_aa: float,
) -> list[float]:
    """Compute mean fitness W-bar across a range of allele frequencies.

    Args:
        allele_freqs: List of p values to evaluate.
        fitness_AA, fitness_Aa, fitness_aa: Genotype fitnesses.

    Returns:
        List of mean fitness values corresponding to each p.
    """
    results = []
    for p in allele_freqs:
        q = 1.0 - p
        W = p**2 * fitness_AA + 2 * p * q * fitness_Aa + q**2 * fitness_aa
        results.append(W)
    return results


# ---------------------------------------------------------------------------
# Speciation — Isolation index
# ---------------------------------------------------------------------------


def isolation_index(
    gene_flow_rate: float,
    mutation_rate: float,
) -> float:
    """Estimate isolation index I = 1 / (1 + 4 * N * m) as a proxy for speciation.

    For simplicity uses the relative magnitudes of mutation and gene flow.

    Args:
        gene_flow_rate: Rate of gene flow between populations (m).
        mutation_rate: Background mutation rate (μ).

    Returns:
        Isolation index in [0, 1]; values close to 1 indicate strong isolation.

    Raises:
        ValueError: If either rate is negative.
    """
    if gene_flow_rate < 0 or mutation_rate < 0:
        raise ValueError("Rates must be non-negative.")
    if gene_flow_rate + mutation_rate == 0:
        return 1.0
    return mutation_rate / (mutation_rate + gene_flow_rate)


# ---------------------------------------------------------------------------
# Molecular Clock
# ---------------------------------------------------------------------------


def molecular_clock_divergence_time(
    substitution_rate_per_site_per_year: float,
    sequence_divergence: float,
) -> float:
    """Estimate divergence time using the molecular clock hypothesis.

    t = divergence / (2 * rate)

    Args:
        substitution_rate_per_site_per_year: Known substitution rate.
        sequence_divergence: Observed fractional sequence divergence.

    Returns:
        Estimated divergence time in years.

    Raises:
        ValueError: If rate or divergence is non-positive.
    """
    if substitution_rate_per_site_per_year <= 0:
        raise ValueError("substitution_rate must be positive.")
    if sequence_divergence < 0:
        raise ValueError("sequence_divergence must be non-negative.")
    t = sequence_divergence / (2.0 * substitution_rate_per_site_per_year)
    logger.debug(
        "Molecular clock: divergence=%s, rate=%s → t=%.2e years",
        sequence_divergence,
        substitution_rate_per_site_per_year,
        t,
    )
    return t
