"""Biology subpackage — top-level init.

Exposes all nine domain subpackages for Units I-X of the textbook plus the
manuscript cross-reference validator (used by the build pipeline to enforce
pandoc-crossref label completeness).
"""

from . import (
    alignment,
    biochemistry,
    botany,
    cell,
    chapter_metadata,
    crossref_validator,
    curriculum,
    ecology,
    evolution,
    foundations,
    genetics,
    microbiology,
    neuroscience,
    physiology,
    toc,
)

__all__ = [
    "alignment",
    "biochemistry",
    "botany",
    "cell",
    "chapter_metadata",
    "crossref_validator",
    "curriculum",
    "ecology",
    "evolution",
    "foundations",
    "genetics",
    "microbiology",
    "neuroscience",
    "physiology",
    "toc",
]
