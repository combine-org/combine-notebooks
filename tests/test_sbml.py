"""Import creation of repressilator in SBML."""
from pathlib import Path

import pytest
from sbmlutils.factory import FactoryResult

from combine_notebooks import example_antimony, example_libsbml, example_sbmlutils


def test_create_repressilator_libsbml(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    sbml_path: Path = tmp_path / "test.xml"
    doc = example_libsbml.create_repressilator(sbml_path)
    assert doc
    assert sbml_path.exists()


def test_create_repressilator_sbmlutils(tmp_path: Path) -> None:
    """Test creation of repressilator with sbmlutils."""
    sbml_path: Path = tmp_path / "test.xml"
    results: FactoryResult = example_sbmlutils.create_repressilator(sbml_path)
    assert results
    assert results.sbml_path.exists()

def test_create_repressilator_antimony(tmp_path: Path) -> None:
    """Test creation of repressilator with antimony."""
    sbml_path: Path = tmp_path / "test.xml"
    doc = example_antimony.create_repressilator(sbml_path)
    assert doc
    assert sbml_path.exists()
