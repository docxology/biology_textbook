"""Publication-readiness audit gate for the biology textbook.

The default check runs the practical project-local gate: quality audits,
current-claim freshness, assessment synchronization, Mermaid alt normalization,
strict figure/diagram generation, visual contracts, lint, mypy, recursive
markdown/prerender validation, artifact counts, WIP resolver smoke, and
tracked-artifact hygiene.

``--full`` adds expensive root orchestration: root setup, the authoritative
project-root pytest with the 90% ``src/`` gate, root render, root output
validation, and the root PDF log gate.

The thin CLI is at ``scripts/audit_publication_readiness.py``.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

from biology.maintenance.models import PROJECT
from textbook_paths import discover_template_root

TEMPLATE_ROOT = discover_template_root(PROJECT)
MANUSCRIPT = PROJECT / "manuscript"
PROJECT_PDF_LOG = PROJECT / "output" / "pdf" / "_combined_manuscript.log"
DEFAULT_REVIEW_ARTIFACT_DIR = Path(tempfile.gettempdir()) / "biology_textbook_publication_readiness"


@dataclass(frozen=True)
class CommandStep:
    """One subprocess-backed audit step."""

    name: str
    command: tuple[str, ...]
    cwd: Path
    full_only: bool = False
    depends_on: frozenset[str] = frozenset()


@dataclass(frozen=True)
class PythonStep:
    """One in-process audit step."""

    name: str
    check: Callable[[], list[str]]
    full_only: bool = False
    depends_on: frozenset[str] = frozenset()


_StepT = TypeVar("_StepT", CommandStep, PythonStep)


def build_command_steps(*, full: bool, artifact_dir: Path | None = None) -> list[CommandStep]:
    """Return subprocess checks for the selected audit depth."""

    py = sys.executable
    template_cwd = TEMPLATE_ROOT or PROJECT
    review_artifacts = artifact_dir or DEFAULT_REVIEW_ARTIFACT_DIR
    review_figures = review_artifacts / "figures"
    review_mermaid = review_figures / "mermaid"
    review_manifest = review_figures / "visual_manifest.json"
    steps = [
        CommandStep(
            "quality-audit",
            (py, "scripts/audit_textbook_quality.py", "--check", "--max-advisories", "0"),
            PROJECT,
        ),
        CommandStep("current-claims", (py, "scripts/audit_current_claims.py", "--check"), PROJECT),
        CommandStep("assessment-sync", (py, "scripts/sync_assessment_metadata.py", "--check"), PROJECT),
        CommandStep("mermaid-alt-sync", (py, "scripts/add_mermaid_alt_text.py", "--check"), PROJECT),
        CommandStep(
            "figures-strict",
            (py, "scripts/generate_figures.py", "--output-dir", str(review_figures)),
            PROJECT,
        ),
        CommandStep(
            "diagrams-strict",
            (py, "scripts/generate_diagrams.py", "--strict-png", "--output-dir", str(review_mermaid)),
            PROJECT,
            depends_on=frozenset({"figures-strict"}),
        ),
        CommandStep(
            "visual-contracts",
            (
                py,
                "scripts/audit_visual_contracts.py",
                "--figures-root",
                str(review_figures),
                "--output",
                str(review_manifest),
                "--render-inline",
                "--check",
            ),
            PROJECT,
            depends_on=frozenset({"diagrams-strict"}),
        ),
        CommandStep(
            "ruff",
            ("uv", "run", "ruff", "check", "src", "scripts", "tests", "--ignore", "E402"),
            PROJECT,
        ),
        CommandStep("mypy", ("uv", "run", "mypy", "src", "scripts", "tests"), PROJECT),
        CommandStep(
            "root-wip-resolver-smoke",
            (
                "uv",
                "run",
                "python",
                "-c",
                "from biology.quality.wip_resolver_smoke import main; main()",
            ),
            PROJECT,
        ),
        CommandStep(
            "project-tests-gate",
            (
                "uv",
                "run",
                "pytest",
                "tests",
                "--cov=src",
                "--cov-fail-under=90",
                "--cov-report=term-missing",
                "-q",
            ),
            PROJECT,
            full_only=True,
        ),
        CommandStep(
            "root-setup",
            ("uv", "run", "python", "scripts/00_setup_environment.py", "--project", "biology_textbook"),
            template_cwd,
            full_only=True,
        ),
        CommandStep(
            "root-render",
            ("uv", "run", "python", "scripts/03_render_pdf.py", "--project", "biology_textbook"),
            template_cwd,
            full_only=True,
            depends_on=frozenset({"root-setup"}),
        ),
        CommandStep(
            "root-validate-output",
            ("uv", "run", "python", "scripts/04_validate_output.py", "--project", "biology_textbook"),
            template_cwd,
            full_only=True,
            depends_on=frozenset({"root-render"}),
        ),
        CommandStep(
            "root-pdf-log",
            (
                sys.executable,
                "scripts/check_pdf_log.py",
                str(PROJECT_PDF_LOG),
                "--max-overfull-pt",
                "2500",
                "--allow-missing-glyphs",
            ),
            PROJECT,
            full_only=True,
            depends_on=frozenset({"root-validate-output"}),
        ),
    ]
    return [step for step in steps if full or not step.full_only]


def build_python_steps(*, full: bool, artifact_dir: Path | None = None) -> list[PythonStep]:
    """Return in-process checks for the selected audit depth."""

    review_artifacts = artifact_dir or DEFAULT_REVIEW_ARTIFACT_DIR
    steps = [
        PythonStep("recursive-markdown", check_recursive_markdown),
        PythonStep("recursive-prerender", check_recursive_prerender),
        PythonStep("artifact-counts", lambda: check_artifact_counts(review_artifacts), depends_on=frozenset({"visual-contracts"})),
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
    if TEMPLATE_ROOT is None:
        return ["template infrastructure not found; set BIOLOGY_TEXTBOOK_TEMPLATE_ROOT"]

    from infrastructure.validation.content.markdown_validator import (  # type: ignore[import-not-found]
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
    if TEMPLATE_ROOT is None:
        return ["template infrastructure not found; set BIOLOGY_TEXTBOOK_TEMPLATE_ROOT"]

    from infrastructure.core.exceptions import RenderingError  # type: ignore[import-not-found]
    from infrastructure.rendering._pdf_combined_renderer import prevalidate_source_markdown  # type: ignore[import-not-found]

    try:
        prevalidate_source_markdown(
            _recursive_manuscript_markdown(),
            repo_root=TEMPLATE_ROOT,
            bib_file=MANUSCRIPT / "references.bib",
        )
    except RenderingError as exc:
        return str(exc).splitlines()
    return []


def check_artifact_counts(artifact_dir: Path | None = None) -> list[str]:
    """Verify strict generation produced enough figure and Mermaid PNG artifacts."""
    from mermaid import ALL_BIOLOGY_DIAGRAMS
    from visualization import ALL_FIGURE_GENERATORS

    issues: list[str] = []
    figures_dir = (artifact_dir or DEFAULT_REVIEW_ARTIFACT_DIR) / "figures"
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
    result = subprocess.run(  # noqa: S603
        ("git", "ls-files", "--", "."),
        cwd=PROJECT,
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


def ready_step_names(steps: Sequence[CommandStep | PythonStep], completed: set[str]) -> list[str]:
    """Return step names whose dependencies are satisfied."""
    return [step.name for step in steps if step.name not in completed and step.depends_on.issubset(completed)]


def _run_step_batches(
    steps: Sequence[_StepT],
    runner: Callable[[_StepT], int],
    *,
    max_workers: int,
    completed_command_names: set[str] | None = None,
) -> int:
    """Run ``steps`` in dependency order, parallelizing each ready wave."""
    if max_workers <= 1:
        failures = 0
        for step in steps:
            failures += runner(step)
        return failures

    remaining = list(steps)
    completed = set(completed_command_names or ())
    failures = 0

    while remaining:
        ready = [
            step
            for step in remaining
            if step.depends_on.issubset(completed)
        ]
        if not ready:
            pending = ", ".join(step.name for step in remaining)
            raise RuntimeError(f"publication gate dependency deadlock among: {pending}")

        with ThreadPoolExecutor(max_workers=min(max_workers, len(ready))) as pool:
            futures = {pool.submit(runner, step): step for step in ready}
            for future in as_completed(futures):
                step = futures[future]
                failures += future.result()
                completed.add(step.name)

        remaining = [step for step in remaining if step.name not in completed]

    return failures


def run_publication_gate(*, full: bool, artifact_dir: Path, max_workers: int = 1) -> int:
    """Run every selected audit step under ``artifact_dir`` and return failure count."""
    command_steps = build_command_steps(full=full, artifact_dir=artifact_dir)
    python_steps = build_python_steps(full=full, artifact_dir=artifact_dir)

    failures = _run_step_batches(command_steps, run_command_step, max_workers=max_workers)
    completed_commands = {step.name for step in command_steps}
    failures += _run_step_batches(
        python_steps,
        run_python_step,
        max_workers=max_workers,
        completed_command_names=completed_commands,
    )
    return failures


__all__ = [
    "CommandStep",
    "DEFAULT_REVIEW_ARTIFACT_DIR",
    "MANUSCRIPT",
    "PROJECT_PDF_LOG",
    "PythonStep",
    "TEMPLATE_ROOT",
    "build_command_steps",
    "build_python_steps",
    "check_artifact_counts",
    "check_recursive_markdown",
    "check_recursive_prerender",
    "check_tracked_artifact_hygiene",
    "ready_step_names",
    "run_command_step",
    "run_publication_gate",
    "run_python_step",
]
