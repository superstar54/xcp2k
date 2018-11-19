from xcp2k.inputsection import InputSection
from _cdft_opt1 import _cdft_opt1


class _outer_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Type = None
        self.Optimizer = None
        self.Bisect_trust_count = None
        self.Eps_scf = None
        self.Diis_buffer_length = None
        self.Extrapolation_order = None
        self.Max_scf = None
        self.Step_size = None
        self.CDFT_OPT = _cdft_opt1()
        self._name = "OUTER_SCF"
        self._keywords = {'Optimizer': 'OPTIMIZER', 'Diis_buffer_length': 'DIIS_BUFFER_LENGTH', 'Max_scf': 'MAX_SCF', 'Step_size': 'STEP_SIZE', 'Eps_scf': 'EPS_SCF', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'Bisect_trust_count': 'BISECT_TRUST_COUNT', 'Type': 'TYPE'}
        self._subsections = {'CDFT_OPT': 'CDFT_OPT'}
        self._attributes = ['Section_parameters']

