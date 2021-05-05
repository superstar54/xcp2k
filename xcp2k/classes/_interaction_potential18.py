from xcp2k.inputsection import InputSection


class _interaction_potential18(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Potential_type = None
        self.Truncation_radius = None
        self.Tshpsc_data = None
        self.Omega = None
        self._name = "INTERACTION_POTENTIAL"
        self._keywords = {'Potential_type': 'POTENTIAL_TYPE', 'Truncation_radius': 'TRUNCATION_RADIUS', 'Tshpsc_data': 'TSHPSC_DATA', 'Omega': 'OMEGA'}

