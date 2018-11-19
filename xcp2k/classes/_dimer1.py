from xcp2k.inputsection import InputSection
from _rot_opt1 import _rot_opt1
from _dimer_vector1 import _dimer_vector1


class _dimer1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dr = None
        self.Interpolate_gradient = None
        self.Angle_tolerance = None
        self.K_dimer = None
        self.Beta = None
        self.ROT_OPT = _rot_opt1()
        self.DIMER_VECTOR = _dimer_vector1()
        self._name = "DIMER"
        self._keywords = {'Interpolate_gradient': 'INTERPOLATE_GRADIENT', 'Beta': 'BETA', 'Dr': 'DR', 'K_dimer': 'K-DIMER', 'Angle_tolerance': 'ANGLE_TOLERANCE'}
        self._subsections = {'ROT_OPT': 'ROT_OPT', 'DIMER_VECTOR': 'DIMER_VECTOR'}

