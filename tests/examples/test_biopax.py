"""Test BioPax functionality."""
from pathlib import Path

import pytest
from pybiopax.biopax.model import BioPaxModel

from combine_notebooks.examples import example_biopax


def test_create_repressilator_biopax(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    biopax_path: Path = tmp_path / "test.xml"

    model: BioPaxModel = example_biopax.create_repressilator(biopax_path)
    assert model
    assert biopax_path.exists()
