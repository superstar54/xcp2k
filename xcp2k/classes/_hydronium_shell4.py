from xcp2k.inputsection import InputSection


class _hydronium_shell4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Oxygens = []
        self.Hydrogens = []
        self.Roo = None
        self.Poo = None
        self.Qoo = None
        self.Roh = None
        self.Poh = None
        self.Qoh = None
        self.Nh = None
        self.Pm = None
        self.Qm = None
        self.Lambda = None
        self._name = "HYDRONIUM_SHELL"
        self._keywords = {'Roh': 'ROH', 'Nh': 'NH', 'Roo': 'ROO', 'Poo': 'POO', 'Lambda': 'LAMBDA', 'Poh': 'POH', 'Qoo': 'QOO', 'Pm': 'PM', 'Qm': 'QM', 'Qoh': 'QOH'}
        self._repeated_keywords = {'Oxygens': 'OXYGENS', 'Hydrogens': 'HYDROGENS'}
        self._aliases = {'Expon_numerator': 'Pm', 'Expon_denominatora': 'Qoo', 'Expon_numeratorb': 'Poh', 'Expon_numeratora': 'Poo', 'Expon_denominatorb': 'Qoh', 'Expon_denominator': 'Qm'}


    @property
    def Expon_numeratora(self):
        """
        See documentation for Poo
        """
        return self.Poo

    @property
    def Expon_denominatora(self):
        """
        See documentation for Qoo
        """
        return self.Qoo

    @property
    def Expon_numeratorb(self):
        """
        See documentation for Poh
        """
        return self.Poh

    @property
    def Expon_denominatorb(self):
        """
        See documentation for Qoh
        """
        return self.Qoh

    @property
    def Expon_numerator(self):
        """
        See documentation for Pm
        """
        return self.Pm

    @property
    def Expon_denominator(self):
        """
        See documentation for Qm
        """
        return self.Qm

    @Expon_numeratora.setter
    def Expon_numeratora(self, value):
        self.Poo = value

    @Expon_denominatora.setter
    def Expon_denominatora(self, value):
        self.Qoo = value

    @Expon_numeratorb.setter
    def Expon_numeratorb(self, value):
        self.Poh = value

    @Expon_denominatorb.setter
    def Expon_denominatorb(self, value):
        self.Qoh = value

    @Expon_numerator.setter
    def Expon_numerator(self, value):
        self.Pm = value

    @Expon_denominator.setter
    def Expon_denominator(self, value):
        self.Qm = value
