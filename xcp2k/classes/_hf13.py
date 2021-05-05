from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info13 import _hf_info13
from xcp2k.classes._periodic20 import _periodic20
from xcp2k.classes._screening14 import _screening14
from xcp2k.classes._interaction_potential19 import _interaction_potential19
from xcp2k.classes._load_balance13 import _load_balance13
from xcp2k.classes._memory14 import _memory14
from xcp2k.classes._ri19 import _ri19


class _hf13(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info13()
        self.PERIODIC = _periodic20()
        self.SCREENING = _screening14()
        self.INTERACTION_POTENTIAL = _interaction_potential19()
        self.LOAD_BALANCE = _load_balance13()
        self.MEMORY = _memory14()
        self.RI = _ri19()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

