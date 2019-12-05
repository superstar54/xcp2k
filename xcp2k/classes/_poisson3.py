from xcp2k.inputsection import InputSection
from xcp2k.classes._mt3 import _mt3
from xcp2k.classes._wavelet3 import _wavelet3
from xcp2k.classes._multipole4 import _multipole4
from xcp2k.classes._ewald3 import _ewald3
from xcp2k.classes._implicit3 import _implicit3


class _poisson3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Poisson_solver = None
        self.Periodic = None
        self.MT = _mt3()
        self.WAVELET = _wavelet3()
        self.MULTIPOLE = _multipole4()
        self.EWALD = _ewald3()
        self.IMPLICIT = _implicit3()
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
