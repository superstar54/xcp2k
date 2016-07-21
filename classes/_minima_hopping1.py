from xcp2k.inputsection import InputSection


class _minima_hopping1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Beta_1 = None
        self.Beta_2 = None
        self.Beta_3 = None
        self.Alpha_1 = None
        self.Alpha_2 = None
        self.E_accept_init = None
        self.Temperature_init = None
        self.Share_history = None
        self._name = "MINIMA_HOPPING"
        self._keywords = {'Beta_1': 'BETA_1', 'Beta_3': 'BETA_3', 'Beta_2': 'BETA_2', 'Share_history': 'SHARE_HISTORY', 'Temperature_init': 'TEMPERATURE_INIT', 'Alpha_2': 'ALPHA_2', 'Alpha_1': 'ALPHA_1', 'E_accept_init': 'E_ACCEPT_INIT'}

