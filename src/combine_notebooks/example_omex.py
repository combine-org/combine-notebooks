# <markdowncell>

# Example for creating a COMBINE archive.

# <codecell>
# from pathlib import Path
from pymetadata.console import console
from pymetadata.omex import EntryFormat, ManifestEntry, Omex

from combine_notebooks import RESULTS_DIR

# <markdowncell>

# Creating an empty archive and adding entry for SBML.


# <codecell>
# create new archive
omex = Omex()
omex.add_entry(
    entry=ManifestEntry(
        location="./sbml/repressilator_libsbml.xml", format=EntryFormat.SBML_L3V2, master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_libsbml.xml"
)

# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./sbml/repressilator_antimony.xml", format=EntryFormat.SBML_L3V2, master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_antimony.xml"
)

# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./sbml/repressilator_sbmlutils.xml", format=EntryFormat.SBML_L3V2, master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_sbmlutils.xml"
)

# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./cellml/repressilator.cellml", format=EntryFormat.CELLML, master=False
    ),
    entry_path=RESULTS_DIR / "repressilator.cellml"
)

# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./biopax/biopax.owl", format=EntryFormat.BIOPAX, master=False
    ),
    entry_path=RESULTS_DIR / "biopax.owl"
)

# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./sbgn/repressilator_sbgn.sbgn", format=EntryFormat.SBGN, master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_sbgn.sbgn"
)

# <codecell>
omex.add_entry(
    entry=ManifestEntry(
        location="./sedml/repressilator_sedml.xml", format=EntryFormat.SEDML, master=False
    ),
    entry_path=RESULTS_DIR / "repressilator_sedml.xml"
    # FIXME: add the model relative and test
)

# <codecell>
console.print(omex)
omex.to_omex(RESULTS_DIR / "combine_notebooks.omex")
