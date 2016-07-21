from xcp2k.inputsection import InputSection
from _thermostat_energy6 import _thermostat_energy6
from _rng_init6 import _rng_init6
from _s3 import _s3


class _gle3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ndim = None
        self.A_scale = None
        self.A_list = []
        self.C_list = []
        self.THERMOSTAT_ENERGY = _thermostat_energy6()
        self.RNG_INIT = _rng_init6()
        self.S = _s3()
        self._name = "GLE"
        self._keywords = {'Ndim': 'NDIM', 'A_scale': 'A_SCALE'}
        self._repeated_keywords = {'A_list': 'A_LIST', 'C_list': 'C_LIST'}
        self._subsections = {'S': 'S', 'THERMOSTAT_ENERGY': 'THERMOSTAT_ENERGY', 'RNG_INIT': 'RNG_INIT'}

