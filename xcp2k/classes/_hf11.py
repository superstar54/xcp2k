from xcp2k.inputsection import InputSection
from _hf_info11 import _hf_info11
from _periodic17 import _periodic17
from _screening12 import _screening12
from _interaction_potential16 import _interaction_potential16
from _load_balance11 import _load_balance11
from _memory12 import _memory12


class _hf11(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info11()
        self.PERIODIC = _periodic17()
        self.SCREENING = _screening12()
        self.INTERACTION_POTENTIAL = _interaction_potential16()
        self.LOAD_BALANCE = _load_balance11()
        self.MEMORY = _memory12()
        self._name = "HF"
        self._keywords = {'Pw_hfx': 'PW_HFX', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Fraction': 'FRACTION', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'MEMORY': 'MEMORY', 'LOAD_BALANCE': 'LOAD_BALANCE', 'HF_INFO': 'HF_INFO'}

