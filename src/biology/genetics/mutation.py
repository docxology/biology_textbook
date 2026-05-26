"""Mutation rate spectrum reference data."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MutationClassRate:
    """Per-base, per-generation mutation rate for one class of variant."""

    mutation_class: str
    rate_per_site_per_generation: float
    organism: str
    notes: str


MUTATION_RATE_SPECTRUM: tuple[MutationClassRate, ...] = (
    MutationClassRate("Single-nucleotide substitution", 1.2e-8, "human germline", "Roach et al. 2010"),
    MutationClassRate("Small insertion or deletion", 1.5e-9, "human germline", "Kondrashov 2003"),
    MutationClassRate("CpG transition", 1.0e-7, "human germline", "Hodgkinson & Eyre-Walker 2011"),
    MutationClassRate("Microsatellite slippage", 1.0e-4, "human germline", "Sun et al. 2012"),
    MutationClassRate("Large structural variant", 1.6e-5, "human germline", "Conrad et al. 2010"),
    MutationClassRate("Whole-gene duplication", 1.0e-5, "human germline", "Lynch & Conery 2000"),
)


def mutation_rate_spectrum() -> tuple[MutationClassRate, ...]:
    """Return the canonical mutation-rate spectrum sorted rarest to most common."""
    return tuple(
        sorted(MUTATION_RATE_SPECTRUM, key=lambda row: row.rate_per_site_per_generation)
    )
