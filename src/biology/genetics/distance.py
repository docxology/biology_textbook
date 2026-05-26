"""Sequence divergence metrics."""

from __future__ import annotations

import math


def hamming_distance(seq1: str, seq2: str) -> int:
    """Compute the Hamming distance between two equal-length sequences."""
    if len(seq1) != len(seq2):
        raise ValueError(f"Sequences must be equal length: {len(seq1)} vs {len(seq2)}")
    return sum(a != b for a, b in zip(seq1.upper(), seq2.upper()))


def jukes_cantor_distance(p_distance: float) -> float:
    """Compute the Jukes-Cantor corrected nucleotide distance."""
    if not (0.0 <= p_distance < 0.75):
        raise ValueError(f"p_distance must be in [0, 0.75), got {p_distance}")
    if p_distance == 0.0:
        return 0.0
    return -(3.0 / 4.0) * math.log(1.0 - (4.0 / 3.0) * p_distance)
