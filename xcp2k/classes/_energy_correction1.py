from xcp2k.inputsection import InputSection
from _xc1 import _xc1


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
        self.XC = _xc1()
        self._name = "ENERGY_CORRECTION"
        self._keywords = {'Algorithm': 'ALGORITHM', 'Mao_max_iter': 'MAO_MAX_ITER', 'Mao_eps_grad': 'MAO_EPS_GRAD', 'Harris_basis': 'HARRIS_BASIS', 'Energy_functional': 'ENERGY_FUNCTIONAL', 'Eps_default': 'EPS_DEFAULT', 'Factorization': 'FACTORIZATION', 'Mao': 'MAO'}
        self._subsections = {'XC': 'XC'}
        self._attributes = ['Section_parameters']

