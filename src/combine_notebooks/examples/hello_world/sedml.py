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

# %%
from pathlib import Path
import libsedml

# %% [markdown]
# ## Declaring the SED-ML model

 # %%
 # create the document
doc = libsedml.SedDocument(1, 4)
# create a first model referencing an sbml file
model = doc.createModel()
model.setId("model1")
model.setSource("model1.xml")
model.setLanguage("urn:sedml:language:sbml") 

# %% [markdown]
# Simulators

# %%
# create simulation
tc = doc.createUniformTimeCourse()
tc.setId("sim1")
tc.setInitialTime(0.0)
tc.setOutputStartTime(0.0)
tc.setOutputEndTime(10.0)
tc.setNumberOfSteps(100)
# need to set the correct KISAO Term
alg = tc.createAlgorithm()
alg.setName("Deterministic (LSODA)")
alg.setKisaoID("KISAO:0000560")
# add algorithm parameters
alg_par1 = alg.createAlgorithmParameter()
alg_par1.setName("Relative Tolerance")
alg_par1.setKisaoID("KISAO:0000209")
alg_par1.setValue("1e-06")
alg_par2 = alg.createAlgorithmParameter()
alg_par2.setName("Absolute Tolerance")
alg_par2.setKisaoID("KISAO:0000211")
alg_par2.setValue("1e-12")
alg_par3 = alg.createAlgorithmParameter()
alg_par3.setName("Integrate Reduced Model")
alg_par3.setKisaoID("KISAO:0000216")
alg_par3.setValue("0")
alg_par4 = alg.createAlgorithmParameter()
alg_par4.setName("Max Internal Steps")
alg_par4.setKisaoID("KISAO:0000415")
alg_par4.setValue("100000")


# %% [markdown]
# Task

# %%
# create a task that uses the simulation and the model above
task = doc.createTask()
task.setId("task1")
task.setModelReference("model1")
task.setSimulationReference("sim1")


# %% [markdown]
# Data generators

# %%
# add a DataGenerator to hold the output for time
dg = doc.createDataGenerator()
dg.setId("_1_task1")
dg.setName("Time")
var = dg.createVariable()
var.setId("p1__1_task1")
var.setName("Time")
var.setTaskReference("task1")
var.setSymbol("urn:sedml:symbol:time")
var.setTerm("KISAO:0000832")
dg.setMath(libsedml.parseFormula("p1__1_task1"))

dg = doc.createDataGenerator()
dg.setId("A_1_task1")
dg.setName("[A]")
var = dg.createVariable()
var.setId("p1_A_1_task1")
var.setName("[A]")
var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id=&apos;A&apos;]")
var.setTaskReference("task1")
var.setTerm("KISAO:0000838")
dg.setMath(libsedml.parseFormula("p1_A_1_task1"))



# %% [markdown]
# Outputs

# %%
# add a 2d plot
plot = doc.createPlot2D()
plot.setId("plot_1_task1")
plot.setName("Concentrations, Volumes, and Global Quantity Values")
curve = plot.createCurve()
curve.setId("p1_curve_1_task1")
curve.setName("[A]")
curve.setLogX(False)
curve.setLogY(False)
curve.setStyle("style1")
curve.setXDataReference("_1_task1")
curve.setYDataReference("A_1_task1")

# %% [markdown]
# Styles

# %%
style : libsedml.SedStyle = doc.createStyle()
style.setId("style1")
line = style.createLineStyle()
line.setType("solid")
line.setThickness(1.2)
marker = style.createMarkerStyle()
marker.setType("none")


# %%
libsedml.writeSedML(doc, str('sedml_path.sedml'))

