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
        self._keywords = {'A': 'A', 'C': 'C', 'B': 'B', 'R1': 'R1', 'R2': 'R2', 'R3': 'R3', 'Rmax': 'RMAX', 'Rmin': 'RMIN', 'Rcut': 'RCUT', 'Atoms': 'ATOMS'}
        self._repeated_keywords = {'Poly2': 'POLY2', 'Poly1': 'POLY1'}

