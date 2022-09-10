# <markdowncell>
# Biological Pathway Exchange (BioPAX) is a standard language that aims to enable integration, exchange, visualization and analysis of biological pathway data. Specifically, BioPAX supports data exchange between pathway data groups and thus reduces the complexity of interchange between data formats by providing an accepted standard format for pathway data. It is an open and collaborative effort by the community of researchers, software developers, and institutions. BioPAX is defined in OWL DL and is represented in the RDF/XML format. For more details, see Demir E et al. 2010. The BioPAX community standard for pathway data sharing, Nature Biotechnology. 28(9).
# <markdowncell>
# http://www.biopax.org/
# Specification: http://www.biopax.org/release/biopax-level3-documentation.pdf
# https://pypi.org/project/pybiopax/
# https://github.com/indralab/pybiopax
# <markdowncell>
# For the reactions you need probably the `BiochemicalReaction` and `Degradation`.
# For the PhysicalEntities you would use `Protein` and `RNA`.
# For the inhibition you will probably use `Modulation`.
# Have a look at the specification and the introduction to BioPax.
# <markdowncell>
# Example for fetching information
# https://github.com/indralab/pybiopax/blob/master/notebooks/tutorial.ipynb

# <codecell>

from pathlib import Path

import pybiopax
from pybiopax.api import model_to_owl_str
from pybiopax.biopax import (
    BioSource,
    CellularLocationVocabulary,
    Control,
    PhysicalEntity,
    Rna,
    UnificationXref,
)
from pybiopax.biopax.base import Protein
from pybiopax.biopax.model import (
    BiochemicalReaction,
    BioPaxModel,
    Provenance,
    PublicationXref,
    Stoichiometry,
)


