from xcp2k.inputsection import InputSection
from _restart8 import _restart8
from _restart_history3 import _restart_history3
from _iteration_info2 import _iteration_info2
from _program_run_info22 import _program_run_info22
from _mo_orthonormality2 import _mo_orthonormality2
from _mo_magnitude2 import _mo_magnitude2
from _detailed_energy2 import _detailed_energy2
from _diis_info3 import _diis_info3
from _total_densities2 import _total_densities2
from _lanczos2 import _lanczos2
from _diag_sub_scf4 import _diag_sub_scf4
from _davidson4 import _davidson4
from _filter_matrix4 import _filter_matrix4
from _mos_molden2 import _mos_molden2


class _print36(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dm_restart_write = None
        self.RESTART = _restart8()
        self.RESTART_HISTORY = _restart_history3()
        self.ITERATION_INFO = _iteration_info2()
        self.PROGRAM_RUN_INFO = _program_run_info22()
        self.MO_ORTHONORMALITY = _mo_orthonormality2()
        self.MO_MAGNITUDE = _mo_magnitude2()
        self.DETAILED_ENERGY = _detailed_energy2()
        self.DIIS_INFO = _diis_info3()
        self.TOTAL_DENSITIES = _total_densities2()
        self.LANCZOS = _lanczos2()
        self.DIAG_SUB_SCF = _diag_sub_scf4()
        self.DAVIDSON = _davidson4()
        self.FILTER_MATRIX = _filter_matrix4()
        self.MOS_MOLDEN = _mos_molden2()
        self._name = "PRINT"
        self._keywords = {'Dm_restart_write': 'DM_RESTART_WRITE'}
        self._subsections = {'DIIS_INFO': 'DIIS_INFO', 'RESTART_HISTORY': 'RESTART_HISTORY', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'MO_ORTHONORMALITY': 'MO_ORTHONORMALITY', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'TOTAL_DENSITIES': 'TOTAL_DENSITIES', 'FILTER_MATRIX': 'FILTER_MATRIX', 'DAVIDSON': 'DAVIDSON', 'LANCZOS': 'LANCZOS', 'ITERATION_INFO': 'ITERATION_INFO', 'MO_MAGNITUDE': 'MO_MAGNITUDE', 'MOS_MOLDEN': 'MOS_MOLDEN', 'RESTART': 'RESTART', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF'}

