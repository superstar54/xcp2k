from xcp2k.inputsection import InputSection
from xcp2k.classes._print_dftd5 import _print_dftd5


class _pair_potential5(InputSection):
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
        self.Short_range_correction = None
        self.Short_range_correction_parameters = None
        self.Molecule_correction = None
        self.Molecule_correction_c8 = None
        self.Verbose_output = None
        self.D3_exclude_kind = None
        self.D3_exclude_kind_pair = []
        self.Kind_coordination_numbers = []
        self.Atom_coordination_numbers = []
        self.Atomparm = []
        self.PRINT_DFTD = _print_dftd5()
        self._name = "PAIR_POTENTIAL"
        self._keywords = {'R_cutoff': 'R_CUTOFF', 'Type': 'TYPE', 'Parameter_file_name': 'PARAMETER_FILE_NAME', 'Reference_functional': 'REFERENCE_FUNCTIONAL', 'Scaling': 'SCALING', 'Exp_pre': 'EXP_PRE', 'Eps_cn': 'EPS_CN', 'D3_scaling': 'D3_SCALING', 'D3bj_scaling': 'D3BJ_SCALING', 'Calculate_c9_term': 'CALCULATE_C9_TERM', 'Reference_c9_term': 'REFERENCE_C9_TERM', 'Long_range_correction': 'LONG_RANGE_CORRECTION', 'Short_range_correction': 'SHORT_RANGE_CORRECTION', 'Short_range_correction_parameters': 'SHORT_RANGE_CORRECTION_PARAMETERS', 'Molecule_correction': 'MOLECULE_CORRECTION', 'Molecule_correction_c8': 'MOLECULE_CORRECTION_C8', 'Verbose_output': 'VERBOSE_OUTPUT', 'D3_exclude_kind': 'D3_EXCLUDE_KIND'}
        self._repeated_keywords = {'D3_exclude_kind_pair': 'D3_EXCLUDE_KIND_PAIR', 'Kind_coordination_numbers': 'KIND_COORDINATION_NUMBERS', 'Atom_coordination_numbers': 'ATOM_COORDINATION_NUMBERS', 'Atomparm': 'ATOMPARM'}
        self._subsections = {'PRINT_DFTD': 'PRINT_DFTD'}

