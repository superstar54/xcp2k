from xcp2k.inputsection import InputSection


class _kpoints1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Scheme = None
        self.Kpoint = []
        self.Units = None
        self.Symmetry = None
        self.Full_grid = None
        self.Verbose = None
        self.Eps_geo = None
        self.Parallel_group_size = None
        self.Wavefunctions = None
        self._name = "KPOINTS"
        self._keywords = {'Scheme': 'SCHEME', 'Units': 'UNITS', 'Symmetry': 'SYMMETRY', 'Full_grid': 'FULL_GRID', 'Verbose': 'VERBOSE', 'Eps_geo': 'EPS_GEO', 'Parallel_group_size': 'PARALLEL_GROUP_SIZE', 'Wavefunctions': 'WAVEFUNCTIONS'}
        self._repeated_keywords = {'Kpoint': 'KPOINT'}

