from xcp2k.inputsection import InputSection


class _becke88_lr_adiabatic3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Omega = None
        self.Lambda = None
        self._name = "BECKE88_LR_ADIABATIC"
        self._keywords = {'Scale_x': 'SCALE_X', 'Omega': 'OMEGA', 'Lambda': 'LAMBDA'}
        self._attributes = ['Section_parameters']

