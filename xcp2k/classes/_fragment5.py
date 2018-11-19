from xcp2k.inputsection import InputSection


class _fragment5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self._name = "FRAGMENT"
        self._repeated_keywords = {'List': 'LIST'}

