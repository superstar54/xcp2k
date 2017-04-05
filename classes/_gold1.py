from xcp2k.inputsection import InputSection


class _gold1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Initial_step = None
        self.Brack_limit = None
        self.Brent_tol = None
        self.Brent_max_iter = None
        self._name = "GOLD"
        self._keywords = {'Brent_tol': 'BRENT_TOL', 'Brack_limit': 'BRACK_LIMIT', 'Initial_step': 'INITIAL_STEP', 'Brent_max_iter': 'BRENT_MAX_ITER'}

