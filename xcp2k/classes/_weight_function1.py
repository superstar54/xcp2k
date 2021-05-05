from xcp2k.inputsection import InputSection


class _weight_function1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Stride = None
        self._name = "WEIGHT_FUNCTION"
        self._keywords = {'Stride': 'STRIDE'}

