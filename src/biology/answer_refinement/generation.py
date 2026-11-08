"""Fail closed when no independently reviewed prompt-specific answer exists."""

from __future__ import annotations


class UnsupportedAnswerRepair(ValueError):
    """An author must supply a substantive answer; no source was changed."""


def generate_answer(
    q_num: int, tier: str, q_text: str, chapter_ref: str,
    category: str = "", evidence: tuple[str, str] | None = None,
) -> str:
    """Refuse heuristic guidance masquerading as a worked answer.

    Chapter excerpts, command verbs and ordinal tiers do not establish a
    solution to a particular prompt. There are currently no reviewed automatic
    solvers registered for this maintenance operation.
    """
    raise UnsupportedAnswerRepair(
        f"Q{q_num} ({chapter_ref}): no reviewed prompt-specific answer; "
        f"author a substantive SOLUTION for {q_text!r}. No changes written."
    )


__all__ = ["UnsupportedAnswerRepair", "generate_answer"]
