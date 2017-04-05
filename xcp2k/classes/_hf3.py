from xcp2k.inputsection import InputSection
from _hf_info3 import _hf_info3
from _periodic3 import _periodic3
from _screening4 import _screening4
from _interaction_potential4 import _interaction_potential4
from _load_balance3 import _load_balance3
from _memory4 import _memory4


class _hf3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info3()
        self.PERIODIC = _periodic3()
        self.SCREENING = _screening4()
        self.INTERACTION_POTENTIAL = _interaction_potential4()
        self.LOAD_BALANCE = _load_balance3()
        self.MEMORY = _memory4()
        self._name = "HF"
        self._keywords = {'Pw_hfx': 'PW_HFX', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Fraction': 'FRACTION', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'MEMORY': 'MEMORY', 'LOAD_BALANCE': 'LOAD_BALANCE', 'HF_INFO': 'HF_INFO'}

