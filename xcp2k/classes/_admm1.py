from xcp2k.inputsection import InputSection
from xcp2k.classes._each644 import _each644
from xcp2k.classes._admm_basis1 import _admm_basis1


class _admm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each644()
        self.ADMM_BASIS = _admm_basis1()
        self._name = "ADMM"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY'}
        self._subsections = {'EACH': 'EACH', 'ADMM_BASIS': 'ADMM_BASIS'}
        self._attributes = ['Section_parameters']

