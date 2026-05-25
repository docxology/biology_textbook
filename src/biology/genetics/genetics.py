# ---------------------------------------------------------------------------
# Biology — Genetics Module
# ---------------------------------------------------------------------------

"""Core genetics utilities: genotypes, Punnett squares, Hardy-Weinberg, chi-squared."""

import math
import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


# Type aliases for legacy compatibility
Allele = str  # Single nucleotide/base letter (e.g. 'A', 'a')
Genotype = str  # Two-character genotype string (e.g. 'Aa', 'AA')


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------


@dataclass
class DiploidGenotype:
    """Diploid genotype of two alleles."""

    allele1: str
    allele2: str

    @property
    def is_homozygous(self) -> bool:
        """True if both alleles are identical (e.g. ``AA`` or ``aa``)."""
        return self.allele1 == self.allele2

    @property
    def is_dominant_phenotype(self) -> bool:
        """True if at least one allele is uppercase (dominant)."""
        return self.allele1.isupper() or self.allele2.isupper()

    def __repr__(self) -> str:
        """Return compact genotype representation."""
        return f"{self.allele1}{self.allele2}"


@dataclass
class PunnettSquareResult:
    """Output of a Punnett square calculation."""

    parent1: str
    parent2: str
    offspring_genotypes: list[str]
    genotype_ratios: dict[str, float]
    phenotype_ratios: dict[str, float]


@dataclass
class HardyWeinbergResult:
    """Hardy-Weinberg equilibrium calculations."""

    p: float  # frequency of dominant allele
    q: float  # frequency of recessive allele
    p_squared: float  # AA frequency
    two_pq: float  # Aa frequency
    q_squared: float  # aa frequency
    is_valid: bool


@dataclass
class ChiSquaredResult:
    """Chi-squared goodness-of-fit test result."""

    chi_squared: float
    degrees_of_freedom: int
    p_value_approx: float  # approximate using chi2 CDF
    observed: list[float]
    expected: list[float]
    reject_null: bool  # at α=0.05


@dataclass(frozen=True)
class LinkageMapResult:
    """Three-point linkage-map inference from pairwise map distances."""

    order: tuple[str, str, str]
    adjacent_distances_cM: tuple[float, float]
    span_cM: float


# ---------------------------------------------------------------------------
# Codons & Genetic Code
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# DNA / RNA Utilities
# ---------------------------------------------------------------------------


def dna_complement(sequence: str) -> str:
    """Return the complementary DNA strand (3'→5' to 5'→3').

    Args:
        sequence: DNA sequence string (A, T, G, C). Case-insensitive.

    Returns:
        Complementary strand in 5'→3' direction.

    Raises:
        ValueError: If sequence contains invalid nucleotides.
    """
    seq = sequence.upper()
    invalid = set(seq) - set(DNA_COMPLEMENT)
    if invalid:
        raise ValueError(f"Invalid DNA nucleotides: {invalid}")
    return "".join(DNA_COMPLEMENT[n] for n in reversed(seq))


def transcribe_dna_to_mrna(dna_template: str) -> str:
    """Transcribe a DNA template strand to mRNA (5'→3').

    Args:
        dna_template: DNA template strand (3'→5'). Case-insensitive.

    Returns:
        mRNA sequence (5'→3').

    Raises:
        ValueError: If sequence contains invalid nucleotides.
    """
    seq = dna_template.upper()
    invalid = set(seq) - set(RNA_COMPLEMENT)
    if invalid:
        raise ValueError(f"Invalid DNA nucleotides: {invalid}")
    mrna = "".join(RNA_COMPLEMENT[n] for n in seq)
    logger.debug(f"Transcribed '{dna_template}' → mRNA '{mrna}'")
    return mrna


def translate_mrna(mrna: str) -> list[str]:
    """Translate an mRNA sequence into amino acids.

    Reads codons from the first AUG; stops at stop codon.

    Args:
        mrna: mRNA sequence. Case-insensitive.

    Returns:
        List of amino acid abbreviations (3-letter codes).

    Raises:
        ValueError: If mRNA contains invalid nucleotides.
    """
    seq = mrna.upper()
    invalid = set(seq) - {"A", "U", "G", "C"}
    if invalid:
        raise ValueError(f"Invalid RNA nucleotides: {invalid}")

    # Find start codon
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

    logger.debug(f"Translated {len(protein)} amino acids.")
    return protein


