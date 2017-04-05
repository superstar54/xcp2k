from xcp2k.inputsection import InputSection


class _wfc_gpw3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_grid = None
        self.Eps_filter = None
        self.Cutoff = None
        self.Rel_cutoff = None
        self.Multipole_two_cent_int = None
        self.Print_level = None
        self._name = "WFC_GPW"
        self._keywords = {'Cutoff': 'CUTOFF', 'Eps_filter': 'EPS_FILTER', 'Rel_cutoff': 'REL_CUTOFF', 'Print_level': 'PRINT_LEVEL', 'Multipole_two_cent_int': 'MULTIPOLE_TWO_CENT_INT', 'Eps_grid': 'EPS_GRID'}
        self._aliases = {'Iolevel': 'Print_level', 'Relative_cutoff': 'Rel_cutoff'}


    @property
    def Relative_cutoff(self):
        """
        See documentation for Rel_cutoff
        """
        return self.Rel_cutoff

    @property
    def Iolevel(self):
        """
        See documentation for Print_level
        """
        return self.Print_level

    @Relative_cutoff.setter
    def Relative_cutoff(self, value):
        self.Rel_cutoff = value

    @Iolevel.setter
    def Iolevel(self, value):
        self.Print_level = value
