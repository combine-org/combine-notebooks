"""
- try to install python library
- try to read an example file
- MK: evaluate usage of biopax (Reactome)
"""

import pybiopax
model = pybiopax.model_from_owl_file('/Users/adityasinghal/PycharmProjects'
                                     '/combine-notebooks/src/combine_notebooks/resources/BIOMD0000000012-biopax3.owl')

biopax = pybiopax.BiochemicalReaction()
