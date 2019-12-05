from xcp2k.inputsection import InputSection
from xcp2k.classes._coord7 import _coord7
from xcp2k.classes._velocity8 import _velocity8


class _nose6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nnos = None
        self.COORD = _coord7()
        self.VELOCITY = _velocity8()
        self._name = "NOSE"
        self._keywords = {'Nnos': 'NNOS'}
        self._subsections = {'COORD': 'COORD', 'VELOCITY': 'VELOCITY'}

