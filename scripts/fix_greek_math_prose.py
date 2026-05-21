#!/usr/bin/env python3
"""Replace ``$\\greek$`` in prose with the Unicode codepoint.

Pandoc has a long-standing issue where ``$\\letter$`` in running text (and
especially inside pipe-table cells) is emitted as ``\\(\\letter)`` — missing
the closing ``\\)``. The result is an avalanche of "Missing $ inserted" and
"Bad math environment delimiter" errors that can abort xelatex.

Substituting the Unicode codepoint sidesteps pandoc entirely and always
typesets correctly with the main font (Linux Libertine O) which already
supports Greek.

The script is idempotent and *only* touches text *outside* fenced code
blocks, ``$$…$$`` display math, and ``\\begin{…}…\\end{…}`` LaTeX
environments — the math contexts where ``\\alpha`` must stay literal.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from scripts.atomic_io import write_text_atomic
except ModuleNotFoundError:  # pragma: no cover - direct script execution path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from atomic_io import write_text_atomic  # type: ignore[import-not-found,no-redef]


MANUSCRIPT = Path(__file__).resolve().parent.parent / "manuscript"

GREEK_MAP = {
    r"\alpha": "α",
    r"\beta": "β",
    r"\gamma": "γ",
    r"\delta": "δ",
    r"\epsilon": "ε",
    r"\zeta": "ζ",
    r"\eta": "η",
    r"\theta": "θ",
    r"\iota": "ι",
    r"\kappa": "κ",
    r"\lambda": "λ",
    r"\mu": "μ",
    r"\nu": "ν",
    r"\xi": "ξ",
    r"\pi": "π",
    r"\rho": "ρ",
    r"\sigma": "σ",
    r"\tau": "τ",
    r"\upsilon": "υ",
    r"\phi": "φ",
    r"\chi": "χ",
    r"\psi": "ψ",
    r"\omega": "ω",
    r"\Alpha": "Α", r"\Beta": "Β", r"\Gamma": "Γ", r"\Delta": "Δ",
    r"\Epsilon": "Ε", r"\Zeta": "Ζ", r"\Eta": "Η", r"\Theta": "Θ",
    r"\Iota": "Ι", r"\Kappa": "Κ", r"\Lambda": "Λ", r"\Mu": "Μ",
    r"\Nu": "Ν", r"\Xi": "Ξ", r"\Pi": "Π", r"\Rho": "Ρ",
    r"\Sigma": "Σ", r"\Tau": "Τ", r"\Upsilon": "Υ", r"\Phi": "Φ",
    r"\Chi": "Χ", r"\Psi": "Ψ", r"\Omega": "Ω",
}


def _protected_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for m in re.finditer(r"```.*?```", text, re.DOTALL):
        spans.append(m.span())
    for m in re.finditer(r"\$\$.*?\$\$", text, re.DOTALL):
        spans.append(m.span())
    for env in ("equation", "align", "gather", "multline", "figure", "table"):
        for m in re.finditer(rf"\\begin\{{{env}\*?\}}.*?\\end\{{{env}\*?\}}", text, re.DOTALL):
            spans.append(m.span())
    for m in re.finditer(r"`[^`\n]+`", text):
        spans.append(m.span())
    return sorted(spans)


def _in_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    for s, e in spans:
        if s <= pos < e:
            return True
        if s > pos:
            return False
    return False


def process(path: Path, dry_run: bool = False) -> int:
    text = path.read_text(encoding="utf-8")
    protected = _protected_spans(text)
    n = 0
    # Build regex:  $\alpha$ | $\beta$ | …   (only simple standalone Greek)
    letters = "|".join(re.escape(g) for g in GREEK_MAP)
    pattern = re.compile(rf"\$({letters})\$")
    # Scan right-to-left to avoid offset issues
    matches = list(pattern.finditer(text))
    out = text
    for m in reversed(matches):
        if _in_protected(m.start(), protected):
            continue
        greek = GREEK_MAP[m.group(1)]
        out = out[: m.start()] + greek + out[m.end():]
        n += 1
    if n and not dry_run:
        write_text_atomic(path, out)
    return n


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in argv
    total = 0
    files = 0
    for md in MANUSCRIPT.rglob("*.md"):
        if md.name in {"README.md", "AGENTS.md", "preamble.md"}:
            continue
        n = process(md, dry_run=dry_run)
        if n:
            files += 1
            total += n
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"[{mode}] greek_replaced={total} files_touched={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
