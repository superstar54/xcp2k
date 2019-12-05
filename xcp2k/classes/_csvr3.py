from xcp2k.inputsection import InputSection
from xcp2k.classes._thermostat_energy5 import _thermostat_energy5
from xcp2k.classes._rng_init5 import _rng_init5


class _csvr3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Timecon = None
        self.THERMOSTAT_ENERGY = _thermostat_energy5()
        self.RNG_INIT = _rng_init5()
        self._name = "CSVR"
        self._keywords = {'Timecon': 'TIMECON'}
        self._subsections = {'THERMOSTAT_ENERGY': 'THERMOSTAT_ENERGY', 'RNG_INIT': 'RNG_INIT'}

