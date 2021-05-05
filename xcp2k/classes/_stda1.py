from xcp2k.inputsection import InputSection


class _stda1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Do_ewald = None
        self.Eps_td_filter = None
        self._name = "STDA"
        self._keywords = {'Fraction': 'FRACTION', 'Do_ewald': 'DO_EWALD', 'Eps_td_filter': 'EPS_TD_FILTER'}
        self._aliases = {'Hfx_fraction': 'Fraction'}


    @property
    def Hfx_fraction(self):
        """
        See documentation for Fraction
        """
        return self.Fraction

    @Hfx_fraction.setter
    def Hfx_fraction(self, value):
        self.Fraction = value