def gc_content(sequence: str) -> float:
    """Calculate GC content of a DNA/RNA sequence.

    Args:
        sequence: Nucleotide sequence.

    Returns:
        GC content as a fraction [0, 1].

    Raises:
        ValueError: If sequence is empty.
    """
    if not sequence:
        raise ValueError("Sequence must not be empty.")
    seq = sequence.upper()
    gc = sum(1 for n in seq if n in ("G", "C"))
    return gc / len(seq)


# ---------------------------------------------------------------------------
# Mendelian Genetics — Punnett Square
# ---------------------------------------------------------------------------


def _gametes(genotype: str) -> list[str]:
    """Generate gametes from a diploid genotype string (e.g. 'Aa' → ['A','a'])."""
    if len(genotype) != 2:
        raise ValueError(f"Genotype must be 2 characters, got '{genotype}'")
    a1, a2 = genotype[0], genotype[1]
    if a1 == a2:
        return [a1]
    return [a1, a2]


def punnett_square(parent1: str, parent2: str) -> PunnettSquareResult:
    """Perform a monohybrid Punnett square cross.

    Args:
        parent1: Diploid genotype of parent 1 (e.g. 'Aa').
        parent2: Diploid genotype of parent 2 (e.g. 'Aa').

    Returns:
        PunnettSquareResult with offspring genotypes and ratios.

    Raises:
        ValueError: If genotypes are malformed.
    """
    g1 = _gametes(parent1)
    g2 = _gametes(parent2)

    offspring: list[str] = []
    for a in g1:
        for b in g2:
            # Dominant allele first by convention
            if a.isupper() or (not b.isupper()):
                offspring.append(f"{a}{b}")
            else:
                offspring.append(f"{b}{a}")

    # Weight equally if parent is heterozygous
    weights = [1.0 / len(offspring)] * len(offspring)

    counts: dict[str, float] = {}
    for geno, w in zip(offspring, weights):
        counts[geno] = counts.get(geno, 0.0) + w

    # Normalize
    total = sum(counts.values())
    genotype_ratios = {k: v / total for k, v in counts.items()}

    # Phenotype: dominant if at least one uppercase allele
    pheno_dom = sum(v for k, v in genotype_ratios.items() if k[0].isupper() or k[1].isupper())
    pheno_rec = 1.0 - pheno_dom
    phenotype_ratios = {"dominant": pheno_dom, "recessive": pheno_rec}

    logger.debug(f"Punnett {parent1}×{parent2}: genotype_ratios={genotype_ratios}")
    return PunnettSquareResult(
        parent1=parent1,
        parent2=parent2,
        offspring_genotypes=offspring,
        genotype_ratios=genotype_ratios,
        phenotype_ratios=phenotype_ratios,
    )


# ---------------------------------------------------------------------------
# Hardy-Weinberg Equilibrium
# ---------------------------------------------------------------------------


def hardy_weinberg(
    p: Optional[float] = None,
    q: Optional[float] = None,
    dominant_homozygous_freq: Optional[float] = None,
    recessive_homozygous_freq: Optional[float] = None,
) -> HardyWeinbergResult:
    """Compute Hardy-Weinberg equilibrium frequencies.

    Provide either (p, q) or (dominant_homozygous_freq, recessive_homozygous_freq).
    p + q must equal 1.0.

    Args:
        p: Frequency of dominant allele A.
        q: Frequency of recessive allele a.
        dominant_homozygous_freq: Observed AA frequency (alternative input).
        recessive_homozygous_freq: Observed aa frequency (alternative input).

    Returns:
        HardyWeinbergResult with all genotype and allele frequencies.

    Raises:
        ValueError: If insufficient arguments are provided.
    """
    if p is not None and q is not None:
        pass  # use directly
    elif recessive_homozygous_freq is not None:
        q = math.sqrt(recessive_homozygous_freq)
        p = 1.0 - q
    elif dominant_homozygous_freq is not None:
        p = math.sqrt(dominant_homozygous_freq)
        q = 1.0 - p
    else:
        raise ValueError("Provide (p, q) or at least one homozygous frequency.")

    if not (0.0 <= p <= 1.0 and 0.0 <= q <= 1.0):
        raise ValueError(f"p={p} and q={q} must be in [0, 1].")

    is_valid = abs(p + q - 1.0) < 1e-9
    result = HardyWeinbergResult(
        p=p,
        q=q,
        p_squared=p**2,
        two_pq=2 * p * q,
        q_squared=q**2,
        is_valid=is_valid,
    )
    logger.debug(
        "HW: p=%.4f, q=%.4f, AA=%.4f, Aa=%.4f, aa=%.4f",
        p,
        q,
        result.p_squared,
        result.two_pq,
        result.q_squared,
    )
    return result


