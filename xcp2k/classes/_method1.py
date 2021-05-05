from xcp2k.inputsection import InputSection
from xcp2k.classes._xc7 import _xc7
from xcp2k.classes._zmp1 import _zmp1
from xcp2k.classes._external_vxc2 import _external_vxc2


class _method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method_type = None
        self.Relativistic = None
        self.XC = _xc7()
        self.ZMP = _zmp1()
        self.EXTERNAL_VXC = _external_vxc2()
        self._name = "METHOD"
        self._keywords = {'Method_type': 'METHOD_TYPE', 'Relativistic': 'RELATIVISTIC'}
        self._subsections = {'XC': 'XC', 'ZMP': 'ZMP', 'EXTERNAL_VXC': 'EXTERNAL_VXC'}

