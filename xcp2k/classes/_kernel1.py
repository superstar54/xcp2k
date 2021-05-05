from xcp2k.inputsection import InputSection
from xcp2k.classes._xc_functional5 import _xc_functional5
from xcp2k.classes._exact_exchange1 import _exact_exchange1


class _kernel1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ri_region = None
        self.XC_FUNCTIONAL = _xc_functional5()
        self.EXACT_EXCHANGE = _exact_exchange1()
        self._name = "KERNEL"
        self._keywords = {'Ri_region': 'RI_REGION'}
        self._subsections = {'XC_FUNCTIONAL': 'XC_FUNCTIONAL', 'EXACT_EXCHANGE': 'EXACT_EXCHANGE'}
        self._aliases = {'Ri_radius': 'Ri_region'}


    @property
    def Ri_radius(self):
        """
        See documentation for Ri_region
        """
        return self.Ri_region

    @Ri_radius.setter
    def Ri_radius(self, value):
        self.Ri_region = value
