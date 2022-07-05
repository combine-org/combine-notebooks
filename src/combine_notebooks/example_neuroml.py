"""Example script for creating SBML repressilator with neuroml.

https://neuroml.org/
https://docs.neuroml.org/Userdocs/CreatingNeuroMLModels.html

https://pyneuroml.readthedocs.io/en/latest/pyneuroml.html#module-pyneuroml.pynml
https://docs.biosimulators.org/Biosimulators_pyNeuroML/installation.html
https://github.com/NeuroML/Documentation/blob/master/source/Userdocs/NML2_examples/SingleNeuron.ipynb

# TODO: create Hudgkin-Huxley model, this is standard Neuron model
"""
from pathlib import Path
import pyneuroml
from neuroml import NeuroMLDocument

# create a neuroml document
nml_doc = NeuroMLDocument(id="repressilator")

#compartment
#species
#parameters
#rules
#reactions