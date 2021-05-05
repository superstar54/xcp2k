from xcp2k.inputsection import InputSection


class _almo_optimizer_trustr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_error = None
        self.Max_iter_early = None
        self.Eps_error_early = None
        self.Max_iter_outer_loop = None
        self.Preconditioner = None
        self.Conjugator = None
        self.Algorithm = None
        self.Eta = None
        self.Model_grad_norm_ratio = None
        self.Initial_trust_radius = None
        self.Max_trust_radius = None
        self._name = "ALMO_OPTIMIZER_TRUSTR"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Eps_error': 'EPS_ERROR', 'Max_iter_early': 'MAX_ITER_EARLY', 'Eps_error_early': 'EPS_ERROR_EARLY', 'Max_iter_outer_loop': 'MAX_ITER_OUTER_LOOP', 'Preconditioner': 'PRECONDITIONER', 'Conjugator': 'CONJUGATOR', 'Algorithm': 'ALGORITHM', 'Eta': 'ETA', 'Model_grad_norm_ratio': 'MODEL_GRAD_NORM_RATIO', 'Initial_trust_radius': 'INITIAL_TRUST_RADIUS', 'Max_trust_radius': 'MAX_TRUST_RADIUS'}

