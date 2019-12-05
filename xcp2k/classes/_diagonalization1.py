from xcp2k.inputsection import InputSection
from xcp2k.classes._ot2 import _ot2
from xcp2k.classes._krylov1 import _krylov1
from xcp2k.classes._diag_sub_scf1 import _diag_sub_scf1
from xcp2k.classes._davidson1 import _davidson1
from xcp2k.classes._filter_matrix1 import _filter_matrix1


class _diagonalization1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Algorithm = None
        self.Jacobi_threshold = None
        self.Eps_jacobi = None
        self.Eps_adapt = None
        self.Max_iter = None
        self.Eps_iter = None
        self.OT = _ot2()
        self.KRYLOV = _krylov1()
        self.DIAG_SUB_SCF = _diag_sub_scf1()
        self.DAVIDSON = _davidson1()
        self.FILTER_MATRIX = _filter_matrix1()
        self._name = "DIAGONALIZATION"
        self._keywords = {'Algorithm': 'ALGORITHM', 'Jacobi_threshold': 'JACOBI_THRESHOLD', 'Eps_jacobi': 'EPS_JACOBI', 'Eps_adapt': 'EPS_ADAPT', 'Max_iter': 'MAX_ITER', 'Eps_iter': 'EPS_ITER'}
        self._subsections = {'OT': 'OT', 'KRYLOV': 'KRYLOV', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF', 'DAVIDSON': 'DAVIDSON', 'FILTER_MATRIX': 'FILTER_MATRIX'}
        self._attributes = ['Section_parameters']

