# <markdowncell>
# Example script for creating SBML repressilator with cellml.
# <markdowncell>
# https://www.cellml.org/getting-started/tutorials/COR-tutorial
# https://models.physiomeproject.org/exposure/bee9fb9df261ba69b51897f2e49b1691/elowitz_leibler_2000.cellml/view?searchterm=repressilator
#
# https://libcellml.org/documentation/v0.2.0/user/tutorials/tutorial3/index
# <markdowncell>
# opencor: https://opencor.ws/downloads/index.html
#
# Issues: https://github.com/cellml/libcellml/issues/1017

# <codecell>
from pathlib import Path

import libcellml
import libsbml

from combine_notebooks.cellml_utilities import print_model


# <codecell>
def create_repressilator(cellml_path: Path) -> libcellml.Model:
    """Create CellML repressilator and save to Path."""
    model = libcellml.Model()
    model.setName("repressilator")

    """
    <units name="minute">
      <unit units="second" multiplier="60"/>
    </units>
    <units name="first_order_rate_constant">
        <unit units="minute" exponent="-1"/>
    </units>
    """
    minute = libcellml.Units("minute")
    minute.addUnit("second", 1, 60)
    model.addUnits(minute)

    # first_order_rate_constant = libcellml.Units("minute")
    # first_order_rate_constant.addUnit("minute")
    # model.addUnits(first_order_rate_constant)
    ##############################################################################################
    """
    <component name="environment">
      <variable units="minute" public_interface="out" name="time" cmeta:id="environment_time"/>
    </component>
    """
    comp_env = libcellml.Component()
    comp_env.setName("environment")
    model.addComponent(comp_env)

    var_n = libcellml.Variable()
    var_n.setName("time")
    var_n.setInterfaceType("out")
    var_n.setUnits("minute")
    var_n.setId("environment_time")
    comp_env.addVariable(var_n)

    comp_parameters = libcellml.Component()
    comp_parameters.setName("parameters")
    model.addComponent(comp_parameters)

    # var n: dimensionless {init: 2, pub: out};
    var_n = libcellml.Variable()
    var_n.setName("n")
    var_n.setInitialValue(2.0)
    var_n.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_n)

    var_alpha_0 = libcellml.Variable()
    var_alpha_0.setName("alpha_0")
    var_alpha_0.setInitialValue(0.216)
    var_alpha_0.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha_0)

    var_alpha = libcellml.Variable()
    var_alpha.setName("alpha")
    var_alpha.setInitialValue(216)
    var_alpha.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha)

    var_beta = libcellml.Variable()
    var_beta.setName("beta")
    var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_K_m = libcellml.Variable()
    var_K_m.setName("K_m")
    var_K_m.setInitialValue(40)
    var_K_m.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_K_m)

    var_efficiency = libcellml.Variable()
    var_efficiency.setName("efficiency")
    var_efficiency.setInitialValue(20)
    var_efficiency.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_efficiency)

    var_mRNA_halflife = libcellml.Variable()
    var_mRNA_halflife.setName("mRNA_halflife")
    var_mRNA_halflife.setInitialValue(2)
    var_mRNA_halflife.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_mRNA_halflife)

    var_t_ave = libcellml.Variable()
    var_t_ave.setName("t_ave")
    var_t_ave.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_t_ave)

    # var_eff = libcellml.Variable()
    # var_eff.setName("eff")
    # var_eff.setInitialValue(20)
    # var_eff.setUnits("minute")
    # comp_parameters.addVariable(var_eff)

    # start with math
    math_ast1: libsbml.ASTNode = libsbml.parseL3Formula("mRNA_halflife/ln(2)")
    math_str = libsbml.writeMathMLToString(math_ast1)
    print(math_str)
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    #    Include the MathML strings in the component.
    math_str = "\n".join([math_header] + math_str.split("\n")[2:])
    print(math_str)
    comp_parameters.setMath(math_str)

    ##############################################################################################

    comp_parameters = libcellml.Component()
    comp_parameters.setName("M_lacl")
    model.addComponent(comp_parameters)

    # var n: dimensionless {init: 2, pub: out};
    var_n = libcellml.Variable()
    var_n.setName("M_lacl")
    var_n.setInitialValue(5.0)
    var_n.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_n)

    var_alpha = libcellml.Variable()
    var_alpha.setName("alpha")
    var_alpha.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha)

    var_beta = libcellml.Variable()
    var_beta.setName("P_cl")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_beta = libcellml.Variable()
    var_beta.setName("n")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_alpha_0 = libcellml.Variable()
    var_alpha_0.setName("alpha_0")
    var_alpha_0.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha_0)

    var_K_m = libcellml.Variable()
    var_K_m.setName("K_m")
    # var_K_m.setInitialValue(40)
    var_K_m.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_K_m)

    var_efficiency = libcellml.Variable()
    var_efficiency.setName("efficiency")
    # var_efficiency.setInitialValue(20)
    var_efficiency.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_efficiency)

    var_t_ave = libcellml.Variable()
    var_t_ave.setName("t_ave")
    var_t_ave.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_t_ave)

    var_mRNA_halflife = libcellml.Variable()
    var_mRNA_halflife.setName("time")
    # var_mRNA_halflife.setInitialValue(2)
    var_mRNA_halflife.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_mRNA_halflife)

    # var_eff = libcellml.Variable()
    # var_eff.setName("eff")
    # var_eff.setInitialValue(20)
    # var_eff.setUnits("minute")
    # comp_parameters.addVariable(var_eff)

    # start with math
    math_ast1 = libsbml.parseL3Formula(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))"
    )
    math_str = libsbml.writeMathMLToString(math_ast1)
    print(math_str)
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    #    Include the MathML strings in the component.
    math_str = "\n".join([math_header] + math_str.split("\n")[2:])
    print(math_str)
    comp_parameters.setMath(math_str)

    ##############################################################################################

    comp_parameters = libcellml.Component()
    comp_parameters.setName("M_tetR")
    model.addComponent(comp_parameters)

    # var n: dimensionless {init: 2, pub: out};
    var_n = libcellml.Variable()
    var_n.setName("M_tetR")
    var_n.setInitialValue(0.0)
    var_n.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_n)

    var_alpha = libcellml.Variable()
    var_alpha.setName("alpha")
    var_alpha.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha)

    var_beta = libcellml.Variable()
    var_beta.setName("P_lacl")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_beta = libcellml.Variable()
    var_beta.setName("n")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_alpha_0 = libcellml.Variable()
    var_alpha_0.setName("alpha_0")
    var_alpha_0.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha_0)

    var_K_m = libcellml.Variable()
    var_K_m.setName("K_m")
    # var_K_m.setInitialValue(40)
    var_K_m.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_K_m)

    var_efficiency = libcellml.Variable()
    var_efficiency.setName("efficiency")
    # var_efficiency.setInitialValue(20)
    var_efficiency.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_efficiency)

    var_t_ave = libcellml.Variable()
    var_t_ave.setName("t_ave")
    var_t_ave.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_t_ave)

    var_mRNA_halflife = libcellml.Variable()
    var_mRNA_halflife.setName("time")
    # var_mRNA_halflife.setInitialValue(2)
    var_mRNA_halflife.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_mRNA_halflife)

    # var_eff = libcellml.Variable()
    # var_eff.setName("eff")
    # var_eff.setInitialValue(20)
    # var_eff.setUnits("minute")
    # comp_parameters.addVariable(var_eff)

    # start with math
    math_ast1 = libsbml.parseL3Formula(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))"
    )
    math_str = libsbml.writeMathMLToString(math_ast1)
    print(math_str)
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    #    Include the MathML strings in the component.
    math_str = "\n".join([math_header] + math_str.split("\n")[2:])
    print(math_str)
    comp_parameters.setMath(math_str)

    ##############################################################################################

    comp_parameters = libcellml.Component()
    comp_parameters.setName("M_cl")
    model.addComponent(comp_parameters)

    # var n: dimensionless {init: 2, pub: out};
    var_n = libcellml.Variable()
    var_n.setName("M_cl")
    var_n.setInitialValue(15.0)
    var_n.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_n)

    var_alpha = libcellml.Variable()
    var_alpha.setName("alpha")
    var_alpha.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha)

    var_beta = libcellml.Variable()
    var_beta.setName("P_tetR")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_beta = libcellml.Variable()
    var_beta.setName("n")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_alpha_0 = libcellml.Variable()
    var_alpha_0.setName("alpha_0")
    var_alpha_0.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha_0)

    var_K_m = libcellml.Variable()
    var_K_m.setName("K_m")
    # var_K_m.setInitialValue(40)
    var_K_m.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_K_m)

    var_efficiency = libcellml.Variable()
    var_efficiency.setName("efficiency")
    # var_efficiency.setInitialValue(20)
    var_efficiency.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_efficiency)

    var_t_ave = libcellml.Variable()
    var_t_ave.setName("t_ave")
    var_t_ave.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_t_ave)

    var_mRNA_halflife = libcellml.Variable()
    var_mRNA_halflife.setName("time")
    # var_mRNA_halflife.setInitialValue(2)
    var_mRNA_halflife.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_mRNA_halflife)

    # var_eff = libcellml.Variable()
    # var_eff.setName("eff")
    # var_eff.setInitialValue(20)
    # var_eff.setUnits("minute")
    # comp_parameters.addVariable(var_eff)

    # start with math
    math_ast1 = libsbml.parseL3Formula(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))"
    )
    math_str = libsbml.writeMathMLToString(math_ast1)
    print(math_str)
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    #    Include the MathML strings in the component.
    math_str = "\n".join([math_header] + math_str.split("\n")[2:])
    print(math_str)
    comp_parameters.setMath(math_str)

    ##############################################################################################

    comp_parameters = libcellml.Component()
    comp_parameters.setName("P_lacl")
    model.addComponent(comp_parameters)

    # var n: dimensionless {init: 2, pub: out};
    var_n = libcellml.Variable()
    var_n.setName("P_lacl")
    var_n.setInitialValue(0.0)
    var_n.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_n)

    var_alpha = libcellml.Variable()
    var_alpha.setName("beta")
    var_alpha.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha)

    var_beta = libcellml.Variable()
    var_beta.setName("M_lacl")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_t_ave = libcellml.Variable()
    var_t_ave.setName("t_ave")
    var_t_ave.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_t_ave)

    var_K_m = libcellml.Variable()
    var_K_m.setName("K_m")
    # var_K_m.setInitialValue(40)
    var_K_m.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_K_m)

    var_efficiency = libcellml.Variable()
    var_efficiency.setName("efficiency")
    # var_efficiency.setInitialValue(20)
    var_efficiency.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_efficiency)

    var_mRNA_halflife = libcellml.Variable()
    var_mRNA_halflife.setName("time")
    # var_mRNA_halflife.setInitialValue(2)
    var_mRNA_halflife.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_mRNA_halflife)

    # var_eff = libcellml.Variable()
    # var_eff.setName("eff")
    # var_eff.setInitialValue(20)
    # var_eff.setUnits("minute")
    # comp_parameters.addVariable(var_eff)

    # start with math
    math_ast1 = libsbml.parseL3Formula(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))"
    )
    math_str = libsbml.writeMathMLToString(math_ast1)
    print(math_str)
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    #    Include the MathML strings in the component.
    math_str = "\n".join([math_header] + math_str.split("\n")[2:])
    print(math_str)
    comp_parameters.setMath(math_str)

    ##############################################################################################

    comp_parameters = libcellml.Component()
    comp_parameters.setName("P_tetR")
    model.addComponent(comp_parameters)

    # var n: dimensionless {init: 2, pub: out};
    var_n = libcellml.Variable()
    var_n.setName("P_tetR")
    var_n.setInitialValue(0.0)
    var_n.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_n)

    var_alpha = libcellml.Variable()
    var_alpha.setName("beta")
    var_alpha.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha)

    var_beta = libcellml.Variable()
    var_beta.setName("M_tetR")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_t_ave = libcellml.Variable()
    var_t_ave.setName("t_ave")
    var_t_ave.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_t_ave)

    var_K_m = libcellml.Variable()
    var_K_m.setName("K_m")
    # var_K_m.setInitialValue(40)
    var_K_m.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_K_m)

    var_efficiency = libcellml.Variable()
    var_efficiency.setName("efficiency")
    # var_efficiency.setInitialValue(20)
    var_efficiency.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_efficiency)

    var_mRNA_halflife = libcellml.Variable()
    var_mRNA_halflife.setName("time")
    # var_mRNA_halflife.setInitialValue(2)
    var_mRNA_halflife.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_mRNA_halflife)

    # var_eff = libcellml.Variable()
    # var_eff.setName("eff")
    # var_eff.setInitialValue(20)
    # var_eff.setUnits("minute")
    # comp_parameters.addVariable(var_eff)

    # start with math
    math_ast1 = libsbml.parseL3Formula(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))"
    )
    math_str = libsbml.writeMathMLToString(math_ast1)
    print(math_str)
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    #    Include the MathML strings in the component.
    math_str = "\n".join([math_header] + math_str.split("\n")[2:])
    print(math_str)
    comp_parameters.setMath(math_str)

    ##############################################################################################

    comp_parameters = libcellml.Component()
    comp_parameters.setName("P_cl")
    model.addComponent(comp_parameters)

    # var n: dimensionless {init: 2, pub: out};
    var_n = libcellml.Variable()
    var_n.setName("P_cl")
    var_n.setInitialValue(0.0)
    var_n.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_n)

    var_alpha = libcellml.Variable()
    var_alpha.setName("beta")
    var_alpha.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_alpha)

    var_beta = libcellml.Variable()
    var_beta.setName("M_cl")
    # var_beta.setInitialValue(0.2)
    var_beta.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_beta)

    var_t_ave = libcellml.Variable()
    var_t_ave.setName("t_ave")
    var_t_ave.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_t_ave)

    var_K_m = libcellml.Variable()
    var_K_m.setName("K_m")
    # var_K_m.setInitialValue(40)
    var_K_m.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_K_m)

    var_efficiency = libcellml.Variable()
    var_efficiency.setName("efficiency")
    # var_efficiency.setInitialValue(20)
    var_efficiency.setUnits("dimensionless")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_efficiency)

    var_mRNA_halflife = libcellml.Variable()
    var_mRNA_halflife.setName("time")
    # var_mRNA_halflife.setInitialValue(2)
    var_mRNA_halflife.setUnits("minute")
    # var_n.setInterfaceType()
    comp_parameters.addVariable(var_mRNA_halflife)

    # var_eff = libcellml.Variable()
    # var_eff.setName("eff")
    # var_eff.setInitialValue(20)
    # var_eff.setUnits("minute")
    # comp_parameters.addVariable(var_eff)

    # start with math
    math_ast1 = libsbml.parseL3Formula(
        "a0_tr + (a_tr * power(KM, n)) / (power(KM, n) + power(PZ, n))"
    )
    math_str = libsbml.writeMathMLToString(math_ast1)
    print(math_str)
    math_header = '<math xmlns="http://www.w3.org/1998/Math/MathML" xmlns:cellml="http://www.cellml.org/cellml/2.0#">'
    #    Include the MathML strings in the component.
    math_str = "\n".join([math_header] + math_str.split("\n")[2:])
    print(math_str)
    comp_parameters.setMath(math_str)
    ############################################################

    comp_env = libcellml.Component()

    model.addComponent(comp_env)

    #  Checking that it worked
    print("-" * 80)
    print_model(model)
    print("-" * 80)

    # Save model
    printer = libcellml.Printer()
    serialised_model: str = printer.printModel(model)
    print("-" * 80)
    print(serialised_model)
    print("-" * 80)

    with open(cellml_path, "w") as f_cellml:
        f_cellml.write(serialised_model)

    return model


# <codecell>
def validate_model(model: libcellml.Model) -> None:
    """Validate existing model."""
    # Validation
    validator = libcellml.Validator()
    validator.validateModel(model)
    num_validation_issues = validator.issueCount()
    print(f"The validator has found {num_validation_issues} issues!")
    #      Retrieve the issues, and print their description, url, reference, and
    #      type of item stored to the terminal.  The type of stored item is
    #      available as an enum, which can be turned into a string for output using
    #      the utility function, getItemTypeFromEnum(type).

    for e in range(0, num_validation_issues):
        issue = validator.issue(e)
        reference = issue.referenceHeading()
        print("  Validator issue[{}]:".format(e))
        print("     Description: {}".format(issue.description()))
        # print('     Type of item stored: {}'.format(cellmlElementTypeAsString(issue.item().type())))
        print("     URL: {}".format(issue.url()))
        if reference != "":
            print("    See section {} in the CellML specification.".format(reference))


# <codecell>
if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR

    cellml_path: Path = RESULTS_DIR / "repressilator.cellml"
    model = create_repressilator(cellml_path)
    validate_model(model)
