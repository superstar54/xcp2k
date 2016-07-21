from xcp2k.inputsection import InputSection
from _each218 import _each218


class _hirshfeld1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Self_consistent = None
        self.Shape_function = None
        self.Reference_charge = None
        self.EACH = _each218()
        self._name = "HIRSHFELD"
        self._keywords = {'Reference_charge': 'REFERENCE_CHARGE', 'Log_print_key': 'LOG_PRINT_KEY', 'Shape_function': 'SHAPE_FUNCTION', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Self_consistent': 'SELF_CONSISTENT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

