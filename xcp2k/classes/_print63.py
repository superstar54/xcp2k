from xcp2k.inputsection import InputSection
from xcp2k.classes._energies2 import _energies2
from xcp2k.classes._energies_var1 import _energies_var1
from xcp2k.classes._forces4 import _forces4
from xcp2k.classes._coord_avg1 import _coord_avg1
from xcp2k.classes._coord_var1 import _coord_var1
from xcp2k.classes._count1 import _count1


class _print63(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ENERGIES = _energies2()
        self.ENERGIES_VAR = _energies_var1()
        self.FORCES = _forces4()
        self.COORD_AVG = _coord_avg1()
        self.COORD_VAR = _coord_var1()
        self.COUNT = _count1()
        self._name = "PRINT"
        self._subsections = {'ENERGIES': 'ENERGIES', 'ENERGIES_VAR': 'ENERGIES_VAR', 'FORCES': 'FORCES', 'COORD_AVG': 'COORD_AVG', 'COORD_VAR': 'COORD_VAR', 'COUNT': 'COUNT'}

