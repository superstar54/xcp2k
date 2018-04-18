from xcp2k.inputsection import InputSection


class _cutoff_calib7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Min = None
        self.Max = None
        self.Delta = None
        self.Eps = None
        self._name = "CUTOFF_CALIB"
        self._keywords = {'Max': 'MAX', 'Delta': 'DELTA', 'Eps': 'EPS', 'Min': 'MIN'}

