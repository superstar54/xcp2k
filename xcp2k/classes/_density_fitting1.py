from xcp2k.inputsection import InputSection
from _program_run_info21 import _program_run_info21


class _density_fitting1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Num_gauss = None
        self.Pfactor = None
        self.Min_radius = None
        self.Radii = None
        self.Gcut = None
        self.PROGRAM_RUN_INFO = _program_run_info21()
        self._name = "DENSITY_FITTING"
        self._keywords = {'Radii': 'RADII', 'Num_gauss': 'NUM_GAUSS', 'Gcut': 'GCUT', 'Pfactor': 'PFACTOR', 'Min_radius': 'MIN_RADIUS'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

