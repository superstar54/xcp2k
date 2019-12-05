from xcp2k.inputsection import InputSection


class _ic4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Print_ic_list = None
        self.Eps_dist = None
        self.Optimize_homo_lumo = None
        self.Gw_eigenvalues = None
        self.Gw_eigenvalues_beta = None
        self._name = "IC"
        self._keywords = {'Print_ic_list': 'PRINT_IC_LIST', 'Eps_dist': 'EPS_DIST', 'Optimize_homo_lumo': 'OPTIMIZE_HOMO_LUMO', 'Gw_eigenvalues': 'GW_EIGENVALUES', 'Gw_eigenvalues_beta': 'GW_EIGENVALUES_BETA'}
        self._aliases = {'Optimize': 'Optimize_homo_lumo'}


    @property
    def Optimize(self):
        """
        See documentation for Optimize_homo_lumo
        """
        return self.Optimize_homo_lumo

    @Optimize.setter
    def Optimize(self, value):
        self.Optimize_homo_lumo = value
