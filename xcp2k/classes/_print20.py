from xcp2k.inputsection import InputSection
from xcp2k.classes._restart6 import _restart6
from xcp2k.classes._restart_history2 import _restart_history2
from xcp2k.classes._iteration_info1 import _iteration_info1
from xcp2k.classes._program_run_info14 import _program_run_info14
from xcp2k.classes._mo_orthonormality1 import _mo_orthonormality1
from xcp2k.classes._mo_magnitude1 import _mo_magnitude1
from xcp2k.classes._detailed_energy1 import _detailed_energy1
from xcp2k.classes._diis_info2 import _diis_info2
from xcp2k.classes._total_densities1 import _total_densities1
from xcp2k.classes._lanczos1 import _lanczos1
from xcp2k.classes._diag_sub_scf2 import _diag_sub_scf2
from xcp2k.classes._davidson2 import _davidson2
from xcp2k.classes._filter_matrix2 import _filter_matrix2


class _print20(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dm_restart_write = None
        self.RESTART = _restart6()
        self.RESTART_HISTORY = _restart_history2()
        self.ITERATION_INFO = _iteration_info1()
        self.PROGRAM_RUN_INFO = _program_run_info14()
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
        self._keywords = {'Dm_restart_write': 'DM_RESTART_WRITE'}
        self._subsections = {'RESTART': 'RESTART', 'RESTART_HISTORY': 'RESTART_HISTORY', 'ITERATION_INFO': 'ITERATION_INFO', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'MO_ORTHONORMALITY': 'MO_ORTHONORMALITY', 'MO_MAGNITUDE': 'MO_MAGNITUDE', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'DIIS_INFO': 'DIIS_INFO', 'TOTAL_DENSITIES': 'TOTAL_DENSITIES', 'LANCZOS': 'LANCZOS', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF', 'DAVIDSON': 'DAVIDSON', 'FILTER_MATRIX': 'FILTER_MATRIX'}

