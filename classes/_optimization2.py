from xcp2k.inputsection import InputSection


class _optimization2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_scf = None
        self.Damping = None
        self.Eps_diis = None
        self.N_diis = None
        self._name = "OPTIMIZATION"
        self._keywords = {'Eps_diis': 'EPS_DIIS', 'Max_iter': 'MAX_ITER', 'Eps_scf': 'EPS_SCF', 'Damping': 'DAMPING', 'N_diis': 'N_DIIS'}

