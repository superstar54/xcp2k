from xcp2k.inputsection import InputSection
from xcp2k.classes._localize4 import _localize4
from xcp2k.classes._ri_info4 import _ri_info4


class _ri5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Eps_filter = None
        self.Eps_filter_2c = None
        self.Eps_storage_scaling = None
        self.Eps_filter_mo = None
        self.Omega = None
        self.Cutoff_radius = None
        self.Ri_metric = None
        self.Num2c_matrix_functions = None
        self.Eps_eigval = None
        self.Check_2c_matrix = None
        self.Calc_cond_num = None
        self.Sqrt_order = None
        self.Eps_lanczos = None
        self.Eps_pgf_orb = None
        self.Max_iter_lanczos = None
        self.Ri_flavor = None
        self.Min_block_size = None
        self.Min_block_size_mo = None
        self.Memory_cut = None
        self.LOCALIZE = _localize4()
        self.RI_INFO = _ri_info4()
        self._name = "RI"
        self._keywords = {'Eps_filter': 'EPS_FILTER', 'Eps_filter_2c': 'EPS_FILTER_2C', 'Eps_storage_scaling': 'EPS_STORAGE_SCALING', 'Eps_filter_mo': 'EPS_FILTER_MO', 'Omega': 'OMEGA', 'Cutoff_radius': 'CUTOFF_RADIUS', 'Ri_metric': 'RI_METRIC', 'Num2c_matrix_functions': '2C_MATRIX_FUNCTIONS', 'Eps_eigval': 'EPS_EIGVAL', 'Check_2c_matrix': 'CHECK_2C_MATRIX', 'Calc_cond_num': 'CALC_COND_NUM', 'Sqrt_order': 'SQRT_ORDER', 'Eps_lanczos': 'EPS_LANCZOS', 'Eps_pgf_orb': 'EPS_PGF_ORB', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS', 'Ri_flavor': 'RI_FLAVOR', 'Min_block_size': 'MIN_BLOCK_SIZE', 'Min_block_size_mo': 'MIN_BLOCK_SIZE_MO', 'Memory_cut': 'MEMORY_CUT'}
        self._subsections = {'LOCALIZE': 'LOCALIZE', 'RI_INFO': 'RI_INFO'}
        self._aliases = {'Calc_condition_number': 'Calc_cond_num'}
        self._attributes = ['Section_parameters']


    @property
    def Calc_condition_number(self):
        """
        See documentation for Calc_cond_num
        """
        return self.Calc_cond_num

    @Calc_condition_number.setter
    def Calc_condition_number(self, value):
        self.Calc_cond_num = value
