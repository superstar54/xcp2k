from xcp2k.inputsection import InputSection
from xcp2k.classes._restart8 import _restart8
from xcp2k.classes._restart_history3 import _restart_history3
from xcp2k.classes._iteration_info2 import _iteration_info2
from xcp2k.classes._program_run_info29 import _program_run_info29
from xcp2k.classes._mo_orthonormality2 import _mo_orthonormality2
from xcp2k.classes._mo_magnitude2 import _mo_magnitude2
from xcp2k.classes._detailed_energy2 import _detailed_energy2
from xcp2k.classes._diis_info3 import _diis_info3
from xcp2k.classes._total_densities2 import _total_densities2
from xcp2k.classes._lanczos2 import _lanczos2
from xcp2k.classes._diag_sub_scf4 import _diag_sub_scf4
from xcp2k.classes._davidson4 import _davidson4
from xcp2k.classes._filter_matrix4 import _filter_matrix4


class _print48(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dm_restart_write = None
        self.RESTART = _restart8()
        self.RESTART_HISTORY = _restart_history3()
        self.ITERATION_INFO = _iteration_info2()
        self.PROGRAM_RUN_INFO = _program_run_info29()
        self.MO_ORTHONORMALITY = _mo_orthonormality2()
        self.MO_MAGNITUDE = _mo_magnitude2()
        self.DETAILED_ENERGY = _detailed_energy2()
        self.DIIS_INFO = _diis_info3()
        self.TOTAL_DENSITIES = _total_densities2()
        self.LANCZOS = _lanczos2()
        self.DIAG_SUB_SCF = _diag_sub_scf4()
        self.DAVIDSON = _davidson4()
        self.FILTER_MATRIX = _filter_matrix4()
        self._name = "PRINT"
        self._keywords = {'Dm_restart_write': 'DM_RESTART_WRITE'}
        self._subsections = {'RESTART': 'RESTART', 'RESTART_HISTORY': 'RESTART_HISTORY', 'ITERATION_INFO': 'ITERATION_INFO', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'MO_ORTHONORMALITY': 'MO_ORTHONORMALITY', 'MO_MAGNITUDE': 'MO_MAGNITUDE', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'DIIS_INFO': 'DIIS_INFO', 'TOTAL_DENSITIES': 'TOTAL_DENSITIES', 'LANCZOS': 'LANCZOS', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF', 'DAVIDSON': 'DAVIDSON', 'FILTER_MATRIX': 'FILTER_MATRIX'}

