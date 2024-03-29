from xcp2k.inputsection import InputSection


class _point72(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Atoms = []
        self.Weights = []
        self.Xyz = None
        self._name = "POINT"
        self._keywords = {'Xyz': 'XYZ', 'Type': 'TYPE'}
        self._repeated_keywords = {'Weights': 'WEIGHTS', 'Atoms': 'ATOMS'}

