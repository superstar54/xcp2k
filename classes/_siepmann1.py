from xcp2k.inputsection import InputSection


class _siepmann1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.B = None
        self.D = None
        self.E = None
        self.F = None
        self.Beta = None
        self.Rcut = None
        self.Allow_oh_formation = None
        self._name = "SIEPMANN"
        self._keywords = {'B': 'B', 'E': 'E', 'D': 'D', 'F': 'F', 'Allow_oh_formation': 'ALLOW_OH_FORMATION', 'Rcut': 'RCUT', 'Atoms': 'ATOMS', 'Beta': 'BETA'}

