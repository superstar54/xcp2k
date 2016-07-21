from xcp2k.inputsection import InputSection


class _eigensolver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N = None
        self.N_loop = None
        self.Diag_method = None
        self.Eigenvalues = None
        self.Init_method = None
        self._name = "EIGENSOLVER"
        self._keywords = {'Diag_method': 'DIAG_METHOD', 'N_loop': 'N_LOOP', 'Init_method': 'INIT_METHOD', 'Eigenvalues': 'EIGENVALUES', 'N': 'N'}

