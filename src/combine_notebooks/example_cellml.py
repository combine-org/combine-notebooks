"""Example script for creating SBML repressilator with cellml.

https://www.cellml.org/getting-started/tutorials/COR-tutorial
https://models.physiomeproject.org/exposure/bee9fb9df261ba69b51897f2e49b1691/elowitz_leibler_2000.cellml/view?searchterm=repressilator

https://libcellml.org/documentation/v0.2.0/user/tutorials/tutorial3/index

opencor: https://opencor.ws/downloads/index.html

"""
from pathlib import Path

import libcellml
from cellml_utilities import print_model


def create_model(cellml_path: Path) -> libcellml.Model:
    """Create CellML repressilator and save to Path."""
    model = libcellml.Model()
    model.setName("repressilator")

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
    print(f'The validator has found {num_validation_issues} issues!')
    #      Retrieve the issues, and print their description, url, reference, and
    #      type of item stored to the terminal.  The type of stored item is
    #      available as an enum, which can be turned into a string for output using
    #      the utility function, getItemTypeFromEnum(type).

    for e in range(0, num_validation_issues):
        issue = validator.issue(e)
        reference = issue.referenceHeading()
        print('  Validator issue[{}]:'.format(e))
        print('     Description: {}'.format(issue.description()))
        # print('     Type of item stored: {}'.format(cellmlElementTypeAsString(issue.item().type())))
        print('     URL: {}'.format(issue.url()))
        if reference != '':
            print('    See section {} in the CellML specification.'.format(reference))


if __name__ == "__main__":
    from combine_notebooks import RESULTS_DIR
    cellml_path: Path = RESULTS_DIR / "repressilator.cellml"
    model = create_model(cellml_path)
    validate_model(model)