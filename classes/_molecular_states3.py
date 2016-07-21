from xcp2k.inputsection import InputSection
from _each307 import _each307
from _cubes5 import _cubes5


class _molecular_states3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Cube_eval_range = None
        self.Mark_states = []
        self.EACH = _each307()
        self.CUBES = _cubes5()
        self._name = "MOLECULAR_STATES"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Cube_eval_range': 'CUBE_EVAL_RANGE', 'Filename': 'FILENAME'}
        self._repeated_keywords = {'Mark_states': 'MARK_STATES'}
        self._subsections = {'CUBES': 'CUBES', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']
