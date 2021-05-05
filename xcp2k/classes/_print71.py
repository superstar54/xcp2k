from xcp2k.inputsection import InputSection
from xcp2k.classes._program_run_info47 import _program_run_info47
from xcp2k.classes._wannier_cubes13 import _wannier_cubes13
from xcp2k.classes._wannier_centers13 import _wannier_centers13
from xcp2k.classes._wannier_spreads13 import _wannier_spreads13
from xcp2k.classes._loc_restart13 import _loc_restart13
from xcp2k.classes._total_dipole12 import _total_dipole12
from xcp2k.classes._molecular_dipoles12 import _molecular_dipoles12
from xcp2k.classes._molecular_moments12 import _molecular_moments12
from xcp2k.classes._molecular_states12 import _molecular_states12
from xcp2k.classes._wannier_states12 import _wannier_states12


class _print71(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info47()
        self.WANNIER_CUBES = _wannier_cubes13()
        self.WANNIER_CENTERS = _wannier_centers13()
        self.WANNIER_SPREADS = _wannier_spreads13()
        self.LOC_RESTART = _loc_restart13()
        self.TOTAL_DIPOLE = _total_dipole12()
        self.MOLECULAR_DIPOLES = _molecular_dipoles12()
        self.MOLECULAR_MOMENTS = _molecular_moments12()
        self.MOLECULAR_STATES = _molecular_states12()
        self.WANNIER_STATES = _wannier_states12()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'LOC_RESTART': 'LOC_RESTART', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'MOLECULAR_MOMENTS': 'MOLECULAR_MOMENTS', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_STATES': 'WANNIER_STATES'}

