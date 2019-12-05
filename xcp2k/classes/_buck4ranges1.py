from xcp2k.inputsection import InputSection


class _buck4ranges1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.A = None
        self.B = None
        self.C = None
        self.R1 = None
        self.R2 = None
        self.R3 = None
        self.Poly1 = []
        self.Poly2 = []
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "BUCK4RANGES"
        self._keywords = {'Atoms': 'ATOMS', 'A': 'A', 'B': 'B', 'C': 'C', 'R1': 'R1', 'R2': 'R2', 'R3': 'R3', 'Rcut': 'RCUT', 'Rmin': 'RMIN', 'Rmax': 'RMAX'}
        self._repeated_keywords = {'Poly1': 'POLY1', 'Poly2': 'POLY2'}

