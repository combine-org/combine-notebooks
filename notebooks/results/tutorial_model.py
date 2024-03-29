# The content of this file was generated using the Python profile of libCellML 0.4.0.

from enum import Enum
from math import *


__version__ = "0.3.1"
LIBCELLML_VERSION = "0.4.0"

STATE_COUNT = 1
VARIABLE_COUNT = 1


class VariableType(Enum):
    VARIABLE_OF_INTEGRATION = 0
    STATE = 1
    CONSTANT = 2
    COMPUTED_CONSTANT = 3
    ALGEBRAIC = 4


VOI_INFO = {"name": "t", "units": "second", "component": "cancer_cells_component", "type": VariableType.VARIABLE_OF_INTEGRATION}

STATE_INFO = [
    {"name": "x", "units": "cell", "component": "cancer_cells_component", "type": VariableType.STATE}
]

VARIABLE_INFO = [
    {"name": "C", "units": "cell_per_second2", "component": "cancer_cells_component", "type": VariableType.CONSTANT}
]


def create_states_array():
    return [nan]*STATE_COUNT


def create_variables_array():
    return [nan]*VARIABLE_COUNT


def initialise_variables(states, variables):
    variables[0] = 1.0
    states[0] = 1.0


def compute_computed_constants(variables):
    pass


def compute_rates(voi, states, rates, variables):
    rates[0] = variables[0]*voi


def compute_variables(voi, states, rates, variables):
    pass
