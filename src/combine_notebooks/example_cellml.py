"""Example script for creating SBML repressilator with cellml.

https://www.cellml.org/getting-started/tutorials/COR-tutorial
https://models.physiomeproject.org/exposure/bee9fb9df261ba69b51897f2e49b1691/elowitz_leibler_2000.cellml/view?searchterm=repressilator

https://libcellml.org/documentation/v0.2.0/user/tutorials/tutorial3/index

opencor: https://opencor.ws/downloads/index.html

Issues: https://github.com/cellml/libcellml/issues/1017

"""
from pathlib import Path

import libcellml
from cellml_utilities import print_model

import libsbml

def create_model(cellml_path: Path) -> libcellml.Model:
    """Create CellML repressilator and save to Path."""
    model = libcellml.Model()
    model.setName("repressilator")

    '''
    <units name="minute">
      <unit units="second" multiplier="60"/>
    </units>
    <units name="first_order_rate_constant">
        <unit units="minute" exponent="-1"/>
    </units>
    '''
    minute = libcellml.Units("minute")
    minute.addUnit("second", 1, 60)  
    model.addUnits(minute)

    # first_order_rate_constant = libcellml.Units("minute")
    # first_order_rate_constant.addUnit("minute")
    # model.addUnits(first_order_rate_constant)

    '''
    <component name="environment">
      <variable units="minute" public_interface="out" name="time" cmeta:id="environment_time"/>
    </component>
    '''
    comp_env = libcellml.Component()
    comp_env.setName("environment")
    model.addComponent(comp_env)
    
    var_n = libcellml.Variable()
    var_n.setName("time")
    # var_n.setInterfaceType("out")
    var_n.setUnits("minute")
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

    math_ast1: libsbml.ASTNode = libsbml.parseL3Formula( "eff / t_ave")
    var_math_ast1 = libsbml.writeMathMLToString(math_ast1)
    print(var_math_ast1)
    comp_parameters.setMath(var_math_ast1)
    
    #  Checking that it worked
    print_model(model)

    # Save model
    printer = libcellml.Printer()
    serialised_model: str = printer.printModel(model)

    with open(cellml_path, "w") as f_cellml:
        f_cellml.write(serialised_model)

    return model


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


if __name__ == "__main__":
    # from combine_notebooks import RESULTS_DIR
    RESOURCES_DIR: Path = Path(__file__).parent / "resources"
    RESULTS_DIR: Path = RESOURCES_DIR / "results"

    cellml_path: Path = RESULTS_DIR / "repressilator.cellml"
    model = create_model(cellml_path)
    validate_model(model)
