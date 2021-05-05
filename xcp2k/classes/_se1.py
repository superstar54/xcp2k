from xcp2k.inputsection import InputSection
from xcp2k.classes._coulomb1 import _coulomb1
from xcp2k.classes._exchange1 import _exchange1
from xcp2k.classes._screening5 import _screening5
from xcp2k.classes._lr_correction1 import _lr_correction1
from xcp2k.classes._neighbor_lists2 import _neighbor_lists2
from xcp2k.classes._memory5 import _memory5
from xcp2k.classes._print35 import _print35
from xcp2k.classes._ga1 import _ga1


class _se1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Orthogonal_basis = None
        self.Sto_ng = None
        self.Analytical_gradients = None
        self.Delta = None
        self.Integral_screening = None
        self.Periodic = None
        self.Force_kdso_d_exchange = None
        self.Dispersion = None
        self.Dispersion_parameter_file = None
        self.Dispersion_radius = None
        self.Coordination_cutoff = None
        self.D3_scaling = None
        self.COULOMB = _coulomb1()
        self.EXCHANGE = _exchange1()
        self.SCREENING = _screening5()
        self.LR_CORRECTION = _lr_correction1()
        self.NEIGHBOR_LISTS = _neighbor_lists2()
        self.MEMORY = _memory5()
        self.PRINT = _print35()
        self.GA = _ga1()
        self._name = "SE"
        self._keywords = {'Orthogonal_basis': 'ORTHOGONAL_BASIS', 'Sto_ng': 'STO_NG', 'Analytical_gradients': 'ANALYTICAL_GRADIENTS', 'Delta': 'DELTA', 'Integral_screening': 'INTEGRAL_SCREENING', 'Periodic': 'PERIODIC', 'Force_kdso_d_exchange': 'FORCE_KDSO-D_EXCHANGE', 'Dispersion': 'DISPERSION', 'Dispersion_parameter_file': 'DISPERSION_PARAMETER_FILE', 'Dispersion_radius': 'DISPERSION_RADIUS', 'Coordination_cutoff': 'COORDINATION_CUTOFF', 'D3_scaling': 'D3_SCALING'}
        self._subsections = {'COULOMB': 'COULOMB', 'EXCHANGE': 'EXCHANGE', 'SCREENING': 'SCREENING', 'LR_CORRECTION': 'LR_CORRECTION', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'MEMORY': 'MEMORY', 'PRINT': 'PRINT', 'GA': 'GA'}

