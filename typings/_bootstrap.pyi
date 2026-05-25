"""Type stubs for script-local imports resolved at runtime via ``sys.path``."""

from pathlib import Path

PROJECT: Path
SRC: Path
SCRIPTS_DIR: Path

def ensure_project_paths(*, include_scripts: bool = False) -> Path: ...
def template_root() -> Path | None: ...
