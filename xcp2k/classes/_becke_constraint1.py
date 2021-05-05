from xcp2k.inputsection import InputSection


class _becke_constraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Adjust_size = None
        self.Atomic_radii = None
        self.Should_skip = None
        self.Cavity_confine = None
        self.Cavity_shape = None
        self.Cavity_use_bohr = None
        self.Cavity_print = None
        self.Cavity_radius = None
        self.Eps_cavity = None
        self.Cutoff_type = None
        self.Global_cutoff = None
        self.Element_cutoff = None
        self.In_memory = None
        self._name = "BECKE_CONSTRAINT"
        self._keywords = {'Adjust_size': 'ADJUST_SIZE', 'Atomic_radii': 'ATOMIC_RADII', 'Should_skip': 'SHOULD_SKIP', 'Cavity_confine': 'CAVITY_CONFINE', 'Cavity_shape': 'CAVITY_SHAPE', 'Cavity_use_bohr': 'CAVITY_USE_BOHR', 'Cavity_print': 'CAVITY_PRINT', 'Cavity_radius': 'CAVITY_RADIUS', 'Eps_cavity': 'EPS_CAVITY', 'Cutoff_type': 'CUTOFF_TYPE', 'Global_cutoff': 'GLOBAL_CUTOFF', 'Element_cutoff': 'ELEMENT_CUTOFF', 'In_memory': 'IN_MEMORY'}

