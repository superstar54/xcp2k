from xcp2k.inputsection import InputSection


class _opt_dmfet1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_iter = None
        self.Trust_rad = None
        self.Dm_conv_max = None
        self.Dm_conv_int = None
        self.Beta_dm_conv_max = None
        self.Beta_dm_conv_int = None
        self.Read_dmfet_pot = None
        self.Dmfet_restart_file_name = None
        self._name = "OPT_DMFET"
        self._keywords = {'N_iter': 'N_ITER', 'Trust_rad': 'TRUST_RAD', 'Dm_conv_max': 'DM_CONV_MAX', 'Dm_conv_int': 'DM_CONV_INT', 'Beta_dm_conv_max': 'BETA_DM_CONV_MAX', 'Beta_dm_conv_int': 'BETA_DM_CONV_INT', 'Read_dmfet_pot': 'READ_DMFET_POT', 'Dmfet_restart_file_name': 'DMFET_RESTART_FILE_NAME'}

