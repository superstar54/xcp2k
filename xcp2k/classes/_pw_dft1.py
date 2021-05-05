from xcp2k.inputsection import InputSection


class _pw_dft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self._name = "PW_DFT"

