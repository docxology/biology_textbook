"""Biology subpackage — top-level init.

Exposes all nine domain subpackages for Units I-X of the textbook plus the
manuscript cross-reference validator (used by the build pipeline to enforce
pandoc-crossref label completeness).
"""

from . import cell
from . import genetics
from . import evolution
from . import ecology
from . import physiology
from . import biochemistry
from . import microbiology
from . import botany
from . import neuroscience
from . import foundations
from . import crossref_validator
from . import chapter_metadata
from . import curriculum
from . import alignment
from . import toc

__all__ = [
    "cell",
    "genetics",
    "evolution",
    "ecology",
    "physiology",
    "biochemistry",
    "microbiology",
    "botany",
    "neuroscience",
    "foundations",
    "crossref_validator",
    "chapter_metadata",
    "curriculum",
    "alignment",
    "toc",
]
