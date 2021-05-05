from xcp2k.inputsection import InputSection


class _xalmo_newton_pcg_solver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_error = None
        self.Max_iter_early = None
        self.Eps_error_early = None
        self.Max_iter_outer_loop = None
        self.Preconditioner = None
        self._name = "XALMO_NEWTON_PCG_SOLVER"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_error': 'EPS_ERROR', 'Max_iter_early': 'MAX_ITER_EARLY', 'Eps_error_early': 'EPS_ERROR_EARLY', 'Max_iter_outer_loop': 'MAX_ITER_OUTER_LOOP', 'Preconditioner': 'PRECONDITIONER'}

