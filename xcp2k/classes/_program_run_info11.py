from xcp2k.inputsection import InputSection
from xcp2k.classes._each99 import _each99


class _program_run_info11(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Mo_overlap_matrix = None
        self.Mo_overlap_eigenvalues = None
        self.EACH = _each99()
        self._name = "PROGRAM_RUN_INFO"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Mo_overlap_matrix': 'MO_OVERLAP_MATRIX', 'Mo_overlap_eigenvalues': 'MO_OVERLAP_EIGENVALUES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

