from xcp2k.inputsection import InputSection
from xcp2k.classes._mixing1 import _mixing1


class _diag_sub_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_iter = None
        self.Eps_ene = None
        self.Eps_adapt_scf = None
        self.Eps_skip_sub_diag = None
        self.MIXING = _mixing1()
        self._name = "DIAG_SUB_SCF"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_ene': 'EPS_ENE', 'Eps_adapt_scf': 'EPS_ADAPT_SCF', 'Eps_skip_sub_diag': 'EPS_SKIP_SUB_DIAG'}
        self._subsections = {'MIXING': 'MIXING'}
        self._attributes = ['Section_parameters']

