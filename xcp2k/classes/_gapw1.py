from xcp2k.inputsection import InputSection
from xcp2k.classes._projectors1 import _projectors1
from xcp2k.classes._rho0_information1 import _rho0_information1


class _gapw1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROJECTORS = _projectors1()
        self.RHO0_INFORMATION = _rho0_information1()
        self._name = "GAPW"
        self._subsections = {'PROJECTORS': 'PROJECTORS', 'RHO0_INFORMATION': 'RHO0_INFORMATION'}

