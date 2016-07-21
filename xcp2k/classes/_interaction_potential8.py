from xcp2k.inputsection import InputSection


class _interaction_potential8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Potential_type = None
        self.Omega = None
        self.Scale_coulomb = None
        self.Scale_longrange = None
        self.Scale_gaussian = None
        self.Cutoff_radius = None
        self.T_c_g_data = None
        self._name = "INTERACTION_POTENTIAL"
        self._keywords = {'Scale_coulomb': 'SCALE_COULOMB', 'T_c_g_data': 'T_C_G_DATA', 'Scale_gaussian': 'SCALE_GAUSSIAN', 'Scale_longrange': 'SCALE_LONGRANGE', 'Potential_type': 'POTENTIAL_TYPE', 'Cutoff_radius': 'CUTOFF_RADIUS', 'Omega': 'OMEGA'}

