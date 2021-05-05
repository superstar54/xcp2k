from xcp2k.inputsection import InputSection


class _becke88_lr8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Omega = None
        self._name = "BECKE88_LR"
        self._keywords = {'Scale_x': 'SCALE_X', 'Omega': 'OMEGA'}
        self._attributes = ['Section_parameters']

