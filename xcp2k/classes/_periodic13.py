from xcp2k.inputsection import InputSection
from xcp2k.classes._multipole3 import _multipole3
from xcp2k.classes._interpolator6 import _interpolator6
from xcp2k.classes._poisson3 import _poisson3
from xcp2k.classes._check_spline5 import _check_spline5


class _periodic13(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Gmax = None
        self.Replica = None
        self.Ngrids = None
        self.MULTIPOLE = _multipole3()
        self.INTERPOLATOR = _interpolator6()
        self.POISSON = _poisson3()
        self.CHECK_SPLINE = _check_spline5()
        self._name = "PERIODIC"
        self._keywords = {'Gmax': 'GMAX', 'Replica': 'REPLICA', 'Ngrids': 'NGRIDS'}
        self._subsections = {'MULTIPOLE': 'MULTIPOLE', 'INTERPOLATOR': 'INTERPOLATOR', 'POISSON': 'POISSON', 'CHECK_SPLINE': 'CHECK_SPLINE'}

