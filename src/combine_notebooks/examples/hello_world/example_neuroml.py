# <markdowncell>

# # Interactive single Izhikevich neuron NeuroML example
#
# To run this interactive Jupyter Notebook, please click on the rocket icon 🚀 in the top panel. For more information, please see {ref}`how to use this documentation <userdocs:usage:jupyterbooks>`.
# Please uncomment the line below if you use the Google Colab (it does not include these packages by default).

# <codecell>
# #%pip install pyneuroml neuromllite NEURON
# <codecell>

from neuroml import NeuroMLDocument
import neuroml.writers as writers
from neuroml.utils import component_factory
from neuroml.utils import validate_neuroml2
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation
import numpy as np

# <markdowncell>

# ## Declaring the NeuroML model

# ### Create a NeuroML document

# <codecell>

nml_doc = component_factory(NeuroMLDocument, id="IzhSingleNeuron")

nml_doc.info()

nml_doc.info(True)

# <markdowncell>

# ### Define the Izhikevich cell and add it to the model

# <codecell>

izh0 = nml_doc.add(
    "Izhikevich2007Cell",
    id="izh2007RS0", v0="-60mV", C="100pF", k="0.7nS_per_mV", vr="-60mV",
    vt="-40mV", vpeak="35mV", a="0.03per_ms", b="-2nS", c="-50.0mV", d="100pA")
izh0.info(True)
nml_doc.info(show_contents=True)

# <markdowncell>

# ### Create a network and add it to the model
# <codecell>

net = nml_doc.add("Network", id="IzNet", validate=False)

# <markdowncell>

# ### Create a population of defined cells and add it to the model
# <codecell>

size0 = 1
pop0 = net.add("Population", id="IzhPop0", component=izh0.id, size=size0)
net.info()

# <markdowncell>

# ### Define an external stimulus and add it to the model
# <codecell>

pg = nml_doc.add(
    "PulseGenerator",
    id="pulseGen_%i" % 0, delay="0ms", duration="1000ms",
    amplitude="0.07 nA"
)
exp_input = net.add("ExplicitInput", target="%s[%i]" % (pop0.id, 0), input=pg.id)

# <markdowncell>

# ### Write the NeuroML model to a file

# <codecell>

from combine_notebooks import RESULTS_DIR

nml_file = str(RESULTS_DIR) + '/hello_world_neuroml.nml'
writers.NeuroMLWriter.write(nml_doc, nml_file)
print("Written network file to: " + nml_file)

# <markdowncell>

# ### Validate the NeuroML model
# <codecell>

validate_neuroml2(nml_file)

# <markdowncell>

# ## Simulating the model

# ### Create a simulation instance of the model
# <codecell>

simulation_id = "example-single-izhikevich2007cell-sim"
simulation = LEMSSimulation(sim_id=simulation_id,
                            duration=1000, dt=0.1, simulation_seed=123)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_file)

# <markdowncell>

# ### Define the output file to store simulation outputs
#
# Here, we record the neuron's membrane potential to the specified data file.
# <codecell>

simulation.create_output_file(
    "output0", "%s.v.dat" % simulation_id
)
simulation.add_column_to_output_file("output0", 'IzhPop0[0]', 'IzhPop0[0]/v')

# <markdowncell>

# ### Save the simulation to a file
# <codecell>

lems_simulation_file = simulation.save_to_file()

# <markdowncell>

# ## Run the simulation using the jNeuroML simulator
# <codecell>

pynml.run_lems_with_jneuroml(
    lems_simulation_file, max_memory="2G", nogui=True, plot=False
)

# <markdowncell>

# ## Plot the recorded data

# Load the data from the file and plot the graph for the membrane potential
# using the pynml generate_plot utility function.

# <codecell>

data_array = np.loadtxt("%s.v.dat" % simulation_id)
pynml.generate_plot(
    [data_array[:, 0]], [data_array[:, 1]],
    "Membrane potential", show_plot_already=True,
    xaxis="time (s)", yaxis="membrane potential (V)"
)


