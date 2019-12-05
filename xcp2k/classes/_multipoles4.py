from xcp2k.inputsection import InputSection
from xcp2k.classes._dipoles1 import _dipoles1
from xcp2k.classes._quadrupoles1 import _quadrupoles1


class _multipoles4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DIPOLES = _dipoles1()
        self.QUADRUPOLES = _quadrupoles1()
        self._name = "MULTIPOLES"
        self._subsections = {'DIPOLES': 'DIPOLES', 'QUADRUPOLES': 'QUADRUPOLES'}

