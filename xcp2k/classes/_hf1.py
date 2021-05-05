from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info1 import _hf_info1
from xcp2k.classes._periodic1 import _periodic1
from xcp2k.classes._screening1 import _screening1
from xcp2k.classes._interaction_potential1 import _interaction_potential1
from xcp2k.classes._load_balance1 import _load_balance1
from xcp2k.classes._memory1 import _memory1
from xcp2k.classes._ri1 import _ri1


class _hf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info1()
        self.PERIODIC = _periodic1()
        self.SCREENING = _screening1()
        self.INTERACTION_POTENTIAL = _interaction_potential1()
        self.LOAD_BALANCE = _load_balance1()
        self.MEMORY = _memory1()
        self.RI = _ri1()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

