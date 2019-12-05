from xcp2k.inputsection import InputSection
from xcp2k.classes._velocity1 import _velocity1
from xcp2k.classes._mass1 import _mass1
from xcp2k.classes._thermostat1 import _thermostat1
from xcp2k.classes._print7 import _print7


class _barostat1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pressure = None
        self.Timecon = None
        self.Temperature = None
        self.Temp_tol = None
        self.Virial = None
        self.VELOCITY = _velocity1()
        self.MASS = _mass1()
        self.THERMOSTAT = _thermostat1()
        self.PRINT = _print7()
        self._name = "BAROSTAT"
        self._keywords = {'Pressure': 'PRESSURE', 'Timecon': 'TIMECON', 'Temperature': 'TEMPERATURE', 'Temp_tol': 'TEMP_TOL', 'Virial': 'VIRIAL'}
        self._subsections = {'VELOCITY': 'VELOCITY', 'MASS': 'MASS', 'THERMOSTAT': 'THERMOSTAT', 'PRINT': 'PRINT'}

