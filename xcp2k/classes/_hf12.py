from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info12 import _hf_info12
from xcp2k.classes._periodic18 import _periodic18
from xcp2k.classes._screening13 import _screening13
from xcp2k.classes._interaction_potential17 import _interaction_potential17
from xcp2k.classes._load_balance12 import _load_balance12
from xcp2k.classes._memory13 import _memory13
from xcp2k.classes._ri17 import _ri17


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
        self.RI = _ri17()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

