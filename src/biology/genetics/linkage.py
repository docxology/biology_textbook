"""Linkage mapping from recombination fractions."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class LinkageMapResult:
    """Three-point linkage-map inference from pairwise map distances."""

    order: tuple[str, str, str]
    adjacent_distances_cM: tuple[float, float]
    span_cM: float


def recombination_frequency(recombinant_offspring: int, total_offspring: int) -> float:
    """Return the observed recombination fraction for a linkage cross."""
    if total_offspring <= 0:
        raise ValueError("total_offspring must be positive.")
    if recombinant_offspring < 0:
        raise ValueError("recombinant_offspring must be non-negative.")
    if recombinant_offspring > total_offspring:
        raise ValueError("recombinant_offspring cannot exceed total_offspring.")
    return recombinant_offspring / total_offspring


def genetic_distance(recombinant_offspring: int, total_offspring: int) -> float:
    """Short-interval approximation ``100*r`` cM, not a general mapping function."""
    return 100.0 * recombination_frequency(recombinant_offspring, total_offspring)


def infer_three_point_order(distances_cM: dict[tuple[str, str], float]) -> LinkageMapResult:
    """Infer an exact additive map (rel_tol=1e-9, abs_tol=1e-9 cM).

    Reversal is arbitrary. Co-located markers admit multiple equivalent
    orders; the lexicographically first orientation is returned. No noisy
    recombination-distance fit or uncertainty estimate is performed.
    """
    if len(distances_cM) != 3:
        raise ValueError("Exactly three pairwise distances are required.")

    normalized: dict[frozenset[str], float] = {}
    genes: set[str] = set()
    for pair, distance in distances_cM.items():
        if len(pair) != 2 or pair[0] == pair[1]:
            raise ValueError(f"Invalid gene pair: {pair!r}")
        if not math.isfinite(distance) or distance < 0:
            raise ValueError("Distances must be finite and non-negative.")
        pair_key = frozenset(pair)
        if pair_key in normalized:
            raise ValueError(f"Duplicate unordered gene pair: {pair!r}")
        normalized[pair_key] = float(distance)
        genes.update(pair)

    if len(genes) != 3:
        raise ValueError("Distances must describe exactly three distinct genes.")

    # Enumerate exact orders, including legitimate co-located-marker ties.
    from itertools import permutations

    for left, middle, right in permutations(sorted(genes)):
        left_distance = normalized[frozenset((left, middle))]
        right_distance = normalized[frozenset((middle, right))]
        span = normalized[frozenset((left, right))]
        if math.isclose(left_distance + right_distance, span, rel_tol=1e-9, abs_tol=1e-9):
            return LinkageMapResult(
                order=(left, middle, right),
                adjacent_distances_cM=(left_distance, right_distance),
                span_cM=span,
            )
    raise ValueError("Pairwise distances do not define an additive three-point map.")
