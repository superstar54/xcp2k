from xcp2k.inputsection import InputSection
from xcp2k.classes._neighbor_lists1 import _neighbor_lists1


class _print26(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NEIGHBOR_LISTS = _neighbor_lists1()
        self._name = "PRINT"
        self._subsections = {'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS'}

