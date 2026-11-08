"""Epigenetic teaching helpers: methylation decay and histone marks."""

from __future__ import annotations

import math


def cpg_methylation_remaining(
    initial_methylation: float,
    divisions: int,
    maintenance_efficiency: float,
) -> float:
    """Fraction of methylated cytosines after semiconservative replication.

    Each old methylated cytosine is retained and its new partner is methylated
    with the given efficiency. No de-novo methylation or active removal:
    f[n+1] = f[n] * (1 + efficiency) / 2.
    """
    if isinstance(divisions, bool) or not isinstance(divisions, int):
        raise TypeError("divisions must be a non-negative integer.")
    if divisions < 0:
        raise ValueError("divisions must be a non-negative integer.")
    if not math.isfinite(initial_methylation) or not 0 <= initial_methylation <= 1:
        raise ValueError("initial_methylation must be finite and in [0, 1].")
    if not math.isfinite(maintenance_efficiency) or not 0 <= maintenance_efficiency <= 1:
        raise ValueError("maintenance_efficiency must be finite and in [0, 1].")
    return initial_methylation * ((1.0 + maintenance_efficiency) / 2.0) ** divisions


def histone_modification_state(mark: str) -> str:
    """Return the transcriptional state associated with a histone mark."""
    repressive_marks = {"H3K9me3", "H3K27me3", "H4K20me3", "H3K9me2"}
    activating_marks = {
        "H3K4me3",
        "H3K36me3",
        "H3K79me2",
        "H3K27ac",
        "H3K9ac",
        "H4K16ac",
        "H3K4me1",
    }

    mark_upper = mark.upper()

    if mark_upper in (m.upper() for m in repressive_marks):
        return "repressed"
    if mark_upper in (m.upper() for m in activating_marks):
        return "active"
    return "context-dependent"


def synthetic_methylation_beta_matrix(
    n_loci: int = 24,
    n_samples: int = 8,
    rng_seed: int = 42,
):
    """Return a deterministic synthetic CpG methylation β matrix for teaching plots."""
    import numpy as np

    rng = np.random.default_rng(rng_seed)
    base = rng.uniform(0.15, 0.85, size=(n_loci, n_samples))
    if n_loci > 14:
        base[8:15, :] *= 0.4
    return np.clip(base, 0.0, 1.0)
