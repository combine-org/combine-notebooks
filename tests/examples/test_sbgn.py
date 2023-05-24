"""Test SBGN functionality."""
from pathlib import Path

import pytest

from combine_notebooks.examples import example_sbgn


@pytest.mark.skip(
    reason="Failure to communicate with sysbioapps.spdns.org; see https://github.com/combine-org/combine-notebooks/issues/26"
)
def test_create_repressilator_libsbgn(tmp_path: Path) -> None:
    """Test creation of repressilator SBGN with libsbgn."""
    sbgn_path: Path = tmp_path / "test.xml"
    doc = example_sbgn.create_repressilator(sbgn_path)
    assert doc
    assert sbgn_path.exists()
