from xcp2k.inputsection import InputSection
from _eri_mme_info2 import _eri_mme_info2
from _cutoff_calib2 import _cutoff_calib2


class _eri_mme2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_minimax = None
        self.Cutoff = None
        self.Do_calibrate_cutoff = None
        self.Do_calibrate_gr_switch = None
        self.Print_calib = None
        self.ERI_MME_INFO = _eri_mme_info2()
        self.CUTOFF_CALIB = _cutoff_calib2()
        self._name = "ERI_MME"
        self._keywords = {'Cutoff': 'CUTOFF', 'N_minimax': 'N_MINIMAX', 'Do_calibrate_cutoff': 'DO_CALIBRATE_CUTOFF', 'Do_calibrate_gr_switch': 'DO_CALIBRATE_GR_SWITCH', 'Print_calib': 'PRINT_CALIB'}
        self._subsections = {'CUTOFF_CALIB': 'CUTOFF_CALIB', 'ERI_MME_INFO': 'ERI_MME_INFO'}

