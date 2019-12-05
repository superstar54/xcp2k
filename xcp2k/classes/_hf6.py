from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info6 import _hf_info6
from xcp2k.classes._periodic8 import _periodic8
from xcp2k.classes._screening7 import _screening7
from xcp2k.classes._interaction_potential8 import _interaction_potential8
from xcp2k.classes._load_balance6 import _load_balance6
from xcp2k.classes._memory7 import _memory7


class _hf6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info6()
        self.PERIODIC = _periodic8()
        self.SCREENING = _screening7()
        self.INTERACTION_POTENTIAL = _interaction_potential8()
        self.LOAD_BALANCE = _load_balance6()
        self.MEMORY = _memory7()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY'}

