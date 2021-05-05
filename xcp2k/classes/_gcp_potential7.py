from xcp2k.inputsection import InputSection


class _gcp_potential7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Parameter_file_name = None
        self.Global_parameters = None
        self.Delta_energy = []
        self.Verbose = None
        self._name = "GCP_POTENTIAL"
        self._keywords = {'Parameter_file_name': 'PARAMETER_FILE_NAME', 'Global_parameters': 'GLOBAL_PARAMETERS', 'Verbose': 'VERBOSE'}
        self._repeated_keywords = {'Delta_energy': 'DELTA_ENERGY'}

