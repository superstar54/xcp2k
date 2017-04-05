from xcp2k.inputsection import InputSection


class _wavelet1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Scf_type = None
        self._name = "WAVELET"
        self._keywords = {'Scf_type': 'SCF_TYPE'}

