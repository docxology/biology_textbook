"""Epigenetic teaching helpers: methylation decay and histone marks."""

from __future__ import annotations


def cpg_methylation_remaining(
    initial_methylation: float,
    divisions: int,
    maintenance_efficiency: float,
) -> float:
    """Return CpG methylation remaining after ``divisions`` cell cycles."""
    if divisions < 0:
        raise ValueError("Number of divisions cannot be negative.")
    return initial_methylation * (maintenance_efficiency**divisions)


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
