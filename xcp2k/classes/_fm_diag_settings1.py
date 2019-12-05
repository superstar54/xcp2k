from xcp2k.inputsection import InputSection


class _fm_diag_settings1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Parameter_a = None
        self.Parameter_x = None
        self.Print_fm_redistribute = None
        self.Elpa_force_redistribute = None
        self._name = "FM_DIAG_SETTINGS"
        self._keywords = {'Parameter_a': 'PARAMETER_A', 'Parameter_x': 'PARAMETER_X', 'Print_fm_redistribute': 'PRINT_FM_REDISTRIBUTE', 'Elpa_force_redistribute': 'ELPA_FORCE_REDISTRIBUTE'}

