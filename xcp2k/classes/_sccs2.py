from xcp2k.inputsection import InputSection
from xcp2k.classes._andreussi1 import _andreussi1
from xcp2k.classes._fattebert_gygi1 import _fattebert_gygi1


class _sccs2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Alpha = None
        self.Beta = None
        self.Delta_rho = None
        self.Derivative_method = None
        self.Relative_permittivity = None
        self.Eps_sccs = None
        self.Eps_scf = None
        self.Gamma = None
        self.Max_iter = None
        self.Method = None
        self.Mixing = None
        self.ANDREUSSI = _andreussi1()
        self.FATTEBERT_GYGI = _fattebert_gygi1()
        self._name = "SCCS"
        self._keywords = {'Alpha': 'ALPHA', 'Beta': 'BETA', 'Delta_rho': 'DELTA_RHO', 'Derivative_method': 'DERIVATIVE_METHOD', 'Relative_permittivity': 'RELATIVE_PERMITTIVITY', 'Eps_sccs': 'EPS_SCCS', 'Eps_scf': 'EPS_SCF', 'Gamma': 'GAMMA', 'Max_iter': 'MAX_ITER', 'Method': 'METHOD', 'Mixing': 'MIXING'}
        self._subsections = {'ANDREUSSI': 'ANDREUSSI', 'FATTEBERT_GYGI': 'FATTEBERT-GYGI'}
        self._aliases = {'Dielectric_constant': 'Relative_permittivity', 'Epsilon_relative': 'Relative_permittivity', 'Epsilon_solvent': 'Relative_permittivity', 'Eps_iter': 'Eps_sccs', 'Tau_pol': 'Eps_sccs', 'Surface_tension': 'Gamma', 'Eta': 'Mixing'}
        self._attributes = ['Section_parameters']


    @property
    def Dielectric_constant(self):
        """
        See documentation for Relative_permittivity
        """
        return self.Relative_permittivity

    @property
    def Epsilon_relative(self):
        """
        See documentation for Relative_permittivity
        """
        return self.Relative_permittivity

    @property
    def Epsilon_solvent(self):
        """
        See documentation for Relative_permittivity
        """
        return self.Relative_permittivity

    @property
    def Eps_iter(self):
        """
        See documentation for Eps_sccs
        """
        return self.Eps_sccs

    @property
    def Tau_pol(self):
        """
        See documentation for Eps_sccs
        """
        return self.Eps_sccs

    @property
    def Surface_tension(self):
        """
        See documentation for Gamma
        """
        return self.Gamma

    @property
    def Eta(self):
        """
        See documentation for Mixing
        """
        return self.Mixing

    @Dielectric_constant.setter
    def Dielectric_constant(self, value):
        self.Relative_permittivity = value

    @Epsilon_relative.setter
    def Epsilon_relative(self, value):
        self.Relative_permittivity = value

    @Epsilon_solvent.setter
    def Epsilon_solvent(self, value):
        self.Relative_permittivity = value

    @Eps_iter.setter
    def Eps_iter(self, value):
        self.Eps_sccs = value

    @Tau_pol.setter
    def Tau_pol(self, value):
        self.Eps_sccs = value

    @Surface_tension.setter
    def Surface_tension(self, value):
        self.Gamma = value

    @Eta.setter
    def Eta(self, value):
        self.Mixing = value
