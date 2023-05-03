# <markdowncell>

# https://libcellml.org/documentation/v0.4.0/user/tutorials/hh_tutorial1/index

# <codecell>

from libcellml import Analyser, Component, Model, Printer, Units, Validator, Variable, cellmlElementTypeAsString
from combine_notebooks.cellml_utilities import print_model

# <markdowncell>

# Setup the model

# <codecell>
#  Setup useful things.
math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">\n'
math_footer = '</math>'

# The first step is to create a Model item which will later contain the component and 
# the units it needs.  
model = Model()

# Each CellML element must have a name, which is set using the setName() function.
model.setName('GateModel')

# We'll create a wrapper component whose only job is to encapsulate the other components.
# This makes is a lot easier for this model to be reused, as the connections between
# components internal to this one won't need to be re-established.
# Note that the constructor for all named CellML entities is overloaded, so 
# you can pass it the name string at the time of creation.
# Create a component named 'gate'.
gate = Component('gate')

# Finally we need to add the component to the model.  This sets it at the top-level of 
# the components' encapsulation hierarchy.  All other components need to be added 
# to this component, rather than the model.
# Add the component to the model using the Model::addComponent() function.
model.addComponent(gate)

# Print the model to the terminal using the print_model helper function and 
# check it is what you'd expect.
print_model(model)

# <markdowncell>

# Create the gateEquations component

# <codecell>

# Create a gateEquations component and name it 'gateEquations'.
gateEquations = Component('gateEquations')

# Add the new gateEquations component to the gate component.
gate.addComponent(gateEquations)

# Add the mathematics to the gateEquations component.
equation = \
    '  <apply><eq/>\n'\
    '    <apply><diff/>\n'\
    '      <bvar><ci>t</ci></bvar>\n'\
    '      <ci>X</ci>\n'\
    '    </apply>\n'\
    '    <apply><minus/>\n'\
    '      <apply><times/>\n'\
    '        <ci>alpha_X</ci>\n'\
    '        <apply><minus/>\n'\
    '          <cn cellml:units="dimensionless">1</cn>\n'\
    '          <ci>X</ci>\n'\
    '        </apply>\n'\
    '      </apply>\n'\
    '      <apply><times/>\n'\
    '        <ci>beta_X</ci>\n'\
    '        <ci>X</ci>\n'\
    '      </apply>\n'\
    '    </apply>\n'\
    '  </apply>\n'

gateEquations.setMath(math_header)
gateEquations.appendMath(equation)
gateEquations.appendMath(math_footer)

#      Print the model to the terminal using the print_model helper function and 
#      check it is what you'd expect.  Include the second argument as True so that 
#      the maths is included.
print_model(model, True)

#  Once the mathematics has been added to the component, and the component to the 
#  model, we can make use of the diagnostic messages within the Validator class
#  to tell us what else needs to be done.  
# <markdowncell>

# Validate the model

# <codecell>

# Create a Validator instance, and pass it your model for processing using the 
# validateModel function.  
validator = Validator()
validator.validateModel(model)
# <markdowncell>

# Add the variables

# <codecell>
# Create items for the missing variables and add them to the gateEquations component.
# You will need to be sure to give them names which match exactly those reported by the
# validator, or are present in the MathML string.  
gateEquations.addVariable(Variable('t'))
gateEquations.addVariable(Variable('alpha_X'))
gateEquations.addVariable(Variable('beta_X'))
gateEquations.addVariable(Variable('X'))

# Validate again, and expect errors relating to missing units.
# Note that you can use the helper function print_issues(validator) to print your
# issues to the screen instead of repeating the code from 3.b.
validator.validateModel(model)
# <markdowncell>

# Add the units

# <codecell>
#  The validator has reported that the four variables are missing units attributes.  
#  In this example none of the units exist yet, so we need to create all of them. 
#  The variables' units should be:
#      - t, time has units of *milliseconds*
#      - X, gate status has units of *dimensionless*
#      - alpha_X and beta_X, rates, have units of *per millisecond*.

# Create the units which will be needed by your variables and add them to the model.
ms = Units('ms')
per_ms = Units('per_ms')

# Add Unit items to the units you created to define them.
ms.addUnit('second', 'milli')
per_ms.addUnit('second', 'milli', -1)

# Add the Units to the model (not the component) so that other components can make 
# use of them too.
model.addUnits(ms)
model.addUnits(per_ms)

