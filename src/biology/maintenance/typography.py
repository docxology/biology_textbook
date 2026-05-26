"""Typography normalization for manuscript prose."""

from __future__ import annotations

import re
from pathlib import Path

from biology.maintenance.manuscript_spans import (
    GREEK_PROSE_SPAN_OPTIONS,
    TYPOGRAPHY_SPAN_OPTIONS,
    in_protected,
    protected_spans,
)

_ARROW_RE = re.compile(r"(?<![=\-])-->(?![>\-])")

GREEK_LATEX_TO_UNICODE: dict[str, str] = {
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
    r"\Alpha": "Α",
    r"\Beta": "Β",
    r"\Gamma": "Γ",
    r"\Delta": "Δ",
    r"\Epsilon": "Ε",
    r"\Zeta": "Ζ",
    r"\Eta": "Η",
    r"\Theta": "Θ",
    r"\Iota": "Ι",
    r"\Kappa": "Κ",
    r"\Lambda": "Λ",
    r"\Mu": "Μ",
    r"\Nu": "Ν",
    r"\Xi": "Ξ",
    r"\Pi": "Π",
    r"\Rho": "Ρ",
    r"\Sigma": "Σ",
    r"\Tau": "Τ",
    r"\Upsilon": "Υ",
    r"\Phi": "Φ",
    r"\Chi": "Χ",
    r"\Psi": "Ψ",
    r"\Omega": "Ω",
}


def normalize_arrows_in_text(text: str) -> tuple[str, int]:
    """Convert ASCII ``-->`` to ``→`` outside protected spans."""
    protected = protected_spans(text, options=TYPOGRAPHY_SPAN_OPTIONS)
    matches = list(_ARROW_RE.finditer(text))
    out = text
    converted = 0
    for match in reversed(matches):
        if in_protected(match.start(), protected):
            continue
        out = out[: match.start()] + "→" + out[match.end():]
        converted += 1
    return out, converted


def replace_greek_math_in_text(text: str) -> tuple[str, int]:
    """Replace ``$\\greek$`` with Unicode outside protected spans."""
    protected = protected_spans(text, options=GREEK_PROSE_SPAN_OPTIONS)
    letters = "|".join(re.escape(greek) for greek in GREEK_LATEX_TO_UNICODE)
    pattern = re.compile(rf"\$({letters})\$")
    matches = list(pattern.finditer(text))
    out = text
    replaced = 0
    for match in reversed(matches):
        if in_protected(match.start(), protected):
            continue
        out = out[: match.start()] + GREEK_LATEX_TO_UNICODE[match.group(1)] + out[match.end():]
        replaced += 1
    return out, replaced


def normalize_arrows_in_file(path: Path, *, write: bool = True) -> int:
    text = path.read_text(encoding="utf-8")
    normalized, count = normalize_arrows_in_text(text)
    if count and write:
        from textbook_io import write_text_atomic

        write_text_atomic(path, normalized)
    return count


def replace_greek_math_in_file(path: Path, *, write: bool = True) -> int:
    text = path.read_text(encoding="utf-8")
    normalized, count = replace_greek_math_in_text(text)
    if count and write:
        from textbook_io import write_text_atomic

        write_text_atomic(path, normalized)
    return count


__all__ = [
    "GREEK_LATEX_TO_UNICODE",
    "normalize_arrows_in_file",
    "normalize_arrows_in_text",
    "replace_greek_math_in_file",
    "replace_greek_math_in_text",
]
