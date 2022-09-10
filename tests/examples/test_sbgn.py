"""Test SBGN functionality."""
from pathlib import Path

from combine_notebooks.examples import example_sbgn


def test_create_repressilator_libsbgn(tmp_path: Path) -> None:
    """Test creation of repressilator SBGN with libsbgn."""
    sbgn_path: Path = tmp_path / "test.xml"
    doc = example_sbgn.create_repressilator(sbgn_path)
    assert doc
    assert sbgn_path.exists()
