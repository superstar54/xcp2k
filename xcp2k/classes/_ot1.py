from xcp2k.inputsection import InputSection


class _ot1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Algorithm = None
        self.Irac_degree = None
        self.Max_irac = None
        self.Ortho_irac = None
        self.Eps_irac_filter_matrix = None
        self.Eps_irac = None
        self.Eps_irac_quick_exit = None
        self.Eps_irac_switch = None
        self.On_the_fly_loc = None
        self.Minimizer = None
        self.Safe_diis = None
        self.N_history_vec = None
        self.Broyden_beta = None
        self.Broyden_gamma = None
        self.Broyden_sigma = None
        self.Broyden_eta = None
        self.Broyden_omega = None
        self.Broyden_sigma_decrease = None
        self.Broyden_sigma_min = None
        self.Broyden_forget_history = None
        self.Broyden_adaptive_sigma = None
        self.Broyden_enable_flip = None
        self.Linesearch = None
        self.Stepsize = None
        self.Gold_target = None
        self.Preconditioner = None
        self.Cholesky = None
        self.Precond_solver = None
        self.Energy_gap = None
        self.Eps_taylor = None
        self.Max_taylor = None
        self.Rotation = None
        self.Energies = None
        self.Occupation_preconditioner = None
        self.Nondiag_energy = None
        self.Nondiag_energy_strength = None
        self._name = "OT"
        self._keywords = {'Algorithm': 'ALGORITHM', 'Irac_degree': 'IRAC_DEGREE', 'Max_irac': 'MAX_IRAC', 'Ortho_irac': 'ORTHO_IRAC', 'Eps_irac_filter_matrix': 'EPS_IRAC_FILTER_MATRIX', 'Eps_irac': 'EPS_IRAC', 'Eps_irac_quick_exit': 'EPS_IRAC_QUICK_EXIT', 'Eps_irac_switch': 'EPS_IRAC_SWITCH', 'On_the_fly_loc': 'ON_THE_FLY_LOC', 'Minimizer': 'MINIMIZER', 'Safe_diis': 'SAFE_DIIS', 'N_history_vec': 'N_HISTORY_VEC', 'Broyden_beta': 'BROYDEN_BETA', 'Broyden_gamma': 'BROYDEN_GAMMA', 'Broyden_sigma': 'BROYDEN_SIGMA', 'Broyden_eta': 'BROYDEN_ETA', 'Broyden_omega': 'BROYDEN_OMEGA', 'Broyden_sigma_decrease': 'BROYDEN_SIGMA_DECREASE', 'Broyden_sigma_min': 'BROYDEN_SIGMA_MIN', 'Broyden_forget_history': 'BROYDEN_FORGET_HISTORY', 'Broyden_adaptive_sigma': 'BROYDEN_ADAPTIVE_SIGMA', 'Broyden_enable_flip': 'BROYDEN_ENABLE_FLIP', 'Linesearch': 'LINESEARCH', 'Stepsize': 'STEPSIZE', 'Gold_target': 'GOLD_TARGET', 'Preconditioner': 'PRECONDITIONER', 'Cholesky': 'CHOLESKY', 'Precond_solver': 'PRECOND_SOLVER', 'Energy_gap': 'ENERGY_GAP', 'Eps_taylor': 'EPS_TAYLOR', 'Max_taylor': 'MAX_TAYLOR', 'Rotation': 'ROTATION', 'Energies': 'ENERGIES', 'Occupation_preconditioner': 'OCCUPATION_PRECONDITIONER', 'Nondiag_energy': 'NONDIAG_ENERGY', 'Nondiag_energy_strength': 'NONDIAG_ENERGY_STRENGTH'}
        self._aliases = {'Safer_diis': 'Safe_diis', 'Ndiis': 'N_history_vec', 'N_diis': 'N_history_vec', 'N_broyden': 'N_history_vec', 'Line_search': 'Linesearch', 'Epstaylor': 'Eps_taylor'}
        self._attributes = ['Section_parameters']


    @property
    def Safer_diis(self):
        """
        See documentation for Safe_diis
        """
        return self.Safe_diis

    @property
    def Ndiis(self):
        """
        See documentation for N_history_vec
        """
        return self.N_history_vec

    @property
    def N_diis(self):
        """
        See documentation for N_history_vec
        """
        return self.N_history_vec

    @property
    def N_broyden(self):
        """
        See documentation for N_history_vec
        """
        return self.N_history_vec

    @property
    def Line_search(self):
        """
        See documentation for Linesearch
        """
        return self.Linesearch

    @property
    def Epstaylor(self):
        """
        See documentation for Eps_taylor
        """
        return self.Eps_taylor

    @Safer_diis.setter
    def Safer_diis(self, value):
        self.Safe_diis = value

    @Ndiis.setter
    def Ndiis(self, value):
        self.N_history_vec = value

    @N_diis.setter
    def N_diis(self, value):
        self.N_history_vec = value

    @N_broyden.setter
    def N_broyden(self, value):
        self.N_history_vec = value

    @Line_search.setter
    def Line_search(self, value):
        self.Linesearch = value

    @Epstaylor.setter
    def Epstaylor(self, value):
        self.Eps_taylor = value
