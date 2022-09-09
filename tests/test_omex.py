"""Test OMEX functionality."""
from pathlib import Path

from combine_notebooks.examples.example_omex import create_omex
from combine_notebooks.create_combine_files import create_combine_files


def test_create_repressilator_omex(tmp_path: Path) -> None:
    """Test creation of COMBINE archive."""
    create_combine_files(tmp_path)
    omex_path: Path = tmp_path / "test.omex"

    create_omex(omex_path=omex_path, results_dir=tmp_path)
    assert omex_path.exists()

