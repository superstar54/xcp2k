from xcp2k.inputsection import InputSection


class _hirshfeld_constraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Shape_function = None
        self.Gaussian_shape = None
        self.Gaussian_radius = None
        self.Atomic_radii = None
        self.Use_bohr = None
        self._name = "HIRSHFELD_CONSTRAINT"
        self._keywords = {'Shape_function': 'SHAPE_FUNCTION', 'Gaussian_shape': 'GAUSSIAN_SHAPE', 'Gaussian_radius': 'GAUSSIAN_RADIUS', 'Atomic_radii': 'ATOMIC_RADII', 'Use_bohr': 'USE_BOHR'}

