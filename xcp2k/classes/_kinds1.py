from xcp2k.inputsection import InputSection
from _each296 import _each296


class _kinds1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Potential = None
        self.Basis_set = None
        self.Se_parameters = None
        self.EACH = _each296()
        self._name = "KINDS"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Potential': 'POTENTIAL', 'Add_last': 'ADD_LAST', 'Basis_set': 'BASIS_SET', 'Se_parameters': 'SE_PARAMETERS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

