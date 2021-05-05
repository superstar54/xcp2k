from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info56 import _program_run_info56
from xcp2k.classes._wannier_cubes16 import _wannier_cubes16
from xcp2k.classes._wannier_centers16 import _wannier_centers16
from xcp2k.classes._wannier_spreads16 import _wannier_spreads16
from xcp2k.classes._loc_restart16 import _loc_restart16
from xcp2k.classes._total_dipole15 import _total_dipole15
from xcp2k.classes._molecular_dipoles15 import _molecular_dipoles15
from xcp2k.classes._molecular_moments15 import _molecular_moments15
from xcp2k.classes._molecular_states15 import _molecular_states15
from xcp2k.classes._wannier_states15 import _wannier_states15


class _print87(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info56()
        self.WANNIER_CUBES = _wannier_cubes16()
        self.WANNIER_CENTERS = _wannier_centers16()
        self.WANNIER_SPREADS = _wannier_spreads16()
        self.LOC_RESTART = _loc_restart16()
        self.TOTAL_DIPOLE = _total_dipole15()
        self.MOLECULAR_DIPOLES = _molecular_dipoles15()
        self.MOLECULAR_MOMENTS = _molecular_moments15()
        self.MOLECULAR_STATES = _molecular_states15()
        self.WANNIER_STATES = _wannier_states15()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

