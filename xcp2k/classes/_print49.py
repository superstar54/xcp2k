from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info30 import _program_run_info30
from xcp2k.classes._wannier_cubes9 import _wannier_cubes9
from xcp2k.classes._wannier_centers9 import _wannier_centers9
from xcp2k.classes._wannier_spreads9 import _wannier_spreads9
from xcp2k.classes._loc_restart9 import _loc_restart9
from xcp2k.classes._total_dipole9 import _total_dipole9
from xcp2k.classes._molecular_dipoles9 import _molecular_dipoles9
from xcp2k.classes._molecular_moments9 import _molecular_moments9
from xcp2k.classes._molecular_states9 import _molecular_states9
from xcp2k.classes._wannier_states9 import _wannier_states9


class _print49(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info30()
        self.WANNIER_CUBES = _wannier_cubes9()
        self.WANNIER_CENTERS = _wannier_centers9()
        self.WANNIER_SPREADS = _wannier_spreads9()
        self.LOC_RESTART = _loc_restart9()
        self.TOTAL_DIPOLE = _total_dipole9()
        self.MOLECULAR_DIPOLES = _molecular_dipoles9()
        self.MOLECULAR_MOMENTS = _molecular_moments9()
        self.MOLECULAR_STATES = _molecular_states9()
        self.WANNIER_STATES = _wannier_states9()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

