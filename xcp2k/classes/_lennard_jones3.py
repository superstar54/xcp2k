from xcp2k.inputsection import InputSection


class _lennard_jones3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Epsilon = None
        self.Sigma = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "LENNARD-JONES"
        self._keywords = {'Rmin': 'RMIN', 'Epsilon': 'EPSILON', 'Rmax': 'RMAX', 'Rcut': 'RCUT', 'Atoms': 'ATOMS', 'Sigma': 'SIGMA'}

