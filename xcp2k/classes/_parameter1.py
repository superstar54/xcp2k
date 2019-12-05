from xcp2k.inputsection import InputSection


class _parameter1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Sk_file = []
        self.Param_file_path = None
        self.Param_file_name = None
        self.Dispersion_type = None
        self.Uff_force_field = None
        self.Dispersion_parameter_file = None
        self.Dispersion_radius = None
        self.Coordination_cutoff = None
        self.D3_scaling = None
        self.Hb_sr_param = None
        self._name = "PARAMETER"
        self._keywords = {'Param_file_path': 'PARAM_FILE_PATH', 'Param_file_name': 'PARAM_FILE_NAME', 'Dispersion_type': 'DISPERSION_TYPE', 'Uff_force_field': 'UFF_FORCE_FIELD', 'Dispersion_parameter_file': 'DISPERSION_PARAMETER_FILE', 'Dispersion_radius': 'DISPERSION_RADIUS', 'Coordination_cutoff': 'COORDINATION_CUTOFF', 'D3_scaling': 'D3_SCALING', 'Hb_sr_param': 'HB_SR_PARAM'}
        self._repeated_keywords = {'Sk_file': 'SK_FILE'}

