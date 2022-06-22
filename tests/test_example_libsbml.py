from pathlib import Path

import pytest

from combine_notebooks.example_libsbml import create_repressilator


def test_create_repressilator(tmp_path):
    sbml_path: Path = tmp_path / "test_repressilator"
    doc = create_repressilator(sbml_path)
    assert doc
    assert sbml_path.exists()
