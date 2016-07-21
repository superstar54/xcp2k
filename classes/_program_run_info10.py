from xcp2k.inputsection import InputSection
from _each73 import _each73


class _program_run_info10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Initial_configuration_info = None
        self.EACH = _each73()
        self._name = "PROGRAM_RUN_INFO"
        self._keywords = {'Initial_configuration_info': 'INITIAL_CONFIGURATION_INFO', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

