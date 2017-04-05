from xcp2k.inputsection import InputSection
from _point30 import _point30


class _hydronium2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Oxygens = []
        self.Hydrogens = []
        self.Roo = None
        self.Pno = None
        self.Qno = None
        self.Roh = None
        self.Pnh = None
        self.Qnh = None
        self.Nh = None
        self.P = None
        self.Q = None
        self.Lambda = None
        self.Lambda = None
        self.POINT_list = []
        self._name = "HYDRONIUM"
        self._keywords = {'Roh': 'ROH', 'Nh': 'NH', 'P': 'P', 'Roo': 'ROO', 'Q': 'Q', 'Pnh': 'PNH', 'Pno': 'PNO', 'Qno': 'QNO', 'Qnh': 'QNH', 'Lambda': 'LAMBDA'}
        self._repeated_keywords = {'Oxygens': 'OXYGENS', 'Hydrogens': 'HYDROGENS'}
        self._repeated_subsections = {'POINT': '_point30'}
        self._aliases = {'Expon_numerator': 'P', 'Nhtest': 'Nh', 'R_oh': 'Roh', 'Expon_denominator': 'Q', 'R_oo': 'Roo', 'Expon_numeratorb': 'Pnh', 'Expon_numeratora': 'Pno', 'Expon_denominatorb': 'Qnh', 'Expon_denominatora': 'Qno'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point30()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def R_oo(self):
        """
        See documentation for Roo
        """
        return self.Roo

    @property
    def Expon_numeratora(self):
        """
        See documentation for Pno
        """
        return self.Pno

    @property
    def Expon_denominatora(self):
        """
        See documentation for Qno
        """
        return self.Qno

    @property
    def R_oh(self):
        """
        See documentation for Roh
        """
        return self.Roh

    @property
    def Expon_numeratorb(self):
        """
        See documentation for Pnh
        """
        return self.Pnh

    @property
    def Expon_denominatorb(self):
        """
        See documentation for Qnh
        """
        return self.Qnh

    @property
    def Nhtest(self):
        """
        See documentation for Nh
        """
        return self.Nh

    @property
    def Expon_numerator(self):
        """
        See documentation for P
        """
        return self.P

    @property
    def Expon_denominator(self):
        """
        See documentation for Q
        """
        return self.Q

    @R_oo.setter
    def R_oo(self, value):
        self.Roo = value

    @Expon_numeratora.setter
    def Expon_numeratora(self, value):
        self.Pno = value

    @Expon_denominatora.setter
    def Expon_denominatora(self, value):
        self.Qno = value

    @R_oh.setter
    def R_oh(self, value):
        self.Roh = value

    @Expon_numeratorb.setter
    def Expon_numeratorb(self, value):
        self.Pnh = value

    @Expon_denominatorb.setter
    def Expon_denominatorb(self, value):
        self.Qnh = value

    @Nhtest.setter
    def Nhtest(self, value):
        self.Nh = value

    @Expon_numerator.setter
    def Expon_numerator(self, value):
        self.P = value

    @Expon_denominator.setter
    def Expon_denominator(self, value):
        self.Q = value