# Use the setUnits function to associate them with the appropriate variables.  
gateEquations.variable('t').setUnits(ms)
gateEquations.variable('alpha_X').setUnits(per_ms)
gateEquations.variable('beta_X').setUnits(per_ms)
gateEquations.variable('X').setUnits('dimensionless')

# Validate again, and expect no errors.
validator.validateModel(model)

# Print the model to the terminal and include the optional second argument of true
# to include the MathML.
print_model(model, True)
# <markdowncell>

# Analyse the model

# <codecell>
# Create an Analyser item and submit the model for processing. 
analyser = Analyser()
analyser.analyseModel(model)

# In order to avoid hard-coding values here, we will need to connect to external 
# values to initialise the X variable and provide the value for alpha_X and beta_X.
# This means that:
#      - we need to create an external component to hold variable values
#      - we need to create external variables in that component 
#      - we need to specify the connections between variables and
#      - we need to permit external connections on the variables.

# Create a component which will store the hard-coded values for initialisation.
# Name it 'gateParameters', and add it to the top-level gate component as a sibling
# of the gateEquations component.
gateParameters = Component('gateParameters')
gate.addComponent(gateParameters)

#      Create appropriate variables in this component, and set their units.
#      Use the setInitialValue function to initialise them.
X = Variable('X')
X.setUnits('dimensionless')
X.setInitialValue(0)
gateParameters.addVariable(X)

alpha = Variable('alpha')
alpha.setUnits(per_ms)
alpha.setInitialValue(0.1)
gateParameters.addVariable(alpha)

beta = Variable('beta')
beta.setUnits(per_ms)
beta.setInitialValue(0.5)
gateParameters.addVariable(beta)

# Specify a variable equivalence between the gateEquations variables and the parameter variables.
# Validate the model again, expecting errors related to the variable interface types.
Variable.addEquivalence(gateEquations.variable('X'), gateParameters.variable('X'))
Variable.addEquivalence(gateEquations.variable('alpha_X'), gateParameters.variable('alpha'))
Variable.addEquivalence(gateEquations.variable('beta_X'), gateParameters.variable('beta'))

validator.validateModel(model)

# Set the variable interface type according to the recommendation from the validator.
# This can either be done individually using the Variable::setInterfaceType() function, or 
# en masse for all the model's interfaces using the Model::fixVariableInterfaces() function.
# Validate and analyse again, expecting no errors. 
model.fixVariableInterfaces()

validator.validateModel(model)

analyser.analyseModel(model)

# <markdowncell>

# Sanity check

# <codecell>
# Print the model to the terminal using the helper function print_model.
print_model(model)

# Looking at the printout we see that the top-level component has no variables.  
# Even though this is clearly a valid situation (as proved by 4.f), it's not
# going to make this model easy to reuse.  We need to make sure that any input and
# output variables are also connected into the top level gate component.  

# Create intermediate variables for time t and gate status X in the gate component,
# and ensure they have a public and private interface to enable two-way connection.
# You may also need to set a public and private connection onto t and X in the
# equations component too.
gate.addVariable(gateEquations.variable('t').clone())
gate.addVariable(gateEquations.variable('X').clone())

gate.variable('t').setInterfaceType('public_and_private')
gate.variable('X').setInterfaceType('public_and_private')
gateEquations.variable('t').setInterfaceType('public_and_private')
gateEquations.variable('X').setInterfaceType('public_and_private')

# Connect the intermediate variables to their respective partners in the equations
# component, and recheck the model.
Variable.addEquivalence(gate.variable('t'), gateEquations.variable('t'))
Variable.addEquivalence(gate.variable('X'), gateEquations.variable('X'))

validator.validateModel(model)
analyser.analyseModel(model)
# <markdowncell>

# Serialise and output the model

# <codecell>
from combine_notebooks import RESULTS_DIR
from pathlib import Path

cellml_path: Path = RESULTS_DIR / 'hello_world_cellml.cellml'

# Create a Printer instance and use it to serialise the model.  This creates a string
# containing the CellML-formatted version of the model.  Write this to a file called
# 'hello_world_cellml.cellml'.
printer = Printer()
write_file = open(cellml_path, 'w')
write_file.write(printer.printModel(model))
write_file.close()

print('The created model has been written to hello_world_cellml.cellml')
