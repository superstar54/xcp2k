from xcp2k.inputsection import InputSection
from _rng_init10 import _rng_init10


class _qtb1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Tau = None
        self.Lambda = None
        self.Fp = None
        self.Taucut = None
        self.Lambcut = None
        self.Nf = None
        self.RNG_INIT = _rng_init10()
        self._name = "QTB"
        self._keywords = {'Fp': 'FP', 'Tau': 'TAU', 'Nf': 'NF', 'Lambcut': 'LAMBCUT', 'Taucut': 'TAUCUT', 'Lambda': 'LAMBDA'}
        self._subsections = {'RNG_INIT': 'RNG_INIT'}

