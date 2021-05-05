from xcp2k.inputsection import InputSection
from xcp2k.classes._each389 import _each389


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
        self.EACH = _each389()
        self._name = "ENERGY_WINDOWS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'N_windows': 'N_WINDOWS', 'Eps_filter': 'EPS_FILTER', 'Restrict_range': 'RESTRICT_RANGE', 'Range': 'RANGE', 'Print_cubes': 'PRINT_CUBES', 'Stride': 'STRIDE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

