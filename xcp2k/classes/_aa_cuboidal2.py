from xcp2k.inputsection import InputSection


class _aa_cuboidal2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.X_xtnt = None
        self.Y_xtnt = None
        self.Z_xtnt = None
        self.N_prtn = None
        self.Smoothing_width = None
        self._name = "AA_CUBOIDAL"
        self._keywords = {'Y_xtnt': 'Y_XTNT', 'Z_xtnt': 'Z_XTNT', 'X_xtnt': 'X_XTNT', 'Smoothing_width': 'SMOOTHING_WIDTH', 'V_d': 'V_D', 'N_prtn': 'N_PRTN'}
        self._aliases = {'Sigma': 'Smoothing_width'}


    @property
    def Sigma(self):
        """
        See documentation for Smoothing_width
        """
        return self.Smoothing_width

    @Sigma.setter
    def Sigma(self, value):
        self.Smoothing_width = value
