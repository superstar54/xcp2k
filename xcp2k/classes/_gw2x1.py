from xcp2k.inputsection import InputSection


class _gw2x1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Xps_only = None
        self.Batch_size = None
        self.Eps_gw2x = None
        self.C_os = None
        self.C_ss = None
        self.Max_gw2x_iter = None
        self.Pseudo_canonical = None
        self._name = "GW2X"
        self._keywords = {'Xps_only': 'XPS_ONLY', 'Batch_size': 'BATCH_SIZE', 'Eps_gw2x': 'EPS_GW2X', 'C_os': 'C_OS', 'C_ss': 'C_SS', 'Max_gw2x_iter': 'MAX_GW2X_ITER', 'Pseudo_canonical': 'PSEUDO_CANONICAL'}
        self._attributes = ['Section_parameters']