# ---------------------------------------------------------------------------
# Chi-Squared Test (genetics ratios)
# ---------------------------------------------------------------------------


def chi_squared_test(
    observed: list[float],
    expected: list[float],
    alpha: float = 0.05,
) -> ChiSquaredResult:
    """Perform a chi-squared goodness-of-fit test for Mendelian ratios.

    Args:
        observed: Observed counts per category.
        expected: Expected counts per category.
        alpha: Significance level (default 0.05).

    Returns:
        ChiSquaredResult with chi-squared statistic and approximate p-value.

    Raises:
        ValueError: If lists differ in length or expected contains zeros.
    """
    if len(observed) != len(expected):
        raise ValueError("observed and expected must have equal length.")
    if any(e <= 0 for e in expected):
        raise ValueError("All expected values must be positive.")
    if len(observed) < 2:
        raise ValueError("Need at least 2 categories.")

    chi2 = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    df = len(observed) - 1

    from scipy.stats import chi2 as chi2_dist

    p_value = float(chi2_dist.sf(chi2, df))

    # Standard chi-squared critical values at alpha=0.05
    CRITICAL_VALUES = {1: 3.841, 2: 5.991, 3: 7.815, 4: 9.488, 5: 11.070}
    critical = CRITICAL_VALUES.get(df, df * 2.0)
    reject_null = chi2 > critical

    logger.debug(f"Chi-squared={chi2:.4f}, df={df}, p≈{p_value:.4f}, reject={reject_null}")
    return ChiSquaredResult(
        chi_squared=chi2,
        degrees_of_freedom=df,
        p_value_approx=p_value,
        observed=list(observed),
        expected=list(expected),
        reject_null=reject_null,
    )


# ---------------------------------------------------------------------------
# Genetic Distance
# ---------------------------------------------------------------------------


def hamming_distance(seq1: str, seq2: str) -> int:
    """Compute the Hamming distance between two equal-length sequences.

    Args:
        seq1, seq2: Nucleotide or protein sequences of equal length.

    Returns:
        Number of positions that differ.

    Raises:
        ValueError: If sequences differ in length.
    """
    if len(seq1) != len(seq2):
        raise ValueError(f"Sequences must be equal length: {len(seq1)} vs {len(seq2)}")
    return sum(a != b for a, b in zip(seq1.upper(), seq2.upper()))


def recombination_frequency(recombinant_offspring: int, total_offspring: int) -> float:
    """Return the observed recombination fraction for a linkage cross.

    Args:
        recombinant_offspring: Count of recombinant progeny.
        total_offspring: Total scored progeny.

    Returns:
        Recombination fraction in the interval [0, 1].

    Raises:
        ValueError: If counts are negative, inconsistent, or total is zero.
    """
    if total_offspring <= 0:
        raise ValueError("total_offspring must be positive.")
    if recombinant_offspring < 0:
        raise ValueError("recombinant_offspring must be non-negative.")
    if recombinant_offspring > total_offspring:
        raise ValueError("recombinant_offspring cannot exceed total_offspring.")
    return recombinant_offspring / total_offspring


def genetic_distance(recombinant_offspring: int, total_offspring: int) -> float:
    """Return map distance in centimorgans from recombinant progeny counts.

    The textbook convention is 1 cM = 1 percent recombination. Two-point
    recombination fractions approach 50 percent for unlinked loci; values above
    50 cM should therefore be interpreted as "effectively unlinked" in the
    accompanying lab, not as a literal physical distance.
    """
    return 100.0 * recombination_frequency(recombinant_offspring, total_offspring)


