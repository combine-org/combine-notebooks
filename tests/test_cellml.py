"""Test CellML functionality."""
from pathlib import Path

import pytest
from sbmlutils.factory import FactoryResult

from combine_notebooks import example_cellml


def test_create_repressilator_cellml(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    cellml_path: Path = tmp_path / "test.xml"
    doc = example_cellml.create_model(cellml_path)
    assert doc
    assert cellml_path.exists()
