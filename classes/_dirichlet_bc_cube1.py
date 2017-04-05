from xcp2k.inputsection import InputSection
from _each209 import _each209


class _dirichlet_bc_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Tile_cubes = None
        self.Stride = None
        self.Append = None
        self.EACH = _each209()
        self._name = "DIRICHLET_BC_CUBE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Tile_cubes': 'TILE_CUBES', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Stride': 'STRIDE', 'Add_last': 'ADD_LAST', 'Append': 'APPEND'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

