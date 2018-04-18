from xcp2k.inputsection import InputSection


class _optx1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.A1 = None
        self.A2 = None
        self.Gamma = None
        self._name = "OPTX"
        self._keywords = {'Scale_x': 'SCALE_X', 'A1': 'A1', 'A2': 'A2', 'Gamma': 'GAMMA'}
        self._attributes = ['Section_parameters']

