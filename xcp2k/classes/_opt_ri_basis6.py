from xcp2k.inputsection import InputSection


class _opt_ri_basis6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Delta_i_rel = None
        self.Delta_ri = None
        self.Eps_deriv = None
        self.Max_iter = None
        self.Num_func = None
        self.Basis_size = None
        self._name = "OPT_RI_BASIS"
        self._keywords = {'Basis_size': 'BASIS_SIZE', 'Max_iter': 'MAX_ITER', 'Num_func': 'NUM_FUNC', 'Eps_deriv': 'EPS_DERIV', 'Delta_ri': 'DELTA_RI', 'Delta_i_rel': 'DELTA_I_REL'}
        self._aliases = {'Dri': 'Delta_ri', 'Eps_num_deriv': 'Eps_deriv', 'Di_rel': 'Delta_i_rel', 'Max_num_iter': 'Max_iter'}


    @property
    def Di_rel(self):
        """
        See documentation for Delta_i_rel
        """
        return self.Delta_i_rel

    @property
    def Dri(self):
        """
        See documentation for Delta_ri
        """
        return self.Delta_ri

    @property
    def Eps_num_deriv(self):
        """
        See documentation for Eps_deriv
        """
        return self.Eps_deriv

    @property
    def Max_num_iter(self):
        """
        See documentation for Max_iter
        """
        return self.Max_iter

    @Di_rel.setter
    def Di_rel(self, value):
        self.Delta_i_rel = value

    @Dri.setter
    def Dri(self, value):
        self.Delta_ri = value

    @Eps_num_deriv.setter
    def Eps_num_deriv(self, value):
        self.Eps_deriv = value

    @Max_num_iter.setter
    def Max_num_iter(self, value):
        self.Max_iter = value
