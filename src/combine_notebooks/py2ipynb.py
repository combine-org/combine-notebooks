"""Convert python files to notebooks."""

from pathlib import Path

from nbformat import v3, v4

import codecs
import ntpath
RESOURCES_DIR: Path = Path(__file__).parent
RESULTS_DIR: Path = RESOURCES_DIR / "notebooks"

# files = Path(RESOURCES_DIR).glob('*')
l=list(RESOURCES_DIR.glob('**/*.py'))
for file in l:

    # if file.endswith(".py"):
    # with open(Path(__file__).parent / file, 'r', encoding='utf-8',
    #                  errors='ignore') as fpin:
    with open(file) as fpin:
        text = fpin.read()
    text += """
    # <markdowncell>

    # If you can read this, reads_py() is no longer broken!
    """
    nbook = v3.reads_py(text)
    nbook = v4.upgrade(nbook)  # Upgrade v3 to v4

    jsonform = v4.writes(nbook) + "\n"
    filename=str(ntpath.basename(file))+".ipynb"
    filename=RESULTS_DIR / filename
    print(filename)
    with open(filename, "w") as fpout:
        fpout.write(jsonform)
