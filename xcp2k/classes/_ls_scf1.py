from xcp2k.inputsection import InputSection
from xcp2k.classes._curvy_steps1 import _curvy_steps1
from xcp2k.classes._chebyshev1 import _chebyshev1
from xcp2k.classes._rho_mixing1 import _rho_mixing1
from xcp2k.classes._pexsi1 import _pexsi1
from xcp2k.classes._pao1 import _pao1


class _ls_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ls_diis = None
        self.Ini_diis = None
        self.Max_diis = None
        self.Nmixing = None
        self.Eps_diis = None
        self.Max_scf = None
        self.Eps_scf = None
        self.Mixing_fraction = None
        self.Eps_filter = None
        self.Eps_lanczos = None
        self.Max_iter_lanczos = None
        self.Mu = None
        self.Fixed_mu = None
        self.Extrapolation_order = None
        self.S_preconditioner = None
        self.S_sqrt_method = None
        self.S_sqrt_order = None
        self.Purification_method = None
        self.Sign_method = None
        self.Submatrix_sign_method = None
        self.Sign_order = None
        self.Sign_symmetric = None
        self.Dynamic_threshold = None
        self.Non_monotonic = None
        self.Matrix_cluster_type = None
        self.Single_precision_matrices = None
        self.Restart_write = None
        self.Restart_read = None
        self.S_inversion = None
        self.Report_all_sparsities = None
        self.Perform_mu_scan = None
        self.Check_s_inv = None
        self.CURVY_STEPS = _curvy_steps1()
        self.CHEBYSHEV = _chebyshev1()
        self.RHO_MIXING = _rho_mixing1()
        self.PEXSI = _pexsi1()
        self.PAO = _pao1()
        self._name = "LS_SCF"
        self._keywords = {'Ls_diis': 'LS_DIIS', 'Ini_diis': 'INI_DIIS', 'Max_diis': 'MAX_DIIS', 'Nmixing': 'NMIXING', 'Eps_diis': 'EPS_DIIS', 'Max_scf': 'MAX_SCF', 'Eps_scf': 'EPS_SCF', 'Mixing_fraction': 'MIXING_FRACTION', 'Eps_filter': 'EPS_FILTER', 'Eps_lanczos': 'EPS_LANCZOS', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS', 'Mu': 'MU', 'Fixed_mu': 'FIXED_MU', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'S_preconditioner': 'S_PRECONDITIONER', 'S_sqrt_method': 'S_SQRT_METHOD', 'S_sqrt_order': 'S_SQRT_ORDER', 'Purification_method': 'PURIFICATION_METHOD', 'Sign_method': 'SIGN_METHOD', 'Submatrix_sign_method': 'SUBMATRIX_SIGN_METHOD', 'Sign_order': 'SIGN_ORDER', 'Sign_symmetric': 'SIGN_SYMMETRIC', 'Dynamic_threshold': 'DYNAMIC_THRESHOLD', 'Non_monotonic': 'NON_MONOTONIC', 'Matrix_cluster_type': 'MATRIX_CLUSTER_TYPE', 'Single_precision_matrices': 'SINGLE_PRECISION_MATRICES', 'Restart_write': 'RESTART_WRITE', 'Restart_read': 'RESTART_READ', 'S_inversion': 'S_INVERSION', 'Report_all_sparsities': 'REPORT_ALL_SPARSITIES', 'Perform_mu_scan': 'PERFORM_MU_SCAN', 'Check_s_inv': 'CHECK_S_INV'}
        self._subsections = {'CURVY_STEPS': 'CURVY_STEPS', 'CHEBYSHEV': 'CHEBYSHEV', 'RHO_MIXING': 'RHO_MIXING', 'PEXSI': 'PEXSI', 'PAO': 'PAO'}
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
