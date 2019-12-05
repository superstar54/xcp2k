from xcp2k.inputsection import InputSection


class _lrigpw2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Lri_overlap_matrix = None
        self.Max_condition_num = None
        self.Eps_o3_int = None
        self.Debug_lri_integrals = None
        self.Exact_1c_terms = None
        self.Ppl_ri = None
        self.Ri_statistic = None
        self.Distant_pair_approximation = None
        self.Distant_pair_method = None
        self.Distant_pair_radii = None
        self.Shg_lri_integrals = None
        self.Ri_sinv = None
        self._name = "LRIGPW"
        self._keywords = {'Lri_overlap_matrix': 'LRI_OVERLAP_MATRIX', 'Max_condition_num': 'MAX_CONDITION_NUM', 'Eps_o3_int': 'EPS_O3_INT', 'Debug_lri_integrals': 'DEBUG_LRI_INTEGRALS', 'Exact_1c_terms': 'EXACT_1C_TERMS', 'Ppl_ri': 'PPL_RI', 'Ri_statistic': 'RI_STATISTIC', 'Distant_pair_approximation': 'DISTANT_PAIR_APPROXIMATION', 'Distant_pair_method': 'DISTANT_PAIR_METHOD', 'Distant_pair_radii': 'DISTANT_PAIR_RADII', 'Shg_lri_integrals': 'SHG_LRI_INTEGRALS', 'Ri_sinv': 'RI_SINV'}

