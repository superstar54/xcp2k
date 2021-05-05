from xcp2k.inputsection import InputSection
from xcp2k.classes._hf_info4 import _hf_info4
from xcp2k.classes._periodic5 import _periodic5
from xcp2k.classes._screening4 import _screening4
from xcp2k.classes._interaction_potential5 import _interaction_potential5
from xcp2k.classes._load_balance4 import _load_balance4
from xcp2k.classes._memory4 import _memory4
from xcp2k.classes._ri5 import _ri5


class _hf4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info4()
        self.PERIODIC = _periodic5()
        self.SCREENING = _screening4()
        self.INTERACTION_POTENTIAL = _interaction_potential5()
        self.LOAD_BALANCE = _load_balance4()
        self.MEMORY = _memory4()
        self.RI = _ri5()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

