from pathlib import Path

PROJECT = Path(__file__).resolve().parents[3]
MANUSCRIPT = PROJECT / "docs" / "manuscript"
SRC = PROJECT / "src"
TEMPLATE_ROOT = PROJECT.parent.parent
