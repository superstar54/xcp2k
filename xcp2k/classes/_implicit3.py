from xcp2k.inputsection import InputSection
from _dielectric3 import _dielectric3
from _dirichlet_bc3 import _dirichlet_bc3


class _implicit3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Boundary_conditions = None
        self.Zero_initial_guess = None
        self.Max_iter = None
        self.Tol = None
        self.Or_parameter = None
        self.Neumann_directions = None
        self.DIELECTRIC = _dielectric3()
        self.DIRICHLET_BC = _dirichlet_bc3()
        self._name = "IMPLICIT"
        self._keywords = {'Zero_initial_guess': 'ZERO_INITIAL_GUESS', 'Max_iter': 'MAX_ITER', 'Boundary_conditions': 'BOUNDARY_CONDITIONS', 'Neumann_directions': 'NEUMANN_DIRECTIONS', 'Tol': 'TOL', 'Or_parameter': 'OR_PARAMETER'}
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
