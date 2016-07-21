from xcp2k.inputsection import InputSection
from _program_run_info22 import _program_run_info22
from _wannier_cubes3 import _wannier_cubes3
from _wannier_centers3 import _wannier_centers3
from _wannier_spreads3 import _wannier_spreads3
from _loc_restart3 import _loc_restart3
from _total_dipole2 import _total_dipole2
from _molecular_dipoles2 import _molecular_dipoles2
from _molecular_states2 import _molecular_states2
from _wannier_states2 import _wannier_states2


class _print31(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info22()
        self.WANNIER_CUBES = _wannier_cubes3()
        self.WANNIER_CENTERS = _wannier_centers3()
        self.WANNIER_SPREADS = _wannier_spreads3()
        self.LOC_RESTART = _loc_restart3()
        self.TOTAL_DIPOLE = _total_dipole2()
        self.MOLECULAR_DIPOLES = _molecular_dipoles2()
        self.MOLECULAR_STATES = _molecular_states2()
        self.WANNIER_STATES = _wannier_states2()
        self._name = "PRINT"
        self._subsections = {'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'LOC_RESTART': 'LOC_RESTART', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'WANNIER_STATES': 'WANNIER_STATES', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'MOLECULAR_STATES': 'MOLECULAR_STATES'}

