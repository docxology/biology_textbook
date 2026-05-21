"""Tests for genetics module — Units IV and V."""

import pytest

from biology.genetics import (
    dna_complement, transcribe_dna_to_mrna, translate_mrna, gc_content,
    punnett_square, hardy_weinberg, chi_squared_test,
    hamming_distance, recombination_frequency, genetic_distance, infer_three_point_order,
    jukes_cantor_distance, cpg_methylation_remaining, histone_modification_state,
    GENETIC_CODE,
)


class TestDNAManipulation:
    def test_complement_AT(self):
        assert dna_complement("AT") == "AT"

    def test_complement_reversal(self):
        # complement of 5'-ATGC-3' template is anti-parallel 3'→5 complement
        assert dna_complement("ATGC") == "GCAT"

    def test_complement_invalid_raises(self):
        with pytest.raises(ValueError, match="Invalid DNA"):
            dna_complement("ATXG")

    def test_complement_all_bases(self):
        assert dna_complement("AATTGGCC") == "GGCCAATT"

    def test_transcription_template(self):
        # Template 3'-TAC-5' → mRNA 5'-AUG-3'
        mrna = transcribe_dna_to_mrna("TAC")
        assert mrna == "AUG"

    def test_transcription_invalid_raises(self):
        with pytest.raises(ValueError):
            transcribe_dna_to_mrna("TAXG")

    def test_gc_content_all_gc(self):
        assert gc_content("GCGC") == 1.0

    def test_gc_content_all_at(self):
        assert gc_content("ATAT") == 0.0

    def test_gc_content_mixed(self):
        assert abs(gc_content("ATGC") - 0.5) < 1e-9

    def test_gc_content_empty_raises(self):
        with pytest.raises(ValueError):
            gc_content("")


class TestTranslation:
    def test_translate_met_start(self):
        aa = translate_mrna("AUGUUU")
        assert aa == ["Met", "Phe"]

    def test_translate_no_start_returns_empty(self):
        aa = translate_mrna("UUUUUU")
        assert aa == []

    def test_translate_stop_codon(self):
        aa = translate_mrna("AUGUUUUAA")
        assert aa == ["Met", "Phe"]  # stops at UAA

    def test_translate_invalid_nucleotide_raises(self):
        with pytest.raises(ValueError):
            translate_mrna("AAAXUUU")

    def test_genetic_code_has_all_64_codons(self):
        assert len(GENETIC_CODE) == 64

    def test_stop_codons_present(self):
        stops = [codon for codon, aa in GENETIC_CODE.items() if aa == "Stop"]
        assert set(stops) == {"UAA", "UAG", "UGA"}


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
            punnett_square("AAA", "Aa")  # too long


class TestHardyWeinberg:
    def test_hw_from_p_q(self):
        result = hardy_weinberg(p=0.6, q=0.4)
        assert abs(result.p_squared - 0.36) < 1e-9
        assert abs(result.two_pq - 0.48) < 1e-9
        assert abs(result.q_squared - 0.16) < 1e-9
        assert result.is_valid

    def test_hw_from_recessive_freq(self):
        result = hardy_weinberg(recessive_homozygous_freq=0.09)
        assert abs(result.q - 0.3) < 1e-9
        assert abs(result.p - 0.7) < 1e-9

    def test_hw_genotype_freqs_sum_to_one(self):
        result = hardy_weinberg(p=0.3, q=0.7)
        total = result.p_squared + result.two_pq + result.q_squared
        assert abs(total - 1.0) < 1e-9

    def test_hw_invalid_p_raises(self):
        with pytest.raises(ValueError):
            hardy_weinberg(p=1.5, q=0.7)

    def test_hw_no_args_raises(self):
        with pytest.raises(ValueError):
            hardy_weinberg()


class TestChiSquared:
    def test_3_to_1_expected(self):
        """Classic Mendelian 3:1 ratio should not be rejected with chi2 ≈ 0."""
        observed = [75.0, 25.0]  # perfect 3:1 from 100 offspring
        expected = [75.0, 25.0]
        result = chi_squared_test(observed, expected)
        assert result.chi_squared == pytest.approx(0.0, abs=1e-9)
        assert not result.reject_null

    def test_chi2_deviation_detected(self):
        """Severely skewed counts should yield large chi-squared."""
        observed = [90.0, 10.0]
        expected = [75.0, 25.0]
        result = chi_squared_test(observed, expected)
        assert result.chi_squared > 5.0  # clearly non-Mendelian

    def test_df1_p_value_matches_critical_threshold(self):
        result = chi_squared_test([113.86, 86.14], [100.0, 100.0])
        assert result.chi_squared == pytest.approx(3.841, rel=1e-3)
        assert result.p_value_approx == pytest.approx(0.05, rel=1e-2)
        strong = chi_squared_test([138.591, 61.409], [100.0, 100.0])
        assert strong.chi_squared == pytest.approx(29.7853, rel=1e-4)
        assert strong.p_value_approx < 0.001

    def test_chi2_length_mismatch_raises(self):
        with pytest.raises(ValueError, match="equal length"):
            chi_squared_test([10, 20], [10, 20, 30])

    def test_chi2_zero_expected_raises(self):
        with pytest.raises(ValueError, match="positive"):
            chi_squared_test([10.0, 0.0], [10.0, 0.0])


class TestGeneticDistance:
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
        assert d > p   # JC correction always increases the estimate

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


class TestEpigeneticUtilities:
    def test_cpg_methylation_decay(self):
        assert cpg_methylation_remaining(0.8, divisions=2, maintenance_efficiency=0.9) == pytest.approx(0.648)

    def test_histone_mark_lookup(self):
        assert histone_modification_state("H3K27me3") == "repressed"
        assert histone_modification_state("H3K27ac") == "active"
        assert histone_modification_state("H3K4me2") == "context-dependent"
