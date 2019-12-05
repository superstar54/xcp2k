from xcp2k.inputsection import InputSection
from xcp2k.classes._each301 import _each301


class _ff_info1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Spline_info = None
        self.Spline_data = None
        self.EACH = _each301()
        self._name = "FF_INFO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Spline_info': 'SPLINE_INFO', 'Spline_data': 'SPLINE_DATA'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

