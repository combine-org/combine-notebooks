"""Example for creating a combine archive."""

from combine_notebooks import RESULTS_DIR
from pymetadata.omex import Omex, ManifestEntry, EntryFormat
from pymetadata.console import console

# create new archive
omex = Omex()
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.SBML_L3V2,
        master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)

omex.to_omex(RESULTS_DIR / "combine_notebooks.omex")
