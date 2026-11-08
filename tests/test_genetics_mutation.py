"""Tests for ``biology.genetics.mutation``."""

from biology.genetics import mutation_rate_spectrum


class TestMutationRateSpectrum:
    def test_numeric_evidence_has_explicit_measurement_basis(self):
        rows = mutation_rate_spectrum()
        assert rows
        for row in rows:
            if row.rate_range is not None:
                low, high = row.rate_range
                assert 0 < low <= high
                assert row.target and row.time_basis and row.organism
                assert row.source_url and row.ascertainment
            else:
                assert row.source_url is None
        assert sum(row.rate_range is None for row in rows) == 2

    def test_mutation_rate_spectrum_includes_canonical_classes(self):
        names = {row.mutation_class.lower() for row in mutation_rate_spectrum()}
        assert any("substitution" in name for name in names)
        assert any("microsatellite" in name for name in names)
