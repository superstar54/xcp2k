from xcp2k.inputsection import InputSection


class _print_orbital_cubes1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Filename = None
        self.Alist = None
        self.Blist = None
        self.Stride = None
        self._name = "PRINT_ORBITAL_CUBES"
        self._keywords = {'Filename': 'FILENAME', 'Alist': 'ALIST', 'Blist': 'BLIST', 'Stride': 'STRIDE'}

