from xcp2k.inputsection import InputSection
from xcp2k.classes._each662 import _each662


class _print101(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Load_balance_info = None
        self.EACH = _each662()
        self._name = "PRINT"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Load_balance_info': 'LOAD_BALANCE_INFO'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

