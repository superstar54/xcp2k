from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info27 import _program_run_info27
from xcp2k.classes._wannier_cubes4 import _wannier_cubes4
from xcp2k.classes._wannier_centers4 import _wannier_centers4
from xcp2k.classes._wannier_spreads4 import _wannier_spreads4
from xcp2k.classes._loc_restart4 import _loc_restart4
from xcp2k.classes._total_dipole3 import _total_dipole3
from xcp2k.classes._molecular_dipoles3 import _molecular_dipoles3
from xcp2k.classes._molecular_states3 import _molecular_states3
from xcp2k.classes._wannier_states3 import _wannier_states3


class _print41(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info27()
        self.WANNIER_CUBES = _wannier_cubes4()
        self.WANNIER_CENTERS = _wannier_centers4()
        self.WANNIER_SPREADS = _wannier_spreads4()
        self.LOC_RESTART = _loc_restart4()
        self.TOTAL_DIPOLE = _total_dipole3()
        self.MOLECULAR_DIPOLES = _molecular_dipoles3()
        self.MOLECULAR_STATES = _molecular_states3()
        self.WANNIER_STATES = _wannier_states3()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

