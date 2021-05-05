from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info32 import _program_run_info32
from xcp2k.classes._wannier_cubes11 import _wannier_cubes11
from xcp2k.classes._wannier_centers11 import _wannier_centers11
from xcp2k.classes._wannier_spreads11 import _wannier_spreads11
from xcp2k.classes._loc_restart11 import _loc_restart11
from xcp2k.classes._total_dipole10 import _total_dipole10
from xcp2k.classes._molecular_dipoles10 import _molecular_dipoles10
from xcp2k.classes._molecular_moments10 import _molecular_moments10
from xcp2k.classes._molecular_states10 import _molecular_states10
from xcp2k.classes._wannier_states10 import _wannier_states10


class _print52(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info32()
        self.WANNIER_CUBES = _wannier_cubes11()
        self.WANNIER_CENTERS = _wannier_centers11()
        self.WANNIER_SPREADS = _wannier_spreads11()
        self.LOC_RESTART = _loc_restart11()
        self.TOTAL_DIPOLE = _total_dipole10()
        self.MOLECULAR_DIPOLES = _molecular_dipoles10()
        self.MOLECULAR_MOMENTS = _molecular_moments10()
        self.MOLECULAR_STATES = _molecular_states10()
        self.WANNIER_STATES = _wannier_states10()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

