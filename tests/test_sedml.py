"""Test SED-ML functionality."""
from pathlib import Path

import pytest
from sbmlutils.factory import FactoryResult

from combine_notebooks import example_sedml


def test_create_repressilator_cellml(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    sedml_path: Path = tmp_path / "test.xml"
    doc = example_sedml.create_dependent_variable_example(sedml_path)
    assert doc
    assert sedml_path.exists()
