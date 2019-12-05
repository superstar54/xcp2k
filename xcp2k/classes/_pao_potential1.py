from xcp2k.inputsection import InputSection


class _pao_potential1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Maxl = None
        self.Beta = None
        self.Weight = None
        self.Max_projector = None
        self._name = "PAO_POTENTIAL"
        self._keywords = {'Maxl': 'MAXL', 'Beta': 'BETA', 'Weight': 'WEIGHT', 'Max_projector': 'MAX_PROJECTOR'}

