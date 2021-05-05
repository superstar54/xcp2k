from xcp2k.inputsection import InputSection
from xcp2k.classes._each204 import _each204


class _write_simple_grid1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Units = None
        self.Fold_coord = None
        self.EACH = _each204()
        self._name = "WRITE_SIMPLE_GRID"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Stride': 'STRIDE', 'Units': 'UNITS', 'Fold_coord': 'FOLD_COORD'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

