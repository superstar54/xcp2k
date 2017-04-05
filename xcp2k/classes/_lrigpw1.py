from xcp2k.inputsection import InputSection


class _lrigpw1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Lri_overlap_matrix = None
        self.Max_condition_num = None
        self.Debug_lri_integrals = None
        self.Shg_lri_integrals = None
        self._name = "LRIGPW"
        self._keywords = {'Shg_lri_integrals': 'SHG_LRI_INTEGRALS', 'Debug_lri_integrals': 'DEBUG_LRI_INTEGRALS', 'Lri_overlap_matrix': 'LRI_OVERLAP_MATRIX', 'Max_condition_num': 'MAX_CONDITION_NUM'}

