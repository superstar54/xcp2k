from xcp2k.inputsection import InputSection
from xcp2k.classes._coord1 import _coord1
from xcp2k.classes._velocity2 import _velocity2
from xcp2k.classes._mass2 import _mass2
from xcp2k.classes._force1 import _force1


class _nose1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord1()
        self.VELOCITY = _velocity2()
        self.MASS = _mass2()
        self.FORCE = _force1()
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
