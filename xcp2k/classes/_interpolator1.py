from xcp2k.inputsection import InputSection
from _conv_info1 import _conv_info1


class _interpolator1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Kind = None
        self.Safe_computation = None
        self.Aint_precond = None
        self.Precond = None
        self.Eps_x = None
        self.Eps_r = None
        self.Max_iter = None
        self.CONV_INFO = _conv_info1()
        self._name = "INTERPOLATOR"
        self._keywords = {'Kind': 'KIND', 'Eps_r': 'EPS_R', 'Max_iter': 'MAX_ITER', 'Eps_x': 'EPS_X', 'Aint_precond': 'AINT_PRECOND', 'Safe_computation': 'SAFE_COMPUTATION', 'Precond': 'PRECOND'}
        self._subsections = {'CONV_INFO': 'CONV_INFO'}
        self._aliases = {'Maxiter': 'Max_iter'}


    @property
    def Maxiter(self):
        """
        See documentation for Max_iter
        """
        return self.Max_iter

    @Maxiter.setter
    def Maxiter(self, value):
        self.Max_iter = value
