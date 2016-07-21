from xcp2k.inputsection import InputSection
from _dielectric1 import _dielectric1
from _dirichlet_bc1 import _dirichlet_bc1


class _implicit1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Boundary_conditions = None
        self.Zero_initial_guess = None
        self.Max_iter = None
        self.Tol = None
        self.Or_parameter = None
        self.DIELECTRIC = _dielectric1()
        self.DIRICHLET_BC = _dirichlet_bc1()
        self._name = "IMPLICIT"
        self._keywords = {'Max_iter': 'MAX_ITER', 'Zero_initial_guess': 'ZERO_INITIAL_GUESS', 'Boundary_conditions': 'BOUNDARY_CONDITIONS', 'Tol': 'TOL', 'Or_parameter': 'OR_PARAMETER'}
        self._subsections = {'DIRICHLET_BC': 'DIRICHLET_BC', 'DIELECTRIC': 'DIELECTRIC'}
        self._aliases = {'Omega': 'Or_parameter'}


    @property
    def Omega(self):
        """
        See documentation for Or_parameter
        """
        return self.Or_parameter

    @Omega.setter
    def Omega(self, value):
        self.Or_parameter = value
