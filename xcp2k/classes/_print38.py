from xcp2k.inputsection import InputSection
from _wannier_cubes2 import _wannier_cubes2
from _wannier_centers2 import _wannier_centers2
from _wannier_spreads2 import _wannier_spreads2
from _loc_restart2 import _loc_restart2
from _iteration_info3 import _iteration_info3
from _program_run_info24 import _program_run_info24
from _xes_spectrum1 import _xes_spectrum1
from _xas_spectrum1 import _xas_spectrum1
from _pdos1 import _pdos1
from _restart9 import _restart9
from _cls_function_cubes1 import _cls_function_cubes1


class _print38(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.WANNIER_CUBES = _wannier_cubes2()
        self.WANNIER_CENTERS = _wannier_centers2()
        self.WANNIER_SPREADS = _wannier_spreads2()
        self.LOC_RESTART = _loc_restart2()
        self.ITERATION_INFO = _iteration_info3()
        self.PROGRAM_RUN_INFO = _program_run_info24()
        self.XES_SPECTRUM = _xes_spectrum1()
        self.XAS_SPECTRUM = _xas_spectrum1()
        self.PDOS = _pdos1()
        self.RESTART = _restart9()
        self.CLS_FUNCTION_CUBES = _cls_function_cubes1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'XAS_SPECTRUM': 'XAS_SPECTRUM', 'LOC_RESTART': 'LOC_RESTART', 'PDOS': 'PDOS', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'XES_SPECTRUM': 'XES_SPECTRUM', 'WANNIER_CUBES': 'WANNIER_CUBES', 'CLS_FUNCTION_CUBES': 'CLS_FUNCTION_CUBES', 'ITERATION_INFO': 'ITERATION_INFO', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'RESTART': 'RESTART'}

