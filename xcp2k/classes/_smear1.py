from xcp2k.inputsection import InputSection


class _smear1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Method = None
        self.List = None
        self.Electronic_temperature = None
        self.Eps_fermi_dirac = None
        self.Window_size = None
        self.Fixed_magnetic_moment = None
        self._name = "SMEAR"
        self._keywords = {'Window_size': 'WINDOW_SIZE', 'Electronic_temperature': 'ELECTRONIC_TEMPERATURE', 'Eps_fermi_dirac': 'EPS_FERMI_DIRAC', 'List': 'LIST', 'Fixed_magnetic_moment': 'FIXED_MAGNETIC_MOMENT', 'Method': 'METHOD'}
        self._aliases = {'Elec_temp': 'Electronic_temperature', 'Telec': 'Electronic_temperature'}
        self._attributes = ['Section_parameters']


    @property
    def Elec_temp(self):
        """
        See documentation for Electronic_temperature
        """
        return self.Electronic_temperature

    @property
    def Telec(self):
        """
        See documentation for Electronic_temperature
        """
        return self.Electronic_temperature

    @Elec_temp.setter
    def Elec_temp(self, value):
        self.Electronic_temperature = value

    @Telec.setter
    def Telec(self, value):
        self.Electronic_temperature = value
