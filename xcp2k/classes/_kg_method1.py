from xcp2k.inputsection import InputSection
from xcp2k.classes._xc1 import _xc1
from xcp2k.classes._lrigpw1 import _lrigpw1
from xcp2k.classes._print29 import _print29


class _kg_method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coloring_method = None
        self.Tnadd_method = None
        self.Integration_grid = None
        self.XC = _xc1()
        self.LRIGPW = _lrigpw1()
        self.PRINT = _print29()
        self._name = "KG_METHOD"
        self._keywords = {'Coloring_method': 'COLORING_METHOD', 'Tnadd_method': 'TNADD_METHOD', 'Integration_grid': 'INTEGRATION_GRID'}
        self._subsections = {'XC': 'XC', 'LRIGPW': 'LRIGPW', 'PRINT': 'PRINT'}

