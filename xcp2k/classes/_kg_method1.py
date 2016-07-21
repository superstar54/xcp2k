from xcp2k.inputsection import InputSection
from _print21 import _print21


class _kg_method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coloring_method = None
        self.Tnadd_method = None
        self.PRINT = _print21()
        self._name = "KG_METHOD"
        self._keywords = {'Coloring_method': 'COLORING_METHOD', 'Tnadd_method': 'TNADD_METHOD'}
        self._subsections = {'PRINT': 'PRINT'}

