from xcp2k.inputsection import InputSection


class _xc_grid7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Xc_smooth_rho = None
        self.Xc_deriv = None
        self.Use_finer_grid = None
        self._name = "XC_GRID"
        self._keywords = {'Xc_smooth_rho': 'XC_SMOOTH_RHO', 'Xc_deriv': 'XC_DERIV', 'Use_finer_grid': 'USE_FINER_GRID'}

