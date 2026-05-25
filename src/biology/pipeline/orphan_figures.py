"""Insert references to orphan figure generators into their natural chapters.

Every figure generator in ``src/visualization/`` should have at least one
corresponding ``\\begin{figure}...\\end{figure}`` block in the manuscript so the
PDF includes the generated PNG. The catalog of insertions lives in
``orphan_figures.yaml`` next to this module; this file owns the data model,
YAML loader, and injection logic. The thin CLI is at
``scripts/insert_orphan_figures.py``.

Idempotent: if the ``\\includegraphics{../figures/<name>.png}`` directive is
already present in the target file, that file is skipped.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol

import yaml

from biology.maintenance.models import PROJECT

MANUSCRIPT = PROJECT / "manuscript"
CATALOG_PATH = Path(__file__).resolve().parent / "orphan_figures.yaml"

_REQUIRED_FIELDS = ("png", "target", "anchor", "caption", "label", "alt")


class _WriteFn(Protocol):
    def __call__(self, path: Path, text: str) -> None: ...


def _default_writer() -> _WriteFn:
    from textbook_io import write_text_atomic

    return write_text_atomic


@dataclass(frozen=True)
class FigureInsertion:
    """One orphan figure insertion request."""

    png: str
    target: Path
    anchor: str
    caption: str
    label: str
    alt: str


_FIGURE_TEMPLATE = (
    "\n\\begin{{figure}}[htbp]\n"
    "\\centering\n"
    "\\includegraphics[width=0.85\\textwidth]{{../figures/{png}.png}}\n"
    "\\caption{{{caption}}}\n"
    "\\label{{{label}}}\n"
    "\\end{{figure}}\n"
    "\n<!-- alt: {alt} -->\n"
)


def load_insertions(
    catalog_path: Path = CATALOG_PATH,
    *,
    manuscript_root: Path = MANUSCRIPT,
) -> list[FigureInsertion]:
    """Parse the YAML catalog into ``FigureInsertion`` records."""
    raw = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    rows = (raw or {}).get("insertions", [])
    out: list[FigureInsertion] = []
    for row in rows:
        missing = [field for field in _REQUIRED_FIELDS if field not in row]
        if missing:
            raise ValueError(f"orphan_figures.yaml row missing fields {missing}: {row}")
        caption = " ".join(str(row["caption"]).split())
        alt = " ".join(str(row["alt"]).split())
        out.append(
            FigureInsertion(
                png=row["png"],
                target=manuscript_root / row["target"],
                anchor=row["anchor"],
                caption=caption,
                label=row["label"],
                alt=alt,
            )
        )
    return out


def inject(
    path: Path,
    ins: FigureInsertion,
    *,
    dry_run: bool = False,
    write_fn: _WriteFn | None = None,
) -> bool:
    """Inject one figure block at the first blank line after ``ins.anchor``."""
    if not path.exists():
        print(f"WARN: missing {path}", file=sys.stderr)
        return False
    text = path.read_text(encoding="utf-8")
    if f"{ins.png}.png" in text:
        return False
    idx = text.lower().find(ins.anchor.lower())
    if idx < 0:
        print(f"WARN: anchor '{ins.anchor}' not found in {path.name}", file=sys.stderr)
        return False
    blank = text.find("\n\n", idx)
    if blank < 0:
        blank = len(text)
    block = _FIGURE_TEMPLATE.format(png=ins.png, caption=ins.caption, label=ins.label, alt=ins.alt)
    new_text = text[: blank + 1] + block + text[blank + 1 :]
    if not dry_run:
        writer = write_fn or _default_writer()
        writer(path, new_text)
    return True


@dataclass(frozen=True)
class OrphanFigureResult:
    inserted: int
    total: int


def apply_orphan_figures(
    *,
    dry_run: bool = False,
    catalog_path: Path = CATALOG_PATH,
    manuscript_root: Path = MANUSCRIPT,
    write_fn: _WriteFn | None = None,
) -> OrphanFigureResult:
    """Inject every catalog row that is not already present in its target file."""
    insertions = load_insertions(catalog_path, manuscript_root=manuscript_root)
    inserted = sum(
        1 for ins in insertions if inject(ins.target, ins, dry_run=dry_run, write_fn=write_fn)
    )
    return OrphanFigureResult(inserted=inserted, total=len(insertions))


__all__ = [
    "CATALOG_PATH",
    "FigureInsertion",
    "MANUSCRIPT",
    "OrphanFigureResult",
    "apply_orphan_figures",
    "inject",
    "load_insertions",
]
