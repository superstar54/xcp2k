from xcp2k.inputsection import InputSection
from xcp2k.classes._each42 import _each42


class _rotational_info2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Coordinates = None
        self.EACH = _each42()
        self._name = "ROTATIONAL_INFO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Coordinates': 'COORDINATES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

