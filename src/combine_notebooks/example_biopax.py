"""
http://www.biopax.org/
Biological Pathway Exchange (BioPAX) is a standard language that aims to enable integration, exchange, visualization and analysis of biological pathway data. Specifically, BioPAX supports data exchange between pathway data groups and thus reduces the complexity of interchange between data formats by providing an accepted standard format for pathway data. It is an open and collaborative effort by the community of researchers, software developers, and institutions. BioPAX is defined in OWL DL and is represented in the RDF/XML format. For more details, see Demir E et al. 2010. The BioPAX community standard for pathway data sharing, Nature Biotechnology. 28(9).
Specification: http://www.biopax.org/release/biopax-level3-documentation.pdf
https://pypi.org/project/pybiopax/
https://github.com/indralab/pybiopax
For the reactions you need probably the `BiochemicalReaction` and `Degradation`.
For the PhysicalEntities you would use `Protein` and `RNA`.
For the inhibition you will probably use `Modulation`.
Have a look at the specification and the introduction to BioPax.
Example for fetching information
https://github.com/indralab/pybiopax/blob/master/notebooks/tutorial.ipynb
"""

import pybiopax
from combine_notebooks import RESOURCES_DIR

from pybiopax.biopax.model import BioPaxModel
from pybiopax.biopax.base import Protein
from pybiopax.api import model_to_owl_str

objects = []
'''
<bp:Protein rdf:about="PX">
 <bp:xref rdf:resource="http://identifiers.org/uniprot/P03023" />
 <bp:displayName rdf:datatype = "http://www.w3.org/2001/XMLSchema#string">LacI protein</bp:displayName>
</bp:Protein>

Protein(LacI protein)
{'_controller_of': set(), 'xref': [<pybiopax.biopax.util.UnificationXref object at 0x7fe1eb423160>], 
'display_name': 'LacI protein', 
'standard_name': None, 
'_name': [], 'evidence': [], 
'uid': 'PX', 'comment': [], 'availability': None, 'data_source': [], 
'_participant_of': set(), 'feature': [], 
'not_feature': [], 'member_physical_entity': [], 
'cellular_location': None, '_component_of': set(), 
'_member_physical_entity_of': {PhysicalEntity(PX), PhysicalEntity(PX), PhysicalEntity(PX)}, 'entity_reference': None}

'''
p = Protein(uid="PX", display_name="LacI protein")
objects.append(p)


model = BioPaxModel(objects={o.uid: o for o in objects}, xml_base="http://www.biopax.org/release/biopax-level3.owl#")
owl_str: str = model_to_owl_str(model)

print("-" * 80)
print(owl_str)
print("-" * 80)

# FIXME: validation



# if True:
#     # Reading a model
#     model1 = pybiopax.model_from_owl_file(str(RESOURCES_DIR / "BIOMD0000000012-biopax3.owl"))
#     # biopax = pybiopax.BiochemicalReaction()
#     print(model1)

#     for obj_key, obj in model1.objects.items():
#         print("-" * 80)
#         print(obj_key)
#         print(obj)
#         print(obj.__dict__)