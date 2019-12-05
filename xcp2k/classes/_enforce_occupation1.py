from xcp2k.inputsection import InputSection


class _enforce_occupation1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Nelec = None
        self.Orbitals = None
        self.Eps_scf = None
        self.Max_scf = None
        self.Smear = None
        self._name = "ENFORCE_OCCUPATION"
        self._keywords = {'Nelec': 'NELEC', 'Orbitals': 'ORBITALS', 'Eps_scf': 'EPS_SCF', 'Max_scf': 'MAX_SCF', 'Smear': 'SMEAR'}
        self._aliases = {'N_electrons': 'Nelec', 'M': 'Orbitals'}
        self._attributes = ['Section_parameters']


    @property
    def N_electrons(self):
        """
        See documentation for Nelec
        """
        return self.Nelec

    @property
    def M(self):
        """
        See documentation for Orbitals
        """
        return self.Orbitals

    @N_electrons.setter
    def N_electrons(self, value):
        self.Nelec = value

    @M.setter
    def M(self, value):
        self.Orbitals = value
