from xcp2k.inputsection import InputSection
from xcp2k.classes._print99 import _print99


class _load_balance13(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nbins = None
        self.Block_size = None
        self.Randomize = None
        self.PRINT = _print99()
        self._name = "LOAD_BALANCE"
        self._keywords = {'Nbins': 'NBINS', 'Block_size': 'BLOCK_SIZE', 'Randomize': 'RANDOMIZE'}
        self._subsections = {'PRINT': 'PRINT'}

