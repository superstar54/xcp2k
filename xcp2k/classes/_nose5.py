from xcp2k.inputsection import InputSection
from xcp2k.classes._coord5 import _coord5
from xcp2k.classes._velocity6 import _velocity6
from xcp2k.classes._mass9 import _mass9
from xcp2k.classes._force5 import _force5


class _nose5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord5()
        self.VELOCITY = _velocity6()
        self.MASS = _mass9()
        self.FORCE = _force5()
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
