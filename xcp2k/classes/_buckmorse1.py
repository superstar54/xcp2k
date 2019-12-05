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
        self._keywords = {'Atoms': 'ATOMS', 'F0': 'F0', 'A1': 'A1', 'A2': 'A2', 'B1': 'B1', 'B2': 'B2', 'C': 'C', 'D': 'D', 'R0': 'R0', 'Beta': 'BETA', 'Rcut': 'RCUT', 'Rmin': 'RMIN', 'Rmax': 'RMAX'}

