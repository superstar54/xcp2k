from xcp2k.inputsection import InputSection


class _auxiliary_density_matrix_method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Admm_purification_method = None
        self.Method = None
        self.Exch_scaling_model = None
        self.Exch_correction_func = None
        self.Optx_a1 = None
        self.Optx_a2 = None
        self.Optx_gamma = None
        self.Block_list = []
        self.Eps_filter = None
        self._name = "AUXILIARY_DENSITY_MATRIX_METHOD"
        self._keywords = {'Optx_gamma': 'OPTX_GAMMA', 'Eps_filter': 'EPS_FILTER', 'Admm_purification_method': 'ADMM_PURIFICATION_METHOD', 'Method': 'METHOD', 'Exch_scaling_model': 'EXCH_SCALING_MODEL', 'Optx_a1': 'OPTX_A1', 'Exch_correction_func': 'EXCH_CORRECTION_FUNC', 'Optx_a2': 'OPTX_A2'}
        self._repeated_keywords = {'Block_list': 'BLOCK_LIST'}

