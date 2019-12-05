from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info2 import _hf_info2
from xcp2k.classes._periodic2 import _periodic2
from xcp2k.classes._screening2 import _screening2
from xcp2k.classes._interaction_potential2 import _interaction_potential2
from xcp2k.classes._load_balance2 import _load_balance2
from xcp2k.classes._memory2 import _memory2


class _hf2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info2()
        self.PERIODIC = _periodic2()
        self.SCREENING = _screening2()
        self.INTERACTION_POTENTIAL = _interaction_potential2()
        self.LOAD_BALANCE = _load_balance2()
        self.MEMORY = _memory2()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY'}

