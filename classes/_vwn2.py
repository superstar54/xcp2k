from xcp2k.inputsection import InputSection


class _vwn2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_c = None
        self.Functional_type = None
        self._name = "VWN"
        self._keywords = {'Scale_c': 'SCALE_C', 'Functional_type': 'FUNCTIONAL_TYPE'}
        self._attributes = ['Section_parameters']

