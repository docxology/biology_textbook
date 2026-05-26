"""Tests for ``biology.genetics.distance``."""

import pytest

from biology.genetics import hamming_distance, jukes_cantor_distance


class TestSequenceDistance:
    def test_hamming_identical(self):
        assert hamming_distance("ATGC", "ATGC") == 0

    def test_hamming_completely_different(self):
        assert hamming_distance("AAAA", "TTTT") == 4

    def test_hamming_length_mismatch_raises(self):
        with pytest.raises(ValueError):
            hamming_distance("ATG", "ATGC")

    def test_jukes_cantor_zero_distance(self):
        assert jukes_cantor_distance(0.0) == 0.0

    def test_jukes_cantor_increases_with_p(self):
        d1 = jukes_cantor_distance(0.1)
        d2 = jukes_cantor_distance(0.3)
        assert d2 > d1

    def test_jukes_cantor_saturated_raises(self):
        with pytest.raises(ValueError):
            jukes_cantor_distance(0.75)

    def test_jukes_cantor_greater_than_p(self):
        p = 0.2
        d = jukes_cantor_distance(p)
        assert d > p
