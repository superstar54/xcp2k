from xcp2k.inputsection import InputSection


class _goodwin4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Vr0 = None
        self.D = None
        self.Dc = None
        self.M = None
        self.Mc = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "GOODWIN"
        self._keywords = {'Rmin': 'RMIN', 'Vr0': 'VR0', 'D': 'D', 'Mc': 'MC', 'Rmax': 'RMAX', 'M': 'M', 'Dc': 'DC', 'Rcut': 'RCUT', 'Atoms': 'ATOMS'}

