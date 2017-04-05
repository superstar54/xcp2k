from xcp2k.inputsection import InputSection


class _torsion1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Kind = None
        self.K = None
        self.Phi0 = None
        self.M = None
        self._name = "TORSION"
        self._keywords = {'Kind': 'KIND', 'Phi0': 'PHI0', 'M': 'M', 'K': 'K', 'Atoms': 'ATOMS'}

