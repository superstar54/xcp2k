from xcp2k.inputsection import InputSection


class _kpoints1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Scheme = None
        self.Kpoint = []
        self.Symmetry = None
        self.Full_grid = None
        self.Verbose = None
        self.Eps_geo = None
        self.Parallel_group_size = None
        self.Wavefunctions = None
        self._name = "KPOINTS"
        self._keywords = {'Wavefunctions': 'WAVEFUNCTIONS', 'Verbose': 'VERBOSE', 'Symmetry': 'SYMMETRY', 'Full_grid': 'FULL_GRID', 'Eps_geo': 'EPS_GEO', 'Scheme': 'SCHEME', 'Parallel_group_size': 'PARALLEL_GROUP_SIZE'}
        self._repeated_keywords = {'Kpoint': 'KPOINT'}

