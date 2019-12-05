from xcp2k.inputsection import InputSection


class _mom2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Mom_type = None
        self.Start_iter = None
        self.Deocc_alpha = None
        self.Deocc_beta = None
        self.Occ_alpha = None
        self.Occ_beta = None
        self.Proj_formula = None
        self._name = "MOM"
        self._keywords = {'Mom_type': 'MOM_TYPE', 'Start_iter': 'START_ITER', 'Deocc_alpha': 'DEOCC_ALPHA', 'Deocc_beta': 'DEOCC_BETA', 'Occ_alpha': 'OCC_ALPHA', 'Occ_beta': 'OCC_BETA', 'Proj_formula': 'PROJ_FORMULA'}
        self._attributes = ['Section_parameters']

