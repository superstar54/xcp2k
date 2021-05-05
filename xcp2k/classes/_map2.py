from xcp2k.inputsection import InputSection
from xcp2k.classes._each472 import _each472


class _map2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Range = []
        self.Grid_spacing = []
        self.EACH = _each472()
        self._name = "MAP"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY'}
        self._repeated_keywords = {'Range': 'RANGE', 'Grid_spacing': 'GRID_SPACING'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

