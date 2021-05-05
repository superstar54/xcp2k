from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info21 import _program_run_info21
from xcp2k.classes._wannier_cubes5 import _wannier_cubes5
from xcp2k.classes._wannier_centers5 import _wannier_centers5
from xcp2k.classes._wannier_spreads5 import _wannier_spreads5
from xcp2k.classes._loc_restart5 import _loc_restart5
from xcp2k.classes._total_dipole5 import _total_dipole5
from xcp2k.classes._molecular_dipoles5 import _molecular_dipoles5
from xcp2k.classes._molecular_moments5 import _molecular_moments5
from xcp2k.classes._molecular_states5 import _molecular_states5
from xcp2k.classes._wannier_states5 import _wannier_states5


class _print37(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info21()
        self.WANNIER_CUBES = _wannier_cubes5()
        self.WANNIER_CENTERS = _wannier_centers5()
        self.WANNIER_SPREADS = _wannier_spreads5()
        self.LOC_RESTART = _loc_restart5()
        self.TOTAL_DIPOLE = _total_dipole5()
        self.MOLECULAR_DIPOLES = _molecular_dipoles5()
        self.MOLECULAR_MOMENTS = _molecular_moments5()
        self.MOLECULAR_STATES = _molecular_states5()
        self.WANNIER_STATES = _wannier_states5()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

