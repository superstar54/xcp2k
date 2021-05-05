from xcp2k.inputsection import InputSection


class _cell6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self.Molname = []
        self._name = "CELL"
        self._repeated_keywords = {'List': 'LIST', 'Molname': 'MOLNAME'}

