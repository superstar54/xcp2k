from xcp2k.inputsection import InputSection
from _each243 import _each243


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
        self.EACH = _each243()
        self._name = "FF_INFO"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Spline_data': 'SPLINE_DATA', 'Spline_info': 'SPLINE_INFO'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

