from xcp2k.inputsection import InputSection


class _r_ldos2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self.Xrange = None
        self.Yrange = None
        self.Zrange = None
        self.Erange = None
        self._name = "R_LDOS"
        self._keywords = {'Xrange': 'XRANGE', 'Yrange': 'YRANGE', 'Zrange': 'ZRANGE', 'Erange': 'ERANGE'}
        self._repeated_keywords = {'List': 'LIST'}

