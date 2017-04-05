from xcp2k.inputsection import InputSection


class _tersoff1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.A = None
        self.B = None
        self.Lambda1 = None
        self.Lambda2 = None
        self.Alpha = None
        self.Beta = None
        self.N = None
        self.C = None
        self.D = None
        self.H = None
        self.Lambda3 = None
        self.Bigr = None
        self.Bigd = None
        self.Rcut = None
        self._name = "TERSOFF"
        self._keywords = {'A': 'A', 'C': 'C', 'B': 'B', 'D': 'D', 'Bigr': 'BIGR', 'H': 'H', 'Rcut': 'RCUT', 'Atoms': 'ATOMS', 'Beta': 'BETA', 'Bigd': 'BIGD', 'Alpha': 'ALPHA', 'N': 'N', 'Lambda1': 'LAMBDA1', 'Lambda2': 'LAMBDA2', 'Lambda3': 'LAMBDA3'}

