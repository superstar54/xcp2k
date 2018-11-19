from xcp2k.inputsection import InputSection
from _each234 import _each234


class _mo_cubes1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Write_cube = None
        self.Nlumo = None
        self.Nhomo = None
        self.Homo_list = []
        self.Append = None
        self.EACH = _each234()
        self._name = "MO_CUBES"
        self._keywords = {'Nlumo': 'NLUMO', 'Log_print_key': 'LOG_PRINT_KEY', 'Nhomo': 'NHOMO', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Write_cube': 'WRITE_CUBE', 'Filename': 'FILENAME', 'Stride': 'STRIDE', 'Add_last': 'ADD_LAST', 'Append': 'APPEND'}
        self._repeated_keywords = {'Homo_list': 'HOMO_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

