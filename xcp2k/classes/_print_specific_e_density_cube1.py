from xcp2k.inputsection import InputSection
from xcp2k.classes._each117 import _each117


class _print_specific_e_density_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Min_energy = None
        self.Max_energy = None
        self.EACH = _each117()
        self._name = "PRINT_SPECIFIC_E_DENSITY_CUBE"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Stride': 'STRIDE', 'Min_energy': 'MIN_ENERGY', 'Max_energy': 'MAX_ENERGY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

