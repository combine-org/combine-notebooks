"""Helpers for cellml."""

import string

import libcellml
from libcellml import Issue


def print_model(model: libcellml.Model, include_maths: bool = False) -> None:
    """Print model."""
    if model is None:
        print("No model passed to this function.")
        return

    spacer = "    "
    print(f"MODEL: '{model.name()}'", end="")
    if model.id() != "":
        print(f", id: '{model.id()}'", end="")

    print()

    print(spacer + f"UNITS: {model.unitsCount()} custom units")
    for u in range(0, model.unitsCount()):
        print(spacer + spacer + f"[{u}]: {model.units(u).name()}", end="")
        if model.units(u).isImport():
            print(", imported from: '", end="")
            print(model.units(u).importReference(), end="")
            print(f"' in '{model.units(u).importSource().url()}'", end="")

        print()

    print(spacer + "COMPONENTS: {n} components".format(n=model.componentCount()))
    for c in range(0, model.componentCount()):
        component = model.component(c)
        print_component_to_terminal(component, c, spacer + spacer, include_maths)


def print_component_to_terminal(
    component: libcellml.Component, c: int, spacer: str, include_maths: bool = False
) -> None:
    """Print document to terminal."""
    local = "    "
    # Print this component
    print(f"{spacer}[{c}]: '{component.name()}'", end="")
    if component.id() != "":
        print(f", id: '{component.id()}'", end="")
    if component.isImport():
        print(" <--- imported from: '", end="")
        print(component.importReference(), end="")
        print(f"' in '{component.importSource().url()}'", end="")

    print()

    print(spacer + local + f"VARIABLES: {component.variableCount()} variables")
    # Print variables in this component
    for v in range(0, component.variableCount()):
        print(spacer + local + local, end="")
        print("[{}]: {}".format(v, component.variable(v).name()), end="")
        if component.variable(v).units() is not None:
            print(" [{}]".format(component.variable(v).units().name()), end="")
        if component.variable(v).initialValue() != "":
            print(", initial = {}".format(component.variable(v).initialValue()), end="")
        print()
        if component.variable(v).equivalentVariableCount() > 0:
            print(spacer + local + local + local, end="")
            con = "  └──> "
            for e in range(0, component.variable(v).equivalentVariableCount()):
                ev = component.variable(v).equivalentVariable(e)
                if ev is None:
                    print("WHOOPS! Null equivalent variable!")
                    continue

                ev_parent = ev.parent()
                if ev_parent is None:
                    print("WHOOPS! Null parent component for equivalent variable!")
                    continue

                print("{}{}:{}".format(con, ev_parent.name(), ev.name()), end="")
                if ev.units() is not None:
                    print(" [{}]".format(ev.units().name()), end="")

                con = ", "
            print()
    if include_maths and component.math():
        print(spacer + "  Maths in the component is:")
        print(component.math())

    # Print the encapsulated components inside this one
    if component.componentCount() > 0:
        print(
            f"{spacer}{local}COMPONENT {component.name()} has {component.componentCount()} child components:"
        )

        for c2 in range(0, component.componentCount()):
            child = component.component(c2)
            one_more_spacer = spacer + local + local
            print_component_to_terminal(child, c2, one_more_spacer, include_maths)


level_as_string = {
    Issue.Level.ERROR: "an ERROR",
    Issue.Level.WARNING: "a WARNING",
    Issue.Level.MESSAGE: "a MESSAGE",
}

# def print_issues(item):
#
#     # Get the number of issues attached to the logger item.  Note that this will
#     # return issues of all levels.  To retrieve the total number of a specific level
#     # of issues, use the errorCount(), warningCount(), hintCount(), or messageCount() functions.
#     number_of_issues = item.issueCount()
#     print(f"Recorded {number_of_issues} issues", end="")
#
#     if number_of_issues != 0:
#         print(":")
#         for e in range(0, number_of_issues):
#
#             # Retrieve the issue at index i.  Note that this is agnostic as to the level of issue.
#             # Specific issue levels can be retrieved using the functions item.error(e), item.warning(e)
#             # etc, where the index must be within appropriate limits.
#             i = item.issue(e)
#
#             # The level of an issue is retrieved using the level() function as an enum value.
#             level = i.level()
#             print(f"Issue {e} is {level_as_string[level]}:")
#
#             # Each issue has a descriptive text field, accessible through the description() function.
#             print("    Description: {d}".format(
#                 d=i.description()))
#
#             # Issues created by the Validator class contain a reference heading number, which indicates
#             # the section reference within the normative specification relevant to the issue.
#             specification = i.referenceHeading()
#             if specification != "":
#                 print("    See section {s} in the CellML specification.".format(
#                     s=specification))
#
#             # An optional URL is given for some issues which directs the user to more detailed information.
#             url = i.url()
#             if url != "":
#                 print("    More information is available at: {url}".format(
#                     url=url))
#
#             # Each issue is associated with an item.  In order to properly deal with the item stored, its type is
#             # recorded too in an enumeration.
#             print("    Stored item type: {}".format(cellmlElementTypeAsString(i.item().type())))
#         print()
#     else:
#         print("!")
#         print()


