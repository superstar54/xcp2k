from xcp2k.inputsection import InputSection
from xcp2k.classes._each378 import _each378


class _dos2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Append = None
        self.Delta_e = None
        self.EACH = _each378()
        self._name = "DOS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Append': 'APPEND', 'Delta_e': 'DELTA_E'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

