from xcp2k.inputsection import InputSection
from xcp2k.classes._energies1 import _energies1
from xcp2k.classes._forces3 import _forces3
from xcp2k.classes._forces_sigma1 import _forces_sigma1
from xcp2k.classes._extrapolation1 import _extrapolation1
from xcp2k.classes._sum_force1 import _sum_force1


class _print59(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ENERGIES = _energies1()
        self.FORCES = _forces3()
        self.FORCES_SIGMA = _forces_sigma1()
        self.EXTRAPOLATION = _extrapolation1()
        self.SUM_FORCE = _sum_force1()
        self._name = "PRINT"
        self._subsections = {'ENERGIES': 'ENERGIES', 'FORCES': 'FORCES', 'FORCES_SIGMA': 'FORCES_SIGMA', 'EXTRAPOLATION': 'EXTRAPOLATION', 'SUM_FORCE': 'SUM_FORCE'}

