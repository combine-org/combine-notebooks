# <markdowncell>

# Example for creating a combine archive.
# <codecell>
# from pathlib import Path
from combine_notebooks import RESULTS_DIR
# RESOURCES_DIR: Path = Path(__file__).parent
# RESULTS_DIR: Path = RESOURCES_DIR / "results"
from pymetadata.omex import Omex, ManifestEntry, EntryFormat
from pymetadata.console import console
# <codecell>
# create new archive
omex = Omex()
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.SBML_L3V2,
        master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
    # entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)
# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.SBML_L3V2,
        master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_antimony.xml"
    # entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)
# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.SBML_L3V2,
        master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_sbmlutils.xml"
    # entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)
# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.CELLML,
        master=False
    ),
    entry_path=RESULTS_DIR / "repressilator.cellml"
    # entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)
# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.BIOPAX,
        master=False
    ),
    entry_path=RESULTS_DIR / "biopax.owl"
    # entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)
# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.SBGN,
        master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_sbgn.sbgn"
    # entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)
# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./repressilator.xml",
        format=EntryFormat.SEDML,
        master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_sedml.xml"
    # entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)
console.print(omex)
# <codecell>
omex.to_omex(RESULTS_DIR / "combine_notebooks.omex")
