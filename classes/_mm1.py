from xcp2k.inputsection import InputSection
from _forcefield1 import _forcefield1
from _neighbor_lists5 import _neighbor_lists5
from _poisson2 import _poisson2
from _print35 import _print35


class _mm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.FORCEFIELD = _forcefield1()
        self.NEIGHBOR_LISTS = _neighbor_lists5()
        self.POISSON = _poisson2()
        self.PRINT = _print35()
        self._name = "MM"
        self._subsections = {'PRINT': 'PRINT', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'FORCEFIELD': 'FORCEFIELD', 'POISSON': 'POISSON'}

