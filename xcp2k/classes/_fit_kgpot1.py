from xcp2k.inputsection import InputSection
from xcp2k.classes._each634 import _each634


class _fit_kgpot1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Num_gaussian = None
        self.Num_polynom = None
        self.EACH = _each634()
        self._name = "FIT_KGPOT"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Num_gaussian': 'NUM_GAUSSIAN', 'Num_polynom': 'NUM_POLYNOM'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

