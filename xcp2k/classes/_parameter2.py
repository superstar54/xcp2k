from xcp2k.inputsection import InputSection


class _parameter2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Param_file_path = None
        self.Param_file_name = None
        self.Dispersion_parameter_file = None
        self.Dispersion_radius = None
        self.Coordination_cutoff = None
        self.D3bj_scaling = None
        self.D3bj_param = None
        self.Huckel_constants = None
        self.Coulomb_constants = None
        self.Cn_constants = None
        self.En_constant = None
        self.Halogen_binding = None
        self.Kab_param = []
        self.Xb_radius = None
        self._name = "PARAMETER"
        self._keywords = {'Param_file_path': 'PARAM_FILE_PATH', 'Param_file_name': 'PARAM_FILE_NAME', 'Dispersion_parameter_file': 'DISPERSION_PARAMETER_FILE', 'Dispersion_radius': 'DISPERSION_RADIUS', 'Coordination_cutoff': 'COORDINATION_CUTOFF', 'D3bj_scaling': 'D3BJ_SCALING', 'D3bj_param': 'D3BJ_PARAM', 'Huckel_constants': 'HUCKEL_CONSTANTS', 'Coulomb_constants': 'COULOMB_CONSTANTS', 'Cn_constants': 'CN_CONSTANTS', 'En_constant': 'EN_CONSTANT', 'Halogen_binding': 'HALOGEN_BINDING', 'Xb_radius': 'XB_RADIUS'}
        self._repeated_keywords = {'Kab_param': 'KAB_PARAM'}

