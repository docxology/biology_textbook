"""Mutation evidence with explicit, non-interchangeable measurement bases.

These historical estimates are not a ranked spectrum or a genomic burden
calculation. Target definitions, ascertainment and time bases differ.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MutationRateEvidence:
    """A source-scoped estimate, or an explicitly unquantified variant class.

    ``rate_range`` is an approximate interval (equal endpoints for a point
    estimate), in events per ``target`` per ``time_basis``. It is not a
    confidence interval unless the ascertainment field explicitly says so.
    None means no verified numeric estimate is provided, never a zero rate.
    """

    mutation_class: str
    rate_range: tuple[float, float] | None
    target: str
    time_basis: str
    organism: str
    source_url: str | None
    source_label: str
    ascertainment: str


MUTATION_RATE_EVIDENCE: tuple[MutationRateEvidence, ...] = (
    MutationRateEvidence(
        "Single-nucleotide substitution", (1.1e-8, 1.1e-8),
        "position per haploid genome", "generation", "human germline",
        "https://pubmed.ncbi.nlm.nih.gov/20220176/", "Roach et al. (2010)",
        "Direct intergeneration estimate from one family quartet; approximate, not a universal constant.",
    ),
    MutationRateEvidence(
        "Microsatellite slippage", (2.73e-4, 2.73e-4),
        "dinucleotide microsatellite locus", "generation", "human germline (Iceland)",
        "https://doi.org/10.1038/ng.2398", "Sun et al. (2012), Table 1",
        "Combined direct dinucleotide estimate at highly polymorphic linkage markers; unadjusted rate. "
        "Tetranucleotide estimate is 10.01e-4; this row is not all microsatellites.",
    ),
    MutationRateEvidence(
        "Copy-number variant >500 bp", (3e-2, 3e-2),
        "haploid genome", "generation", "human",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC3330748/", "Conrad et al. (2010)",
        "Population Watterson-estimator inference after ascertainment correction; excludes purifying "
        "selection and is likely a lower bound, not a direct pedigree measurement or all structural variants.",
    ),
    MutationRateEvidence(
        "Whole-gene duplication", (0.01, 0.01),
        "gene", "million years", "several eukaryotic species",
        "https://pubmed.ncbi.nlm.nih.gov/11073452/", "Lynch & Conery (2000)",
        "Average inferred from genomic databases; evolutionary-time estimate, not a human germline rate.",
    ),
    MutationRateEvidence(
        "Small insertion or deletion", None, "not specified", "not specified", "not specified",
        None, "No verified numeric estimate supplied",
        "The previous per-base constant lacked verified primary support; no quantitative comparison is made.",
    ),
    MutationRateEvidence(
        "CpG transition", None, "CpG context (not all bases)", "not specified", "not specified",
        None, "No verified numeric estimate supplied",
        "Context-specific substitution subclass, overlapping the substitution category; "
        "the previous constant lacked verified primary support.",
    ),
)


def mutation_rate_spectrum() -> tuple[MutationRateEvidence, ...]:
    """Return the unsorted evidence catalog, without unit conversion or ranking.

    Rate comparisons require the same target, time basis and ascertainment.
    Burden additionally needs eligible target sizes and non-overlapping classes;
    neither is supplied here. A per-locus or per-gene rate is not per-base.
    """
    return MUTATION_RATE_EVIDENCE
