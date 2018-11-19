from xcp2k.inputsection import InputSection
from _each273 import _each273


class _energy_windows1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.N_windows = None
        self.Eps_filter = None
        self.Restrict_range = None
        self.Range = None
        self.Print_cubes = None
        self.Stride = None
        self.EACH = _each273()
        self._name = "ENERGY_WINDOWS"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'N_windows': 'N_WINDOWS', 'Restrict_range': 'RESTRICT_RANGE', 'Eps_filter': 'EPS_FILTER', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Stride': 'STRIDE', 'Range': 'RANGE', 'Add_last': 'ADD_LAST', 'Print_cubes': 'PRINT_CUBES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

