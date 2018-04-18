from xcp2k.inputsection import InputSection
from _print17 import _print17


class _mixed_cdft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Lambda = None
        self.Force_states = None
        self.Coupling = None
        self.Dlb = None
        self.Metric = None
        self.Wfn_overlap = None
        self.Lowdin = None
        self.Ci = None
        self.Nonorthogonal_coupling = None
        self.Scale_with_occupation_numbers = None
        self.Wfn_restart_file_name = None
        self.Eps_svd = None
        self.Eps_occupied = None
        self.Load_scale = None
        self.More_work = None
        self.Very_overloaded = None
        self.PRINT = _print17()
        self._name = "MIXED_CDFT"
        self._keywords = {'Dlb': 'DLB', 'Ci': 'CI', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME', 'Coupling': 'COUPLING', 'Force_states': 'FORCE_STATES', 'More_work': 'MORE_WORK', 'Metric': 'METRIC', 'Nonorthogonal_coupling': 'NONORTHOGONAL_COUPLING', 'Scale_with_occupation_numbers': 'SCALE_WITH_OCCUPATION_NUMBERS', 'Wfn_overlap': 'WFN_OVERLAP', 'Eps_svd': 'EPS_SVD', 'Eps_occupied': 'EPS_OCCUPIED', 'Load_scale': 'LOAD_SCALE', 'Lowdin': 'LOWDIN', 'Very_overloaded': 'VERY_OVERLOADED', 'Lambda': 'LAMBDA'}
        self._subsections = {'PRINT': 'PRINT'}
        self._aliases = {'Nonortho_coupling': 'Nonorthogonal_coupling', 'Coupling_metric': 'Metric', 'Configuration_interaction': 'Ci'}


    @property
    def Coupling_metric(self):
        """
        See documentation for Metric
        """
        return self.Metric

    @property
    def Configuration_interaction(self):
        """
        See documentation for Ci
        """
        return self.Ci

    @property
    def Nonortho_coupling(self):
        """
        See documentation for Nonorthogonal_coupling
        """
        return self.Nonorthogonal_coupling

    @Coupling_metric.setter
    def Coupling_metric(self, value):
        self.Metric = value

    @Configuration_interaction.setter
    def Configuration_interaction(self, value):
        self.Ci = value

    @Nonortho_coupling.setter
    def Nonortho_coupling(self, value):
        self.Nonorthogonal_coupling = value
