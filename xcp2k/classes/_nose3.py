from xcp2k.inputsection import InputSection
from xcp2k.classes._coord3 import _coord3
from xcp2k.classes._velocity4 import _velocity4
from xcp2k.classes._mass6 import _mass6
from xcp2k.classes._force3 import _force3


class _nose3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord3()
        self.VELOCITY = _velocity4()
        self.MASS = _mass6()
        self.FORCE = _force3()
        self._name = "NOSE"
        self._keywords = {'Length': 'LENGTH', 'Yoshida': 'YOSHIDA', 'Timecon': 'TIMECON', 'Mts': 'MTS'}
        self._subsections = {'COORD': 'COORD', 'VELOCITY': 'VELOCITY', 'MASS': 'MASS', 'FORCE': 'FORCE'}
        self._aliases = {'Multiple_time_steps': 'Mts', 'Mult_t_steps': 'Mts'}


    @property
    def Multiple_time_steps(self):
        """
        See documentation for Mts
        """
        return self.Mts

    @property
    def Mult_t_steps(self):
        """
        See documentation for Mts
        """
        return self.Mts

    @Multiple_time_steps.setter
    def Multiple_time_steps(self, value):
        self.Mts = value

    @Mult_t_steps.setter
    def Mult_t_steps(self, value):
        self.Mts = value
