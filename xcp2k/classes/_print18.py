from xcp2k.inputsection import InputSection
from _restart6 import _restart6
from _restart_history2 import _restart_history2
from _iteration_info1 import _iteration_info1
from _program_run_info12 import _program_run_info12
from _mo_orthonormality1 import _mo_orthonormality1
from _mo_magnitude1 import _mo_magnitude1
from _detailed_energy1 import _detailed_energy1
from _diis_info2 import _diis_info2
from _total_densities1 import _total_densities1
from _lanczos1 import _lanczos1
from _diag_sub_scf2 import _diag_sub_scf2
from _davidson2 import _davidson2
from _filter_matrix2 import _filter_matrix2


class _print18(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.RESTART = _restart6()
        self.RESTART_HISTORY = _restart_history2()
        self.ITERATION_INFO = _iteration_info1()
        self.PROGRAM_RUN_INFO = _program_run_info12()
        self.MO_ORTHONORMALITY = _mo_orthonormality1()
        self.MO_MAGNITUDE = _mo_magnitude1()
        self.DETAILED_ENERGY = _detailed_energy1()
        self.DIIS_INFO = _diis_info2()
        self.TOTAL_DENSITIES = _total_densities1()
        self.LANCZOS = _lanczos1()
        self.DIAG_SUB_SCF = _diag_sub_scf2()
        self.DAVIDSON = _davidson2()
        self.FILTER_MATRIX = _filter_matrix2()
        self._name = "PRINT"
        self._subsections = {'DIIS_INFO': 'DIIS_INFO', 'RESTART_HISTORY': 'RESTART_HISTORY', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'MO_ORTHONORMALITY': 'MO_ORTHONORMALITY', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'TOTAL_DENSITIES': 'TOTAL_DENSITIES', 'FILTER_MATRIX': 'FILTER_MATRIX', 'DAVIDSON': 'DAVIDSON', 'LANCZOS': 'LANCZOS', 'ITERATION_INFO': 'ITERATION_INFO', 'MO_MAGNITUDE': 'MO_MAGNITUDE', 'RESTART': 'RESTART', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF'}