# <codecell>
def create_repressilator(biopax_path: Path) -> BioPaxModel:
    """Create repressilator using biopax."""
    objects = []

    # <bp:Protein rdf:about="PX">
    #  <bp:xref rdf:resource="http://identifiers.org/uniprot/P03023" />
    #  <bp:displayName rdf:datatype = "http://www.w3.org/2001/XMLSchema#string">LacI protein</bp:displayName>
    # </bp:Protein>
    # Protein(LacI protein)
    # {'_controller_of': set(), 'xref': [<pybiopax.biopax.util.UnificationXref object at 0x7fe1eb423160>],
    # 'display_name': 'LacI protein', 'standard_name': None, '_name': [], 'evidence': [], 'uid': 'PX', 'comment': [], 'availability': None, 'data_source': [], '_participant_of': set(), 'feature': [], 'not_feature': [], 'member_physical_entity': [], 'cellular_location': None, '_component_of': set(), '_member_physical_entity_of': {PhysicalEntity(PX), PhysicalEntity(PX), PhysicalEntity(PX)}, 'entity_reference': None}
    #
    # <bp:PhysicalEntity rdf:about="RIGHT_0_conversion_Reaction5_PY">
    #  <bp:cellularLocation rdf:resource="cell" />
    #  <bp:displayName rdf:datatype = "http://www.w3.org/2001/XMLSchema#string">PY</bp:displayName>
    #  <bp:memberPhysicalEntity rdf:resource="PY" />
    # </bp:PhysicalEntity>

    p1 = PhysicalEntity(
        uid="RIGHT_0_conversion_Reaction5_PY",
        display_name="PY",
        cellular_location="cell",
        member_physical_entity="PY",
    )
    objects.append(p1)

    # <bp:Stoichiometry rdf:about="LEFT_0_conversion_Reaction2_Y_STOICHIOMETRY">
    #  <bp:physicalEntity rdf:resource="LEFT_0_conversion_Reaction2_Y" />
    #  <bp:stoichiometricCoefficient rdf:datatype = "http://www.w3.org/2001/XMLSchema#float">1.0</bp:stoichiometricCoefficient>
    # </bp:Stoichiometry>
    s1 = Stoichiometry(
        uid="LEFT_0_conversion_Reaction2_Y_STOICHIOMETRY",
        physical_entity="LEFT_0_conversion_Reaction2_Y",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    # '''
    # <bp:Provenance rdf:about="datasource_1">
    #  <bp:xref rdf:resource="http://identifiers.org/biomodels.db/BIOMD0000000012" />
    #  <bp:displayName rdf:datatype = "http://www.w3.org/2001/XMLSchema#string">BioModels Database</bp:displayName>
    # </bp:Provenance>
    # '''
    p3 = Provenance(
        uid="datasource_1",
        xref="http://identifiers.org/biomodels.db/BIOMD0000000012",
        display_name="BioModels Database",
    )
    objects.append(p3)
    #
    p4 = PublicationXref(
        uid="http://identifiers.org/pubmed/10659856", id="10659856", db="PubMed"
    )
    objects.append(p4)

    p5 = Provenance(
        uid="datasource_2",
        xref="http://identifiers.org/biomodels.db/MODEL6615351360",
        display_name="BioModels Database",
    )
    objects.append(p5)

    u1 = UnificationXref(
        uid="http://identifiers.org/biomodels.db/BIOMD0000000012",
        id="BIOMD0000000012",
        db="BioModels Database",
    )
    objects.append(u1)

    u2 = UnificationXref(
        uid="http://identifiers.org/obo.go/GO:0006402",
        id="GO:0006402",
        db="Gene Ontology",
    )
    objects.append(u2)

    s2 = Stoichiometry(
        uid="LEFT_0_conversion_Reaction7_PX_STOICHIOMETRY",
        physical_entity="LEFT_0_conversion_Reaction7_PX",
        stoichiometric_coefficient="1",
    )
    objects.append(s2)

    #
    # '''
    # <bp:Control rdf:about="control_Reaction4_X_0">
    #  <bp:controlled rdf:resource="conversion_Reaction4" />
    #  <bp:controlType rdf:datatype = "http://www.w3.org/2001/XMLSchema#string">INHIBITION</bp:controlType>
    #  <bp:controller rdf:resource="PEP0_control_Reaction4X" />
    # </bp:Control>
    # '''
    c1 = Control(
        uid="control_Reaction4_X_0",
        controlled="conversion_Reaction4",
        control_type="INHIBITION",
        controller="PEP0_control_Reaction4X",
    )
    objects.append(c1)

    s2 = Stoichiometry(
        uid="RIGHT_0_conversion_Reaction6_PZ_STOICHIOMETRY",
        physical_entity="RIGHT_0_conversion_Reaction6_PZ",
        stoichiometric_coefficient="1",
    )
    objects.append(s2)

    c2 = PhysicalEntity(
        uid="PEP0_control_Reaction4X",
        cellular_location="cell",
        display_name="X",
        member_physical_entity="X",
    )
    objects.append(c2)

    u3 = UnificationXref(
        uid="http://identifiers.org/obo.go/GO:0030163",
        id="GO:0030163",
        db="Gene Ontology",
    )
    objects.append(u3)

    s3 = Stoichiometry(
        uid="RIGHT_0_conversion_Reaction12_Z_STOICHIOMETRY",
        physical_entity="RIGHT_0_conversion_Reaction12_Z",
        stoichiometric_coefficient="1",
    )
    objects.append(s3)

    c3 = PhysicalEntity(
        uid="LEFT_0_conversion_Reaction7_PX",
        cellular_location="cell",
        display_name="PX",
        member_physical_entity="PX",
    )
    objects.append(c3)

    s4 = Stoichiometry(
        uid="RIGHT_0_conversion_Reaction11_Y_STOICHIOMETRY",
        physical_entity="RIGHT_0_conversion_Reaction11_Y",
        stoichiometric_coefficient="1",
    )
    objects.append(s4)

    c4 = CellularLocationVocabulary(
        uid="cell", term="cell", xref="http://identifiers.org/obo.go/GO:0005623"
    )
    objects.append(c4)

    b1 = BiochemicalReaction(
        uid="conversion_Reaction12",
        xref="http://identifiers.org/obo.go/GO:0006351",
        participant_stoichiometry="RIGHT_0_conversion_Reaction12_Z_STOICHIOMETRY",
        display_name="transcription of CI",
        right="RIGHT_0_conversion_Reaction12_Z",
    )
    objects.append(b1)

    b1 = BiochemicalReaction(
        uid="conversion_Reaction11",
        xref="http://identifiers.org/obo.go/GO:0006351",
        participant_stoichiometry="RIGHT_0_conversion_Reaction11_Y_STOICHIOMETRY",
        display_name="transcription of TetR",
        right="RIGHT_0_conversion_Reaction11_Y",
    )
    objects.append(b1)

    b1 = BiochemicalReaction(
        uid="conversion_Reaction10",
        xref="http://identifiers.org/obo.go/GO:0006351",
        participant_stoichiometry="RIGHT_0_conversion_Reaction10_X_STOICHIOMETRY",
        display_name="transcription of LacI",
        right="RIGHT_0_conversion_Reaction10_X",
    )
    objects.append(b1)

    p1 = PhysicalEntity(
        uid="LEFT_0_conversion_Reaction9_PZ",
        cellular_location="cell",
        display_name="PZ",
        member_physical_entity="PZ",
    )
    objects.append(p1)

    u1 = UnificationXref(
        uid="http://identifiers.org/kegg.compound/C00046",
        id="C00046",
        db="KEGG Compound",
    )
    objects.append(u1)

    u1 = UnificationXref(
        uid="http://identifiers.org/obo.go/GO:0005623",
        id="GO:0005623",
        db="Gene Ontology",
    )
    objects.append(u1)

    p1 = PhysicalEntity(
        uid="LEFT_0_conversion_Reaction8_PY",
        cellular_location="cell",
        display_name="PY",
        member_physical_entity="PY",
    )
    objects.append(p1)

    u1 = UnificationXref(
        uid="http://identifiers.org/chebi/CHEBI:33699", id="CHEBI:33699", db="ChEBI"
    )
    objects.append(u1)

    p1 = Protein(
        uid="PX",
        xref="http://identifiers.org/uniprot/P03023",
        display_name="LacI protein",
    )
    objects.append(p1)

    p1 = Protein(
        uid="PY",
        xref="http://identifiers.org/uniprot/P04483",
        display_name="TetR protein",
    )
    objects.append(p1)

    s1 = Stoichiometry(
        uid="RIGHT_0_conversion_Reaction10_X_STOICHIOMETRY",
        physical_entity="RIGHT_0_conversion_Reaction10_X",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    p1 = Protein(
        uid="PZ",
        xref="http://identifiers.org/uniprot/P03034",
        display_name="cI protein",
    )
    objects.append(p1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction2",
        xref="http://identifiers.org/obo.go/GO:0006402",
        participant_stoichiometry="LEFT_0_conversion_Reaction2_Y_STOICHIOMETRY",
        left="LEFT_0_conversion_Reaction2_Y",
        display_name="degradation of TetR transcripts",
    )
    objects.append(c1)

    s1 = Stoichiometry(
        uid="RIGHT_0_conversion_Reaction4_PX_STOICHIOMETRY",
        physical_entity="RIGHT_0_conversion_Reaction4_PX",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    p1 = PhysicalEntity(
        uid="LEFT_0_conversion_Reaction3_Z",
        cellular_location="cell",
        display_name="Z",
        member_physical_entity="Z",
    )
    objects.append(p1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction3",
        xref="http://identifiers.org/obo.go/GO:0006402",
        participant_stoichiometry="LEFT_0_conversion_Reaction3_Z_STOICHIOMETRY",
        left="LEFT_0_conversion_Reaction3_Z",
        display_name="degradation of CI transcripts",
    )
    objects.append(c1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction4",
        xref="http://identifiers.org/obo.go/GO:0006412",
        participant_stoichiometry="RIGHT_0_conversion_Reaction4_PX_STOICHIOMETRY",
        display_name="translation of LacI",
        right="RIGHT_0_conversion_Reaction4_PX",
    )
    objects.append(c1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction5",
        xref="http://identifiers.org/obo.go/GO:0006412",
        participant_stoichiometry="RIGHT_0_conversion_Reaction5_PY_STOICHIOMETRY",
        display_name="translation of TetR",
        right="RIGHT_0_conversion_Reaction5_PY",
    )
    objects.append(c1)

    p1 = PhysicalEntity(
        uid="LEFT_0_conversion_Reaction2_Y",
        cellular_location="cell",
        display_name="Y",
        member_physical_entity="Y",
    )
    objects.append(p1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction6",
        xref="http://identifiers.org/obo.go/GO:0006412",
        participant_stoichiometry="RIGHT_0_conversion_Reaction6_PZ_STOICHIOMETRY",
        display_name="translation of CI",
        right="RIGHT_0_conversion_Reaction6_PZ",
    )
    objects.append(c1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction7",
        xref="http://identifiers.org/obo.go/GO:0030163",
        participant_stoichiometry="LEFT_0_conversion_Reaction7_PX_STOICHIOMETRY",
        display_name="degradation of LacI",
        left="LEFT_0_conversion_Reaction7_PX",
    )
    objects.append(c1)

    s1 = Stoichiometry(
        uid="LEFT_0_conversion_Reaction9_PZ_STOICHIOMETRY",
        physical_entity="LEFT_0_conversion_Reaction9_PZ",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction8",
        xref="http://identifiers.org/obo.go/GO:0030163",
        participant_stoichiometry="LEFT_0_conversion_Reaction8_PY_STOICHIOMETRY",
        display_name="degradation of TetR",
        left="LEFT_0_conversion_Reaction8_PY",
    )
    objects.append(c1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction9",
        xref="http://identifiers.org/obo.go/GO:0030163",
        participant_stoichiometry="LEFT_0_conversion_Reaction9_PZ_STOICHIOMETRY",
        display_name="degradation of CI",
        left="LEFT_0_conversion_Reaction9_PZ",
    )
    objects.append(c1)

    u1 = UnificationXref(
        uid="http://identifiers.org/taxonomy/562", id="562", db="Taxonomy"
    )
    objects.append(u1)

    s1 = Stoichiometry(
        uid="LEFT_0_conversion_Reaction1_X_STOICHIOMETRY",
        physical_entity="LEFT_0_conversion_Reaction1_X",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    p1 = PhysicalEntity(
        uid="RIGHT_0_conversion_Reaction4_PX",
        cellular_location="cell",
        display_name="PX",
        member_physical_entity="PX",
    )
    objects.append(p1)

    u1 = UnificationXref(
        uid="http://identifiers.org/uniprot/P03034",
        id="P03034",
        db="UniProt Knowledgebase",
    )
    objects.append(u1)

    p1 = PhysicalEntity(
        uid="PEP0_control_Reaction10PZ",
        cellular_location="cell",
        display_name="PZ",
        member_physical_entity="PZ",
    )
    objects.append(p1)

    s1 = Stoichiometry(
        uid="LEFT_0_conversion_Reaction3_Z_STOICHIOMETRY",
        physical_entity="LEFT_0_conversion_Reaction3_Z",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    p1 = PhysicalEntity(
        uid="RIGHT_0_conversion_Reaction10_X",
        cellular_location="cell",
        display_name="X",
        member_physical_entity="X",
    )
    objects.append(p1)

    b1 = BioSource(uid="biosource_1", xref="http://identifiers.org/taxonomy/562")
    objects.append(b1)

    p1 = PhysicalEntity(
        uid="RIGHT_0_conversion_Reaction11_Y",
        cellular_location="cell",
        display_name="Y",
        member_physical_entity="Y",
    )
    objects.append(p1)

    p1 = PhysicalEntity(
        uid="RIGHT_0_conversion_Reaction12_Z",
        cellular_location="cell",
        display_name="Z",
        member_physical_entity="Z",
    )
    objects.append(p1)

    s1 = Stoichiometry(
        uid="LEFT_0_conversion_Reaction8_PY_STOICHIOMETRY",
        physical_entity="LEFT_0_conversion_Reaction8_PY",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    p1 = PhysicalEntity(
        uid="RIGHT_0_conversion_Reaction6_PZ",
        cellular_location="cell",
        display_name="PZ",
        member_physical_entity="PZ",
    )
    objects.append(p1)

    p1 = PhysicalEntity(
        uid="PEP0_control_Reaction6Z",
        cellular_location="cell",
        display_name="Z",
        member_physical_entity="Z",
    )
    objects.append(p1)

    p1 = PhysicalEntity(
        uid="PEP0_control_Reaction11PX",
        cellular_location="cell",
        display_name="PX",
        member_physical_entity="PX",
    )
    objects.append(p1)

    r1 = Rna(
        uid="Y",
        xref=[
            "http://identifiers.org/chebi/CHEBI:33699",
            "http://identifiers.org/kegg.compound/C00046",
            "http://identifiers.org/uniprot/P04483",
        ],
        display_name="TetR mRNA",
    )
    objects.append(r1)

    r1 = Rna(
        uid="X",
        xref=[
            "http://identifiers.org/chebi/CHEBI:33699",
            "http://identifiers.org/kegg.compound/C00046",
            "http://identifiers.org/uniprot/P03023",
        ],
        display_name="LacI mRNA",
    )
    objects.append(r1)

    s1 = Stoichiometry(
        uid="RIGHT_0_conversion_Reaction5_PY_STOICHIOMETRY",
        physical_entity="RIGHT_0_conversion_Reaction5_PY",
        stoichiometric_coefficient="1",
    )
    objects.append(s1)

    r1 = Rna(
        uid="Z",
        xref=[
            "http://identifiers.org/chebi/CHEBI:33699",
            "http://identifiers.org/kegg.compound/C00046",
            "http://identifiers.org/uniprot/P03034",
        ],
        display_name="cI mRNA",
    )
    objects.append(r1)

    c1 = Control(
        uid="control_Reaction6_Z_0",
        controlled="conversion_Reaction6",
        control_type="INHIBITION",
        controller="PEP0_control_Reaction6Z",
    )
    objects.append(c1)

    c1 = Control(
        uid="control_Reaction12_PY_0",
        controlled="conversion_Reaction12",
        control_type="INHIBITION",
        controller="PEP0_control_Reaction12PY",
    )
    objects.append(c1)

    p1 = PhysicalEntity(
        uid="PEP0_control_Reaction12PY",
        cellular_location="cell",
        display_name="PY",
        member_physical_entity="PY",
    )
    objects.append(p1)

    u1 = UnificationXref(
        uid="http://identifiers.org/biomodels.db/MODEL6615351360",
        id="MODEL6615351360",
        db="BioModels Database",
    )
    objects.append(u1)

    u1 = UnificationXref(
        uid="http://identifiers.org/uniprot/P03023",
        id="P03023",
        db="UniProt Knowledgebase",
    )
    objects.append(u1)

    c1 = Control(
        uid="control_Reaction10_PZ_0",
        controlled="conversion_Reaction10",
        control_type="INHIBITION",
        controller="PEP0_control_Reaction10PZ",
    )
    objects.append(c1)

    u1 = UnificationXref(
        uid="http://identifiers.org/obo.go/GO:0006412",
        id="GO:0006412",
        db="Gene Ontology",
    )
    objects.append(u1)

    u1 = UnificationXref(
        uid="http://identifiers.org/obo.go/GO:0040029",
        id="GO:0040029",
        db="Gene Ontology",
    )
    objects.append(u1)

    u1 = UnificationXref(
        uid="http://identifiers.org/obo.go/GO:0006351",
        id="GO:0006351",
        db="Gene Ontology",
    )
    objects.append(u1)

    c1 = Control(
        uid="control_Reaction5_Y_0",
        controlled="conversion_Reaction5",
        control_type="INHIBITION",
        controller="PEP0_control_Reaction5Y",
    )
    objects.append(c1)

    p1 = PhysicalEntity(
        uid="LEFT_0_conversion_Reaction1_X",
        cellular_location="cell",
        display_name="X",
        member_physical_entity="X",
    )
    objects.append(p1)

    p1 = PhysicalEntity(
        uid="PEP0_control_Reaction5Y",
        cellular_location="cell",
        display_name="Y",
        member_physical_entity="Y",
    )
    objects.append(p1)

    c1 = Control(
        uid="control_Reaction11_PX_0",
        controlled="conversion_Reaction11",
        control_type="INHIBITION",
        controller="PEP0_control_Reaction11PX",
    )
    objects.append(c1)

    c1 = BiochemicalReaction(
        uid="conversion_Reaction1",
        xref="http://identifiers.org/obo.go/GO:0006402",
        participant_stoichiometry="LEFT_0_conversion_Reaction1_X_STOICHIOMETRY",
        display_name="degradation of LacI transcripts",
        left="LEFT_0_conversion_Reaction1_X",
    )
    objects.append(c1)

    u1 = UnificationXref(
        uid="http://identifiers.org/uniprot/P04483",
        id="P04483",
        db="UniProt Knowledgebase",
    )
    objects.append(u1)
    # '''
    # <bp:BiochemicalReaction rdf:about="conversion_Reaction12">
    #  <bp:xref rdf:resource="http://identifiers.org/obo.go/GO:0006351" />
    #  <bp:participantStoichiometry rdf:resource="RIGHT_0_conversion_Reaction12_Z_STOICHIOMETRY" />
    #  <bp:displayName rdf:datatype = "http://www.w3.org/2001/XMLSchema#string">transcription of CI</bp:displayName>
    #  <bp:right rdf:resource="RIGHT_0_conversion_Reaction12_Z" />
    # </bp:BiochemicalReaction>
    # '''
    # b1=BiochemicalReaction(uid="conversion_Reaction12", displayName="transcription of CI")
    # objects.append(b1)

    model = BioPaxModel(
        objects={o.uid: o for o in objects},
        xml_base="http://www.biopax.org/release/biopax-level3.owl#",
    )
    owl_str: str = model_to_owl_str(model)

    with open(biopax_path, "w") as f_biopax:
        f_biopax.write(owl_str)

    print("-" * 80)
    print(owl_str)
    print("-" * 80)

    return model


# <codecell>
if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    create_repressilator(biopax_path=RESULTS_DIR / "repressilator_biopax.owl")
