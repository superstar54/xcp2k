from xcp2k.inputsection import InputSection


class _alchemical_change1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Parameter = None
        self.Weighting_function = None
        self.Eps_conv = None
        self.Nequil_steps = None
        self._name = "ALCHEMICAL_CHANGE"
        self._keywords = {'Parameter': 'PARAMETER', 'Weighting_function': 'WEIGHTING_FUNCTION', 'Eps_conv': 'EPS_CONV', 'Nequil_steps': 'NEQUIL_STEPS'}

