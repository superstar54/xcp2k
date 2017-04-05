from xcp2k.inputsection import InputSection


class _filter_matrix1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Filter_temperature = None
        self.Auto_cutoff_scale = None
        self.Eps_fb = None
        self.Collective_communication = None
        self._name = "FILTER_MATRIX"
        self._keywords = {'Collective_communication': 'COLLECTIVE_COMMUNICATION', 'Filter_temperature': 'FILTER_TEMPERATURE', 'Auto_cutoff_scale': 'AUTO_CUTOFF_SCALE', 'Eps_fb': 'EPS_FB'}

