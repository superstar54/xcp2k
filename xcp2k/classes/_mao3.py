from xcp2k.inputsection import InputSection


class _mao3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mao_occ = None
        self.Mao_virt = None
        self.Max_iter_occ = None
        self.Max_iter_virt = None
        self.Eps_grad_occ = None
        self.Eps_grad_virt = None
        self.Optimize_scaled_occ_dm = None
        self.Optimize_scaled_virt_dm = None
        self._name = "MAO"
        self._keywords = {'Mao_occ': 'MAO_OCC', 'Mao_virt': 'MAO_VIRT', 'Max_iter_occ': 'MAX_ITER_OCC', 'Max_iter_virt': 'MAX_ITER_VIRT', 'Eps_grad_occ': 'EPS_GRAD_OCC', 'Eps_grad_virt': 'EPS_GRAD_VIRT', 'Optimize_scaled_occ_dm': 'OPTIMIZE_SCALED_OCC_DM', 'Optimize_scaled_virt_dm': 'OPTIMIZE_SCALED_VIRT_DM'}
        self._aliases = {'Opt_sc_dm_occ': 'Optimize_scaled_occ_dm', 'Opt_sc_dm_virt': 'Optimize_scaled_virt_dm'}


    @property
    def Opt_sc_dm_occ(self):
        """
        See documentation for Optimize_scaled_occ_dm
        """
        return self.Optimize_scaled_occ_dm

    @property
    def Opt_sc_dm_virt(self):
        """
        See documentation for Optimize_scaled_virt_dm
        """
        return self.Optimize_scaled_virt_dm

    @Opt_sc_dm_occ.setter
    def Opt_sc_dm_occ(self, value):
        self.Optimize_scaled_occ_dm = value

    @Opt_sc_dm_virt.setter
    def Opt_sc_dm_virt(self, value):
        self.Optimize_scaled_virt_dm = value
