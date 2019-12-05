from xcp2k.inputsection import InputSection
from xcp2k.classes._each365 import _each365
from xcp2k.classes._cubes7 import _cubes7


class _molecular_states4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Cube_eval_range = None
        self.Mark_states = []
        self.EACH = _each365()
        self.CUBES = _cubes7()
        self._name = "MOLECULAR_STATES"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Cube_eval_range': 'CUBE_EVAL_RANGE'}
        self._repeated_keywords = {'Mark_states': 'MARK_STATES'}
        self._subsections = {'EACH': 'EACH', 'CUBES': 'CUBES'}
        self._attributes = ['Section_parameters']

