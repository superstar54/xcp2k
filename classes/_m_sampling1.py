from xcp2k.inputsection import InputSection


class _m_sampling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Distribution_type = None
        self.M_value = None
        self.M_ratio = None
        self._name = "M-SAMPLING"
        self._keywords = {'M_value': 'M-VALUE', 'Distribution_type': 'DISTRIBUTION-TYPE', 'M_ratio': 'M-RATIO'}

