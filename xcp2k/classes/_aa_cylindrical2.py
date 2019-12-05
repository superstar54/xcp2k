from xcp2k.inputsection import InputSection


class _aa_cylindrical2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.Oscillating_fraction = None
        self.Frequency = None
        self.Phase = None
        self.Parallel_axis = None
        self.Xtnt = None
        self.Base_center = None
        self.Base_radius = None
        self.N_sides = None
        self.Apx_type = None
        self.N_prtn = None
        self.Thickness = None
        self.Smoothing_width = None
        self.Delta_alpha = None
        self._name = "AA_CYLINDRICAL"
        self._keywords = {'V_d': 'V_D', 'Oscillating_fraction': 'OSCILLATING_FRACTION', 'Frequency': 'FREQUENCY', 'Phase': 'PHASE', 'Parallel_axis': 'PARALLEL_AXIS', 'Xtnt': 'XTNT', 'Base_center': 'BASE_CENTER', 'Base_radius': 'BASE_RADIUS', 'N_sides': 'N_SIDES', 'Apx_type': 'APX_TYPE', 'N_prtn': 'N_PRTN', 'Thickness': 'THICKNESS', 'Smoothing_width': 'SMOOTHING_WIDTH', 'Delta_alpha': 'DELTA_ALPHA'}
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
