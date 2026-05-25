"""Network topology helpers for complex adaptive systems pedagogy.

Provides closed-form degree distributions for two reference network classes
used in the textbook: Erdos-Renyi-style random graphs (Poisson degree law) and
Barabasi-Albert-style scale-free graphs (power-law degree law). The helpers
return non-random tabulated probabilities so figures, tests, and prose all
agree on the same numbers.

References:
    Barabasi & Albert (1999) ``Emergence of scaling in random networks``.
    Erdos & Renyi (1960) ``On the evolution of random graphs``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from textbook_logging import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class DegreeDistribution:
    """Tabulated degree distribution P(k) for a network class."""

    name: str
    degrees: tuple[int, ...]
    probabilities: tuple[float, ...]
    mean_degree: float
    model: str


def _validate(k_min: int, k_max: int) -> None:
    if k_min < 1:
        raise ValueError("k_min must be at least 1 (degree zero is degenerate).")
    if k_max <= k_min:
        raise ValueError("k_max must exceed k_min.")


def poisson_degree_distribution(
    mean_degree: float,
    k_min: int = 1,
    k_max: int = 30,
) -> DegreeDistribution:
    """Return the Poisson degree distribution P(k) = e^{-lambda} lambda^k / k!.

    The Erdos-Renyi G(n, p) graph has approximately Poisson-distributed
    degrees with mean ``lambda = mean_degree`` when ``n`` is large.

    Args:
        mean_degree: Expected degree ``lambda`` (must be positive).
        k_min: Smallest degree to tabulate (inclusive).
        k_max: Largest degree to tabulate (inclusive).

    Returns:
        DegreeDistribution with degrees ``k_min..k_max`` and their P(k).

    Raises:
        ValueError: If ``mean_degree`` is non-positive or the range is invalid.
    """
    if mean_degree <= 0:
        raise ValueError("mean_degree must be positive.")
    _validate(k_min, k_max)

    degrees = tuple(range(k_min, k_max + 1))
    log_lambda = math.log(mean_degree)
    # Compute in log-space to avoid overflow at large k:
    # log P(k) = -lambda + k * log(lambda) - log(k!)
    probs = tuple(
        math.exp(-mean_degree + k * log_lambda - math.lgamma(k + 1)) for k in degrees
    )
    logger.debug(
        "Poisson degree distribution: mean=%.2f, k=%d..%d", mean_degree, k_min, k_max
    )
    return DegreeDistribution(
        name="random_network",
        degrees=degrees,
        probabilities=probs,
        mean_degree=mean_degree,
        model="erdos_renyi_poisson",
    )


def powerlaw_degree_distribution(
    gamma: float = 2.5,
    k_min: int = 1,
    k_max: int = 200,
) -> DegreeDistribution:
    """Return the discrete power-law degree distribution P(k) ~ k^{-gamma}.

    Probabilities are normalized over ``k_min..k_max`` so the tabulated
    distribution sums to 1 exactly within float precision.

    Args:
        gamma: Power-law exponent. Empirical biological networks typically
            sit in 2.0 < gamma < 3.5.
        k_min: Smallest degree to tabulate (inclusive, defaults to 1).
        k_max: Largest degree to tabulate (inclusive, defaults to 200).

    Returns:
        DegreeDistribution with the normalized power-law P(k) and the mean
        degree implied by the truncation.

    Raises:
        ValueError: If ``gamma`` is non-positive or the range is invalid.
    """
    if gamma <= 0:
        raise ValueError("gamma must be positive.")
    _validate(k_min, k_max)

    degrees = tuple(range(k_min, k_max + 1))
    raw = tuple(float(k) ** (-gamma) for k in degrees)
    total = sum(raw)
    if total <= 0:
        raise ValueError("power-law normalization yielded non-positive total.")
    probs = tuple(value / total for value in raw)
    mean = sum(k * p for k, p in zip(degrees, probs))
    logger.debug(
        "Power-law degree distribution: gamma=%.2f, mean=%.2f, k=%d..%d",
        gamma,
        mean,
        k_min,
        k_max,
    )
    return DegreeDistribution(
        name="scale_free_network",
        degrees=degrees,
        probabilities=probs,
        mean_degree=mean,
        model="barabasi_albert_powerlaw",
    )


def scale_free_vs_random(
    mean_degree: float = 4.0,
    gamma: float = 2.5,
    k_min: int = 1,
    k_max: int = 200,
) -> tuple[DegreeDistribution, DegreeDistribution]:
    """Return a (random, scale-free) pair on a common degree axis.

    Args:
        mean_degree: Poisson mean for the random network.
        gamma: Power-law exponent for the scale-free network.
        k_min: Smallest degree to tabulate (inclusive).
        k_max: Largest degree to tabulate (inclusive).

    Returns:
        ``(poisson, powerlaw)`` distributions sharing the same degree axis.

    Raises:
        ValueError: If any input is out of range (delegated to the per-model
            helpers above).
    """
    return (
        poisson_degree_distribution(mean_degree, k_min=k_min, k_max=k_max),
        powerlaw_degree_distribution(gamma, k_min=k_min, k_max=k_max),
    )
