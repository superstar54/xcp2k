from xcp2k.inputsection import InputSection


class _staging1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.J = None
        self.Q_end = None
        self._name = "STAGING"
        self._keywords = {'J': 'J', 'Q_end': 'Q_END'}

