"""Test SBML functionality."""
from pathlib import Path

from sbmlutils.factory import FactoryResult

from combine_notebooks.examples import (
    example_sbml_antimony,
    example_sbml_libsbml,
    example_sbml_sbmlutils,
)


def test_create_repressilator_libsbml(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    sbml_path: Path = tmp_path / "test.xml"
    doc = example_sbml_libsbml.create_repressilator(sbml_path)
    assert doc
    assert sbml_path.exists()


def test_create_repressilator_sbmlutils(tmp_path: Path) -> None:
    """Test creation of repressilator with sbmlutils."""
    sbml_path: Path = tmp_path / "test.xml"
    results: FactoryResult = example_sbml_sbmlutils.create_repressilator(sbml_path)
    assert results
    assert results.sbml_path.exists()


def test_create_repressilator_antimony(tmp_path: Path) -> None:
    """Test creation of repressilator with antimony."""
    sbml_path: Path = tmp_path / "test.xml"
    doc = example_sbml_antimony.create_repressilator(sbml_path)
    assert doc
    assert sbml_path.exists()
