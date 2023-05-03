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
            location="./sbml/hello_world_sbml.xml",
            format=EntryFormat.SBML_L3V2,
            master=False,
        ),
        entry_path=results_dir / "hello_world_sbml.xml",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./cellml/hello_world_cellml.cellml",
            format=EntryFormat.CELLML,
            master=False,
        ),
        entry_path=results_dir / "hello_world_cellml.cellml",
    )

    """omex.add_entry(
        entry=ManifestEntry(
            location="./biopax/repressilator_biopax.owl",
            format=EntryFormat.BIOPAX,
            master=False,
        ),
        entry_path=results_dir / "repressilator_biopax.owl",
    )"""

    omex.add_entry(
        entry=ManifestEntry(
            location="./sbgn/hello_world_sbgn.sbgn",
            format=EntryFormat.SBGN,
            master=False,
        ),
        entry_path=results_dir / "hello_world_sbgn.sbgn",
    )
    omex.add_entry(
        entry=ManifestEntry(
            location="./sbgn/hello_world_sbgn.png",
            format=EntryFormat.PNG,
            master=False,
        ),
        entry_path=results_dir / "hello_world_sbgn.png",
    )

    omex.add_entry(
        entry=ManifestEntry(
            location="./sedml/hello_world_sedml.sedml",
            format=EntryFormat.SEDML,
            master=False,
        ),
        entry_path=results_dir / "hello_world_sedml.sedml"
        # FIXME: add the model relative and test
    )

    console.print(omex)
    omex.to_omex(omex_path)
    
# <codecell>

if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    create_omex(omex_path=RESULTS_DIR / "combine_hello_world.omex", results_dir=RESULTS_DIR)

        # <markdowncell>
# -


