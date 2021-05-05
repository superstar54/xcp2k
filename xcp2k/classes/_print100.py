from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info62 import _program_run_info62
from xcp2k.classes._wannier_cubes18 import _wannier_cubes18
from xcp2k.classes._wannier_centers18 import _wannier_centers18
from xcp2k.classes._wannier_spreads18 import _wannier_spreads18
from xcp2k.classes._loc_restart18 import _loc_restart18
from xcp2k.classes._total_dipole17 import _total_dipole17
from xcp2k.classes._molecular_dipoles17 import _molecular_dipoles17
from xcp2k.classes._molecular_moments17 import _molecular_moments17
from xcp2k.classes._molecular_states17 import _molecular_states17
from xcp2k.classes._wannier_states17 import _wannier_states17


class _print100(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info62()
        self.WANNIER_CUBES = _wannier_cubes18()
        self.WANNIER_CENTERS = _wannier_centers18()
        self.WANNIER_SPREADS = _wannier_spreads18()
        self.LOC_RESTART = _loc_restart18()
        self.TOTAL_DIPOLE = _total_dipole17()
        self.MOLECULAR_DIPOLES = _molecular_dipoles17()
        self.MOLECULAR_MOMENTS = _molecular_moments17()
        self.MOLECULAR_STATES = _molecular_states17()
        self.WANNIER_STATES = _wannier_states17()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

