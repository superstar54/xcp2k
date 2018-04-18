from xcp2k.inputsection import InputSection
from _basis5 import _basis5


class _pp_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Basis_type = None
        self.Num_gto = None
        self.Num_slater = None
        self.Start_index = None
        self.S_exponents = None
        self.P_exponents = None
        self.D_exponents = None
        self.F_exponents = None
        self.S_quantum_numbers = None
        self.P_quantum_numbers = None
        self.D_quantum_numbers = None
        self.F_quantum_numbers = None
        self.Geometrical_factor = None
        self.Geo_start_value = None
        self.Basis_set_file_name = None
        self.Basis_set = None
        self.Quadrature = None
        self.Grid_points = None
        self.Eps_eigenvalue = None
        self.BASIS = _basis5()
        self._name = "PP_BASIS"
        self._keywords = {'Eps_eigenvalue': 'EPS_EIGENVALUE', 'Grid_points': 'GRID_POINTS', 'D_exponents': 'D_EXPONENTS', 'Num_gto': 'NUM_GTO', 'D_quantum_numbers': 'D_QUANTUM_NUMBERS', 'S_quantum_numbers': 'S_QUANTUM_NUMBERS', 'F_exponents': 'F_EXPONENTS', 'Basis_set_file_name': 'BASIS_SET_FILE_NAME', 'Num_slater': 'NUM_SLATER', 'Quadrature': 'QUADRATURE', 'Geometrical_factor': 'GEOMETRICAL_FACTOR', 'F_quantum_numbers': 'F_QUANTUM_NUMBERS', 'P_exponents': 'P_EXPONENTS', 'Geo_start_value': 'GEO_START_VALUE', 'Basis_set': 'BASIS_SET', 'Basis_type': 'BASIS_TYPE', 'P_quantum_numbers': 'P_QUANTUM_NUMBERS', 'S_exponents': 'S_EXPONENTS', 'Start_index': 'START_INDEX'}
        self._subsections = {'BASIS': 'BASIS'}
        self._aliases = {'Orbital_basis_set': 'Basis_set', 'Orb_basis': 'Basis_set'}


    @property
    def Orbital_basis_set(self):
        """
        See documentation for Basis_set
        """
        return self.Basis_set

    @property
    def Orb_basis(self):
        """
        See documentation for Basis_set
        """
        return self.Basis_set

    @Orbital_basis_set.setter
    def Orbital_basis_set(self, value):
        self.Basis_set = value

    @Orb_basis.setter
    def Orb_basis(self, value):
        self.Basis_set = value
