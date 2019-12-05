from xcp2k.inputsection import InputSection
from xcp2k.classes._run_info1 import _run_info1
from xcp2k.classes._atom_info1 import _atom_info1
from xcp2k.classes._fock_gap1 import _fock_gap1
from xcp2k.classes._fock_eigenvalues1 import _fock_eigenvalues1
from xcp2k.classes._ml_variance1 import _ml_variance1
from xcp2k.classes._ml_training_data1 import _ml_training_data1
from xcp2k.classes._opt_info1 import _opt_info1
from xcp2k.classes._restart7 import _restart7


class _print21(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.RUN_INFO = _run_info1()
        self.ATOM_INFO = _atom_info1()
        self.FOCK_GAP = _fock_gap1()
        self.FOCK_EIGENVALUES = _fock_eigenvalues1()
        self.ML_VARIANCE = _ml_variance1()
        self.ML_TRAINING_DATA = _ml_training_data1()
        self.OPT_INFO = _opt_info1()
        self.RESTART = _restart7()
        self._name = "PRINT"
        self._subsections = {'RUN_INFO': 'RUN_INFO', 'ATOM_INFO': 'ATOM_INFO', 'FOCK_GAP': 'FOCK_GAP', 'FOCK_EIGENVALUES': 'FOCK_EIGENVALUES', 'ML_VARIANCE': 'ML_VARIANCE', 'ML_TRAINING_DATA': 'ML_TRAINING_DATA', 'OPT_INFO': 'OPT_INFO', 'RESTART': 'RESTART'}

