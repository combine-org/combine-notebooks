# %% [markdown]
# Create the repressilator step by step.

# See on biomodels.

# Add project directory to system path so that all project files can be imported
import os
import sys

# https://github.com/sbmlteam/libsbml
# %%
from pathlib import Path

import libsbml


module_path = os.path.abspath(os.path.join(".."))
if module_path not in sys.path:
    sys.path.append(module_path + "\\src\\")

from combine_notebooks.validation.validation_sbml import validate_sbml


# %% [markdown]

# # Helper Functions

# %%


def create_annotation(qualifier_type, biological_qualifier_type, resource):
    cv: libsbml.CVTerm = libsbml.CVTerm()
    cv.setQualifierType(qualifier_type)
    cv.setBiologicalQualifierType(biological_qualifier_type)
    cv.addResource(resource)
    return cv


def add_annotation_resource(cv, biological_qualifier_type, resource):
    cv.setBiologicalQualifierType(biological_qualifier_type)
    cv.addResource(resource)
    return cv


def add_compartment(model, id, size, meta_id, sbo_term):
    c: libsbml.Compartment = model.createCompartment()
    c.setId(id)
    c.setSize(size)
    c.setMetaId(meta_id)
    c.setSBOTerm(sbo_term)
    return c


def add_species(
    model,
    id,
    meta_id,
    compartment,
    name,
    sbo_term,
    initial_amount,
    has_only_substance_units,
):
    s: libsbml.Species = model.createSpecies()
    s.setId(id)
    s.setMetaId(meta_id)
    s.setCompartment(compartment)
    s.setName(name)
    s.setSBOTerm(sbo_term)
    s.setInitialAmount(initial_amount)
    s.setHasOnlySubstanceUnits(has_only_substance_units)
    return s


def add_parameters(model, id, name, constant, sbo_term=None, value=None):
    p: libsbml.Parameter = model.createParameter()
    p.setId(id)
    p.setName(name)
    p.setConstant(constant)
    if sbo_term is not None:
        p.setSBOTerm(sbo_term)
    if value is not None:
        p.setValue(value)


def add_assignment_rule(model, variable, l3_formaula):
    a: libsbml.AssignmentRule = model.createAssignmentRule()
    a.setVariable(variable)
    math_ast: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(l3_formaula, model)
    a.setMath(math_ast)


def add_reactions(
    model,
    id,
    meta_id,
    sbo_term,
    name,
    reversible,
    qualifier_type,
    biological_qualifier_type,
    resource,
    l3_formaula,
    kinetic_sbo_term,
):
    r: libsbml.Reaction = model.createReaction()
    r.setId(id),  # set reaction id
    r.setMetaId(meta_id)
    r.setSBOTerm(sbo_term)
    r.setName(name)
    r.setReversible(reversible)
    # set annotation
    r_cv: libsbml.CVTerm = libsbml.CVTerm()
    r_cv.setQualifierType(qualifier_type)
    r_cv.setBiologicalQualifierType(biological_qualifier_type)
    r_cv.addResource(resource)
    r.addCVTerm(r_cv)

    math_ast: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(l3_formaula, model)
    kinetic_law = r.createKineticLaw()
    if kinetic_sbo_term is not None:
        kinetic_law.setSBOTerm(kinetic_sbo_term)
    kinetic_law.setMath(math_ast)
    return r


def add_reactant_to_reaction(r, species):
    species_ref: libsbml.SpeciesReference = r.createReactant()
    species_ref.setSpecies(species)  # assign reactant species


def add_product_to_reaction(r, species):
    species_ref = r.createProduct()
    species_ref.setSpecies(species)  # assign product species


def add_modifier_to_reaction(r, species, sbo_term):
    species_ref = r.createModifier()
    species_ref.setSpecies(species)
    species_ref.setSBOTerm(sbo_term)


# %% [markdown]

# # Create SBML Model

