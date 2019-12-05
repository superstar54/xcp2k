from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info3 import _hf_info3
from xcp2k.classes._periodic4 import _periodic4
from xcp2k.classes._screening3 import _screening3
from xcp2k.classes._interaction_potential4 import _interaction_potential4
from xcp2k.classes._load_balance3 import _load_balance3
from xcp2k.classes._memory3 import _memory3


class _hf3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info3()
        self.PERIODIC = _periodic4()
        self.SCREENING = _screening3()
        self.INTERACTION_POTENTIAL = _interaction_potential4()
        self.LOAD_BALANCE = _load_balance3()
        self.MEMORY = _memory3()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY'}

