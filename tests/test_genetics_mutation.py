"""Tests for ``biology.genetics.mutation``."""

from biology.genetics import mutation_rate_spectrum


class TestMutationRateSpectrum:
    def test_mutation_rate_spectrum_has_positive_rates(self):
        rows = list(mutation_rate_spectrum())
        assert rows
        for row in rows:
            assert row.rate_per_site_per_generation > 0

    def test_mutation_rate_spectrum_includes_canonical_classes(self):
        names = {row.mutation_class.lower() for row in mutation_rate_spectrum()}
        assert any("substitution" in name for name in names)
        assert any("microsatellite" in name for name in names)
