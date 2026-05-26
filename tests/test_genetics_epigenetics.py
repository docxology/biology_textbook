"""Tests for ``biology.genetics.epigenetics``."""

import pytest

from biology.genetics import (
    cpg_methylation_remaining,
    histone_modification_state,
    synthetic_methylation_beta_matrix,
)


class TestEpigeneticUtilities:
    def test_cpg_methylation_decay(self):
        assert cpg_methylation_remaining(0.8, divisions=2, maintenance_efficiency=0.9) == pytest.approx(0.648)

    def test_histone_mark_lookup(self):
        assert histone_modification_state("H3K27me3") == "repressed"
        assert histone_modification_state("H3K27ac") == "active"
        assert histone_modification_state("H3K4me2") == "context-dependent"

    def test_synthetic_methylation_beta_matrix_shape(self):
        matrix = synthetic_methylation_beta_matrix(n_loci=12, n_samples=4, rng_seed=7)
        assert matrix.shape == (12, 4)
        assert float(matrix.min()) >= 0.0
        assert float(matrix.max()) <= 1.0
