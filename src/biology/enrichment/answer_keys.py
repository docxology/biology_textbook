"""Identify unreviewed legacy solutions without fabricating replacement answers."""

from __future__ import annotations

import re

from biology.answer_refinement.classification import is_v1_generated
from biology.crossref.source import visible_text
from biology.enrichment.models import ChapterRecord

_SOLUTION_BLOCK = re.compile(
    r"<!-- SOLUTION\s*\n(?P<body>.*?)\n\s*SOLUTION -->", re.DOTALL
)


def refine_question_banks(records: list[ChapterRecord], dry_run: bool) -> tuple[int, int]:
    """Preview authoring needs, or refuse unreviewed answers before any writes.

    A prompt and chapter title cannot determine a correct biological answer.
    Reviewed solutions are immutable inputs to enrichment, not generated output.
    """
    needs_review: list[tuple[str, int]] = []
    for path in sorted({record.question_path for record in records}):
        text = path.read_text(encoding="utf-8")
        for number, match in enumerate(_SOLUTION_BLOCK.finditer(text), start=1):
            body = visible_text(match.group("body"))
            if is_v1_generated(body):
                needs_review.append((str(path), number))
    if needs_review and not dry_run:
        locations = "; ".join(f"{path}: solution {number}" for path, number in needs_review)
        raise ValueError(
            "Author reviewed, question-specific solutions; automatic answer generation "
            f"is unsupported. No question banks were written. {locations}"
        )
    return len({path for path, _number in needs_review}), len(needs_review)


__all__ = ["refine_question_banks"]
