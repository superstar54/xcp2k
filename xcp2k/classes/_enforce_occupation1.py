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
        self._keywords = {'Max_scf': 'MAX_SCF', 'Eps_scf': 'EPS_SCF', 'Nelec': 'NELEC', 'Orbitals': 'ORBITALS', 'Smear': 'SMEAR'}
        self._aliases = {'M': 'Orbitals', 'N_electrons': 'Nelec'}
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
