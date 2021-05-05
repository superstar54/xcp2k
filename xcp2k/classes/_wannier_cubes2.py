from xcp2k.inputsection import InputSection
from xcp2k.classes._each148 import _each148


class _wannier_cubes2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Cubes_lu_bounds = None
        self.Cubes_list = []
        self.Append = None
        self.EACH = _each148()
        self._name = "WANNIER_CUBES"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Stride': 'STRIDE', 'Cubes_lu_bounds': 'CUBES_LU_BOUNDS', 'Append': 'APPEND'}
        self._repeated_keywords = {'Cubes_list': 'CUBES_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Cubes_lu': 'Cubes_lu_bounds'}
        self._attributes = ['Section_parameters']


    @property
    def Cubes_lu(self):
        """
        See documentation for Cubes_lu_bounds
        """
        return self.Cubes_lu_bounds

    @Cubes_lu.setter
    def Cubes_lu(self, value):
        self.Cubes_lu_bounds = value
