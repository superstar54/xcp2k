from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info57 import _program_run_info57
from xcp2k.classes._wannier_cubes17 import _wannier_cubes17
from xcp2k.classes._wannier_centers17 import _wannier_centers17
from xcp2k.classes._wannier_spreads17 import _wannier_spreads17
from xcp2k.classes._loc_restart17 import _loc_restart17
from xcp2k.classes._total_dipole16 import _total_dipole16
from xcp2k.classes._molecular_dipoles16 import _molecular_dipoles16
from xcp2k.classes._molecular_moments16 import _molecular_moments16
from xcp2k.classes._molecular_states16 import _molecular_states16
from xcp2k.classes._wannier_states16 import _wannier_states16


class _print89(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info57()
        self.WANNIER_CUBES = _wannier_cubes17()
        self.WANNIER_CENTERS = _wannier_centers17()
        self.WANNIER_SPREADS = _wannier_spreads17()
        self.LOC_RESTART = _loc_restart17()
        self.TOTAL_DIPOLE = _total_dipole16()
        self.MOLECULAR_DIPOLES = _molecular_dipoles16()
        self.MOLECULAR_MOMENTS = _molecular_moments16()
        self.MOLECULAR_STATES = _molecular_states16()
        self.WANNIER_STATES = _wannier_states16()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

