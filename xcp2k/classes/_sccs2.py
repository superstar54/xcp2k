from xcp2k.inputsection import InputSection
from _andreussi1 import _andreussi1
from _fattebert_gygi1 import _fattebert_gygi1


class _sccs2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Alpha = None
        self.Beta = None
        self.Delta_rho = None
        self.Derivative_method = None
        self.Dielectric_constant = None
        self.Eps_sccs = None
        self.Eps_scf = None
        self.Gamma = None
        self.Max_iter = None
        self.Method = None
        self.Mixing = None
        self.ANDREUSSI = _andreussi1()
        self.FATTEBERT_GYGI = _fattebert_gygi1()
        self._name = "SCCS"
        self._keywords = {'Derivative_method': 'DERIVATIVE_METHOD', 'Max_iter': 'MAX_ITER', 'Mixing': 'MIXING', 'Beta': 'BETA', 'Eps_scf': 'EPS_SCF', 'Eps_sccs': 'EPS_SCCS', 'Dielectric_constant': 'DIELECTRIC_CONSTANT', 'Alpha': 'ALPHA', 'Method': 'METHOD', 'Gamma': 'GAMMA', 'Delta_rho': 'DELTA_RHO'}
        self._subsections = {'ANDREUSSI': 'ANDREUSSI', 'FATTEBERT_GYGI': 'FATTEBERT-GYGI'}
        self._aliases = {'Tau_pol': 'Eps_sccs', 'Eps_iter': 'Eps_sccs', 'Surface_tension': 'Gamma', 'Eta': 'Mixing', 'Epsilon_solvent': 'Dielectric_constant'}
        self._attributes = ['Section_parameters']


    @property
    def Epsilon_solvent(self):
        """
        See documentation for Dielectric_constant
        """
        return self.Dielectric_constant

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

    @Epsilon_solvent.setter
    def Epsilon_solvent(self, value):
        self.Dielectric_constant = value

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
