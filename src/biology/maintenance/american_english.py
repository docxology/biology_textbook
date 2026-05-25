"""American English spelling normalization for textbook prose."""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml

from biology.maintenance.models import PROJECT

MANUSCRIPT = PROJECT / "manuscript"
DATA_FILE = Path(__file__).resolve().parent / "data" / "british_to_american.yaml"

SKIP_FILENAMES = frozenset({"references.bib", "preamble.md"})
SKIP_RELATIVE_PATHS = frozenset(
    {
        "src/biology/maintenance/american_english.py",
        "src/biology/maintenance/data/british_to_american.yaml",
        "src/biology/quality/patterns.py",
    }
)


@dataclass(frozen=True)
class NormalizeResult:
    """Outcome of normalizing one file."""

    path: Path
    replacements: int
    changed: bool


@lru_cache(maxsize=1)
def _load_mapping() -> tuple[tuple[str, str], ...]:
    raw = yaml.safe_load(DATA_FILE.read_text(encoding="utf-8"))
    pairs = [(str(british), str(american)) for british, american in raw]
    return tuple(sorted(pairs, key=lambda pair: len(pair[0]), reverse=True))


def british_to_american_pairs() -> tuple[tuple[str, str], ...]:
    """Return British→American replacement pairs, longest first."""
    return _load_mapping()


def british_spelling_pattern() -> re.Pattern[str]:
    """Compiled alternation of British forms for audit scans."""
    british = [re.escape(british) for british, _ in _load_mapping()]
    return re.compile(r"\b(" + "|".join(british) + r")\b", flags=re.IGNORECASE)


PROTECTED_FENCE_LANGS = frozenset(
    {
        "python",
        "py",
        "yaml",
        "yml",
        "json",
        "bash",
        "sh",
        "shell",
        "r",
        "sql",
        "javascript",
        "js",
        "typescript",
        "ts",
    }
)


def _protected_spans(text: str) -> list[tuple[int, int]]:
    """Return spans that must not be rewritten (code, math)."""
    spans: list[tuple[int, int]] = []
    fence_re = re.compile(r"```([a-zA-Z0-9_-]*)\s*\n.*?\n```", re.DOTALL)
    for match in fence_re.finditer(text):
        lang = match.group(1).strip().lower()
        if lang in PROTECTED_FENCE_LANGS:
            spans.append(match.span())
    for match in re.finditer(r"\$\$.*?\$\$", text, re.DOTALL):
        spans.append(match.span())
    for env in ("equation", "align", "gather", "multline", "figure", "table"):
        for match in re.finditer(
            rf"\\begin\{{{env}\*?\}}.*?\\end\{{{env}\*?\}}", text, re.DOTALL
        ):
            spans.append(match.span())
    for match in re.finditer(r"(?<!\$)\$[^$\n]+\$", text):
        spans.append(match.span())
    for match in re.finditer(r"`[^`\n]+`", text):
        spans.append(match.span())
    for match in re.finditer(r"https?://[^\s)>\]}]+", text):
        spans.append(match.span())
    front_matter = re.match(r"\A---\n.*?\n---\n", text, re.DOTALL)
    if front_matter:
        spans.append(front_matter.span())
    return sorted(spans)


def _is_protected(pos: int, spans: list[tuple[int, int]]) -> bool:
    for start, end in spans:
        if start <= pos < end:
            return True
        if start > pos:
            return False
    return False


def _apply_case(source: str, replacement: str) -> str:
    if source.isupper():
        return replacement.upper()
    if source[0].isupper():
        return replacement[0].upper() + replacement[1:]
    return replacement


def normalize_text(text: str) -> tuple[str, int]:
    """Rewrite British spellings in ``text`` outside protected spans."""
    protected = _protected_spans(text)
    replacements: list[tuple[int, int, str]] = []
    for british, american in _load_mapping():
        pattern = re.compile(rf"\b{re.escape(british)}\b", flags=re.IGNORECASE)
        for match in pattern.finditer(text):
            if _is_protected(match.start(), protected):
                continue
            replacements.append(
                (match.start(), match.end(), _apply_case(match.group(0), american))
            )
    if not replacements:
        return text, 0
    out = text
    for start, end, american in sorted(replacements, key=lambda item: item[0], reverse=True):
        out = out[:start] + american + out[end:]
    return out, len(replacements)


def normalize_file(path: Path, *, write: bool) -> NormalizeResult:
    """Normalize one markdown or YAML file."""
    original = path.read_text(encoding="utf-8")
    normalized, count = normalize_text(original)
    changed = normalized != original
    if changed and write:
        from textbook_io import write_text_atomic

        write_text_atomic(path, normalized)
    return NormalizeResult(path, count, changed)


def _should_normalize(path: Path, root: Path) -> bool:
    rel = path.resolve().relative_to(root.resolve()).as_posix()
    return rel not in SKIP_RELATIVE_PATHS


def iter_target_files(root: Path) -> list[Path]:
    """Return project files that should use American English."""
    files: list[Path] = []
    manuscript = root / "manuscript"
    if manuscript.exists():
        for path in sorted(manuscript.rglob("*")):
            if not path.is_file() or path.name in SKIP_FILENAMES:
                continue
            if path.suffix in {".md", ".yaml", ".yml"} and _should_normalize(path, root):
                files.append(path)
    docs = root / "docs"
    if docs.exists():
        files.extend(
            path
            for path in sorted(docs.rglob("*.md"))
            if _should_normalize(path, root)
        )
    for name in ("README.md", "AGENTS.md", "REVIEW.md"):
        candidate = root / name
        if candidate.exists() and _should_normalize(candidate, root):
            files.append(candidate)
    for rel in ("tests/README.md", "tests/AGENTS.md"):
        candidate = root / rel
        if candidate.exists() and _should_normalize(candidate, root):
            files.append(candidate)
    biology_src = root / "src" / "biology"
    if biology_src.exists():
        files.extend(
            path
            for path in sorted(biology_src.rglob("*"))
            if path.is_file()
            and path.suffix in {".py", ".yaml", ".yml", ".md"}
            and path.name != "american_english.py"
            and _should_normalize(path, root)
        )
    deduped: list[Path] = []
    seen: set[Path] = set()
    for path in files:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            deduped.append(path)
    return deduped


def find_british_spellings(text: str) -> list[tuple[int, str, str]]:
    """Return line number, matched token, and line excerpt for audit failures."""
    hits: list[tuple[int, str, str]] = []
    protected = _protected_spans(text)
    pattern = british_spelling_pattern()
    offset = 0
    for line_no, line in enumerate(text.splitlines(keepends=True), start=1):
        for match in pattern.finditer(line):
            if _is_protected(offset + match.start(), protected):
                continue
            excerpt = line.strip()
            hits.append((line_no, match.group(0), excerpt))
        offset += len(line)
    return hits
