from xcp2k.inputsection import InputSection


class _xaa_cylindrical2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.X_xtnt = None
        self.Base_center = None
        self.Base_radius = None
        self.N_sides = None
        self.Apx_type = None
        self.N_prtn = None
        self.Thickness = None
        self.Smoothing_width = None
        self.Delta_alpha = None
        self._name = "XAA_CYLINDRICAL"
        self._keywords = {'N_sides': 'N_SIDES', 'X_xtnt': 'X_XTNT', 'Smoothing_width': 'SMOOTHING_WIDTH', 'Base_radius': 'BASE_RADIUS', 'V_d': 'V_D', 'N_prtn': 'N_PRTN', 'Delta_alpha': 'DELTA_ALPHA', 'Base_center': 'BASE_CENTER', 'Thickness': 'THICKNESS', 'Apx_type': 'APX_TYPE'}
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
