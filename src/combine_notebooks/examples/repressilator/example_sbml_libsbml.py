# <markdowncell>
# Create the repressilator step by step.

# See on biomodels.

# https://github.com/sbmlteam/libsbml
# <codecell>
from pathlib import Path

import libsbml

from combine_notebooks.validation.validation_sbml import validate_sbml


# <codecell>


def create_repressilator(sbml_path: Path) -> libsbml.SBMLDocument:
    """Create repressilator."""
    print("Create SBML model")
    # create a new document

    doc: libsbml.SBMLDocument = libsbml.SBMLDocument(3, 2)
    model: libsbml.Model = doc.createModel()

    # --- compartments ---
    # add compartment
    c1: libsbml.Compartment = model.createCompartment()
    c1.setId("cell")
    c1.setSize(1.0)
    c1.setMetaId("meta_cell")
    c1.setSBOTerm("SBO:0000290")
    # set annotation
    c1_cv: libsbml.CVTerm = libsbml.CVTerm()
    c1_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    c1_cv.setBiologicalQualifierType(libsbml.BQB_IS)
    c1_cv.addResource("http://identifiers.org/GO:0005623")
    c1.addCVTerm(c1_cv)

    # --- species ---
    # add species for the 3 mRNAs and 3 Proteins
    s1: libsbml.Species = model.createSpecies()
    s1.setId("PX")
    s1.setMetaId("PX")
    s1.setCompartment("cell")
    s1.setName("LacI protein")
    s1.setSBOTerm("SBO:0000252")
    s1.setInitialAmount(0)
    s1.setHasOnlySubstanceUnits(True)
    # set annotation
    s1_cv: libsbml.CVTerm = libsbml.CVTerm()
    s1_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    s1_cv.setBiologicalQualifierType(libsbml.BQB_IS)
    s1_cv.addResource("http://identifiers.org/uniprot/P03023")
    s1.addCVTerm(s1_cv)

    s2: libsbml.Species = model.createSpecies()
    s2.setId("PY")
    s2.setMetaId("PY")
    s2.setCompartment("cell")
    s2.setName("TetR protein")
    s2.setSBOTerm("SBO:0000252")
    s2.setInitialAmount(0)
    s2.setHasOnlySubstanceUnits(True)
    # set annotation
    s2_cv: libsbml.CVTerm = libsbml.CVTerm()
    s2_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    s2_cv.setBiologicalQualifierType(libsbml.BQB_IS)
    s2_cv.addResource("http://identifiers.org/uniprot/P04483")
    s2.addCVTerm(s2_cv)

    s3: libsbml.Species = model.createSpecies()
    s3.setId("PZ")
    s3.setMetaId("PZ")
    s3.setCompartment("cell")
    s3.setName("cI protein")
    s3.setSBOTerm("SBO:0000252")
    s3.setInitialAmount(0)
    s3.setHasOnlySubstanceUnits(True)
    # set annotation
    s3_cv: libsbml.CVTerm = libsbml.CVTerm()
    s3_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    s3_cv.setBiologicalQualifierType(libsbml.BQB_IS)
    # example setting a model qualifier
    # s3_cv.setQualifierType(libsbml.MODEL_QUALIFIER)
    # s3_cv.setBiologicalQualifierType(libsbml.BQM_IS)
    s3_cv.addResource("http://identifiers.org/uniprot/P03034")
    s3.addCVTerm(s3_cv)

    s4: libsbml.Species = model.createSpecies()
    s4.setId("X")
    s4.setMetaId("meta_X")
    s4.setCompartment("cell")
    s4.setName("LacI mRNA")
    s4.setSBOTerm("SBO:0000250")
    s4.setInitialAmount(0)
    s4.setHasOnlySubstanceUnits(True)
    # set annotation
    s4_cv: libsbml.CVTerm = libsbml.CVTerm()
    s4_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    s4_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    s4_cv.addResource("http://identifiers.org/CHEBI:33699")
    s4_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    s4_cv.addResource("http://identifiers.org/kegg.compound/C00046")
    s4.addCVTerm(s4_cv)
    s4_cv.setBiologicalQualifierType(libsbml.BQB_ENCODES)
    s4_cv.addResource("http://identifiers.org/uniprot/P03023")
    s4.addCVTerm(s4_cv)

    s5: libsbml.Species = model.createSpecies()
    s5.setId("Y")
    s5.setMetaId("meta_Y")
    s5.setCompartment("cell")
    s5.setName("TetR mRNA")
    s5.setSBOTerm("SBO:0000250")
    s5.setInitialAmount(20)
    s5.setHasOnlySubstanceUnits(True)
    # set annotation
    s5_cv: libsbml.CVTerm = libsbml.CVTerm()
    s5_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    s5_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    s5_cv.addResource("http://identifiers.org/CHEBI:33699")
    s5_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    s5_cv.addResource("http://identifiers.org/kegg.compound/C00046")
    s5.addCVTerm(s5_cv)
    s5_cv.setBiologicalQualifierType(libsbml.BQB_ENCODES)
    s5_cv.addResource("http://identifiers.org/uniprot/P04483")
    s5.addCVTerm(s5_cv)

    s6: libsbml.Species = model.createSpecies()
    s6.setId("Z")
    s6.setMetaId("meta_Z")
    s6.setCompartment("cell")
    s6.setName("cl mRNA")
    s6.setSBOTerm("SBO:0000250")
    s6.setInitialAmount(0)
    s6.setHasOnlySubstanceUnits(True)
    # set annotation
    s6_cv: libsbml.CVTerm = libsbml.CVTerm()
    s6_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    s6_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    s6_cv.addResource("http://identifiers.org/CHEBI:33699")
    s6_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    s6_cv.addResource("http://identifiers.org/kegg.compound/C00046")
    s6.addCVTerm(s6_cv)
    s6_cv.setBiologicalQualifierType(libsbml.BQB_ENCODES)
    s6_cv.addResource("http://identifiers.org/uniprot/P03034")
    s6.addCVTerm(s6_cv)

    # --- parameters ---
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

    # <parameter metaid="metaid_0000233" sboTerm="SBO:0000016" id="k_tl" name="k_tl" constant="false">
    p3: libsbml.Parameter = model.createParameter()
    p3.setId("k_tl")
    p3.setName("k_tl")
    p3.setSBOTerm("SBO:0000016")
    p3.setConstant(False)

    # <parameter metaid="metaid_0000025" id="eff" name="translation efficiency" value="20">
    p4: libsbml.Parameter = model.createParameter()
    p4.setId("eff")
    p4.setName("translation efficiency")
    p4.setConstant(True)
    p4.setValue(20)

    # <parameter metaid="metaid_0000032" sboTerm="SBO:0000348" id="t_ave" name="average mRNA life time" constant="false"/>
    p5: libsbml.Parameter = model.createParameter()
    p5.setId("t_ave")
    p5.setName("average mRNA life time")
    p5.setSBOTerm("SBO:0000348")
    p5.setConstant(False)

    # <parameter metaid="metaid_0000133" sboTerm="SBO:0000356" id="kd_prot" name="kd_prot" constant="false">
    p6: libsbml.Parameter = model.createParameter()
    p6.setId("kd_prot")
    p6.setName("kd_prot")
    p6.setSBOTerm("SBO:0000356")
    p6.setConstant(False)

    # <parameter metaid="metaid_0000128" sboTerm="SBO:0000332" id="tau_prot" name="protein half life" value="10"/>
    p7: libsbml.Parameter = model.createParameter()
    p7.setId("tau_prot")
    p7.setName("protien half life")
    p7.setConstant(True)
    p7.setValue(10)

    # <parameter metaid="metaid_0000234" sboTerm="SBO:0000485" id="a0_tr" name="a0_tr" constant="false">
    p8: libsbml.Parameter = model.createParameter()
    p8.setId("a0_tr")
    p8.setName("a0_tr")
    p8.setSBOTerm("SBO:0000485")
    p8.setConstant(False)

    # <parameter metaid="metaid_0500235" sboTerm="SBO:0000485" id="ps_0" name="tps_repr" value="0.0005">
    p9: libsbml.Parameter = model.createParameter()
    p9.setId("ps_0")
    p9.setName("tps_repr")
    p9.setConstant(True)
    p9.setValue(0.0005)

    # <parameter metaid="metaid_0900235" sboTerm="SBO:0000186" id="a_tr" name="a_tr" constant="false">
    p10: libsbml.Parameter = model.createParameter()
    p10.setId("a_tr")
    p10.setName("a_tr")
    p10.setSBOTerm("SBO:0000186")
    p10.setConstant(False)

    # <parameter metaid="metaid_0800235" sboTerm="SBO:0000186" id="ps_a" name="tps_active" value="0.5">
    p11: libsbml.Parameter = model.createParameter()
    p11.setId("ps_a")
    p11.setName("tps_active")
    p11.setConstant(True)
    p11.setValue(0.5)

    # <parameter metaid="metaid_0000027" sboTerm="SBO:0000288" id="KM" name="KM" value="40">
    p12: libsbml.Parameter = model.createParameter()
    p12.setId("KM")
    p12.setName("KM")
    p12.setConstant(True)
    p12.setValue(40)

    # <parameter metaid="metaid_0000026" sboTerm="SBO:0000190" id="n" name="n" value="2">
    p13: libsbml.Parameter = model.createParameter()
    p13.setId("n")
    p13.setName("n")
    p13.setConstant(True)
    p13.setValue(2.0)

    # TODO: a0_tr, a_tr, n, KM

    # --- rules ---
    a1: libsbml.AssignmentRule = model.createAssignmentRule()
    a1.setVariable("kd_mRNA")
    math_ast1: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(
        "ln(2) / tau_mRNA", model
    )
    a1.setMath(math_ast1)

    a2: libsbml.AssignmentRule = model.createAssignmentRule()
    a2.setVariable("t_ave")
    math_ast2: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(
        "tau_mRNA / ln(2)", model
    )
    a2.setMath(math_ast2)

    a3: libsbml.AssignmentRule = model.createAssignmentRule()
    a3.setVariable("k_tl")
    math_ast3: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("eff / t_ave", model)
    a3.setMath(math_ast3)

    a4: libsbml.AssignmentRule = model.createAssignmentRule()
    a4.setVariable("kd_prot")
    math_ast4: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(
        "ln(2) / tau_prot", model
    )
    a4.setMath(math_ast4)

    a5: libsbml.AssignmentRule = model.createAssignmentRule()
    a5.setVariable("a0_tr")
    math_ast5: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("ps_0 * 60", model)
    a5.setMath(math_ast5)

    a6: libsbml.AssignmentRule = model.createAssignmentRule()
    a6.setVariable("a_tr")
    math_ast6: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(
        "(ps_a - ps_0) * 60", model
    )
    a6.setMath(math_ast6)

    # --- reaction ---
    # X -> None
    r1: libsbml.Reaction = model.createReaction()
    r1.setId("Reaction1"),  # set reaction id
    r1.setMetaId("meta_Reaction1")
    r1.setSBOTerm("SBO:0000179")
    r1.setName("degradation of LacI transcripts")
    r1.setReversible(False)
    # set annotation
    r1_cv: libsbml.CVTerm = libsbml.CVTerm()
    r1_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r1_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r1_cv.addResource("http://identifiers.org/GO:0006402")
    r1.addCVTerm(r1_cv)

    species_ref1: libsbml.SpeciesReference = r1.createReactant()
    species_ref1.setSpecies("X")  # assign reactant species

    math_ast7: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("kd_mRNA * X", model)
    kinetic_law = r1.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast7)

    r2 = model.createReaction()
    r2.setId("Reaction2"),  # set reaction id
    r2.setMetaId("meta_Reaction2")
    r2.setSBOTerm("SBO:0000179")
    r2.setName("degradation of TetR transcripts")
    r2.setReversible(False)

    r2_cv: libsbml.CVTerm = libsbml.CVTerm()
    r2_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r2_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r2_cv.addResource("http://identifiers.org/GO:0006402")
    r2.addCVTerm(r1_cv)

    species_ref2 = r2.createReactant()
    species_ref2.setSpecies("Y")  # assign reactant species

    math_ast8: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("kd_mRNA * Y", model)
    kinetic_law = r2.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast8)

    r3 = model.createReaction()
    r3.setId("Reaction3"),  # set reaction id
    r3.setMetaId("meta_Reaction3")
    r3.setSBOTerm("SBO:0000179")
    r3.setName("degradation of CI transcripts")
    r3.setReversible(False)
    # set annotation
    r3_cv: libsbml.CVTerm = libsbml.CVTerm()
    r3_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r3_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r3_cv.addResource("http://identifiers.org/GO:0006402")
    r3.addCVTerm(r3_cv)

    species_ref3 = r3.createReactant()
    species_ref3.setSpecies("Z")  # assign reactant species

    math_ast9: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("kd_mRNA * Z", model)
    kinetic_law = r3.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast9)

    r4 = model.createReaction()
    r4.setId("Reaction4"),  # set reaction id
    r4.setMetaId("meta_Reaction4")
    r4.setSBOTerm("SBO:0000184")
    r4.setName("translation of LacI")
    r4.setReversible(False)
    # set annotation
    r4_cv: libsbml.CVTerm = libsbml.CVTerm()
    r4_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r4_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r4_cv.addResource("http://identifiers.org/GO:0006412")
    r4.addCVTerm(r4_cv)

    species_ref4 = r4.createProduct()
    species_ref4.setSpecies("PX")  # assign product species

    species_ref_4 = r4.createModifier()
    species_ref_4.setSpecies("X")
    species_ref_4.setSBOTerm("SBO:0000461")

    math_ast10: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("k_tl * X", model)
    kinetic_law = r4.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast10)

    r5 = model.createReaction()
    r5.setId("Reaction5"),  # set reaction id
    r5.setMetaId("meta_Reaction5")
    r5.setSBOTerm("SBO:0000184")
    r5.setName("translation of TetR")
    r5.setReversible(False)
    s3_cv = libsbml.CVTerm()
    # set annotation
    r5_cv: libsbml.CVTerm = libsbml.CVTerm()
    r5_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r5_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r5_cv.addResource("http://identifiers.org/GO:0006412")
    r5.addCVTerm(r5_cv)

    species_ref5 = r5.createProduct()
    species_ref5.setSpecies("PY")  # assign product species
    species_ref_5 = r5.createModifier()
    species_ref_5.setSpecies("Y")
    species_ref_5.setSBOTerm("SBO:0000461")

    math_ast11: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("k_tl * Y", model)
    kinetic_law = r5.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast11)

    r6 = model.createReaction()
    r6.setId("Reaction6"),  # set reaction id
    r6.setMetaId("meta_Reaction6")
    r6.setSBOTerm("SBO:0000184")
    r6.setName("translation of CI")
    r6.setReversible(False)
    # set annotation
    r6_cv: libsbml.CVTerm = libsbml.CVTerm()
    r6_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r6_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r6_cv.addResource("http://identifiers.org/GO:0006412")
    r6.addCVTerm(r6_cv)

    species_ref6 = r6.createProduct()
    species_ref6.setSpecies("PZ")  # assign product species
    species_ref_6 = r6.createModifier()
    species_ref_6.setSpecies("Z")
    species_ref_6.setSBOTerm("SBO:0000461")

    math_ast12: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("k_tl * Z", model)
    kinetic_law = r6.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast12)

    r7 = model.createReaction()
    r7.setId("Reaction7"),  # set reaction id
    r7.setMetaId("meta_Reaction7")
    r7.setSBOTerm("SBO:0000179")
    r7.setName("degradation of LacI")
    r7.setReversible(False)
    # set annotation
    r7_cv: libsbml.CVTerm = libsbml.CVTerm()
    r7_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r7_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r7_cv.addResource("http://identifiers.org/GO:0030163")
    r7.addCVTerm(r7_cv)

    species_ref7 = r7.createReactant()
    species_ref7.setSpecies("PX")  # assign reactant species

    math_ast13: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("kd_prot * PX", model)
    kinetic_law = r7.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast13)

    r8 = model.createReaction()
    r8.setId("Reaction8"),  # set reaction id
    r8.setMetaId("meta_Reaction8")
    r8.setSBOTerm("SBO:0000179")
    r8.setName("degradation of TetR")
    r8.setReversible(False)
    # set annotation
    r8_cv: libsbml.CVTerm = libsbml.CVTerm()
    r8_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r8_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r8_cv.addResource("http://identifiers.org/GO:0030163")
    r8.addCVTerm(r8_cv)

    species_ref8 = r8.createReactant()
    species_ref8.setSpecies("PY")  # assign reactant species

    math_ast14: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("kd_prot * PY", model)
    kinetic_law = r8.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast14)

    r9 = model.createReaction()
    r9.setId("Reaction9"),  # set reaction id
    r9.setMetaId("meta_Reaction9")
    r9.setSBOTerm("SBO:0000179")
    r9.setName("degradation of CI")
    r9.setReversible(False)
    # set annotation
    r9_cv: libsbml.CVTerm = libsbml.CVTerm()
    r9_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r9_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r9_cv.addResource("http://identifiers.org/GO:0030163")
    r9.addCVTerm(r9_cv)

    species_ref9 = r9.createReactant()
    species_ref9.setSpecies("PZ")  # assign reactant species

    math_ast15: libsbml.ASTNode = libsbml.parseL3FormulaWithModel("kd_prot * PZ", model)
    kinetic_law = r9.createKineticLaw()
    kinetic_law.setSBOTerm("SBO:0000049")
    kinetic_law.setMath(math_ast15)

    r10 = model.createReaction()
    r10.setId("Reaction10"),  # set reaction id
    r10.setMetaId("meta_Reaction10")
    r10.setSBOTerm("SBO:0000183")
    r10.setName("transcription of LacI")
    r10.setReversible(False)
    # set annotation
    r10_cv: libsbml.CVTerm = libsbml.CVTerm()
    r10_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r10_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r10_cv.addResource("http://identifiers.org/GO:0006351")
    r10.addCVTerm(r10_cv)

    species_ref10 = r10.createProduct()
    species_ref10.setSpecies("X")  # assign product species
    species_ref_10 = r10.createModifier()
    species_ref_10.setSpecies("PZ")
    species_ref_10.setSBOTerm("SBO:0000536")

    math_ast16: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))", model
    )
    kinetic_law = r10.createKineticLaw()
    kinetic_law.setMath(math_ast16)

    r11 = model.createReaction()
    r11.setId("Reaction11"),  # set reaction id
    r11.setMetaId("meta_Reaction11")
    r11.setSBOTerm("SBO:0000183")
    r11.setName("transcription of TetR")
    r11.setReversible(False)
    # set annotation
    r11_cv: libsbml.CVTerm = libsbml.CVTerm()
    r11_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r11_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r11_cv.addResource("http://identifiers.org/GO:0006351")
    r11.addCVTerm(r11_cv)

    species_ref11 = r11.createProduct()
    species_ref11.setSpecies("Y")  # assign product species
    species_ref_11 = r11.createModifier()
    species_ref_11.setSpecies("PX")
    species_ref_11.setSBOTerm("SBO:0000536")

    math_ast17: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PX, n))", model
    )
    kinetic_law = r11.createKineticLaw()
    kinetic_law.setMath(math_ast17)

    r12 = model.createReaction()
    r12.setId("Reaction12"),  # set reaction id
    r12.setMetaId("meta_Reaction12")
    r12.setSBOTerm("SBO:0000183")
    r12.setName("transcription of CI")
    r12.setReversible(False)
    # set annotation
    r12_cv: libsbml.CVTerm = libsbml.CVTerm()
    r12_cv.setQualifierType(libsbml.BIOLOGICAL_QUALIFIER)
    r12_cv.setBiologicalQualifierType(libsbml.BQB_IS_VERSION_OF)
    r12_cv.addResource("http://identifiers.org/GO:0006351")
    r12.addCVTerm(r12_cv)

    species_ref12 = r12.createProduct()
    species_ref12.setSpecies("Z")  # assign product species
    species_ref_12 = r12.createModifier()
    species_ref_12.setSpecies("PY")
    species_ref_12.setSBOTerm("SBO:0000536")

    math_ast18: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PY, n))", model
    )
    kinetic_law = r12.createKineticLaw()
    kinetic_law.setMath(math_ast18)

    print("-" * 80)
    print(libsbml.writeSBMLToString(doc))
    print("-" * 80)

    # write to file
    libsbml.writeSBMLToFile(doc, str(sbml_path))

    # validate file
    validate_sbml(doc, units_consistency=False)

    return doc


# <codecell>
if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    # RESOURCES_DIR: Path = Path(__file__).parent / "resources"
    # RESULTS_DIR: Path = RESOURCES_DIR / "results"
    doc: libsbml.SBMLDocument = create_repressilator(
        sbml_path=RESULTS_DIR / "repressilator_libsbml.xml"
    )
