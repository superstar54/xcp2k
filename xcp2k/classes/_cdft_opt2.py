from xcp2k.inputsection import InputSection


class _cdft_opt2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Broyden_type = None
        self.Jacobian_type = None
        self.Jacobian_step = None
        self.Jacobian_freq = None
        self.Jacobian_restart = None
        self.Jacobian_vector = None
        self.Max_ls = None
        self.Factor_ls = None
        self.Continue_ls = None
        self._name = "CDFT_OPT"
        self._keywords = {'Factor_ls': 'FACTOR_LS', 'Jacobian_restart': 'JACOBIAN_RESTART', 'Jacobian_freq': 'JACOBIAN_FREQ', 'Continue_ls': 'CONTINUE_LS', 'Jacobian_vector': 'JACOBIAN_VECTOR', 'Jacobian_step': 'JACOBIAN_STEP', 'Broyden_type': 'BROYDEN_TYPE', 'Max_ls': 'MAX_LS', 'Jacobian_type': 'JACOBIAN_TYPE'}

