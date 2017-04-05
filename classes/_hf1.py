from xcp2k.inputsection import InputSection
from _hf_info1 import _hf_info1
from _periodic1 import _periodic1
from _screening2 import _screening2
from _interaction_potential1 import _interaction_potential1
from _load_balance1 import _load_balance1
from _memory2 import _memory2


class _hf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info1()
        self.PERIODIC = _periodic1()
        self.SCREENING = _screening2()
        self.INTERACTION_POTENTIAL = _interaction_potential1()
        self.LOAD_BALANCE = _load_balance1()
        self.MEMORY = _memory2()
        self._name = "HF"
        self._keywords = {'Pw_hfx': 'PW_HFX', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Fraction': 'FRACTION', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'MEMORY': 'MEMORY', 'LOAD_BALANCE': 'LOAD_BALANCE', 'HF_INFO': 'HF_INFO'}

