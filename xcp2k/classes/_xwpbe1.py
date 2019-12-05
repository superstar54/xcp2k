from xcp2k.inputsection import InputSection


class _xwpbe1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Scale_x0 = None
        self.Omega = None
        self._name = "XWPBE"
        self._keywords = {'Scale_x': 'SCALE_X', 'Scale_x0': 'SCALE_X0', 'Omega': 'OMEGA'}
        self._attributes = ['Section_parameters']

