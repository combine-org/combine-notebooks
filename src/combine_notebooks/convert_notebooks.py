"""Convert python files to notebooks."""

from pathlib import Path
from typing import List

from nbformat import v3, v4


def create_notebooks(input_dir: Path, output_dir: Path) -> List[Path]:
    """Create notebooks for all COMBINE examples.

    Returns list of notebook paths.
    """
    module_paths = input_dir.glob("**/*.py")
    notebook_paths: List[Path] = []
    for module_path in module_paths:
        if "__init__" in str(module_path):
            continue
        if "example_neuroml" in str(module_path):
            continue
        if "example_sbol" in str(module_path):
            continue

        with open(module_path) as f_module:
            text = f_module.read()

        # add empty markdowncell to ensure last cell is written
        text += """
        # <markdowncell>
        """

        # conversion
        nbook = v3.reads_py(text)
        nbook = v4.upgrade(nbook)

        # write notebook
        notebook_path = output_dir / f"{module_path.stem}.ipynb"
        with open(notebook_path, "w") as f_notebook:
            f_notebook.write(v4.writes(nbook) + "\n")
        notebook_paths.append(notebook_path)

    return notebook_paths


if __name__ == "__main__":
    from combine_notebooks import EXAMPLE_DIR, NOTEBOOK_DIR

    notebook_paths = create_notebooks(input_dir=EXAMPLE_DIR, output_dir=NOTEBOOK_DIR)
    print(notebook_paths)
