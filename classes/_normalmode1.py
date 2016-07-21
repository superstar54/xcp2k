from xcp2k.inputsection import InputSection


class _normalmode1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Q_centroid = None
        self.Q_bead = None
        self.Modefactor = None
        self._name = "NORMALMODE"
        self._keywords = {'Q_centroid': 'Q_CENTROID', 'Modefactor': 'MODEFACTOR', 'Q_bead': 'Q_BEAD'}

