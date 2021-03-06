from xcp2k.inputsection import InputSection


class _xalmo_optimizer_pcg1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_error = None
        self.Lin_search_eps_error = None
        self.Lin_search_step_size_guess = None
        self.Max_iter_outer_loop = None
        self.Preconditioner = None
        self.Conjugator = None
        self._name = "XALMO_OPTIMIZER_PCG"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_error': 'EPS_ERROR', 'Lin_search_eps_error': 'LIN_SEARCH_EPS_ERROR', 'Lin_search_step_size_guess': 'LIN_SEARCH_STEP_SIZE_GUESS', 'Max_iter_outer_loop': 'MAX_ITER_OUTER_LOOP', 'Preconditioner': 'PRECONDITIONER', 'Conjugator': 'CONJUGATOR'}

