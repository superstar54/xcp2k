from xcp2k.inputsection import InputSection


class _krylov2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nkrylov = None
        self.Nblock = None
        self.Eps_krylov = None
        self.Eps_std_diag = None
        self.Check_mos_conv = None
        self._name = "KRYLOV"
        self._keywords = {'Nkrylov': 'NKRYLOV', 'Nblock': 'NBLOCK', 'Eps_krylov': 'EPS_KRYLOV', 'Eps_std_diag': 'EPS_STD_DIAG', 'Check_mos_conv': 'CHECK_MOS_CONV'}

