from xcp2k.inputsection import InputSection
from _hf_info12 import _hf_info12
from _periodic18 import _periodic18
from _screening13 import _screening13
from _interaction_potential17 import _interaction_potential17
from _load_balance12 import _load_balance12
from _memory13 import _memory13


class _hf12(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info12()
        self.PERIODIC = _periodic18()
        self.SCREENING = _screening13()
        self.INTERACTION_POTENTIAL = _interaction_potential17()
        self.LOAD_BALANCE = _load_balance12()
        self.MEMORY = _memory13()
        self._name = "HF"
        self._keywords = {'Pw_hfx': 'PW_HFX', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Fraction': 'FRACTION', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'MEMORY': 'MEMORY', 'LOAD_BALANCE': 'LOAD_BALANCE', 'HF_INFO': 'HF_INFO'}

