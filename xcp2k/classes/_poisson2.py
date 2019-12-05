from xcp2k.inputsection import InputSection
from xcp2k.classes._mt2 import _mt2
from xcp2k.classes._wavelet2 import _wavelet2
from xcp2k.classes._multipole2 import _multipole2
from xcp2k.classes._ewald2 import _ewald2
from xcp2k.classes._implicit2 import _implicit2


class _poisson2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Poisson_solver = None
        self.Periodic = None
        self.MT = _mt2()
        self.WAVELET = _wavelet2()
        self.MULTIPOLE = _multipole2()
        self.EWALD = _ewald2()
        self.IMPLICIT = _implicit2()
        self._name = "POISSON"
        self._keywords = {'Poisson_solver': 'POISSON_SOLVER', 'Periodic': 'PERIODIC'}
        self._subsections = {'MT': 'MT', 'WAVELET': 'WAVELET', 'MULTIPOLE': 'MULTIPOLE', 'EWALD': 'EWALD', 'IMPLICIT': 'IMPLICIT'}
        self._aliases = {'Poisson': 'Poisson_solver', 'Psolver': 'Poisson_solver'}


    @property
    def Poisson(self):
        """
        See documentation for Poisson_solver
        """
        return self.Poisson_solver

    @property
    def Psolver(self):
        """
        See documentation for Poisson_solver
        """
        return self.Poisson_solver

    @Poisson.setter
    def Poisson(self, value):
        self.Poisson_solver = value

    @Psolver.setter
    def Psolver(self, value):
        self.Poisson_solver = value
