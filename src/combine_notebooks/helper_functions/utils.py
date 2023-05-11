"""Helper functions for constructing SBML model."""

from typing import Callable, Optional

import libsbml


def run_if_not_none(function: Callable, value: object) -> None:
    """Run a setter method if and only if the given value is not None."""
    if value is not None:
        function(value)


def create_annotation(
    qualifier_type: int, biological_qualifier_type: int, resource: str
) -> libsbml.CVTerm:
    """
    Create an annotation, but this will not be automatically be added to a model.

    Annotations can be used for adding metadata to models and model component.
    """
    cv: libsbml.CVTerm = libsbml.CVTerm()
    cv.setQualifierType(qualifier_type)
    cv.setBiologicalQualifierType(biological_qualifier_type)
    cv.addResource(resource)
    return cv


def add_annotation_resource(
    cv: libsbml.CVTerm, biological_qualifier_type: int, resource: str
) -> libsbml.CVTerm:
    """
    Add a resource to an existing annotation.

    See
    https://registry.identifiers.org/registry for available resources.
    """
    cv.setBiologicalQualifierType(biological_qualifier_type)
    cv.addResource(resource)
    return cv


def add_compartment(
    model: libsbml.Model, id: str, size: float, meta_id: str, sbo_term: str
) -> libsbml.Compartment:
    """
    Create a compartment and adds to an existing model.

    A compartment in SBML
    represents a bounded space in which species are located.
    """
    c: libsbml.Compartment = model.createCompartment()
    c.setId(id)
    c.setSize(size)
    c.setMetaId(meta_id)
    c.setSBOTerm(sbo_term)
    return c


def add_species(
    model: libsbml.Model,
    id: str,
    meta_id: str,
    compartment: str,
    name: str,
    sbo_term: str,
    initial_amount: int,
    has_only_substance_units: bool,
) -> libsbml.Species:
    """
    Create a species and adds to an existing model.

    A species in SBML refers to a pool
    of entities that (a) are considered indistinguishable from each other for the
    purposes of the model, (b) participate in reactions, and (c) are located in a
    specific compartment.
    """
    s: libsbml.Species = model.createSpecies()
    s.setId(id)
    s.setMetaId(meta_id)
    s.setCompartment(compartment)
    s.setName(name)
    s.setSBOTerm(sbo_term)
    s.setInitialAmount(initial_amount)
    s.setHasOnlySubstanceUnits(has_only_substance_units)
    return s


def add_parameters(
    model: libsbml.Model,
    id: str,
    name: str,
    constant: bool,
    sbo_term: Optional[str] = None,
    value: Optional[float] = None,
) -> None:
    """
    Create a parameters and adds to an existing model.

    A Parameter is used in SBML to
    define a symbol associated with a value; this symbol can then be used in
    mathematical formulas in a model.
    """
    p: libsbml.Parameter = model.createParameter()
    p.setId(id)
    p.setName(name)
    p.setConstant(constant)
    run_if_not_none(p.setSBOTerm, sbo_term)
    run_if_not_none(p.setValue, value)


def add_assignment_rule(model: libsbml.Model, variable: str, l3_formaula: str) -> None:
    """
    Create an assignment rule and adds to an existing model.

    An assignment rule is used
    to express equations that set the values of variables.
    """
    a: libsbml.AssignmentRule = model.createAssignmentRule()
    a.setVariable(variable)
    math_ast: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(l3_formaula, model)
    a.setMath(math_ast)


def add_reactions(
    model: libsbml.Model,
    id: str,
    meta_id: str,
    sbo_term: str,
    name: str,
    reversible: bool,
    qualifier_type: int,
    biological_qualifier_type: int,
    resource: str,
    l3_formaula: str,
    kinetic_sbo_term: Optional[str],
) -> libsbml.Reaction:
    """
    Create a reactions and a corresponding resource.

    These are then added to an existing model.
    A reaction represents any transformation, transport or binding process,
    typically a chemical reaction, that can change the quantity of one or more species.
    """
    r: libsbml.Reaction = model.createReaction()
    r.setId(id),  # set reaction id
    r.setMetaId(meta_id)
    r.setSBOTerm(sbo_term)
    r.setName(name)
    r.setReversible(reversible)
    # set annotation
    r_cv = create_annotation(qualifier_type, biological_qualifier_type, resource)
    r.addCVTerm(r_cv)

    math_ast: libsbml.ASTNode = libsbml.parseL3FormulaWithModel(l3_formaula, model)
    kinetic_law = r.createKineticLaw()
    run_if_not_none(kinetic_law.setSBOTerm, kinetic_sbo_term)
    kinetic_law.setMath(math_ast)
    return r


def add_reactant_to_reaction(r: libsbml.Reaction, species: str) -> None:
    """Add a reactant to a pre defined reaction."""
    species_ref: libsbml.SpeciesReference = r.createReactant()
    species_ref.setSpecies(species)  # assign reactant species


def add_product_to_reaction(r: libsbml.Reaction, species: str) -> None:
    """Add a product_ to a pre defined reaction."""
    species_ref = r.createProduct()
    species_ref.setSpecies(species)  # assign product species


def add_modifier_to_reaction(r: libsbml.Reaction, species: str, sbo_term: str) -> None:
    """Add a modifier to a pre defined reaction."""
    species_ref = r.createModifier()
    species_ref.setSpecies(species)
    species_ref.setSBOTerm(sbo_term)
