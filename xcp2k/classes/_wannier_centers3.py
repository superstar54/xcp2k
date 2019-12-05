from xcp2k.inputsection import InputSection
from xcp2k.classes._each213 import _each213


class _wannier_centers3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Ionspluscenters = None
        self.Format = None
        self.Charge_occup = None
        self.Charge_beta = None
        self.Charge_extended = None
        self.EACH = _each213()
        self._name = "WANNIER_CENTERS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Unit': 'UNIT', 'Ionspluscenters': 'IONS+CENTERS', 'Format': 'FORMAT', 'Charge_occup': 'CHARGE_OCCUP', 'Charge_beta': 'CHARGE_BETA', 'Charge_extended': 'CHARGE_EXTENDED'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Charge_o': 'Charge_occup', 'Charge_b': 'Charge_beta'}
        self._attributes = ['Section_parameters']


    @property
    def Charge_o(self):
        """
        See documentation for Charge_occup
        """
        return self.Charge_occup

    @property
    def Charge_b(self):
        """
        See documentation for Charge_beta
        """
        return self.Charge_beta

    @Charge_o.setter
    def Charge_o(self, value):
        self.Charge_occup = value

    @Charge_b.setter
    def Charge_b(self, value):
        self.Charge_beta = value
