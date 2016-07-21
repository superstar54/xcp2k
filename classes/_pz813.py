from xcp2k.inputsection import InputSection


class _pz813(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Parametrization = None
        self.Scale_c = None
        self._name = "PZ81"
        self._keywords = {'Scale_c': 'SCALE_C', 'Parametrization': 'PARAMETRIZATION'}
        self._attributes = ['Section_parameters']

