"""Tests for ``biology.genetics.sequence``."""

import pytest

from biology.genetics import (
    GENETIC_CODE,
    dna_complement,
    gc_content,
    transcribe_dna_to_mrna,
    translate_mrna,
)


class TestDNAManipulation:
    def test_complement_AT(self):
        assert dna_complement("AT") == "AT"

    def test_complement_reversal(self):
        assert dna_complement("ATGC") == "GCAT"

    def test_complement_invalid_raises(self):
        with pytest.raises(ValueError, match="Invalid DNA"):
            dna_complement("ATXG")

    def test_complement_all_bases(self):
        assert dna_complement("AATTGGCC") == "GGCCAATT"

    def test_transcription_template(self):
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
        assert aa == ["Met", "Phe"]

    def test_translate_invalid_nucleotide_raises(self):
        with pytest.raises(ValueError):
            translate_mrna("AAAXUUU")

    def test_genetic_code_has_all_64_codons(self):
        assert len(GENETIC_CODE) == 64

    def test_stop_codons_present(self):
        stops = [codon for codon, aa in GENETIC_CODE.items() if aa == "Stop"]
        assert set(stops) == {"UAA", "UAG", "UGA"}
