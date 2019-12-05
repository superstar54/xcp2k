from xcp2k.inputsection import InputSection
from xcp2k.classes._each275 import _each275


class _s_csr_write1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Threshold = None
        self.Upper_triangular = None
        self.Binary = None
        self.EACH = _each275()
        self._name = "S_CSR_WRITE"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Threshold': 'THRESHOLD', 'Upper_triangular': 'UPPER_TRIANGULAR', 'Binary': 'BINARY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

