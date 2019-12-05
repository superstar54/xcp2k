from xcp2k.inputsection import InputSection


class _lennard_jones1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Epsilon = None
        self.Sigma = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "LENNARD-JONES"
        self._keywords = {'Atoms': 'ATOMS', 'Epsilon': 'EPSILON', 'Sigma': 'SIGMA', 'Rcut': 'RCUT', 'Rmin': 'RMIN', 'Rmax': 'RMAX'}

