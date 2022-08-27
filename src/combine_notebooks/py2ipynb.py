from nbformat import v3, v4
from pathlib import Path
RESOURCES_DIR: Path = Path(__file__).parent / "resources"
RESULTS_DIR: Path = RESOURCES_DIR / "results"

with open(Path(__file__).parent/"example_sedml.py") as fpin:
    text = fpin.read()
text += """
# <markdowncell>

# If you can read this, reads_py() is no longer broken! 
"""
nbook = v3.reads_py(text)
nbook = v4.upgrade(nbook)  # Upgrade v3 to v4

jsonform = v4.writes(nbook) + "\n"
with open(RESULTS_DIR/"output-file-sedml.ipynb", "w") as fpout:
    fpout.write(jsonform)