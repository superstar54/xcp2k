from xcp2k.inputsection import InputSection
from _xc1 import _xc1
from _lrigpw1 import _lrigpw1
from _print26 import _print26
from _energy_correction1 import _energy_correction1


class _kg_method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coloring_method = None
        self.Tnadd_method = None
        self.XC = _xc1()
        self.LRIGPW = _lrigpw1()
        self.PRINT = _print26()
        self.ENERGY_CORRECTION = _energy_correction1()
        self._name = "KG_METHOD"
        self._keywords = {'Coloring_method': 'COLORING_METHOD', 'Tnadd_method': 'TNADD_METHOD'}
        self._subsections = {'PRINT': 'PRINT', 'XC': 'XC', 'ENERGY_CORRECTION': 'ENERGY_CORRECTION', 'LRIGPW': 'LRIGPW'}

