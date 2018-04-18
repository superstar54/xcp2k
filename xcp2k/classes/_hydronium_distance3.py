from xcp2k.inputsection import InputSection


class _hydronium_distance3(InputSection):
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
        self._keywords = {'Roh': 'ROH', 'Nh': 'NH', 'Nn': 'NN', 'Lambda': 'LAMBDA', 'Pf': 'PF', 'Poh': 'POH', 'Qf': 'QF', 'Qoh': 'QOH', 'Qm': 'QM', 'Pm': 'PM'}
        self._repeated_keywords = {'Oxygens': 'OXYGENS', 'Hydrogens': 'HYDROGENS'}

