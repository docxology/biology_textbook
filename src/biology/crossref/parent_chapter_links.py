"""Insert parent-chapter cross-references into labs and question banks."""

from __future__ import annotations

from pathlib import Path


def derive_parent_section_label(path: Path) -> str | None:
    """Return ``sec:unit_X_<stem>`` for a lab or question bank path."""
    try:
        idx_unit = [part.startswith("unit_") or part == "unit_0" for part in path.parts].index(True)
    except ValueError:
        return None
    unit = path.parts[idx_unit]
    stem = path.stem
    for prefix in ("lab_", "questions_"):
        if stem.startswith(prefix):
            stem = stem[len(prefix) :]
            break
    return f"sec:{unit}_{stem}"


def insert_parent_chapter_cref(text: str, path: Path) -> str | None:
    """Insert a parent-chapter ``\\cref`` note when absent; return new text or None."""
    label = derive_parent_section_label(path)
    if label is None or f"\\cref{{{label}}}" in text:
        return None
    lines = text.splitlines()
    label_marker = "\\label{sec:"
    for index, line in enumerate(lines):
        if not line.strip().startswith(label_marker):
            continue
        insert_at = index + 1
        while insert_at < len(lines) and (
            lines[insert_at].strip() == ""
            or lines[insert_at].strip().startswith("##")
            or lines[insert_at].strip().startswith("<!--")
            or lines[insert_at].strip().startswith(">")
        ):
            insert_at += 1
        if insert_at >= len(lines):
            break
        note = (
            f"*This activity accompanies \\cref{{{label}}} of the textbook — "
            f"review that chapter before attempting the exercises below.*"
        )
        new_lines = lines[:insert_at] + [note, ""] + lines[insert_at:]
        updated = "\n".join(new_lines) + ("\n" if text.endswith("\n") else "")
        return updated
    return None


def apply_parent_chapter_cref(path: Path, *, write: bool = True) -> bool:
    """Write parent-chapter cross-reference into ``path`` when missing."""
    text = path.read_text(encoding="utf-8")
    updated = insert_parent_chapter_cref(text, path)
    if updated is None:
        return False
    if write:
        from textbook_io import write_text_atomic

        write_text_atomic(path, updated)
    return True


__all__ = [
    "apply_parent_chapter_cref",
    "derive_parent_section_label",
    "insert_parent_chapter_cref",
]
