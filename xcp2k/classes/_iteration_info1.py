from xcp2k.inputsection import InputSection
from xcp2k.classes._each104 import _each104


class _iteration_info1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Time_cumul = None
        self.EACH = _each104()
        self._name = "ITERATION_INFO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Time_cumul': 'TIME_CUMUL'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

