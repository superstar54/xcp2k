from xcp2k.inputsection import InputSection


class _williams1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.A = None
        self.B = None
        self.C = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "WILLIAMS"
        self._keywords = {'Atoms': 'ATOMS', 'A': 'A', 'B': 'B', 'C': 'C', 'Rcut': 'RCUT', 'Rmin': 'RMIN', 'Rmax': 'RMAX'}

