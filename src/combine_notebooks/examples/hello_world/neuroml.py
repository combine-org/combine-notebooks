# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Interactive single Izhikevich neuron NeuroML example
#
# To run this interactive Jupyter Notebook, please click on the rocket icon 🚀 in the top panel. For more information, please see {ref}`how to use this documentation <userdocs:usage:jupyterbooks>`.
# Please uncomment the line below if you use the Google Colab (it does not include these packages by default).

# %%
# #%pip install pyneuroml neuromllite NEURON

# %%
from neuroml import NeuroMLDocument
import neuroml.writers as writers
from neuroml.utils import component_factory
from neuroml.utils import validate_neuroml2
from pyneuroml import pynml
from pyneuroml.lems import LEMSSimulation
import numpy as np

# %% [markdown]
# ## Declaring the NeuroML model

# %% [markdown]
# ### Create a NeuroML document

# %%
nml_doc = component_factory(NeuroMLDocument, id="IzhSingleNeuron")

# %%
nml_doc.info()

# %%
nml_doc.info(True)

# %% [markdown]
# ### Define the Izhikevich cell and add it to the model

# %%
izh0 = nml_doc.add(
    "Izhikevich2007Cell",
    id="izh2007RS0", v0="-60mV", C="100pF", k="0.7nS_per_mV", vr="-60mV",
    vt="-40mV", vpeak="35mV", a="0.03per_ms", b="-2nS", c="-50.0mV", d="100pA")
izh0.info(True)
nml_doc.info(show_contents=True)

# %% [markdown]
# ### Create a network and add it to the model

# %%
net = nml_doc.add("Network", id="IzNet", validate=False)

# %% [markdown]
# ### Create a population of defined cells and add it to the model

# %%
size0 = 1
pop0 = net.add("Population", id="IzhPop0", component=izh0.id, size=size0)
net.info()

# %% [markdown]
# ### Define an external stimulus and add it to the model

# %%
pg = nml_doc.add(
    "PulseGenerator",
    id="pulseGen_%i" % 0, delay="0ms", duration="1000ms",
    amplitude="0.07 nA"
)
exp_input = net.add("ExplicitInput", target="%s[%i]" % (pop0.id, 0), input=pg.id)

# %% [markdown]
# ### Write the NeuroML model to a file

# %%
nml_file = 'izhikevich2007_single_cell_network.nml'
writers.NeuroMLWriter.write(nml_doc, nml_file)
print("Written network file to: " + nml_file)

# %% [markdown]
# ### Validate the NeuroML model

# %%
validate_neuroml2(nml_file)

# %% [markdown]
# ## Simulating the model

# %% [markdown]
# ### Create a simulation instance of the model

# %%
simulation_id = "example-single-izhikevich2007cell-sim"
simulation = LEMSSimulation(sim_id=simulation_id,
                            duration=1000, dt=0.1, simulation_seed=123)
simulation.assign_simulation_target(net.id)
simulation.include_neuroml2_file(nml_file)

# %% [markdown]
# ### Define the output file to store simulation outputs
#
# Here, we record the neuron's membrane potential to the specified data file.

# %%
simulation.create_output_file(
    "output0", "%s.v.dat" % simulation_id
)
simulation.add_column_to_output_file("output0", 'IzhPop0[0]', 'IzhPop0[0]/v')

# %% [markdown]
# ### Save the simulation to a file

# %%
lems_simulation_file = simulation.save_to_file()

# %% [markdown]
# ## Run the simulation using the jNeuroML simulator

# %%
pynml.run_lems_with_jneuroml(
    lems_simulation_file, max_memory="2G", nogui=True, plot=False
)

# %% [markdown]
# ## Plot the recorded data

# %%
# Load the data from the file and plot the graph for the membrane potential
# using the pynml generate_plot utility function.
data_array = np.loadtxt("%s.v.dat" % simulation_id)
pynml.generate_plot(
    [data_array[:, 0]], [data_array[:, 1]],
    "Membrane potential", show_plot_already=True,
    xaxis="time (s)", yaxis="membrane potential (V)"
)

# %%
