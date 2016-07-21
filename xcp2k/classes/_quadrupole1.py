from xcp2k.inputsection import InputSection


class _quadrupole1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom = None
        self.Cpol = None
        self._name = "QUADRUPOLE"
        self._keywords = {'Cpol': 'CPOL', 'Atom': 'ATOM'}

