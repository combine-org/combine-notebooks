"""Runs all the example scripts and generates all COMBINE files."""
from pathlib import Path

from combine_notebooks.examples.example_biopax import create_repressilator as biopax
from combine_notebooks.examples.example_cellml import create_repressilator as cellml
from combine_notebooks.examples.example_omex import create_omex
from combine_notebooks.examples.example_sbgn import create_repressilator as sbgn
from combine_notebooks.examples.example_sbml_antimony import (
    create_repressilator as sbml_antimony,
)
from combine_notebooks.examples.example_sbml_libsbml import (
    create_repressilator as sbml_libsbml,
)
from combine_notebooks.examples.example_sbml_sbmlutils import (
    create_repressilator as sbml_sbmlutils,
)
from combine_notebooks.examples.example_sedml import create_repressilator as sedml


def create_combine_files(output_dir: Path) -> None:
    """Create all the COMBINE files."""
    biopax(biopax_path=output_dir / "repressilator_biopax.owl")
    cellml(cellml_path=output_dir / "repressilator_cellml.cellml")
    sbgn(sbgn_path=output_dir / "repressilator_sbgn.sbgn")
    sedml(sedml_path=output_dir / "repressilator_sedml.xml")
    sbml_antimony(sbml_path=output_dir / "repressilator_sbml_antimony.xml")
    sbml_libsbml(sbml_path=output_dir / "repressilator_sbml_libsbml.xml")
    sbml_sbmlutils(sbml_path=output_dir / "repressilator_sbml_sbmlutils.xml")


if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    create_combine_files(output_dir=RESULTS_DIR)
    create_omex(omex_path=RESULTS_DIR / "combine.omex", results_dir=RESULTS_DIR)
