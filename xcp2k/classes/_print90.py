from xcp2k.inputsection import InputSection


class _print90(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self._name = "PRINT"

