from xcp2k.inputsection import InputSection
from xcp2k.classes._ot4 import _ot4
from xcp2k.classes._krylov2 import _krylov2
from xcp2k.classes._diag_sub_scf3 import _diag_sub_scf3
from xcp2k.classes._davidson3 import _davidson3
from xcp2k.classes._filter_matrix3 import _filter_matrix3


class _diagonalization2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Algorithm = None
        self.Jacobi_threshold = None
        self.Eps_jacobi = None
        self.Eps_adapt = None
        self.Max_iter = None
        self.Eps_iter = None
        self.OT = _ot4()
        self.KRYLOV = _krylov2()
        self.DIAG_SUB_SCF = _diag_sub_scf3()
        self.DAVIDSON = _davidson3()
        self.FILTER_MATRIX = _filter_matrix3()
        self._name = "DIAGONALIZATION"
        self._keywords = {'Algorithm': 'ALGORITHM', 'Jacobi_threshold': 'JACOBI_THRESHOLD', 'Eps_jacobi': 'EPS_JACOBI', 'Eps_adapt': 'EPS_ADAPT', 'Max_iter': 'MAX_ITER', 'Eps_iter': 'EPS_ITER'}
        self._subsections = {'OT': 'OT', 'KRYLOV': 'KRYLOV', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF', 'DAVIDSON': 'DAVIDSON', 'FILTER_MATRIX': 'FILTER_MATRIX'}
        self._attributes = ['Section_parameters']

