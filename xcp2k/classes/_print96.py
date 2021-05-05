from xcp2k.inputsection import InputSection
from xcp2k.classes._dos3 import _dos3


class _print96(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DOS = _dos3()
        self._name = "PRINT"
        self._subsections = {'DOS': 'DOS'}

