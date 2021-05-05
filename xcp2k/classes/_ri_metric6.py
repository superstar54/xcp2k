from xcp2k.inputsection import InputSection


class _ri_metric6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Potential_type = None
        self.Omega = None
        self.Cutoff_radius = None
        self.T_c_g_data = None
        self.Eps_range = None
        self._name = "RI_METRIC"
        self._keywords = {'Potential_type': 'POTENTIAL_TYPE', 'Omega': 'OMEGA', 'Cutoff_radius': 'CUTOFF_RADIUS', 'T_c_g_data': 'T_C_G_DATA', 'Eps_range': 'EPS_RANGE'}

