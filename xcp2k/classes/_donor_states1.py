from xcp2k.inputsection import InputSection


class _donor_states1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Define_excited = None
        self.Atom_list = None
        self.Kind_list = None
        self.State_types = []
        self.Types = self.State_types
        self.N_search = None
        self.Localize = None
        self._name = "DONOR_STATES"
        self._keywords = {'Define_excited': 'DEFINE_EXCITED', 'Atom_list': 'ATOM_LIST', 'Kind_list': 'KIND_LIST', 'N_search': 'N_SEARCH', 'Localize': 'LOCALIZE'}
        self._repeated_keywords = {'State_types': 'STATE_TYPES'}
        self._aliases = {'At_list': 'Atom_list', 'Loc': 'Localize', 'Do_loc': 'Localize'}
        self._repeated_aliases = {'Types': 'State_types'}


    @property
    def At_list(self):
        """
        See documentation for Atom_list
        """
        return self.Atom_list

    @property
    def Loc(self):
        """
        See documentation for Localize
        """
        return self.Localize

    @property
    def Do_loc(self):
        """
        See documentation for Localize
        """
        return self.Localize

    @At_list.setter
    def At_list(self, value):
        self.Atom_list = value

    @Loc.setter
    def Loc(self, value):
        self.Localize = value

    @Do_loc.setter
    def Do_loc(self, value):
        self.Localize = value
