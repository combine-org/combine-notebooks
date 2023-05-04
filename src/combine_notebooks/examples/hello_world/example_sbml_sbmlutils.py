# <markdowncell>
# Here we show how to create a basic SBML model using basiCO, and simulating it. We start as usual by importing basiCO.

# <codecell>
from basico import *


# <markdowncell>
# Lets create a new model, passing along the name that we want to give it.

# <codecell>
new_model(name="New Model")

# <markdowncell>
# Now we add a basic reaction of a metabolite A degrading.

# <codecell>
add_reaction("r1", "A -> ")

# <markdowncell>
# We export the model to an sbml format and print it.

# <codecell>
from combine_notebooks import RESULTS_DIR


sbml_file = str(RESULTS_DIR) + "/hello_world_sbml.xml"
save_model(sbml_file, type="sbml")
xml = open(sbml_file).read()
print(xml)

# <markdowncell>
# To change the initial concentration, we use set_species, and specify which property we want to change.

# <codecell>
set_species("A", initial_concentration=10)
get_species().initial_concentration

# <codecell>
result = run_time_course(duration=50)
result.plot()
