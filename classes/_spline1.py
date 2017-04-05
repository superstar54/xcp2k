from xcp2k.inputsection import InputSection


class _spline1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.R0_nb = None
        self.Rcut_nb = None
        self.Emax_spline = None
        self.Emax_accuracy = None
        self.Eps_spline = None
        self.Npoints = None
        self.Unique_spline = None
        self._name = "SPLINE"
        self._keywords = {'Eps_spline': 'EPS_SPLINE', 'Rcut_nb': 'RCUT_NB', 'Emax_spline': 'EMAX_SPLINE', 'Emax_accuracy': 'EMAX_ACCURACY', 'Npoints': 'NPOINTS', 'R0_nb': 'R0_NB', 'Unique_spline': 'UNIQUE_SPLINE'}

