from xcp2k.inputsection import InputSection
from _each62 import _each62


class _coordinates1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Format = None
        self.EACH = _each62()
        self._name = "COORDINATES"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Format': 'FORMAT', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']
