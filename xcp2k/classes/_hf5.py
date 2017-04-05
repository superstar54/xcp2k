from xcp2k.inputsection import InputSection
from _hf_info5 import _hf_info5
from _periodic6 import _periodic6
from _screening6 import _screening6
from _interaction_potential7 import _interaction_potential7
from _load_balance5 import _load_balance5
from _memory6 import _memory6


class _hf5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info5()
        self.PERIODIC = _periodic6()
        self.SCREENING = _screening6()
        self.INTERACTION_POTENTIAL = _interaction_potential7()
        self.LOAD_BALANCE = _load_balance5()
        self.MEMORY = _memory6()
        self._name = "HF"
        self._keywords = {'Pw_hfx': 'PW_HFX', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Fraction': 'FRACTION', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'MEMORY': 'MEMORY', 'LOAD_BALANCE': 'LOAD_BALANCE', 'HF_INFO': 'HF_INFO'}

