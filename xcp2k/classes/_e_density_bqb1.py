from xcp2k.inputsection import InputSection
from xcp2k.classes._each368 import _each368


class _e_density_bqb1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Skip_first = None
        self.Store_step_number = None
        self.Check = None
        self.Overwrite = None
        self.History = None
        self.Parameter_key = None
        self.Optimize = None
        self.EACH = _each368()
        self._name = "E_DENSITY_BQB"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Skip_first': 'SKIP_FIRST', 'Store_step_number': 'STORE_STEP_NUMBER', 'Check': 'CHECK', 'Overwrite': 'OVERWRITE', 'History': 'HISTORY', 'Parameter_key': 'PARAMETER_KEY', 'Optimize': 'OPTIMIZE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

