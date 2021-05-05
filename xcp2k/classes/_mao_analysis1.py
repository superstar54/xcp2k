from xcp2k.inputsection import InputSection
from xcp2k.classes._each385 import _each385


class _mao_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Eps_filter = None
        self.Reference_basis = None
        self.Print_basis = None
        self.Eps_grad = None
        self.Eps_function = None
        self.Max_iter = None
        self.Neglect_abc = None
        self.Ab_threshold = None
        self.Abc_threshold = None
        self.Analyze_unassigned_charge = None
        self.EACH = _each385()
        self._name = "MAO_ANALYSIS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Eps_filter': 'EPS_FILTER', 'Reference_basis': 'REFERENCE_BASIS', 'Print_basis': 'PRINT_BASIS', 'Eps_grad': 'EPS_GRAD', 'Eps_function': 'EPS_FUNCTION', 'Max_iter': 'MAX_ITER', 'Neglect_abc': 'NEGLECT_ABC', 'Ab_threshold': 'AB_THRESHOLD', 'Abc_threshold': 'ABC_THRESHOLD', 'Analyze_unassigned_charge': 'ANALYZE_UNASSIGNED_CHARGE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

