"""Replay the reviewed Unit 0 flowcharts with a browser-free renderer."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory
from xml.etree import ElementTree as ET

from .verify import verify_flowchart

TOOLS = Path(__file__).resolve().parent
CHAPTERS = ("systems_science", "complex_adaptive_systems", "active_inference")
FENCE = re.compile(r"^```mermaid\n(.*?)^```$", re.MULTILINE | re.DOTALL)


def checksum(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replay_flowcharts(unit: Path, destination: Path) -> None:
    """Replay unchanged audited inputs and record source and asset hashes."""
    if not __debug__:
        raise RuntimeError("Flowchart verification requires Python assertions")
    expected = {
        name: digest
        for digest, name in map(
            str.split, (TOOLS / "sources.sha256").read_text().splitlines()
        )
    }
    sources = {}
    for chapter in CHAPTERS:
        text = (unit / f"{chapter}.md").read_text(encoding="utf-8")
        for index, diagram in enumerate(FENCE.findall(text), 1):
            sources[f"{chapter}-{index}.mmd"] = diagram
    if sources.keys() != expected.keys():
        raise ValueError("The diagram roster differs from the reviewed Unit 0 sources")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(
        prefix=".unit0-flowcharts-", dir=destination.parent
    ) as temporary:
        staging = Path(temporary)
        for name, source in sources.items():
            path = staging / name
            path.write_text(source, encoding="utf-8")
            if checksum(path) != expected[name]:
                raise ValueError(f"Unreviewed Mermaid change in {name}")
        subprocess.run(["node", str(TOOLS / "render.mjs"), str(staging)], check=True)
        manifest = {}
        for name in sorted(sources):
            path = staging / name
            svg = path.with_suffix(".svg")
            png = path.with_suffix(".png")
            root = ET.parse(svg).getroot()
            axis = (
                "width"
                if float(root.attrib["width"]) >= float(root.attrib["height"])
                else "height"
            )
            subprocess.run(
                [
                    "inkscape",
                    f"--export-{axis}=1600",
                    "--export-background=white",
                    f"--export-filename={png}",
                    str(svg),
                ],
                check=True,
            )
            stats = verify_flowchart(path)
            manifest[name] = {
                "source_sha256": expected[name],
                "svg_sha256": checksum(svg),
                "png_sha256": checksum(png),
                **stats,
            }
            path.with_suffix(".json").unlink()
        (staging / "manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )
        # Reserve the requested path without overwriting any existing destination.
        destination.mkdir()
        try:
            for artifact in staging.iterdir():
                artifact.rename(destination / artifact.name)
        except OSError:
            for artifact in destination.iterdir():
                artifact.unlink()
            destination.rmdir()
            raise
