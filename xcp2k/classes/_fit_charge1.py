from xcp2k.inputsection import InputSection
from xcp2k.classes._each556 import _each556


class _fit_charge1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Type_of_density = None
        self.EACH = _each556()
        self._name = "FIT_CHARGE"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Type_of_density': 'TYPE_OF_DENSITY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

