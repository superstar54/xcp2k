from xcp2k.inputsection import InputSection
from _each274 import _each274


class _ks_csr_write1(InputSection):
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
        self.EACH = _each274()
        self._name = "KS_CSR_WRITE"
        self._keywords = {'Binary': 'BINARY', 'Log_print_key': 'LOG_PRINT_KEY', 'Upper_triangular': 'UPPER_TRIANGULAR', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Threshold': 'THRESHOLD'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

