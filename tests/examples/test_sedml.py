"""Test SED-ML functionality."""
from pathlib import Path

from combine_notebooks.examples.repressilator import example_sedml


def test_create_repressilator_cellml(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    sedml_path: Path = tmp_path / "test.xml"
    doc = example_sedml.create_repressilator(sedml_path)
    assert doc
    assert sedml_path.exists()
