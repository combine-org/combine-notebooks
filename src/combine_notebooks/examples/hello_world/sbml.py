# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# Here we show how to create a basic SBML model using basiCO, and simulating it. We start as usual by importing basiCO.

# %%
from basico import *

# %% [markdown]
# Lets create a new model, passing along the name that we want to give it.

# %%
new_model(name="New Model") 

# %% [markdown]
# Now we add a basic reaction of a metabolite A degrading.  

# %%
add_reaction('r1', 'A -> ')

# %% [markdown]
# We export the model to an sbml format and print it.

# %%
save_model('sbml.xml', type='sbml')
xml = open('sbml.xml').read()
print(xml)

# %% [markdown]
# To change the initial concentration, we use set_species, and specify which property we want to change.

# %%
set_species('A', initial_concentration=10)
get_species().initial_concentration

# %%
result = run_time_course(duration=50)
result.plot()

# %%
