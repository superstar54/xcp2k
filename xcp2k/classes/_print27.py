from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info16 import _program_run_info16
from xcp2k.classes._wannier_cubes2 import _wannier_cubes2
from xcp2k.classes._wannier_centers2 import _wannier_centers2
from xcp2k.classes._wannier_spreads2 import _wannier_spreads2
from xcp2k.classes._loc_restart2 import _loc_restart2
from xcp2k.classes._total_dipole2 import _total_dipole2
from xcp2k.classes._molecular_dipoles2 import _molecular_dipoles2
from xcp2k.classes._molecular_moments2 import _molecular_moments2
from xcp2k.classes._molecular_states2 import _molecular_states2
from xcp2k.classes._wannier_states2 import _wannier_states2


class _print27(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info16()
        self.WANNIER_CUBES = _wannier_cubes2()
        self.WANNIER_CENTERS = _wannier_centers2()
        self.WANNIER_SPREADS = _wannier_spreads2()
        self.LOC_RESTART = _loc_restart2()
        self.TOTAL_DIPOLE = _total_dipole2()
        self.MOLECULAR_DIPOLES = _molecular_dipoles2()
        self.MOLECULAR_MOMENTS = _molecular_moments2()
        self.MOLECULAR_STATES = _molecular_states2()
        self.WANNIER_STATES = _wannier_states2()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

