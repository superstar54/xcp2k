from xcp2k.inputsection import InputSection
from _temp_control1 import _temp_control1
from _vel_control1 import _vel_control1


class _md2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_steps = None
        self.Timestep = None
        self.Temperature = None
        self.TEMP_CONTROL = _temp_control1()
        self.VEL_CONTROL = _vel_control1()
        self._name = "MD"
        self._keywords = {'Timestep': 'TIMESTEP', 'Max_steps': 'MAX_STEPS', 'Temperature': 'TEMPERATURE'}
        self._subsections = {'TEMP_CONTROL': 'TEMP_CONTROL', 'VEL_CONTROL': 'VEL_CONTROL'}

