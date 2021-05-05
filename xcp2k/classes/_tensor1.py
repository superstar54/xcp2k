from xcp2k.inputsection import InputSection


class _tensor1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Tas_split_factor = None
        self._name = "TENSOR"
        self._keywords = {'Tas_split_factor': 'TAS_SPLIT_FACTOR'}

