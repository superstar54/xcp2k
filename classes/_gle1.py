from xcp2k.inputsection import InputSection
from _thermostat_energy2 import _thermostat_energy2
from _rng_init2 import _rng_init2
from _s1 import _s1


class _gle1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ndim = None
        self.A_scale = None
        self.A_list = []
        self.C_list = []
        self.THERMOSTAT_ENERGY = _thermostat_energy2()
        self.RNG_INIT = _rng_init2()
        self.S = _s1()
        self._name = "GLE"
        self._keywords = {'Ndim': 'NDIM', 'A_scale': 'A_SCALE'}
        self._repeated_keywords = {'A_list': 'A_LIST', 'C_list': 'C_LIST'}
        self._subsections = {'S': 'S', 'THERMOSTAT_ENERGY': 'THERMOSTAT_ENERGY', 'RNG_INIT': 'RNG_INIT'}

