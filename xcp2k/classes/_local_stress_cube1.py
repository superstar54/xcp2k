from xcp2k.inputsection import InputSection
from xcp2k.classes._each377 import _each377


class _local_stress_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Append = None
        self.EACH = _each377()
        self._name = "LOCAL_STRESS_CUBE"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Stride': 'STRIDE', 'Append': 'APPEND'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