def infer_three_point_order(distances_cM: dict[tuple[str, str], float]) -> LinkageMapResult:
    """Infer gene order from three pairwise map distances.

    The largest distance spans the two outside genes; the gene absent from that
    largest pair is the middle marker. This simple classroom inference assumes
    internally consistent pairwise distances and does not correct for
    interference or unobserved double crossovers.

    Args:
        distances_cM: Mapping from unordered gene-pair tuples to distances.

    Returns:
        LinkageMapResult containing the inferred order and adjacent distances.

    Raises:
        ValueError: If the mapping does not describe exactly three genes and
            three non-negative pairwise distances.
    """
    if len(distances_cM) != 3:
        raise ValueError("Exactly three pairwise distances are required.")

    normalized: dict[frozenset[str], float] = {}
    genes: set[str] = set()
    for pair, distance in distances_cM.items():
        if len(pair) != 2 or pair[0] == pair[1]:
            raise ValueError(f"Invalid gene pair: {pair!r}")
        if distance < 0:
            raise ValueError("Distances must be non-negative.")
        pair_key = frozenset(pair)
        if pair_key in normalized:
            raise ValueError(f"Duplicate unordered gene pair: {pair!r}")
        normalized[pair_key] = float(distance)
        genes.update(pair)

    if len(genes) != 3:
        raise ValueError("Distances must describe exactly three distinct genes.")

    max_pair, span = max(normalized.items(), key=lambda item: item[1])
    outside = tuple(sorted(max_pair))
    middle_candidates = genes - set(outside)
    if len(middle_candidates) != 1:
        raise ValueError("Could not identify a unique middle gene.")
    middle = next(iter(middle_candidates))
    left, right = outside

    left_distance = normalized[frozenset((left, middle))]
    right_distance = normalized[frozenset((middle, right))]
    return LinkageMapResult(
        order=(left, middle, right),
        adjacent_distances_cM=(left_distance, right_distance),
        span_cM=span,
    )


def jukes_cantor_distance(p_distance: float) -> float:
    """Compute the Jukes-Cantor corrected nucleotide distance.

    d = -(3/4) * ln(1 - (4/3)*p)

    Args:
        p_distance: Proportional sequence difference [0, 0.75).

    Returns:
        Jukes-Cantor corrected distance.

    Raises:
        ValueError: If p_distance is out of valid range.
    """
    if not (0.0 <= p_distance < 0.75):
        raise ValueError(f"p_distance must be in [0, 0.75), got {p_distance}")
    if p_distance == 0.0:
        return 0.0
    d = -(3.0 / 4.0) * math.log(1.0 - (4.0 / 3.0) * p_distance)
    return d


def cpg_methylation_remaining(initial_methylation: float, divisions: int, maintenance_efficiency: float) -> float:
    """
    Calculates the proportion of CpG methylation remaining after a number of cell divisions,
    given a specific DNA methylation maintenance efficiency (e.g. by DNMT1).

    Args:
        initial_methylation (float): Initial proportion of methylated CpGs (0 to 1.0).
        divisions (int): Number of cell divisions.
        maintenance_efficiency (float): Efficiency of maintenance methylation per division (0 to 1.0).

    Returns:
        float: Proportion of methylation remaining.
    """
    if divisions < 0:
        raise ValueError("Number of divisions cannot be negative.")
    return initial_methylation * (maintenance_efficiency**divisions)


def histone_modification_state(mark: str) -> str:
    """
    Returns the general transcriptional state associated with a given canonical histone mark.

    Args:
        mark (str): Standard nomenclature for a histone mark (e.g. 'H3K4me3', 'H3K27me3').

    Returns:
        str: 'active', 'repressed', or 'context-dependent'
    """
    repressive_marks = {"H3K9me3", "H3K27me3", "H4K20me3", "H3K9me2"}
    activating_marks = {"H3K4me3", "H3K36me3", "H3K79me2", "H3K27ac", "H3K9ac", "H4K16ac", "H3K4me1"}

    mark = mark.upper()

    if mark in (m.upper() for m in repressive_marks):
        return "repressed"
    elif mark in (m.upper() for m in activating_marks):
        return "active"
    else:
        return "context-dependent"


def synthetic_methylation_beta_matrix(
    n_loci: int = 24,
    n_samples: int = 8,
    rng_seed: int = 42,
):
    """Return a deterministic synthetic CpG methylation β matrix for teaching plots.

    Args:
        n_loci: Number of CpG loci (rows).
        n_samples: Number of samples (columns).
        rng_seed: RNG seed for reproducibility.

    Returns:
        ``numpy.ndarray`` of shape ``(n_loci, n_samples)`` with β in [0, 1].
    """
    import numpy as np

    rng = np.random.default_rng(rng_seed)
    base = rng.uniform(0.15, 0.85, size=(n_loci, n_samples))
    if n_loci > 14:
        base[8:15, :] *= 0.4
    return np.clip(base, 0.0, 1.0)


gametes = _gametes
