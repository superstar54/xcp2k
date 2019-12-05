from xcp2k.inputsection import InputSection


class _point27(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Atoms = []
        self.Weights = []
        self.Xyz = None
        self._name = "POINT"
        self._keywords = {'Type': 'TYPE', 'Xyz': 'XYZ'}
        self._repeated_keywords = {'Atoms': 'ATOMS', 'Weights': 'WEIGHTS'}

