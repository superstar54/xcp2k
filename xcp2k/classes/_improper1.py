from xcp2k.inputsection import InputSection


class _improper1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Kind = None
        self.K = None
        self.Phi0 = None
        self._name = "IMPROPER"
        self._keywords = {'Kind': 'KIND', 'Phi0': 'PHI0', 'K': 'K', 'Atoms': 'ATOMS'}

