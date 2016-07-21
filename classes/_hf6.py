from xcp2k.inputsection import InputSection
from _hf_info6 import _hf_info6
from _periodic7 import _periodic7
from _screening7 import _screening7
from _interaction_potential8 import _interaction_potential8
from _load_balance6 import _load_balance6
from _memory7 import _memory7


class _hf6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info6()
        self.PERIODIC = _periodic7()
        self.SCREENING = _screening7()
        self.INTERACTION_POTENTIAL = _interaction_potential8()
        self.LOAD_BALANCE = _load_balance6()
        self.MEMORY = _memory7()
        self._name = "HF"
        self._keywords = {'Pw_hfx': 'PW_HFX', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Fraction': 'FRACTION', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'MEMORY': 'MEMORY', 'LOAD_BALANCE': 'LOAD_BALANCE', 'HF_INFO': 'HF_INFO'}
