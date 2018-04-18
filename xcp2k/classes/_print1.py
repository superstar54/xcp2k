from xcp2k.inputsection import InputSection
from _each5 import _each5


class _print1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Basic_data_types = None
        self.Physcon = None
        self.Spherical_harmonics = None
        self.Rng_matrices = None
        self.Rng_check = None
        self.Global_gaussian_rng = None
        self.EACH = _each5()
        self._name = "PRINT"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Global_gaussian_rng': 'GLOBAL_GAUSSIAN_RNG', 'Rng_check': 'RNG_CHECK', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Spherical_harmonics': 'SPHERICAL_HARMONICS', 'Add_last': 'ADD_LAST', 'Physcon': 'PHYSCON', 'Rng_matrices': 'RNG_MATRICES', 'Basic_data_types': 'BASIC_DATA_TYPES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

