from xcp2k.inputsection import InputSection


class _acid_hydronium_shell1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Oxygens_water = []
        self.Oxygens_acid = []
        self.Hydrogens = []
        self.Pwoh = None
        self.Qwoh = None
        self.Rwoh = None
        self.Paoh = None
        self.Qaoh = None
        self.Raoh = None
        self.Poo = None
        self.Qoo = None
        self.Roo = None
        self.Pm = None
        self.Qm = None
        self.Nh = None
        self.Pcut = None
        self.Qcut = None
        self.Nc = None
        self.Lambda = None
        self.Lambda = None
        self._name = "ACID_HYDRONIUM_SHELL"
        self._keywords = {'Pwoh': 'PWOH', 'Qwoh': 'QWOH', 'Rwoh': 'RWOH', 'Paoh': 'PAOH', 'Qaoh': 'QAOH', 'Raoh': 'RAOH', 'Poo': 'POO', 'Qoo': 'QOO', 'Roo': 'ROO', 'Pm': 'PM', 'Qm': 'QM', 'Nh': 'NH', 'Pcut': 'PCUT', 'Qcut': 'QCUT', 'Nc': 'NC', 'Lambda': 'LAMBDA'}
        self._repeated_keywords = {'Oxygens_water': 'OXYGENS_WATER', 'Oxygens_acid': 'OXYGENS_ACID', 'Hydrogens': 'HYDROGENS'}

