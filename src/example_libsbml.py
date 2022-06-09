"""
Create the repressilator step by step.
See on biomodels.
"""


from pathlib import Path

import libsbml

print("Create SBML model")
# create a new document

doc: libsbml.SBMLDocument = libsbml.SBMLDocument(3, 2)
model: libsbml.Model = doc.createModel()

# add compartment


# add species for the 3 mRNAs and 3 Proteins

# add kinetic laws

print("-" * 80)
print(libsbml.writeSBMLToString(doc))
print("-" * 80)

# writing to file

results_dir: Path = Path(__file__).parent / "results"
results_dir.mkdir(exist_ok=True)
libsbml.writeSBMLToFile(doc, str(results_dir / "repressilator.xml"))