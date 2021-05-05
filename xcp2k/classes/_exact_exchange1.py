from xcp2k.inputsection import InputSection
from xcp2k.classes._ri_metric5 import _ri_metric5


class _exact_exchange1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Potential_type = None
        self.Cutoff_radius = None
        self.T_c_g_data = None
        self.Omega = None
        self.Eps_range = None
        self.Eps_screening = None
        self.Scale = None
        self.RI_METRIC = _ri_metric5()
        self._name = "EXACT_EXCHANGE"
        self._keywords = {'Potential_type': 'POTENTIAL_TYPE', 'Cutoff_radius': 'CUTOFF_RADIUS', 'T_c_g_data': 'T_C_G_DATA', 'Omega': 'OMEGA', 'Eps_range': 'EPS_RANGE', 'Eps_screening': 'EPS_SCREENING', 'Scale': 'SCALE'}
        self._subsections = {'RI_METRIC': 'RI_METRIC'}
        self._aliases = {'Op': 'Potential_type', 'Operator': 'Potential_type', 'Potential': 'Potential_type', 'R_c': 'Cutoff_radius', 'Rc': 'Cutoff_radius', 'Range': 'Cutoff_radius', 'Eps_screen': 'Eps_screening', 'Fraction': 'Scale'}
        self._attributes = ['Section_parameters']


    @property
    def Op(self):
        """
        See documentation for Potential_type
        """
        return self.Potential_type

    @property
    def Operator(self):
        """
        See documentation for Potential_type
        """
        return self.Potential_type

    @property
    def Potential(self):
        """
        See documentation for Potential_type
        """
        return self.Potential_type

    @property
    def R_c(self):
        """
        See documentation for Cutoff_radius
        """
        return self.Cutoff_radius

    @property
    def Rc(self):
        """
        See documentation for Cutoff_radius
        """
        return self.Cutoff_radius

    @property
    def Range(self):
        """
        See documentation for Cutoff_radius
        """
        return self.Cutoff_radius

    @property
    def Eps_screen(self):
        """
        See documentation for Eps_screening
        """
        return self.Eps_screening

    @property
    def Fraction(self):
        """
        See documentation for Scale
        """
        return self.Scale

    @Op.setter
    def Op(self, value):
        self.Potential_type = value

    @Operator.setter
    def Operator(self, value):
        self.Potential_type = value

    @Potential.setter
    def Potential(self, value):
        self.Potential_type = value

    @R_c.setter
    def R_c(self, value):
        self.Cutoff_radius = value

    @Rc.setter
    def Rc(self, value):
        self.Cutoff_radius = value

    @Range.setter
    def Range(self, value):
        self.Cutoff_radius = value

    @Eps_screen.setter
    def Eps_screen(self, value):
        self.Eps_screening = value

    @Fraction.setter
    def Fraction(self, value):
        self.Scale = value
