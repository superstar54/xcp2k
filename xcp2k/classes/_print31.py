from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info17 import _program_run_info17
from xcp2k.classes._wannier_cubes3 import _wannier_cubes3
from xcp2k.classes._wannier_centers3 import _wannier_centers3
from xcp2k.classes._wannier_spreads3 import _wannier_spreads3
from xcp2k.classes._loc_restart3 import _loc_restart3
from xcp2k.classes._total_dipole3 import _total_dipole3
from xcp2k.classes._molecular_dipoles3 import _molecular_dipoles3
from xcp2k.classes._molecular_moments3 import _molecular_moments3
from xcp2k.classes._molecular_states3 import _molecular_states3
from xcp2k.classes._wannier_states3 import _wannier_states3


class _print31(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info17()
        self.WANNIER_CUBES = _wannier_cubes3()
        self.WANNIER_CENTERS = _wannier_centers3()
        self.WANNIER_SPREADS = _wannier_spreads3()
        self.LOC_RESTART = _loc_restart3()
        self.TOTAL_DIPOLE = _total_dipole3()
        self.MOLECULAR_DIPOLES = _molecular_dipoles3()
        self.MOLECULAR_MOMENTS = _molecular_moments3()
        self.MOLECULAR_STATES = _molecular_states3()
        self.WANNIER_STATES = _wannier_states3()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

