"""Load orphan citation insertion catalog from YAML."""

from __future__ import annotations

from pathlib import Path

import yaml

from biology.citations import OrphanCitationInsertion
from biology.maintenance.models import PROJECT

CATALOG_PATH = Path(__file__).resolve().parent / "orphan_citations.yaml"
_REQUIRED_FIELDS = ("citekey", "target", "anchor")


def load_orphan_citation_insertions(
    catalog_path: Path = CATALOG_PATH,
    *,
    manuscript_root: Path = PROJECT / "manuscript",
) -> tuple[OrphanCitationInsertion, ...]:
    """Parse the YAML catalog into ``OrphanCitationInsertion`` records."""
    raw = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    rows = (raw or {}).get("insertions", [])
    out: list[OrphanCitationInsertion] = []
    for row in rows:
        missing = [field for field in _REQUIRED_FIELDS if field not in row]
        if missing:
            raise ValueError(f"orphan_citations.yaml row missing fields {missing}: {row}")
        out.append(
            OrphanCitationInsertion(
                citekey=str(row["citekey"]),
                target=manuscript_root / row["target"],
                anchor=str(row["anchor"]),
                form=str(row.get("form", "citep")),
                prefix=str(row.get("prefix", "")),
                replace_with=str(row.get("replace_with", "")),
            )
        )
    return tuple(out)


__all__ = ["CATALOG_PATH", "load_orphan_citation_insertions"]
