from xcp2k.inputsection import InputSection
from xcp2k.classes._xc1 import _xc1
from xcp2k.classes._lrigpw1 import _lrigpw1
from xcp2k.classes._print26 import _print26
from xcp2k.classes._energy_correction1 import _energy_correction1


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
        self._subsections = {'XC': 'XC', 'LRIGPW': 'LRIGPW', 'PRINT': 'PRINT', 'ENERGY_CORRECTION': 'ENERGY_CORRECTION'}

