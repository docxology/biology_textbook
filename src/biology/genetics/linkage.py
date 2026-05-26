"""Linkage mapping from recombination fractions."""

from __future__ import annotations

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
    """Return map distance in centimorgans from recombinant progeny counts."""
    return 100.0 * recombination_frequency(recombinant_offspring, total_offspring)


def infer_three_point_order(distances_cM: dict[tuple[str, str], float]) -> LinkageMapResult:
    """Infer gene order from three pairwise map distances."""
    if len(distances_cM) != 3:
        raise ValueError("Exactly three pairwise distances are required.")

    normalized: dict[frozenset[str], float] = {}
    genes: set[str] = set()
    for pair, distance in distances_cM.items():
        if len(pair) != 2 or pair[0] == pair[1]:
            raise ValueError(f"Invalid gene pair: {pair!r}")
        if distance < 0:
            raise ValueError("Distances must be non-negative.")
        pair_key = frozenset(pair)
        if pair_key in normalized:
            raise ValueError(f"Duplicate unordered gene pair: {pair!r}")
        normalized[pair_key] = float(distance)
        genes.update(pair)

    if len(genes) != 3:
        raise ValueError("Distances must describe exactly three distinct genes.")

    max_pair, span = max(normalized.items(), key=lambda item: item[1])
    outside = tuple(sorted(max_pair))
    middle_candidates = genes - set(outside)
    if len(middle_candidates) != 1:
        raise ValueError("Could not identify a unique middle gene.")
    middle = next(iter(middle_candidates))
    left, right = outside

    left_distance = normalized[frozenset((left, middle))]
    right_distance = normalized[frozenset((middle, right))]
    return LinkageMapResult(
        order=(left, middle, right),
        adjacent_distances_cM=(left_distance, right_distance),
        span_cM=span,
    )
