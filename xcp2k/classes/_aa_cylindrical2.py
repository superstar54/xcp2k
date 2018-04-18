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
        self._keywords = {'N_sides': 'N_SIDES', 'Smoothing_width': 'SMOOTHING_WIDTH', 'N_prtn': 'N_PRTN', 'Base_radius': 'BASE_RADIUS', 'V_d': 'V_D', 'Phase': 'PHASE', 'Frequency': 'FREQUENCY', 'Delta_alpha': 'DELTA_ALPHA', 'Parallel_axis': 'PARALLEL_AXIS', 'Oscillating_fraction': 'OSCILLATING_FRACTION', 'Base_center': 'BASE_CENTER', 'Thickness': 'THICKNESS', 'Apx_type': 'APX_TYPE', 'Xtnt': 'XTNT'}
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
