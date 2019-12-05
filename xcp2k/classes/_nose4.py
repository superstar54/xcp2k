from xcp2k.inputsection import InputSection
from xcp2k.classes._coord4 import _coord4
from xcp2k.classes._velocity5 import _velocity5
from xcp2k.classes._mass8 import _mass8
from xcp2k.classes._force4 import _force4


class _nose4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord4()
        self.VELOCITY = _velocity5()
        self.MASS = _mass8()
        self.FORCE = _force4()
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
