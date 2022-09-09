"""Validation from libsbgn-python.

see https://github.com/matthiaskoenig/libsbgn-python/blob/develop/src/libsbgnpy/validation/validator.py
"""
from libsbgnpy.validation.validator import validate_schematron, validate_xsd

from combine_notebooks import RESULTS_DIR


f_sbgn = str(RESULTS_DIR / "repressilator_sbgn.sbgn")
# f = "error-test-files/PD/pd10101-pass.sbgn"
# f = "../examples/sbgn/glycolysis.sbgn"

xsd_valid = validate_xsd(f_sbgn) is None
print("XSD valid ({}): {}".format(f_sbgn, xsd_valid))
