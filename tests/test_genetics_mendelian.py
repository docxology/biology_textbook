"""Tests for ``biology.genetics.mendelian``."""

import pytest

from biology.genetics import DiploidGenotype, gametes, punnett_square


class TestPunnettSquare:
    def test_monohybrid_Aa_x_Aa_genotype_ratios(self):
        result = punnett_square("Aa", "Aa")
        assert abs(result.genotype_ratios["AA"] - 0.25) < 0.01
        assert abs(result.genotype_ratios["aa"] - 0.25) < 0.01

    def test_monohybrid_dominant_phenotype_ratio(self):
        result = punnett_square("Aa", "Aa")
        assert abs(result.phenotype_ratios["dominant"] - 0.75) < 0.01
        assert abs(result.phenotype_ratios["recessive"] - 0.25) < 0.01

    def test_homozygous_dominant_cross(self):
        result = punnett_square("AA", "aa")
        assert result.phenotype_ratios["dominant"] == 1.0

    def test_homozygous_recessive_cross(self):
        result = punnett_square("aa", "aa")
        assert result.phenotype_ratios["recessive"] == 1.0

    def test_invalid_genotype_raises(self):
        with pytest.raises(ValueError):
            punnett_square("AAA", "Aa")

    def test_gametes_alias_matches_internal(self):
        assert gametes("Aa") == ["A", "a"]

    def test_diploid_genotype_properties(self):
        genotype = DiploidGenotype("A", "a")
        assert not genotype.is_homozygous
        assert genotype.is_dominant_phenotype
        assert repr(genotype) == "Aa"
