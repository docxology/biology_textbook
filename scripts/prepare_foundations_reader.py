"""Export selected textbook passages and their references into a new reader project."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "docs/manuscript"
CHAPTER = MANUSCRIPT / "unit_0/history_philosophy_biology.md"
SECTIONS = (
    "Opening Vignette: Darwin, Wallace, and Evidence Before an Audience",
    "Biology as Practice: Instruments, Organisms, and Arguments",
    "Models, Evidence, and Explanation",
)
CITATION = re.compile(r"\\citep\{([^{}]+)\}")
INTRO = """# History, evidence, and models in biology

This foundations reader reproduces three passages from Daniel Ari Friedman's
*Introduction to Biology: A Generative Approach*, edition 1.1, with their cited sources.
It covers biological history and reasoning from evidence. The working textbook and
the prior release (DOI 10.5281/zenodo.20286478) have their own publication records.
The selection and cover art are provided under CC BY 4.0.

![Original textbook cover showing molecules, a cell, a leafy stem, and an ecological network.](../../output/figures/biology_textbook_cover.png)

![Historical events including Hooke’s microscopy, the presentation of natural selection, and the rise of molecular biology, positioned by year.](../../output/figures/biology_milestones.png)
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New output directory")
    parser.add_argument(
        "--unit0-flowcharts",
        action="store_true",
        help="Replay the 11 reviewed Unit 0 flowcharts without building a reader",
    )
    args = parser.parse_args()
    destination = args.destination
    if destination.exists() or destination.is_symlink():
        parser.error("destination must be a new path")

    if args.unit0_flowcharts:
        destination = destination.resolve()
        if (ROOT / "output") not in destination.parents:
            parser.error(
                "flowchart output must be inside this checkout's output directory"
            )
        from unit0_flowcharts import replay_flowcharts

        replay_flowcharts(MANUSCRIPT / "unit_0", destination)
        return

    chapter = CHAPTER.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^#{1,2} (.+)$", chapter, re.MULTILINE))
    passages = []
    for title in SECTIONS:
        section_index, heading = next(
            (index, item) for index, item in enumerate(headings) if item[1] == title
        )
        passage = chapter[heading.start() : headings[section_index + 1].start()].strip()
        passages.append(passage.removesuffix("---").rstrip())
    selected = "\n\n".join(passages)
    keys = {key for match in CITATION.findall(selected) for key in match.split(",")}
    bibliography = (MANUSCRIPT / "references.bib").read_text(encoding="utf-8")
    records = {
        match[1]: match[0]
        for match in re.finditer(r"^@\w+\{([^,]+),.*?^\}", bibliography, re.MULTILINE | re.DOTALL)
        if match[1] in keys
    }
    missing = keys.difference(records)
    if missing:
        raise ValueError(f"Missing references: {sorted(missing)}")

    source = destination / "docs/manuscript"
    figures = destination / "output/figures"
    source.mkdir(parents=True)
    figures.mkdir(parents=True)
    shutil.copyfile(MANUSCRIPT / "reader/config.yaml", source / "config.yaml")
    shutil.copyfile(
        MANUSCRIPT / "assets/cover/biology_textbook_cover.png",
        figures / "biology_textbook_cover.png",
    )
    (source / "01_reader.md").write_text(
        INTRO + "\n" + CITATION.sub(lambda match: "[" + "; ".join(
            f"@{key}" for key in match[1].split(",")
        ) + "]", selected) + "\n",
        encoding="utf-8",
    )
    (source / "references.bib").write_text("\n\n".join(records.values()) + "\n", encoding="utf-8")

    os.environ.setdefault("MPLBACKEND", "Agg")
    sys.path.insert(0, str(ROOT / "src"))
    from visualization.plots_foundations import plot_biology_milestones

    plot_biology_milestones(figures)


if __name__ == "__main__":
    main()
