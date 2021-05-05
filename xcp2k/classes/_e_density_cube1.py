from xcp2k.inputsection import InputSection
from xcp2k.classes._each364 import _each364


class _e_density_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Total_density = None
        self.Append = None
        self.Xrd_interface = None
        self.Ngauss = None
        self.EACH = _each364()
        self._name = "E_DENSITY_CUBE"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Stride': 'STRIDE', 'Total_density': 'TOTAL_DENSITY', 'Append': 'APPEND', 'Xrd_interface': 'XRD_INTERFACE', 'Ngauss': 'NGAUSS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

