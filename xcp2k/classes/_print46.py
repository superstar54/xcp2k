from xcp2k.inputsection import InputSection
from xcp2k.classes._current1 import _current1


class _print46(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.CURRENT = _current1()
        self._name = "PRINT"
        self._subsections = {'CURRENT': 'CURRENT'}

