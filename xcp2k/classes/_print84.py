from xcp2k.inputsection import InputSection
from xcp2k.classes._couplings1 import _couplings1


class _print84(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.COUPLINGS = _couplings1()
        self._name = "PRINT"
        self._subsections = {'COUPLINGS': 'COUPLINGS'}

