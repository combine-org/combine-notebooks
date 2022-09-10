"""Test creation of notebooks."""
from pathlib import Path

from combine_notebooks import EXAMPLE_DIR
from combine_notebooks.convert_notebooks import create_notebooks


def test_create_notebooks(tmp_path: Path) -> None:
    """Test creation of notebooks with nbconvert."""
    create_notebooks(input_dir=EXAMPLE_DIR, output_dir=tmp_path)
