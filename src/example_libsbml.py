"""
Create the repressilator step by step.
See on biomodels.
"""

from pathlib import Path

import libsbml
from libsbml import *


def create_repressilator():
    print("Create SBML model")
    # create a new document

    doc: libsbml.SBMLDocument = libsbml.SBMLDocument(2, 3)
    model: libsbml.Model = doc.createModel()

    # --- compartments ---
    # add compartment
    c1: libsbml.Compartment = model.createCompartment()
    c1.setId("cell")
    c1.setSize(1.0)
    c1.setSBOTerm("SBO:0000290")

    # --- species ---
    # add species for the 3 mRNAs and 3 Proteins
    s1: libsbml.Species = model.createSpecies()
    s1.setId("PX")
    s1.setCompartment("cell")
    s1.setName("LacI protein")
    s1.setSBOTerm("SBO:0000252")
    s1.setInitialAmount(0)
    s1.setHasOnlySubstanceUnits(True)

    s2: libsbml.Species = model.createSpecies()
    s2.setId("PY")
    s2.setCompartment("cell")
    s2.setName("TetR protein")
    s2.setSBOTerm("SBO:0000252")
    s2.setInitialAmount(0)
    s2.setHasOnlySubstanceUnits(True)

    s3: libsbml.Species = model.createSpecies()
    s3.setId("PZ")
    s3.setCompartment("cell")
    s3.setName("cI protein")
    s3.setSBOTerm("SBO:0000252")
    s3.setInitialAmount(0)
    s3.setHasOnlySubstanceUnits(True)

    s4: libsbml.Species = model.createSpecies()
    s4.setId("X")
    s4.setCompartment("cell")
    s4.setName("Lacl mRNA")
    s4.setSBOTerm("SBO:0000250")
    s4.setInitialAmount(0)
    s4.setHasOnlySubstanceUnits(True)

    s5: libsbml.Species = model.createSpecies()
    s5.setId("Y")
    s5.setCompartment("cell")
    s5.setName("TetR mRNA")
    s5.setSBOTerm("SBO:0000250")
    s5.setInitialAmount(20)
    s5.setHasOnlySubstanceUnits(True)

    s6: libsbml.Species = model.createSpecies()
    s6.setId("Z")
    s6.setCompartment("cell")
    s6.setName("cl mRNA")
    s6.setSBOTerm("SBO:0000250")
    s6.setInitialAmount(0)
    s6.setHasOnlySubstanceUnits(True)

    # --- parameters ---
    parameters_info = [
        {"id": "tau_mRNA", "name": "mRNA half life"},
    ]

    # <parameter id="kd_mRNA" constant="false" name="kd_mRNA" sboTerm="SBO:0000356">
    p1: libsbml.Parameter = model.createParameter()
    p1.setId("tau_mRNA")
    p1.setName("mRNA half life")
    p1.setConstant(True)
    p1.setValue(2.0)

    # <parameter id="kd_mRNA" constant="false" name="kd_mRNA" sboTerm="SBO:0000356">
    p2: libsbml.Parameter = model.createParameter()
    p2.setId("kd_mRNA")
    p2.setName("kd_mRNA")
    p2.setSBOTerm("SBO:0000356")
    p2.setConstant(False)

    # TODO: a0_tr, a_tr, n, KM

    # --- rules ---
    a1: libsbml.AssignmentRule = model.createAssignmentRule()
    a1.setVariable("kd_MRNA")
    math_ast: libsbml.ASTNode = libsbml.parseL3FormulaWithModel('ln(2) / tau_mRNA', model)
    a1.setMath(math_ast)

    # --- reaction ---
    # X -> None
    r1: libsbml.Reaction = model.createReaction()
    r1.setId('Reaction1'),  # set reaction id
    r1.setSBOTerm("SBO:0000179")
    r1.setName("degradation of LacI transcripts")
    r1.setReversible(False)


    species_ref1: libsbml.SpeciesReference = r1.createReactant()
    species_ref1.setSpecies('X')  # assign reactant species

    math_ast: libsbml.ASTNode = libsbml.parseL3FormulaWithModel('kd_mRNA * X', model)
    kinetic_law = r1.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast)


    # r2 = model.createReaction()
    # r2.setId('Reaction2'),  # set reaction id
    # r2.setSBOTerm("SBO:0000179")
    # r2.setName("degradation of TetR transcripts")
    # r2.setReversible(False)
    # species_ref2 = r2.createReactant()
    # species_ref2.setSpecies('Y')  # assign reactant species
    # math_ast = libsbml.parseL3Formula('kd_mRNA * Y')
    # kinetic_law = r2.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    # r3 = model.createReaction()
    # r3.setId('Reaction3'),  # set reaction id
    # r3.setSBOTerm("SBO:0000179")
    # r3.setName("degradation of CI transcripts")
    # r3.setReversible(False)
    # species_ref3 = r3.createReactant()
    # species_ref3.setSpecies('Z')  # assign reactant species
    # math_ast = libsbml.parseL3Formula('kd_mRNA * Z')
    # kinetic_law = r3.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    # r4 = model.createReaction()
    # r4.setId('Reaction4'),  # set reaction id
    # r4.setSBOTerm("SBO:0000184")
    # r4.setName("translation of LacI")
    # r4.setReversible(False)
    # species_ref4 = r4.createProduct()
    # species_ref4.setSpecies('PX')  # assign product species
    # species_ref_4 = r4.createModifier()
    # species_ref_4.setSpecies('X')
    # species_ref_4.setSBOTerm("SBO:0000461")
    # math_ast = libsbml.parseL3Formula('k_tl * X')
    # kinetic_law = r4.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    # r5 = model.createReaction()
    # r5.setId('Reaction5'),  # set reaction id
    # r5.setSBOTerm("SBO:0000184")
    # r5.setName("translation of TetR")
    # r5.setReversible(False)
    # species_ref5 = r5.createProduct()
    # species_ref5.setSpecies('PY')  # assign product species
    # species_ref_5 = r5.createModifier()
    # species_ref_5.setSpecies('Y')
    # species_ref_5.setSBOTerm("SBO:0000461")
    # math_ast = libsbml.parseL3Formula('k_tl * Y')
    # kinetic_law = r5.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    # r6 = model.createReaction()
    # r6.setId('Reaction6'),  # set reaction id
    # r6.setSBOTerm("SBO:0000184")
    # r6.setName("translation of CI")
    # r6.setReversible(False)
    # species_ref6 = r6.createProduct()
    # species_ref6.setSpecies('PZ')  # assign product species
    # species_ref_6 = r6.createModifier()
    # species_ref_6.setSpecies('Z')
    # species_ref_6.setSBOTerm("SBO:0000461")
    # math_ast = libsbml.parseL3Formula('k_tl * Z')
    # kinetic_law = r6.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    # r7 = model.createReaction()
    # r7.setId('Reaction7'),  # set reaction id
    # r7.setSBOTerm("SBO:0000179")
    # r7.setName("degradation of LacI")
    # r7.setReversible(False)
    # species_ref7 = r7.createReactant()
    # species_ref7.setSpecies('PX')  # assign reactant species
    # math_ast = libsbml.parseL3Formula('kd_prot * PX')
    # kinetic_law = r7.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    # r8 = model.createReaction()
    # r8.setId('Reaction8'),  # set reaction id
    # r8.setSBOTerm("SBO:0000179")
    # r8.setName("degradation of TetR")
    # r8.setReversible(False)
    # species_ref8 = r8.createReactant()
    # species_ref8.setSpecies('PY')  # assign reactant species
    # math_ast = libsbml.parseL3Formula('kd_prot * PY')
    # kinetic_law = r8.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    # r9 = model.createReaction()
    # r9.setId('Reaction9'),  # set reaction id
    # r9.setSBOTerm("SBO:0000179")
    # r9.setName("degradation of CI")
    # r9.setReversible(False)
    # species_ref9 = r9.createReactant()
    # species_ref9.setSpecies('PZ')  # assign reactant species
    # math_ast = libsbml.parseL3Formula('kd_prot * PZ')
    # kinetic_law = r9.createKineticLaw()
    # kinetic_law.setSBOTerm("SBO:0000049")
    # kinetic_law.setMath(math_ast)
    #
    r10 = model.createReaction()
    r10.setId('Reaction10'),  # set reaction id
    r10.setSBOTerm("SBO:0000183")
    r10.setName("transcription of LacI")
    r10.setReversible(False)
    species_ref10 = r10.createProduct()
    species_ref10.setSpecies('X')  # assign product species
    species_ref_10 = r10.createModifier()
    species_ref_10.setSpecies('PZ')
    species_ref_10.setSBOTerm("SBO:0000536")
    kinetic_law = r10.createKineticLaw()
    math_ast: libsbml.ASTNode = libsbml.parseL3FormulaWithModel('a0_tr + (a_tr * power(KM, 2) / (power(KM, 2) + power(PZ, 2))', model)

    # r11 = model.createReaction()
    # r11.setId('Reaction11'),  # set reaction id
    # r11.setSBOTerm("SBO:0000183")
    # r11.setName("transcription of TetR")
    # r11.setReversible(False)
    # species_ref11 = r11.createProduct()
    # species_ref11.setSpecies('Y')  # assign product species
    # species_ref_11 = r11.createModifier()
    # species_ref_11.setSpecies('PX')
    # species_ref_11.setSBOTerm("SBO:0000536")
    #
    # r12 = model.createReaction()
    # r12.setId('Reaction12'),  # set reaction id
    # r12.setSBOTerm("SBO:0000183")
    # r12.setName("transcription of CI")
    # r12.setReversible(False)
    # species_ref12 = r12.createProduct()
    # species_ref12.setSpecies('Z')  # assign product species
    # species_ref_12 = r12.createModifier()
    # species_ref_12.setSpecies('PY')
    # species_ref_12.setSBOTerm("SBO:0000536")

    print("-" * 80)
    print(libsbml.writeSBMLToString(doc))
    print("-" * 80)

    # writing to file

    results_dir: Path = Path(__file__).parent / "results"
    results_dir.mkdir(exist_ok=True)
    libsbml.writeSBMLToFile(doc, str(results_dir / "repressilator.xml"))


def validate_model():
    pass


if __name__ == '__main__':
    create_repressilator()
