from xcp2k.inputsection import InputSection
from xcp2k.classes._neighbor_lists9 import _neighbor_lists9
from xcp2k.classes._subcell5 import _subcell5


class _print50(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NEIGHBOR_LISTS = _neighbor_lists9()
        self.SUBCELL = _subcell5()
        self._name = "PRINT"
        self._subsections = {'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'SUBCELL': 'SUBCELL'}

