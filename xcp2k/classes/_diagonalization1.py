from xcp2k.inputsection import InputSection
from _ot2 import _ot2
from _krylov1 import _krylov1
from _diag_sub_scf1 import _diag_sub_scf1
from _davidson1 import _davidson1
from _filter_matrix1 import _filter_matrix1


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
        self._keywords = {'Algorithm': 'ALGORITHM', 'Eps_jacobi': 'EPS_JACOBI', 'Max_iter': 'MAX_ITER', 'Jacobi_threshold': 'JACOBI_THRESHOLD', 'Eps_iter': 'EPS_ITER', 'Eps_adapt': 'EPS_ADAPT'}
        self._subsections = {'FILTER_MATRIX': 'FILTER_MATRIX', 'KRYLOV': 'KRYLOV', 'OT': 'OT', 'DAVIDSON': 'DAVIDSON', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF'}
        self._attributes = ['Section_parameters']

