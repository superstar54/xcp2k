from xcp2k.inputsection import InputSection
from xcp2k.classes._thermostat_info2 import _thermostat_info2
from xcp2k.classes._temperature2 import _temperature2
from xcp2k.classes._energy3 import _energy3


class _print8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.THERMOSTAT_INFO = _thermostat_info2()
        self.TEMPERATURE = _temperature2()
        self.ENERGY = _energy3()
        self._name = "PRINT"
        self._subsections = {'THERMOSTAT_INFO': 'THERMOSTAT_INFO', 'TEMPERATURE': 'TEMPERATURE', 'ENERGY': 'ENERGY'}

