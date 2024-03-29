"""combine_notebooks - COMBINE jupyter notebooks in python."""
from pathlib import Path

__version__ = "0.1.4"

BASE_DIR: Path = Path(__file__).parent.parent.parent
RESULTS_DIR: Path = BASE_DIR / "notebooks/results"
NOTEBOOK_DIR: Path = BASE_DIR / "notebooks"
EXAMPLE_DIR: Path = Path(__file__).parent / "examples"
GLYPH_DIR: Path = Path(__file__).parent / "sbol_visual_glyphs"
