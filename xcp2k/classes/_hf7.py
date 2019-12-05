from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info7 import _hf_info7
from xcp2k.classes._periodic10 import _periodic10
from xcp2k.classes._screening8 import _screening8
from xcp2k.classes._interaction_potential10 import _interaction_potential10
from xcp2k.classes._load_balance7 import _load_balance7
from xcp2k.classes._memory8 import _memory8


class _hf7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info7()
        self.PERIODIC = _periodic10()
        self.SCREENING = _screening8()
        self.INTERACTION_POTENTIAL = _interaction_potential10()
        self.LOAD_BALANCE = _load_balance7()
        self.MEMORY = _memory8()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY'}

