from xcp2k.inputsection import InputSection
from xcp2k.classes._mixed5 import _mixed5


class _u4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MIXED = _mixed5()
        self._name = "U"
        self._subsections = {'MIXED': 'MIXED'}

