from xcp2k.inputsection import InputSection


class _buckmorse1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.F0 = None
        self.A1 = None
        self.A2 = None
        self.B1 = None
        self.B2 = None
        self.C = None
        self.D = None
        self.R0 = None
        self.Beta = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "BUCKMORSE"
        self._keywords = {'F0': 'F0', 'C': 'C', 'R0': 'R0', 'D': 'D', 'Rmax': 'RMAX', 'Rmin': 'RMIN', 'Rcut': 'RCUT', 'Atoms': 'ATOMS', 'A1': 'A1', 'Beta': 'BETA', 'A2': 'A2', 'B1': 'B1', 'B2': 'B2'}

