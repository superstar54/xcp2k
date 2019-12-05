from xcp2k.inputsection import InputSection


class _hydronium_distance4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Oxygens = []
        self.Hydrogens = []
        self.Roh = None
        self.Poh = None
        self.Qoh = None
        self.Nh = None
        self.Pm = None
        self.Qm = None
        self.Nn = None
        self.Pf = None
        self.Qf = None
        self.Lambda = None
        self._name = "HYDRONIUM_DISTANCE"
        self._keywords = {'Roh': 'ROH', 'Poh': 'POH', 'Qoh': 'QOH', 'Nh': 'NH', 'Pm': 'PM', 'Qm': 'QM', 'Nn': 'NN', 'Pf': 'PF', 'Qf': 'QF', 'Lambda': 'LAMBDA'}
        self._repeated_keywords = {'Oxygens': 'OXYGENS', 'Hydrogens': 'HYDROGENS'}

