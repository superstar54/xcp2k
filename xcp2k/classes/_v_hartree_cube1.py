from xcp2k.inputsection import InputSection
from _each246 import _each246


class _v_hartree_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Append = None
        self.EACH = _each246()
        self._name = "V_HARTREE_CUBE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Stride': 'STRIDE', 'Add_last': 'ADD_LAST', 'Append': 'APPEND'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

