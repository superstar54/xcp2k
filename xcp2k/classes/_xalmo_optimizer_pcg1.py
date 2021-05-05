from xcp2k.inputsection import InputSection
from xcp2k.classes._xalmo_newton_pcg_solver1 import _xalmo_newton_pcg_solver1


class _xalmo_optimizer_pcg1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_error = None
        self.Max_iter_early = None
        self.Eps_error_early = None
        self.Max_iter_outer_loop = None
        self.Preconditioner = None
        self.Lin_search_eps_error = None
        self.Lin_search_step_size_guess = None
        self.Precond_filter_threshold = None
        self.Conjugator = None
        self.XALMO_NEWTON_PCG_SOLVER = _xalmo_newton_pcg_solver1()
        self._name = "XALMO_OPTIMIZER_PCG"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_error': 'EPS_ERROR', 'Max_iter_early': 'MAX_ITER_EARLY', 'Eps_error_early': 'EPS_ERROR_EARLY', 'Max_iter_outer_loop': 'MAX_ITER_OUTER_LOOP', 'Preconditioner': 'PRECONDITIONER', 'Lin_search_eps_error': 'LIN_SEARCH_EPS_ERROR', 'Lin_search_step_size_guess': 'LIN_SEARCH_STEP_SIZE_GUESS', 'Precond_filter_threshold': 'PRECOND_FILTER_THRESHOLD', 'Conjugator': 'CONJUGATOR'}
        self._subsections = {'XALMO_NEWTON_PCG_SOLVER': 'XALMO_NEWTON_PCG_SOLVER'}

