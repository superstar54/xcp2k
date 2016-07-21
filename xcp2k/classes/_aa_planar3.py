from xcp2k.inputsection import InputSection


class _aa_planar3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.Parallel_plane = None
        self.Intercept = None
        self.X_xtnt = None
        self.Y_xtnt = None
        self.Z_xtnt = None
        self.N_prtn = None
        self.Thickness = None
        self.Smoothing_width = None
        self._name = "AA_PLANAR"
        self._keywords = {'Y_xtnt': 'Y_XTNT', 'Z_xtnt': 'Z_XTNT', 'X_xtnt': 'X_XTNT', 'Smoothing_width': 'SMOOTHING_WIDTH', 'N_prtn': 'N_PRTN', 'Thickness': 'THICKNESS', 'V_d': 'V_D', 'Intercept': 'INTERCEPT', 'Parallel_plane': 'PARALLEL_PLANE'}
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
