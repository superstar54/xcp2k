from xcp2k.inputsection import InputSection
from xcp2k.classes._linres1 import _linres1
from xcp2k.classes._et_coupling1 import _et_coupling1
from xcp2k.classes._resp1 import _resp1
from xcp2k.classes._atomic1 import _atomic1
from xcp2k.classes._fit_charge1 import _fit_charge1
from xcp2k.classes._tddfpt2 import _tddfpt2


class _properties1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.LINRES = _linres1()
        self.ET_COUPLING = _et_coupling1()
        self.RESP = _resp1()
        self.ATOMIC = _atomic1()
        self.FIT_CHARGE = _fit_charge1()
        self.TDDFPT = _tddfpt2()
        self._name = "PROPERTIES"
        self._subsections = {'LINRES': 'LINRES', 'ET_COUPLING': 'ET_COUPLING', 'RESP': 'RESP', 'ATOMIC': 'ATOMIC', 'FIT_CHARGE': 'FIT_CHARGE', 'TDDFPT': 'TDDFPT'}

