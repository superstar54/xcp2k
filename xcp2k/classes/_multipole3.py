from xcp2k.inputsection import InputSection
from xcp2k.classes._interpolator5 import _interpolator5
from xcp2k.classes._check_spline3 import _check_spline3
from xcp2k.classes._program_run_info31 import _program_run_info31


class _multipole3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Rcut = None
        self.Ewald_precision = None
        self.Analytical_gterm = None
        self.Ngrids = None
        self.INTERPOLATOR = _interpolator5()
        self.CHECK_SPLINE = _check_spline3()
        self.PROGRAM_RUN_INFO = _program_run_info31()
        self._name = "MULTIPOLE"
        self._keywords = {'Rcut': 'RCUT', 'Ewald_precision': 'EWALD_PRECISION', 'Analytical_gterm': 'ANALYTICAL_GTERM', 'Ngrids': 'NGRIDS'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'CHECK_SPLINE': 'CHECK_SPLINE', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}
        self._attributes = ['Section_parameters']

