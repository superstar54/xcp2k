from xcp2k.inputsection import InputSection


class _almo_optimizer_diis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_error = None
        self.Max_iter_early = None
        self.Eps_error_early = None
        self.N_diis = None
        self._name = "ALMO_OPTIMIZER_DIIS"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_error': 'EPS_ERROR', 'Max_iter_early': 'MAX_ITER_EARLY', 'Eps_error_early': 'EPS_ERROR_EARLY', 'N_diis': 'N_DIIS'}

