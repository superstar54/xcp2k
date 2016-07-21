from xcp2k.inputsection import InputSection
from _m_sampling1 import _m_sampling1
from _rdf1 import _rdf1
from _rho1 import _rho1
from _coord8 import _coord8
from _perm1 import _perm1
from _averages2 import _averages2
from _force6 import _force6
from _rng_state1 import _rng_state1
from _print14 import _print14


class _helium1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Helium_only = None
        self.Interaction_pot_scan = None
        self.Num_env = None
        self.Potential_file_name = None
        self.Get_forces = None
        self.Solute_interaction = None
        self.Natoms = None
        self.Nbeads = None
        self.N_inner = None
        self.N_outer = None
        self.Bisection = None
        self.Max_perm_cycle = None
        self.Sampling_method = None
        self.Periodic = None
        self.Cell_size = None
        self.Cell_shape = None
        self.Droplet_radius = None
        self.Density = None
        self.Presample = None
        self.Drop_unused_envs = None
        self.M_SAMPLING = _m_sampling1()
        self.RDF = _rdf1()
        self.RHO = _rho1()
        self.COORD = _coord8()
        self.PERM = _perm1()
        self.AVERAGES = _averages2()
        self.FORCE = _force6()
        self.RNG_STATE = _rng_state1()
        self.PRINT = _print14()
        self._name = "HELIUM"
        self._keywords = {'Get_forces': 'GET_FORCES', 'Natoms': 'NATOMS', 'N_inner': 'N_INNER', 'Max_perm_cycle': 'MAX_PERM_CYCLE', 'Nbeads': 'NBEADS', 'Interaction_pot_scan': 'INTERACTION_POT_SCAN', 'N_outer': 'N_OUTER', 'Density': 'DENSITY', 'Sampling_method': 'SAMPLING_METHOD', 'Cell_shape': 'CELL_SHAPE', 'Periodic': 'PERIODIC', 'Num_env': 'NUM_ENV', 'Potential_file_name': 'POTENTIAL_FILE_NAME', 'Bisection': 'BISECTION', 'Droplet_radius': 'DROPLET_RADIUS', 'Presample': 'PRESAMPLE', 'Helium_only': 'HELIUM_ONLY', 'Cell_size': 'CELL_SIZE', 'Solute_interaction': 'SOLUTE_INTERACTION', 'Drop_unused_envs': 'DROP_UNUSED_ENVS'}
        self._subsections = {'RNG_STATE': 'RNG_STATE', 'FORCE': 'FORCE', 'COORD': 'COORD', 'RDF': 'RDF', 'PERM': 'PERM', 'RHO': 'RHO', 'PRINT': 'PRINT', 'AVERAGES': 'AVERAGES', 'M_SAMPLING': 'M-SAMPLING'}
        self._aliases = {'Inorot': 'N_inner', 'Irot': 'N_outer'}
        self._attributes = ['Section_parameters']


    @property
    def Inorot(self):
        """
        See documentation for N_inner
        """
        return self.N_inner

    @property
    def Irot(self):
        """
        See documentation for N_outer
        """
        return self.N_outer

    @Inorot.setter
    def Inorot(self, value):
        self.N_inner = value

    @Irot.setter
    def Irot(self, value):
        self.N_outer = value
