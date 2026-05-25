#!/usr/bin/env python3
"""Append a "Debrief and Further Reading" block to every lab under 100 lines.

For each lab markdown under ``manuscript/labs/**/lab_*.md`` with fewer
than 100 lines, append a uniform closing section containing:

* A Debrief and Reflection prompt (3-4 items) tying the lab's observable
  results to the chapter's big concepts.
* A Further Reading pointer to the parent chapter and glossary.
* A "Module" footer consistent with the textbook-wide pattern.

The block is idempotent: if the lab already contains ``## Debrief and
Reflection`` the file is skipped.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from _bootstrap import ensure_project_paths

ensure_project_paths(include_scripts=True)

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"
LABS = MANUSCRIPT / "labs"


# The appended block. ``{chapter_label}`` is replaced per lab.
BLOCK_TEMPLATE = """
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
   summarising the lab's take-home message, suitable for a tweet. Compare
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


_LABEL_RE = re.compile(r"\\label\{sec:lab_(unit_[0-9IVX]+)_([a-z_]+)\}")


def append_block(path: Path, dry_run: bool = False) -> bool:
    """Append the Debrief block if the lab is short and lacks one."""
    text = path.read_text(encoding="utf-8")
    if "## Debrief and Reflection" in text:
        return False
    line_count = text.count("\n")
    if line_count >= 100:
        return False
    # Find the chapter label (sec:lab_unit_X_<stem> → sec:unit_X_<stem>)
    m = _LABEL_RE.search(text)
    if not m:
        print(f"WARN: no \\label anchor in {path}", file=sys.stderr)
        return False
    unit, stem = m.group(1), m.group(2)
    chapter_label = f"sec:{unit}_{stem}"
    new_text = text.rstrip() + "\n" + BLOCK_TEMPLATE.format(chapter_label=chapter_label)
    if not dry_run:
        write_text_atomic(path, new_text)
    return True


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    touched = 0
    for lab in sorted(LABS.rglob("lab_*.md")):
        if append_block(lab, dry_run=dry_run):
            touched += 1
            print(f"  [{'D' if dry_run else '+'}] {lab.relative_to(MANUSCRIPT)}: +Debrief block")
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n[{mode}] labs_padded={touched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
