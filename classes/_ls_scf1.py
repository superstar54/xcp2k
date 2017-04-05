from xcp2k.inputsection import InputSection
from _curvy_steps1 import _curvy_steps1
from _chebyshev1 import _chebyshev1
from _rho_mixing1 import _rho_mixing1
from _pexsi1 import _pexsi1
from _pao1 import _pao1


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
        self.Purification_method = None
        self.Dynamic_threshold = None
        self.Non_monotonic = None
        self.Matrix_cluster_type = None
        self.Single_precision_matrices = None
        self.Restart_write = None
        self.Restart_read = None
        self.S_inversion = None
        self.Sign_sqrt_order = None
        self.Report_all_sparsities = None
        self.Perform_mu_scan = None
        self.Check_s_inv = None
        self.CURVY_STEPS = _curvy_steps1()
        self.CHEBYSHEV = _chebyshev1()
        self.RHO_MIXING = _rho_mixing1()
        self.PEXSI = _pexsi1()
        self.PAO = _pao1()
        self._name = "LS_SCF"
        self._keywords = {'Matrix_cluster_type': 'MATRIX_CLUSTER_TYPE', 'Eps_lanczos': 'EPS_LANCZOS', 'Purification_method': 'PURIFICATION_METHOD', 'Eps_filter': 'EPS_FILTER', 'Eps_diis': 'EPS_DIIS', 'Eps_scf': 'EPS_SCF', 'Report_all_sparsities': 'REPORT_ALL_SPARSITIES', 'Max_scf': 'MAX_SCF', 'Restart_write': 'RESTART_WRITE', 'Sign_sqrt_order': 'SIGN_SQRT_ORDER', 'Mixing_fraction': 'MIXING_FRACTION', 'Non_monotonic': 'NON_MONOTONIC', 'Max_diis': 'MAX_DIIS', 'Ini_diis': 'INI_DIIS', 'S_preconditioner': 'S_PRECONDITIONER', 'Single_precision_matrices': 'SINGLE_PRECISION_MATRICES', 'Nmixing': 'NMIXING', 'Check_s_inv': 'CHECK_S_INV', 'S_inversion': 'S_INVERSION', 'Mu': 'MU', 'Dynamic_threshold': 'DYNAMIC_THRESHOLD', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'Fixed_mu': 'FIXED_MU', 'Perform_mu_scan': 'PERFORM_MU_SCAN', 'Restart_read': 'RESTART_READ', 'Ls_diis': 'LS_DIIS', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS'}
        self._subsections = {'CHEBYSHEV': 'CHEBYSHEV', 'CURVY_STEPS': 'CURVY_STEPS', 'RHO_MIXING': 'RHO_MIXING', 'PEXSI': 'PEXSI', 'PAO': 'PAO'}

