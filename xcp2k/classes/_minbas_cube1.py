from xcp2k.inputsection import InputSection
from _each271 import _each271


class _minbas_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Atom_list = []
        self.EACH = _each271()
        self._name = "MINBAS_CUBE"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Stride': 'STRIDE', 'Filename': 'FILENAME'}
        self._repeated_keywords = {'Atom_list': 'ATOM_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

