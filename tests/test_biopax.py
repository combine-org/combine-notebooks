"""Test BioPax functionality."""
from pathlib import Path

import pytest

from combine_notebooks.examples import example_biopax


def test_create_repressilator_biopax(tmp_path: Path) -> None:
    """Test creation of repressilator with libsbml."""
    biopax_path: Path = tmp_path / "test.xml"
    doc = example_biopax.create_repressilator(biopax_path)
    assert doc
    assert biopax_path.exists()
