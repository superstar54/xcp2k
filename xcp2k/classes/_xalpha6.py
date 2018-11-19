from xcp2k.inputsection import InputSection


class _xalpha6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Xa = None
        self.Scale_x = None
        self._name = "XALPHA"
        self._keywords = {'Scale_x': 'SCALE_X', 'Xa': 'XA'}
        self._attributes = ['Section_parameters']

