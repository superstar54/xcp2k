from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info63 import _program_run_info63
from xcp2k.classes._wannier_cubes19 import _wannier_cubes19
from xcp2k.classes._wannier_centers19 import _wannier_centers19
from xcp2k.classes._wannier_spreads19 import _wannier_spreads19
from xcp2k.classes._loc_restart19 import _loc_restart19
from xcp2k.classes._total_dipole18 import _total_dipole18
from xcp2k.classes._molecular_dipoles18 import _molecular_dipoles18
from xcp2k.classes._molecular_moments18 import _molecular_moments18
from xcp2k.classes._molecular_states18 import _molecular_states18
from xcp2k.classes._wannier_states18 import _wannier_states18


class _print102(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info63()
        self.WANNIER_CUBES = _wannier_cubes19()
        self.WANNIER_CENTERS = _wannier_centers19()
        self.WANNIER_SPREADS = _wannier_spreads19()
        self.LOC_RESTART = _loc_restart19()
        self.TOTAL_DIPOLE = _total_dipole18()
        self.MOLECULAR_DIPOLES = _molecular_dipoles18()
        self.MOLECULAR_MOMENTS = _molecular_moments18()
        self.MOLECULAR_STATES = _molecular_states18()
        self.WANNIER_STATES = _wannier_states18()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

