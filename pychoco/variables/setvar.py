from pychoco import backend
from pychoco._handle_wrapper import _HandleWrapper
from pychoco._utils import get_int_array
from pychoco.variables.variable import Variable


class SetVar(Variable, _HandleWrapper):
    """
    A Set Variable is defined by a domain which is a set interval [lb, ub], where:
    lb is the set of integers that must belong to every single solution.
    ub is the set of integers that may belong to at least one solution.
    In the context of SetVars, a value of the variable is a set of integers.
    """

    def get_lb(self):
        """
        :return: The lower bound of this setvar (a set of integers).
        """
        return set(get_int_array(backend.get_setvar_lb(self.handle)))

    def get_ub(self):
        """
        :return: The upper bound of this setvar (a set of integers).
        """
        return set(get_int_array(backend.get_setvar_ub(self.handle)))

    def get_value(self):
        """
        :return: The value of this set variable (only valid if it is instantiated).
        """
        return set(get_int_array(backend.get_setvar_value(self.handle)))

    def get_type(self):
        return "SetVar"
