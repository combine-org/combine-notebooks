# <markdowncell>
# Create repressilator using SED-ML

# SED-ML encodes in a computer-readable exchange format the information required by MIASE to enable reproduction of simulation experiments.

# https://sed-ml.org/
# <codecell>
from pathlib import Path

import libsedml


# <codecell>


def create_repressilator(sedml_path: Path) -> libsedml.SedDocument:
    """Create repressilator using SED-ML."""
    # create the document
    doc = libsedml.SedDocument(1, 4)

    # create a first model referencing an sbml file

    """
    <listOfSimulations>
        <uniformTimeCourse id="sim1" initialTime="0" outputStartTime="0" outputEndTime="1000" numberOfPoints="1000">
          <algorithm kisaoID="KISAO:0000019"/>
        </uniformTimeCourse>
      </listOfSimulations>
    """
    # create simulation
    tc = doc.createUniformTimeCourse()
    tc.setId("sim1")
    tc.setInitialTime(0.0)
    tc.setOutputStartTime(0.0)
    tc.setOutputEndTime(1000.0)
    tc.setNumberOfPoints(1000)
    # need to set the correct KISAO Term
    alg = tc.createAlgorithm()
    alg.setKisaoID("KISAO:0000019")

    """
    <listOfModels>
    <model id="model1" language="urn:sedml:language:sbml.level-3.version-1" source="https://www.ebi.ac.uk/biomodels/model/download/BIOMD0000000012?filename=BIOMD0000000012_url.xml"/>
    <model id="model2" language="urn:sedml:language:sbml.level-3.version-1" source="#model1">
      <listOfChanges>
        <changeAttribute target="/sbml:sbml/sbml:model/sbml:listOfParameters/sbml:parameter[@id='ps_0']/@value" newValue="1.3e-05"/>
        <changeAttribute target="/sbml:sbml/sbml:model/sbml:listOfParameters/sbml:parameter[@id='ps_a']/@value" newValue="0.013"/>
      </listOfChanges>
    </model>
    </listOfModels>
    """
    # create a first model referencing an sbml file
    model = doc.createModel()
    model.setId("model1")
    model.setSource(
        "https://www.ebi.ac.uk/biomodels/model/download/BIOMD0000000012?filename=BIOMD0000000012_url.xml"
    )
    model.setLanguage("urn:sedml:language:sbml.level-3.version-1")

    # create a second model modifying a variable of that other sbml file
    model = doc.createModel()
    model.setId("model2")
    model.setSource("#model1")
    model.setLanguage("urn:sedml:language:sbml.level-3.version-1")

    change = model.createChangeAttribute()
    change.setTarget(
        "/sbml:sbml/sbml:model/sbml:listOfParameters/sbml:parameter[@id='ps_0']/@value"
    )
    change.setNewValue("1.3e-05")

    change = model.createChangeAttribute()
    change.setTarget(
        "/sbml:sbml/sbml:model/sbml:listOfParameters/sbml:parameter[@id='ps_a']/@value"
    )
    change.setNewValue("0.013")

    """
    <listOfTasks>
    <task id="task1" modelReference="model1" simulationReference="sim1"/>
    <task id="task2" modelReference="model2" simulationReference="sim1"/>
    </listOfTasks>
    """
    # create a task that uses the simulation and the model above
    task = doc.createTask()
    task.setId("task1")
    task.setModelReference("model1")
    task.setSimulationReference("sim1")

    # create a task that uses the simulation and the model above
    task = doc.createTask()
    task.setId("task2")
    task.setModelReference("model2")
    task.setSimulationReference("sim1")

    """
    <dataGenerator id="dg_0_0_0" name="task1.time">
      <listOfVariables>
        <variable id="task1_____time" symbol="urn:sedml:symbol:time" taskReference="task1"/>
      </listOfVariables>
      <math xmlns="http://www.w3.org/1998/Math/MathML">
        <ci> task1_____time </ci>
      </math>
    </dataGenerator>
    """
    # add a DataGenerator to hold the output for time
    dg = doc.createDataGenerator()
    dg.setId("dg_0_0_0")
    dg.setName("task1.time")
    var = dg.createVariable()
    var.setId("task1_____time")
    var.setTaskReference("task1")
    var.setSymbol("urn:sedml:symbol:time")
    dg.setMath(libsedml.parseFormula("task1_____time"))

    dg = doc.createDataGenerator()
    dg.setId("dg_0_0_1")
    dg.setName("PX (lacI)")
    var = dg.createVariable()
    var.setId("task1_____PX")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PX']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    dg.setMath(libsedml.parseFormula("task1_____PX"))

    dg = doc.createDataGenerator()
    dg.setId("dg_0_1_1")
    dg.setName("PZ (cI)")
    var = dg.createVariable()
    var.setId("task1_____PZ")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PZ']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    dg.setMath(libsedml.parseFormula("task1_____PZ"))

    dg = doc.createDataGenerator()
    dg.setId("dg_0_2_1")
    dg.setName("PY (tetR)")
    var = dg.createVariable()
    var.setId("task1_____PY")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PY']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    dg.setMath(libsedml.parseFormula("task1_____PY"))

    dg = doc.createDataGenerator()
    dg.setId("dg_1_0_0")
    dg.setName("time")
    var = dg.createVariable()
    var.setId("task2_____time")
    var.setSymbol("urn:sedml:symbol:time")
    var.setTaskReference("task2")
    dg.setMath(libsedml.parseFormula("task2_____time"))

    dg = doc.createDataGenerator()
    dg.setId("dg_1_0_1")
    dg.setName("PX (lacI)")
    var = dg.createVariable()
    var.setId("task2_____PX")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PX']")
    var.setTaskReference("task2")
    var.setModelReference("model2")
    dg.setMath(libsedml.parseFormula("task2_____PX"))

    dg = doc.createDataGenerator()
    dg.setId("dg_1_1_1")
    dg.setName("PZ (cI)")
    var = dg.createVariable()
    var.setId("task2_____PZ")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PZ']")
    var.setTaskReference("task2")
    var.setModelReference("model2")
    dg.setMath(libsedml.parseFormula("task2_____PZ"))

    dg = doc.createDataGenerator()
    dg.setId("dg_1_2_1")
    dg.setName("PY (tetR)")
    var = dg.createVariable()
    var.setId("task2_____PY")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PY']")
    var.setTaskReference("task2")
    var.setModelReference("model2")
    dg.setMath(libsedml.parseFormula("task2_____PY"))

    dg = doc.createDataGenerator()
    dg.setId("dg_2_0_0")
    dg.setName("PX/max(PX) (lacI normalized)")
    var = dg.createVariable()
    var.setId("task1_____PX")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PX']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    var = dg.createVariable()
    var.setId("task1_____PX_max")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PX']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    var.setDimensionTerm("KISAO:0000828")
    dg.setMath(libsedml.parseFormula("task1_____PX / task1_____PX_max"))

    dg = doc.createDataGenerator()
    dg.setId("dg_2_0_1")
    dg.setName("PZ/max(PZ) (cI normalized)")
    var = dg.createVariable()
    var.setId("task1_____PZ")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PZ']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    var = dg.createVariable()
    var.setId("task1_____PZ_max")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PX']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    var.setDimensionTerm("KISAO:0000828")
    dg.setMath(libsedml.parseFormula("task1_____PZ / task1_____PZ_max"))

    dg = doc.createDataGenerator()
    dg.setId("dg_2_1_0")
    dg.setName("PY/max(PY) (tetR normalized)")
    var = dg.createVariable()
    var.setId("task1_____PY")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PY']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    var = dg.createVariable()
    var.setId("task1_____PY_max")
    var.setTarget("/sbml:sbml/sbml:model/sbml:listOfSpecies/sbml:species[@id='PY']")
    var.setTaskReference("task1")
    var.setModelReference("model1")
    var.setDimensionTerm("KISAO:0000828")
    dg.setMath(libsedml.parseFormula("task1_____PY / task1_____PY_max"))

    # add a 2d plot
    plot = doc.createPlot2D()
    plot.setId("timecourse")
    plot.setName("Timecourse of repressilator")
    curve = plot.createCurve()
    curve.setId("plot_0__plot_0_0_0__plot_0_0_1")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_0_0_0")
    curve.setYDataReference("dg_0_0_1")
    curve = plot.createCurve()
    curve.setId("plot_0__plot_0_0_0__plot_0_1_1")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_0_0_0")
    curve.setYDataReference("dg_0_1_1")
    curve = plot.createCurve()
    curve.setId("plot_0__plot_0_0_0__plot_0_2_1")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_0_0_0")
    curve.setYDataReference("dg_0_2_1")

    # add a 2d plot
    plot = doc.createPlot2D()
    plot.setId("preprocessing")
    plot.setName("Timecourse after pre-processing")
    curve = plot.createCurve()
    curve.setId("plot_1__plot_1_0_0__plot_1_0_1")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_1_0_0")
    curve.setYDataReference("dg_1_0_1")
    curve = plot.createCurve()
    curve.setId("plot_1__plot_1_0_0__plot_1_1_1")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_1_0_0")
    curve.setYDataReference("dg_1_1_1")
    curve = plot.createCurve()
    curve.setId("plot_1__plot_1_0_0__plot_1_2_1")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_1_0_0")
    curve.setYDataReference("dg_1_2_1")

    # add a 2d plot
    plot = doc.createPlot2D()
    plot.setId("postprocessing")
    plot.setName("Timecourse after post-processing")
    curve = plot.createCurve()
    curve.setId("plot_2__plot_2_0_0__plot_2_0_1")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_2_0_0")
    curve.setYDataReference("dg_2_0_1")
    curve = plot.createCurve()
    curve.setId("plot_2__plot_2_1_0__plot_2_0_0")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_2_1_0")
    curve.setYDataReference("dg_2_0_0")
    curve = plot.createCurve()
    curve.setId("plot_2__plot_2_0_1__plot_2_1_0")
    curve.setLogX(False)
    curve.setLogY(False)
    curve.setXDataReference("dg_2_0_1")
    curve.setYDataReference("dg_2_1_0")

    # write doc
    libsedml.writeSedML(doc, str(sedml_path))
    return doc


# <codecell>
if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    create_repressilator(sedml_path=RESULTS_DIR / "repressilator_sedml.xml")
