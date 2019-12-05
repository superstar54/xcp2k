from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info8 import _hf_info8
from xcp2k.classes._periodic11 import _periodic11
from xcp2k.classes._screening9 import _screening9
from xcp2k.classes._interaction_potential11 import _interaction_potential11
from xcp2k.classes._load_balance8 import _load_balance8
from xcp2k.classes._memory9 import _memory9


class _hf8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info8()
        self.PERIODIC = _periodic11()
        self.SCREENING = _screening9()
        self.INTERACTION_POTENTIAL = _interaction_potential11()
        self.LOAD_BALANCE = _load_balance8()
        self.MEMORY = _memory9()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY'}

