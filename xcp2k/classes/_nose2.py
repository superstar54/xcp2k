from xcp2k.inputsection import InputSection
from xcp2k.classes._coord2 import _coord2
from xcp2k.classes._velocity3 import _velocity3
from xcp2k.classes._mass4 import _mass4
from xcp2k.classes._force2 import _force2


class _nose2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord2()
        self.VELOCITY = _velocity3()
        self.MASS = _mass4()
        self.FORCE = _force2()
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
