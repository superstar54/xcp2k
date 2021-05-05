from xcp2k.inputsection import InputSection
from xcp2k.classes._print83 import _print83


class _block1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Nelectron = None
        self.PRINT = _print83()
        self._name = "BLOCK"
        self._keywords = {'Atoms': 'ATOMS', 'Nelectron': 'NELECTRON'}
        self._subsections = {'PRINT': 'PRINT'}

