from xcp2k.inputsection import InputSection


class _model1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Weights = None
        self._name = "MODEL"
        self._keywords = {'Weights': 'WEIGHTS'}

