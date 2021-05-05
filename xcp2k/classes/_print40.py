from xcp2k.inputsection import InputSection


class _print40(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self._name = "PRINT"

