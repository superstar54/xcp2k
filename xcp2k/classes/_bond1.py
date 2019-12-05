from xcp2k.inputsection import InputSection


class _bond1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Kind = None
        self.K = None
        self.Cs = None
        self.R0 = None
        self._name = "BOND"
        self._keywords = {'Atoms': 'ATOMS', 'Kind': 'KIND', 'K': 'K', 'Cs': 'CS', 'R0': 'R0'}

