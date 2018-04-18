from xcp2k.inputsection import InputSection


class _planar3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.Oscillating_fraction = None
        self.Frequency = None
        self.Phase = None
        self.A = None
        self.B = None
        self.C = None
        self.N_prtn = None
        self.Thickness = None
        self.Smoothing_width = None
        self._name = "PLANAR"
        self._keywords = {'A': 'A', 'C': 'C', 'B': 'B', 'Smoothing_width': 'SMOOTHING_WIDTH', 'N_prtn': 'N_PRTN', 'Thickness': 'THICKNESS', 'V_d': 'V_D', 'Phase': 'PHASE', 'Frequency': 'FREQUENCY', 'Oscillating_fraction': 'OSCILLATING_FRACTION'}
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
