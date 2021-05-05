from xcp2k.inputsection import InputSection


class _saop7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Alpha = None
        self.Beta = None
        self.K_rho = None
        self._name = "SAOP"
        self._keywords = {'Alpha': 'ALPHA', 'Beta': 'BETA', 'K_rho': 'K_RHO'}

