from xcp2k.inputsection import InputSection


class _xgga7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Functional = None
        self._name = "XGGA"
        self._keywords = {'Functional': 'FUNCTIONAL'}
        self._attributes = ['Section_parameters']

