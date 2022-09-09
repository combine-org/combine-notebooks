# <markdowncell>

# Example for creating a COMBINE archive.

# <codecell>
from pathlib import Path

from pymetadata.console import console
from pymetadata.omex import EntryFormat, ManifestEntry, Omex


# <markdowncell>

# Creating an empty archive and adding entry for SBML.


# <codecell>


def create_omex(omex_path: Path, results_dir: Path) -> None:
    """Create OMEX archive of resources."""
    omex = Omex()
    omex.add_entry(
        entry=ManifestEntry(
            location="./sbml/repressilator_sbml_libsbml.xml",
            format=EntryFormat.SBML_L3V2,
            master=False,
        ),
        entry_path=results_dir / "repressilator_sbml_libsbml.xml",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./sbml/repressilator_sbml_antimony.xml",
            format=EntryFormat.SBML_L3V2,
            master=False,
        ),
        entry_path=results_dir / "repressilator_sbml_antimony.xml",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./sbml/repressilator_sbml_sbmlutils.xml",
            format=EntryFormat.SBML_L3V2,
            master=False,
        ),
        entry_path=results_dir / "repressilator_sbml_sbmlutils.xml",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./cellml/repressilator_cellml.cellml",
            format=EntryFormat.CELLML,
            master=False,
        ),
        entry_path=results_dir / "repressilator_cellml.cellml",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./biopax/repressilator_biopax.owl",
            format=EntryFormat.BIOPAX,
            master=False,
        ),
        entry_path=results_dir / "repressilator_biopax.owl",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./sbgn/repressilator_sbgn.sbgn",
            format=EntryFormat.SBGN,
            master=False,
        ),
        entry_path=results_dir / "repressilator_sbgn.sbgn",
    )
    omex.add_entry(
        entry=ManifestEntry(
            location="./sbgn/repressilator_sbgn.png",
            format=EntryFormat.PNG,
            master=False,
        ),
        entry_path=results_dir / "repressilator_sbgn.png",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./sedml/repressilator_sedml.xml",
            format=EntryFormat.SEDML,
            master=False,
        ),
        entry_path=results_dir / "repressilator_sedml.xml"
        # FIXME: add the model relative and test
    )

    console.print(omex)
    omex.to_omex(omex_path)


if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    create_omex(omex_path=RESULTS_DIR / "combine.omex", results_dir=RESULTS_DIR)
