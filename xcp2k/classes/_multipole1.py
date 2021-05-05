from xcp2k.inputsection import InputSection
from xcp2k.classes._interpolator2 import _interpolator2
from xcp2k.classes._check_spline1 import _check_spline1
from xcp2k.classes._program_run_info25 import _program_run_info25


class _multipole1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rcut = None
        self.Ewald_precision = None
        self.Analytical_gterm = None
        self.Ngrids = None
        self.INTERPOLATOR = _interpolator2()
        self.CHECK_SPLINE = _check_spline1()
        self.PROGRAM_RUN_INFO = _program_run_info25()
        self._name = "MULTIPOLE"
        self._keywords = {'Rcut': 'RCUT', 'Ewald_precision': 'EWALD_PRECISION', 'Analytical_gterm': 'ANALYTICAL_GTERM', 'Ngrids': 'NGRIDS'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'CHECK_SPLINE': 'CHECK_SPLINE', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

