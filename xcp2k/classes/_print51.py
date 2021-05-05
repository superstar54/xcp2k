from xcp2k.inputsection import InputSection
from xcp2k.classes._spectrum1 import _spectrum1
from xcp2k.classes._pdos2 import _pdos2
from xcp2k.classes._cubes19 import _cubes19
from xcp2k.classes._restart10 import _restart10


class _print51(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.SPECTRUM = _spectrum1()
        self.PDOS = _pdos2()
        self.CUBES = _cubes19()
        self.RESTART = _restart10()
        self._name = "PRINT"
        self._subsections = {'SPECTRUM': 'SPECTRUM', 'PDOS': 'PDOS', 'CUBES': 'CUBES', 'RESTART': 'RESTART'}

