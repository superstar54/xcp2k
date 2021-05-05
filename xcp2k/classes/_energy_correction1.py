from xcp2k.inputsection import InputSection
from xcp2k.classes._xc2 import _xc2
from xcp2k.classes._ls_solver1 import _ls_solver1


class _energy_correction1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Energy_functional = None
        self.Harris_basis = None
        self.Mao = None
        self.Mao_max_iter = None
        self.Mao_eps_grad = None
        self.Algorithm = None
        self.Factorization = None
        self.Eps_default = None
        self.XC = _xc2()
        self.LS_SOLVER = _ls_solver1()
        self._name = "ENERGY_CORRECTION"
        self._keywords = {'Energy_functional': 'ENERGY_FUNCTIONAL', 'Harris_basis': 'HARRIS_BASIS', 'Mao': 'MAO', 'Mao_max_iter': 'MAO_MAX_ITER', 'Mao_eps_grad': 'MAO_EPS_GRAD', 'Algorithm': 'ALGORITHM', 'Factorization': 'FACTORIZATION', 'Eps_default': 'EPS_DEFAULT'}
        self._subsections = {'XC': 'XC', 'LS_SOLVER': 'LS_SOLVER'}
        self._attributes = ['Section_parameters']

