"""Backward-compatible re-export shim for ``biology.genetics.genetics`` imports."""

from __future__ import annotations

from .distance import hamming_distance, jukes_cantor_distance
from .epigenetics import (
    cpg_methylation_remaining,
    histone_modification_state,
    synthetic_methylation_beta_matrix,
)
from .linkage import (
    LinkageMapResult,
    genetic_distance,
    infer_three_point_order,
    recombination_frequency,
)
from .mendelian import DiploidGenotype, PunnettSquareResult, gametes, punnett_square
from .mutation import MUTATION_RATE_SPECTRUM, MutationClassRate, mutation_rate_spectrum
from .population import ChiSquaredResult, HardyWeinbergResult, chi_squared_test, hardy_weinberg
from .replication import ReplicationForkProfile, replication_fork_progression
from .sequence import (
    DNA_COMPLEMENT,
    GENETIC_CODE,
    RNA_COMPLEMENT,
    Allele,
    Genotype,
    dna_complement,
    gc_content,
    transcribe_dna_to_mrna,
    translate_mrna,
)

__all__ = [
    "Allele",
    "ChiSquaredResult",
    "DNA_COMPLEMENT",
    "DiploidGenotype",
    "GENETIC_CODE",
    "Genotype",
    "HardyWeinbergResult",
    "LinkageMapResult",
    "MUTATION_RATE_SPECTRUM",
    "MutationClassRate",
    "PunnettSquareResult",
    "RNA_COMPLEMENT",
    "ReplicationForkProfile",
    "chi_squared_test",
    "cpg_methylation_remaining",
    "dna_complement",
    "gametes",
    "gc_content",
    "genetic_distance",
    "hamming_distance",
    "hardy_weinberg",
    "histone_modification_state",
    "infer_three_point_order",
    "jukes_cantor_distance",
    "mutation_rate_spectrum",
    "punnett_square",
    "recombination_frequency",
    "replication_fork_progression",
    "synthetic_methylation_beta_matrix",
    "transcribe_dna_to_mrna",
    "translate_mrna",
]
