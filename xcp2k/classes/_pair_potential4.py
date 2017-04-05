from xcp2k.inputsection import InputSection
from _print_dftd4 import _print_dftd4


class _pair_potential4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.R_cutoff = None
        self.Type = None
        self.Parameter_file_name = None
        self.Reference_functional = None
        self.Scaling = None
        self.Exp_pre = None
        self.Eps_cn = None
        self.D3_scaling = None
        self.D3bj_scaling = None
        self.Calculate_c9_term = None
        self.Reference_c9_term = None
        self.Long_range_correction = None
        self.Verbose_output = None
        self.Kind_coordination_numbers = []
        self.Atom_coordination_numbers = []
        self.Atomparm = []
        self.PRINT_DFTD = _print_dftd4()
        self._name = "PAIR_POTENTIAL"
        self._keywords = {'Exp_pre': 'EXP_PRE', 'Reference_functional': 'REFERENCE_FUNCTIONAL', 'Verbose_output': 'VERBOSE_OUTPUT', 'Calculate_c9_term': 'CALCULATE_C9_TERM', 'Reference_c9_term': 'REFERENCE_C9_TERM', 'Scaling': 'SCALING', 'R_cutoff': 'R_CUTOFF', 'Parameter_file_name': 'PARAMETER_FILE_NAME', 'Eps_cn': 'EPS_CN', 'Long_range_correction': 'LONG_RANGE_CORRECTION', 'D3_scaling': 'D3_SCALING', 'D3bj_scaling': 'D3BJ_SCALING', 'Type': 'TYPE'}
        self._repeated_keywords = {'Atomparm': 'ATOMPARM', 'Kind_coordination_numbers': 'KIND_COORDINATION_NUMBERS', 'Atom_coordination_numbers': 'ATOM_COORDINATION_NUMBERS'}
        self._subsections = {'PRINT_DFTD': 'PRINT_DFTD'}

