from xcp2k.inputsection import InputSection
from _each198 import _each198


class _stm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Nlumo = None
        self.Bias = None
        self.Th_torb = []
        self.Ref_energy = None
        self.Append = None
        self.EACH = _each198()
        self._name = "STM"
        self._keywords = {'Nlumo': 'NLUMO', 'Log_print_key': 'LOG_PRINT_KEY', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Ref_energy': 'REF_ENERGY', 'Stride': 'STRIDE', 'Bias': 'BIAS', 'Add_last': 'ADD_LAST', 'Append': 'APPEND'}
        self._repeated_keywords = {'Th_torb': 'TH_TORB'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

