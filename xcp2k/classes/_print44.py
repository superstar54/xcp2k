from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info24 import _program_run_info24
from xcp2k.classes._wannier_cubes8 import _wannier_cubes8
from xcp2k.classes._wannier_centers8 import _wannier_centers8
from xcp2k.classes._wannier_spreads8 import _wannier_spreads8
from xcp2k.classes._loc_restart8 import _loc_restart8
from xcp2k.classes._total_dipole8 import _total_dipole8
from xcp2k.classes._molecular_dipoles8 import _molecular_dipoles8
from xcp2k.classes._molecular_moments8 import _molecular_moments8
from xcp2k.classes._molecular_states8 import _molecular_states8
from xcp2k.classes._wannier_states8 import _wannier_states8


class _print44(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info24()
        self.WANNIER_CUBES = _wannier_cubes8()
        self.WANNIER_CENTERS = _wannier_centers8()
        self.WANNIER_SPREADS = _wannier_spreads8()
        self.LOC_RESTART = _loc_restart8()
        self.TOTAL_DIPOLE = _total_dipole8()
        self.MOLECULAR_DIPOLES = _molecular_dipoles8()
        self.MOLECULAR_MOMENTS = _molecular_moments8()
        self.MOLECULAR_STATES = _molecular_states8()
        self.WANNIER_STATES = _wannier_states8()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