# The following code builds a repressilator model in SBML.  To do this libSBML is used.  The repressilator is a genetic regulatory network consisting of at least one feedback loop with at least three genes, each expressing a protein that represses the next gene in the loop.  See the diagram below for a graphic respresentation of what we are building.

# <img src="https://raw.githubusercontent.com/combine-org/combine-notebooks/main/results/repressilator_sbgn.png" width="40%" height="40%" />

# %%


def create_repressilator(sbml_path: Path) -> libsbml.SBMLDocument:
    """Create repressilator."""
    print("Create SBML model")
    # create a new document

    doc: libsbml.SBMLDocument = libsbml.SBMLDocument(3, 2)
    model: libsbml.Model = doc.createModel()

    # --- compartments ---
    # add compartment and set annotation
    c1 = add_compartment(model, "cell", 1.0, "meta_cell", "SBO:0000290")
    c1_cv = create_annotation(
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS,
        "http://identifiers.org/GO:0005623",
    )
    c1.addCVTerm(c1_cv)

    # --- species ---
    # add species for the 3 mRNAs and 3 Proteins and set annotations
    s1 = add_species(model, "PX", "PX", "cell", "LacI protein", "SBO:0000252", 0, True)
    s1_cv = create_annotation(
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS,
        "http://identifiers.org/uniprot/P03023",
    )
    s1.addCVTerm(s1_cv)

    s2 = add_species(model, "PY", "PY", "cell", "TetR protein", "SBO:0000252", 0, True)
    s2_cv = create_annotation(
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS,
        "http://identifiers.org/uniprot/P04483",
    )
    s2.addCVTerm(s2_cv)

    s3 = add_species(model, "PZ", "PZ", "cell", "cI protein", "SBO:0000252", 0, True)
    s3_cv = create_annotation(
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS,
        "http://identifiers.org/uniprot/P03034",
    )
    # example setting a model qualifier
    # s3_cv.setQualifierType(libsbml.MODEL_QUALIFIER)
    # s3_cv.setBiologicalQualifierType(libsbml.BQM_IS)
    s3.addCVTerm(s3_cv)

    s4 = add_species(model, "X", "meta_X", "cell", "LacI mRNA", "SBO:0000250", 0, True)
    s4_cv = create_annotation(
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/CHEBI:33699",
    )
    s4_cv = add_annotation_resource(
        s4_cv, libsbml.BQB_IS_VERSION_OF, "http://identifiers.org/kegg.compound/C00046"
    )
    s4.addCVTerm(s4_cv)
    s4_cv = add_annotation_resource(
        s4_cv, libsbml.BQB_ENCODES, "http://identifiers.org/uniprot/P03023"
    )
    s4.addCVTerm(s4_cv)

    s5 = add_species(model, "Y", "meta_Y", "cell", "TetR mRNA", "SBO:0000250", 20, True)
    s5_cv = create_annotation(
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/CHEBI:33699",
    )
    s5_cv = add_annotation_resource(
        s5_cv, libsbml.BQB_IS_VERSION_OF, "http://identifiers.org/kegg.compound/C00046"
    )
    s5.addCVTerm(s5_cv)
    s5_cv = add_annotation_resource(
        s5_cv, libsbml.BQB_ENCODES, "http://identifiers.org/uniprot/P04483"
    )
    s5.addCVTerm(s5_cv)

    s6 = add_species(model, "Z", "meta_Z", "cell", "cl mRNA", "SBO:0000250", 0, True)
    s6_cv = create_annotation(
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/CHEBI:33699",
    )
    s6_cv = add_annotation_resource(
        s6_cv, libsbml.BQB_IS_VERSION_OF, "http://identifiers.org/kegg.compound/C00046"
    )
    s6.addCVTerm(s6_cv)
    s6_cv = add_annotation_resource(
        s6_cv, libsbml.BQB_ENCODES, "http://identifiers.org/uniprot/P03034"
    )
    s6.addCVTerm(s6_cv)

    # --- parameters ---
    # <parameter id="tau_mRNA" name="mRNA half life" value="2" constant="true"/>
    add_parameters(model, "tau_mRNA", "mRNA half life", True, value=2.0)
    # <parameter id="kd_mRNA" constant="false" name="kd_mRNA" sboTerm="SBO:0000356">
    add_parameters(model, "kd_mRNA", "kd_mRNA", False, sbo_term="SBO:0000356")
    # <parameter metaid="metaid_0000233" sboTerm="SBO:0000016" id="k_tl" name="k_tl" constant="false">
    add_parameters(model, "k_tl", "k_tl", False, sbo_term="SBO:0000016")
    # <parameter metaid="metaid_0000025" id="eff" name="translation efficiency" value="20">
    add_parameters(model, "eff", "translation efficiency", True, value=20)
    # <parameter metaid="metaid_0000032" sboTerm="SBO:0000348" id="t_ave" name="average mRNA life time" constant="false"/>
    add_parameters(
        model, "t_ave", "average mRNA life time", False, sbo_term="SBO:0000348"
    )
    # <parameter metaid="metaid_0000133" sboTerm="SBO:0000356" id="kd_prot" name="kd_prot" constant="false">
    add_parameters(model, "kd_prot", "kd_prot", False, sbo_term="SBO:0000356")
    # <parameter metaid="metaid_0000128" sboTerm="SBO:0000332" id="tau_prot" name="protein half life" value="10"/>
    add_parameters(model, "tau_prot", "protien half life", True, value=10)
    # <parameter metaid="metaid_0000234" sboTerm="SBO:0000485" id="a0_tr" name="a0_tr" constant="false">
    add_parameters(model, "a0_tr", "a0_tr", False, sbo_term="SBO:0000485")
    # <parameter metaid="metaid_0500235" sboTerm="SBO:0000485" id="ps_0" name="tps_repr" value="0.0005">
    add_parameters(model, "ps_0", "tps_repr", True, value=0.0005)
    # <parameter metaid="metaid_0900235" sboTerm="SBO:0000186" id="a_tr" name="a_tr" constant="false">
    add_parameters(model, "a_tr", "a_tr", False, sbo_term="SBO:0000186")
    # <parameter metaid="metaid_0800235" sboTerm="SBO:0000186" id="ps_a" name="tps_active" value="0.5">
    add_parameters(model, "ps_a", "tps_active", True, value=0.5)
    # <parameter metaid="metaid_0000027" sboTerm="SBO:0000288" id="KM" name="KM" value="40">
    add_parameters(model, "KM", "KM", True, value=40)
    # <parameter metaid="metaid_0000026" sboTerm="SBO:0000190" id="n" name="n" value="2">
    add_parameters(model, "n", "n", True, value=2.0)

    # TODO: a0_tr, a_tr, n, KM

    # --- rules ---
    add_assignment_rule(model, "kd_mRNA", "ln(2) / tau_mRNA")
    add_assignment_rule(model, "t_ave", "tau_mRNA / ln(2)")
    add_assignment_rule(model, "k_tl", "eff / t_ave")
    add_assignment_rule(model, "kd_prot", "ln(2) / tau_prot")
    add_assignment_rule(model, "a0_tr", "ps_0 * 60")
    add_assignment_rule(model, "a_tr", "(ps_a - ps_0) * 60")

    # --- reaction ---
    # X -> None
    r1 = add_reactions(
        model,
        "Reaction1",
        "meta_Reaction1",
        "SBO:0000179",
        "degradation of LacI transcripts",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006402",
        "kd_mRNA * X",
        "SBO:0000049",
    )
    add_reactant_to_reaction(r1, "X")

    r2 = add_reactions(
        model,
        "Reaction2",
        "meta_Reaction2",
        "SBO:0000179",
        "degradation of TetR transcripts",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006402",
        "kd_mRNA * Y",
        "SBO:0000049",
    )
    add_reactant_to_reaction(r2, "Y")

    r3 = add_reactions(
        model,
        "Reaction3",
        "meta_Reaction3",
        "SBO:0000179",
        "degradation of CI transcripts",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006402",
        "kd_mRNA * Z",
        "SBO:0000049",
    )
    add_reactant_to_reaction(r3, "Z")

    r4 = add_reactions(
        model,
        "Reaction4",
        "meta_Reaction4",
        "SBO:0000184",
        "translation of LacI",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006412",
        "k_tl * X",
        "SBO:0000049",
    )
    add_product_to_reaction(r4, "PX")
    add_modifier_to_reaction(r4, "X", "SBO:0000461")

    r5 = add_reactions(
        model,
        "Reaction5",
        "meta_Reaction5",
        "SBO:0000184",
        "translation of TetR",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006412",
        "k_tl * Y",
        "SBO:0000049",
    )
    add_product_to_reaction(r5, "PY")
    add_modifier_to_reaction(r5, "Y", "SBO:0000461")

    r6 = add_reactions(
        model,
        "Reaction6",
        "meta_Reaction6",
        "SBO:0000184",
        "translation of CI",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006412",
        "k_tl * Z",
        "SBO:0000049",
    )
    add_product_to_reaction(r6, "PZ")
    add_modifier_to_reaction(r6, "Z", "SBO:0000461")

    r7 = add_reactions(
        model,
        "Reaction7",
        "meta_Reaction7",
        "SBO:0000179",
        "degradation of LacI",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0030163",
        "kd_prot * PX",
        "SBO:0000049",
    )
    add_reactant_to_reaction(r7, "PX")

    r8 = add_reactions(
        model,
        "Reaction8",
        "meta_Reaction8",
        "SBO:0000179",
        "degradation of TetR",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0030163",
        "kd_prot * PY",
        "SBO:0000049",
    )
    add_reactant_to_reaction(r8, "PY")

    r9 = add_reactions(
        model,
        "Reaction9",
        "meta_Reaction9",
        "SBO:0000179",
        "degradation of CI",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0030163",
        "kd_prot * PZ",
        "SBO:0000049",
    )
    add_reactant_to_reaction(r9, "PZ")

    r10 = add_reactions(
        model,
        "Reaction10",
        "meta_Reaction10",
        "SBO:0000183",
        "transcription of LacI",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006351",
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))",
        None,
    )
    add_product_to_reaction(r10, "X")
    add_modifier_to_reaction(r10, "PZ", "SBO:0000536")

    r11 = add_reactions(
        model,
        "Reaction11",
        "meta_Reaction11",
        "SBO:0000183",
        "transcription of TetR",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006351",
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PX, n))",
        None,
    )
    add_product_to_reaction(r11, "Y")
    add_modifier_to_reaction(r11, "PX", "SBO:0000536")

    r12 = add_reactions(
        model,
        "Reaction12",
        "meta_Reaction12",
        "SBO:0000183",
        "transcription of CI",
        False,
        libsbml.BIOLOGICAL_QUALIFIER,
        libsbml.BQB_IS_VERSION_OF,
        "http://identifiers.org/GO:0006351",
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PY, n))",
        None,
    )
    add_product_to_reaction(r12, "Z")
    add_modifier_to_reaction(r12, "PY", "SBO:0000536")

    print("-" * 80)
    print(libsbml.writeSBMLToString(doc))
    print("-" * 80)

    # write to file
    libsbml.writeSBMLToFile(doc, str(sbml_path))

    # validate file
    validate_sbml(doc, units_consistency=False)

    return doc


# %%
if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    # RESOURCES_DIR: Path = Path(__file__).parent / "resources"
    # RESULTS_DIR: Path = RESOURCES_DIR / "results"
    doc: libsbml.SBMLDocument = create_repressilator(
        sbml_path=RESULTS_DIR / "repressilator_libsbml.xml"
    )
