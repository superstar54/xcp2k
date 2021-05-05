from xcp2k.inputsection import InputSection


class _becke978(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Scale_c = None
        self.Parametrization = None
        self._name = "BECKE97"
        self._keywords = {'Scale_x': 'SCALE_X', 'Scale_c': 'SCALE_C', 'Parametrization': 'PARAMETRIZATION'}
        self._attributes = ['Section_parameters']

