from xcp2k.inputsection import InputSection
from _print65 import _print65


class _block1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Nelectron = None
        self.PRINT = _print65()
        self._name = "BLOCK"
        self._keywords = {'Nelectron': 'NELECTRON', 'Atoms': 'ATOMS'}
        self._subsections = {'PRINT': 'PRINT'}

