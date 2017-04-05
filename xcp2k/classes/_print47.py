from xcp2k.inputsection import InputSection
from _program_run_info36 import _program_run_info36
from _wannier_cubes4 import _wannier_cubes4
from _wannier_centers4 import _wannier_centers4
from _wannier_spreads4 import _wannier_spreads4
from _loc_restart4 import _loc_restart4
from _total_dipole3 import _total_dipole3
from _molecular_dipoles3 import _molecular_dipoles3
from _molecular_states3 import _molecular_states3
from _wannier_states3 import _wannier_states3


class _print47(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info36()
        self.WANNIER_CUBES = _wannier_cubes4()
        self.WANNIER_CENTERS = _wannier_centers4()
        self.WANNIER_SPREADS = _wannier_spreads4()
        self.LOC_RESTART = _loc_restart4()
        self.TOTAL_DIPOLE = _total_dipole3()
        self.MOLECULAR_DIPOLES = _molecular_dipoles3()
        self.MOLECULAR_STATES = _molecular_states3()
        self.WANNIER_STATES = _wannier_states3()
        self._name = "PRINT"
        self._subsections = {'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'LOC_RESTART': 'LOC_RESTART', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'WANNIER_STATES': 'WANNIER_STATES', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'MOLECULAR_STATES': 'MOLECULAR_STATES'}

