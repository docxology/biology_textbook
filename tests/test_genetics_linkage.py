"""Tests for ``biology.genetics.linkage``."""

import pytest

from biology.genetics import genetic_distance, infer_three_point_order, recombination_frequency


class TestLinkageMapping:
    def test_recombination_frequency_from_counts(self):
        assert recombination_frequency(24, 200) == pytest.approx(0.12)
        assert genetic_distance(24, 200) == pytest.approx(12.0)

    def test_recombination_frequency_invalid_counts_raise(self):
        with pytest.raises(ValueError, match="cannot exceed"):
            recombination_frequency(11, 10)
        with pytest.raises(ValueError, match="positive"):
            genetic_distance(0, 0)

    def test_infer_three_point_order_from_pairwise_distances(self):
        result = infer_three_point_order({("A", "B"): 12.0, ("B", "C"): 8.0, ("A", "C"): 20.0})
        assert result.order == ("A", "B", "C")
        assert result.adjacent_distances_cM == (12.0, 8.0)
        assert result.span_cM == 20.0

    def test_infer_three_point_order_requires_three_genes(self):
        with pytest.raises(ValueError, match="three distinct genes"):
            infer_three_point_order({("A", "B"): 1.0, ("A", "C"): 2.0, ("A", "D"): 3.0})
