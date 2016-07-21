from xcp2k.inputsection import InputSection
from _each161 import _each161
from _cubes1 import _cubes1


class _molecular_states1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Cube_eval_range = None
        self.Mark_states = []
        self.EACH = _each161()
        self.CUBES = _cubes1()
        self._name = "MOLECULAR_STATES"
        self._keywords = {'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Cube_eval_range': 'CUBE_EVAL_RANGE', 'Filename': 'FILENAME'}
        self._repeated_keywords = {'Mark_states': 'MARK_STATES'}
        self._subsections = {'CUBES': 'CUBES', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']
