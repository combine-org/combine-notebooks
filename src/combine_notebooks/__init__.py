"""combine_notebooks - COMBINE jupyter notebooks in python."""
from pathlib import Path

__version__ = "0.1.1"

BASE_DIR: Path = Path(__file__).parent.parent.parent
RESULTS_DIR: Path = BASE_DIR / "results"
NOTEBOOK_DIR: Path = BASE_DIR / "notebooks"
EXAMPLE_DIR: Path = Path(__file__).parent / "examples"
