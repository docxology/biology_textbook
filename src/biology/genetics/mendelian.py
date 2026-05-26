"""Mendelian genetics: gametes and Punnett squares."""

from __future__ import annotations

from dataclasses import dataclass

from textbook_logging import get_logger


logger = get_logger(__name__)


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


def _gametes(genotype: str) -> list[str]:
    """Generate gametes from a diploid genotype string (e.g. 'Aa' → ['A','a'])."""
    if len(genotype) != 2:
        raise ValueError(f"Genotype must be 2 characters, got '{genotype}'")
    a1, a2 = genotype[0], genotype[1]
    if a1 == a2:
        return [a1]
    return [a1, a2]


def punnett_square(parent1: str, parent2: str) -> PunnettSquareResult:
    """Perform a monohybrid Punnett square cross."""
    g1 = _gametes(parent1)
    g2 = _gametes(parent2)

    offspring: list[str] = []
    for a in g1:
        for b in g2:
            if a.isupper() or (not b.isupper()):
                offspring.append(f"{a}{b}")
            else:
                offspring.append(f"{b}{a}")

    weights = [1.0 / len(offspring)] * len(offspring)

    counts: dict[str, float] = {}
    for geno, w in zip(offspring, weights):
        counts[geno] = counts.get(geno, 0.0) + w

    total = sum(counts.values())
    genotype_ratios = {k: v / total for k, v in counts.items()}

    pheno_dom = sum(v for k, v in genotype_ratios.items() if k[0].isupper() or k[1].isupper())
    pheno_rec = 1.0 - pheno_dom
    phenotype_ratios = {"dominant": pheno_dom, "recessive": pheno_rec}

    logger.debug("Punnett %s×%s: genotype_ratios=%s", parent1, parent2, genotype_ratios)
    return PunnettSquareResult(
        parent1=parent1,
        parent2=parent2,
        offspring_genotypes=offspring,
        genotype_ratios=genotype_ratios,
        phenotype_ratios=phenotype_ratios,
    )


gametes = _gametes
