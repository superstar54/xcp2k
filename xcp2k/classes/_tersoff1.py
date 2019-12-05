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
        self._keywords = {'Atoms': 'ATOMS', 'A': 'A', 'B': 'B', 'Lambda1': 'LAMBDA1', 'Lambda2': 'LAMBDA2', 'Alpha': 'ALPHA', 'Beta': 'BETA', 'N': 'N', 'C': 'C', 'D': 'D', 'H': 'H', 'Lambda3': 'LAMBDA3', 'Bigr': 'BIGR', 'Bigd': 'BIGD', 'Rcut': 'RCUT'}

