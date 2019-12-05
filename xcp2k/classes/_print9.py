from xcp2k.inputsection import InputSection
from xcp2k.classes._thermostat_info3 import _thermostat_info3
from xcp2k.classes._temperature3 import _temperature3
from xcp2k.classes._energy4 import _energy4


class _print9(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.THERMOSTAT_INFO = _thermostat_info3()
        self.TEMPERATURE = _temperature3()
        self.ENERGY = _energy4()
        self._name = "PRINT"
        self._subsections = {'THERMOSTAT_INFO': 'THERMOSTAT_INFO', 'TEMPERATURE': 'TEMPERATURE', 'ENERGY': 'ENERGY'}

