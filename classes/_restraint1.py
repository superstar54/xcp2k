from xcp2k.inputsection import InputSection


class _restraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.K = None
        self._name = "RESTRAINT"
        self._keywords = {'K': 'K'}

