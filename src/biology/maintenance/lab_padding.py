"""Append debrief blocks to short lab manuscripts."""

from __future__ import annotations

import re
from pathlib import Path

LAB_LABEL_RE = re.compile(r"\\label\{sec:lab_(unit_[0-9IVX]+)_([a-z_]+)\}")

LAB_DEBRIEF_TEMPLATE = """
## Debrief and Reflection

After you finish the practical work, spend 5–10 minutes in your small group
comparing results and discussing the following prompts. Each member should
contribute at least one observation before moving to the next prompt:

1. **What did your measurements show** — compare the group's results to
   the textbook's predictions. Where they diverge, suggest at least one
   mechanistic explanation before concluding "experimental error."
2. **What would change the outcome** — propose one modification to the
   procedure that would sharpen the measurement or extend the result to a
   new biological context, and predict what you would observe.
3. **One-sentence headline** — each student composes a single sentence
   summarizing the lab's take-home message, suitable for a tweet. Compare
   sentences across groups; good headlines are short, quantitative, and
   mechanistic.
4. **Connection back to the textbook** — identify one section of
   \\cref{{{chapter_label}}} that your data either confirmed or
   complicated. Cite the specific passage.

## Further Reading (Lab)

- Revisit the parent chapter \\cref{{{chapter_label}}} for the theoretical
  foundations on which this lab is built.
- Look up any **bolded glossary term** introduced in the textbook chapter
  (each has a `[**term**](#gl:slug)` link in the text) — its master
  definition is in `manuscript/glossary.md`.
- Explore the appended `src/` module that implements the corresponding
  quantitative model (when applicable) — referenced in the parent
  chapter's "Bridge to Computation" subsection.

*Module footer: parent chapter `\\cref{{{chapter_label}}}`; all numerical
quantities in this lab use SI units — see Appendix B of the textbook for
unit conversions and biological-scale reference values.*
"""


def derive_chapter_label_from_lab(text: str) -> str | None:
    """Return parent chapter label from a lab ``\\label{sec:lab_...}`` anchor."""
    match = LAB_LABEL_RE.search(text)
    if match is None:
        return None
    unit, stem = match.group(1), match.group(2)
    return f"sec:{unit}_{stem}"


def append_debrief_if_short(text: str, *, min_lines: int = 100) -> str | None:
    """Append debrief block when lab is short and lacks one; return new text or None."""
    if "## Debrief and Reflection" in text:
        return None
    if text.count("\n") >= min_lines:
        return None
    chapter_label = derive_chapter_label_from_lab(text)
    if chapter_label is None:
        return None
    return text.rstrip() + "\n" + LAB_DEBRIEF_TEMPLATE.format(chapter_label=chapter_label)


def apply_lab_debrief(path: Path, *, write: bool = True, min_lines: int = 100) -> bool:
    """Append debrief block to ``path`` when eligible."""
    text = path.read_text(encoding="utf-8")
    updated = append_debrief_if_short(text, min_lines=min_lines)
    if updated is None:
        return False
    if write:
        from textbook_io import write_text_atomic

        write_text_atomic(path, updated)
    return True


__all__ = [
    "LAB_DEBRIEF_TEMPLATE",
    "append_debrief_if_short",
    "apply_lab_debrief",
    "derive_chapter_label_from_lab",
]
