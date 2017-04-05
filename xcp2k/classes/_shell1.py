from xcp2k.inputsection import InputSection
from _thermostat3 import _thermostat3


class _shell1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Temperature = None
        self.Temp_tol = None
        self.Nose_particle = None
        self.Displacement_shell_tol = None
        self.THERMOSTAT = _thermostat3()
        self._name = "SHELL"
        self._keywords = {'Temp_tol': 'TEMP_TOL', 'Displacement_shell_tol': 'DISPLACEMENT_SHELL_TOL', 'Temperature': 'TEMPERATURE', 'Nose_particle': 'NOSE_PARTICLE'}
        self._subsections = {'THERMOSTAT': 'THERMOSTAT'}

