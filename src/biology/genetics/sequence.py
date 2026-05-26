"""DNA/RNA sequence utilities and the standard genetic code."""

from __future__ import annotations

from textbook_logging import get_logger


logger = get_logger(__name__)

Allele = str  # Single nucleotide/base letter (e.g. 'A', 'a')
Genotype = str  # Two-character genotype string (e.g. 'Aa', 'AA')

GENETIC_CODE: dict[str, str] = {
    "UUU": "Phe",
    "UUC": "Phe",
    "UUA": "Leu",
    "UUG": "Leu",
    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",
    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",
    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",
    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",
    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",
    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",
    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",
    "UAU": "Tyr",
    "UAC": "Tyr",
    "UAA": "Stop",
    "UAG": "Stop",
    "CAU": "His",
    "CAC": "His",
    "CAA": "Gln",
    "CAG": "Gln",
    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",
    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",
    "UGU": "Cys",
    "UGC": "Cys",
    "UGA": "Stop",
    "UGG": "Trp",
    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",
    "AGU": "Ser",
    "AGC": "Ser",
    "AGA": "Arg",
    "AGG": "Arg",
    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly",
}

DNA_COMPLEMENT: dict[str, str] = {"A": "T", "T": "A", "G": "C", "C": "G"}
RNA_COMPLEMENT: dict[str, str] = {"A": "U", "T": "A", "G": "C", "C": "G"}


def dna_complement(sequence: str) -> str:
    """Return the complementary DNA strand (3'→5' to 5'→3')."""
    seq = sequence.upper()
    invalid = set(seq) - set(DNA_COMPLEMENT)
    if invalid:
        raise ValueError(f"Invalid DNA nucleotides: {invalid}")
    return "".join(DNA_COMPLEMENT[n] for n in reversed(seq))


def transcribe_dna_to_mrna(dna_template: str) -> str:
    """Transcribe a DNA template strand to mRNA (5'→3')."""
    seq = dna_template.upper()
    invalid = set(seq) - set(RNA_COMPLEMENT)
    if invalid:
        raise ValueError(f"Invalid DNA nucleotides: {invalid}")
    mrna = "".join(RNA_COMPLEMENT[n] for n in seq)
    logger.debug("Transcribed %r → mRNA %r", dna_template, mrna)
    return mrna


def translate_mrna(mrna: str) -> list[str]:
    """Translate an mRNA sequence into amino acids from the first AUG."""
    seq = mrna.upper()
    invalid = set(seq) - {"A", "U", "G", "C"}
    if invalid:
        raise ValueError(f"Invalid RNA nucleotides: {invalid}")

    start = seq.find("AUG")
    if start == -1:
        logger.warning("No AUG start codon found.")
        return []

    protein = []
    for i in range(start, len(seq) - 2, 3):
        codon = seq[i : i + 3]
        if len(codon) < 3:
            break
        aa = GENETIC_CODE.get(codon, "?")
        if aa == "Stop":
            break
        protein.append(aa)

    logger.debug("Translated %d amino acids.", len(protein))
    return protein


def gc_content(sequence: str) -> float:
    """Calculate GC content of a DNA/RNA sequence as a fraction [0, 1]."""
    if not sequence:
        raise ValueError("Sequence must not be empty.")
    seq = sequence.upper()
    gc = sum(1 for n in seq if n in ("G", "C"))
    return gc / len(seq)
