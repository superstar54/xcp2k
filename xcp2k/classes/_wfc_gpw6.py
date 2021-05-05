from xcp2k.inputsection import InputSection


class _wfc_gpw6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_grid = None
        self.Eps_filter = None
        self.Cutoff = None
        self.Rel_cutoff = None
        self.Print_level = None
        self.Eps_pgf_orb_s = None
        self._name = "WFC_GPW"
        self._keywords = {'Eps_grid': 'EPS_GRID', 'Eps_filter': 'EPS_FILTER', 'Cutoff': 'CUTOFF', 'Rel_cutoff': 'REL_CUTOFF', 'Print_level': 'PRINT_LEVEL', 'Eps_pgf_orb_s': 'EPS_PGF_ORB_S'}
        self._aliases = {'Relative_cutoff': 'Rel_cutoff', 'Iolevel': 'Print_level'}


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
