from xcp2k.inputsection import InputSection


class _ipbv1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "IPBV"
        self._keywords = {'Rmin': 'RMIN', 'Rmax': 'RMAX', 'Rcut': 'RCUT', 'Atoms': 'ATOMS'}

