from xcp2k.inputsection import InputSection
from _each398 import _each398


class _mo_cubes2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Mo_list = []
        self.Nlumo = None
        self.Nhomo = None
        self.EACH = _each398()
        self._name = "MO_CUBES"
        self._keywords = {'Nlumo': 'NLUMO', 'Log_print_key': 'LOG_PRINT_KEY', 'Nhomo': 'NHOMO', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Stride': 'STRIDE', 'Add_last': 'ADD_LAST'}
        self._repeated_keywords = {'Mo_list': 'MO_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

