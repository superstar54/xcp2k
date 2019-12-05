from xcp2k.inputsection import InputSection
from xcp2k.classes._dos3 import _dos3
from xcp2k.classes._transmission1 import _transmission1


class _print73(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DOS = _dos3()
        self.TRANSMISSION = _transmission1()
        self._name = "PRINT"
        self._subsections = {'DOS': 'DOS', 'TRANSMISSION': 'TRANSMISSION'}

