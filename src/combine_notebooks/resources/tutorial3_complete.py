"""
    TUTORIAL 3: MODEL CREATION THROUGH THE API

    By the time you have worked through Tutorial 3 you will be able to:
      - Create a new model and its child entities from scratch using the API
      - Define custom combinations of built-in units
      - Define your own custom units independent from the built-in units and
      - Use the Generator to create C or Python code representing the model.

    This tutorial assumes that you are comfortable with:
      - Accessing and adjusting names of items inside a model hierarchy (T2)
      - Creating a validator and using it to check a model for errors (T2)
      - Accessing the errors produced by a validator and using them to correct
        the model (T2) and
      - Serialising and printing a model to a CellML file (T1).
"""

from libcellml import Analyser, Component, Generator, GeneratorProfile, Model, Units, Validator, Variable

from utilities import print_issues, print_model

if __name__ == "__main__":
    print("-------------------------------------------------------------")
    print(" TUTORIAL 3: MODEL CREATION AND CODE GENERATION WITH THE API ")
    print("-------------------------------------------------------------")

    print("-------------------------------------------------------------")
    print("   Step 1: Create model instance and maths                   ")
    print("-------------------------------------------------------------")

    #  1.a   
    #      Create a Model and name it.
    model = Model()
    model.setName("tutorial3_model")

    #  1.b   
    #      Create a component to use as an integrator, set its attributes and
    #      add it to the model.
    component = Component()
    component.setName("component")
    model.addComponent(component)

    #  Checking that it worked
    print_model(model)

    #  1.c
    #      Create the MathML2 string representing the governing equations.  
    equation1 = \
        "  <apply><eq/>"\
        "    <ci>c</ci>"\
        "    <apply><plus/>"\
        "      <ci>a</ci>"\
        "      <cn>2.0</cn>"\
        "    </apply>"\
        "  </apply>"

    #  1.d
    equation2 = \
        "  <apply><eq/>"\
        "    <apply><diff/>"\
        "      <bvar><ci>time</ci></bvar>"\
        "      <ci>y_s</ci>"\
        "    </apply>"\
        "    <apply><plus/>"\
        "      <apply><times/>"\
        "        <ci>a</ci>"\
        "        <ci>y_s</ci>"\
        "      </apply>"\
        "      <apply><times/>"\
        "        <ci>b</ci>"\
        "        <ci>y_s</ci>"\
        "        <ci>y_f</ci>"\
        "      </apply>"\
        "    </apply>"\
        "  </apply>"

    #  1.e
    equation3 = \
        "  <apply><eq/>"\
        "    <apply><diff/>"\
        "      <bvar><ci>time</ci></bvar>"\
        "      <ci>y_f</ci>"\
        "    </apply>"\
        "    <apply><plus/>"\
        "      <apply><times/>"\
        "        <ci>c</ci>"\
        "        <ci>y_f</ci>"\
        "      </apply>"\
        "      <apply><times/>"\
        "        <ci>d</ci>"\
        "        <ci>y_s</ci>"\
        "        <ci>y_f</ci>"\
        "      </apply>"\
        "    </apply>"\
        "  </apply>"

    #  1.f
    #    Add the header and footer strings.
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    math_footer = '</math>'

    #  1.g
    #    Include the MathML strings in the component.
    component.setMath(math_header)
    component.appendMath(equation1)
    component.appendMath(equation2)
    component.appendMath(equation3)
    component.appendMath(math_footer)

    #  1.h   
    #    Create a validator and use it to check the model so far.
    validator = Validator()
    validator.validateModel(model)
    print_issues(validator)

    #  end 1

    print("-------------------------------------------------------------")
    print("   Step 2: Create the variables                              ")
    print("-------------------------------------------------------------")

    #  2.a
    #      Create the variables listed by the validator: d, a, b, c, time, y_s, y_f.
    sharks = Variable("y_s")
    fish = Variable("y_f")
    time = Variable("time")
    a = Variable("a")
    b = Variable("b")
    c = Variable("c")
    d = Variable("d")

    #  2.b
    #      Add the variables into the component.
    component.addVariable(sharks)
    component.addVariable(fish)
    component.addVariable(time)
    component.addVariable(a)
    component.addVariable(b)
    component.addVariable(c)
    component.addVariable(d)

    #  2.c  
    #      Call the validator again to check the model.
    validator.validateModel(model)
    print_issues(validator)

    #  end 2

    print("-------------------------------------------------------------")
    print("   Step 3: Create user-defined units                         ")
    print("-------------------------------------------------------------")

    #  From the validation errors printed above you'll see that none of the
    #  units we need are built-in. The good news is that we can create the ones
    #  we need from the set of built-in units, we just need to define the
    #  relationship.  NB: Even though units are used by Variables, which sit
    #  'inside' Components, Units sit inside the Model itself.  This helps you to
    #  reuse Units when you have more than one component (more on that in
    #  Tutorial 5)

    #  3.a  
    #      Define the relationship between our custom units and the built-in
    #      units. There is a list of built-in units and their definitions
    #      available in section 19.2 of the CellML2 specification.
    #      First we create the "month" units, which will be equivalent to
    #      60*60*24*30 = 2,592,000 seconds.
    month = Units("month")
    month.addUnit("second", 1, 2592000)  # Setting a month to be 2592000 seconds.
    model.addUnits(month)

    #  "second" is a built-in unit, used with a multiplier of 2592000.
    #  Note that this could have been written:
    #    month.addUnit("second", "mega", 1, 2.592)
    #    month.addUnit("second", 5, 25.92)

    #  3.b  
    #      Create units which represent "per_month", which
    #      is simply the inverse of the "month" unit above.
    per_month = Units()
    per_month.setName("per_month")
    per_month.addUnit("month", -1)
    model.addUnits(per_month)

    #  3.c      
    #      Create the sharks and fishes base units.
    number_of_sharks = Units()
    number_of_sharks.setName("number_of_sharks")
    model.addUnits(number_of_sharks)
    thousands_of_fish = Units()
    thousands_of_fish.setName("thousands_of_fish")
    model.addUnits(thousands_of_fish)

    #  3.d  
    #      Create the combined units for the constants.  Note that each item included
    #      with the addUnit command is multiplied to create the final Units definition.
    b_units = Units()
    b_units.setName("per_shark_month")
    b_units.addUnit("per_month")
    b_units.addUnit("number_of_sharks", -1)
    model.addUnits(b_units)

    d_units = Units()
    d_units.setName("per_fish_month")
    d_units.addUnit("per_month")
    d_units.addUnit("thousands_of_fish", -1)
    model.addUnits(d_units)

    #  3.e  
    #      Set the units to their respective variables.
    time.setUnits(month)
    sharks.setUnits(number_of_sharks)
    fish.setUnits(thousands_of_fish)
    a.setUnits(per_month)
    b.setUnits(b_units)
    c.setUnits(per_month)
    d.setUnits(d_units)

    #  3.f  
    #      Call the validator again to check the model.
    #      Expect one error regarding a missing unit in the MathML.
    validator.validateModel(model)
    print_issues(validator)

    #  3.g  
    #      Units for constants inside the MathML must be specified at the time.
    #      This means we need to adjust equation1 to include the per_month units.
    #      We have to wipe all the existing MathML and replace it.
    component.removeMath()
    component.setMath(math_header)
    equation1 = \
        "  <apply><eq/>"\
        "    <ci>c</ci>"\
        "    <apply><plus/>"\
        "      <ci>a</ci>"\
        "      <cn cellml:units=\"per_month\">2.0</cn>"\
        "    </apply>"\
        "  </apply>"
    component.appendMath(equation1)
    component.appendMath(equation2)
    component.appendMath(equation3)
    component.appendMath(math_footer)

    #  3.h  
    #      Validate once more, and expect there to be no errors this time.
    validator.validateModel(model)
    print_issues(validator)

    #  end 3

    print("-------------------------------------------------------------")
    print("   Step 4: Analyse the mathematics                           ")
    print("-------------------------------------------------------------")

    #  4.a 
    #     Create an Analyser instance and pass it the model using the
    #     analyseModel function.  
    analyser = Analyser()
    analyser.analyseModel(model)

    #  4.b 
    #     Check for errors found in the analyser. You should expect 6 errors,
    #     related to variables whose values are not computed or initialised.
    print_issues(analyser)

    #  4.c 
    #     Add initial conditions to all variables except the base variable, time
    #     and the constant c which will be computed. Reprocess the model.
    a.setInitialValue(-0.8)
    b.setInitialValue(0.3)
    d.setInitialValue(-0.6)
    sharks.setInitialValue(1.0)
    fish.setInitialValue(2.0)

    #  4.d 
    #     Reprocess the model and check that the analyser is now free of errors.
    analyser.analyseModel(model)
    print_issues(analyser)

    #  end 4

    print("-------------------------------------------------------------")
    print("   Step 5: Generate code and output                          ")
    print("-------------------------------------------------------------")

    #  5.a  
    #     Create a Generator instance.  Instead of giving it the Model item to process, 
    #     the generator takes the output from the analyser.  
    #     Retrieve the analysed model using the Analyser.model() function and pass it
    #     to the generator using the Generator.setModel function.
    generator = Generator()
    generator.setModel(analyser.model())

    #  The generator takes the CellML model and turns it into procedural code in another 
    #  language.  The default is C, but Python is available too.  This language choice is
    #  called the "profile", and is stored in a GeneratorProfile item.

    #  The default profile has a C flavour, and it already exists inside the Generator you've just created.
    #  We need to edit that profile a little, but only to tell it the file name where they interface
    #  (header file) code will be written.  This is so that the implementation code (source file) knows
    #  where to look when it tries to #include it.  

    #  5.b
    #     Retrieve the C profile from the generator, and use its setInterfaceFileNameString function
    #     to pass in the same filename that you'll use in 5.c for the interface code.
    generator.profile().setInterfaceFileNameString('PredatorPrey.h')

    #  5.c
    #     First we'll use the default profile (C), so we need to output both the
    #     interfaceCode (the header file) and the implementationCode (source file)
    #     from the generator and write them to their respective files.
    implementation_code_C = generator.implementationCode()
    with open("PredatorPrey.c", "w") as f:
        f.write(implementation_code_C)

    interface_code = generator.interfaceCode()
    with open("PredatorPrey.h", "w") as f:
        f.write(interface_code)

    #  5.d
    #     Create a GeneratorProfile item using the libcellml.GeneratorProfile.Profile.PYTHON
    #     enum value in the constructor.  Pass this profile to the setProfile function in the
    #     generator.
    profile = GeneratorProfile(GeneratorProfile.Profile.PYTHON)
    generator.setProfile(profile)

    #  5.e
    #     Retrieve the Python implementation code (there is no header file) and write to a *.py file.
    implementation_code_python = generator.implementationCode()
    with open("PredatorPrey.py", "w") as f:
        f.write(implementation_code_python)

    #  end 5

    print("All the files have been printed.")
