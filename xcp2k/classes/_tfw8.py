from xcp2k.inputsection import InputSection


class _tfw8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self._name = "TFW"
        self._attributes = ['Section_parameters']

