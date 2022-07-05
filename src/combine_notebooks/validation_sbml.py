"""Validation function."""
from typing import List

import libsbml


def validate_sbml(doc: libsbml.SBMLDocument, units_consistency: bool = False) -> None:
    """Validate sbml."""
    # set the unit checking, similar for the other settings
    doc.setConsistencyChecks(libsbml.LIBSBML_CAT_UNITS_CONSISTENCY, units_consistency)
    doc.checkConsistency()
    # get errors/warnings
    n_errors: int = doc.getNumErrors()
    errors: List[libsbml.SBMLError] = list()
    warnings: List[libsbml.SBMLError] = list()
    for k in range(n_errors):
        error: libsbml.SBMLError = doc.getError(k)
        severity = error.getSeverity()
        if (severity == libsbml.LIBSBML_SEV_ERROR) or (
            severity == libsbml.LIBSBML_SEV_FATAL
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
