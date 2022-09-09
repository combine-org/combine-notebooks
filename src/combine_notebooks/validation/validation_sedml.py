"""Validation function."""
from typing import List

import libsedml

from combine_notebooks import RESULTS_DIR


def validate_sedml(doc: libsedml.SedDocument) -> None:
    """Validate SED-ML."""
    # set the unit checking, similar for the other settings

    n_errors: int = doc.getNumErrors()
    errors: List[libsedml.SedError] = list()
    warnings: List[libsedml.SedError] = list()
    for k in range(n_errors):
        error: libsedml.SedError = doc.getError(k)
        severity = error.getSeverity()
        if (severity == libsedml.LIBSEDML_SEV_ERROR) or (
            severity == libsedml.LIBSEDML_SEV_FATAL
        ):
            errors.append(error)
        else:
            warnings.append(error)
    # print results
    print("-" * 80)
    print(f"{'validation error(s)':<25}: {len(errors)}")
    print(f"{'validation warning(s)':<25}: {len(warnings)}")
    if len(errors) > 0:
        print("--- errors ---")
        for kerr in enumerate(errors):
            print(f"E{kerr}: {error.getCategoryAsString()} L{error.getLine()}")
            print(
                f"[{error.getSeverityAsString()}] {error.getShortMessage()} | {error.getMessage()}"
            )
    if len(warnings) > 0:
        print("--- warnings ---")
        for kwarn in enumerate(warnings):
            print(f"E{kwarn}: {error.getCategoryAsString()} L{error.getLine()}")
            print(
                f"[{error.getSeverityAsString()}] {error.getShortMessage()} | {error.getMessage()}"
            )
    print("-" * 80)


if __name__ == "__main__":

    doc: libsedml.SedDocument = libsedml.readSedMLFromFile(
        str(RESULTS_DIR / "repressilator_sedml.xml")
    )
    validate_sedml(doc)
