from xcp2k.inputsection import InputSection


class _ls_solver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_filter = None
        self.Eps_lanczos = None
        self.Max_iter_lanczos = None
        self.Mu = None
        self.Fixed_mu = None
        self.Extrapolation_order = None
        self.S_preconditioner = None
        self.S_sqrt_method = None
        self.S_sqrt_order = None
        self.Sign_method = None
        self.Sign_order = None
        self.Dynamic_threshold = None
        self.Non_monotonic = None
        self.Matrix_cluster_type = None
        self.Single_precision_matrices = None
        self.S_inversion = None
        self.Report_all_sparsities = None
        self.Check_s_inv = None
        self._name = "LS_SOLVER"
        self._keywords = {'Eps_filter': 'EPS_FILTER', 'Eps_lanczos': 'EPS_LANCZOS', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS', 'Mu': 'MU', 'Fixed_mu': 'FIXED_MU', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'S_preconditioner': 'S_PRECONDITIONER', 'S_sqrt_method': 'S_SQRT_METHOD', 'S_sqrt_order': 'S_SQRT_ORDER', 'Sign_method': 'SIGN_METHOD', 'Sign_order': 'SIGN_ORDER', 'Dynamic_threshold': 'DYNAMIC_THRESHOLD', 'Non_monotonic': 'NON_MONOTONIC', 'Matrix_cluster_type': 'MATRIX_CLUSTER_TYPE', 'Single_precision_matrices': 'SINGLE_PRECISION_MATRICES', 'S_inversion': 'S_INVERSION', 'Report_all_sparsities': 'REPORT_ALL_SPARSITIES', 'Check_s_inv': 'CHECK_S_INV'}
        self._aliases = {'Sign_sqrt_order': 'S_sqrt_order'}


    @property
    def Sign_sqrt_order(self):
        """
        See documentation for S_sqrt_order
        """
        return self.S_sqrt_order

    @Sign_sqrt_order.setter
    def Sign_sqrt_order(self, value):
        self.S_sqrt_order = value
