from xcp2k.inputsection import InputSection
from xcp2k.classes._each383 import _each383


class _lowdin1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Print_gop = None
        self.Print_all = None
        self.EACH = _each383()
        self._name = "LOWDIN"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Print_gop': 'PRINT_GOP', 'Print_all': 'PRINT_ALL'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

