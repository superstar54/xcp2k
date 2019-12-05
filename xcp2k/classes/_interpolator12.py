from xcp2k.inputsection import InputSection
from xcp2k.classes._conv_info12 import _conv_info12


class _interpolator12(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Kind = None
        self.Safe_computation = None
        self.Aint_precond = None
        self.Precond = None
        self.Eps_x = None
        self.Eps_r = None
        self.Max_iter = None
        self.CONV_INFO = _conv_info12()
        self._name = "INTERPOLATOR"
        self._keywords = {'Kind': 'KIND', 'Safe_computation': 'SAFE_COMPUTATION', 'Aint_precond': 'AINT_PRECOND', 'Precond': 'PRECOND', 'Eps_x': 'EPS_X', 'Eps_r': 'EPS_R', 'Max_iter': 'MAX_ITER'}
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
