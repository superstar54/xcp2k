from xcp2k.inputsection import InputSection
from xcp2k.classes._neighbor_lists3 import _neighbor_lists3
from xcp2k.classes._subcell1 import _subcell1
from xcp2k.classes._ewald_info1 import _ewald_info1


class _print29(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NEIGHBOR_LISTS = _neighbor_lists3()
        self.SUBCELL = _subcell1()
        self.EWALD_INFO = _ewald_info1()
        self._name = "PRINT"
        self._subsections = {'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'SUBCELL': 'SUBCELL', 'EWALD_INFO': 'EWALD_INFO'}

