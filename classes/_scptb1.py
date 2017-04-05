from xcp2k.inputsection import InputSection


class _scptb1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Parameter_file_name = None
        self.Dispersion_parameter_file = None
        self.Dispersion = None
        self.Dispersion_radius = None
        self.Coordination_cutoff = None
        self.D3_scaling = None
        self.Sto_ng = None
        self.Pair_cutoff = None
        self.Do_ewald = None
        self.Do_scc = None
        self.Do_scp = None
        self._name = "SCPTB"
        self._keywords = {'Sto_ng': 'STO_NG', 'Do_scp': 'DO_SCP', 'Do_ewald': 'DO_EWALD', 'Coordination_cutoff': 'COORDINATION_CUTOFF', 'Dispersion_radius': 'DISPERSION_RADIUS', 'Pair_cutoff': 'PAIR_CUTOFF', 'Dispersion': 'DISPERSION', 'Dispersion_parameter_file': 'DISPERSION_PARAMETER_FILE', 'Parameter_file_name': 'PARAMETER_FILE_NAME', 'Do_scc': 'DO_SCC', 'D3_scaling': 'D3_SCALING'}

