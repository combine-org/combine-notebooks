"""Test OMEX functionality."""
from pathlib import Path

from combine_notebooks.combine_files import create_combine_files
from combine_notebooks.examples.repressilator.example_omex import create_omex


def test_create_repressilator_omex(tmp_path: Path) -> None:
    """Test creation of COMBINE archive."""
    create_combine_files(tmp_path)
    omex_path: Path = tmp_path / "test.omex"

    create_omex(omex_path=omex_path, results_dir=tmp_path)
    assert omex_path.exists()
