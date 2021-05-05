from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info22 import _program_run_info22
from xcp2k.classes._wannier_cubes6 import _wannier_cubes6
from xcp2k.classes._wannier_centers6 import _wannier_centers6
from xcp2k.classes._wannier_spreads6 import _wannier_spreads6
from xcp2k.classes._loc_restart6 import _loc_restart6
from xcp2k.classes._total_dipole6 import _total_dipole6
from xcp2k.classes._molecular_dipoles6 import _molecular_dipoles6
from xcp2k.classes._molecular_moments6 import _molecular_moments6
from xcp2k.classes._molecular_states6 import _molecular_states6
from xcp2k.classes._wannier_states6 import _wannier_states6


class _print39(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info22()
        self.WANNIER_CUBES = _wannier_cubes6()
        self.WANNIER_CENTERS = _wannier_centers6()
        self.WANNIER_SPREADS = _wannier_spreads6()
        self.LOC_RESTART = _loc_restart6()
        self.TOTAL_DIPOLE = _total_dipole6()
        self.MOLECULAR_DIPOLES = _molecular_dipoles6()
        self.MOLECULAR_MOMENTS = _molecular_moments6()
        self.MOLECULAR_STATES = _molecular_states6()
        self.WANNIER_STATES = _wannier_states6()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

