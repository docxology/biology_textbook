#!/usr/bin/env python3
"""Run the biology textbook publication-readiness gate.

Default ``--check`` runs the practical project-local gate: quality audits,
current-claim freshness, assessment synchronization, Mermaid alt normalization,
strict figure/diagram generation, lint, mypy, recursive markdown/prerender
validation, artifact counts, WIP resolver smoke, and tracked-artifact hygiene.

``--full`` adds expensive root orchestration: root setup, root project-only test
stage, root render, root output validation, and project coverage.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
from dataclasses import dataclass
import subprocess
import sys
from pathlib import Path


PROJECT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = PROJECT.parent.parent
SRC = PROJECT / "src"
MANUSCRIPT = PROJECT / "manuscript"

for path in (TEMPLATE_ROOT, SRC):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)


@dataclass(frozen=True)
class CommandStep:
    """One subprocess-backed audit step."""

    name: str
    command: tuple[str, ...]
    cwd: Path
    full_only: bool = False


@dataclass(frozen=True)
class PythonStep:
    """One in-process audit step."""

    name: str
    check: Callable[[], list[str]]
    full_only: bool = False


def build_command_steps(*, full: bool) -> list[CommandStep]:
    """Return subprocess checks for the selected audit depth."""

    py = sys.executable
    steps = [
        CommandStep(
            "quality-audit",
            (py, "scripts/audit_textbook_quality.py", "--check", "--max-advisories", "0"),
            PROJECT,
        ),
        CommandStep("current-claims", (py, "scripts/audit_current_claims.py", "--check"), PROJECT),
        CommandStep("visual-contracts", (py, "scripts/audit_visual_contracts.py", "--check"), PROJECT),
        CommandStep("assessment-sync", (py, "scripts/sync_assessment_metadata.py", "--check"), PROJECT),
        CommandStep("mermaid-alt-sync", (py, "scripts/add_mermaid_alt_text.py", "--check"), PROJECT),
        CommandStep("figures-strict", (py, "scripts/generate_figures.py"), PROJECT),
        CommandStep("diagrams-strict", (py, "scripts/generate_diagrams.py", "--strict-png"), PROJECT),
        CommandStep("ruff", ("uv", "run", "ruff", "check", "src", "scripts", "tests"), PROJECT),
        CommandStep("mypy", ("uv", "run", "mypy", "src", "scripts", "tests"), PROJECT),
        CommandStep(
            "root-wip-resolver-smoke",
            (
                "uv",
                "run",
                "python",
                "-c",
                (
                    "from pathlib import Path; "
                    "from infrastructure.project.discovery import resolve_project_root; "
                    "p=resolve_project_root(Path('.'), 'biology_textbook'); "
                    "assert p.is_dir() and p.name == 'biology_textbook' and 'projects_in_progress' in p.parts; "
                    "print(p)"
                ),
            ),
            TEMPLATE_ROOT,
        ),
        CommandStep(
            "coverage",
            ("uv", "run", "pytest", "tests", "--cov=src", "--cov-report=term-missing"),
            PROJECT,
            full_only=True,
        ),
        CommandStep(
            "root-setup",
            ("uv", "run", "python", "scripts/00_setup_environment.py", "--project", "biology_textbook"),
            TEMPLATE_ROOT,
            full_only=True,
        ),
        CommandStep(
            "root-project-tests",
            (
                "uv",
                "run",
                "python",
                "scripts/01_run_tests.py",
                "--project",
                "biology_textbook",
                "--project-only",
                "--quiet",
            ),
            TEMPLATE_ROOT,
            full_only=True,
        ),
        CommandStep(
            "root-render",
            ("uv", "run", "python", "scripts/03_render_pdf.py", "--project", "biology_textbook"),
            TEMPLATE_ROOT,
            full_only=True,
        ),
        CommandStep(
            "root-validate-output",
            ("uv", "run", "python", "scripts/04_validate_output.py", "--project", "biology_textbook"),
            TEMPLATE_ROOT,
            full_only=True,
        ),
    ]
    return [step for step in steps if full or not step.full_only]


def build_python_steps(*, full: bool) -> list[PythonStep]:
    """Return in-process checks for the selected audit depth."""

    steps = [
        PythonStep("recursive-markdown", check_recursive_markdown),
        PythonStep("recursive-prerender", check_recursive_prerender),
        PythonStep("artifact-counts", check_artifact_counts),
        PythonStep("tracked-artifact-hygiene", check_tracked_artifact_hygiene),
    ]
    return [step for step in steps if full or not step.full_only]


def run_command_step(step: CommandStep) -> int:
    """Run one command step and return its exit code."""

    print(f"\n== {step.name} ==")
    print(f"$ {' '.join(step.command)}")
    result = subprocess.run(step.command, cwd=step.cwd, check=False)  # noqa: S603
    if result.returncode:
        print(f"{step.name}: FAIL ({result.returncode})")
    else:
        print(f"{step.name}: PASS")
    return result.returncode


def run_python_step(step: PythonStep) -> int:
    """Run one Python check and return its exit code."""

    print(f"\n== {step.name} ==")
    issues = step.check()
    for issue in issues:
        print(issue)
    if issues:
        print(f"{step.name}: FAIL ({len(issues)} issue(s))")
        return 1
    print(f"{step.name}: PASS")
    return 0


def _recursive_manuscript_markdown() -> list[str]:
    skip_names = {"AGENTS.md", "README.md", "preamble.md"}
    return [str(path) for path in sorted(MANUSCRIPT.rglob("*.md")) if path.name not in skip_names]


def check_recursive_markdown() -> list[str]:
    """Run infrastructure markdown validators over the recursive manuscript set."""

    from infrastructure.validation.content.markdown_validator import (
        collect_symbols,
        validate_citations,
        validate_images,
        validate_math,
        validate_pandoc_pitfalls,
        validate_refs,
    )

    md_paths = _recursive_manuscript_markdown()
    labels, anchors = collect_symbols(md_paths)
    problems = []
    problems += validate_images(md_paths, TEMPLATE_ROOT)
    problems += validate_refs(md_paths, TEMPLATE_ROOT, labels, anchors)
    problems += validate_math(md_paths, TEMPLATE_ROOT)
    problems += validate_pandoc_pitfalls(md_paths, TEMPLATE_ROOT)
    problems += validate_citations(md_paths, TEMPLATE_ROOT, bib_file=MANUSCRIPT / "references.bib")
    formatted: list[str] = []
    for problem in problems:
        severity = getattr(problem.severity, "name", str(problem.severity))
        code = getattr(problem.code, "value", str(problem.code))
        formatted.append(f"{severity} {code} [{problem.file_path}] {problem.message}")
    return formatted


def check_recursive_prerender() -> list[str]:
    """Run the render-blocking source markdown gate over recursive manuscript files."""

    from infrastructure.core.exceptions import RenderingError
    from infrastructure.rendering._pdf_combined_renderer import prevalidate_source_markdown

    try:
        prevalidate_source_markdown(
            _recursive_manuscript_markdown(),
            repo_root=TEMPLATE_ROOT,
            bib_file=MANUSCRIPT / "references.bib",
        )
    except RenderingError as exc:
        return str(exc).splitlines()
    return []


def check_artifact_counts() -> list[str]:
    """Verify strict generation produced enough figure and Mermaid PNG artifacts."""

    from mermaid import ALL_BIOLOGY_DIAGRAMS
    from visualization import ALL_FIGURE_GENERATORS

    issues: list[str] = []
    figures_dir = PROJECT / "output" / "figures"
    mermaid_dir = figures_dir / "mermaid"
    figure_pngs = [path for path in figures_dir.glob("*.png") if path.is_file()]
    mermaid_pngs = [path for path in mermaid_dir.glob("*.png") if path.is_file()]

    expected_figures = len(ALL_FIGURE_GENERATORS)
    expected_diagrams = len(ALL_BIOLOGY_DIAGRAMS)
    if len(figure_pngs) < expected_figures:
        issues.append(f"expected at least {expected_figures} figure PNGs, found {len(figure_pngs)}")
    if len(mermaid_pngs) < expected_diagrams:
        issues.append(f"expected at least {expected_diagrams} Mermaid PNGs, found {len(mermaid_pngs)}")
    return issues


def check_tracked_artifact_hygiene() -> list[str]:
    """Fail if generated/cache artifacts under this WIP tree are tracked by git."""

    rel_project = PROJECT.relative_to(TEMPLATE_ROOT)
    result = subprocess.run(  # noqa: S603
        ("git", "ls-files", "--", str(rel_project)),
        cwd=TEMPLATE_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return [result.stderr.strip() or "git ls-files failed"]

    forbidden = (
        "/output/",
        "/.mypy_cache/",
        "/__pycache__/",
        ".pyc",
        ".pyo",
        ".pytest_cache/",
    )
    offenders = [
        path
        for path in result.stdout.splitlines()
        if any(fragment in f"/{path}" for fragment in forbidden)
    ]
    return [f"tracked generated/cache artifact: {path}" for path in offenders]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit non-zero if any readiness step fails.")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Include expensive root setup/test/render/validation and coverage.",
    )
    args = parser.parse_args(argv)

    failures = 0
    for command_step in build_command_steps(full=args.full):
        failures += 1 if run_command_step(command_step) else 0
    for python_step in build_python_steps(full=args.full):
        failures += 1 if run_python_step(python_step) else 0

    status = "PASS" if failures == 0 else "FAIL"
    depth = "full" if args.full else "default"
    print(f"\naudit_publication_readiness: {status} ({depth}, failures={failures})")
    if args.check and failures:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
