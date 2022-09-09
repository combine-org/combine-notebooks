"""Test SBGN functionality."""
from pathlib import Path

from combine_notebooks.examples import example_libsbgn


def test_create_repressilator_libsbgn(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    sbgn_path: Path = tmp_path / "test.xml"
    doc = example_libsbgn.create_repressilator(sbgn_path)
    assert doc
    assert sbgn_path.exists()
