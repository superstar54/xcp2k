from xcp2k.inputsection import InputSection
from xcp2k.classes._thermostat_energy7 import _thermostat_energy7
from xcp2k.classes._rng_init7 import _rng_init7
from xcp2k.classes._s4 import _s4


class _gle4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ndim = None
        self.A_scale = None
        self.A_list = []
        self.C_list = []
        self.THERMOSTAT_ENERGY = _thermostat_energy7()
        self.RNG_INIT = _rng_init7()
        self.S = _s4()
        self._name = "GLE"
        self._keywords = {'Ndim': 'NDIM', 'A_scale': 'A_SCALE'}
        self._repeated_keywords = {'A_list': 'A_LIST', 'C_list': 'C_LIST'}
        self._subsections = {'THERMOSTAT_ENERGY': 'THERMOSTAT_ENERGY', 'RNG_INIT': 'RNG_INIT', 'S': 'S'}