# def print_component_only_to_terminal(component, spacer):
#
#     print("{s}Component '{c}' has {n} child components".format(
#         s=spacer,
#         c=component.name(),
#         n=component.componentCount()))
#
#     for c in range(0, component.componentCount()):
#         another_spacer = "    " + spacer
#         child_component = component.component(c)
#         print_component_only_to_terminal(child_component, another_spacer)
#
#
# def print_encapsulation(model):
#     # Prints the encapsulation structure of the model to the terminal
#     spacer = "  - "
#     print("Model '{m}' has {c} components".format(
#         m=model.name(), c=model.componentCount()))
#
#     for c in range(0, model.componentCount()):
#         child_component = model.component(c)
#         print_component_only_to_terminal(child_component, spacer)
#
#
# def get_model_type_from_enum(my_type):
#
#     my_type_as_string = "dunno"
#
#     if my_type == Generator.ModelType.UNKNOWN:
#         my_type_as_string = "UNKNOWN"
#     elif my_type == Generator.ModelType.ALGEBRAIC:
#         my_type_as_string = "ALGEBRAIC"
#     elif my_type == Generator.ModelType.ODE:
#         my_type_as_string = "ODE"
#     elif my_type == Generator.ModelType.INVALID:
#         my_type_as_string = "INVALID"
#     elif my_type == Generator.ModelType.UNDERCONSTRAINED:
#         my_type_as_string = "UNDERCONSTRAINED"
#     elif my_type == Generator.ModelType.OVERCONSTRAINED:
#         my_type_as_string = "OVERCONSTRAINED"
#     elif my_type == Generator.ModelType.UNSUITABLY_CONSTRAINED:
#         my_type_as_string = "UNSUITABLY_CONSTRAINED"
#
#     return my_type_as_string
#
#
# def get_profile_from_enum(my_type):
#
#     my_type_as_string = "dunno"
#
#     if my_type == GeneratorProfile.Profile.C:
#         my_type_as_string = "C"
#     elif my_type == GeneratorProfile.Profile.PYTHON:
#         my_type_as_string = "PYTHON"
#
#     return my_type_as_string
#
# # START get_issue_level_from_enum
# def get_issue_level_from_enum(my_level):
#
#     my_type_as_string = "dunno"
#
#     if my_level == Issue.Level.ERROR:
#         my_type_as_string = "ERROR"
#
#     elif my_level == Issue.Level.WARNING:
#         my_type_as_string = "WARNING"
#
#     elif my_level == Issue.Level.MESSAGE:
#         my_type_as_string = "MESSAGE"
#
#     return my_type_as_string
# # END get_issue_level_from_enum
#
# # START print_equivalent_variable_set
# def list_equivalent_variables(variable, variable_set):
#     if variable is None:
#         return
#     for i in range(0, variable.equivalentVariableCount()):
#         equivalent_variable = variable.equivalentVariable(i)
#         if equivalent_variable not in variable_set:
#             variable_set.push_back(equivalent_variable)
#             list_equivalent_variables(equivalent_variable, variable_set)
#
#
# def print_equivalent_variable_set(variable):
#
#     if variable is None:
#         print("None variable submitted to print_equivalent_variable_set.")
#         return
#
#     variable_set = set()
#     variable_set.add(variable)
#     list_equivalent_variables(variable, variable_set)
#
#     component = variable.parent()
#     print_me = ''
#     if component != None:
#         print_me += "Tracing: {c}.{v}".format(
#             c=component.name(), v=variable.name())
#         if variable.units() is not None:
#             print_me += " [{u}]".format(u=variable.units().name())
#
#         if variable.initialValue() != "":
#             print_me += ", initial = {i}".format(i=variable.initialValue())
# CellmlElementType, cellmlElementTypeAsString
#         print(print_me)
#
#     if len(variable_set) > 1:
#         for e in variable_set:
#             print_me = ''
#             component = e.parent()
#             if component is not None:
#                 print_me += "    - {c}.{v}".format(
#                     c=component.name(), v=e.name())
#                 if e.units() is not None:
#                     print_me += " [{u}]".format(u=e.units().name())
#                 if e.initialValue() != "":
#                     print_me += ", initial = {i}".format(i=e.initialValue())
#                 print(print_me)
#             else:
#                 print(
#                     "Variable {v} does not have a parent component.".format(v=e.name()))
#         else:
#             print("    - Not connected to any equivalent variables.")
# END print_equivalent_variable_set
